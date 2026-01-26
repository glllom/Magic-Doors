import os

from data_loaders import ExcelOrderLoader, get_all_models_parameters, get_bom_components
from search import *

# Get the directory where main.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_path(filename):
    return os.path.join(BASE_DIR, filename)


def load_order(order_num):
    """Main function to load an order using ExcelOrderLoader"""
    loader = ExcelOrderLoader(get_path("orders_example.xlsx"))
    return loader.load(order_num)


def calculate_panel_size(item):
    model_params = get_all_models_parameters()
    params = model_params.get(item.sku)
    if params:
        pcw = params['pcw']
        pch = params['pch']
        # Panel dimensions: order dimensions + calculation parameters
        panel_w = (item.width or 0) + pcw
        panel_h = (item.height or 0) + pch - item.undercut
        # print(f"item.undercut: {item.undercut}, panel_h: {panel_h}, pch: {pch}, pcw: {pcw}")
        item.panel_size = (panel_w, panel_h)


def divide_to_double_door(item, customizer):
    params = get_all_models_parameters().get(item.sku)
    ddc = params['ddc'] if params else 0  # double door calculation
    width, height = item.panel_size
    new_width = round((width * customizer.par1 if customizer.par1 < 1 else customizer.par1) + 0.5, 0) + 1
    second_width = width - new_width + ddc
    item.set_panel_size(new_width, height)
    item.set_second_panel_size(second_width, height)


def process_order(order_num):
    """Load order and calculate """
    current_order = load_order(order_num)
    order_summary = {}
    # Calculate panel sizes
    for item in current_order.items:
        calculate_panel_size(item)

    # Modify if there are double doors
    for item in current_order.items:
        for customizer in item.customizers:
            if customizer.tag == "double_door_mod":
                divide_to_double_door(item, customizer)

    # Create full base BOM
    for item in current_order.items:
        item.bom = get_bom_components(item.sku)

    # ToDo: modify BOM according to customizers
    for item in current_order.items:
        print(item)
    # find cover materials
    order_summary["materials"] = suit_cover_materials(current_order)

    # add filling materials
    for item in current_order.items:
        for component in item.bom:
            if component.tag == "filling_material":
                order_summary["materials"][component.sku] += (component.qty *
                                                                   (2 if item.second_panel_size else 1))
    # round to 1 decimal place and convert to dict
    order_summary["materials"] = dict(map(lambda x: (x[0], round(x[1], 1)), order_summary["materials"].items()))

    # calculate hardware
    order_summary["hardware"] = defaultdict(int)
    for item in current_order.items:
        for component in item.bom:
            if component.tag == "locks":
                order_summary["hardware"][component.sku] += component.qty
            elif component.tag == "hinges":
                order_summary["hardware"][component.sku] += (component.qty *
                                                             (2 if item.second_panel_size else 1))
            # elif component.tag == "hardware_accessories":
    # print(order_summary)
    return order_summary


if __name__ == "__main__":
    # Test data loading
    try:
        print("Processing order 1002 with panel calculations...")
        order_components = process_order(1002)

    except Exception as e:
        import traceback

        traceback.print_exc()
        print(f"Error during loading: {e}")

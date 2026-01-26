from data_loaders import get_sheet_materials
from collections import defaultdict

def get_suitable_material(component, dimensions):
    all_materials = get_sheet_materials()
    current_group = None
    for group, materials in all_materials.items():
        for material in materials:
            if material.sku == component.sku:
                current_group = group
    all_materials = all_materials[current_group]
    # rearrange sheet materials by width and height
    all_materials.sort(key=lambda item: (item.width, item.length))
    for material in all_materials:
        if material.width > dimensions[0] and material.length > dimensions[1]:
            # print(f"Suitable material for dimensions {dimensions} found: {material.sku}")
            return material.sku
    return None

def suit_cover_materials(order):
    """Search for compatible and suitable sheet materials"""
    materials = defaultdict(int)
    for item in order.items:
        for component in item.bom:
            if component.tag == "cover_material":
                suitable_sku = get_suitable_material(component, item.panel_size)
                if suitable_sku:
                    materials[suitable_sku] += component.qty
                if item.second_panel_size and item.second_panel_size != (0, 0):
                    suitable_sku = get_suitable_material(component, item.second_panel_size)
                    if suitable_sku:
                        materials[suitable_sku] += component.qty
    return materials

# def suit_filling_materials(order):
#     pass
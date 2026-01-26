class Order:
    """Order class to represent an order"""
    def __init__(self, order_num):
        self.order_num = order_num
        self.items = []

    def __repr__(self):
        return f"Order(order_num={self.order_num}, items={self.items})"

class Item:
    """Item class to represent an item in an order"""
    def __init__(self, number, sku, width=None, height=None, direction=None, opening=None, undercut=None):
        self.number = number
        self.sku = sku
        self.width = width
        self.height = height
        self.direction = direction
        self.opening = opening
        self.customizers = []
        self.panel_size = (0, 0)
        self.second_panel_size = None
        self.undercut = undercut or 0
        self.bom = []

    def __repr__(self):
        return f"Item(number={self.number}, sku='{self.sku}', width={self.width}, height={self.height}, panel_size={self.panel_size}, customizers={self.customizers})"
    def set_panel_size(self, width, height):
        self.panel_size = (width, height)
    def set_second_panel_size(self, width, height):
        self.second_panel_size = (width, height)

    def remove_bom_item(self, sku):
        self.bom[:] = [item for item in self.bom if item.sku != sku]

    def add_bom_item(self, sku, qty, tag=None):
        self.bom.append(BOMItem(sku, qty, tag))

class Customizer:
    """Modifier class to represent an additional component for an item"""
    def __init__(self, name, sku, tag=None, par1=None, par2=None, par3=None):
        self.name = name
        self.sku = sku
        self.tag = tag
        self.par1 = par1
        self.par2 = par2
        self.par3 = par3

    def __repr__(self):
        return f"Customizer(sku='{self.sku}, name='{self.name}', tag='{self.tag}', par1={self.par1}, par2={self.par2}, par3={self.par3}')"

class Material:
    """Class to represent a sheet material"""
    def __init__(self, sku, name, width, length, thickness, group):
        self.sku = sku
        self.name = name
        self.width = width
        self.length = length
        self.group = group
        self.thickness = thickness

    def __repr__(self):
        return f"Material(sku='{self.sku}', name='{self.name}', width={self.width}, length={self.length}, group='{self.group}')"

class BOMItem:
    """Class to represent an item in a Bill of Materials"""
    def __init__(self, sku, tag, qty):
        self.sku = sku
        self.tag = tag
        self.qty = qty

    def __repr__(self):
        return f"BOMItem(sku='{self.sku}', qty={self.qty}, tag='{self.tag}')"

class ComponentChanger:
    def __init__(self, sku, compatible_models, components_to_remove, components_to_add):
        self.sku = sku
        self.compatible_models = compatible_models
        self.components_to_remove = components_to_remove
        self.components_to_add = components_to_add

    def add_component_to_remove(self, components_to_remove):
        self.components_to_remove += components_to_remove

    def add_component_to_add(self, components_to_add):
        self.components_to_add += components_to_add

    def __repr__(self):
        return f"ComponentChanger(sku='{self.sku}', compatible_models={self.compatible_models}, components_to_remove={self.components_to_remove}, components_to_add={self.components_to_add})"




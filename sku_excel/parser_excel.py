from openpyxl import load_workbook
from functions import *

products = get_products_from_db("../db.sqlite3")

"""materials. temporary"""
aqua_low = [(65, 205),(75, 205),(85, 205),(95, 205),
            (65, 215),(75, 215),(85, 215),(95, 215),
            (65, 225),(75, 225),(85, 225),(95, 225)]
aqua_high = [(122,244)]
hdf4_low = [(90,215)]
hdf4_high = [(122,244)]

"""divide products aqua by height"""
products_aqua_low = []
products_aqua_high = []
for product in products:
    if "aqua" in product[3]:
        if "set" in product[3]:
            if get_height_from_sku(product[3]) <= 225:
                products_aqua_low.append(product)
            else:
                products_aqua_high.append(product)
        if "door" in product[3]:
            if get_height_from_sku(product[3]) <= 222:
                products_aqua_low.append(product)
            else:
                products_aqua_high.append(product)
versions = generate_product_versions_sku(products_aqua_low, aqua_low)
versions.extend(generate_product_versions_sku(products_aqua_high, aqua_high))
# noinspection SpellCheckingInspection
# add_product_versions_to_db("../db.sqlite3", "production_productversion", versions)
products_hdf4_low = []
products_hdf4_high = []
for product in products:
    if "hdf" in product[3]:
        if "set" in product[3]:
            if get_height_from_sku(product[3]) <= 218:
                products_hdf4_low.append(product)
            else:
                products_hdf4_high.append(product)
        if "door" in product[3]:
            if get_height_from_sku(product[3]) <= 215:
                products_hdf4_low.append(product)
            else:
                products_hdf4_high.append(product)

versions = generate_product_versions_sku(products_hdf4_low, hdf4_low)
versions.extend(generate_product_versions_sku(products_hdf4_high, hdf4_high))

# add_product_versions_to_db("../db.sqlite3", "production_productversion", versions)



wb = load_workbook('../עץ מוצר דוגמה.xlsx')
ws = wb['מהדורות']



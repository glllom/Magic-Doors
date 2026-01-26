import pandas as pd
from production.product_data import product_families, product, series, front, models

def create_families(writer):
    """
    Создает лист "product_families". 
    ID это ключ, а verbose_name это value[0].
    """
    data = []
    for file_id, value in product_families.items():
        data.append({
            'ID': file_id,
            'verbose_name': value[0]
        })
    df = pd.DataFrame(data)
    df.to_excel(writer, sheet_name='product_families', index=False)

def create_product(writer):
    """
    Создает лист "products". 
    ID это ключ, а verbose_name это value[0]. 
    value[1] это поле product_families_id.
    """
    data = []
    for file_id, value in product.items():
        data.append({
            'ID': file_id,
            'verbose_name': value[0],
            'product_families_id': value[1]
        })
    df = pd.DataFrame(data)
    df.to_excel(writer, sheet_name='products', index=False)

def create_series(writer):
    """
    Создает лист "series". 
    ID это ключ, а verbose_name это value[0].
    """
    data = []
    for file_id, value in series.items():
        data.append({
            'ID': file_id,
            'verbose_name': value[0]
        })
    df = pd.DataFrame(data)
    df.to_excel(writer, sheet_name='series', index=False)

def create_front(writer):
    """
    Создает лист "front". 
    ID это ключ, а verbose_name это value[0]. 
    value[1] это поле series_id.
    """
    data = []
    for file_id, value in front.items():
        data.append({
            'ID': file_id,
            'verbose_name': value[0],
            'series_id': value[1]
        })
    df = pd.DataFrame(data)
    df.to_excel(writer, sheet_name='front', index=False)

def create_models(writer):
    """
    Создает лист "models". 
    ID это ключ, а verbose_name это value[0]. 
    value[1] это поле product_families_id, value[2] это поле series_id.
    """
    data = []
    for file_id, value in models.items():
        data.append({
            'ID': file_id,
            'verbose_name': value[0],
            'product_families_id': value[1],
            'series_id': value[2]
        })
    df = pd.DataFrame(data)
    df.to_excel(writer, sheet_name='models', index=False)

def create_file_excel():
    """
    Создает файл excel "data.xlsx" с таблицами данных.
    Запускает поочередно отдельные функции для создания отдельных таблиц.
    """
    with pd.ExcelWriter('data.xlsx', engine='openpyxl') as writer:
        create_families(writer)
        create_product(writer)
        create_series(writer)
        create_front(writer)
        create_models(writer)
    print("Файл 'data.xlsx' успешно создан.")

if __name__ == "__main__":
    create_file_excel()

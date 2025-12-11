import os
import sys
import django
import csv

# Устанавливаем UTF-8 для вывода
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MagicDoors.settings')
django.setup()

from main.models import ProductClass, ProductFamily, Product

# Читаем CSV файл
with open('base_excel.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    next(reader)  # Пропускаем заголовок

    current_class = None
    current_family = None

    for row in reader:
        if not row or not any(row):  # Пропускаем пустые строки
            continue

        category, family, product = row[0], row[1], row[2]

        # Если есть категория - создаем ProductClass
        if category:
            current_class, created = ProductClass.objects.get_or_create(name=category)
            print(f"{'Created' if created else 'Found'} ProductClass: {category}")
            current_family = None

        # Если есть семейство - создаем ProductFamily
        if family:
            if current_class:
                current_family, created = ProductFamily.objects.get_or_create(
                    name=family,
                    product_class=current_class
                )
                print(f"  {'Created' if created else 'Found'} ProductFamily: {family}")

        # Если есть продукт - создаем Product
        if product:
            # Если нет семейства, создаем дефолтное для этого класса
            if not current_family and current_class:
                current_family, created = ProductFamily.objects.get_or_create(
                    name=f"{current_class.name} - Общее",
                    product_class=current_class
                )
                if created:
                    print(f"  Created default ProductFamily: {current_family.name}")

            product_obj, created = Product.objects.get_or_create(
                name=product,
                product_family=current_family
            )
            print(f"    {'Created' if created else 'Found'} Product: {product}")

print("\nДанные успешно импортированы!")

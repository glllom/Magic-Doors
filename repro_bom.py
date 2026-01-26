
import openpyxl
from domain.main import get_bom
from domain.classes import BOMItem

def test_get_bom():
    # Мы знаем, что в domain/BOM.xlsx есть модель 'mdl_1_aqua'
    # И у нее должны быть компоненты: 'msh_aqua1.8x75x205', 'msh_flex38', 'Pine_38'
    sku = 'mdl_1_aqua'
    try:
        bom = get_bom(sku)
        print(f"BOM for {sku}:")
        for item in bom:
            print(item)
        
        expected_skus = ['msh_aqua1.8x75x205', 'msh_flex38', 'Pine_38']
        found_skus = [item.sku for item in bom]
        
        for e_sku in expected_skus:
            if e_sku not in found_skus:
                print(f"FAILED: Missing {e_sku}")
                return False
        print("SUCCESS: All components found")
        return True
    except Exception as e:
        print(f"ERROR: {e}")
        return False

if __name__ == "__main__":
    test_get_bom()

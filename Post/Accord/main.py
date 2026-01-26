from classes import *
from file_operations import *

hinge_cemom = Hinge("cemom", "סמום" )
hinge_book102 = Hinge("book_102", "ספר" , symmetric=False)
lock_magnet = Lock("magnet", "מגנט" )
lock_alba = Lock("alba", "אלבא" )
lock_iseo60 = Lock("iseo60", "ISEO-60" )





door1 = DoorProgram("door1", "דלת_נסתרת", "AD", direction='R')

file_name = f"{door1.verbose_name}-{door1.direction}.xxl"
code = door1.get_code()


os.chdir(ROOT_FOLDER)
create_folder("דלתות נסתרות")

with open(file_name, "w") as file:
     file.write(code)
convert(file_name)

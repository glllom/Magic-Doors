ROOT_FOLDER = "C:\\Program Files\\SCM Group\\Xilog Plus\\Job\\Product"
TEMPLATES_FOLDER = f"{ROOT_FOLDER}Templates_2.0"

class Lock:
    def __init__(self, name, verbose_name):
        self.name = name
        self.verbose_name = verbose_name


    def get_code(self, pos_x, pos_y):
        return f'XS X={pos_x} Y={pos_y} Z=0 N="{TEMPLATES_FOLDER}\\LOCKS\\{self.name}"\n'

class Hinge:
    def __init__(self, name, verbose_name, symmetric=True):
        self.name = name
        self.verbose_name = verbose_name
        self.symmetric = symmetric


    def get_code(self, pos_x=0, pos_y=0):
        return f'XS X={pos_x} Y={pos_y} Z=0 N="{TEMPLATES_FOLDER}\\HINGES\\{self.name}"\n'

class Engraving:
    def __init__(self, name, verbose_name):
        self.name = name
        self.verbose_name = verbose_name

    def get_code(self):
        return f'XS X=0 Y=0 Z=0 N="{TEMPLATES_FOLDER}\\ENGRAVINGS\\{self.name}"\n'


class DoorProgram:
    def __init__(self, name, verbose_name, field, direction=None, dx=2120, dy=720, dz=61):
        self.name = name
        self.verbose_name = verbose_name
        self.direction = direction
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.field = field

    def get_header(self):
        return f"H DX={self.dx} DY={self.dy} DZ={self.dz} -{self.field} C=0 T=0 R=100 V=10 T=100 *MM /\"def.tlg\"\n"

    # def get_code(self):
    #     code = self.get_header()
    #     code +=""
    #     return code


class HiddenDoor:
    def __init__(self, name, verbose_name, direction, dx, dy, dz):
        self.name = name
        self.verbose_name = verbose_name
        self.direction = direction
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.gcode = f'H DX={dx} DY={dy} DZ={dz} -AD C=0 T=0 R=100 *MM /"def.tlg"\n'

    def get_header(self):
        return self.gcode


class DoorStandard(DoorProgram):
    def __init__(self, name, verbose_name, field, direction, dx, dy, dz, hinges: tuple, locks: tuple):
        super().__init__(name, verbose_name, field, direction, dx, dy, dz)
        self.hinges = hinges
        self.locks = locks

    

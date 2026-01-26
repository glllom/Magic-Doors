import subprocess
import os, re

JOB = "C:\\Program Files\\SCM Group\\Xilog Plus\\Job\\"
ENGRAVING = "C:\\Program Files\\SCM Group\\Xilog Plus\\Job\\Templates\\Engraving\\"
ENGRAVING_ITALIAN = "C:\\Program Files\\SCM Group\\Xilog Plus\\Job\\Templates\\EngravingItalian\\"
LOCKS = "C:\\Program Files\\SCM Group\\Xilog Plus\\Job\\Templates\\Locks\\"
HINGES = "C:\\Program Files\\SCM Group\\Xilog Plus\\Job\\Templates\\Hinges\\"


def convert(filename):
    subprocess.run([r"C:\Program Files\SCM Group\Xilog Plus\Bin\Winxiso.exe", filename, '-s',
                    r"-fC:\Users\glebo\PycharmProjects\MagicDoors\Post\Accord\generated.bmp"])
    os.remove(filename)


def create_folder(name):
    if not os.path.exists(name):
        os.mkdir(name)
    os.chdir(name)


def get_files_dirs(path):
    engraving_list = []
    dir_files = os.scandir(path)
    for element in dir_files:
        if os.path.isfile(element):
            with open(element, "rb") as f:
                mid_correction = re.search(r'lock correction - \d\d', str(f.read()))
                if mid_correction:
                    mid_correction = mid_correction[0][18:]
                    # print(mid_correction)
            engraving_list.append({'name': str(element.name).split('.')[0], 'mid_correction': mid_correction})
        elif element.name != "corners":
            engraving_list.extend(list(map(lambda file: (file, element.name.split('.')[0]),
                                           get_files_dirs(f"{path}{element.name.split('.')[0]}"))))
    # for elem in engraving_list:
    #     print(elem)
    return engraving_list


# get_files_dirs(ENGRAVING)
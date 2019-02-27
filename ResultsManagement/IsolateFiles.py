

import shutil


path_to_structures = 'C:/ShareSSD/scop/structures/'
new_path = 'C:/ShareSSD/scop/_send/'

with open('C:/ShareSSD/scop/auxi', 'r') as fp:

    line = fp.readline()
    while line:

        structure = str(line).strip().split()[0].split('/')[-1]

        shutil.copy(path_to_structures+structure, new_path+structure)

        line = fp.readline()

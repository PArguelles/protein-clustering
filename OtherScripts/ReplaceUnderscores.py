
import os

def replaceUnderscores():

    path_to_files = 'C:/ShareSSD/scop/tables/'

    for filename in os.listdir(path_to_files):
        os.rename(path_to_files+filename, str(path_to_files+filename).replace('-',''))

replaceUnderscores()

import os
import shutil 

def getBestScoresFromSingle():

    path_to_results = 'C:/ShareSSD/scop/clustering_results_single/'
    path_to_best = 'C:/ShareSSD/scop/best_results/'

    algorithm = 'average'
    measure = 'rmsd'
    sample = 'b.2'

    metric = 'Homogeneity'
    
    maxv = 0.0
    maxv_filename = ''

    for filename in os.listdir(path_to_results):

        if algorithm in filename and measure in filename and sample in filename:

            with open(path_to_results+filename, 'r') as fp:

                line = fp.readline()
                while line:

                    if metric in line:
                        current = str(line).strip().split()[1]
                        if float(current) > float(maxv):
                            maxv = current
                            maxv_filename = filename
                        break
                    line = fp.readline()

    print(maxv)
    print(maxv_filename)
    shutil.copy(path_to_results+maxv_filename, path_to_best+maxv_filename)

getBestScoresFromSingle()
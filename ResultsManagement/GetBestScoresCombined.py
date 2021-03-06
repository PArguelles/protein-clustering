

import os
import re
import shutil

path_to_results = 'C:/ShareSSD/scop/clustering_results_combined/'
path_to_best = 'C:/ShareSSD/scop/best_results_combined_test/'

combinations = [('rmsd','gdt_2'),('rmsd','gdt_4'),
                ('rmsd','maxsub'),('rmsd','tm'),
                ('gdt_2','gdt_4'),('gdt_2','maxsub'),
                ('gdt_2','tm'), ('gdt_4','maxsub'),
                ('gdt_4','tm'), ('maxsub','tm')]

#metric = 'Silhouette'
    
maxv = 0.0
maxv_filename = ''

#get best
for spl in ['a.1','a.3','b.2','b.3']:
    for alg in ['complete','average','kmedoids']:
        for m1, m2 in combinations:
            for filename in os.listdir(path_to_results):

                values = []

                if m1 in filename and m2 in filename and spl in filename and alg in filename:
                    
                    with open(path_to_results+filename, 'r') as fp:

                        line = fp.readline()
                        while line:
                            #if metric in line:
                            if 'Homogeneity' in line or 'Completeness' in line or 'V-measure' in line or 'AMI' in line:
                                current = str(line).strip().split()[-1]
                                if float(current) > float(maxv):
                                    maxv = current
                                    maxv_filename = filename
                                    #break
                            line = fp.readline()

            shutil.copy(path_to_results+maxv_filename, path_to_best+maxv_filename)
            maxv = 0.0
            maxv_filename = ''



import MatrixFunctions as mf
import numpy as np

def readDistancesMaxsub(sample, measure):
    path_to_matrix = 'C:/ShareSSD/scop/tests/sim_'+sample+'_'+measure
    path_to_values = 'C:/ShareSSD/scop/tests/values_'+sample+'_'+measure

    counter = 0
    matrix = []
    row = []

    with open(path_to_matrix, 'r') as fp:

        size = 0
        domains = []

        #get structures
        line = fp.readline()
        while line:
            if 'PDB  :' in str(line) or 'PDB:' in str(line): 
                if '#' not in str(line):
                    size += 1
                    domain = str(line).strip().split()[-1].split('/')[-1]
                    domains.append(str(domain))
            if '# Maxsub records' in str(line):
                break
            line = fp.readline()

        while line:
            if 'MS :' in str(line): 
                if '#' not in str(line):

                    

                    parsed = str(line).strip().split()
                    current_row = parsed[2]
                    value = float(parsed[4])

                    while current_row == parsed[2]:

                        row.append(value)
                        line = fp.readline()
                        parsed = str(line).strip().split()

                        # value is the average between the two
                        value = (float(parsed[4])+float(parsed[5]))/2

                    counter += 1

                    matrix.append(row)

                    row = []    

                    #REVER ORDEM DAS OPERACOES

                    i = 0
                    while i < counter:
                        row.append(0)
                        i += 1
                    i = 0
                    row.append(value)

            line = fp.readline()

    
    row = []
    i = 0
    while i < counter:
        row.append(0)
        i += 1
    i = 0
    row.append(1.0)
    matrix.append(row)

    matrix = np.asmatrix(matrix)
    print(matrix)

    # if the diagonal is 1 symmetrization does not work properly
    # set to 0 temporarilly
    n, m = matrix.shape
    for i in range(n):
        matrix[i,i] = 0

    matrix = mf.symmetrizeMatrix(matrix)

    for i in range(n):
        matrix[i,i] = 1

    print(matrix)

    with open(path_to_values, 'w') as nf:
        for i in range(0,n):
            for j in range(0,m):
                nf.write(str(matrix[i,j])+'\n')

    matrix.dump('C:/ShareSSD/scop/tests/matrix_'+sample+'_'+measure)


readDistancesMaxsub('a.1.','tm')
readDistancesMaxsub('a.1.','maxsub')
readDistancesMaxsub('a.3.','maxsub')
readDistancesMaxsub('b.2.','maxsub')
readDistancesMaxsub('b.3.','maxsub')
readDistancesMaxsub('a.3.','tm')
readDistancesMaxsub('b.2.','tm')
readDistancesMaxsub('b.3.','tm')
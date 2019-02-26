
import MatrixFunctions as mf
import numpy as np

def readDistances(sample, measure):
    path_to_matrix = 'C:/ShareSSD/scop/data/sim_'+sample+'_'+measure
    path_to_values = 'C:/ShareSSD/scop/values_'+sample+'_'+measure

    counter = 0
    matrix = []

    with open(path_to_matrix, 'r') as fp:

        size = 0
        domains = []

        #get structures
        line = fp.readline()
        while line:
            if 'PDB  :' in str(line): 
                if '#' not in str(line):
                    size += 1
                    domain = str(line).strip().split()[-1].split('/')[-1]
                    domains.append(str(domain))
            if 'Distance records' in str(line):
                break
            line = fp.readline()

        #get distance matrix
        while line:
            if 'DIST :' in str(line): 
                if '#' not in str(line):
                    print(line)
                    parsed = str(line).strip().split()
                    current_row = parsed[2]
                    value = float(parsed[4])
            
                    while current_row == parsed[2]:
                    
                        matrix.append(value)
                        line = fp.readline()
                        parsed = str(line).strip().split()
                        value = float(parsed[4])

                    counter += 1

                    i = 0
                    while i < counter:
                        matrix.append(0)
                        i += 1
                    i = 0

                    matrix.append(value)

            line = fp.readline()

    counter += 1

    i = 0
    while i < counter:
        matrix.append(0)
        i += 1
    i = 0

    matrix = np.asmatrix(matrix)
    matrix = matrix.reshape(size,size-1)
    n, m = matrix.shape 
    X0 = np.zeros((n,1))
    matrix = np.hstack((X0,matrix))

    # np.savetxt("C:/ShareSSD/scop/data_old2/kernel_"+measure, matrix, delimiter=' ', newline='\n')

    # if 'rmsd' in path_to_matrix:
    #     matrix = matrix/(matrix.max()/1)

    # if 'gdt' in path_to_matrix:
    #     matrix = mf.processgdtmatrix(matrix)

    matrix = mf.symmetrizeMatrix(matrix)

    # save kernel values
    with open(path_to_values, 'w') as nf:
        for i in range(0,n):
            for j in range(0,m):
                nf.write(str(matrix[i,j])+'\n')


    # np.savetxt("C:/ShareSSD/scop/data_old2/matrix_"+measure, matrix, delimiter=' ', newline='\n')
    matrix.dump('C:/ShareSSD/scop/matrix_'+sample+'_'+measure)
    return domains, matrix

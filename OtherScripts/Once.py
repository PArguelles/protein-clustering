


with open('C:/ShareSSD/scop/auxi','w') as nf:
    with open('C:/ShareSSD/scop/sim_a.1._rmsd','r') as fp:

        line = fp.readline()
        while line:

            if 'PDB' in line and '#' not in line:

                structure = str(line).strip().split()[-1].split('/')[-1]
                nf.write('C:/ShareSSD/scop/structures/'+structure+'\n')

            line = fp.readline()
##   PYTHON FILE HEADER #
##
##   File:      [getControls.py]
##
##   Author(s): ['Pedro H.F Matias','Mateus R. Barbosa']
##   Site(s):   ['https://github.com/phfmatias','https://github.com/Mateus-RB']
##   Email(s):  ['phfmatias@discente.ufg.br']
##   Credits:   ['Copyright © 2022 LEEDMOL. All rights reserved.']
##   Date:      ['22.10.2022']

from sys import exit
class getinfo:
    def __init__(self):
        """
        Initializes the class with default parameters.

        Parameters
        ----------
        nx -> int
            Size of the cell in the x-direction.
        ny -> int
            Size of the cell in the y-direction.
        nz -> int
            Size of the cell in the z-direction.
        name -> str 
            Name of your system.
        method -> str
            Computational method to be used.
        base -> str
            Basis set to be used.
        mem -> str
            Memory allocation for the G16.
        cpu -> int
            Number of CPU cores to be used in G16.
        cMethod -> str
            Charge method to be used.
        nsteps -> int
            Number of steps for the convergence.
        restart -> bool
            Flag to indicate if the job is a restart.
        vsns -> bool  
            Flag to indicate if the compound is VSNS.
        radii -> list
            List to store radii values.
        """

        self.nx = 7
        self.ny = 7
        self.nz = 7
        self.name = 'test'
        self.method = 'b3lyp'
        self.base = '6-31g'
        self.mem = '2GB'
        self.cpu = 1
        self.cMethod = 'ChelpG'
        self.nsteps = 10
        self.restart = False
        self.vsns = False
        self.radii = []
        self.get_info()

    def get_info(self):

        """
        This method reads the file 'info.in' and stores the parameters in the class attributes.   
        """

        try:
            arq = open('info.in','r')
        except:
            print('Parameters file not found. Exiting...')
            exit(0)
            
        rlines = arq.readlines()
        for lines in rlines:
            if 'nx' in lines:
                self.nx = int(lines.split()[2])

            elif 'ny' in lines:
                self.ny = int(lines.split()[2])

            elif 'nz' in lines:
                self.nz = int(lines.split()[2])

            elif 'name' in lines:
                self.name = lines.split()[2]

            elif 'method' in lines:
                self.method = lines.split()[2]

            elif 'base' in lines:
                self.base = lines.split()[2]
            
            elif 'mem' in lines:
                self.mem = lines.split()[2]

            elif 'nsteps' in lines:
                self.nsteps = int(lines.split()[2])+1

            elif 'vsns' in lines:
                if lines.split()[2] == 'False':
                    self.vsns = False
                else:
                    self.vsns = True

            elif 'restart' in lines:
                if lines.split()[2] == 'False':
                    self.restart = False
                else:
                    self.restart = True

            elif 'cpu' in lines:
                self.cpu = int(lines.split()[2])
    
            elif 'cMethod' in lines:
                self.cMethod = lines.split()[2]

            elif 'radii' in lines:
                self.radii = lines.split()[2:]

if __name__ == '__main__':
    getinfo()
##   PYTHON FILE HEADER #
##
##   File:      [runqm.py]
##
##   Author(s): ['Pedro H.F Matias','Mateus R. Barbosa']
##   Site(s):   ['https://github.com/phfmatias','https://github.com/Mateus-RB']
##   Email(s):  ['phfmatias@discente.ufg.br']
##   Credits:   ['Copyright © 2022 LEEDMOL. All rights reserved.']
##   Date:      ['22.10.2022']

from os import listdir, system

class run_g16:
    def __init__(self):     
        """
        This class is responsible for running the Gaussian16 software in the current directory.
        """   
        self.runQM()
    
    def runQM(self):
        """
        This method runs the Gaussian16 software in the current directory.
        """
        for a in listdir():
            if '.gjf' in a:
                system('g16 '+a)

if __name__ == "__main__":
    run_g16().runQM()

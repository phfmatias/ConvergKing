##   PYTHON FILE HEADER #
##
##   File:      [header.py]
##
##   Author(s): ['Pedro H.F Matias','Mateus R. Barbosa]
##   Site(s):   ['https://github.com/phfmatias','https://github.com/Mateus-RB']
##   Email(s):  ['phfmatias@discente.ufg.br']
##   Credits:   ['Copyright © 2022 LEEDMOL. All rights reserved.']
##   Date:      ['22.10.2022']


import os
from MoleKing import G16LOGfile

class header:
    def __init__(self):

        """
        This class is responsible for creating the header of the output file.
        """

        self.headerfile = open('convKing.out','w')

        headertxt='''                                                                                                                                                                                                        
                                                                                                                                                                                                        
     &&&&                     &&&&&&&&&&&/            &&&&&&&&&&%&          &&&&&&&&&&&&&&&&&&&&&&&    &&&&&                         &&&&      &&&&&&&&&&&&&&&&&&&&&&&&&&&&    /&&&                     
     &&&&                   &&&&&                   &&&&&                   &&&&                /&&&&  &&&&&&&                     &&&&&&.  &&&&&&                      &&&&&& /&&&                     
     &&&&                   &&&&                    &&&&                    &&&&                  &&&& &&&&&&&&&                 &&&&/&&&. &&&&&&                        &&&&& /&&&                     
     &&&&                   &&&&                    &&&&                    &&&&                  &&&& &&&&  &&&&&             &%&&*  &&&. &&&&&&                        &&&&& /&&&                     
     &&&&                   &&&&&&&&&&&&&&&&&&&&&&& &&&&&&&&&&&&%&&&&&&&&&& &&&&                  &&&& &&&&    &&&&&         &&&%.    &&&. &&&&&&                        &&&&& /&&&                     
     &&&&                   &&&&                    &&&&                    &&&&                  &&&& &&&&      &&&&&     &&&&(      &&&. (&&&&&                        &&&&& /&&&                     
     &&&&                   &&&&                    &&&&                    &&&&                 #&&&& &&&&        &&&&& &&&&,        &&&.   &&&%&&&&&&&&&&&&&&&%&&&&&&&&&&&,   %&&&                    
      &&&&&&&&&&&&&&&&&&&&&& &&&&&&&&&&&&&&&&&&&&&&  %&&&&&&&&&&&&&&&&&&&&& &&&&&&&&&&&&&&&&&&&&&&&&   &&&&          &&&&&&,          &&&.                 &&&.                  &&&&&&&&&&&&&&&&&&&&&( 
                                                                                                                                                        &&&&&&&&&                                       
#########################################################################################################################################################################################################

                                                Script for Crystal Convergence of Dipole Moment by: Pedro HF and Mateus RB
                                                
#########################################################################################################################################################################################################
                                                                                                                                                                                         
'''
        self.headerfile.write(headertxt)

    def getDipole(self, cMethod):

        """
        This function is responsible for extracting the dipole moment from the log file.

        Returns
        -------
        dipole -> float
            Dipole moment value in Debye.

        Description
        ----------- 
        This function will search for the log file in the current directory and extract the dipole moment using the G16LOGfile class from MoleKing.
        """
        if cMethod == 'aim':
            log= [x for x in os.listdir() if '.log' in x][0]
            x = open(log,'r')
            rlines = x.readlines()
            tot = []
            for i in range(len(rlines)):
                if 'Tot=' in rlines[i] and 'NPt' not in rlines[i]:
                    tot.append(rlines[i])
            dipole = float(tot[-1].split()[7])

        else:
            log = [x for x in os.listdir() if '.log' in x][0]
            dipole = G16LOGfile(log).getDipole()

        return dipole


if __name__ == "__main__":
    run = header()

    
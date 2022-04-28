from os import listdir, system

class run_g16:

    def __init__(self):        
        self.runQM()
    
    def runQM(self):
        for a in listdir():
            if '.gjf' in a:
                system('g16 '+a)

class run_mwfn:
    def __init__(self,cMethod):       
        self.cMethod = cMethod
        self.runMFWN()

    def runMFWN(self):
        for a in listdir():
            if '.wfn' in a:
                if self.cMethod.lower() == 'aim':
                    system('''Multiwfn {0} > {1} << !
17
1
1
2
7
1
1
-10
q'''.format(a,a.replace('.wfn', '_results.txt')))


if __name__ == "__main__":
    run = run_g16()

from os import listdir, system, popen

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
        self.doMFWN()
        #self.runMFWN()

    def doMFWN(self):
        for a in listdir():
            if '.wfn' in a:
                if self.cMethod.lower() == 'aim':
                    runs = [0]
                    runs[0] = popen('echo -e "17\n1\n1\n2\n7\n1\n1\n\n-10\nq" | Multiwfn {} > {}'.format(a,a.replace('.wfn','_results.txt')))
                    runs[0].read()
                    #tmp = open('temp.sh','w')
                    #tmp.write('''Multiwfn {0} > {1} << !
#17
#1
#1
#2
#7
#1
#1
#-10
#q
#!'''.format(a,a.replace('.wfn', '_results.txt')))
#                    tmp.close()
    #def runMFWN(self):
    #    system('bash temp.sh')

if __name__ == "__main__":
    run = run_mwfn('aim')

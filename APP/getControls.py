from sys import exit

class getinfo:
    def __init__(self):
        self.ncela = 4
        self.nx = 7
        self.ny = 7
        self.nz = 7
        self.name = 'test'
        self.metodo = 'b3lyp'
        self.base = '6-31g'
        self.mem = '2GB'
        self.cpu = 1
        self.sheril = True
        self.cMethod = 'ChelpG'
        self.nsteps = 10
        self.restart = False
        self.radii = []
        self.get_info()

    def get_info(self):
        try:
            arq = open('info.in','r')
        except:
            print('Arquivo de Parametrôs não encontrado...')
            exit(0)
            
        rlines = arq.readlines()
        for lines in rlines:
            if 'nx' in lines:
                self.nx = int(lines.split()[2])

            elif 'ny' in lines:
                self.ny = int(lines.split()[2])

            elif 'nz' in lines:
                self.nz = int(lines.split()[2])

            #elif 'ncela' in lines:
            #    self.ncela = int(lines.split()[2])

            elif 'name' in lines:
                self.name = lines.split()[2]

            elif 'metodo' in lines:
                self.metodo = lines.split()[2]

            elif 'base' in lines:
                self.base = lines.split()[2]
            
            elif 'mem' in lines:
                self.mem = lines.split()[2]

            elif 'nsteps' in lines:
                self.nsteps = int(lines.split()[2])+1

            elif 'restart' in lines:
                if lines.split()[2] == 'False':
                    self.restart = False
                else:
                    self.restart = True

            elif 'cpu' in lines:
                self.cpu = int(lines.split()[2])
        
            elif 'sheril' in lines:
                self.sheril = lines.split()[2] == 'True'

            elif 'cMethod' in lines:
                self.cMethod = lines.split()[2]

            elif 'radii' in lines:
                self.radii = lines.split()[2:]

            #print(self.nx,self.ny,self.nz,self.ncela,self.name,self.metodo,self.base,self.mem,self.cpu,self.sheril,self.cMethod,self.radii) #Debug Reasons

if __name__ == '__main__':
    getinfo()
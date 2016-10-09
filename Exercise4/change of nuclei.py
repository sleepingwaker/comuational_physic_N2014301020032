import pylab as pl


class nucleichange:
    ###the class to realize the process of A and B's mutual transformation
    def __init__(self, sum_of_nuclei = 100, number_of_a = 0, time_constant = 1, time_of_duration = 5, time_step = 0.05):
        ###the unit of time is second
        sum_of_nuclei = int(input('please input the num A+B\n'))
        number_of_a = int(input('please input the num A\n'))
        time_constant = int(input('please input the time constant\n'))
        time_of_duration = int(input('please input the time of duration\n'))
        time_step = float(input('please input the time_step\n'))
        
        number_of_b = sum_of_nuclei - number_of_a
        self.n_a = [number_of_a]
        self.n_b = [number_of_b]
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        print("print the totality of nuclei ->", sum_of_nuclei)
        print("print the totality of nuclei A->", number_of_a)
        print("print the totality of nuclei B->", number_of_b)
        print("Time constant ->", time_constant)
        print("time step -> ", time_step)
        print("total time -> ", time_of_duration)
    def calculate(self):
        for i in range(self.nsteps):
            tmp1 = self.n_a[i] + (self.n_b[i] / self.tau - self.n_a[i] / self.tau) * self.dt
            tmp2 = self.n_b[i] + (self.n_a[i] / self.tau - self.n_b[i] / self.tau) * self.dt
            self.n_a.append(tmp1)
            self.n_b.append(tmp2)
            self.t.append(self.t[i] + self.dt)
    def show_results(self):
        plot1, = pl.plot(self.t, self.n_a, 'r')
        plot2, = pl.plot(self.t, self.n_b, '--')
        pl.title('nuclei mutual transformation')
        pl.xlabel('time ($s$)')
        pl.ylabel('num of nuclei')
        pl.legend([plot1, plot2], ['num of A', 'num of B'], loc='best')
        pl.show()
    def store_results(self):
        myfile = open('nuclei_decay_data.txt', 'w')
        for i in range(len(self.t)):
            print(self.t[i], self.n_a[i], self.n_b[i], file = myfile)
        myfile.close()     

a = nucleichange()
a.calculate()
a.show_results()
a.store_results()       
            
        
        

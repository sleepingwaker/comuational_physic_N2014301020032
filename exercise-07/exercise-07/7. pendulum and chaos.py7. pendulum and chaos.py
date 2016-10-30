/import pylab as pl
import math


class pendulun():
    ###the class to caculate the motivation of pendulum and chaos
    def __init__(self, init_angle_rad = 0.2, init_omiga = 0, time_of_duration = 100, time_step = 0.04, \
    f_d = 0.5, ohm_d = 2/3, g = 9.8, l = 9.8, q = 0.5):
        
        self.rad = 180 / math.pi
        
        self.thita1 = [init_angle_rad]
        self.omiga1 = [init_omiga]
        self.thita2 = [init_angle_rad]
        self.omiga2 = [init_omiga]
        self.delta_thita = [0]
        self.t = [0]
        
        self.dthitamax = []
        self.dtmax = []
        self.T =[]
        self.F =[]
        
        self.g = g
        self.l = l
        self.q1 = q
        self.q2 = q + 0.1
        self.fd = f_d
        self.ohmd = ohm_d
        
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps= int(time_of_duration//time_step+1)
        
        
    def move(self):
        for i in range(self.nsteps):
            tmp_omiga1 = - ( self.g / self.l) * math.sin(self.thita1[i] * self.rad) + self.q1 * self.omiga1[i] +\
            self.fd * math.sin(self.ohmd * self.t[i] * self.rad)
            
            tmp_thita1 = tmp_omiga1 * self.dt
            
            tmp_omiga2 = - ( self.g / self.l) * math.sin(self.thita2[i] * self.rad) + self.q2 * self.omiga2[i] +\
            self.fd * math.sin(self.ohmd * self.t[i] * self.rad)
            
            tmp_thita2 = tmp_omiga2 * self.dt
            
            
            self.omiga1.append(tmp_omiga1)
            self.thita1.append(tmp_thita1)
            self.omiga2.append(tmp_omiga2)
            self.thita2.append(tmp_thita2)
            self.t.append(self.t[i] + self.dt)
            self.delta_thita.append(abs(self.thita2[i+1] - self.thita1[i+1]))
            
            for i in range(len(self.delta_thita)):
                if i >1:
                    self.F.append(math.log10(self.delta_thita[i]))
                    self.T.append(self.t[i])
            for i in range(len(self.F)):
                if i > 1 and i < len(self.F)-1:
                    if self.F[i+1] < self.F[i] and self.F[i] >= self.F[i-1]:
                        self.dthitamax.append(self.F[i])
                        self.dtmax.append(self.T[i])
            
            del self.dthitamax[0:2]
            del self.dtmax[0:2]
            
    def draw(self):
        pl.plot(self.t, self.thita)
        pl.plot(self.dtmax, self.dthitamax,'--')
        pl.title('move of pendulum')
        pl.xlabel('time($s$)')
        pl.ylabel('log10(dertaxita) ($e-10$)')
        pl.show
        
        
a = pendulun()
a.move()
a.draw()
            
            
        

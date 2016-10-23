
import math


class cannonshell:
    ###the class to analysis the trajectory of the cannonshell whether the different air had been considered
    def __init__(self,position_of_x = 0, position_of_y = 0, time_of_duration = 100, time_step = 0.05, \
          mass_of_shell = 1, sea_level_temperture = 298, air_drag_force = 0.01):
        ###the unit of time is second, unit of angle is degree
        
        self.m = mass_of_shell
        self.b2 = air_drag_force
        self.t0 = sea_level_temperture
        self.r_x = [position_of_x]
        self.r_y = [position_of_y]
        self.t = [0]
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)

    def calculate(self, speed_initial = 100, angle_initial = 45,  hight_of_goal = 0):
        ###have air drag and effect of air desity
        
        self.hight = hight_of_goal
        angle_rad = math.pi * angle_initial / 180
        speed_of_x = speed_initial * math.cos(angle_rad)
        speed_of_y = speed_initial * math.sin(angle_rad)
        ###calculate the componet of v
        self.v_x = [speed_of_x]
        self.v_y = [speed_of_y]
        
        
        alpha = 2.5
        a = 0.0065
        
        ###this is the constant about the attitude 
        
        for i in range(self.nsteps):
            tmpv = (self.v_x[i] ** 2 + self.v_y[i] ** 2) ** 0.5
            k = (1 - a * self.r_y[i] / self.t0 ) ** alpha###k is the rate
            tmpvx = self.v_x[i] + (- k * (self.b2 / self.m) * tmpv * self.v_x[i]) * self.dt
            tmpvy = self.v_y[i] + (-10 - k * (self.b2 / self.m) * tmpv * self.v_y[i]) * self.dt
            tmprx = self.r_x[i] + (tmpvx) * self.dt
            tmpry = self.r_y[i] + (tmpvy) * self.dt
            if (self.v_y[i] > 0) or (tmpry > self.hight):
                self.v_x.append(tmpvx)
                self.v_y.append(tmpvy)
                self.r_x.append(tmprx)
                self.r_y.append(tmpry)
                self.t.append(self.t[i] + self.dt)
            else:
                t_over = - (self.r_y[i] - self.hight)/ self.v_y[i]
                if t_over > 0 or t_over == 0:
                    self.v_x.append(self.v_x[i])
                    self.v_y.append(self.v_y[i])
                    self.r_x.append(self.r_x[i] + self.v_x[i] * t_over)
                    self.r_y.append(0)
                    self.t.append(self.t[i] + t_over)
                    print('self.r_x[i]=',self.r_x[i],'hight=',self.hight,'speed=',speed_initial)
                    return self.r_x[i]
                    del self.r_x[1:]
                    del self.r_y[1:]
                    del self.v_x[1:]
                    del self.v_y[1:]
                    del self.t
                    break
                else:
                    return 0
                    break
                
    

        
        
'''
-----------------------------
        this is the main
-----------------------------       
'''        

b_x=float(input('the position x of target:\n'))
b_y=float(input('the position y of target:\n'))
s = []
s[1,1] = cannonshell()
v_min = []
for m in range(1,89):
    for n in range(1,10000):
        s[m,n]=cannonshell()
        x = s[m.n].calculate(n,m,b_y)
        if x > b_x:
            v_min.append(n)
            break
    if v_min[m+1]>v_min[m]:
        print('theta=',n,'v_min=',v_min[-1])
        break
    
    

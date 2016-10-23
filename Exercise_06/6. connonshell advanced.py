import pylab as pl
import math


class cannonshell:
    ###the class to analysis the trajectory of the cannonshell whether the different air had been considered
    def __init__(self, speed_initial = 100, angle_initial = 45, position_of_x = 0, position_of_y = 0, time_of_duration = 100, time_step = 0.05, \
          mass_of_shell = 1, hight_of_goal = 0, sea_level_temperture = 298, air_drag_force = 0.01):
        ###the unit of time is second, unit of angle is degree
        
        choose1 = int(input('if you want to change the initial date, input 0, if not, please input 1：\n'))
        if choose1 == 0:
            speed_initial = float(input('please input the inital compositon of speed (m/s)：\n'))
            angle_initial = float(input('please input the inital angle of speed (degree 0~90)：\n'))
            mass_of_shell = float(input('please input the mass of shell (kg)：\n'))
            hight_of_goal = float(input('please input the hight of goal (m)：\n'))
            sea_level_temperture = float(input('please input the constant number of air drag force(kg/m)\n'))
            air_drag_force = float(input('please input the sea level temperture(K)\n'))
        else:
            print('speed initial = 100m/s, angle_initial = 45, position_of_x = 0m, position_of_y = 0m, mass_of_shell = 1kg, hight_of_goal = 0m,\
            sea_level_temperture = 298K, air_drag_force = 0.01kg/m')
        ###help to set the date you want
        
        angle_rad = math.pi * angle_initial / 180
        speed_of_x = speed_initial * math.cos(angle_rad)
        speed_of_y = speed_initial * math.sin(angle_rad)
        ###calculate the componet of v
        
        self.m = mass_of_shell
        self.hight = hight_of_goal
        self.b2 = air_drag_force
        self.t0 = sea_level_temperture
        self.v_x = [speed_of_x]
        self.v_y = [speed_of_y]
        self.r_x = [position_of_x]
        self.r_y = [position_of_y]
        self.t = [0]
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)

    def calculate(self):
        ###have air drag and effect of air desity
        
        alpha = 2.5
        a = 0.0065
        print("the constant number a is", a, "K/m", "the exponent alpha is", alpha )
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
                    print('horizontal axis of the point of fall is', self.r_x[-1], 'm')
                    break
                else:
                    print('cannot reach this hight')
                    break
                
    
    def show_results(self):
        pl.plot(self.r_x, self.r_y)
        pl.title('the trajectory of cannon shell')
        pl.xlabel('x/m')
        pl.ylabel('y/m')
        pl.show()
        
        
        
        
        
'''
-----------------------------
        this is the main
-----------------------------       
'''        
shell1 = cannonshell()
shell1.calculate()
shell1.show_results()
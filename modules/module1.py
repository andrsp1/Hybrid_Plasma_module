import module2 as md2
import matplotlib.pyplot as plt
import os
plt.rcParams.update({'font.size': 20})

class Hybrid_Plasma: #Hybrid plasma class
    pass
    def __init__(self, N, delta):
        self.N = N #number of particles in the beam
        self.delta = delta #time-step
    def run_program(self):
        #This function runs the first test for N particles with time step dt
        (t, v) = md2.sherlock_func(self.N, self.delta)
        #The solution is saved in a CSV file
        file = open("speed_solution_{}.csv".format('data'), "w")
        for i in range(len(v)):
            file.write("{} {}".format(t[i],v[i]) + os.linesep)
        file.close()
        return (t, v)
    def run_programT(self):
        # This function runs the first test for N particles with time step dt
        (t, Temp) = md2.sherlock_funcT(self.N, self.delta)
        # The solution is saved in a CSV file
        file = open("temperature_solution_{}.csv".format('data'), "w")
        for i in range(len(Temp)):
            file.write("{} {}".format(t[i], Temp[i]) + os.linesep)
        file.close()
        return (t, Temp)
    def plot_results(self):
        (t, v) = self.run_program()
        plt.semilogy(t, v, color = 'black', linestyle = '-', label = "$N = 100$", linewidth = 0.5)
        plt.title("$\Delta t = 0.01\\tau_{ch}$")
        plt.xlabel('t/$\\tau_{ch}$')
        plt.ylabel('$v/v_0$')
        plt.legend()
        plt.legend()
        plt.show()
    def plot_resultsT(self):
        (t, T) = self.run_programT()
        plt.plot(t, T, color = 'red', linestyle = '-', label = "$\\Delta t = 0.01$", linewidth = 1)
        plt.plot([0.0,8.0],[0.1,0.1], color = 'black', linestyle = '-.', label = "Fluid", linewidth = 1)
        plt.title("$T_i(t=0) = 10T_e$ ")
        plt.xlabel('$t/\\tau_\epsilon$')
        plt.ylabel('$T_i(t)/T_i(t=0)$')
        plt.legend()
        plt.show()
    def __del__(self):
        pass

#We create an object "Plasma" to run the first test
plasma = Hybrid_Plasma(100, 0.01)
plasma.plot_results()
#We create an second object "PlasmaT" to run the second test
#uncomment the following two lines to plot the temperature equilibration plot and comment the first test.
#plasmaT = Hybrid_Plasma(1000, 0.01)
#plasmaT.plot_resultsT()

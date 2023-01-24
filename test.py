import matplotlib.pyplot as plt
import scipy
import numpy as np
A = -0.004
B = 1
C = 0.048
kp = 0.607338773069937
ki = 0.00245637321622817
kd = 0

def model(t, x, yd):
    e = yd - x[0]                         #feedback
    e_int = x[1]
    u = kp * e + ki * e_int
    if u > 1:
        u = 1
    if u < 0:
        u = 0
    dx = A *x[0] + B*u
    return dx, e_int

def create_plot(t, x, title, xlabel="", ylabel="", x2 = np.array([]), legend = [""]):
    plt.figure()
    plt.plot(t, x)
    if x2.any() != 0:
        plt.plot(t, x2)
    plt.legend(legend)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    plt.show()

t_start = 0; t_stop = 700;
t = [t_start, t_stop]
samples = 1000
t_lin = np.linspace(t_start, t_stop, samples)
init_cond = [0, 0]
u = 30 * 1/C
sol = scipy.integrate.solve_ivp(model, t, init_cond, t_eval= t_lin, args=(u,))
t = np.array(sol.t).T
y = np.array(sol.y).T
create_plot(t, (C*y[:,0])+25, 'cos')





# H = k/(1+s*T)*exp(-s*delay); %model
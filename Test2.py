from matplotlib.pyplot import close,figure, plot, axis, grid, xlabel, ylabel, legend, savefig, subplot, show
from scipy.integrate import ode
from numpy import *

def myeuler(f,tspan,y0,N,params):
    h = float(tspan[1]-tspan[0])/N # time step
    t = tspan[0]; y = y0
    tout = zeros((N+1,1)); yout = zeros((N+1,2)) # reserve space for output
    tout[0] = t; yout[0] = y # set initial t and y
    for n in range(1,N+1): # n=1..N
        f1 = f(t,y,params) # y' @ current t
        t += h # update t
        y += h*f1 # update y
        tout[n] = t; yout[n] = y
    return tout,yout

def odesolve(f,tspan,y0,N,params):
    r = ode(f)
    r.set_integrator('vode',rtol=1e-6) # pick method, relative accuracy
    h = float(tspan[1]-tspan[0])/N # time step
    t = zeros((N+1,1)); y = zeros((N+1,2)) # initialize output
    n = 0
    r.set_initial_value(y=y0,t=tspan[0]) # initial condition
    r.set_f_params(params) # parameters
    t[0] = r.t; y[0] = r.y;
    while r.successful() and n < N:
        r.integrate(r.t+h) # integrate ODE r from t to t+h
        n += 1; t[n] = r.t; y[n] = r.y; # record new values
    return t,y

def f(t,y,params):
    s,i = y # retrieve s and i from 2x1 vector y
    mu,beta,gamma,alpha = params # retrieve parameters from params list
    dsdt = mu*10-beta*10*60
    didt = gamma*10*60-alpha*60
    return array([dsdt,didt])

tspan = [0,20] # initial and final times
y0 = s0,i0 = [10,60] # initial values
params = mu,beta,gamma,alpha = [.8,.01,.6,.1] # parameters
N = 20 # "exact" solution plotted using sufficiently many points
t,y = odesolve(f,tspan,y0,N,params)
t = t[:,0]; s = y[:,0]; i = y[:,1]; # extract variables
N = 25 # Euler solution with step size (tspan[1]-tspan[0])/N=2
t1,y1 = myeuler(f,tspan,y0,N,params)
t1 = t1[:,0]; s1 = y1[:,0]; i1 = y1[:,1]; # extract variables
close() # if figure already open
figure(1) # open figure
subplot(2,1,1) # partitions figure as 2x1 and select first (top)
plot(t,s,'b-',t1,s1,'bo',t,i,'r-',t1,i1,'ro',linewidth=2,markersize=5)
legend([r'$s(t)$','Euler',r'$i(t)$','Euler'])
grid('on')
subplot(2,1,2) # partitions figure as 2x1 and select second (bottom)
plot(s,i,'k-',s1,i1,'ro',linewidth=2,markersize=5) # phase plot i vs s
legend(['exact','Euler'],loc='best')
xlabel(r'$s$')
ylabel(r'$i$')
grid('on')
savefig('s_and_i.jpg')
show()
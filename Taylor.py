from matplotlib.pyplot import close,figure, plot, axis, grid, xlabel, ylabel, legend, savefig
from scipy.integrate import ode

def myeuler(f,tspan,y0,N,params):
    h = float(tspan[1]-tspan[0])/N # time step
    t = tspan[0]; y = y0
    tout = [0]*(N+1); yout = [0]*(N+1) # reserve space for output
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
    t = [0]*(N+1); y = [0]*(N+1) # initialize output
    n = 0
    r.set_initial_value(y=y0,t=tspan[0]) # initial condition
    r.set_f_params(params) # parameters, duh...
    t[0] = r.t; y[0] = r.y;
    while r.successful() and n < N:
        r.integrate(r.t+h) # integrate ODE r from t to t+h
        n += 1; t[n] = r.t; y[n] = r.y; # record new values
    return t,y

f = lambda t,y,a: a*y*(1-y) # ODE rhs
close()
figure(1)
tspan = [0,10]
y0 = 0.2 # IC
a = (-1.,0.,.25,.5,1.,2.) # list of parameter values
colors = 'kbgrcm' # one color for each parameter value
N = 100 # first "exact" solution plotted using sufficiently many points
for k in range(0,6): # k=0...5
    t,y = odesolve(f,tspan,y0,N,a[k]) # uses VODE
    plot(t,y,label=r'$a = %.2f$' % a[k],linewidth=2,color=colors[k])
N = 10 # Euler with step size (tspan[1]-tspan[0])/N = 1
for k in range(0,6):
    t,y = myeuler(f,tspan,y0,N,a[k])
    plot(t,y,'.-',markersize=20,color=colors[k])
    axis(tspan+[-.2,1.2]) # [0.,10.,-.2,1.2]
grid('on')
xlabel(r'time $t$',fontsize=16)
ylabel(r'solution $y(t)$',fontsize=16)
legend(loc='lower right')
savefig('myode.eps')
show()
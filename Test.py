from matplotlib.pyplot import close, figure, plot, grid, xlabel, ylabel, legend, savefig, show
from scipy.integrate import ode

def odesolve(f,tspan,y0,N,params):
    r = ode(f)
    r.set_integrator('vode',rtol=1e-6) 
    h = float(tspan[1]-tspan[0])/N 
    t = [0]*(N+1); y = [0]*(N+1)
    n = 0
    r.set_initial_value(y=y0,t=tspan[0])
    r.set_f_params(params) 
    t[0] = r.t; y[0] = r.y;
    while r.successful() and n < N:
        r.integrate(r.t+h)
        n += 1; t[n] = r.t; y[n] = r.y;
    return t,y

f=lambda t,y,a: a*y*(1-y)
tspan=[0,10]
y0=0.2
N=100
a = 2

close()
figure(1)
#ODE Solve used to give "exact"
t1,y1 = odesolve(f,tspan,y0,N,a)
plot(t1,y1,label=r'$a = %.2f$' % a,linewidth=2, color='blue')
#Solutions provided through paper
t2=[1,2,3,4,5,6,7,8,9,10]
y2=[0.5,0.711234594228,0.967877920506,0.997363685939,0.999662877617,0.999954571513,0.999993851681,0.999999168462,0.999999168471,0.999999887465]
plot(t2,y2,'.-',markersize=20, color='blue')
grid('on')
xlabel(r'time $t$',fontsize=16)
ylabel(r'solution $y(t)$',fontsize=16)
legend(loc='lower right')
savefig('myode.jpg')
show()
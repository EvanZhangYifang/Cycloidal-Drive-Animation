import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

interval = 50 # ms, time between animation frames

fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(left=0.15, bottom=0.35)

ax.set_aspect('equal')
plt.xlim(-1.5*40,1.4*2*40)
plt.ylim(-1.5*40,1.4*40)
#plt.grid()
t = np.linspace(0, 2*np.pi, 2000)
t1 = np.linspace(90*np.pi/180.0, 270*np.pi/180.0, 2000)
t2 = np.linspace(-90*np.pi/180.0, 90*np.pi/180.0, 2000)

delta = 1

m1, = ax.plot([0], [0],'k-')
m2, = ax.plot([0], [0],'k-')
#line1, = ax.plot([], [], 'k-')
#line2, = ax.plot([], [], 'k-')
def draw_circle(e,D,d):
    r = D/2 - d/2 +e
    # draw arc1
    x1 = r*np.cos(t1)
    y1 = r*np.sin(t1)
    m1.set_data(x1,y1)

    x2 = D - d + r*np.cos(t2)
    y2 = r*np.sin(t2)
    m2.set_data(x2,y2)

    # draw line1
    #x3 = [[0,D - d ]]
    #y3 = [[r,r]]
    #line1.set_data(x3,y3)

    # draw line1
    #x4 = [[0,D - d ]]
    #y4 = [[-r,-r]]
    #line2.set_data(x4,y4)


##ehypocycloidA:
ehypocycloidA, = ax.plot([0],[0],'r-')
edot, = ax.plot([0],[0], 'ro', ms=5)
def update_ehypocycloidA(e,n,D,d, phis):
    RD=D/2
    rd=d/2
    rc = (n-1)*(RD/n)
    rm = (RD/n)
    xa = (rc+rm)*np.cos(t)-e*np.cos((rc+rm)/rm*t)
    ya = (rc+rm)*np.sin(t)-e*np.sin((rc+rm)/rm*t)

    dxa = (rc+rm)*(-np.sin(t)+(e/rm)*np.sin((rc+rm)/rm*t))
    dya = (rc+rm)*(np.cos(t)-(e/rm)*np.cos((rc+rm)/rm*t))
    
    xd = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))
    yd = (ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)

    x = xd*np.cos(-phis/(n-1) )-yd*np.sin(-phis/(n-1) )   # + np.pi/(n-1)
    y = xd*np.sin(-phis/(n-1) )+yd*np.cos(-phis/(n-1) ) 

    ehypocycloidA.set_data(x,y)
    edot.set_data(x[0], y[0])

##ehypocycloidB:
ehypocycloidB, = ax.plot([0],[0],'b-')
def update_ehypocycloidB(e,n,D,d, phis):
    RD=D/2
    rd=d/2
    rc = (n-1)*(RD/n)
    rm = (RD/n)
    xa = (rc+rm)*np.cos(t)-e*np.cos((rc+rm)/rm*t)
    ya = (rc+rm)*np.sin(t)-e*np.sin((rc+rm)/rm*t)

    dxa = (rc+rm)*(-np.sin(t)+(e/rm)*np.sin((rc+rm)/rm*t))
    dya = (rc+rm)*(np.cos(t)-(e/rm)*np.cos((rc+rm)/rm*t))
    
    xd = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))
    yd = (ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)

    if (n+1)%2 != 1:
        x = xd*np.cos(phis/(n-1) + np.pi/(n-1) )-yd*np.sin(phis/(n-1) + np.pi/(n-1) ) + D - d  # + np.pi/(n-1)
        y = xd*np.sin(phis/(n-1) + np.pi/(n-1) )+yd*np.cos(phis/(n-1) + np.pi/(n-1) ) 
    if (n+1)%2 != 0:
        x = xd*np.cos(phis/(n-1) )-yd*np.sin(phis/(n-1) ) + D - d  # + np.pi/(n-1)
        y = xd*np.sin(phis/(n-1) )+yd*np.cos(phis/(n-1) ) 
    ehypocycloidB.set_data(x,y)


axcolor = 'lightgoldenrodyellow'

ax_fm = plt.axes([0.25, 0.21, 0.5, 0.02], facecolor=axcolor)
#ax_Rm = plt.axes([0.25, 0.24, 0.5, 0.02], facecolor=axcolor)
#ax_n = plt.axes([0.25, 0.21, 0.5, 0.02], facecolor=axcolor)
ax_Rd = plt.axes([0.25, 0.18, 0.5, 0.02], facecolor=axcolor)
ax_rd = plt.axes([0.25, 0.15, 0.5, 0.02], facecolor=axcolor)
ax_e = plt.axes([0.25, 0.12, 0.5, 0.02], facecolor=axcolor)
ax_N = plt.axes([0.25, 0.09, 0.5, 0.02], facecolor=axcolor)
ax_d = plt.axes([0.25, 0.06, 0.5, 0.02], facecolor=axcolor)
ax_D = plt.axes([0.25, 0.03, 0.5, 0.02], facecolor=axcolor)

sli_fm = Slider(ax_fm, 'fm', 10, 100, valinit=50, valstep=delta)
#sli_Rm = Slider(ax_Rm, 'Rm', 1, 10, valinit=20, valstep=delta)
#sli_n = Slider(ax_n, 'n', 3, 10, valinit=6, valstep=delta)
sli_Rd = Slider(ax_Rd, 'Rd', 1, 40, valinit=20, valstep=delta)
sli_rd = Slider(ax_rd, 'rd', 0.1, 10, valinit=1.5, valstep=delta/10)
sli_e = Slider(ax_e, 'e', 0.1, 10, valinit=2, valstep=delta/10)
sli_N = Slider(ax_N, 'N', 3, 80, valinit=10, valstep=delta)
sli_d = Slider(ax_d, 'd', 2, 20, valinit=5,valstep=delta/10)
sli_D = Slider(ax_D, 'D', 5, 100, valinit=55,valstep=delta)

def update(val):
    sfm = sli_Rd.val
    #sRm = sli_Rm.val
    sRd = sli_Rd.val
    #sn = sli_n.val
    srd = sli_rd.val    
    se = sli_e.val
    sN = sli_N.val
    sd = sli_d.val
    sD = sli_D.val
    ax.set_xlim(-1.5*0.5*sD,1.4*sD)
    ax.set_ylim(-1.5*0.5*sD,1.4*0.5*sD)



sli_fm.on_changed(update)
#sli_Rm.on_changed(update)
sli_Rd.on_changed(update)
#sli_n.on_changed(update)
sli_rd.on_changed(update)
sli_e.on_changed(update)
sli_N.on_changed(update)
sli_d.on_changed(update)
sli_D.on_changed(update)

resetax = plt.axes([0.8, 0.0, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sli_fm.reset()    
    #sli_Rm.reset()
    #sli_n.reset()
    sli_rd.reset()
    sli_Rd.reset()    
    sli_e.reset()
    sli_N.reset()
    sli_d.reset()
    sli_D.reset()

button.on_clicked(reset)

def animate(frame):
    sfm = sli_fm.val
    #sRm = sli_Rm.val
    sRd = sli_Rd.val
    #sn = sli_n.val
    srd = sli_rd.val    
    se = sli_e.val
    sN = sli_N.val
    sd = sli_d.val
    sD = sli_D.val
    frame = frame+1
    phi = 2*np.pi*frame/sfm

    draw_circle(se,sD,sd)

    update_ehypocycloidA(se,sN,sD,sd, phi)
    update_ehypocycloidB(se,sN,sD,sd, phi)


    fig.canvas.draw_idle()



ani = animation.FuncAnimation(fig, animate,frames=int(sli_fm.val*(sli_N.val-1)), interval=interval)
dpi=100

plt.show()

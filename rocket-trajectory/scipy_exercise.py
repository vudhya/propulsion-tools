# ============================================
# Day 7 Exercise: SciPy — fsolve and solve_ivp
# ============================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.integrate import solve_ivp

# =============================================
# PART A: fsolve — Replacing bisection method
# =============================================

gamma = 1.4

def area_equation(M, target, gamma):
    term1 = ((2/(gamma+1)) * (1 + ((gamma-1)/2) * M**2))**((gamma+1)/(2*(gamma-1)))
    computed_A_ratio = (1/M) * term1
    return computed_A_ratio - target

M_sub = fsolve(area_equation, 0.3, args=(2.0, gamma))
M_sup = fsolve(area_equation, 2.0, args=(2.0, gamma))
print(f"Subsonic Mach number: {M_sub[0]:.4f}")
print(f"Supersonic Mach number: {M_sup[0]:.4f}")


# =============================================
# PART B: solve_ivp — Sounding Rocket Trajectory
# =============================================
# A sounding rocket launches vertically. Model its trajectory.
#
# PHYSICS:
#   The rocket has two phases:
#   1. Powered flight (0 to t_burn): thrust is ON, mass decreases
#   2. Coast phase (t_burn to impact): no thrust, only gravity + drag
#
# EQUATIONS (two coupled ODEs):
#   dh/dt = v                    (height changes with velocity)
#   dv/dt = T/m - g - D/m        (Newton's second law)
#
# Where:
#   h = altitude (m)
#   v = velocity (m/s)
#   T = thrust (N) — only during powered flight
#   m = mass (kg) — decreases during burn
#   g = 9.81 m/s²
#   D = 0.5 * Cd * A * rho_air * v² (aerodynamic drag)
#
# GIVEN:
#   m_initial = 500 kg (total mass at launch)
#   m_propellant = 200 kg
#   t_burn = 40 s (burn time)
#   m_dot = m_propellant / t_burn = 5 kg/s (mass flow rate)
#   thrust = 15000 N (constant during burn)
#   Cd = 0.5 (drag coefficient)
#   A = 0.1 m² (cross-section area)
#   rho_air = 1.225 kg/m³ 
#
# STATE VECTOR:
#   y = [h, v]  → two variables being solved simultaneously
#   dydt = [v, (T - m*g - D) / m]

# GIVEN VALUES
m_initial = 500       # kg
m_propellant = 200    # kg
t_burn = 40           # s
m_dot = m_propellant / t_burn
thrust = 15000        # N
Cd = 0.5
A = 0.1               # m²
rho_air = 1.225        # kg/m³
g = 9.81

def rocket_ode(t, y):
    h = y[0]
    v = y[1]
    
    #Determine if we're in powered phase or coast phase
    if t < t_burn:
        T = thrust
        m = m_initial - m_dot * t
    else:
        T = 0
        m = m_initial - m_propellant
        
    #Drag
    D = 0.5 * Cd * A * rho_air * v * abs(v)
    
    #Accelerations
    dhdt = v
    dvdt = (T - m*g - D) / m
    return [dhdt, dvdt]


# Step 2: Solve the ODE
solution = solve_ivp(rocket_ode, [0, 200], [0, 0], t_eval = np.linspace(0, 200, 1000))
t = solution.t
h = solution.y[0]
v = solution.y[1]

# Step 3: Plot altitude and velocity vs time (2 subplots)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
ax1.plot(t, h)
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Altitude (m)')
ax1.set_title('Rocket Trajectory: Altitude vs Time')
ax1.axvline(x=t_burn, color='r', linestyle='--', label='Burnout')
ax1.legend()
ax1.grid()
ax2.plot(t, v)
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Velocity (m/s)')
ax2.set_title('Rocket Trajectory: Velocity vs Time')
ax2.axvline(x=t_burn, color='r', linestyle='--', label='Burnout')
ax2.legend()
ax2.grid()
plt.tight_layout()
plt.savefig('rocket_trajectory.png', dpi=200)
plt.show()

# Step 4: Find and print key results
max_altitude = np.max(h)
time_of_apogee = t[np.argmax(h)]
max_velocity = np.max(v)
time_of_max_velocity = t[np.argmax(v)]
velocity_at_burnout = v[np.argmin(np.abs(t - t_burn))]
print(f"Maximum altitude (apogee): {max_altitude:.2f} m at t = {time_of_apogee:.2f} s")
print(f"Maximum velocity: {max_velocity:.2f} m/s at t = {time_of_max_velocity:.2f} s")
print(f"Velocity at burnout: {velocity_at_burnout:.2f} m/s at t = {t_burn} s")



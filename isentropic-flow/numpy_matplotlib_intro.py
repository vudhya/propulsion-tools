import numpy as np  # type: ignore[import]
import matplotlib.pyplot as plt  # type: ignore[import]

gamma = 1.4

# =============================================
# PART A: NumPy — Isentropic Table Without Loops
# =============================================
M = np.linspace(0.1, 3.0, 30)

term = 1 + (gamma-1)/2 * M**2
T_ratio = term ** (-1)
P_ratio = term ** (-gamma/(gamma-1))
rho_ratio = term ** (-1/(gamma-1))
A_ratio = (1/M) * ((2/(gamma+1)) * term) ** ((gamma+1)/(2*(gamma-1)))

for i in range(len(M)):
    print(f"{M[i]:.1f} {T_ratio[i]:.4f} {P_ratio[i]:.4f} {rho_ratio[i]:.4f} {A_ratio[i]:.4f}")
    if M[i] == 1.0:
        print("-" * 40)  # Print a separator after M=1.0
    

# =============================================
# PART B: Matplotlib — Plotting
# =============================================
plt.plot(M, T_ratio, label = 'T/T0')
plt.plot(M, P_ratio, label = 'P/P0')
plt.plot(M, rho_ratio, label = 'rho/rho0')
plt.xlabel('Mach')
plt.ylabel('Ratio')
plt.title('Isentropic Ratios vs Mach Number')
plt.legend()
plt.grid(True)
plt.savefig('isentropic_ratios.png', dpi=200)
plt.show()

plt.plot(M, A_ratio, label = 'A/A*')
plt.plot(1, 1, 'ro', markersize = 8)
plt.xlabel('Mach')
plt.ylabel('A/A*')
plt.title('Area Ratio vs Mach Number')
plt.grid(True)
plt.savefig('area_ratio.png', dpi=200)
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].plot(M, T_ratio)
axes[0, 0].set_title('T/T0')
axes[0, 0].set_xlabel('Mach')
axes[0, 0].grid(True)

axes[0, 1].plot(M, P_ratio)
axes[0, 1].set_title('P/P0')
axes[0, 1].set_xlabel('Mach')
axes[0, 1].grid(True)

axes[1, 0].plot(M, rho_ratio)
axes[1, 0].set_title('rho/rho0')
axes[1, 0].set_xlabel('Mach')
axes[1, 0].grid(True)

axes[1, 1].plot(M, A_ratio)
axes[1, 1].set_title('A/A*')
axes[1, 1].set_xlabel('Mach')
axes[1, 1].grid(True)

plt.tight_layout()
plt.savefig('isentropic_subplots.png', dpi=200)
plt.show()

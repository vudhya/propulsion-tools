
gamma = 1.4

mach_numbers = []
for i in range(1,31):
    M = i * 0.1
    mach_numbers.append(M)

T_ratios = []
P_ratios = []
rho_ratios = []
A_ratios = []
for M in mach_numbers:
    term = (1 + (gamma -1)/2 * M**2)
    T_ratio = term ** (-1)
    P_ratio = term ** (-gamma/(gamma-1))
    rho_ratio = term ** (-1/(gamma-1))
    A_ratio = (1/M) * ((2/(gamma+1)) * term) ** ((gamma+1)/(2*(gamma-1)))
    T_ratios.append(T_ratio)
    P_ratios.append(P_ratio)
    rho_ratios.append(rho_ratio)
    A_ratios.append(A_ratio)

print(f"{'M':<8} {'T/T0':<8} {'P/P0':<8} {'rho/rho0':<10} {'A/A*':<8}")
print("-" * 40)

for i in range(len(mach_numbers)):
    print(f"{mach_numbers[i]:<8.1f} {T_ratios[i]:<8.4f} {P_ratios[i]:<8.4f} {rho_ratios[i]:<10.4f} {A_ratios[i]:<8.4f}")
    if mach_numbers[i] == 1.0:
        print(f"At M=1.0: T/T0={T_ratios[i]:.4f}, P/P0={P_ratios[i]:.4f}, rho/rho0={rho_ratios[i]:.4f}")







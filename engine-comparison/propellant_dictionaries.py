
import math

# Engine 1: Raptor (SpaceX)
#   Tc = 3800, gamma = 1.15, R = 370, Pc = 300, Pe = 1
raptor = {
    "name": "Raptor",
    "fuel": "CH4",
    "oxidizer": "LOX",
    "Tc": 3800,
    "gamma": 1.15,
    "R": 370,
    "Pc": 300,
    "Pe": 1
}

# Engine 2: F-1 (Apollo Saturn V)
#   Tc = 3500, gamma = 1.2, R = 330, Pc = 70, Pe = 1
f1 = {
    "name": "F-1",
    "fuel": "RP-1",
    "oxidizer": "LOX",
    "Tc": 3500,
    "gamma": 1.2,
    "R": 330,
    "Pc": 70,
    "Pe": 1
}

# Engine 3: RS-25 (Space Shuttle / SLS)
#   Tc = 3600, gamma = 1.25, R = 460, Pc = 200, Pe = 1
rs25 = {
    "name": "RS-25",
    "fuel": "LH2",
    "oxidizer": "LOX",
    "Tc": 3600,
    "gamma": 1.25,
    "R": 460,
    "Pc": 200,
    "Pe": 1
}


def analyze_engine(engine):
    # Extract values from the dictionary
    gamma = engine["gamma"]
    R = engine["R"]
    Tc = engine["Tc"]
    Pc = engine["Pc"] * 1e5 # Convert bar to Pascal
    Pe = engine["Pe"] * 1e5 # Convert bar to Pascal
    # Calculate Ve
    Ve = math.sqrt((2*gamma/(gamma-1)) * R * Tc * (1 - (Pe/Pc)**((gamma-1)/gamma)))
    # Calculate Isp (use g0 = 9.81)
    Isp = Ve / 9.81
    
    engine["Ve"] = Ve
    engine["Isp"] = Isp


engine_list = [raptor, f1, rs25]

for engine in engine_list:
    analyze_engine(engine)
    # Print the results
    print(f"Engine: {engine['name']}")
    print(f"Propellants: {engine['fuel']} / {engine['oxidizer']}")
    print(f"Chamber Pressure: {engine['Pc']} bar")
    print(f"Calculated Isp: {engine['Isp']:.2f} s")
    print("-" * 40)
    

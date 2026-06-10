# ============================================
# Day 4 Exercise: Dictionaries
# ============================================
# Use dictionaries to organize propellant data.
# Write a function that accepts a dictionary
# and computes performance metrics.
# ============================================

import math

# --- Step 1: Create the Dictionaries ---
# Create dictionaries for three different engine configurations.
# Each dictionary should have the following keys:
#   "name" (string)
#   "fuel" (string)
#   "oxidizer" (string)
#   "Tc" (float, chamber temperature in K)
#   "gamma" (float, ratio of specific heats)
#   "R" (float, specific gas constant in J/kg·K)
#   "Pc" (float, chamber pressure in bar)
#   "Pe" (float, exit pressure in bar)

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


# --- Step 2: Write a function that takes a dictionary ---
# Write a function called `analyze_engine(engine)`
# It should take ONE argument (the dictionary) and calculate
# the ideal exhaust velocity (Ve) and specific impulse (Isp).
# (You already wrote the math for this in Day 1!)
#
# Remember to extract the values from the dictionary inside the function:
#   gamma = engine["gamma"]
#   ...

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


# --- Step 3: Loop through a list of dictionaries ---
# We can put our dictionaries into a list.
engine_list = [raptor, f1, rs25]

# Loop through the list, pass each engine to your function,
# and print a formatted summary report for each engine.
#
# Format example:
# ----------------------------------------
# Engine: Raptor
# Propellants: CH4 / LOX
# Chamber Pressure: 300 bar
# Calculated Isp: 345.2 s
# ----------------------------------------

for engine in engine_list:
    analyze_engine(engine)
    # Print the results
    print(f"Engine: {engine['name']}")
    print(f"Propellants: {engine['fuel']} / {engine['oxidizer']}")
    print(f"Chamber Pressure: {engine['Pc']} bar")
    print(f"Calculated Isp: {engine['Isp']:.2f} s")
    print("-" * 40)
    

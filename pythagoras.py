# Pythagoras Theorem
# Find 'Hypotenuse', 'Base' or 'Perpendicular'

cmd = str(input("to find 'Hypotenuse' press 'h' \nto find 'Perpendicular' press 'p'\nto find 'Base' press 'b' : "))

# Hypotenuse
if cmd == "h":
    p = float(input("Enter Perpendicular : "))
    b = float(input("Enter Base : "))
    h = (p**2 + b**2) ** 0.5
    print(f"Hypotenuse is : {h}")

# Perpendicular   
if cmd == "p":
    h = float(input("Enter Hypotenuse : "))
    b = float(input("Enter Base : "))
    p = (h**2 - b**2) ** 0.5
    print(f"Perpendicular is : {p}")

# Base
if cmd == "b":
    h = float(input("Enter Hypotenuse : "))
    p = float(input("Enter Perpendicular : "))
    b = (h**2 - p**2) ** 0.5
    print(f"Base is : {b}")
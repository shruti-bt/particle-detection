
def particle_detection():
    a = "Sphere|0.2334|FBS"
    b = (a.split('|'))[-1]
    
    if b == "FBS":
        print("Fragment")
    elif b == "SBF":
        print("Sphere")
    else:
        print(b)
particle_detection()
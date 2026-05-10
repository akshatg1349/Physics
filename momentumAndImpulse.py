print("Which topic will you choose?")
print("A: change in momentum/force of impact/time")
print("or B: a comprehensive table-esque showing initial momentum, final momentum, and momentum change")
adventure = input("Just say the letter!:")
#The program asks for mass, initial velocity, and final velocity because that is needed to calculate impulse
#Note that this formula makes sense due to our prior knowledge that p=mv or momentum = mass*velocity
if adventure.upper() == "A":
    mass = float(input("What is the mass of the object you want in kg?: "))
    vi = float(input("What is the initial velocity of the object you want in m/s?: "))
    vf = float(input("What is the final velocity of the object you want in m/s?: "))
    impulse = mass * (vf - vi)
    print("Your change in momentum/impulse is ", impulse, "kg*m/s")
    #time is asked for because we need that to calculate j, the impulse, from the formula: j=Ft
    #you may or may not need to rearrange the formula into F=j/t
    t = float(input("What is the time of impact in seconds?: "))
    force = impulse/t
    print("The force of impact is ", force, "N")
if adventure.upper() == "B":
    print("Would you like to know what happens when there is: ")
    print("A: an elastic collision or B: an inelastic collision")
    adventure = input("Just say the letter!: ")
    #Elastic collision
    if adventure.upper() == "A":
        #m1v1i + m2v2i = m1v1f + m2v2f
        m1 = float(input("What is the mass of object 1 in kg?: "))
        m2 = float(input("What is the mass of object 2 in kg?: "))
        v1i = float(input("What is the initial velocity of object 1 in m/s?: "))
        v1f = float(input("What is the final velocity of object 1 in m/s?: "))
        v2i = float(input("What is the initial velocity of object 2 is m/s?: "))
        #Rearranged the equation to get the final velocity of object 2
        v2f = (m1*v1i + m2*v2i - m1*v1f)/m2
        #this can be made into a table
        print("the final velocity of the second object is ", v2f, "m/s")
        print("the initial momentum of object 1 is", m1*v1i, "kg*m/s")
        print("the initial momentum of object 2 is", m2*v2i, "kg*m/s")
        print("the total initial momentum is", m1*v1i + m2*v2i, "kg*m/s")
        print("the final momentum of object 1 is", m1*v1f, "kg*m/s")
        print("the final momentum of object 2 is", m2*v2f, "kg*m/s")
        print("the total final momentum is", m1*v1f + m2*v2f, "kg*m/s")
        print("the momentum change of object 1 is ", (m1*v1f) - (m1*v1i), "kg*m/s")
        print("the momentum change of object 2 is ", (m2*v2f) - (m2*v2i), "kg*m/s")
        print("the change in momentum is ", (m1*v1f + m2*v2f)-(m1*v1i + m2*v2i), "kg*m/s")
    #Inelastic collision
    if adventure.upper() == "B":
        #m1v1i + m2v2i = m*vf
        m1 = float(input("What is the mass of object 1 in kg?: "))
        m2 = float(input("What is the mass of object 2 in kg?: "))
        v1i = float(input("What is the initial velocity of object 1 in m/s?: "))
        v2i = float(input("What is the initial velocity of object 2 is m/s?: "))
        m = m1+m2
        #Rearranged the equation to get the final velocity
        vf = (m1*v1i + m2*v2i) / m
        print("the final velocity of the combined mass is ", vf, "m/s")
        print("the initial momentum of object 1 is", m1*v1i, "kg*m/s")
        print("the initial momentum of object 2 is", m2*v2i, "kg*m/s")
        print("the total initial momentum is", m1*v1i + m2*v2i, "kg*m/s")
        print("the final momentum of object 1 is", m1*vf, "kg*m/s")
        print("the final momentum of object 2 is", m2*vf, "kg*m/s")
        print("the total final momentum is", m*vf, "kg*m/s")
        print("the momentum change of object 1 is ", (m1*vf) - (m1*v1i), "kg*m/s")
        print("the momentum change of object 2 is ", (m2*vf) - (m2*v2i), "kg*m/s")
        print("the change in momentum is ", (m1*vf + m2*vf)-(m1*v1i + m2*v2i), "kg*m/s")

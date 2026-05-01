#Calculate the work and energy of an object
#May or may not have any work external
#If Wext is present, some force has to be there; you should expect negative force
print("Would you like to see what happens to an object when A) there is work external or B) change in certain factors due to KE and PE? (e.g. height and velocity) ")
adventure1 = input("Just say the letter!: ")

g = 10  # gravity constant

if adventure1.upper() == "A":
    print("Keep in mind that your object is at ground level for the entire experiment and it will stop moving at the end")
    m = float(input("What is the mass of that object you would like to use in kg?: "))
    v = float(input("What is the velocity of that object you would like to use in m/s?: "))
    #KE = 0.5mv^2 is used to calculate the kinetic energy
    Kei = 0.5*m*v**2
    print("Kei = ", Kei, "J")
    #In this case, work is change in kinetic energy
    #Work has the same magnitude but opposite direction as kinetic energy
    #This is because the final kinetic energy is 0 J and for instance, if the initial kinetic energy were 2 J
    #The work would be -2 J
    Work = -Kei
    stairs = input("Are you trying to include stairs in this problem? Yes or No: ")
    if stairs.upper() == "YES":
        noOfStairs = int(input("How many stairs does the guy climb?: "))
        heightOfEachStair = float(input("What will be the height for each stair you use in meters?: "))
        total_height = noOfStairs * heightOfEachStair
        force = Work/(total_height)
        #W = Fd -> F = W/d
        print("F =", force, "N")
        print("W = ", Work, "J")
        time = float(input("How much time did it take for the guy to climb those stairs?: "))
        #P = W/t
        print("P = ", Work/time, "W")
    else:
        print("Kei = ", Kei, "J")
        #0 m/s velocity at the end
        print("KEf = 0 J")
        #0 m height throughout the entire experiment
        print("PEi = 0 J")
        print("PEf = 0 J")
        print("TMEi = ", Kei, "J")
        print("TMEf = 0 J")
        #Change in KE will only depend on KEi
        print("Change in KE = ", -Kei, "J")
        print("Change in PE = 0 J")
        print("W = ", -Kei, "J")


if adventure1.upper() == "B":
    print("Do you want to solve for A) the final velocity or B) the final height?: ")
    adventure2 = input("Just say the letter!")
    if adventure2.upper() == "A":
        print("Keep in mind that your object is at some height for the entire experiment and it will end at a different height")
        print("Also initial velocity is 0 m/s")
        height1 = float(input("What is the initial height of your object in meters?: "))
        height2 = float(input("What is the final height of your object in meters?: "))
        m = float(input("What is the mass of that object you would like to use in kg?: "))
        #compute KEf

        #g = 10
        PEi = m*10*height1
        PEf = m*10*height2
        TMEi = PEi

        Work = float(input("How much external work is done on the object (J)? "))

        TMEf = TMEi + Work
        KEf = TMEf - PEf

        #Initially, there is no speed, so KEi = 0.5mv^2 yields that KE = 0 J
        print("KEi = 0 J")
        print("KEf = ", KEf, "J")
        print("PEi = ", PEi, "J")
        print("PEf = ", PEf, "J")
        print("TMEi = ", PEi, "J")
        print("TMEf = ", TMEf, "J")
        #Because initial KEi is 0 J, the change will only depend on KEf for now
        print("Change in KE = ", KEf, "J")
        print("Change in PE = ", PEf - PEi, "J")
        #In this case, work is change in mechanical energy (could be +, -, or 0)
        print("Work = ", Work, "J")

        if KEf < 0:
            print("Error: Final kinetic energy is negative. Check your inputs.")
        else:
            #Use KE = 0.5mv^2 -> v = sqrt(2KE/m) to determine the velocity
            v = (2*KEf/m)**0.5
            print("vf = ", v, "m/s")

    else:
        print("Keep in mind that your object is initially at h=0 and it will end at a different height")
        print("Also final velocity is 0 m/s")
        m = float(input("What is the mass of that object you would like to use in kg?: "))
        v = float(input("What is the initial velocity of your object in meters per seconds?: "))
        KEi = 0.5*m*v**2
        PEf = KEi
        #KEf is excluded because the object ends up with 0 m/s velocity
        #PEi is excluded because the objects starts at ground level
        TMEi = KEi
        TMEf = PEf
        Work = TMEf - TMEi
        print("KEi = ", KEi, "J")
        print("KEf = 0 J")
        print("PEi = 0 J")
        print("PEf = ", PEf, "J")
        #PEf = mgh, g is always 10, so the formula used in this program is PE = 10mh
        #Depending on which teacher you have, you might need to rearrange the equation as h = PE/10m
        h = PEf/(10*m)
        print("h = ", h, "m")
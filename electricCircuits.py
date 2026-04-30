def seriesCircuitCurrent(resistors, voltage):
    totalResistance = 0
    for i in range(0, len(resistors)):
        totalResistance += resistors[i]
    return voltage/totalResistance

def seriesCircuitPower(resistors, voltage):
    totalResistance = 0
    for i in range(0, len(resistors)):
        totalResistance += resistors[i]
    return voltage**2/totalResistance
    
def parallelCircuitCurrent(resistors, voltage):
    reciprocalSum = 0
    for r in resistors:
        reciprocalSum += 1 / r
    totalResistance = 1 / reciprocalSum
    return voltage / totalResistance

def parallelCircuitPower(resistors, voltage):
    reciprocalSum = 0
    for r in resistors:
        reciprocalSum += 1 / r
    totalResistance = 1 / reciprocalSum
    return voltage**2 / totalResistance

x = seriesCircuitCurrent([2,2,2], 12)
print("In the series circuit, I = " + str(x) + " A")

p1 = seriesCircuitPower([2,2,2], 12)
print("In the series circuit, P = " + str(p1) + " W")

if x >= 30:
    print("Circuit breaker activated for the series circuit")

y = parallelCircuitCurrent([2,2,2], 12)
print("In the parallel circuit, I = " + str(y) + " A")

p2 = parallelCircuitPower([2,2,2], 12)
print("In the parallel circuit, P = " + str(p2) + " W")

if y >= 30:
    print("Circuit breaker activated for the parallel circuit")
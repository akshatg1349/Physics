"""
This program calculates the current and power in series and parallel circuits
The Ohm's Law and power formula are rewritten to match what we are trying to calculate
Current: V=IR -> I=V/R
Power: P = VI -> P=V²/R

    I = current in amperes (A)
    V = voltage in volts (V)
    R = resistance in ohms (Ω)
    P = power in watts (W)
"""

def seriesCircuitCurrent(resistors, voltage):
    """
    Calculate the current in a series circuit.
    In a series circuit, the total resistance is Req = R1+R2+R3+...
    resistors is a list that contains the resistance for each resistor
    voltage is a float that stores the battery's voltage
    we return the current
    """
    totalResistance = 0

    for i in range(0, len(resistors)):
        totalResistance += resistors[i]

    return voltage / totalResistance


def seriesCircuitPower(resistors, voltage):
    """
    Calculate the power in a series circuit.
    In a series circuit, the total power is V*V/R
    resistors is a list that contains the resistance for each resistor
    voltage is a float that stores the battery's voltage
    we return the power
    """
    totalResistance = 0

    for i in range(0, len(resistors)):
        totalResistance += resistors[i]

    return voltage**2 / totalResistance


def parallelCircuitCurrent(resistors, voltage):
    """
    Calculate the current in a parallel circuit.
    In a parallel circuit, the total resistance is 1/Req = 1/R1 + 1/R2 + 1/R3+...
    resistors is a list that contains the resistance for each resistor
    voltage is a float that stores the battery's voltage
    we return the current
    """
    reciprocalSum = 0

    for r in resistors:
        reciprocalSum += 1 / r

    totalResistance = 1 / reciprocalSum

    return voltage / totalResistance


def parallelCircuitPower(resistors, voltage):
    """
    Calculate the power in a series circuit.
    In a parallel circuit, the total power is V*V/R
    resistors is a list that contains the resistance for each resistor
    voltage is a float that stores the battery's voltage
    we return the power
    """
    reciprocalSum = 0

    for r in resistors:
        reciprocalSum += 1 / r

    totalResistance = 1 / reciprocalSum

    return voltage**2 / totalResistance


# Calculate and display current for the series circuit
x = seriesCircuitCurrent([2, 2, 2], 12)
print("In the series circuit, I = " + str(x) + " A")

# Calculate and display power for the series circuit
p1 = seriesCircuitPower([2, 2, 2], 12)
print("In the series circuit, P = " + str(p1) + " W")

# Check if the series circuit current is high enough to activate the breaker
if x >= 30:
    print("Circuit breaker activated for the series circuit")

# Calculate and display current for the parallel circuit
y = parallelCircuitCurrent([2, 2, 2], 12)
print("In the parallel circuit, I = " + str(y) + " A")

# Calculate and display power for the parallel circuit
p2 = parallelCircuitPower([2, 2, 2], 12)
print("In the parallel circuit, P = " + str(p2) + " W")

# Check if the parallel circuit current is high enough to activate the breaker
if y >= 30:
    print("Circuit breaker activated for the parallel circuit")
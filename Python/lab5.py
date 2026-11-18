import math

value=int(input("Enter a numerical value:"))
exp=int(input("Enter an exponent:"))
dec=float(input("Enter a decimal measurement:"))

print("RESULTS")
print("VALUE: ",value)
print("EXPONENT: ",exp)
print("POWER: ", math.pow(value, exp))
print("SQUARE ROOT: ", math.sqrt(value))

print("DECIMAL VALUE: ",dec)
print("CEIL VALUE: ",math.ceil(dec))
print("FLOOR VALUE: ",math.floor(dec))
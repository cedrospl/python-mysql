print(8 * 3)
five = 5
three = 3
print(five * three)
type(five)
type(five * three)
print(five/three)
print(type(five/three))
import sys
print(sys.maxsize)
veryBigValue = 999999999999999999999999999999999999999999999999999999
print(veryBigValue)
print(veryBigValue + 1)
print(type(veryBigValue))
print((veryBigValue + 1)/2)
print(type((veryBigValue + 1)/2))
print(five//three)
print(five % three)
print(float('inf'))
print(type(float)('inf'))
print(float("inf") > 99999999999999)
print(float("inf") > 999999999999999999999999999999999999999999999999999999)
print(-float("inf"))

# Formatowanie napisów i typy numeryczne - LAB
name1 = "Mariusz"
age1 = 27
daysInYear = 365
message = "%s is %d years old, so is about %d days old"
print(message % ("Jan", 26, 26 * daysInYear))
name2 = "Jan"
age2 = 26
print(message % (name2, age2, age2 * daysInYear))
message1 = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message1.format("Chris", 17, 17 * daysInYear))
integerCalculation = "{0:d} divided by {1:d} is {2:d} and the rest is {3:d}"
int1 = 1234567890
int2 = 12345
int3 = int1 // int2
int4 = int1 % int2
print(integerCalculation.format(int1, int2, int3, int4))

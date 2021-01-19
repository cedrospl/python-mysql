Title = "Python"
print("Title is", type(Title))

Version = 3
print("Version is", type(Version))

Progress = 0.21
print("Progress is", type(Progress))

print("This expression is", type(Progress * Version))

x = 1
y = 1
z = 1
print(x, y, z)

a=b=c = 2
print(a, b, c)

c = 3
print(a, b, c)

print(2+ 2 * 2)

print(6 / 2 * (1+2))

print(4 ** 3 ** 2)

a = 1
print(x + 1)
print(x)
x = x + 1
print(x)
x += 1
print(x)
x -= 1
print(x)

# Zmienne Tips & tricks. Kolejność działań - LAB
v1 = 126
v2 = '126'
v3 = 126.0
v4 = '126.0'
print(type(v1))
print(type(v2))
print(type(v3))
print(type(v4))

print(v1 + v3)
print(type(v1 + v3))
print(v2 + v4)
print(type(v2 + v4))
print(7 - 1 * 0 + 3 + 3)
print(4 ** 5 / 2 ** 3)
print(99 + 9 / 9)
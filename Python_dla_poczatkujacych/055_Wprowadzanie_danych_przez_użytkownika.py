#filename = input("Enter filename: ")
#print("The file name is: %s" % (filename))

while True:

    filesizeStr = input("Enter the max file size: ")

    if filesizeStr.isdecimal():
        filesizeInt = int(filesizeStr)
        break

print("The max size is %d" % (filesizeInt))

print("Size in KB is %d" % (filesizeInt * 1024))

# Wprowadzanie danych przez użytkownika - LAB

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

a_str = input("Please provide integer for a: ")
b_str = input("Please provide integer for b: ")
c_str = input("Please provide integer for c: ")

if not check_int(a_str) and check_int(b_str) and check_int(c_str):
    print("a, b and c need to be integer!!")
else:
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)
    if a == 0:
        print("a cannot be 0!")
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            print("There is no solution!")
        elif delta == 0:
            x1 = -b / (2*a)
            print("There is only one solution: ", x1)
        else:
            x1 = (-b - delta ** 0.5) / (2 * a)
            x2 = (-b + delta ** 0.5) / (2 * a)
            print("There are two solutions:", x1, "and", x2)


s = "A Python script"
print(s[0])
print(s[2])
print(s[2:7])
print(s[2:8])
print(s[:8])
print(s[8:])
print(s[2:999])
print(s[222:999])

message = 'Document "cv.doc" was printed on printer: XEROX'
print(message.find(':'))
print(message[message.find(':') + 2 :])

print(message[message.find('"') + 1 :])
tmp = message[message.find('"') + 1 :]
print(tmp[:tmp.find('"')])

# Napis jako tablica znaków - LAB

q = "THE EYES"
print(q[0] + q[1] + q[2] + q[5] + q[3] + q[7] + q[4] + q[6])

q = "a gentleman"
print(q[3]+ q[6] + q[7] + q[2] + q[0] + q[4] + q[5] + q[1] + q[8:])
a = "THE MORSE CODE"
print(a[1:3] + a[6] + a[2] + a[3] + a[10:12] + a[4] + a[2] + a[3] + a[12] + a[5] + a[0] + a[7])

line = 'Program "Kropka nad i" nadamy o: 22:00'
time = line[line.find(":") + 2:]
print(time)
tmp1 = line[line.find('"') + 1:]
title = tmp1[:tmp1.find('"')]
print(title)
print(time)

line2 = 'Program "Pytanie na śniadanie" nadamy o: 6:00'
time2 = line2[line2.find(":") + 2 :]
print(time2)
tmp2 = line2[line2.find('"') + 1:]
title2 = tmp2[:tmp2.find('"')]
print(title2)
print(time2)
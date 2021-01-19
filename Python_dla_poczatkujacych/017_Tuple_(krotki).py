Tax = (4, 7, 8, 23)

print(Tax[-1])
print(Tax.index(7))
print(Tax.count(8))
print(max(Tax))

#Tax.revert()
Taxlist = list(Tax)
Taxlist.append(30)
NewTax = tuple(Taxlist)

print(Tax)
print(Taxlist)
print(NewTax)

(tax1, tax2, tax3, tax4) = Tax
print(tax1, tax2, tax3, tax4)

a = 1
b = 10
print("a =",a,"\tb =",b)
#temp = a
#a = b
#b = temp
(a, b) = (b, a)
print("a =",a,"\tb =",b)

# Listy, tuples - LAB

#1
marketing = ['loyalty program', 'client promotion', 'market research']
print(marketing)
#2
marketing.append('public relations')
print(marketing)
#3
print(marketing[2])
#4
marketing.insert(1, 'investor relations')
print(marketing)
#5
emailMarketing = marketing.copy()
print(emailMarketing)
#6
emailMarketing.sort()
print(emailMarketing)
#7
internalEmails = ['internal communication']
print(internalEmails)
#8
emailMarketing.extend(internalEmails)
print(emailMarketing)
#9
emailTuple = tuple(emailMarketing)
print(emailTuple)
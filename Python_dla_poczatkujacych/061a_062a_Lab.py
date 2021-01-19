import sys
# Obsługa błędu - instrukcja try - LAB + Obsługa błędu - instrukcja except - LAB

#import modułu sys na górze pliku

file_path = r"/home/oem/PycharmProjects/Git repo/Python_dla_poczatkujacych/orders.csv"

with open(file_path, "r") as file:
    for line in file:
        line = line.replace('\n', '')
        order = line.split(',')
        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print("Order from drugstore '%s', item '%s', amount '%d'" % (pharmacy_name, item, amount))
        except ValueError as e:
            print("There was a problem in line '%s' with converting data into 'int'" %line)
        except IndexError as e:
            print ("There was a problem in line '%s' with amount of fields" %line)
        except:
            print("Problem with line %s" % line)
            print(sys.exc_info()[0])
print("Processing finished")

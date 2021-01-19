import os
import datetime

#while True:

#    filename = input("Enter path to results file: ")

#    if os.path.isfile(filename):
#        break
#    else:
#        print("File name is not correct, try again!")
#print("The results file is %s" % filename)

# Kontrola ścieżki do pliku - LAB

#import modułów os i datetime na górze pliku

data_input_catalog = '/home/oem/PycharmProjects/Git repo/Python_dla_poczatkujacych/data_input'
data_output_catalog = '/home/oem/PycharmProjects/Git repo/Python_dla_poczatkujacych/data_output'

today = datetime.date.today()
today_output_catalog = os.path.join(data_output_catalog, today.strftime("%Y-%m-%d"))

is_input_catalog_ok = os.path.isdir(data_input_catalog)

is_output_catalog_ok = os.path.isdir(data_output_catalog)

is_today_output_catalog_ok = not(os.path.isdir(today_output_catalog)) and not(os.path.isfile(today_output_catalog))


if is_input_catalog_ok and is_output_catalog_ok and is_today_output_catalog_ok:
    print("Conditions met! We can continue!")
else:
    print("Prerequisites not met! Check the paths!")

    if not is_input_catalog_ok:
        print("Input catalog %s must exist!" % is_input_catalog_ok)
    if not is_output_catalog_ok:
        print("Output catalog %s must exist!" % is_output_catalog_ok)
    if not is_today_output_catalog_ok:
        print("Today's output %s cannot exist (neither as directory nor as file)!" % is_today_output_catalog_ok)

import sys

print("Liczba argumentow przekazanych do programu: ",
      len(sys.argv))
print("Wszystkie argumenty to: ", str(sys.argv))

print("Nazwa programu to: ", sys.argv[0])
print("Wynik dodawania parametrow to: ", sys.argv[0] + sys.argv[0])

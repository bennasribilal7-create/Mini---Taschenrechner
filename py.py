
def addieren(a, b):
    return a + b

def subtrahieren(a, b):
    return a - b

def multiplizieren(a, b):
    return a * b

def dividieren(a, b):
    if b == 0:
        print ("undefiniert")
    else:
        return a / b
    

print ("addieren")
print ("subtrahieren")
print ("multiplizieren")
print ("dividieren")

while True:
   option = int(input("Auszuführende Rechenoperation (1-4):"))

   a = int(input("Gebe deine erste Zahl ein:"))

   b = int(input("Gebe deine zweite Zahl ein:"))


   Ergebnis1 = addieren(a, b)
   Ergebnis2 = subtrahieren(a, b)
   Ergebnis3 = multiplizieren(a, b)
   Ergebnis4 = dividieren(a, b)


   if option == 1:
       print (Ergebnis1)

   elif option == 2:
       print (Ergebnis2)

   elif option == 3:
       print (Ergebnis3)

   elif option == 4:
       print (Ergebnis4)


   Abfrage = input("Möchtest du noch eine Rechenoperation durchführen? (j/n): ")
   if Abfrage == "n":
      print ("Programm beendet.")
      break
i = 8
while i < 10:
    print("Die Zahl ist kleiner als 10.")
    i += 2
else:
    print("Und jetzt ist die Zahl größer als 10.")

for i in range(1, 10):
    if i >= 4:
        break
    print(i)
else:
    print("Die Schleife ist beendet")

print("Außerhalb der Schleife")

import os

n = int(input("Ingrese un número entre el 1 y 10: "))
file_name = f"./tabla-{n}.txt"
with open(file_name,mode="w") as f:
    for i in range(1,13):
        cadena = f"{n} x {i} = {i*n}\n"
        f.write(cadena)
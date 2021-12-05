import os
n = int(input("Ingrese un número entre el 1 y 10: "))
file_name = f"./tabla-{n}.txt"
if os.path.exists(file_name):
    with open(file_name,mode="r") as f:
        m = f.read()
        print(m)
else:
    print(f"""El fichero {str(file_name.split("/")[-1])} no Existe""")



from casillas import Casillas


tableros = []


# Lectura del archivo
file = open("A-small-practice.in")

lines = file.readlines()
k = 1
print("Numero de elementos: ",lines[0])
for i in range(int(lines[0])):
    tablero = [list(lst[0:int(lines[k])]) for lst in lines[k+1:k+int(lines[k])+1]]
    tableros.append(tablero)

    k = k+int(lines[k])+1

file.close()


# Solucion del problema
buscaminas = {}
tablero = tableros[0]
print(tablero)


cont = 0
x = 0
for i in tablero:
    buscaminas[cont] = []
    print(i)
    for j in i:
        casilla = Casillas(x,cont)
        if(j=="*"):
            casilla.setType(0)
        buscaminas[cont].append(casilla)
        x = x+1
    cont = cont+1

            
            
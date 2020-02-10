
# Traductor
numbers = {
    "0":[1,1,1,1,1,1,0],
    "1":[0,1,1,0,0,0,0],
    "2":[1,1,0,1,1,0,1],
    "3":[1,1,1,1,0,0,1],
    "4":[0,1,1,0,0,1,1],
    "5":[1,0,1,1,0,1,1],
    "6":[1,0,1,1,1,1,1],
    "7":[1,1,1,0,0,0,0],
    "8":[1,1,1,1,1,1,1],
    "9":[1,1,1,1,0,1,1]
}

# Entradas
INPUT = []

# Leyendo archivo de INPUT
f = open("text.txt")
lines = f.readlines()
for i in range(1,int(lines[0])+1):
    k = 2
    INPUT_temp = []
    for j in range(int(lines[i][0])): 
        temp = list(lines[i][k:k+7])
        k = k+8
        INPUT_temp.append(temp)
    INPUT.append(INPUT_temp)

f.close()

# Funcion posibilidades de 'numbers'
def posNumber(eval,numbers):

    keys = numbers.keys()
    index = []
    pos = []

    for i in range(7):
        if(eval[i]=='1'):
            index.append(i)
            
    for key in keys:
        state = True
        for i in index:
            if(numbers[key][i]!=1):
                state = False
        if(state==True):
            pos.append(int(key))

    return pos

soluciones = []

for i in INPUT:
    #print("============================")
    pos = []
    for j in i:
        pos.append(posNumber(j,numbers))

    #print(pos)
    res = pos[-1]
    for j in range(1,len(pos)):
        temp = [(x+1)%10 for x in res]
        inte = [v for v in temp if v in pos[-j-1]]
    
        res = inte
        #print("=====>",res)

    if(len(res)==1):
        val = res[0]
        #print("Valor: ",val-len(pos))

        err = []
        Co = numbers[str(val)] #Numeros
        In = i[0] #String

        #print("Co: ",Co)
        #print("In: ",In)

        for k in range(len(i[0])):
            if(str(Co[k])!=In[k]):
                err.append(k)

        #print("Errores: ",err)
        
        bus = numbers[str(abs(val-len(pos)))][:]
        #print("Bus: ",bus)

        for k in err:
            bus[k] = 0
        #print(bus)
        soluciones.append(bus)
    else:
        #print("No hay suficiente informacion")
        soluciones.append(["ERROR!"])

case = 1
for i in soluciones:
    if(len(i)>1):
        print("Case #"+str(case)+": "+(''.join(str(e) for e in i)))
    else:
        print("Case #"+str(case)+": "+(i[0]))
    case = case+1







        


def arithmetic_arranger(lista, consresul):
#lista = ["32 + 8", "1 - 381", "996699 + 999999", "523 - 49"]
#lista = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49","32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
#conresul = True
fila1 = list()
fila2 = list()
fila3 = list()
fila4 = list()
fi1 = ""
fi2 = ""
fi3 = ""
fi4 = ""
for i in lista:
    li = i.split()
    fila1.append(" ")
    fila2.append(li[1])
    fila3.append("-")

    fila1.append(li[0])
    fila2.append(li[2])
    fila3.append("-")

    fila1.append("    ")
    fila2.append("    ")
    fila3.append("    ")

    if conresul :
        fila4.append(" ")
        if li[1]=="+":
            fila4.append(str(int(li[0])+int(li[2])))
        else:
            fila4.append(str(int(li[0])-int(li[2])))
        fila4.append("    ")


for i in range(len(fila1)):
    if conresul:
        maximo = max(len(fila1[i]),len(fila2[i]),len(str(fila4[i])))
    else:
        maximo = max(len(fila1[i]),len(fila2[i]))
    fi1 = fi1 + fila1[i].rjust(maximo," ")
    fi2 = fi2 + fila2[i].rjust(maximo," ")
    fi3 = fi3 + fila3[i].rjust(maximo,"-") # ///////
    if conresul:
        fi4 = fi4 + fila4[i].rjust(maximo," ")


print(fi1)
print(fi2)
print(fi3)
if conresul:
    print(fi4)

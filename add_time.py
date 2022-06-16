def add_time(a,b,dia="0"):
    semana = ['Domingo','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado']
    #########[ 0 , 1, 2, 3, 4, 5, 6],
    param1 = a.split()
    am_pm  = param1[1]
    param1 = param1[0].split(":")
    param2 = b.split(":")
    # dias, fecha y hora origen
    do = 0
    ho = int(param1[0]) # Hora original
    mo = int(param1[1]) # Minutos original
    if am_pm == "PM":
        ho = ho + 12
    # dias, horas y minutos de demora
    dd = int(param2[0]) // 24
    hd = int(param2[0]) - (dd * 24)   # Resto de Horas del ultimo dia
    md = int(param2[1])   # Minutos
    # dias, horas y minutos finales
    df = do + dd
    hf = ho + hd
    mf = mo + md

    if hf == 0:
        hf = 12
    if mf > 60:
        mf = mf - 60
        hf = hf + 1
    if hf >= 24:
        hf = hf - 24
        df = df + 1
    if hf > 12:
        hf = hf - 12
    if hf == 0:
        hf = 12
    if hf + ho > 12:
        if am_pm == "AM":
            am_pm = "PM"
        else:
            am_pm = "AM"

    if dia == "0" and df == 0:
        dia = ""
        dia2 = ""
    elif dia == "0" and df == 1:
        dia = ""
        dia2 = " (next day)"
    elif dia == "0" and df > 1:
        dia = ""
        dia2 = " (" + str(df) + " days later)"
    elif df == 0:
        indice = semana.index(dia.capitalize())
        dia = ", " + semana[ indice + df]
        df = indice + df
        dia2 = " "
    else:
        indice = semana.index(dia.capitalize()) # indice  7
        resto = indice+df + (indice+df) // 6
        dia = ", " + semana[resto]
        dia2 = " (" + str(df) + " days later)"
    # Imprimo el resultado final
    print(str(hf)+":"+str(mf).rjust(2,"0")+" "+am_pm+dia + dia2 )

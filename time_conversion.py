def timeConversion(s):
    period = s[-2:]
    s = s[:-2]
    hora, minute, seconds = s.split(":")
    int(hora)
    int(minute)
    int(seconds)    
    hora = int(hora)
    if period == "AM" and hora == 12:
        hora = 0
    elif period == "PM" and hora != 12:
        hora += 12
    
    resposta = (f"{hora:02d}:{minute}:{seconds}")
    
    return resposta
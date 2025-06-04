import time

data = time.localtime()

print("ano:", data.tm_year)
print("mes:", data.tm_mon)
print("dia:", data.tm_mday)
print(f"Hoje é , {data.tm_mday}/{data.tm_mon}/{data.tm_year}")

print(time.strftime("Hoje é dia %d de %B de %Y e agora são %H horas %M minutos %S segundos"))
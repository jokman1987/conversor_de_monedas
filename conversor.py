menu = print("""

Bienvenido al conversor de monedas💲💵
1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos
""")
def conversor(tipo_pesos, valor_moneda):
    pesos = input("Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_moneda
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares +" dolares")

opcion =int(input("Elige una opción: "))

if opcion == 1:
    conversor("Colombianos", 3875)
elif opcion == 2:
    conversor("Argentinos", 65)
elif opcion == 3:
    conversor("Mexicanos", 24)
else:
    print("No ingresaste la opcion correcta")




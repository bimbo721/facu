import random


opciones = ["piedra", "papel", "tijera"]

opciones_pc = random.choice(opciones)

opciones_humano = str(input("ingrese si elige piedra,papel o tijera: ")).lower()

print(opciones_pc)

if opciones_pc == opciones_humano:
    print("empate")
elif opciones_humano == "piedra" and opciones_pc == "tijera":
    print("ganaste")
elif opciones_humano == "piedra" and opciones_pc == "papel":
    print("perdiste")
elif opciones_humano == "papel" and opciones_pc == "tijera":
    print("perdiste")
elif opciones_humano == "papel" and opciones_pc == "piedra":
    print("ganaste")
elif opciones_humano == "tijera" and opciones_pc == "piedra":
    print("perdiste")
elif opciones_humano == "tijera" and opciones_pc == "papel":
    print("ganaste")



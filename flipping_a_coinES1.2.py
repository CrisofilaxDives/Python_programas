# Tirar la monedas

import random

# Función de tirar la moneda
def moneda():
    print("""Bienvenido a Tirar la Moneda.
Podrá apostar sus monedas y ganar más.
Usted comienza con 100 monedas.
Recuerda que puedes escrbir 'Salir' para salir y ver cuantas monedas ganaste.
""")

    # input() del lado de la moneda
    dinero = 100
    while dinero > 0:
        while True:
            lado_moneda = input("""Escriba el lado de la moneda por la que quiere apostar.
Puede escribir 'Salir' para salir del juego.
Ahora elija, 'Cara' o 'Sello': """).lower()
            if lado_moneda == "salir":
                break
            else:
                if lado_moneda == "cara":
                    print("Usted escogió Cara.")
                    break
                elif lado_moneda == "sello":
                    print("Usted escogió Sello.")
                    break
                else:
                    print("""Hubo un error.
Intente de nuevo.
""")
                    continue

        # Condiciones para salir del loop del input()
        if lado_moneda == "salir":
            print(f"""
Gracias por sus apuestas.
Usted ganó {dinero}.
Qué tenga buen día.""")
            break
        elif dinero == 0:
            print("""
Su dinero ha llegado a 0.
Las apuestas se cerraron.
Qué tenga buen día.""")
            break

        # input() de la apuesta
        while True:
            apuesta = input("""
Ahora ingrese el valor de su apuesta.
Recuerde que no puede apostar una suma mayor a la de sus monedas.
Puede escribir 'Salir' para salir del programa.
Escriba cuanto quiere apostar: """).lower()
            if apuesta == "salir":
                break
            try:
                int_apuesta = int(apuesta)
                if int_apuesta >= 0 and int_apuesta <= dinero:
                    print(f"Usted apostó {int_apuesta} monedas")
                    break
                elif int_apuesta < 0:
                    print("""Su apusta no es valida.
Intende de nuevo""")
                    continue
                else:
                    print(f"{int_apuesta} monedas es mayor que el total de sus monedas.")
                    print("Intende de nuevo.")
                    continue
            except:
                print("Hubo un error. Intente de nuevo ingresar el valor de su apuesta.")
                continue

        # Condiciones para salir del loop del input()
        if apuesta == "salir":
            print(f"""
Gracias por sus apuestas.
Usted ganó {dinero}.
Qué tenga buen día.""")
            break
        elif dinero == 0:
            print("""
Su dinero ha llegado a 0.
Las apuestas se cerraron.
Qué tenga buen día.""")
            break

        # Tirando la moneda
        lado_random = random.randint(0, 1)
        print("""
Ahora miremos que lado de la moneda salío.
Tirando la moneda...""")
        if lado_random == 0:
            print("La moneda salió en Cara")
            if lado_moneda == "cara":
                dinero += int_apuesta
                print(f"Ganaste {int_apuesta} monedas. Ahora tienes {dinero} monedas")
            else:
                dinero -= int_apuesta
                print(f"Perdiste {int_apuesta} monedas. Ahora tienes {dinero} monedas")
        elif lado_random == 1:
            print("La moneda salió en Sello")
            if lado_moneda == "sello":
                dinero += int_apuesta
                print(f"Ganaste {int_apuesta} monedas. Ahora tienes {dinero} monedas")
            else:
                dinero -= int_apuesta
                print(f"Perdiste {int_apuesta} monedas. Ahora tienes {dinero} monedas")
        
        # Continuar las apuestas   
        while True:

            print("¿Quiere seguir jugando?")
            continuar = input("Escriba 'Si' para continuar o 'No' para terminar y ver sus monedas actuales: ").lower()
            try:
                if continuar == "si" and dinero > 0:
                    break
                elif dinero == 0:
                    print("Su dinero es 0, no puede continuar.")
                    break   
                elif continuar == "no":
                    break
            except:
                print("Hubo un error. Intente de nuevo")
                continue
        
        if continuar == "no" or dinero == 0:
            print(f"""
Gracias por sus apuestas.
Usted ganó {dinero}.
Qué tenga buen día.""")
            break

moneda()

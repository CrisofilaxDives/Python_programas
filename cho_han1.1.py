# Cho-Han
import random

def chohan():

    # Mensaje de presentación
    print("""Bienvenido al juego Cho-Han.
Este consiste en tirar dos dados, sumar sus resultados
y apostar Par o Impar, según el resultado de la suma.
Cuenta con 100 monedas al comienzo
""")

    monedas = 100

    while True:

        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma_dados = dado1 + dado2
        par_impar_division = suma_dados % 2

        # Loop para escoger par o impar
        while True:

            par_impar = input("""Ingrese si apuesta por par o impar escribiendo 'Par' o 'Impar'.
Puede escribir 'Salir' para terminar el juego y saber cuantas monedas tiene al final: """).lower()
            if par_impar == "salir":
                break
            else:
                if par_impar == "par":
                    print("Usted apuesta por 'Par'.")
                    break
                elif par_impar == "impar":
                    print("Usted apuesta por 'Impar'.")
                    break
                else:
                    print("Hubo un error. Intente de nuevo.")
                    continue

        if par_impar == "salir":
            print(f"Usted terminó con {monedas} monedas.")
            print("Qué tenga buen día.")
            break

        # Loop para escribir la apuesta
        while True:

            apuesta = input(f"""Ingrese el valor de su apuesta.
Recuerde que esta no puede ser mayor que las monedas que actualmente tiene.
Puede escribir 'Salir' para terminar el juego y saber cuantas monedas tiene al final: """).lower()
            if apuesta == "salir":
                break
            try:
                int_apuesta = int(apuesta)
                if int_apuesta < 0 or int_apuesta > monedas:
                    print(f"{int_apuesta} monedas, no es una apuesta valida. Intentelo de nuevo.")
                    continue
                else:
                    print(f"Usted apostó {int_apuesta} monedas.")
                    break
            except:
                print("Hubo un error. Intente de nuevo.")
                continue

        if apuesta == "salir":
            print(f"Usted terminó con {monedas} monedas.")
            print("Qué tenga buen día.")
            break
        
        # Condiciones para ganar o perder la apuesta
        print(f"""Tiremos los dados...
En el primer dado salió {dado1}.
En el segundo dado salió {dado2}.
""")
        if par_impar_division == 0 and par_impar == "par":
            monedas += int_apuesta
            print(f"Felicidades salió par, ahora tienes {monedas} monedas.")
        elif par_impar_division == 0 and par_impar == "impar":
            monedas -= int_apuesta
            print(f"Qué mal salió par, ahora tienes {monedas} monedas.")
        elif par_impar_division == 1 and par_impar == "impar":
            monedas += int_apuesta
            print(f"Felicidades salió impar, ahora tienes {monedas} monedas.")
        elif par_impar_division == 1 and par_impar == "par":
            monedas -= int_apuesta
            print(f"Qué mal salió impar, ahora tienes {monedas} monedas.")

        # Condiciones para seguir jugando
        while True:

            print("¿Quiere seguir jugando?")
            continuar = input("Escriba 'Si' para continuar o 'No' para terminar y ver sus monedas actuales: ").lower()
            try:
                if continuar == "si" and monedas > 0:
                    break
                elif monedas == 0:
                    print("Su dinero es 0, no puede continuar.")
                    break   
                elif continuar == "no":
                    break
            except:
                print("Hubo un error. Intente de nuevo")
                continue
        
        if continuar == "no" or monedas == 0:
            print(f"Usted terminó con {monedas} monedas.")
            print("Qué tenga buen día.")
            break

chohan()
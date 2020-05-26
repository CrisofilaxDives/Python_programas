# Cho_Han

import random

def chohan(apuesta, par_impar):
    # Primer dado
    dado1 = random.randint(1, 6)
    print(dado1)
    
    # Segundo dado
    dado2 = random.randint(1, 6)
    print(dado2)

    # Suma dados
    suma_dados = dado1 + dado2
    print(suma_dados)

    # Par o impar
    par_impar_division = suma_dados % 2
    if par_impar_division == 0:
        print("Par")
    else:
        print("Impar")

    # Apuesta
    monedas = 100
    if par_impar == "par" and par_impar_division == 0:
        monedas += apuesta
        print(f"Usted ahora tiene {monedas}.")
    elif par_impar == "impar" and par_impar_division == 0:
        monedas -= apuesta
        print(f"Usted ahora tiene {monedas}.")
    if par_impar == "impar" and par_impar_division > 0:
        monedas += apuesta
        print(f"Usted ahora tiene {monedas}.")
    elif par_impar == "par" and par_impar_division > 0:
        monedas -= apuesta
        print(f"Usted ahora tiene {monedas}.")

chohan(20, "par")   


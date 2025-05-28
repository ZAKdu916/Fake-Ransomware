import time
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def ransomware_simulation():
    clear_screen()
    print("\n" + "*" * 50)
    print("!!! VOTRE ORDINATEUR EST INFECTÉ PAR UN RANSOMWARE !!!")
    print("TOUS VOS FICHIERS SONT CHIFFRÉS.")
    print("POUR LES DÉCHIFFRER, PAYEZ 1000€ EN BITCOIN.")
    print("*" * 50 + "\n")

    countdown = 10
    while countdown > 0:
        print(f"Délai avant suppression définitive : {countdown} secondes", end='\r')
        time.sleep(1)
        countdown -= 1

    print("\n\nVous avez échoué à payer. Suppression des fichiers en cours... (simulation)\n")
    time.sleep(3)

    print("...mais en fait non, ceci est une simulation. Ne paniquez pas !")
    print("Gardez toujours une sauvegarde de vos données et faites attention aux liens suspects.")
    print("\nAppuyez sur Ctrl+C pour quitter.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        clear_screen()
        print("Simulation terminée. Merci d'avoir joué.")

if __name__ == "__main__":
    ransomware_simulation()

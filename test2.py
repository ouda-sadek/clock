import time 
def main():

    heure_alarme = int(input("Heure de l'alarme (0-23) : "))
    minute_alarme = int(input("Minute de l'alarme (0-59) : "))
    seconde_alarme = int(input("Seconde de l'alarme (0-59) : "))
    alarme = (heure_alarme, minute_alarme, seconde_alarme)
    while True:
        heure_actuelle = time.localtime()
        print(f"Heure actuelle : {heure_actuelle}")
        if alarme == heure_actuelle:
            print("Ring !")
            return
        time.sleep(1)
if __name__ == "__main__":
    main()
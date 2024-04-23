#region banner
def banner():
        print(" "* 40, r'  _   _       _       _  ')
        print(" "* 40, r' | | | | ___ | |_ ___| | ')
        print(" "* 40, r' | |_| |/ _ \| __/ _ \ | ')
        print(" "* 40, r' |  _  | (_) | ||  __/ | ')
        print(" "* 40, r' |_| |_|\___/ \__\___|_| ')


        print(" ","-"*103) # teli vonal sor
        # print (" |", " "*101, "|") # üres sor széle elemekkel
        # print("{:<22} {:<22} {:<22} {:<22} {:<22}".format(
        #         " | Szoba Szám", "Ágyak", "Ár", "Dátum", "Foglaló Neve | "))
        # print (" |", "-"*101, "|")
        print("")

#endregion 

import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def menu():
        
        print(" Válasszon azalábbiak közül:     \n Szoba foglaláshoz: [1]         \n Szoba foglalás lemondásához: [2]       \n Foglat szobák listája: [3] \n ")
        
        selected = int(input("Válaszon: "))
        
        if selected == 1:
               print("Szoba foglalást választotta")
        elif selected == 2:
               print("Szoba foglalás lemondását választotta")
        elif selected == 3:
                print("Szoba foglalást választotta")
        else:
                print("Nem megfelelő formátum! \n")
                return menu()
       


def Main():
        menu()



cls()
banner()
Main()
print("")
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

#region console clear
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
#endregion

#region classes
class Hotel:
        def __init__(self):
                self.name = 'Hotel-MD'
                self.oneBedRoom = self.oneBedRoom()
                self.twoBedRoom = self.twoBedRoom()
                
        class oneBedRoom:
                def __init__(self):
                       self.roomInfo = self.roomInfo()
                       
                class roomInfo:
                        def __init__(self, roomNumber,equipment,  price):
                                self.roomNumber = roomNumber
                                self.equipment = equipment        
                                self.price = price * (equipment/2)        
                                
                
        class twoBedRoom:
                def __init__(self):
                       self.roomInfo = self.roomInfo()
        
                class roomInfo:
                        def __init__(self, roomNumber, equipment, price):
                                self.roomNumber = roomNumber
                                self.equipment = equipment       
                                self.price = price*2*(equipment/2)       
                                
        
class reservation:
        def __init__(self, reservNumber, name, email, roomNumber, pay):
                self.reservNumber = reservNumber
                self.name = name
                self.email = email
                self.roomNumber = roomNumber
                self.pay = pay
                                                      
#endregion                    
                       
#region Factory

import random

roomsList = []
reservationList = []

def factory():
        def personGenerator():
                surnamelist = ["Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson"]
                firstNamelist = ["Emma", "Liam", "Olivia", "Noah", "Ava", "Ethan", "Sophia", "Mason", "Isabella", "James"]
                surname = random.choice(surnamelist)
                firstName = random.choice(firstNamelist)
                name = firstName + ' ' + surname
                email = name.replace(' ', '')+'@gmail.com'
                
                return name, email
        
        
                
                
        #legenerálom a szobák tulajdonságit
        roomNumCount = 0
        for item in range(random.randint(3,6)):
             roomNumCount += 1
             roomsList.append(Hotel.oneBedRoom.roomInfo(roomNumCount, random.randint(1,10), 10))
             roomNumCount += 1
             roomsList.append(Hotel.twoBedRoom.roomInfo(roomNumCount, random.randint(1,10), 10))
        
        #random foglalások legenrálása
        reservNumCount = 0
        for item in range(random.randint(5,8)):
                reservNumCount += 1
                templist = personGenerator()
                reservationList.append(reservation(reservNumCount, templist[0], templist[1],random.randint(1,12) , 69)) #innen folyt kov ranndom.randit csere ellenorzesre h van e szoba szam

#endregion         

# roomList = []
# roomList.append(Hotel.oneBedRoom.roomInfo(3,300,5))
# roomList.append(Hotel.twoBedRoom.roomInfo(4,300,6))




def menu():
        
        print(" Válasszon azalábbiak közül:     \n Szoba foglaláshoz: [1]         \n Szoba foglalás lemondásához: [2]       \n Foglat szobák listája: [3] \n ")
        
        selected = int(input("Válaszon: "))
        
        if selected == 1:
               print("Szoba foglalást választotta")
        elif selected == 2:
               print("Szoba foglalás lemondását választotta")
                
        elif selected == 3:
                print("Szobák listázását választotta!")
                
                for item in roomsList:
                        print(f"Szoba száma: {item.roomNumber} felszereltsége: {item.equipment} ára: {item.price}$")
                for item in reservationList:
                        print(f"Foglalás száma: {item.reservNumber} név: {item.name} email: {item.email} szoba szám: {item.roomNumber} péz: {item.pay}")
        else:
                print("Nem megfelelő formátum! \n")
                return menu()
                
   

       
def Main():
        cls()
        banner()
        factory()
        menu()

Main()
print("")
 
#region banner
def banner():
        cls()
        print(" "* 80, r'  _   _       _       _  ')
        print(" "* 80, r' | | | | ___ | |_ ___| | ')
        print(" "* 80, r' | |_| |/ _ \| __/ _ \ | ')
        print(" "* 80, r' |  _  | (_) | ||  __/ | ')
        print(" "* 80, r' |_| |_|\___/ \__\___|_| ')
        # print (" |", " "*185, "|") # üres sor széle elemekkel
        print (" /", "-"*184, r'\ ')
        print(" |", " "*184, "|")
        print("{:<80} {:<105} {:<3}".format(" | ","Válasszon azalábbiak közül"," | "))
        print(" |", "-"*184, "|")
        print(" |", " "*184, "|")
        print("{:<80} {:<105} {:<3}".format(" | ","Szoba foglaláshoz: [1]"," | "))
        print("{:<80} {:<105} {:<3}".format(" | ","Szoba foglalás lemondásához: [2]"," | "))
        print("{:<80} {:<105} {:<3}".format(" | ","Foglat szobák listája: [3]"," | "))
        print("{:<80} {:<105} {:<3}".format(" | ","Foglalások listázása: [4]"," | "))
        print("{:<80} {:<105} {:<3}".format(" | ","Kilépés: [0]"," | "))
        print(" |", " "*184, "|")
        print(" |", "-"*184, "|")
        
#endregion 

#region console clear
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
#endregion

#region Classes
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
                                self.bedRoom = "Egyszobás"        
                                
                
        class twoBedRoom:
                def __init__(self):
                       self.roomInfo = self.roomInfo()
        
                class roomInfo:
                        def __init__(self, roomNumber, equipment, price):
                                self.roomNumber = roomNumber
                                self.equipment = equipment       
                                self.price = price*2*(equipment/2)
                                self.bedRoom = "Kétszobás"      
                                
        
class reservation:
        def __init__(self, reservNumber, name, email, roomNumber, date, pay):
                self.reservNumber = reservNumber
                self.name = name
                self.email = email
                self.roomNumber = roomNumber
                self.date = date
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
        
        rolls = []
        def validatedReservation():
                while True:
                        tempRoom = random.randint(1,roomNumCount)
                        if tempRoom not in rolls:
                                rolls.append(tempRoom)
                                
                                tempPrice = 0
                                for item in roomsList:
                                        if tempRoom == item.roomNumber:
                                               tempPrice = item.price
                                return tempRoom, tempPrice
        def dateGenerator():
                day = random.randint(1,31)
                month = random.randint(5,12)
                date = "2024-"+str(month)+"-"+str(day)
                return date
                        
                        
        #Szobák legenerálása
        roomNumCount = 0
        for item in range(random.randint(5,8)):
             roomNumCount += 1
             roomsList.append(Hotel.oneBedRoom.roomInfo(roomNumCount, random.randint(1,10), 10))
             roomNumCount += 1
             roomsList.append(Hotel.twoBedRoom.roomInfo(roomNumCount, random.randint(1,10), 10))
        
        #random foglalások legenrálása
        reservNumCount = 0
        for item in range(random.randint(5,8)):
                reservNumCount += 1
                tempnameList = personGenerator()
                temproomList = validatedReservation()
                        
                reservationList.append(reservation(reservNumCount, tempnameList[0], tempnameList[1], temproomList[0] , dateGenerator() , temproomList[1])) #innen folyt kov ranndom.randit csere ellenorzesre h van e szoba szam
#endregion         

def reservedListings():
        banner()
        print("{:<79} {:<106} {:<3}".format(" | ","Folgalt szobákat választotta"," | "))
        print (" |", "-"*184, "|")
        print("{:<3} {:<30} {:<30} {:<30} {:<30} {:<31}{:<27} {:<3}".format(" | ","Foglalás Száma", "Név", "Email cím", "Szobaszám", "Dátum","Fizetendő összeg"," | "))
        print (" |", "-"*184, "|")
        for item in reservationList:       
                print("{:<3} {:<30} {:<30} {:<30} {:<30} {:<30} {:<27} {:<3}".format(f" | ",f"{item.reservNumber}", f"{item.name}", f"{item.email}", f"{item.roomNumber}",f"{item.date}", f"{item.pay} $"," | "))   
        x = ' \c'
        print(x.replace('c',""),"-"*184, "/")

def roomListing():
        banner()
        print("{:<79} {:<106} {:<3}".format(" | ","Szobák listázását választotta"," | "))
        print (" |", "-"*184, "|")
        print("{:<3} {:<45} {:<45} {:<45} {:<44} {:<3}".format(" | ","Szoba Szám","Szobák","Felszereltség","Ár"," | "))
        print (" |", "-"*184, "|")
        for item in roomsList:
                print("{:<3} {:<45} {:<45} {:<45} {:<44} {:<3}".format(" | ",f"{item.roomNumber}",f"{item.bedRoom}", f"{item.equipment} / 10", f"{item.price} $", " | "))
        x = ' \c'
        print(x.replace('c',""),"-"*184, "/")

#region Main
def Main():
        banner()
        factory()
        while True:
                selected = int(input())
                
                if selected == 1:
                        print("Szoba foglalást választotta")
                elif selected == 2:
                        print("Szoba foglalás lemondását választotta")   
                elif selected == 3:
                        roomListing()
                elif selected == 4:
                        reservedListings()
                elif selected == 0:
                        break
                else:
                        print("Nem megfelelő formátum! \n")
#endregion 

Main()

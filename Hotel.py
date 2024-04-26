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
         
#region Booking
def booking():
        from datetime import datetime
        from datetime import date
        def refresh():
                banner()
                print("{:<80} {:<105} {:<3}".format(" | ","Foglalást választotta"," | "))
                print (" |", "-"*184, "|")
        
        #region Validation
        def validateName():
                temp = input()
                return temp
        
        def validateEmail():
                try:
                        temp = input()
                        if "@" not in temp:
                                return False, temp
                        else:
                                return True, temp
                except:
                        return False, temp
                
        def validateRoomNumber():
                try:
                        temp = int(input())
                        availableRooms = len(roomsList)
                        if 1 <= temp <= availableRooms:
                                return True, temp
                        else:
                                return False, "outbounderror"
                        
                except ValueError:
                        return False, "interror"
        
        def validateDate(wantedRoom):

                temp = input()
                try:
                        datetime.strptime(temp, "%Y-%m-%d")
                        if datetime.now().strftime('%Y-%m-%d') > temp:
                                return False, "pasterror"
                        for item in reservationList:
                                if item.roomNumber == wantedRoom and temp == item.date:
                                        return False, temp
                        return True, temp
                except ValueError:
                       return False, "formaterror"
        #endregion       
        
        def savebooking():
                price = 0
                for item in roomsList:
                        if book[2] == item.roomNumber:
                                price = item.price
                id = int(len(reservationList))
                # print(book)
                reservationList.append(reservation(id+1,book[0],book[1],book[2],book[3],price))
                print(" |", " "*184, "|")
                print("{:<80} {:<105} {:<3}".format(" | ",f"Sikeres szoba foglalás!"," | "))
                print(" |", "-"*184, "|")
                print("{:<58} {:<127} {:<3}".format(" | ",f"A {book[2]}. Szoba {book[3]}-ai dátummal, {book[0]}-néven lefoglalva"," | "))
                print("{:<80} {:<105} {:<3}".format(" | ",f"Fizetendő összeg: {price} $"," | "))
                print(" |", " "*184, "|")
                x = ' \c'
                print(x.replace('c',""),"-"*184, "/")
                
                
        book = []
        refresh()
#region Nightmare
        def lvl1():
                refresh()
                print("{:<80} {:<105} {:<3}".format(" | ",f"Név: {book[0]} "," | "))
        def lvl2():
                lvl1()
                print("{:<80} {:<105} {:<3}".format(" | ",f"Email: {book[1]} "," | "))
        def lvl3():
                lvl2()
                print("{:<80} {:<105} {:<3}".format(" | ",f"Szoba szám: {book[2]} "," | "))
        def lvl4():
                lvl3()
                print("{:<80} {:<105} {:<3}".format(" | ",f"Dátum: {book[3]} "," | "))
#endregion

        while True: 
                if len(book) != 0:
                        lvl1()
                        if len(book) != 1:
                                lvl2()
                                if len(book) != 2:
                                        lvl3()
                                        if len(book) !=3:
                                                lvl4()
                                                savebooking()
                                                break
                                        else:
                                                print("{:<80} {:<105} {:<3}".format(" | ",f"Dátum: [(YYYY-MM-DD)] "," | "))
                                                array = validateDate(book[2])
                                                while True:
                                                        if array[0] is True:
                                                                book.append(array[1])
                                                                break
                                                        elif array[0] is False and array[1] == "formaterror":
                                                                print("{:<80} {:<105} {:<3}".format(" | ",f"A megadott dátum helytelen! (YYYY-MM-DD)-formátumba adja meg!"," | "))
                                                                print("{:<80} {:<105} {:<3}".format(" | ",f"Nyomj entert az újrapróbáláshoz! "," | "))
                                                                input()
                                                                break 
                                                        elif array[0] is False and array[1] == "pasterror":
                                                                print("{:<80} {:<105} {:<3}".format(" | ",f"A megadott dátum helytelen (Múltbeli)"," | "))
                                                                print("{:<80} {:<105} {:<3}".format(" | ",f"Nyomj entert az újrapróbáláshoz! "," | "))
                                                                input()
                                                                break
                                                        else:
                                                                print("{:<80} {:<105} {:<3}".format(" | ",f"A {book[2]}. szoba már foglalt {array[1]} dátumon! "," | "))
                                                                print("{:<80} {:<105} {:<3}".format(" | ",f"Nyomj entert az újrapróbáláshoz! "," | "))
                                                                input()
                                                                break
                                                
                                else:
                                        print("{:<80} {:<105} {:<3}".format(" | ",f"Szoba szám: [____________] "," | "))
                                        array = validateRoomNumber()
                                        while True:
                                                if array[0] is True:
                                                        book.append(array[1])
                                                        break
                                                elif array[0] is False and array[1] == "outbounderror":
                                                        print("{:<80} {:<105} {:<3}".format(" | ",f"Hibás Szobaszám (1-{array[1]}.ig válasszon) "," | "))
                                                        print("{:<80} {:<105} {:<3}".format(" | ",f"Nyomj entert az újrapróbáláshoz! "," | "))
                                                        input()
                                                        break
                                                elif array[0] is False and array[1] == "interror":
                                                        print("{:<80} {:<105} {:<3}".format(" | ",f"Csak szám érték szerepelhet! "," | "))
                                                        print("{:<80} {:<105} {:<3}".format(" | ",f"Nyomj entert az újrapróbáláshoz! "," | "))
                                                        input()
                                                        break
                                
                        else: 
                                print("{:<80} {:<105} {:<3}".format(" | ",f"Email: [____________] "," | "))
                                array = validateEmail()
                                while True:
                                        if array[0] is True:
                                                book.append(array[1])
                                                break
                                        else:
                                                print("{:<80} {:<105} {:<3}".format(" | ",f"Hibás Formátum! (@-ot tartalmaznia kell!) "," | "))
                                                print("{:<80} {:<105} {:<3}".format(" | ",f"Nyomj entert az újrapróbáláshoz! "," | "))
                                                input()
                                                break
                else:
                        print("{:<80} {:<105} {:<3}".format(" | ",f"Név: [____________] "," | "))
                        book.append(validateName())
#endregion                                         

#region Resignation

def resignation():
        def refresh():
                banner()
                print("{:<80} {:<105} {:<3}".format(" | ",f"A foglalás lemondását választotta!"," | "))
                print (" |", "-"*184, "|")
                print("{:<3} {:<30} {:<30} {:<30} {:<30} {:<31}{:<27} {:<3}".format(" | ","Foglalás Száma", "Név", "Email cím", "Szobaszám", "Dátum","Fizetendő összeg"," | "))
                print (" |", "-"*184, "|")
                for item in reservationList:       
                        print("{:<3} {:<30} {:<30} {:<30} {:<30} {:<30} {:<27} {:<3}".format(f" | ",f"{item.reservNumber}", f"{item.name}", f"{item.email}", f"{item.roomNumber}",f"{item.date}", f"{item.pay} $"," | "))   
                print (" |", "-"*184, "|") 
                print (" |", " "*184, "|")
        def validateInput():
                try:
                        asd = int(input())
                        return True, asd
                
                except ValueError:
                        return False, "format"
        resigNumber = 0
        while True:
                refresh()
                print("{:<70} {:<115} {:<3}".format(" | ",f"Adja meg a sorszámát, a törölni kívánt foglalásnak: [___] "," | "))
                if resigNumber == 0:
                        array = validateInput()
                        while True:
                                refresh()
                                print("{:<70} {:<115} {:<3}".format(" | ",f"Adja meg a sorszámát, a törölni kívánt foglalásnak: [___] "," | "))
                                if array[0] is True:
                                        resigNumber = array[1]
                                        break
                                elif array[1] == "format":
                                        print("{:<88} {:<97} {:<3}".format(" | ",f"Hibás Formátum! "," | "))
                                        print("{:<80} {:<105} {:<3}".format(" | ",f"Nyomj entert az újrapróbáláshoz! "," | "))
                                        input()
                                        break
                else:
                       
                        for i, item in enumerate(reservationList):
                                if item.reservNumber == resigNumber:
                                        del reservationList[i]
                                        refresh()
                                        print("{:<78} {:<107} {:<3}".format(" | ",f"Sikeresen törölte a {i+1}. foglalást!"," | "))
                                        print(" |", " "*184, "|")
                                        x = ' \c'
                                        print(x.replace('c',""),"-"*184, "/")   
                        break                
                              

#endregion

#region Listings
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
#endregion

#region Main
def Main():
        banner()
        factory()
        
        while True:
                try:
                        selected = int(input())
                        if selected == 1:
                                booking()
                        elif selected == 2:
                                resignation() 
                        elif selected == 3:
                                roomListing()
                        elif selected == 4:
                                reservedListings()
                        elif selected == 0:
                                break
                        else:
                                print("Nem megfelelő formátum! \n")
                except:
                        pass
#endregion 


Main()
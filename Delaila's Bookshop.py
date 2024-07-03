#Programming Final Project by Mariam Wael Elkholey 
#ID : 320230093
from abc import ABC , abstractmethod



#Items in the store
class Item(ABC):
    def __init__(self , title , author , price = None ):
        self.title = title
        self.author = author
        self.__price = price #private altribute so that it cannot be changable 
        
        
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def BasicDetails(self):
        print(f"Title : {self.get_title()} ")
        print(f"Author : {self.get_author()} ")
        print(f"Price : {self.get_price()} ")

    @abstractmethod
    def Update(self): 
        pass

    @abstractmethod
    def Display(self):
        pass

class Book(Item):

    def __init__(self , title , author , price , genre , isbn , pages):
        super().__init__(title , author , price )
        self.genre = genre
        self.isbn = isbn 
        self.pages = pages
        self.__discount = 0.1

    def Display(self):
        self.BasicDetails()
        print(f"Genre : {self.genre} ")
        print(f"ISBN : {self.isbn} ")
        print(f"Pages : {self.pages} ")

    def Update(self , title = None , author = None , price = None  ,genre = None ,isbn = None , pages = None   ):
        if title :
            self.title = title
        elif author :
            self.author = author 
        elif price :
            self.set_price(price)
        elif genre :
            self.genre = genre 
        elif isbn :
            self.isbn = isbn 
        print("Updated Succesfully !!") 

class Magazine(Item):
    def __init__(self, title, author, price, issue_number, publication_date, editor):
        super().__init__(title, author, price)
        self.issue_number = issue_number
        self.publication_date = publication_date
        self.editor = editor

    def get_title(self):
        return super().get_title()

    def Display(self):
        self.BasicDetails()
        print(f"issue Number : {self.issue_number} ")
        print(f"Publication Date : {self.publication_date} ")
        print(f"Editor : {self.editor} ")

    def Update(self , title = None, author = None, price = None, issue_number= None, publication_date= None, editor= None):
        if title:
            self.title = title
        elif author :
            self.author = author
        elif price :
            self.set_price(price)
        elif issue_number :
            self.issue_number = issue_number
        elif publication_date :
            self.publication_date = publication_date
        elif editor :
            self.editor = editor
        print("Updated Succesfully !!")
        
class DVD(Item):
    def __init__(self, title, author, price , director, duration, genre):
        super().__init__(title, author, price)
        self.director = director
        self.duration = duration
        self.genre = genre

    def Display(self):
        self.BasicDetails()
        print(f"Director : {self.director} ")
        print(f"Duration : {self.duration} mins ")
        print(f"Genre : {self.genre} ")

    def Update(self,title  = None, author = None, price = None, director =None, duration = None, genre = None):
        if title:
            self.title = title
        elif author :
            self.author = author
        elif price :
            self.set_price(price)
        elif director :
            self.director =director
        elif duration :
            self.duration = duration
        elif genre : 
            self.genre = genre
        print("Updated Succesfully !!")

#People in the system
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def add_book_to_inventory(self, bookstore, book):
        if isinstance(book, Book):
            bookstore.add_item(book)
            print(f"{self.name} added {book.title} to the inventory.")
        else:
            print("Only books can be added to the inventory by employees.")

class Client:
    def __init__(self, name):
        self.name = name

    def search_item(self, bookstore, title):
        items = bookstore.search_by_title(title)
        if items:
            print(f"Items found with title '{title}':")
            for item in items:
                print(f"- {item.title} by {item.author}")
        else:
            print(f"No items found with title '{title}'.")

class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def get_cutomer_name(self):
        return self.customer_name
    
    def add_item(self, item):
        self.items.append(item)
        print(f"{item.title} is add to the cart successfully !")

    def calculate_total(self):
        return sum(item.get_price() for item in self.items)  
    
    def displayItems(self):
        return f"Items : {', '.join(item.title for item in self.items)}"

#Store
class Bookstore:
    def __init__(self):
        self.inventory = []
        self.employees = []
        self.orders = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} has been added to the list of employees.")
    
    def add_item(self, item , item2 = None , item3 = None ,item4 = None):
        self.inventory.append(item )
        self.inventory.append(item2)
        self.inventory.append(item3)
        self.inventory.append(item4)
        #print(f"{item.title} has been added to the inventory.")

    def search_by_title(self, title):
        for item in self.inventory:
            if item.title.lower() == title.lower():
                print("Item exists !")
                x= input("Do you want the Details ? (y / n) ")
                if x.lower() == "y" :
                    print("------- Details --------- ")
                    item.Display()
                    return item
                else:
                    print("Item does not exist !")
                    return item
                    
    def search_by_Author(self, author):
        for item in self.inventory:
            if item.author.lower() == author.lower():
                print("Item exists !")
                x= input("Do you want the Details ? (y / n) ")
                if x.lower() == "y" :
                    print("------- Details --------- ")
                    item.Display()
                    return item
                else:
                    print("Item does not exist !")
                    return item
                
    def search_by_genre(self, genre):
        for item in self.inventory:
            if item.genre.lower() == genre.lower():
                print("Item exists !")
                x= input("Do you want the Details ? (y / n) ")
                if x.lower() == "y" :
                    print("------- Details --------- ")
                    item.Display()
                    return item
                else:
                    print("Item does not exist !")
                    return item        


    def place_order(self, customer_name, order ):
        
        self.orders.append(order)
        print(f"Order placed successfully .")

    def display_orders(self):
        for order in self.orders:
            print(f"Customer: {order.customer_name}")
            print("Items:")
            for item in order.items:
                print(f"- {item.get_title()} (${item.get_price()})")
            print(f"Total: ${order.calculate_total()}")
            
#Intiation 
bookstore = Bookstore()
book1 = Book("Linear Algebra" , "George Thomas" , 80 , "Educational" , 154 , 567)
book2 = Book("Advanced Programming" , "Dr.Mohamed Issa" , 100 , "Educational" , 154 , 660)
harry_potter = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 12.99, "Fantasy", 2234567890, 309)

# Create a Magazine object
mag1 = Magazine("Time", "John F. Kennedy", 5.99, 2023, "Jane Smith", "January")
mag2 = Magazine("National Geographic", "John Doe", 1299, 2022, "Jane Smith", "January")

# Create a DVD object
dvd2 = DVD("Inception", "Christopher Nolan", 14.99, "Thriller", 148, "Sci-Fi")
dvd3 = DVD("The Dark Knight", "Christopher Nolan", 14.99, "Action", 152, "Crime")
bookstore.add_item(book1 , book2 , harry_potter )
bookstore.add_item(mag1 , mag2 , dvd2 , dvd3 )

# Create an Employee object
emp1 = Employee("Alice Smith", "Manager")
emp2 = Employee("Charlie Brown", "Sales")
emp3 = Employee("Mariam Elkholey" , "CEO")


# Create a Client object
client1 = Client("John Doe")
client2 = Client("Sally Smith")
client3 = Client("Mariam Elkholey")


#Create People
def CreateEmployee():
    try:
        name = input("Enter Name : ")
        role = input("Enter your Role : ")
        passcode = int(input("Enter the intended passcode : "))
        if passcode == 1234:
                emp = Employee(name , role)
                return emp 
        else:
            print("Wrong Passcode : Program is Termenating......")
            return 0 
    except ValueError : 
        print("Value Error")
        return 
    
    except Exception as e : 
        print("Unexpected Error happened : " , e)
        return

def CreateClient():
    name = input("Enter Name : ")
    client = Client(name)
    return client

#Create Items

def CreateBook():
    try:
        title = input("Title of the book : ")
        Author = input("The Author: ")
        genre = input ("The Genre : ")
        isbn = input("ISBN : ")
        nop = int(input("Enter the no. of Pages : "))
        price = float(input("Enter Price : "))
        book = Book(title , Author , price ,genre , isbn  , nop )
        book.set_price(price)
        return book
    
    except ValueError : 
            print("Value Error")
            return 
    
    except Exception as e : 
        print("Unexpected Error happened : " , e)
        return

def CreateMagazine():
    try:
        title = input("Title of the Magazine : ")
        author = str(input("The Author : "))
        issue_number = input ("The Issue Number : ")
        publication_date = input("Publication Date : ")
        editor = input("Enter the Editor : ")
        price = float(input("Enter Price : "))
        

        mag = Magazine(title, author, price, issue_number, publication_date, editor)
        mag.set_price(price)
        return mag
    
    except ValueError : 
        print("Value Error")
        return 
    except TypeError:
        print("Type Error") 
    except Exception as e : 
        print("Unexpected Error happened : ", e)

def CreateDVD():
    try:
        title = input("Title of the DVD : ")
        author = str(input("The Author / Singer: "))
        director = input ("The Director : ")
        duration = input("Duration : ")
        genre = input ("The Genre : ")
        price = float(input("Enter Price : "))

        dvd = DVD( title, author, price, director, duration, genre)
        dvd.set_price = price
        return dvd
    except ValueError : 
            print("Value Error")
            return 
    except TypeError:
        print("Type Error") 
    except Exception as e : 
        print("Unexpected Error happened : " , e)
    

#Search
def SearchForanItem():
    print("---Search for an Item ---\n")
    print("1 . Book ")
    print("2 . Magazine")
    print("3 . DVD ")
    y = int(input("Enter your Choice -> "))
    if y == 1:
        print("*"*50)
        print("Search for an Item by title : \n")
        x = input("Enter the title  -> ")
        result = bookstore.search_by_title(x)
        
        

    else:
        print("Invalid Input ")       

def SearchandPrice():## not implemented 
    print("---Search for an Item ---\n")
    print("1 . Book ")
    print("2 . Magazine")
    print("3 . DVD ")
    y = int(input("Enter your Choice -> "))
    if y == 1:
        print("*"*50)
        print("Search for an Item by title : \n")
        x = input("Enter the title of the book -> ")
        result = bookstore.search_by_title(x)
        print("The Price is : " , result.get_price() , " EGP." )


#Return Menus
def Returnifemp():
    print("---- Return ----")
    print("1 . Main Menu")
    print("2 . Employee Menu")
    print("3 . Terminate Program")
    choice = int(input("Enter an Option -> "))
    if choice == 1 :
        clientOrEmployee()
    elif choice == 2 :
        EmployeeList()
    else :
        print("The Program is Terminating .......")
        return

def Returnifclient(client):
    print("---- Return ----")
    print("1 . Main Menu")
    print("2 . Client Menu")
    print("3 . Terminate Program")
    choice = int(input("Enter an Option -> "))
    if choice == 1 :
        clientOrEmployee()
    elif choice == 2 :
        ClientList(client)
    else :
        print("The Program is Terminating .......")
        return

def ReturnToMenu():
    option4 = str(input("Do you want to return to the main menu ? (y/n)"))  
    if option4.lower() == "y":
        clientOrEmployee()
    else :
        print("The Program is Terminating .......")

#Lists
def EmployeeList():
    print("_"*50)
    print("Acessibilities : ")
    print("1 . Add to Inventory ")
    print("2 . Check the Price for an Item ")
    print("3 . Search for an Item ")
    print("4 . View Customer Orders ")
    print("5 . Update an Item ")
    option = int(input("Enter an Option -> "))
    if option == 1 :
        print("\n") 
        print("_"*50)
        print("What do u want to add in the inventory ? : ")
        print("*"*50)
        print("1 . Book ")
        print("2 . Magazine ")
        print("3 . DVD ")
        
        item = int(input("Enter a Number -> "))
        if item == 1 :
            book = CreateBook()
            bookstore.add_item(book)
            print(f"{book.get_title()} by {book.get_author()} is added Succesfully")
            EmployeeList()
            
        elif item == 2:
            mag = CreateMagazine()
            bookstore.add_item(mag)
            print(f"{mag.get_title()} by {mag.author} is added Succesfully")

        elif item == 3:
            dvd = CreateDVD()
            bookstore.add_item(dvd)
            print(f"{dvd.get_title()} by {dvd.get_author()} is added Succesfully")


        else :
            print("Invalid input : Program is terminating ....")
            return
    
    elif option == 2 : 
        x = input("What is the title ? ")
        item =  bookstore.search_by_title(x)
        print("-"*40)
        print("\nThe price is : ",item.get_price() , " EGP .\n")
        print("*"*50)
        Returnifemp()

    elif option == 3:
        x = input("What is the title ? ")
        item =  bookstore.search_by_title(x)
        print("-"*40)
        

    elif option == 4 :
        if bookstore.display_orders() :
            bookstore.display_orders()
        else :
            print("." *50)
            print("No orders to Display ... ")
            Returnifemp()

    elif option == 5 :
        UpdateItem()

def ClientList(client):
    print(f"----- Welcome {client.name} -----\n")
    print("1. Place an Order ")
    print("2. Check Price ")
    print("3. Search for an Item\n")
    print("-"*40)

    ans = int(input("Enter you choice -> "))
    print("_" * 40)
    print("\n")
    if ans == 1:
        print("*" * 50)
        noi = int(input("How many items Do you want to Order ? "))
        order = Order(client)
        while noi >= 1:
            x = input("What is the title of the book ? ")
            item = bookstore.search_by_title(x)
            order.add_item(item)
            print("*" * 50)
            noi = noi - 1
        while True:
            print("1 . Check Out \n2 . See Cart \n3 . Return to Main Menu")
            x = int(input("Enter your Choice -> "))
            if x == 1:
                print("Total is : ", order.calculate_total(), " EGP.")
                bookstore.place_order(client, order)
                Returnifclient(client)
            elif x == 2:
                print(order.displayItems())
                print("Total is : ", order.calculate_total())
                print("-" * 50)
            elif x == 3:
                Returnifclient(client)
            else:
                print("Invalid input : Program is terminating ....")
                return


    elif ans == 2 :
        x = input("What is the title ? ")
        item =  bookstore.search_by_title(x)
        print("-"*40)
        print("\nThe price is : ",item.get_price() , " EGP .\n")
        print("*"*50)
        Returnifclient(client)
    
    elif ans == 3 : 
        #Search for an Item 
        SearchForanItem()
        Returnifclient(client)

    else:
        print("Invalid input : Program is terminating ....")
        return


#Updating Info

#For BOOKS , MAGAZINES & DVDs
def UpdateTitle(item):
    new_title = str(input("Enter the new title : "))
    item.Update(title = new_title)
    option3 = str(input("Do you want to display the new Details ? (y/n)"))
    if option3.lower() == "y":
        item.Display()
        Returnifemp()
    else:
        Returnifemp()

def UpdateAuthor(item):
    new_author = str(input("Enter the new Author : "))
    item.Update(author = new_author)
    option3 = str(input("Do you want to display the new Details ? (y/n)"))
    if option3.lower() == "y":
        item.Display()
        Returnifemp()
        
    else:
        Returnifemp()

def UpdateGenre(item):
    new_genre = str(input("Enter the new Genre : "))
    item.Update(genre = new_genre)
    option3 = str(input("Do you want to display the new Details ? (y/n)"))
    if option3.lower() == "y":
        item.Display()
        Returnifemp()
    else:
        Returnifemp()

def UpdatePrice(item):
    new_price = float(input("Enter the new Price : "))
    item.Update(price = new_price)
    option3 = str(input("Do you want to display the new Details ? (y/n)"))
    if option3.lower() == "y":
        item.Display()
        Returnifemp()
        
    else:
        Returnifemp()

#For Books
def UpdateISNB(item):
    new_isnb = eval(input("Enter the new ISNB : "))
    item.Update(isnb = new_isnb)
    option3 = str(input("Do you want to display the new Details ? (y/n)"))
    if option3.lower() == "y":
        item.Display()
        Returnifemp()
        
    else:
        Returnifemp()

def UpdatePages(item):
    new_pages = int(input("Enter the new Number of Pages : "))
    item.Update(pages = new_pages)
    option3 = str(input("Do you want to display the new Details ? (y/n)"))
    if option3.lower() == "y":
        item.Display()
        Returnifemp()
        
    else:
        Returnifemp()

#For Magazines
def UpdateEditor(item):
    new_editor = str(input("Enter the new Editor : "))
    item.Update(editor = new_editor)
    option3 = str(input("Do you want to display the new Details ? (y/n)"))
    if option3.lower() == "y":
        item.Display()
        Returnifemp()
        
    else:
        Returnifemp()

def UpdateIssueNumber(item):
    new_issue_number = int(input("Enter the new Issue Number : "))
    item.Update(issue_number = new_issue_number )
    option3 = str(input("Do you want to display the new Details ? (y/n)"))
    if option3.lower() == "y":
        item.Display()
        Returnifemp()
        
    else:
        Returnifemp()

def UpdatePublicationDate(item):
    new_publication_date = eval(input("Enter the new Publication Date : "))
    item.Update(publication_date = new_publication_date)
    option3 = str(input("Do you want to display the new Details ? (y/n)"))
    if option3.lower() == "y":
        item.Display()
        Returnifemp()
        
    else:
        Returnifemp()

#For DVDs
def UpdateDirector(item):
    new_director = str(input("Enter the new Director : "))
    item.Update(director = new_director )
    option3 = str(input("Do you want to display the new Details ? (y/n)"))
    if option3.lower() == "y":
        item.Display()
        Returnifemp()
        
    else:
        Returnifemp()

def UpdateDuration(item):
    new_duration = eval(input("Enter the new Duration : "))
    item.Update(duration = new_duration )
    option3 = str(input("Do you want to display the new Details ? (y/n)"))
    if option3.lower() == "y":
        item.Display()
        Returnifemp()
        
    else:
        Returnifemp()

#General Excution Function
def UpdateItem():
    print("\n") 
    print("_"*50)
    print("What do u want to Update ? : ")
    print("*"*50)
    print("1 . Book ")
    print("2 . Magazine ")
    print("3 . DVD ")
    option = int(input("Enter a Number -> "))
    

    if option == 1 :
        x = input("What is the title of the book ? ")
        book =  bookstore.search_by_title(x)
        if book : 
            #title , author , price , genre , isbn , pages
            print("What do u want to Update ? : ")
            print("1. Title")
            print("2. Author")
            print("3. Genre")
            print("4. ISBN ")
            print("5. Number of Pages ")
            print("6. Price")

            option2 = int(input("Enter a Number -> "))

            if option2 == 1 :
                UpdateTitle(book)
            elif option2 == 2 : 
                UpdateAuthor(book)
            elif option2 == 3 :
                UpdateGenre(book)
            elif option2 == 4 :
                UpdateISNB(book)
            elif option2 == 5 :
                UpdatePages(book)
            elif option2 == 6 :
                UpdatePrice(book)

    elif option == 2 :
        x = input("What is the title of the book ? ")
        mag =  bookstore.search_by_title(x)
        if mag : 
            #title, author, price, issue_number, publication_date, editor
            print("What do u want to Update ? : ")
            print("1. Title")
            print("2. Author")
            print("3. Editor")
            print("4. Issue Number ")
            print("5. Publication Date ")
            print("6. Price")
            option2 = int(input("Enter a Number -> "))
            if option2 == 1 :
                UpdateTitle(mag)
            elif option2 == 2 : 
                UpdateAuthor(mag)
            elif option2 == 3 :
                UpdateEditor(mag)
            elif option2 == 4 :
                UpdateIssueNumber(mag)
            elif option2 == 5 :
                UpdatePublicationDate(mag)
            elif option2 == 6 :
                UpdatePrice(mag)
            else : 
                print("Invalid Option")

    elif option == 3 :
        x = input("What is the title of the book ? ")
        dvd =  bookstore.search_by_title(x)
        if dvd : 
            #title, author, price , director, duration, genre
            print("What do u want to Update ? : ")
            print("1. Title")
            print("2. Author")
            print("3. Genre")
            print("4. Director ")
            print("5. Duration ")
            print("6. Price")
            option2 = int(input("Enter a Number -> "))
            if option2 == 1 :
                UpdateTitle(dvd)
            elif option2 == 2 : 
                UpdateAuthor(dvd)
            elif option2 == 3 :
                UpdateGenre(dvd)
            elif option2 == 4 :
                UpdateDirector(dvd)
            elif option2 == 5 :
                UpdateDuration(dvd)
            elif option2 == 6 :
                UpdatePrice(dvd)
    else :
        print("Invalid Option")
         



def clientOrEmployee ():
    print("---- Welcome to Delailia's Bookshop ----")
    x = input("Are you an Employee or a Client ?: ")
    if x.lower() == "employee" :
        try:    
            emp = CreateEmployee()
            if emp :
                bookstore.add_employee(emp)
            else:
                return
        except ValueError : 
            print("Value Error")
            return 
        except TypeError:
            print("Type Error") 
        except Exception as e : 
            print("Unexpected Error happened : " , e)

        EmployeeList()

    elif x.lower() == "client" : 
        client = CreateClient()
        ClientList(client)
                 
 


clientOrEmployee ()
# Last Updated by: Cody 10/2 6:30 PM
from tkinter import *



class Pizza:
    def __init__(self):
        window = Tk()
        window.title("Pizza Shop")
        
       
      


       

        frame1 = Frame(window)
        frame1.pack()
        

        


        Label(frame1, text = "Pizza Shop").grid(row = 1, column = 3, pady = 20)

        frame2 = Frame(window)
        frame2.pack()
        
        #create radio buttons for pizza size
        self.v1 = IntVar()

        Label(frame2, text = "Choose Pizza Size:").grid(row = 1, column = 1, sticky = W)
        
        Radiobutton(frame2, text = "Small",variable = self.v1, value = 1).grid(row = 2, column = 2,sticky = W)

        
        Radiobutton(frame2, text = "Medium",variable = self.v1, value = 2).grid(row = 3, column = 2,sticky = W)

       
        Radiobutton(frame2, text = "Large",variable = self.v1, value = 3).grid(row = 4, column = 2,sticky = W)



        #create radio buttons for crust
        self.v2 = IntVar()

        Label(frame2, text = "Choose Pizza Crust:").grid(row = 1, column = 4)
        
        Radiobutton(frame2, text = "Original",variable = self.v2, value = 1).grid(row = 2,padx = 6, column = 5, sticky = W)

        
        Radiobutton(frame2, text = "Pan",variable = self.v2, value = 2).grid(row = 3,padx = 6, column = 5, sticky = W)

       
        Radiobutton(frame2, text = "Thin",variable = self.v2, value = 3).grid(row = 4,padx = 6, column = 5, sticky = W)


        # create label for checkbutton
        Label(frame2, text = "Choose Toppings:").grid(row = 5,column = 1)




        # create variables and checkbuttons for toppings
        self.pep = IntVar()
        self.pep.set(1)
        Checkbutton(frame2, text = "Pepperoni", variable = self.pep).grid(row = 6, padx = 6,pady = 6,column = 2, sticky = W)
        
        self.sausage = IntVar()
        self.sausage.set(0)
        Checkbutton(frame2, text = "Sausage", variable = self.sausage).grid(row = 6,padx = 6,pady = 6, column = 3, sticky = W)
        
        self.ham = IntVar()
        self.ham.set(0)
        Checkbutton(frame2, text = "Ham", variable = self.ham).grid(row = 6, padx = 6,pady = 6,column = 4, sticky = W)
        
        self.bacon = IntVar()
        self.bacon.set(0)
        Checkbutton(frame2, text = "Bacon", variable = self.bacon).grid(row = 6,padx = 6,pady = 6, column = 5 , sticky = W)
        
        self.peppers = IntVar()
        self.peppers.set(0)
        Checkbutton(frame2, text = "Peppers", variable = self.peppers).grid(row = 7,padx = 6,pady = 6, column = 2, sticky = W)
        
        self.olives = IntVar()
        self.olives.set(0)
        Checkbutton(frame2, text = "Olives", variable = self.olives).grid(row = 7,padx = 6,pady = 6, column = 3, sticky = W)
        
        self.mush = IntVar()
        self.mush.set(1)
        Checkbutton(frame2, text = "Mushrooms", variable = self.mush).grid(row = 7,padx = 6,pady = 6, column = 4, sticky = W)
        
        self.onions = IntVar()
        self.onions.set(0)
        Checkbutton(frame2, text = "Onions", variable = self.onions).grid(row = 7,padx = 6,pady = 6, column =5 , sticky = W)


        # extra items checkboxes

       

        
        # creat label for extra items
        Label(frame2, text = "Extra Items:").grid(row = 9, column = 1,sticky =  W)

        # create checkbuttons for extra items
        self.bread = IntVar()
        self.bread.set(1)
        Checkbutton(frame2, text = "Cheese Bread", variable = self.bread).grid(row = 10, padx = 6,pady = 26,column = 2)
        self.wings = IntVar()
        self.wings.set(1)
        Checkbutton(frame2, text = "Wings", variable = self.wings).grid(row = 10,padx = 6,pady = 26, column = 3)
        self.rolls = IntVar()
        self.rolls.set(1)
        Checkbutton(frame2, text = "Cinnamon Rolls", variable = self.rolls).grid(row = 10,padx = 6,pady = 26, column = 4)



        # create label variable and label
        self.total = StringVar()
        Label(frame2,textvariable = self.total).grid(row = 15,padx = 6,pady = 6, column = 2)
        

        # create calcualtion buttons

        Button(frame2, text = "Get Total", command = self.calcTotal).grid(row = 14,padx = 6,pady = 6, column = 1,sticky = W)

        Label(frame2, text = "Total").grid(row = 14,padx = 6,pady = 6, column = 2)


        

        # create discount button
        Button(frame2, text = "Discount", command = self.calcDiscount).grid(row = 17, pady = 6,padx = 6, column = 1, sticky = W)

        

        
       

        self.discount = StringVar()

      
        Label(frame2, text = "Discounted Total").grid(row = 14,padx = 6,pady = 6, column = 4)
        
        Label(frame2,textvariable = self.discount).grid(row = 15,padx = 6,pady = 6, column = 4)
        
        # create windows loop
        window.mainloop()

       

    def pizzaSize(self):
        SMALL = 7.99
        MEDIUM = 10.99
        LARGE = 14.99
        
        # get pizza size total
        if self.v1.get() == 1:
            size = SMALL
            
        elif self.v1.get() == 2:
            size = MEDIUM

        elif self.v1.get() == 3:
            size = LARGE
        return size
        
 

    
    def pizzaCrust(self):

        # pizza size plus type of crust
        if self.v2.get() == 1:
            crust = 1

        elif self.v2.get() == 2:
            crust = .50

        elif self.v2.get() == 3:
            crust = 0
        return crust
    

    def calcTotal(self):

        # calculation
        total = self.pizzaCrust() + self.pizzaSize()
        self.total.set(format(total))
              
    def calcDiscount(self):
        SENIOR = .10

        total = self.calcTotal()

        discount = total - (total * SENIOR)

        self.discount.set(discount)

           










Pizza()






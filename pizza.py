from tkinter import *



class Pizza:
    def __init__(self):
        window = Tk()
        window.title("Pizza Shop")
        
       
      


       

        frame1 = Frame(window)
        frame1.pack()
        

        


        Label(frame1, text = "Pizza Shop").grid(row = 1, column = 3)

        frame2 = Frame(window)
        frame2.pack()
        
    #create radio buttons for pizza size
        self.v1 = IntVar()

        Label(frame2, text = "Choose Pizza Size:").grid(row = 1, column = 1, sticky = W)
        
        Radiobutton(frame2, text = "Small",variable = self.v1, value = 1).grid(row = 2, column = 2,sticky = E)

        
        Radiobutton(frame2, text = "Medium",variable = self.v1, value = 2).grid(row = 3, column = 2,sticky = E)

       
        Radiobutton(frame2, text = "Large",variable = self.v1, value = 3).grid(row = 4, column = 2,sticky = E)



         #create radio buttons for crust
        self.v2 = IntVar()

        Label(frame2, text = "Choose Pizza Crust:").grid(row = 1, column = 4)
        
        Radiobutton(frame2, text = "Original",variable = self.v2, value = 1).grid(row = 2,padx = 6, column = 5)

        
        Radiobutton(frame2, text = "Pan",variable = self.v2, value = 2).grid(row = 3,padx = 6, column = 5)

       
        Radiobutton(frame2, text = "Thin",variable = self.v2, value = 3).grid(row = 4,padx = 6, column = 5)


        # create label for checkbutton

        Label(frame2, text = "Choose Toppings:").grid(row = 5,column = 1)




        # create variables and checkbuttons for toppings
        self.pep = IntVar()
        self.pep.set(0)
        Checkbutton(frame2, text = "Pepperoni", variable = self.pep).grid(row = 6, padx = 6,pady = 6,column = 2)
        
        self.sausage = IntVar()
        self.sausage.set(0)
        Checkbutton(frame2, text = "Sausage", variable = self.sausage).grid(row = 6,padx = 6,pady = 6, column = 3)
        
        self.ham = IntVar()
        self.ham.set(0)
        Checkbutton(frame2, text = "Ham", variable = self.ham).grid(row = 6, padx = 6,pady = 6,column = 4)
        
        self.bacon = IntVar()
        self.bacon.set(0)
        Checkbutton(frame2, text = "Bacon", variable = self.bacon).grid(row = 6,padx = 6,pady = 6, column = 5)
        
        self.peppers = IntVar()
        self.peppers.set(0)
        Checkbutton(frame2, text = "Peppers", variable = self.peppers).grid(row = 7,padx = 6,pady = 6, column = 2)
        
        self.olives = IntVar()
        self.olives.set(0)
        Checkbutton(frame2, text = "Olives", variable = self.olives).grid(row = 7,padx = 6,pady = 6, column = 3)
        
        self.mush = IntVar()
        self.mush.set(0)
        Checkbutton(frame2, text = "Mushrooms", variable = self.mush).grid(row = 7,padx = 6,pady = 6, column = 4)
        
        self.onions = IntVar()
        self.onions.set(0)
        Checkbutton(frame2, text = "Onions", variable = self.onions).grid(row = 7,padx = 6,pady = 6, column = 5)


        # extra items checkboxes

       

        
        # creat label for extra items
        Label(frame2, text = "Extra Items:").grid(row = 9, column = 1)

        # create checkbuttons for extrA items
        self.bread = IntVar()
        self.bread.set(0)
        Checkbutton(frame2, text = "Cheese Bread", variable = self.bread).grid(row = 10, padx = 6,pady = 6,column = 2)
        self.wings = IntVar()
        self.wings.set(0)
        Checkbutton(frame2, text = "Wings", variable = self.wings).grid(row = 10,padx = 6,pady = 6, column = 3)
        self.rolls = IntVar()
        self.rolls.set(0)
        Checkbutton(frame2, text = "Cinnamon Rolls", variable = self.rolls).grid(row = 10,padx = 6,pady = 6, column = 4)



         # create label variable and label
        self.total = StringVar()
        Label(frame2,textvariable = self.total).grid(row = 15,padx = 6,pady = 6, column = 2)
        

        # create calcualtion buttons

        Button(frame2, text = "Get Total", command = self.calcTotal).grid(row = 14,padx = 6,pady = 6, column = 1,sticky = W)

        Label(frame2, text = "Total").grid(row = 14,padx = 6,pady = 6, column = 2)


        

          # create discount button
        #Button(frame2, text = "Senior Discount", command = self.calcDiscount).grid(row = 17, pady = 6, column = 1, sticky = W)

        

        
       

        

      
        Label(frame2, text = "Discounted Total").grid(row = 14,padx = 6,pady = 6, column = 4)
        
        Label(frame2,textvariable = self.discount).grid(row = 15,padx = 6,pady = 6, column = 4)
        
         # create windows loop
        window.mainloop()


        

    def calcTotal(self):
        SMALL = 7.99
        MEDIUM = 10.99
        LARGE = 14.99
        
          # get pizza size total
        if self.v1.get() == 1:
            total = SMALL
            
        elif self.v1.get() == 2:
            total = MEDIUM

        elif self.v1.get() == 3:
                total = LARGE
        self.total.set(format(total))
       
        
        
                
    def calcDiscount(self):
            return self.discount

            
            
       
       

        











Pizza()
























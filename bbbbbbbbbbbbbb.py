# PROLOG SECTION
# pizza.py
# GUI Pizza Pricing
# November 16th, 2017
# Timothy Weaver, Cody Fenwick, Adam Endres, & Samuel Hatcher
# Unresolved bugs: None

from tkinter import *



class Pizza:
    def __init__(self):
        window = Tk()
        window.title("The Pizza Shop")
        
#---------------------------------------------------------------------------------------------------------------------------------
# frame 1

        frame1 = Frame(window)
        frame1.pack()


        pizzaImage = PhotoImage(file ="image/pizza2.gif")
       

        Label(frame1, image = pizzaImage).grid(row = 1, column = 3)

#---------------------------------------------------------------------------------------------------------------------------------
# frame 2

        frame2 = Frame(window)
        frame2.pack()

#---------------------------------------------------------------------------------------------------------------------------------
# create buttons for pizza size
        
        #create radio buttons for pizza size
        self.v1 = IntVar()
        self.v1.set(1)  # initializing the choice

        Label(frame2, text = "Choose Pizza Size:").grid(row = 1, column = 1, sticky = W)
        
        Radiobutton(frame2, text = "Small  ($7.99)",variable = self.v1, value = 1).grid(row = 2, column = 2,sticky = W)

        

        
        Radiobutton(frame2, text = "Medium  ($10.99)",variable = self.v1, value = 2).grid(row = 3, column = 2,sticky = W)

        

       
        Radiobutton(frame2, text = "Large  ($14.99)",variable = self.v1, value = 3).grid(row = 4, column = 2,sticky = W)

        

#---------------------------------------------------------------------------------------------------------------------------------
# create buttons for crust type

        #create radio buttons for crust
        self.v2 = IntVar()
        self.v2.set(1)  # initializing the choice

        Label(frame2, text = "Choose Pizza Crust:").grid(row = 1, column = 4)
        
        Radiobutton(frame2, text = "Original (+ $1.00)",variable = self.v2, value = 1).grid(row = 2,padx = 6, column = 5, sticky = W)

        

        
        Radiobutton(frame2, text = "Pan  (+$.50)",variable = self.v2, value = 2).grid(row = 3,padx = 6, column = 5, sticky = W)

        

       
        Radiobutton(frame2, text = "Thin",variable = self.v2, value = 3).grid(row = 4,padx = 6, column = 5, sticky = W)

#---------------------------------------------------------------------------------------------------------------------------------
# create pizza toppings checkboxes

        # create label for choose topping
        Label(frame2, text = "Choose Toppings:").grid(row = 5,column = 1)

        # create variables and checkbuttons for toppings
        self.pep = IntVar()
        self.pep.set(0)
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
        self.mush.set(0)
        Checkbutton(frame2, text = "Mushrooms", variable = self.mush).grid(row = 7,padx = 6,pady = 6, column = 4, sticky = W)
        
        self.onions = IntVar()
        self.onions.set(0)
        Checkbutton(frame2, text = "Onions", variable = self.onions).grid(row = 7,padx = 6,pady = 6, column =5 , sticky = W)

#---------------------------------------------------------------------------------------------------------------------------------
# extra items checkboxes
    
       
        # creat label for extra items
        Label(frame2, text = "Extra Items:").grid(row = 9, column = 1,sticky =  E)

        # create checkbuttons for extra items
        self.bread = IntVar()
        self.bread.set(0)
        Checkbutton(frame2, text = "Cheese Bread  ($4.99)", variable = self.bread).grid(row = 10, padx = 6,pady = 26,column = 2)
        self.wings = IntVar()
        self.wings.set(0)
        Checkbutton(frame2, text = "Wings  ($6.99)", variable = self.wings).grid(row = 10,padx = 6,pady = 26, column = 3)
        self.rolls = IntVar()
        self.rolls.set(0)
        Checkbutton(frame2, text = "Cinnamon Rolls  ($5.99)", variable = self.rolls).grid(row = 10,padx = 6,pady = 26, column = 4)



#---------------------------------------------------------------------------------------------------------------------------------
# create labels & textboxes for name, address, & phone number

        # create name label
        Label(frame2, text = "Name:").grid(row = 11, column = 1,padx = 2,pady = 1, sticky = E)

        # create textbox
        self.name = StringVar()
        Entry(frame2, textvariable = self.name).grid(row = 11, column = 2, sticky = W)
        
        # create name label
        Label(frame2, text = "Address:").grid(row = 12, column = 1,padx = 1,pady = 1, sticky = E)

        # create textbox
        self.address = StringVar()
        Entry(frame2, textvariable = self.address).grid(row = 12, column = 2, sticky = W)
        
        # create name label
        Label(frame2, text = "City:").grid(row = 13, column = 1,padx = 1,pady = 1, sticky = E)

        # create textbox
        self.city = StringVar()
        Entry(frame2, textvariable = self.city).grid(row = 13, column = 2, sticky = W)
        
        # create name label
        Label(frame2, text = "State:").grid(row = 14, column = 1,padx = 1,pady = 1, sticky = E)

        # create textbox
        self.state = StringVar()
        Entry(frame2, textvariable = self.state, width = 4).grid(row = 14, column = 2, sticky = W)
        
        # create name label
        Label(frame2, text = "Zip:").grid(row = 15, column = 1,padx = 1,pady = 1, sticky = E)

        # create textbox
        self.zip = StringVar()
        Entry(frame2, textvariable = self.zip, width = 9).grid(row = 15, column = 2, sticky = W)
        
        # create name label
        Label(frame2, text = "Phone:").grid(row = 16, column = 1,padx = 1,pady = 1, sticky = E)

        # create textbox
        self.phone = StringVar()
        Entry(frame2, textvariable = self.phone).grid(row = 16, column = 2, sticky = W)
        
#---------------------------------------------------------------------------------------------------------------------------------
# create summary section
        
         # label for summary
        Label(frame2, text = "Summary").grid(row = 11,column = 4, sticky = E)
        
         # label and variable for total in summary area
        self.total = StringVar()
        self.total.set("$0.00")
        
        Label(frame2, text = "Subtotal").grid(row = 12, column = 4, sticky = W)
        Label(frame2, textvariable = self.total).grid(row = 12, column = 5,sticky = W)

        # label for tax in summary
        self.tax = StringVar()

        Label(frame2, text = "Tax").grid(row = 13, column = 4, sticky = W)
        Label(frame2, textvariable = self.tax).grid(row = 13, column = 5,sticky = W)

        self.plus = StringVar()
        Label(frame2, textvariable = self.plus).grid(row = 13, column = 4, sticky = E)

        # label for discount in summary
        self.difference = StringVar()
        Label(frame2, textvariable = self.difference).grid(row = 14, column = 5, sticky = W)

        self.minus = StringVar()
        Label(frame2, textvariable = self.minus).grid(row = 14, column = 4, sticky = E)
        

        # label for total in summary 
        Label(frame2, text = "Total").grid(row = 15, column = 4, sticky = W)

        # label for new total after discount
        self.discount = StringVar()
        
        Label(frame2, textvariable = self.discount).grid(row = 15, column = 5, sticky = W)

        # creat buttons
        Button(frame2,text = "Clear", command = self.clear).grid(row = 16, column = 3)
        
        # create calcualtion buttons
        Button(frame2,text = "Checkout", command = self.calcTotal).grid(row = 16,padx = 6, pady = 6, column = 4,sticky = W)

        # create discount button
        Button(frame2, text = "Discount", command = self.calcDiscount).grid(row = 16, pady = 6, padx = 6, column = 5, sticky = W)

#--------------------------------------------------------------------------------------------------------------------------------
# create processing functions


        # create windows loop
        window.mainloop()

       

    def calcSize(self):
        # pizza size list prices
        list1 = [7.99, 10.99, 14.99]
        
        # get pizza size total
        if self.v1.get() == 1:
            size = list1[0]
            
        elif self.v1.get() == 2:
            size = list1[1]

        elif self.v1.get() == 3:
            size = list1[2]
        return size

    
    def calcCrust(self):
        # pizza crust list prices
        list2 = [0, .50, 1]
        
        # get pizza crust total
        if self.v2.get() == 1:
            crust = list2[2]

        elif self.v2.get() == 2:
            crust = list2[1]

        elif self.v2.get() == 3:
            crust = list2[0]
        return crust


    def calcToppings(self):
        # pizza Toppings list prices
        list3 = [.25, .50, .75, 1]

        # get pizza topping total
        toppings = 0

        if self.pep.get():
            
            toppings = toppings + list3[2]

        if self.sausage.get():
            toppings = toppings + list3[3]

        if self.ham.get():
            toppings = toppings + list3[2]

        if self.bacon.get():
            toppings = toppings + list3[3]

        if self.peppers.get():
            toppings = toppings + list3[0]

        if self.olives.get():
            toppings = toppings + list3[1]

        if self.mush.get():
            toppings = toppings + list3[1]

        if self.onions.get():
            toppings = toppings + list3[0]

        return toppings


    def calcExtras(self):

        # get extras total
        extra = 0

        if self.bread.get():
            extra = extra + 4.99

        if self.wings.get():
            extra = extra + 6.99

        if self.rolls.get():
            extra = extra + 5.99

        return extra


    def calcTotal(self):

        # total calculation
        total = self.calcCrust() + self.calcSize() + self.calcToppings() + self.calcExtras()
        total = round(total, 2)

        rate = .06

        tax = total * rate

        difference = total + tax

        self.plus.set("+")

        tax = float(round(tax, 2))
        
        discount = float(round(difference,2))

        self.tax.set('${:,.2f}'.format(tax))

        self.total.set('${:,.2f}'.format(total))

        self.discount.set('${:,.2f}'.format(discount))

        self.minus.set("")
        
        self.difference.set("")

              
    def calcDiscount(self):
        amount = .10       

        # calculate discount for senoirs
        discount = float(self.total.get()) - float(self.total.get()) * amount
        discount = float(round(discount, 2))

        
        self.discount.set('${:,.2f}'.format(discount))

        # calculates the differnce so it can display in the label
        difference = float(self.total.get()) * amount

        difference = float(round(difference,2))
        
        self.difference.set('${:,.2f}'.format(difference))

        self.minus.set("-")

    def clear(self):

        self.pep.set(0)
        self.sausage.set(0)
        self.ham.set(0)
        self.bacon.set(0)
        self.peppers.set(0)
        self.olives.set(0)
        self.onions.set(0)
        self.mush.set(0)
        self.bread.set(0)
        self.wings.set(0)
        self.rolls.set(0)
        self.name.set("")
        self.address.set("")
        self.city.set("")
        self.state.set("")
        self.zip.set("")
        self.phone.set("")
        self.total.set(0)
        self.difference.set("")
        self.discount.set("")
        self.minus.set("")
        self.tax.set("")
        
Pizza()

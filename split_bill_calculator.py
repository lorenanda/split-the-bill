from tkinter import *

class BillCalculator: 
  
    def __init__(self): 
  
        window = Tk() 
        window.title("Bill Calculator")
        
        # input fields
        Label(window, text = "How much is the bill?").grid(row = 1,column = 1, sticky = W) 
        Label(window, text = "How many people?").grid(row = 2, column = 1, sticky = W) 
        Label(window, text = "How much % tip?").grid(row = 3, column = 1, sticky = W) 
        Label(window, text = "Bill per person:").grid(row = 4, column = 1, sticky = W) 
  
        # for taking inputs 
        self.billVar = StringVar()  
        Entry(window, textvariable = self.billVar, justify = RIGHT).grid(row = 1, column = 2) 
        
        self.peopleVar = StringVar() 
        Entry(window, textvariable = self.peopleVar, justify = RIGHT).grid(row = 2, column = 2) 
        
        self.tipVar = StringVar() 
        Entry(window, textvariable = self.tipVar, justify = RIGHT).grid(row = 3, column = 2) 
        
        self.splitBillVar = StringVar() 
        lblSplitBill = Label(window, textvariable = self.splitBillVar).grid(row = 4, column = 2, sticky = E) 
          
        # calculate button
        button_calculate = Button(window, text = "Calculate", command = self.calculateBill).grid(row = 6, column = 2, sticky = E)  
        window.mainloop() # Create an event loop 
  
  
    # calculate total payment
    def calculateBill(self): 
        splitBill = self.totalSum(float(self.billVar.get()), float(self.tipVar.get()), int(self.peopleVar.get()))
        self.splitBillVar.set(splitBill) 
  
    def totalSum(self, bill, tip, people):  
        splitBill = round(((bill + ((tip * bill) / 100)) / people), 2)
        return splitBill
        root = Tk() # create the widget 
  
# run the program
BillCalculator() 
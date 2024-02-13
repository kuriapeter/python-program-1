# program to calculate electricity bill
def electricity_bill(units,customerID,customerName)
       bill=charges*units
    if units<=199:
        charges=1.20*units   
    elif units>200 and units<400:
        charges=1.50*units
    elif units>400 and units <600:
        charges=1.80*units
    elif units>=600:
        charges= 2.0*units
           return charges
         customerID=int(input("Enter your ID:"))    
         customerName=int(input("Enter your name:"))  
         units=int(input("Enter units:"))   
 print(bill(customerID,customerName,units))                 
def TicketPriceCalculator(age):
    price=0
    
    if age<=5:
        price=0
    elif 5<age<9:
        price=5
    elif 9<age<15:
        price=10
    elif age>=15:
        price=13


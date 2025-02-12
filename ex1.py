def TicketPriceCalculator(age):
    price=0
    
    if age <= 5:
        price = 0
    elif age >= 6 and age <= 8:  
        price = 5
    elif age >= 9 and age <= 14:
        price = 10
    else:  
        price = 13
    return price

if __name__=="__main__":
    
    age =int(input("enter your age: "))
    price = TicketPriceCalculator(age)
    print(f"Your movie ticket price is: ${price}")


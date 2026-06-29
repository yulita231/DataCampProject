

#define a function named apply_discount.
def apply_discount(price, discount):
    #check if the price and discount are valid numbers
    if not isinstance(price, (int, float)):
        return('The price should be a number')
    #check if the discount is a valid number
    elif not isinstance(discount, (int,float)):
        return('The discount should be a number')
    #check if the price is greater than 0 and the discount is between 0 and 100
    elif price <= 0:
        return('The price should be greater than 0')
    #check if the discount is between 0 and 100
    elif discount < 0 or discount > 100:
        return ('The discount should be between 0 and 100')
    #if all the conditions are met, calculate the discounted price
    else:
        potongan = price * (discount / 100)
        harga_akhir = price - potongan
        return harga_akhir
    
try:
        price=float(input('Enter the price: '))
        discount=float(input('Enter the discount: '))
        last_price=apply_discount(price, discount)
        print(f'The final price after applying the discount is: {last_price}')
        
except ValueError:
        print('Please enter valid numbers for price and discount.')
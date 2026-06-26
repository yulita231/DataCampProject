
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
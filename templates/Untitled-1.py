#lex_auth_012693780491968512136

def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_cnt=no_of_five
    one_cnt=no_of_one
    
    while rupees_to_make > 4 and no_of_five > 0:
         rupees_to_make-=5
         no_of_five-=1
    
    while rupees_to_make > 0 and no_of_one > 0:
         rupees_to_make-=1
         no_of_one-=1

    
    if rupees_to_make > 0:
        return -1
    
    return five_cnt-no_of_five , one_cnt-no_of_one
    

    


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
print(make_amount(100,21,5))
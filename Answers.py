def calculate_discount(price, discount):
    discount_paid = price * discount/100
    price_paid= price-discount_paid
    return price_paid

original_cost = float(input('what was the original price of the item? '))
discount_offered=input("Were you offered any discount? (Yes / No) ").strip() .lower()

if discount_offered == "yes":
    discount_value=float(input('What was the discount offered? '))
    if discount_value > 100:
        print('Discount can\'t be greater than 100%')
    elif discount_value < 20:
        print(f"since the {discount_value}% discount offered doesn't meet the NTSES's minimum threshold,it was not accounted for. You ended up paying the original price.")
    else:
        total_price_paid= calculate_discount(original_cost, discount_value )
        print(f'Since a {discount_value}% discount was offered the total price you paid was : {total_price_paid}')
elif discount_offered == "no":
    print(f"Since no discount was offered; you paid the original price: {original_cost}")
else:
    print("sorry error occured during processing: are you sure your input at first was yes or no if not please try again, Thank you")


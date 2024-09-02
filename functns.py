def calculate_discount(original_price, discount_percent):
    if discount_percent >= 20:
        discount_amount = original_price * (discount_percent / 100)
        final_price = original_price - discount_amount
        return final_price
    else:
        return (original_price)


original_price = float(input(f" please enter original price of item: "))
discount_percentage = float(input(f"Enter discount percentage: "))

final_price = calculate_discount(original_price, discount_percentage)

if final_price == original_price:
    print(f"No discount applied on item: ${original_price:.2f}")
else:
    print(f"Final price after discount: ${final_price:.2f}")
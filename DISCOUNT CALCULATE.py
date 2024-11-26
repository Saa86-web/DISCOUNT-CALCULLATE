def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

def main():
    try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))
        
        final_price = calculate_discount(price, discount_percent)
        
        if discount_percent >= 20:
            print(f"The final price after applying the discount is: {final_price:.2f}")
        else:
            print(f"No discount applied. The original price is: {price:.2f}")
    except ValueError:
        print("Please enter valid numbers for price and discount percentage.")

if __name__ == "__main__":
    main()

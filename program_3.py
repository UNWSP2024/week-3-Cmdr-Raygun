# Title: Shipping Charges
# Author: Andrew Bittner
# Date: 9/13/2024

# Programming Excersize 3-13

# The Fast Freight Shipping Company charges the following rates:

# Weight    	Price Per Pound
# 2 pounds or less   	$1.50
# Over 2 pounds but not more than 6 pounds  	$3.00
# Over 6 pounds but not more than 10 pounds	$4.00
# Over 10 pounds	$4.75
# Write a program which calculates the shipping charge and displays the total.

def weight_conversion(weight):
    # Calculate the shipping charge.
    shippingCost = 0.0
    active = True
    while active:
        weight = (float(input("Please input your package weight, in numeric form (no units): ")))
        if weight >= 0.0:
            if weight <= 2.0:
                shippingCost = 1.5
                active = False
            elif weight <= 6.0:
                shippingCost = 3.0
                active = False
            elif weight  <= 10.0:
                shippingCost = 4.0
                active = False
            elif weight > 10.0:
                shippingCost = 4.75
                active = False
        else:
            print("Invalid input: negative numbers. Please try again.")

    
    return shippingCost

#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    weight = 0.0
    shippingCost = 0.0
    # Get package weight from the user.
    # weight = float(input('Enter the weight of the package: '))
    # Display the shipping charge.
    shippingCost = weight_conversion(weight)
    print ('Shipping charge: $', format(shippingCost, '.2f'))
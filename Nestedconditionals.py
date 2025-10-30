#1.juice shop discount
"""If a customer buys more than 2 bottles of juice:
    if they are Regular customer --> give 15% Discount
    if not --> give 5% Discount
    otherwise, No Discount"""
    
bottles_bought = int(input("Enter how many bottles you bought:"))
bottle_price=100
sub_total=bottles_bought*bottle_price
if bottles_bought > 2:
    customer_type=input("Regular/weekly once:")
    if customer_type == "Regular":
        discount_amount =sub_total*0.15
        print("Discount Applied: 15% (Regular customer & > 2 bottles)")
        print(discount_amount)
        print(f"final_total = {sub_total - discount_amount}")
    else:
        discount_amount =sub_total*0.05
        print("Discount Applied: 5% (Non-regular customer & > 2 bottles)")
        print(discount_amount)
        print(f"final_total = {sub_total - discount_amount}")
else:
    print("Discount Applied: 0% (2 or fewer bottles)")
    print(sub_total)


#2.Fuel check
"""if fuel level is below 25%:
    -if the vehicle type is "car" ->print "Refuel soon at a petrol station"
    -if vehicle is "bike"-> print "Refuel at Nearest pump"
    -Else print "check vehicle type"   """

fuel_level=int(input("Enter your fuel level in the form of percentage:"))
if fuel_level<25:
    vehicle_type=input("Enter your vehicle type:").lower()
    if vehicle_type=="car":
        print("Refuel soon at a petrol station")
    elif vehicle_type=="bike":
        print("Refuel at nearest pump")
    else:
        print("check vehicle type")
else:
    print("Enough fuel to ride")




#3.ScholarShip Eligibility
students_grade=int(input("Enter your grade (1-100):"))
if students_grade>85:
    income=int(input("Enter your family income:"))
    if income<300000:
        print("Eligible for full scholarship")
    elif income>=300000 and income<=600000:
        print("Eligible for Half Scholarship")
    else:
        print("No Scholarship")
else:
    print("No Scholarship")




#4.Shopping Cart Offer
totalcartValue=int(input("How much amount you spend:"))
if totalcartValue>=1000:
    paymentMethod=input("sir card/upi:")
    if paymentMethod=="card":
        card=totalcartValue*0.1
        print(f"sir you get this {card} discount")
    elif paymentMethod=="upi":
        upi=totalcartValue*0.15
        print(f"sir you get this {upi} discount")
else:
    print("No discount")



#5.Restaurant Entry Check
age=int(input("Enter your age:"))
if age>=18:
    vaccinated_status=input("Are you vaccinated[True/False]:")
    if vaccinated_status.lower()=="true":
        print("Allowed to Dine in")
    else:
        print("Takeaway only")
else:
    print("You must atleast 18 to dine here")
#6.Sports TryOut
player_age=int(input("Enter your Age:"))
if player_age>=14 and player_age<=18:
    height=int(input("Enter your height in cm:"))
    if height>160:
        print("Your are eligible")
    else:
        print("Your are not eligible(too short)")
else:
    print("Not Eligible(Age Out Of Range)")

#Bonus challenge
units=int(input("Enter the total units consumed: "))
rate=None
if units < 0:
    print("Error: Units consumed cannot be negative.")
if units < 100:
        print("Free Electricity")
elif units < 300:
    usage_type = input("Enter usage type (Residential or Commercial): ").lower()
    if usage_type == 'residential':
        rate = 5.0  # Rs. 5 per unit for residential
        
    elif usage_type == 'commercial':
        rate = 8.0  # Rs. 8 per unit for commercial
       
    else:
        print(f"Error: Invalid usage type{usage_type}")
else:
    rate = 10.0

if rate is not None:
    print(f"Rate Applied: Rs. {rate:.2f} per unit")
    total_bill = units * rate
    print(f"Total Bill:  Rs. {total_bill:.2f}")

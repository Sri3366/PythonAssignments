#1.Traffic light
light_color = input("Traffic light color(Green/Red/Yellow):").lower()
action = "Go" if light_color == "green" else "Stop"
print(action)

#2.Movie Ticket Based on Age
age=int(input("Enter your age:"))
print("Adult Ticket" if age>=18 else "Child Ticket")

#3.Discount offer
amount_spent=int(input("Enter how much amount you spent:"))
print("You Get a Free Gift" if amount_spent>=500 else "No Gift")

#4.Delivery Fee
Location=input("Are u from Local/Non=Local:").lower()
print("Rs.20 Delivery Fee" if Location=="local" else "Rs.50 Delivery Fee")

#5.Fever Check
temperature=int(input("Enter your Body Temperature:"))
print("High Fever" if temperature>=100 else "Normal")

#6.Time Based Greeting
"""Based on hour of day(24 Hours Format)
   - <12 => "Good Morning"
   - <17 => "Good After Noon"
   - Else:  "Good Evening"   """
time=int(input("Enter the current time now(24hrs format):"))
print("Good Morning" if time<12 else( "Good Afternoon" if time<17 else "Good Evening"))



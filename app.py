print("Welcome to the tip calculator")
total_bill = input("What was the total bill : ")
number_of_people = input("How many people you want to split in : ")
tip_percentage = input("What percentage of tip you like to give : ")
total_bill = int(total_bill)
number_of_people = int(number_of_people)
tip_percentage = int(tip_percentage)
tip = tip_percentage / total_bill * 100
tip = int(tip)
final_bill = total_bill / number_of_people + tip / number_of_people
print("Each person should pay",round(final_bill))
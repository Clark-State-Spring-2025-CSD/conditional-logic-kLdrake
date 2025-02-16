
month = int(input("What month is it (1-2)? "))

if month in [3, 4, 5]:
    season = "Spring"
elif month in [6, 7, 8]:
    season = "Summer"
elif month in [9, 10, 11]:
    season = "Fall"   
else:
    season = "Winter"    

if month == 1:
    M = "January"    
if month == 2:
    M = "February"    
if month == 3:
    M = "March"
if month == 4:
    M = "April"
if month == 5:
    M = "May"    
if month == 6:
    M = "June"
if month == 7:
    M = "July"    
if month == 8:
    M = "August"    
if month == 9:
    M = "September"
if month == 10:
    M = "October"
if month == 11:
    M = "November"    
if month == 12:
    M = "December"    

print(f"The month is {M} and the current season is {season}.")    

#Updated 1 Feb 2025
#Create a program that will ask the user for a number between 1 and 12. You may assume the input is correct.
#After getting the number display which season it is. The ranges are:
#Spring: 3,4,5
#Summer: 6,7,8
#Fall: 9,10,11
#Winter 12,1,2
#Here is a sample output:
#What month is it? (1-12): 2
#The current season is Winter.
#For an extra 2 points, display the month as all. So the output becomes:
#What month is it? (1-12): 2
#The month is February and the current season is Winter.
#Remember to also complete the flowchart. It is strongly advised that you do the flowchart first,
#as this will help you write the code.

Name = str(input("Enter your name: "))
English = int(input("Enter marks for english: "))
Maths = int(input("Enter marks for maths: "))
Science = int(input("Enter marks for science: "))
Geography = int(input("Enter marks for geography: "))                  
History = int(input("Enter marks for history: "))
if English > 100 or Maths > 100 or Science > 100 or Geography > 100 or History > 100:
    print("Invalid input!!")
else:
    Total = English + Maths + Science + Geography + History
    Percentage = (Total / 500) * 100
if Percentage >= 90:
    Grade = "A"
elif Percentage >= 75:
    Grade = "B"
elif Percentage >= 60:
    Grade = "C"
else:
    Grade = "D"
print("Name: ", Name)
print("Total marks: ",Total)
print("Percentage: ", Percentage)
print("Grade: ", Grade)
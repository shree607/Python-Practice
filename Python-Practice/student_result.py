name = str(input("Enter your name: "))
marks = int(input("Enter your marks: "))
if marks > 90:
    print("You scored A grade!!")
elif marks > 80 and marks < 90:
    print("You scored A2 grade!!")
elif marks > 65 and marks < 80:
    print("You scored B grade!!")
elif marks > 40 and marks < 65:
    print("You scored C grade!!")
else:
    print("You have failed in your exams!!")

grade = int(input("What is your grade code? "))
print (grade)

if grade >= 90:
  print("Your grade is A")


elif grade >= 80 and grade <90:
  print("Your grade is B")

elif grade >= 70 and grade <80:
  print("Your grade is C")

elif grade >= 60 and grade <70:
  print("Your grade is D")

else:
  print ("Fail")
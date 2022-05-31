# The input statement always returns a string
name = input("What is your name? ")
print("Hello, " + name)
birth_year = input("What year were you born? ") 
#Convert birth year string into integer with int
age = 2022 - int(birth_year)
print(age)

#other
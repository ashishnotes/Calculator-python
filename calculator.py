while True :
  choice = input("Enter operator (+, -, *, /, %) = ") 
  if choice == "%": 
    k = int(input("Enter your marks = ")) 
    per = k / 500 * 100 
    print("Your percentage =", per) 
  elif choice == "+": 
    a = int(input("Enter first number = ")) 
    b = int(input("Enter second number = ")) 
    print("Sum =", a + b) 
  elif choice == "-": 
    a = int(input("Enter first number = ")) 
    b = int(input("Enter second number = ")) 
    print("Subtraction =", a - b) 
  elif choice == "*": 
    a = int(input("Enter first number = ")) 
    b = int(input("Enter second number = ")) 
    print("Multiplication =", a * b) 
  elif choice == "/": 
    a = int(input("Enter first number = ")) 
    b = int(input("Enter second number = ")) 
    if b != 0: 
      print("Division =", a / b) 
    else: 
      print("Cannot divide by zero") 
  else: 
    print("Wrong input")

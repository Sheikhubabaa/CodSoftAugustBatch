# Function to perform arithmetic operations
def calculate(num1, num2, operator):
     if operator == "+":
          return num1 + num2
     elif operator == "-":
          return num1 - num2
     elif operator == "*":
          return num1 * num2
     elif operator == "/":
          if num2 == 0:
               return "Error: Division by zero"
          return num1 / num2
     elif operator == "%":
          if num2 == 0:
               return "Error : Module by zero"
          return num1 % num2 
     elif operator == "e" or "E":
          exit()
     else:
          return "\nInvalid operator"


# Get user input
while True:
     try:
          num1 = float(input("Enter the first number: "))
          num2 = float(input("Enter the second number: "))
          operator = input("\nEnter the operation\n Press (+) to add\n Press (-) to Subtract\n Press (*) to Multiplie\n Press (/) to Divide\n Press (%) to Module\n Press (e) to Exit :- ")

          # Perform the calculation and display the result
          result = calculate(num1, num2, operator)
          print(f"\nResult: {result}\n")

     except ValueError:
          print("Invalid input. Please enter valid numbers.\n")
     except Exception as e:
          print(f"An error occurred: {e}\n")

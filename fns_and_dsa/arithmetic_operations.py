def perform_operation() :
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation: ")
    match operation:
        case "add":
            return num1 + num2
        case "substract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide" :
            if num2 != 0 :
                return num1 / num2
            else:
                return "Cannot divide by 0"
        case _ :
            "Incorrect input"

result = perform_operation()
print(f"The result is {result}")
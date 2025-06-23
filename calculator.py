def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed!"
    return x / y

def display_menu():
    print("\n" + "="*40)
    print("         CALCULATOR CLI APP")
    print("="*40)
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")
    print("="*40)

def get_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers!")
        return None, None

def main():
    print("Calculator CLI App Starting...")
    print("Welcome to Calculator CLI App!")
    
    while True:
        display_menu()
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            print("\nThank you for using Calculator CLI App!")
            print("Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4']:
            num1, num2 = get_numbers()
            
            if num1 is not None and num2 is not None:
                if choice == '1':
                    result = add(num1, num2)
                    operation = "+"
                elif choice == '2':
                    result = subtract(num1, num2)
                    operation = "-"
                elif choice == '3':
                    result = multiply(num1, num2)
                    operation = "*"
                elif choice == '4':
                    result = divide(num1, num2)
                    operation = "/"
                
                print(f"\nResult: {num1} {operation} {num2} = {result}")
            
            input("\nPress Enter to continue...")
        else:
            print("Invalid choice! Please select 1-5.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
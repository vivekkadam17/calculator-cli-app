Calculator CLI App

A simple command-line calculator application built with Python that supports basic arithmetic operations.

Features

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Error handling for division by zero
- User-friendly menu interface
- Input validation
- Continuous operation until user exits

Requirements

- Python 3.x
- No external libraries required

How to Run

1. Clone this repository:
   
   git clone https://github.com/YOUR_USERNAME/calculator-cli-app.git
   

2. Navigate to the project directory:

   cd calculator-cli-app
   

3. Run the calculator:
   
   python calculator.py
   

 Usage

1. Run the program
2. Select an operation from the menu (1-5)
3. Enter two numbers when prompted
4. View the result
5. Choose to continue or exit (option 5)

Example

```
=========================================
         CALCULATOR CLI APP
=========================================
Select operation:
1. Add (+)
2. Subtract (-)
3. Multiply (*)
4. Divide (/)
5. Exit
=========================================
Enter your choice (1-5): 1
Enter first number: 10
Enter second number: 5

Result: 10.0 + 5.0 = 15.0


 Code Structure

- `add()` - Addition function
- `subtract()` - Subtraction function
- `multiply()` - Multiplication function
- `divide()` - Division function with zero-division handling
- `display_menu()` - Shows the main menu
- `get_numbers()` - Gets user input with validation
- `main()` - Main program loop




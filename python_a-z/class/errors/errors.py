try:
    numerator= int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
else:
    print(f"Result: {result}")
finally:
    print("Execution completed.")
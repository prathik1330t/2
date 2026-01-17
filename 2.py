def arithmetic_operations(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    return add, sub, mul, div

if _name_ == "_main_":
    num1 = 10
    num2 = 5
    print(arithmetic_operations(num1, num2))

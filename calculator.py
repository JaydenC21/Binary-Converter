def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"
    
    binary = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary = str(remainder) + binary
        decimal_num = decimal_num // 2
    
    return binary

def binary_to_decimal(binary_str):
    decimal = 0
    power = 0
    
    for digit in reversed(binary_str):
        if digit == "1":
            decimal += 2 ** power
        power += 1
    
    return decimal

decimal_num = int(input("Please enter a decimal integer."))
binary_str = decimal_to_binary(decimal_num)
print(f"Decimal {decimal_num} to Binary: {binary_str}")

binary_str = input("Please enter an integer in binary.")
decimal_num = binary_to_decimal(binary_str)
print(f"Binary {binary_str} to Decimal: {decimal_num}")

def Roman(s: str) -> int:
    values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    Total = 0
    Last_vaule = 0
    
    for char in reversed(s):
        current_value = values[char]
        
        if current_value < Last_vaule:
            Total -= current_value
        else:
            Total += current_value
        
        Last_vaule = current_value
    
    return Total

Rom = input("Введіть римське число: ")
print(f"Цілочислове значення {Rom} це {Roman(Rom)}")

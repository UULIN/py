import json
with open("./source/numbers.json", 'r') as f_obj:
    numbers = json.load(f_obj)

print(numbers)
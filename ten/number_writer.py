import json
numbers = [2, 3, 4, 5, 6]

with open('./source/numbers.json', 'w') as f_obj:
    json.dump(numbers, f_obj)


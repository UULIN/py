def describe_pet(animal_type, pet_name='dog'):
    """显示宠物的信息"""
    print("\n I have a " + animal_type + ".")
    print("My animal name is " + pet_name)


describe_pet('1')
describe_pet(pet_name="name", animal_type="dog")
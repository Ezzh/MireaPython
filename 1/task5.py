import random

def generate_character():
    names = ['John', 'Jane', 'Bob', 'Alice', 'Charlie', 'Eva', 'Max', 'Lily']
    name = random.choice(names)

    age = random.randint(18, 50)

    classes = ['Warrior', 'Mage', 'Rogue']
    character_class = random.choice(classes)

    traits = ['Strength', 'Perception', 'Endurance', 'Charisma', 'Intelligence', 'Agility', 'Luck']
    characteristics = {trait: random.randint(1, 10) for trait in traits}

    skills = ['Lockpicking', 'Sneak', 'Speech', 'Melee Weapons', 'Science', 'Medicine', 'Explosives']
    num_skills = random.randint(1, len(skills))
    character_skills = random.sample(skills, num_skills)

    character = {
        'Name': name,
        'Age': age,
        'Class': character_class,
        'Characteristics': characteristics,
        'Skills': character_skills
    }

    return character

character = generate_character()
print("Сгенерированный персонаж:")
print(character)

import random

# name

first = ["Aiden", "Jacob", "Ethan", "Ryan", "Matthew", "Jack", "Noah", "Nicholas", "Joshua", "Logan"]
last = [" Smith", " Johnson", "William", " Brown", " Jones"]
final = (random.choice(first) + random.choice(last))
print(final)

# origins

print(("Place of Birth: ") + (random.choice(open("usaStates.txt").readline().split())) + (", USA"))

# age

print(random.randrange(18, 88))

# occupation

job = ["Construction Worker", "Retail Employee", "Teacher", "Unemployed"]
print(random.choice(job))

# physical features

height = ["5'9", "5'10", "5'11", "6'0", "6'1", "6'2", "6'3", "6'4", "6'5"]
print(("\nHeight: ") + random.choice(height))
print(("Weight: ") + str(random.randrange(75, 200)))

eyecolors = ["Red", "Green", "Blue"]
haircolors = ["Black", "Brown", "Blonde"]
hairtypes = ["Long", "Short", "Messy"]
print(str(random.choice(eyecolors)) + (" Eyes"))
print(str(random.choice(haircolors)) + (' & ') + str(random.choice(hairtypes) + (" Hair")))
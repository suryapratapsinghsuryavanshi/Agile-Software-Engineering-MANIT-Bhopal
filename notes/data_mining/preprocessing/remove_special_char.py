import re

# Input Data | Reading from file
data = None
with open("./data.txt", "r", encoding="utf8") as f:
    data = f.read()

if not data:
    print("Data not abilable! Exit")
    exit(0)

# Remove special & Number charector from dataset.

# 1. Remove Sepcial charector
special_pattern = re.compile(r"[^\w\s]")
data_without_special_char = re.sub(special_pattern, '', data)
# print(data_without_special_char)

# 2. Remove Numbers
number_pattern = re.compile(r"\d+")
data_without_number_and_sepcial_char = re.sub(number_pattern, '', data_without_special_char)
print(data_without_number_and_sepcial_char)

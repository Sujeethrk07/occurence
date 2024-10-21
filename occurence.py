name = "sujeet"
for char in set(name): 
    if char.isalpha(): 
        print(f"{char}: {name.count(char)}")
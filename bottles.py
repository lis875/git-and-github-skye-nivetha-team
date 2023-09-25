beverage = "Whiskey"
count = 101

for i in range(100):
    count = count - 1
    print(count, "bottles of", beverage, "on the wall")
    
    if i % 2 == 0:
        print(count, "bottles of", beverage)
        print("Take one down, pass it around,", count - 1, "bottles of ", beverage, " on the wall...")
    else:
        print(count, "bottles of", beverage)
        print("If one of those bottles should happen to fall,", count - 1, "bottles of",beverage, "on the wall...")
    
    print("")

print("No more bottles of ",beverage," on the wall, no more bottles of "+beverage+". We've taken them down and passed them around; now we're drunk and passed out!")

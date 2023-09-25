beverage = "wine"
count = 101
for i in range(100):
    count = count - 1
    print(count, "bottles of", beverage, "on the wall")
    print(count, "bottles of", "wine")
    print("If one of those bottles should happen to fall, ", count - 1, "bottles of beer on the wall...")
    print("")

print("No more bottles of beer on the wall, no more bottles of beer. We've taken them down and passed them around; now we're drunk and passed out!")

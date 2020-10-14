print("How many live cables must I avoid?")
live_cables = int(input())

cables = 0
print()

while (cables < live_cables):
    print("Avoiding...", end="")
    cables = cables + 1
    print("Done!", cables, "cables avoided.")
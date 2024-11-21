with open("miss.txt", "w") as f:
    f.write("junk\na\nb")
with open("miss.txt", "r") as f:
    for line in f.readlines():
        print(line)
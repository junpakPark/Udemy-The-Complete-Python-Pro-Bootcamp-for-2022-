with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("new_thang.txt", mode='a') as file:
    file.write("New thangs (ayy, what?), new thangs (whoo)")

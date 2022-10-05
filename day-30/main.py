# try:
#     file = open("file.txt")
#     file_dict = {"key": "value"}
#     print(file_dict["key"])
# except FileNotFoundError:
#     file = open("file.txt", "w")
#     file.write("Something")
# except KeyError as err_message:
#     print(f"the key {err_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("file was closed")
#     raise TypeError("This is an error that i made up")

height = float(input("Height: "))
weight = int(input("weight: "))

if height > 3.5:
    raise ValueError

bmi = weight / height ** 2
print(bmi)

f = open("test.txt", "w")
f.write("Hello, World!\n")
f.write("This is a test file.\n")
f.close()

f = open("test.txt", "r")
# data = f.read()
data = f.readlines()
print(data)
f.close()


# while True:
#     data = f.readline()
#     print(data)
#     if not data:
#         break


# f = open("test.txt", "a")
# f.write("Appending a new line.\n")
# f.close()

# f = open("test.txt", "r")
# data = f.read()
# print(data)
# f.close()


f= open("test.txt", "w")
f.writelines(['Hello python!\n','Hello java!\n','Hello c++!\n'])
f.close()

f = open("test.txt", "r")
data = f.read()
print(data)
f.close()


# with open("home.txt", "r") as f:
#     f.seek(5)
#     print(f.tell())
#     data = f.read()
#     print(f.tell())
#     print(data)
    
# with open("home.txt", "r+") as f:
#     f.write("Hello, World!\n")
#     f.seek(0)
#     data = f.read()
#     print(data)    


# with open('img.jpg', 'rb') as f:
#     data = f.read()
#     print(data)



# import json

# d = {"name":"Sonali", "age": 25, "city": "Pune"}
# with open("data.json", "w") as f:
#     json.dump(d, f)
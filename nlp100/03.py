string = "Now I need a drink, alcoholic of course, after heavy lectures involving quantum mechanics."
str_list = list(string.split())
str_length = []

for i in str_list:
    if(i[len(i)-1] == "," or i[len(i)-1] == "."):
        str_length.append(len(i) - 1)
    else:
        str_length.append(len(i))

print(str_length)        
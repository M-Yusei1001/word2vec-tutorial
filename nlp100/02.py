str1 = "パトカー"
str2 = "タクシー"
str_comb = ""

for i in range(len(str1)):
    str_comb += str1[i]
    str_comb += str2[i]

print(str_comb)

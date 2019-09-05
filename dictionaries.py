yes = {"1":"10", "2":"20","3":"30"}

yes["4"] = "40"

del yes["4"]

print(yes["1"])

for key, value in dict.items(yes):
       print(key, value)


input1 = input()

if input1 in key:
        print("ja")
else:
        print("nee")





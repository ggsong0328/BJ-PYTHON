import string

nums = input()
arr = []
result = 0
for num in nums:
    if (65 <= ord(num) <= 67):
        arr.append("2")
    elif (68 <= ord(num) <= 70):
        arr.append("3")
    elif (71<= ord(num) <= 73):
        arr.append("4")
    elif (74<= ord(num) <= 76):
        arr.append("5")
    elif (77<= ord(num) <= 79):
        arr.append("6")
    elif (80<= ord(num) <= 83):
        arr.append("7")
    elif (84<= ord(num) <= 86):
        arr.append("8")
    else:
        arr.append("9")

for ar in arr:
    result = result + int(ar) + 1

print(result)

import string

sentence = input()
count = sentence.count(' ')
if (sentence[0] == ' '):
    count = count - 1

if (sentence[-1] == ' '):
    count = count - 1

print(count + 1)

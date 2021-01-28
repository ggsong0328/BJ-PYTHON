import string

croactian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
sentence = input()
count = 0

for croa in croactian:
    if sentence.count(croa) > 0:
        sentence = sentence.replace(croa, "@")
        
count = len(sentence)

print(count)

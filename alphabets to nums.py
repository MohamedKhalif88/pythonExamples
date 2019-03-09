import string

print('write a string of letters here: ')
inputLetter = input('--> ')
list1 = []
list2 = []


def alphabet_position():
    dict1 = {value: (int(key) + 1) for key, value in enumerate(list(string.ascii_lowercase))}
    return " ".join([str(dict1[alp]) for alp in list(inputLetter.lower()) if alp.isalpha()])


result1 = alphabet_position()
print(result1)
print('\n')

for i in result1:
    list1.append(i)
    while True:
        try:
            list1.remove(" ") # removing the space
        except ValueError:
            break
    for x in range(len(list1)):
        list1[x] = int(list1[x])
    sum = 0
    for num in list1:
        sum += num

print(sum)


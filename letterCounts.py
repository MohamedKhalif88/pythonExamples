print('write a mix of letters and digits')
ip = input('--> ')
lc = {'Letters': 0, 'Digits': 0}
for i in ip:
    if i.isalpha():
        lc['Letters'] += 1
    elif i.isnumeric():
        lc['Digits'] += 1

    else:
        pass
print("Letters: ", lc['Letters'])
print("Digits: ", lc['Digits'])
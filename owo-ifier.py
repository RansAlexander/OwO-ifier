import random

uwuified = str()
owolist = ['OwO', 'UwU', 'owo', ';;w;;', '(。O ω O。)', '(ʘωʘ)']
randint = random.randint(0, len(owolist)-1)
owo = owolist[randint]

klinker = ['a', 'e', 'i', 'o', 'u']
medeklinker = ['r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'v', 'b', 'n', 'm']
medeklinkerreverse = ['q']
dictionary = {}

# main loop
while True:
    string = input("UwU-ify: ")
    while True:
        print("How terrible do you want it to be?")
        print("Terrible: 1")
        print("Hell: 2")
        print("Make it stop: 3")
        terribleness = int(input())
        if terribleness == 1 or terribleness == 2 or terribleness == 3:
            break
        else:
            print('Please select 1 or 2')
    if terribleness == 3:
        break

    # dict loop to owo-ify some stuff
    for x in klinker:
        for i in medeklinker:
            dictionary.update({x + i: x + 'w' + i})
            dictionary.update({i + x: i + 'w' + x})
            dictionary.update({x.upper() + i: x.upper() + 'w' + i})
            dictionary.update({i.upper() + x: i.upper() + 'w' + x})
        for i in medeklinkerreverse:
            dictionary.update({x + i: x + i + 'w'})
            dictionary.update({x.upper() + i: x.upper() + i + 'w'})

    # main owo-ifier
    uwuified = string
    uwuified = uwuified.replace('r', 'w')
    uwuified = uwuified.replace('l', 'w')
    for x in uwuified:
        if x in ['.', '!']:
            uwuified = uwuified.replace(x, ' ' + owo + x)
            randint = random.randint(0, len(owolist) - 1)
            owo = owolist[randint]

    # loop to owo-ify it even worse
    if terribleness == 2:
        for x in dictionary:
            uwuified = uwuified.replace(x, dictionary.get(x))

    print(uwuified)
    uwuified = ''

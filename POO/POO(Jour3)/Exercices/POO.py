import copy

Liste=[1, 2, 3]
Liste2=[4, 5]

Liste.append(Liste2)

#Liste3=copy.copy(Liste)

Liste3=copy.deepcopy(Liste)

Liste2.append(6)

print(Liste3)
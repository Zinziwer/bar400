## Бар! А сделай на питоне ту же фигню с массивом и тройками, что ты делал на Java.
from random import randint

arrrr = []
arrrr400 =[]
arrrr500 =[]
for i in range(0, 15):
    arrrr.append(randint(0, 3))


print(arrrr)
left = 0
right = len(arrrr) - 1
counter = 1
while right > left:
    # if arrrr[left] == 3 and arrrr[right] != 3:
    #     (arrrr[left], arrrr[right]) = (arrrr[right], arrrr[left])
    #     arrrr400.append(left)
    #     arrrr500.append(right)
    #     left += 1
    #     right -= 1
    # elif arrrr[left] == 3 and arrrr[right] == 3:
    #     right -= 1
    # elif arrrr[left] != 3 and arrrr[right] == 3:
    #     right -= 1
    #     left += 1
    # else:
    #     left += 1

    if arrrr[right] == 3:
        right -= 1
    if arrrr[left] != 3:
        left += 1
    if arrrr[left] == 3 and arrrr[right] != 3:
        (arrrr[left], arrrr[right]) = (arrrr[right], arrrr[left])
        left += 1
        right -= 1

print(arrrr)

ObstList = open(r"Commerce-Repository\apps\product\Obst.txt").readlines()
NewObstList = []

for obst in ObstList:
    if len(obst) == 2:
        ObstList.remove(obst)
    NewObstList.append(obst.replace("\n", ""))

for obst in NewObstList:
    if obst == '':
        NewObstList.remove(obst)

print(NewObstList)
    



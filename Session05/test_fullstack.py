map_sokoban = {
    "size_x":5,
    "size_y":5
}

enemies = [
    {"x": 3, "y": 4},
    {"x": 1, "y": 2}
]
enemies_left = [
    {"x": 3, "y": 4},
    {"x": 1, "y": 2}
]

playing = True
targets = []
live = 5 
while playing:
    if len(enemies_left) == 0:
        print("You won")
        playing = False
    elif live == 0:
        print("No live no play")
        playing = False
    else:         
        # input
        target = dict()  
        user_input = input("Enter your target: ")  
        value1, value2 = user_input.split(" ")   
        target["x"] = int(value2) + 1
        target["y"] = int(value1) + 1
        if target in targets:
            print("Bắn vào đây rồi nhé. Bắn lại đi")
        elif target["x"] < 5 and target["y"] < 5:
            targets.append(target)
            # print(targets)
            
            # vẽ map
            for y in range (map_sokoban["size_y"]):
                for x in range (map_sokoban["size_x"]):
                    enemy_is_here = False
                    for enemy in enemies:
                        if (enemy["x"] == x and enemy["y"] == y):
                            enemy_is_here = True

                    target_is_here = False
                    for tar in targets:
                        if (tar["x"] == x and tar["y"] == y):
                            target_is_here = True
            
                    if (enemy_is_here == True and target_is_here == True):
                        print("o", end=" ")
                    elif (enemy_is_here == False and target_is_here == True):
                        print("x", end=" ")
                    elif x == 0 and y == 0 :
                        print(" ", end=" ")
                    elif x == 0:
                        print(y - 1, end=" ")
                    elif y == 0:
                        print(x - 1, end=" ")
                    else:
                        print("-", end=" ")
                print()
            
            # check hit
            if target in enemies:
                print("You hit")
                if target in enemies_left:
                    enemies_left.remove(target)
            else:
                print("You missed")
            
            
            
            # check around
            targets_around = []
            for a in range(target["y"]-1,target["y"]+2):
                for b in range(target["x"]-1,target["x"]+2):
                    if (a != target["y"] or b != target["x"]):
                        targets_around.append({"x": b, "y": a})
            around = 0
            for enemy in enemies_left:
                if enemy in targets_around:
                    around += 1
            print(around, "enemy(s) around")

            # check live
            live -= 1
            print(live, "rockets left") 

            # check enemy left
            left = len(enemies_left)
            print(left, "enemy(s) left")
        else:
            print("Bắn ra ngoài bản đồ rồi. Bắn lại đi")
        

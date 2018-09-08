map_sokoban = {
    "size_x":5,
    "size_y":5
}

enemies = [
    {"x": 3, "y": 4},
    {"x": 1, "y": 2}
]
enemies_hit = []
playing = True
targets = []
live = 5 
while playing:
    win =  all(elem in targets  for elem in enemies)
    if win:
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
                if target not in enemies_hit:
                    enemies_hit.append(target)
            else:
                print("You missed")
            
            
            
            # check around
            targets_around = []
            for a in range(target["y"]-1,target["y"]+2):
                for b in range(target["x"]-1,target["x"]+2):
                    if (a != target["y"] or b != target["x"]):
                        if {"x": b, "y": a} not in enemies_hit:
                            targets_around.append({"x": b, "y": a})
            # print("targets_around:",targets_around)
            result =  any(elem in targets_around  for elem in enemies)
            result2 = all(elem in targets_around  for elem in enemies)
            if result2:
                print("2 enemy(s) around")
            elif result:
                print("1 enemy(s) around")
            else :
                print("0 enemy(s) around")  

            # check live
            live -= 1
            print(live, "rockets left") 

            # check enemy left
            left = 2 - len(enemies_hit)
            print(left, "enemy(s) left")
        else:
            print("Bắn ra ngoài bản đồ rồi. Bắn lại đi")
        

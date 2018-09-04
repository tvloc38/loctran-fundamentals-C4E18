import os
map_sokoban = {
    "size_x":5,
    "size_y":5
}

enemies = [
    {"x": 3, "y": 4},
    {"x": 1, "y": 2}
]
print(enemies)
playing = True
targets = []
win = 0
live = 5 
while playing:
    if win > 1:
        print("You won!")
        playing = False
    elif live == 0:
        print("No live no play")
        playing = False
    else:
        target = dict()
        
        user_input = input("Enter your target: ")
        
        value1, value2 = user_input.split(" ")

        target["x"] = int(value2)
        target["y"] = int(value1)
        targets.append(target)
        print(targets)
        # os.system ('clear')
        for y in range (map_sokoban["size_y"]):
            for x in range (map_sokoban["size_x"]):
                enemy_is_here = False
                for enemy in enemies:
                    if (enemy["x"] == x and enemy["y"] == y):
                        enemy_is_here = True

                target_is_here = False
                for tar in targets:
                    if (tar["x"] + 1 == x and tar["y"] + 1 == y):
                        target_is_here = True

                if (enemy_is_here == True and target_is_here == True):
                    pic = 'o'
                elif (enemy_is_here == False and target_is_here == True):
                    pic = 'x'
                elif x == 0 and y == 0 :
                    pic = ' '
                elif x == 0:
                    pic = y - 1
                elif y == 0:
                    pic = x - 1
                else:
                    pic = '-'
                print (pic, end=' ')
            print()
        live -= 1
        for enemy in enemies:
            if (enemy["x"] == target["x"] + 1 and enemy["y"] == target["y"] + 1):
                win += 1
                print("You hit")
                break;
            else:
                print("You missed")  
                
        
                
        
# for enemy in enemies:
#     if (enemy["x"] == target["x"] and enemy["y"] == target["y"]):
#         print("Hit")
#     else:
#         print("Missed")

# enemy_is_here = False
# for enemy in enemies:
#     if (enemy["x"] == x and enemy["y"] == y):
#         enemy_is_here = True

# target_is_here = False
# if (target["x"] == x and target["y"] == y):
#     target_is_here = True

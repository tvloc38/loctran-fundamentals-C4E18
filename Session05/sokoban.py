ma = {
    "size_x": 5,
    "size_y": 5
}

player = {
    "x": 4,
    "y": 0
}

boxes = [
    {"x": 1 ,"y": 1},
    {"x": 2 ,"y": 2}, 
    {"x": 3, "y": 3}
    ]

destination = [
    {"x": 2 ,"y": 1},
    {"x": 3 ,"y": 2}, 
    {"x": 4, "y": 3}
]

loop = True
while loop:
    for y in range(ma["size_y"]):
        for x in range(ma["size_x"]):
            
            box_is_here = False  
            # for b in range(0,len(boxes)):
            #     if (x == boxes[b]["x"] and y == boxes[b]["y"]):
            #         print("B", end="")
            #         box_is_here = True

            for box in boxes:
                if box['x'] == x and box['y'] == y:
                    # print("B", end ="")
                    box_is_here = True

            player_is_here = False
            if (x == player["x"] and y == player["y"]):
                # print("P", end="")
                player_is_here = True

            destination_is_here = False
            for des in destination:
                if des["x"] == x and des["y"] == y:
                    destination_is_here = True
            #check win
            win = True
            for box in boxes: 
                if box not in destination:
                    win = False
            if win:
                print("You win")
                loop = False

            if player_is_here:
                print("P", end="")
            elif box_is_here:
                print("B", end="")
            elif destination_is_here:
                print("D", end="")
            elif player_is_here and box_is_here:
                player_box = True
            else:      
                print("-", end="")
        print()

    ans = input("What's next: ").lower()

    dx = 0
    dy = 0

    if ans == "w":
        dy = -1
    elif ans == "a": 
        dx = -1
    elif ans == "s":
        dy = 1
    elif ans == "d":
        dx = 1
    else:
        loop = False

    if 0 <= player['x'] + dx < ma['size_x'] and 0 <= player['y'] + dy < ma['size_y']:
        player['x'] += dx
        player['y'] += dy 
    for box in boxes:
        if box["x"] == player["x"] and box["y"] == player["y"]:
            if 0 <= box['x'] + dx < ma['size_x'] and 0 <= box['y'] + dy < ma['size_y']:
                box["x"] += dx
                box["y"] += dy


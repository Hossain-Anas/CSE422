import random
import math

def utility(max_val, min_val):
    p = random.choice([0,1])
    val = random.randint(1,10) / 10
    return (strength(max_val) - strength(min_val)  + ((-1)**p) * val)

def strength(x):
    return math.log2(x+1) + (x/10)

def minimax(depth, nodeidx, max_player, val, alpha, beta):
    
    if depth == 0:
        return val[nodeidx]
    
    if max_player:
        best = float('-inf')

        tmp_val = minimax(depth - 1, nodeidx*2, False, val, alpha, beta)
        best = max(best, tmp_val)
        alpha = max(best, alpha)
    
        if alpha >= beta:
            return best
        
        tmp_val = minimax(depth - 1, nodeidx*2 + 1, False, val, alpha, beta)
        best = max(best, tmp_val)
        alpha = max(best, alpha)

        return best
    
    else:

        best = float('inf')

        tmp_val = minimax(depth - 1, nodeidx*2, True, val, alpha, beta)
        best = min(best, tmp_val)
        beta = min(best, beta)
    
        if alpha >= beta:
            return best
        
        tmp_val = minimax(depth - 1, nodeidx*2 + 1, True, val, alpha, beta)
        best = min(best, tmp_val)
        beta = min(best, beta)

        return best


def minimax_mind_control(depth, nodeidx, max_player, val):
    if depth == 0:
        return val[nodeidx]
    
    if max_player:
        left_val = minimax_mind_control(depth-1, nodeidx*2, False, val)
        right_val = minimax_mind_control(depth-1, nodeidx*2 + 1, False, val)

        return max(left_val, right_val)
    
    else:
        left_val = minimax_mind_control(depth-1, nodeidx*2, True, val)
        right_val = minimax_mind_control(depth-1, nodeidx*2 + 1, True, val)

        # return min(left_val, right_val)
        return max(left_val, right_val)




def play_game(game_number, start, p1_st, p2_st):
    
    
    if game_number %2 == 1:
        if start == 0:
            max_val, min_val = p1_st, p2_st
            max_p, min_p = "Magnus Carlsen", "Fabiano Caruana"
        
        else:
            max_val, min_val = p2_st, p1_st
            max_p, min_p = "Fabiano Caruana" , "Magnus Carlsen"
    
    else:
        if start == 0:
            max_val, min_val = p2_st, p1_st
            max_p, min_p =  "Fabiano Caruana", "Magnus Carlsen"
        
        else:
            max_val, min_val = p1_st, p2_st
            max_p, min_p = "Magnus Carlsen", "Fabiano Caruana"


    
    leaf_val = []

    for i in range(32):
        leaf_val.append(utility(max_val, min_val))
    
    res = minimax(5,0,True, leaf_val, float('-inf'), float('inf'))

    if res>0:
        winner = max_p + " (MAX) "
    elif res < 0:
        winner = min_p + " (MIN) "
    
    else:
        winner = "DRAW"
    
    return winner, res


def run_task1():

    start = int(input("Enter starting player for game 1 (0 for Carlsen, 1 for Caruana): "))
    magnus_st = float(input("Enter base strength for Carlsen: "))
    caruana_st = float(input("Enter base strength for Caruana: "))

    magnus_w = 0
    caruana_w = 0
    draws = 0

    win1, val1 = play_game(1, start, magnus_st, caruana_st)
    print(f"Game 1 Winner: {win1} (Utility value: {val1:.2f})")
    if "Magnus Carlsen" in win1:
        magnus_w+=1

    elif "Fabiano Caruana" in win1:
        caruana_w += 1

    else:
        draws +=1


    win2, val2 = play_game(2, start, magnus_st, caruana_st)
    print(f"Game 2 Winner: {win2} (Utility value: {val2:.2f})")
    if "Magnus Carlsen" in win2:
        magnus_w+=1

    elif "Fabiano Caruana" in win2:
        caruana_w += 1

    else:
        draws +=1


    win3, val3 = play_game(3, start, magnus_st, caruana_st)
    print(f"Game 3 Winner: {win3} (Utility value: {val3:.2f})")
    if "Magnus Carlsen" in win3:
        magnus_w+=1

    elif "Fabiano Caruana" in win3:
        caruana_w += 1

    else:
        draws +=1

    win4, val4 = play_game(4, start, magnus_st, caruana_st)
    print(f"Game 4 Winner: {win4} (Utility value: {val4:.2f})")
    if "Magnus Carlsen" in win4:
        magnus_w+=1

    elif "Fabiano Caruana" in win4:
        caruana_w += 1

    else:
        draws +=1

    print(f'''Overall Results:
Magnus Carlsen Wins: {magnus_w}
Fabiano Caruana Wins: {caruana_w}
Draws: {draws}''')

    if magnus_w > caruana_w:
        print("Overall Winner: Magnus Carlsen ")
    elif magnus_w < caruana_w:
        print("Overall Winner: Fabiano Caruana ")
    else:
        print("Overall Winner: Draw")


def run_task2():
    start = int(input("Enter who goes first (0 for Light, 1 for L): "))
    cost = float(input("Enter the cost of using Mind Control: "))

    if start == 0:
        max_player = "Light"
        light_st = float(input("Enter base strength for Light: "))
        l_st = float(input("Enter base strength for L: "))
        
        max_val, min_val = light_st, l_st
    
    else:
        max_player = "L"
        light_st = float(input("Enter base strength for Light: "))
        l_st = float(input("Enter base strength for L: "))
        
        max_val, min_val =  l_st, light_st
    
    leaf_vals = []

    for i in range(32):
        leaf_vals.append(utility(max_val, min_val))
    
    without_mind_control = minimax(5,0,True,leaf_vals, float('-inf'), float('inf'))
    with_mind_control = minimax_mind_control(5,0,True, leaf_vals)

    res = with_mind_control - cost

    print(f'''Minimax value without Mind Control: {without_mind_control:.2f}
Minimax value with Mind Control: {with_mind_control:.2f}
Minimax value with Mind Control after incurring the cost: {res:.2f}''')
    
    if without_mind_control > 0 and res > 0:
        if without_mind_control >= res :
            print(f"{max_player} should NOT use Mind Control as the position is already winning.")
        else:
            print(f"{max_player} should use Mind Control.")
    
    elif without_mind_control <= 0 and res > 0:
        print(f"{max_player} should use Mind Control.")
    
    elif without_mind_control <= 0 and res <= 0:
        print(f"{max_player} should NOT use Mind Control as the position is losing either way.")
    
    elif without_mind_control > 0 and res <= 0:
         print(f"{max_player} should NOT use Mind Control as it backfires.")


        
run_task1()
# run_task2()



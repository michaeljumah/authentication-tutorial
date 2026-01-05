def pick_highest(scores):
    
    highest = 0
    for i, a in enumerate(scores):
        #print(i, a)
        if a > highest:
            highest = a
            
    print ("the highest value is", highest)
    

scores = [12,34,67,96,235,999,543,13,678] 
print(pick_highest(scores))
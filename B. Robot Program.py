def RobotProgram():
    tc=int(input())

    for _ in range(tc):
        
        m, x, k = map(int, input().split())
        ins = input()

        time_to_reach_zero = -1
        curr = x 
    
        for i in range(m):
            if ins[i] == "L":
                curr -= 1
            elif ins[i] == "R":
                curr += 1
            
            if curr == 0:
                time_to_reach_zero = i + 1
                break
        
        if time_to_reach_zero == -1 or time_to_reach_zero > k:
            print(0)
            continue

        count = 1
        remaining_time = k - time_to_reach_zero
        
        curr = 0 
        loopTime = -1

        for i in range(m):
            if ins[i] == "L":
                curr -= 1
            elif ins[i] == "R":
                curr += 1
            
            if curr == 0:
                loopTime = i + 1
                break
        
        if loopTime == -1:
            print(count)

        else:
            loops = remaining_time // loopTime
            count += loops
            print(count)

RobotProgram()
 

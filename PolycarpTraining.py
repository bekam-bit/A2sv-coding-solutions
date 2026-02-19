def polycarp():
    numOfContests=int(input())
    contests=list(map(int, input().split()))

    sorted_contests=sorted(contests)

    days=1

    max_days_to_train=0
    
    for contest in sorted_contests:
        
        if contest >= days:
            max_days_to_train += 1
        
        else:
            continue

        days += 1
    
    print(max_days_to_train)

polycarp()

def countdown(start_time):
    if start_time < 0:
        print("Start must be non-negative!")
        return
    
    print(str(start_time) + " minute countdown")
    for i in range(start_time, -1, -10):
        print(str(i))
    print("Done!")

countdown(60)
print()
countdown(15)
print()
countdown(-4)
print()
countdown(0)

    


    
def fibonacci(max_num):
    prev_num = 0
    curr_num = 1

    while (curr_num <= max_num):
        temp = curr_num
        curr_num += prev_num
        prev_num = temp
    return curr_num
        
assert fibonacci(3) == 5
assert fibonacci(6) == 8
assert fibonacci(-2) == 1
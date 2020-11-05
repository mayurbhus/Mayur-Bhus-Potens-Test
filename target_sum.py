array = [1,2,6,3,9]
target_sum = 13
for i in array:
    for j in array:
        if(i==j):
            break
        else:
            a = i + j
        for k in array:
            if(k==j):
                break
            else:
                b = k + a
            if(b == target_sum):
                print(k,j,i)

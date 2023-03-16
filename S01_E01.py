inpt = input().split()
n, t = int(inpt[0]), int(inpt[1])
arr = [int(x) for x in input().split()]

count = 0
for i in range(n):
    for j in range(i, n):
        sub_arr_sum = sum(arr[i:j+1])
        if sub_arr_sum < t:
            count += 1

print(count)

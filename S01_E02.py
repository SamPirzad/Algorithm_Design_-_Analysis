#inut data
inpt = input().split()
person , day = int(inpt[0]), int(inpt[1])
experience = [int(x) for x in input().split()]
interview = []

for i in range(day):
    row = list(map(int, input().split()))
    interview.append(row)

#calsulate the least differance
def calculate_smallest_difference(arr, i1, i2):
   
    diff = abs(arr[i1] - arr[i2])
    for i in range(i1 , i2):
        if i != i1:
            new_diff = abs(arr[i] - arr[i2])
            if new_diff < diff:
                diff = new_diff
    return diff

#output the differances
for i in range(day):
    smallest_diff = calculate_smallest_difference(experience, interview[i][0]-1, interview[i][1]-1)
    print(smallest_diff)





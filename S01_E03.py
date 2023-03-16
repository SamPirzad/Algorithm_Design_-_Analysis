n = int(input())

# Store the relations in a dictionary for faster lookups
relations = {}
for i in range(n * (n-1) // 2):
    a, b, rel1, rel2 = input().split()
    relations[(int(a), int(b))] = rel1 + rel2

# Store the groups in a list of sets
groups = []
for i in range(1, n+1):
    group_found = False
    for group in groups:
        if i in group:
            group_found = True
            break
    if not group_found:
        group = {i}
        for j in range(i+1, n+1):
            if relations.get((i, j)) == "++":
                group.add(j)
        groups.append(group)

# Assign the + and - signs based on the group size
answer = ""
for i in range(1, n+1):
    count = 0
    for group in groups:
        if i in group:
            count = len(group)
            break
    if count >= (n//2) + 1:
        answer += "+"
    else:
        answer += "-"

print(answer)




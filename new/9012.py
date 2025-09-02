T = int(input())

for _ in range(T):
    s = input().strip()
    stack = []
    valid = True

    for i in s:
        if i == '(':
            stack.append(i)
        
        else:
            if stack:
                stack.pop()
            
            else:
                valid = False
                break

    if not stack and valid :
        print("YES")
    else:
        print("NO")

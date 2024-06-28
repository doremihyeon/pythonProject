while True:
    n = int(input())
    if n == -1:
        break;
    else:
        arr = []
        for i in range(1, n//2+1):
            if n % i == 0:
                arr.append(i)
        if sum(arr) == n: #arr에 있는 요소들의 합
            print(n, '=', end = ' ')
            print(*arr, sep = ' + ') #요소들을 +로 구분
        else:
            print(n, 'is NOT perfect.')
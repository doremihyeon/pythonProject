num = [] #입력 값을 넣어줄 배열을 선언

for i in range(5): #0-4까지 반복하는 반복문 생성
    num.append(int(input())) #num이라는 배열에 입력값들을 넣어줌
num.sort() #정렬함수를 사용해 배열안의 값들을 정렬해줌
print (int(sum(num)/5)) #num에 있는 값들의 합을 5로 나눈 결과값을 출력
print (num[len(num)//2]) #num에 길이를 반으로 나눴을때 그 위치에 있는 값을 출력
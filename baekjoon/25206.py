score={'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
sum=0
sum_score=0
for i in range(20):
    A,B,C=input().split()
    B=float(B)
    if(C=='P'): pass
    else:
        sum+=B
        sum_score+=B*score[C]
print(sum_score/sum)
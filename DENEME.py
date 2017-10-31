
A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
n = A[-1]

List=range(-1,n,2)
i=2
while List[i:]:List=sorted(set(List)-set(List[List[i]::List[i]]));i+=1
print(List[1:n+1])


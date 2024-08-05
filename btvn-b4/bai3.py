mucdohanhphuc=int(0)
a=input("nhap vao n va m :")
a=a.split()
n=int(a[0])
m=int(a[1])
A=[]
for i in range (m):
    A.append(int(input()))
A=set(A)
print("A=",A)

B=[]
for i in range (m):
    B.append(int(input()))
B=set(B)
print("B=",B)
C=[]
for i in range (n):
    C.append(int(input()))
C=set(C)
print("C=",C)
D=A&C
D=list(D)
E=B&C
E=list(E)
print("so diem hanh phuc =",len(D)-len(E))











#find gcd
def gcd_fun(x,y):
    if(x==0):
        return y
    else:
        return gcd_fun(y%x,x)
num = gcd_fun(132,320)
print(num)
##########

#euclid_hcf
def euclid_hcf(a,b):
    while(a>0):
        a,b=b%a,a
    return b

num = euclid_hcf(132,320)
print(num)

#######

#Min value repetition in matrix

m,n=6,8
cons_num=[]
matrix=[
        [2,3,4,5,6,2,4,3],
        [2,3,4,7,6,7,6,2],
        [2,3,5,5,5,5,2,5],
        [2,3,1,1,0,1,3,6],
        [1,1,1,1,9,0,3,5],
        [2,3,1,1,5,1,0,7],
        ]
for i in range(m):
    for j in range(n):
        if(j<n-2):
            if(matrix[i][j]==matrix[i][j+1]==matrix[i][j+2]):
                cons_num.append(matrix[i][j])
        if(i<m-2):
            if(matrix[i][j]==matrix[i+1][j]==matrix[i+2][j]):
                cons_num.append(matrix[i][j])
        if(j<n-2 and i>=2):
            if(matrix[i][j]==matrix[i-1][j+1]==matrix[i-2][j+2]):
                cons_num.append(matrix[i][j])
            
        if(i>=2 and j>=2):
            if(matrix[i][j]==matrix[i-1][j-1]==matrix[i-2][j-2]):
                cons_num.append(matrix[i][j])

if len(matrix)==0:
    print(-1)
else:
    print(cons_num,min(cons_num))
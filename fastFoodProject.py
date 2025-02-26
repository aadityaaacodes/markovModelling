import numpy as np

# first stage matrix
mat1 = {
    "burger" : {
        "burger" : 0.2, 
        "pizza" : 0.6,
        "hotdog" : 0.2
    }, 
    "pizza" : {
        "burger" : 0.3, 
        "pizza" : 0,
        "hotdog" : 0.7
    }, 
    "hotdog" : {
        "burger" : 0.5, 
        "pizza" : 0,
        "hotdog" : 0.5
    }
}

c=0
A = []
temp = []
for i in mat1:
    for k in mat1[i]:
        temp.append(mat1[i][k])
    A.append(temp)
    temp = []

print(A)


mat2 = {
    "burger" : 0.35211, 
        "pizza" : 0.21127,
        "hotdog" : 0.43662
    }

pi =[]
for j in mat2:
    pi.append(mat2[k])

res = np.matmul(pi, np.array(A))
print(res)

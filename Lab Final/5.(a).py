max0 = [
                [20,30,40],
                [50 ,60,70],
                [80 ,90,100]
           ]

max1 = [
                [-1,-2,-3],
                [-4,-5,-6],
                [-7,-8,-9]
           ]

result = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
         ]


for i in range(len(max0)):
   
   for j in range(len(max0[0])):
       result[i][j] = max0[i][j] + max1[i][j]

for r in result:
   print(r)
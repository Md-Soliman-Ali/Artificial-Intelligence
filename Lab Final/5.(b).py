max = [
            [1,2],
            [3,4],
            [5,6]
          ]

result = [
            [0,0,0],
            [0,0,0]
         ]

for i in range(len(max)):
   
   for j in range(len(max[0])):
       result[j][i] = max[i][j]

for r in result:
   print(r)
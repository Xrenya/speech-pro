import pprint

mati = [0, 7, 8, 4, 5, 0, 0]
matj = [1, 5, 6, 9 ,0 ,0 ,0]
mat = [[0] * len(mati) for _ in range(len(mati))]
for i in range(len(mati)):
    for j in range(len(mati)):
        mat[i][j] = abs(mati[j] - matj[i])
pprint.pprint(mat)
for i in range(1, len(mati)):
    mat[0][i] += mat[0][i - 1]

pprint.pprint(mat)
for i in range(1, len(mati)):
    mat[i][0] += mat[i - 1][0]
pprint.pprint(mat)
route = 0
for i in range(1, len(mati)):
    for j in range(1, len(mati)):
        mat[i][j] += min(mat[i - 1][j - 1], mat[i][j - 1], mat[i - 1][j])
        

pprint.pprint(mat)

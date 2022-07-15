magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2],]
         

i = 0
while i < len(magic_square):
    sum = 0
    j = 0
    while j < len(magic_square[i]):
        sum += magic_square[i][j]
        j += 1
    i += 1
    print(sum)

x = 0
while x < len(magic_square):
    s = 0
    y = 0
    while y < len(magic_square[x]):
        s+=magic_square[x][y]
        y+=1
    x+=1
    print(s,end = " ")
print()
if sum == s:
    print("it's magic square")
else:
    print("it's not magic square")
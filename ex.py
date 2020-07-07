row=int(input())
for row in range(1, row+1):
    if  row%2!=0:
        print("*", end=' ')
        for column in range(1, row+1):

            print( str(column),end=' ')
        print(" ")
    else:
        for column in range(row, 0, -1):
            print(column, end=' ')
        print("*")




grid = """         0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15 : X
        --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
 0  |    I   E   R   G   V   Q   H   L   E   N   H   T   N   R   L   D 
 1  |    Z   S   C   B   V   S   R   B   L   V   A   I   M   A   R   G 
 2  |    Y   T   M   B   A   H   C   P   N   D   Y   N   N   R   S   C 
 3  |    L   A   N   Z   S   D   S   Q   H   L   T   Y   D   N   E   C 
 4  |    M   Z   E   W   I   Q   Y   S   F   S   C   V   C   E   K   B 
 5  |    K   G   C   S   A   W   T   H   T   S   C   F   B   O   I   Y 
 6  |    E   E   K   T   Y   X   K   O   T   E   L   F   P   I   Z   S 
 7  |    I   X   E   N   W   V   B   R   F   S   N   L   N   H   F   S 
 8  |    F   H   R   X   U   J   C   T   Y   G   C   Y   R   A   V   G 
 9  |    V   C   C   F   R   X   E   E   S   Z   A   Q   A   H   V   U 
 10 |    M   F   H   Q   K   B   N   N   J   S   F   L   E   D   V   U 
 11 |    T   T   I   M   N   S   S   I   H   I   M   T   E   S   C   I 
 12 |    E   U   E   S   G   J   O   N   Z   P   M   J   W   S   Y   J 
 13 |    W   Y   F   J   J   D   R   G   N   H   M   V   H   H   D   K 
 14 |    Y   Q   T   E   V   L   S   S   H   I   C   Z   Y   V   E   G 
 15 |    S   A   T   X   B   Z   N   Q   K   A   P   U   R   R   O   V 
 ---
  Y 
"""
word = "GALES"
grid = grid.splitlines()
grid = grid[2:]
new_grid = [ [0] * 16 for _ in range(16)]
for i in range(len(grid)):
    grid[i] = grid[i][8:]
    grid[i] = grid[i].replace(" ", "")
    row = grid[i]
    for j in range(len(row)):
        new_grid[i][j] = row[j]

# print(new_grid)
length = len(word)

for i in range(len(new_grid)):
    for j in range(len(new_grid)):
        if (new_grid[i][j] == word[0]):
            # get all strings in 8 directions of the starting letter
            # time + mem complexity gg ... but at least the grid is only a fixed 16 by 16
            string_1 = [""]
            string_2 = [""]
            string_3 = [""]
            string_4 = [""]
            string_5 = [""]
            string_6 = [""]
            string_7 = [""]
            string_8 = [""]
            for x in range(length):
                if i+length <= 15:
                    string_1[0] += new_grid[i+x][j]
                    string_1.append((j, i+x))
                if i+length <= 15 and j+length <=15:
                    string_2[0] += new_grid[i+x][j+x]
                    string_2.append((j+x, i+x))
                if j+length <= 15:
                    string_3[0] += new_grid[i][j+x]
                    string_3.append((j+x, i))
                if i-length >= 0:
                    string_4[0] += new_grid[i-x][j]
                    string_4.append((j, i-x))
                if i-length >= 0 and j-length >= 0:
                    string_5[0] += new_grid[i-x][j-x]
                    string_5.append((j-x, i-x))
                if j-length >= 0:
                    string_6[0] += new_grid[i][j-x]
                    string_6.append((j-x, i))
                if i+length <= 15 and j-length >= 0:
                    string_7[0] += new_grid[i+x][j-x]
                    string_7.append((j-x, i+x))
                if i-length >= 0 and j+length <= 15:
                    string_8[0] += new_grid[i-x][j+x]
                    string_8.append((j+x, i-x))

            array_of_strings = [string_1, string_2, string_3,string_4, string_5, string_6, string_7, string_8]
            for s in array_of_strings:
                if s[0] == word:
                    print(s[1:]) 




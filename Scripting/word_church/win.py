from pwn import *

def solve(length, new_grid):
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
	                	solution = s[1:]
	                	return solution


p = remote("challenge.ctf.games", "31623")

# get rid of outputs until its time to send play
p.recv()
p.recv()

# send play
p.send(b'play')


# get rid of wordsearch #1/30
p.recv()

# get the puzzle and convert to string
res = p.recv()
resStr = res.decode("utf-8")

# separate out target word
resStrSplit = resStr.split('\n')
targetWordWithColon = resStrSplit[len(resStrSplit) - 1]
puzzleStr = resStr[0:len(resStr) - len(targetWordWithColon)]
targetWord = targetWordWithColon.split(":")[0]
print(targetWOrd)

word = targetWord
grid = puzzleStr

grid = grid.splitlines()
grid = grid[2:]
new_grid = [ [0] * 16 for _ in range(16)]
for i in range(len(grid)):
    grid[i] = grid[i][8:]
    grid[i] = grid[i].replace(" ", "")
    row = grid[i]
    for j in range(len(row)):
        new_grid[i][j] = row[j]

length = len(word)
print (solve(length,new_grid))
#Creating the Board 

import random, os

def flattenIndex(row, col):
    return row * 4 + col
    
arr = [x for x in range(16)]
# random.shuffle(arr)

print(arr)
class Tile: 
    def __init__(self,r,c,count,x,y):
        self.r=r
        self.c=c
        self.count=count
        self.x=x
        self.y=y
        self.occupied = True
        self.img = loadImage("images/"+str(arr[self.count])+".png")

    def display(self):
        image(self.img,self.x,self.y)


class Puzzle: 
    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
        
        #adding cells row by row 
        self.board=[]
        self.imgList=[]

    def CreateBoard(self):
        count = 0
        y=0
        for r in range(0,self.rows):
            x=0
            for c in range(0,self.cols):
                self.board.append(Tile(r,c,count,x,y))
                self.imgList.append(self.board[-1].img)
                count+=1
                x+=100
            y+=100
        self.board[-1].occupied = False
        self.board[-1].img = loadImage("images/black.png")
        self.imgList[-1] = self.board[-1].img
    
    def findBlankNeighbor(self, row, col):
        neighbors = [(row-1, col), (row, col-1), (row, col+1), (row+1, col)]
        for (r, c) in neighbors:
            if r in range(4) and c in range(4):
                if self.board[flattenIndex(r, c)].occupied == False:
                    return flattenIndex(r,c)
        return -1
                    
        
    def swapTiles(self, swapA, withB):
        self.board[swapA].occupied = False
        self.board[withB].occupied = True
    
        tempimg = self.board[swapA].img
        self.board[swapA].img = self.board[withB].img
        self.board[withB].img = tempimg
    
         
    
    def display(self):
        for t in self.board:
            t.display()

    def shuffleBoard(self, n=10):
        blank = (self.rows-1, self.cols-1)
        def getNonBlankTileAround(coordinate): # coordinate = (3,5)
            around = [(-1,0),(0,-1),(0,1),(1,0)]
            tiles = []
            for delta in around:
                testTile = r, c = coordinate[0] + delta[0], coordinate[1] + delta[1]
                if 0 <= r and r < self.rows and 0 <= c and c < self.cols:
                    if self.board[flattenIndex(r, c)].occupied:
                        tiles.append(testTile)
            return random.choice(tiles) # 8
        for i in range(n):
            target = getNonBlankTileAround(blank)
            self.swapTiles(flattenIndex(*target), flattenIndex(*blank))
            blank = target
    
    def ifgameover(self):
        for i in range(self.rows * self.cols):
            if self.imgList[i] != self.board[i].img:
                return False 
        return True 
                    
p = Puzzle(4,4)

def setup():
    size(400, 400)
    background(0)
    p.CreateBoard()
    p.shuffleBoard(n=10)

def draw():
    p.display()

def mouseClicked():
    global p
    a = flattenIndex(mouseY // 100, mouseX //100)
    index = p.findBlankNeighbor(mouseY // 100, mouseX // 100)
    if index >= 0:
        print("Going to swap " + str(a) + " with " + str(index))
        p.swapTiles(a, index)
        p.display()

    if p.ifgameover():
        print("game over! you have won")
        p = Puzzle(4,4)
        p.CreateBoard()
        p.shuffleBoard(n=10)

#Win Condition 

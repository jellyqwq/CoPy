class ClassName:
    def __init__(self) -> None:
        self.dirs = [
            lambda x,y:(x+1,y),
            lambda x,y:(x-1,y),
            lambda x,y:(x,y+1),
            lambda x,y:(x,y-1)
        ]

    def dfs(self, target,grid,i,j):
        tmp=[]
        tmp.append((i,j))
        n=1
        while n <= len(target)-1:
            curnode = tmp[-1]
            for dir in self.dirs :
                nextnode = dir(curnode[0],curnode[1])
                if 0<=nextnode[0]<len(grid) and 0<=nextnode[1]<len(grid[0]):
                    if grid[nextnode[0]][nextnode[1]]== target[n]:
                        tmp.append(nextnode)
                        grid[nextnode[0]][nextnode[1]]=1
                        n+=1
                        break
                else:
                    grid[nextnode[0]][nextnode[1]]=1
                    tmp.pop()
                    if len(tmp)==0:
                        return False
        else:
            return True
        
    def serch(self, grid, target):
        for i in range(len(grid)):
            for j in range(4):
                if grid[i][j] == target[0]:
                    self.dfs(target,grid,i,j)
                    break
     
# grid=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# target="SEE"
grid = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
target = "ABCCED"
ClassNameInstance = ClassName()
print(ClassNameInstance.serch(grid, target))
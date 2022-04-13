
from itertools import product
import copy 
dest = [[0,1],[0,-1],[1,0],[-1,0]]
def makelist(qlist, origingrid):
    _grid = copy.deepcopy(origingrid)
    idx = 0
    for iidx,i in enumerate(_grid):
        for jidx,j in enumerate(i):
            if j == '?':
                _grid[iidx][jidx] = qlist[idx]
                idx += 1
    return _grid

def findtarget(x,y,target,grid):
    if x>len(grid)-1 or y>len(grid[0])-1 or x<0 or y<0 : return
    if grid[x][y] != target:
        return
    else:
        grid[x][y] = ''
        for dx,dy in dest:
            findtarget(x+dx,y+dy,target,grid)




def solution(grid_list):
    aflag,bflag,cflag = True,True,True
    global answer 
    answer = 0
    answer = 0
    numq = 0
    grid = []
    for i in grid_list:
        element = []
        for j in i:
            element.append(j)
            if j == "?":
                numq += 1
        grid.append(element)
    print(grid)
    possibleq = []
    for i in product(['a','b','c'],repeat=numq):
        possibleq.append(i)
    print(possibleq)
    for i in possibleq:
        new_g = []
        new_g = makelist(i, grid[:])
        print("start", new_g)
        aflag,bflag,cflag = True,True,True
        for jdx, j in enumerate(new_g):
            
            print(aflag, bflag, cflag)
            if not (aflag or bflag or cflag):
                break
            for kdx,k in enumerate(j):
                if k == 'a' and aflag:
                    aflag = False
                    findtarget(jdx,kdx,'a',new_g)
                if k == 'b' and bflag:
                    bflag = False
                    findtarget(jdx,kdx,'b',new_g)
                if k == 'c' and cflag:
                    cflag = False
                    findtarget(jdx, kdx, 'c', new_g)
        print("end",new_g)
        answerflag = True
        for j in new_g:
            for k in j:
                if k != '':
                    answerflag = False
                    break
        if answerflag : 
            answer += 1

    print(answer)
    return answer

solution(["??b", "abc", "cc?"])
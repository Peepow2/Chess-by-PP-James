queue = list()
chess = list()
num =  int(0)

def pos(x, y):
    return (x-1) + (y-1)*8
    
def not_out_of_area(x, y):
    x = int(x); y = int(y);
    if(1 <= x <= 8 and 1 <= y <= 8):
        return True
    return False

def input_queue(x, y, n):
    x = int(x); y = int(y); n = int(n);
    if(not_out_of_area(x,y)):
        idx = pos(x, y)
        if(chess[idx] == 0):
           chess[idx] = int(1)
           queue.append([x, y, n])
        
# Driver Code
st, en = [int(e) for e in input().split()]

chess = [0]*65

sx = int((st % 8) + 1);    sy = int((st // 8) + 1);
ex = int((en % 8) + 1);    ey = int((en // 8) + 1);

print(sx, sy);  print(ex, ey)

queue += [[sx, sy, 0]]

while(len(queue) != 0):
    x = int(queue[0][0]); y = int(queue[0][1]);
    n = int(queue[0][2]);
    queue.pop(0)

    if(x == ex and y == ey):
        num  = n
        break;
        
    input_queue(x + 1, y - 2, n + 1) # 1
    input_queue(x - 1, y - 2, n + 1) # 2
    input_queue(x + 1, y + 2, n + 1) # 3
    input_queue(x - 1, y + 2, n + 1) # 4
    input_queue(x - 2, y + 1, n + 1) # 5
    input_queue(x - 2, y - 1, n + 1) # 6
    input_queue(x + 2, y + 1, n + 1) # 7
    input_queue(x + 2, y - 1, n + 1) # 8
    
print(num)

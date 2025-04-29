import random
harita = []
x = 0
y = 0
p = 0
konum = x
evet = 'evet'

for i in range(10):
    satir = []
    for j in range(10):
        satir.append('.')
    harita.append(satir)
for i in range(10):
        random_sutun = random.randint(1 , 9)
        harita[i][random_sutun] = "B"
harita[x][y] = 'R'
for satir in harita:
    print(' '.join(satir))

def move(x , y , p):
    while evet == 'evet':
        print('puaniniz' , p ,)
        if p == 10:
            print('game ended!')
            break
        else:
            hamle = input('nereye gitmek istersiniz?(w , a , s , d , quit)')
            if hamle == 's':
             harita[x][y] = '.'
             x = (x + 1)
             if harita[x][y] == 'B':
                p = (p+1)
                harita[x][y] = '.'
             else:
                harita[x][y] = '.'
             harita[x][y] = 'R'
                
            if hamle == 'a':
             harita[x][y] = '.'
             y = (y - 1)
             if harita[x][y] == 'B':
                p = (p+1)
                harita[x][y] = '.'
             else:
                harita[x][y] = '.'
             harita[x][y] = 'R'
             

            if hamle == 'd':
             harita[x][y] = '.'
             y = (y + 1)
             if harita[x][y] == 'B':
                p = (p+1)
                harita[x][y] = '.'
             else:
                harita[x][y] = '.'
             harita[x][y] = 'R'
             

            if hamle == 'w':
             harita[x][y] = '.'
             x = (x - 1)
             if harita[x][y] == 'B':
                p = (p+1)
                harita[x][y] = '.'
             else:
                harita[x][y] = '.'
             harita[x][y] = 'R'

            for satir in harita:
                print(' '.join(satir))
            
            if hamle == 'quit':
                break
            if p == 10:
                print('game ended!')
                break
    return p          
p = move(x , y , p)
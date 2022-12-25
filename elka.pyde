x = 500
v = 430
c = 360
b = 290
def setup():
    size(400,600)
def draw():
    background(0, 255, 255)
    global x,c,v,b
    push()
    fill(0, 128, 0)
    triangle(50,x,150,x,100,v)
    triangle(50,v,150,v,100,c)
    triangle(50,c,150,c,100,b)
    pop()
    push()
    fill(139, 69, 19)
    rect(85,x,30,10000)
    pop()
    ellipse(240,550,100,100)
    ellipse(240,480,75,75)
    ellipse(240,430,50,50)
    line(220,440,250,440)
    push()
    strokeWeight(15)
    point(225,430)
    point(240,430)
    pop()
    x -= 5
    v -= 5
    c -= 5
    b -= 5

#Graficos simples

x=seq(0,10,.1)
y=sin(x)

plot(x,y,type="lN",col=2)
points(5,0,col=3)
lines(x,y*y,col=4)

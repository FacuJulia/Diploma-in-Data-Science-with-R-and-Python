#ciclos indefinidos

a=100

while(a>10){
  print(a)
  a=a/2
}


a=100
while(TRUE){
  print(a)
  a=a/2
  
  if(a<=10)
    break
}

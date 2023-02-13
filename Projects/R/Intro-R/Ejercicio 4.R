#Ciclos definidos

for(i in 1:5){
  #print(i)
  for(j in 1:3){
    print(i*j)
    if(i==j)
      break
  }
}

s=seq(1,10,3)

for(i in s)
  print(i)

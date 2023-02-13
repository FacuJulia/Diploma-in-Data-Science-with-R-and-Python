#Ejecucion condicional

a=15
if(a>7 & a<16)
{
  print("a entre 7 y 16")
}else{
  print("a fuera de 7 a 16")
}



a=15
if(a>7 || a<16)
{
  print("a mayor que 7 o menor que 16")
}else{
  print("")
}


#Clasificar triangulos

a=4
b=4
c=4

if(a==b & b==c)
{
  print("Equilatero")
}else{
  if(a==b | b==c | c==a)
  {
    print("Isoceles")
  }else{
    print("Escaleno")
  }
}


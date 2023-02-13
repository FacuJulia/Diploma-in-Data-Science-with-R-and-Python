#Ejecucion condicional
#Ciclos definidos
#Ciclos indefinidos 
#Graficos simples
#Funciones estadisticas

m <- matrix(nrow = 3, ncol = 4, 0)
h <- as.data.frame(m)



m[1,1] <- "a"
h[1,1] <- "a"

str(m)
str(h)

h$V1
h$V2
colnames(h)<-c("A","B","C","D")
h$B[3]="B"
h
h$B="X"
h
h$A=c("X","Y","Z")
h
h$A=as.numeric(h$A) #No hay error pero completa con NA similar a NULL

h2=rbind(h,h)
h2
h3=cbind(h,h)
h3
h4=rbind(h3,h3)
h4
write.csv(h4,"borrame.csv")
getwd()
h5=read.csv("borrame.csv")
h5
h5$X=NULL
h5

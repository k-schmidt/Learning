# #########################
# Declaring and Installing Packages 
# #########################
library(tree)
#install.packages('ISLR')
library(ISLR)

# #########################
# Declare Datasets
# #########################

attach(Carseats)

# #########################
# Manipulating Data and Merge
# #########################

High = ifelse(Sales <= 8,"No","Yes")
Carseats = data.frame(Carseats, High)
drops <- c("High.1","High.2")
Carseats[,!(names(Carseats) %in% drops)]

# #########################
# Modeling Decision Tree
# #########################

tree.carseats = tree(High ~ . -Sales, Carseats)
summary(tree.carseats)
plot(tree.carseats)
text(tree.carseats,pretty=0)

tree.carseats

set.seed(2)
train = sample(1:nrow(Carseats), 200)
Carseats.test = Carseats[-train,]
High.test=High[-train]
tree.carseats = tree(High~.-Sales,Carseats,subset=train)
tree.pred=predict(tree.carseats,Carseats.test,type="class")
table(tree.pred,High.test)

set.seed(3)
cv.carseats=cv.tree(tree.carseats,FUN=prune.misclass)
names(cv.carseats)
cv.carseats

par(mfrow=c(1,2))
plot(cv.carseats$size,cv.carseats$dev,type = "b")
plot(cv.carseats$k,cv.carseats$dev, type = 'b')

prune.carseats=prune.misclass(tree.carseats, best =9)
plot(prune.carseats)
text(prune.carseats, pretty = 0)

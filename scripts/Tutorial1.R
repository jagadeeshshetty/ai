
# set working directory and import data files
setwd("E:\\ai\\data\\titanic")
train <- read.csv("train.csv")
test <- read.csv("test.csv")

# Examine structure of dataframe
str(train)

# Look at number of peoples who survived
table(train$Survived)
prop.table(table(train$Survived))






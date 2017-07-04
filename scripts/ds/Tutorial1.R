
# set working directory and import data files
setwd("E:\\Git\\ai\\scripts\\ds")
train <- read.csv("train.csv")
test <- read.csv("test.csv")

# Examine structure of dataframe
str(train)

# Look at number of peoples who survived
table(train$Survived)
prop.table(table(train$Survived))



# Factor is different categories.

# > library(readr)
# > train <- read_csv("E:/Git/ai/data/titanic/train.csv", col_types = cols(Pclass = col_factor(levels = c("1", "2", "3")), Sex = col_factor(levels = c("male", "female")), Survived = col_factor(levels = c("0", "1"))))
# > View(train)





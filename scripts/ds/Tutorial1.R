
# Factor is different categories.

# > library(readr)
# > train <- read_csv("E:/Git/ai/data/titanic/train.csv", col_types = cols(Pclass = col_factor(levels = c("1", "2", "3")), Sex = col_factor(levels = c("male", "female")), Survived = col_factor(levels = c("0", "1"))))
# > View(train)
# > setwd("E:\\Git\\ai\\scripts\\ds")
# > test <- read.csv("test.csv")

# Machine learning code works in three najor parts.
# 1. Reading the data from files. Ex: CSV file.
# 2. Analysis of data.
# 3. Write prediction or classifictaion into new files or new column in db.

# set working directory and import data files
setwd("E:\\Git\\ai\\scripts\\ds")

train <- read.csv("train.csv") 
        or
library(readr)
train <- read_csv("E:/Git/ai/data/titanic/train.csv", col_types = cols(Pclass = col_factor(levels = c("1", "2", "3")), Sex = col_factor(levels = c("male", "female")), Survived = col_factor(levels = c("0", "1"))))

test <- read.csv("test.csv")
View(train)
View(test)

# Examine structure of dataframe
str(train)

# Look at number of peoples who survived
table(train$Survived)
prop.table(table(train$Survived))





#Note:
#  Test data < Train data



  



# set working directory and import data files
setwd("E:\\ai\\data\\titanic")
train <- read.csv("train.csv")
test <- read.csv("test.csv")

# Look at gender patterns
summary(train$Sex)


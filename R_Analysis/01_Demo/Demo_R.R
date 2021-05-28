demo_table <- read.csv(file='demo.csv',check.names=F,stringsAsFactors = F)

library(jsonlite)

demo_table3 <- read.xl('Vehicle_Data.xlsx',check.names = F,stringsAsFactors = F)

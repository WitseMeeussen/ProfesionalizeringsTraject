data("mtcars")

mean(mtcars$mpg)
median(mtcars$mpg)
min(mtcars$mpg)
max(mtcars$mpg)
var(mtcars$mpg)
sd(mtcars$mpg)

s = summary(mtcars)

library(psych)
describe(mtcars)


s = describe(mtcars)

s["gear","max"]

s[c("disp","wt","vs"),c("min","max","sd","mean")]

boxplot(mtcars)

hist(mtcars$mpg, breaks=10)

data(Arthritis)
tab1 = table(Arthritis)
install.packages("https://cran.r-project.org/src/contrib/colorspace_2.0-2.tar.gz", repos=NULL)
install.packages("https://cran.r-project.org/src/contrib/zoo_1.8-9.tar.gz", repos=NULL)
install.packages("https://cran.r-project.org/src/contrib/lmtest_0.9-39.tar.gz", repos=NULL)
install.packages("https://cran.r-project.org/src/contrib/vcd_1.4-9.tar.gz", repos=NULL)
library(grid)
library(vcd)
data("Arthritis")
tab1 = table(Arthritis$Improved)
prop.table(tab1)
round(prop.table(tab1),2)
table(Arthritis$Improved,Arthritis$Sex)
prop.table(xtabs(~Treatment+Improved,data=Arthritis),1)
prop.table(xtabs(~Treatment+Improved,data=Arthritis),2)
tab2 = xtabs(~Treatment+Improved,data=Arthritis)
margin.table(tab2,1)
margin.table(tab2,2)
addmargins(tab2)

tab3 = xtabs(~Treatment+Sex+Improved,data=Arthritis)
ftable(tab3)
margin.table(tab3,1)
margin.table(tab3,c(1,3))

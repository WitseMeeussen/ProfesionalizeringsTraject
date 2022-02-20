data = read.csv("adult.csv", stringsAsFactors = F)


# 2samples T-test
t.test(data$capital.gain,data$capital.loss,paired = T)


var.test(data$hours.per.week[data$sex == "Female"],data$hours.per.week[data$sex == "Male"])

var.test(data$hours.per.week[data$income == "<=50K"],data$hours.per.week[data$income != "<=50K"])


t.test(data$hours.per.week ~ data$sex, paired=F,var.equal=F)
# man significantly work more

t.test(data$hours.per.week ~ data$income, paired=F,var.equal=F)

#anova
summary(aov(education.num~workclass, data=data))

pairwise.t.test(data$education.num,data$workclass,p.adjust.method = 'bonf')


chisq.test(data$race, data$income)

d2 = read.csv("winequalityN.csv")

# one sample T -test
t.test(d2$fixed.acidity, mu=7.10,conf.level = 0.01)

# one sample T -test that H0: mean is less than
t.test(d2$fixed.acidity, mu=7.10,alternative = 'greater')

# paired T-test : H0: the are sumulare
t.test(d2$fixed.acidity,d2$residual.sugar, paired = TRUE)


unique(d2$quality)

#2 sample T-test
# H0: no difference in mean alcohol level in quality 3 and 9

var.test(d2$alcohol[d2$quality==3],d2$alcohol[d2$quality==9])
# variance is simular -> var = TRUE

t.test(d2$alcohol[d2$quality==3],d2$alcohol[d2$quality==9], var =TRUE)


#anova  H0: if the alcohol levels are simular per quality
summary(aov(alcohol ~ quality, data=d2))
# low p so H0 is rejected

# goes pairewise tru the qualitys and does a 2 sample T-test
pairwise.t.test(d2$alcohol,d2$quality,p.adjust.method = 'bonf')

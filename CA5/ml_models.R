
library(e1071)
library(ggplot2)


mydata <- read.csv("C:/Documents/Post Graduate Study/Higher Diploma DA/Big Data/CA5/Automobile_data.csv")

head(mydata)
summary(mydata)
sapply(mydata, function(x) sum(is.na(x)))
xtabs(~price + make , data = mydata)
xtabs(~price + fuel.type, data = mydata)
xtabs(~price + aspiration , data = mydata)
xtabs(~price + num.of.doors, data = mydata)
xtabs(~price + body.style, data = mydata)
xtabs(~price + drive.wheels, data = mydata)
xtabs(~price + engine.location, data = mydata)
xtabs(~price + engine.type, data = mydata)
xtabs(~price +num.of.cylinders, data = mydata)
xtabs(~price +fuel.system, data = mydata)


mydata$make <- factor(mydata$make)
mydata$fuel.type <- factor(mydata$fuel.type)
mydata$aspiration <- factor(mydata$aspiration)
mydata$num.of.doors <- factor(mydata$num.of.doors)
mydata$body.style <- factor(mydata$body.style)
mydata$drive.wheels <- factor(mydata$drive.wheels)
mydata$engine.location <- factor(mydata$engine.location)
mydata$engine.type <- factor(mydata$engine.type)
mydata$num.of.cylinders <- factor(mydata$num.of.cylinders)
mydata$fuel.system <- factor(mydata$fuel.system)

mylogit <- glm(price ~ 
                 make + 
                 fuel.type + 
                 aspiration + 
                 num.of.doors + 
                 body.style + 
                 drive.wheels + 
                 engine.location + 
                 engine.type + 
                 num.of.cylinders + 
                 fuel.system+
                 wheel.base+
                 length +
                 height +
                 curb.weight+
                 engine.size+
                 bore+
                 stroke+
                 compression.ratio+
                 horsepower+
                 peak.rpm+
                 city.mpg+
                 highway.mpg, 
               data = mydata, family = "binomial")
summary(mylogit)


scatter.smooth(x= mydata$highway.mpg, y =mydata$price, main= "Highway mileage ~ Car's Price", col = "red" )


par(mfrow = c(1,2))

boxplot(mydata$highway.mpg, main = "Highway mileage", sub= paste("outlier rows :" ,boxplot.stats(mydata$highway.mpg)$out))# box plot for highway mileage variable predictor.
boxplot(mydata$price, main = "Car's price", sub= paste("outlier rows :" ,boxplot.stats(mydata$price)$out))# box plot for price variable response.


library(e1071)
par(mfrow=c(1, 2))  # divide graph area in 2 columns
plot(density(mydata$highway.mpg), main="Density Plot: Highway mileage", ylab="Frequency", sub=paste("Skewness:", round(e1071::skewness(mydata$highway.mpg), 2)))  # density plot for 'Highway mileage'
polygon(density(mydata$highway.mpg), col="red")
plot(density(mydata$price), main="Density Plot: Car's price", ylab="Frequency", sub=paste("Skewness:", round(e1071::skewness(mydata$price), 2)))  # density plot for 'Car's price
polygon(density(mydata$price), col="red")



scatter.smooth(x= mydata$city.mpg, y =mydata$price, main= "City Mileage ~ Car's price", col = "red" )


par(mfrow = c(1,2))

boxplot(mydata$city.mpg, main = "City Mileage", sub= paste("outlier rows :" ,boxplot.stats(mydata$city.mpg)$out))# box plot for City Mileage variable predictor.
boxplot(mydata$price, main = "Car's price", sub= paste("outlier rows :" ,boxplot.stats(mydata$price)$out))# box plot for price variable response.


library(e1071)
par(mfrow=c(1, 2))  # divide graph area in 2 columns
plot(density(mydata$city.mpg), main="Density Plot: City Mileage", ylab="Frequency", sub=paste("Skewness:", round(e1071::skewness(mydata$city.mpg), 2)))  # density plot for 'City Mileage'
polygon(density(mydata$highway.mpg), col="red")
plot(density(mydata$price), main="Density Plot: Car's price", ylab="Frequency", sub=paste("Skewness:", round(e1071::skewness(mydata$price), 2)))  # density plot for 'price'
polygon(density(mydata$price), col="red")

scatter.smooth(x= mydata$compression.ratio, y =mydata$price, main= "Compression ratio ~ Car's Price", col = "red" )


par(mfrow = c(1,2))

boxplot(mydata$compression.ratio, main = "Compression ratio", sub= paste("outlier rows :" ,boxplot.stats(mydata$compression.ratio)$out))# box plot for Compression ratio variable predictor.
boxplot(mydata$price, main = "Car's price", sub= paste("outlier rows :" ,boxplot.stats(mydata$price)$out))# box plot for price variable response.


library(e1071)
par(mfrow=c(1, 2))  # divide graph area in 2 columns
plot(density(mydata$compression.ratio), main="Density Plot: Compression ratio", ylab="Frequency", sub=paste("Skewness:", round(e1071::skewness(mydata$compression.ratio), 2)))  # density plot for 'Compression ratio'
polygon(density(mydata$compression.ratio), col="red")
plot(density(mydata$price), main="Density Plot: Car's price", ylab="Frequency", sub=paste("Skewness:", round(e1071::skewness(mydata$price), 2)))  # density plot for 'Car's price
polygon(density(mydata$price), col="red")

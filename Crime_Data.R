# Load the dataset
crime <- read.csv(file.choose())
View(crime)

# Exploratory data analysis:
# 1. Measures of central tendency
# 2. Measures of dispersion
# 3. Third moment business decision
# 4. Fourth moment business decision
# 5. Probability distributions of variables 
# 6. Graphical representations (Histogram, Box plot, Dot plot, Stem & Leaf plot, Bar plot, etc.)

summary(crime)
attach(crime)

# Graphical representations (Histogram, Box plot, Dot plot, Stem & Leaf plot, Bar plot, etc.)

# Box plot Representation

boxplot(Murder, col = "dodgerblue4",main = "Murder")
boxplot(Assault, col = "dodgerblue4",main = "Assault")
boxplot(UrbanPop, col = "dodgerblue4",main = "UrbanPop")
boxplot(Rape, col = "red", horizontal = T,main = "Rape")

# Histogram Representation

hist(Murder,col = "blue", main = "Murder" )
hist(Assault,col = "blue", main = "Assault")
hist(UrbanPop,col = "blue", main = "UrbanPop")
hist(Rape,col = "blue", main = "Rape")


# Normalize the data
normalized_data <- scale(crime[, 2:5]) # Excluding the university name

summary(normalized_data)

# Distance matrix
d <- dist(normalized_data, method = "euclidean") 

fit <- hclust(d, method = "complete")

# Display dendogram
plot(fit) 
plot(fit, hang = -1)

groups <- cutree(fit, k = 5) # Cut tree into 3 clusters

rect.hclust(fit, k = 5, border = "red")

membership <- as.matrix(groups)

final <- data.frame(membership, crime)
View(final)
aggregate(crime[, 2:5], by = list(final$membership), FUN = mean)

library(readr)
write_csv(final, "crimeoutput.csv")

getwd()

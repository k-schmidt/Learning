# #########################
# Declaring and Installing Packages 
# #########################

#install.packages('MASS')
library(MASS)

c
set.seed(1)
train = sample(1:nrow(Boston), nrow(Boston)/2)
summary(tree.Boston)

# #########################
# Notice that the Output of summary () indicates that only three of the variables have been
# used in constructing the tree. In the context of a regression tree, the deviance is simply
# the sum of squared errors for the tree. We now plot the tree.
# #########################

plot(tree.boston)
text(tree.boston, pretty = 0)

# #########################
# The variable lstat measures the percentage of individuals with lower socioeconomic status.
# The tree indicates that lower values of lstat correspond to more expensive houses.
# The tree predicts a median house price of $46,400 for larger homes in suburbs in which
# residents have high socioeconomic status (rm >= 7.437 and lstat < 9.715).
# Now we use the cv.tree() function to see whether pruning the tree will improve performance.
# #########################

cv.boston = cv.tree(tree.boston)
plot(cv.boston$size, cv.boston$dev, type = 'b')

# #########################
# In this case, the most complex tree is selected by cross-validation. However, if we wish
# to prune the tree, we could do so as follows, using the prune.tree() function:
# #########################

prune.boston = prune.tree(tree.boston, best = 5)
plot(prune.boston)
text(prune.boston, pretty = 0)

# #########################
# In keeping with the cross-validation results, we use the unpruned tree to make predictions
# on the test set.
# #########################

yhat = predict(tree.boston, newdata = Boston[-train,])
boston.test = Boston [-train, "medv"]
plot(yhat, boston.test)
abline(0,1)
mean((yhat - boston.test)^2)

# #########################
# In other words, the test set MSE associated with the regression tree is 25.05. The square
# root of the MSE is therefore around 5.005, indicating that this model leads to test
# predictions that are within around $5,005 of the true median home value for the suburb.
# #########################

# #########################
# Bagging and Random Forests
# The randomforest() function can be used to perform both random forests and bagging since
# bagging is simply a special case of random forest with m = p.
# #########################


#install.packages('randomForest')
library('randomForest')
set.seed(1)
bag.boston = randomForest(medv ~., data = Boston, subset = train,
                          mtry = 13, importance = TRUE)
bag.boston


# #########################
# The argument mtry = 13 indicates that all 13 predictors should be considered for each split
# of the tree - in other words, that bagging should be done. How well does this bagged model
# perform on the test set?
# #########################

yhat.bag = predict(bag.boston, newdata = Boston[-train,])
plot(yhat.bag, boston.test)
abline(0,1)
mean((yhat.bag - boston.test)^2)

# #########################
# Growing a random forest proceeds in exactly the same way, except that we use a smaller value
# of mtry argument. By default, randomForest() uses p/3 variables when building a random forest
# of regression trees, and sqrt(p) variables when building a random forest of classification trees.
# Here we use mtry = 6.
# #########################

set.seed(1)
rf.boston = randomForest(medv ~., data = Boston, subset = train,
                         mtry = 6, importance = TRUE)
yhat.rf = predict(rf.boston, newdata = Boston[-train,])
mean((yhat.rf - boston.test)^2)

# #########################
# The test set MSE is 11.48; this indicates that random forests yielded an improvement over bagging
# in this case. Using the importance() function, we can view the importance of each variable.
# #########################

importance(rf.boston)

# #########################
# Two measures of variable importance are reported. The former is based upon the mean decrease
# of accuracy in predictions on the out of bag samples when a given variable is excluded from
# the model. The latter is a measure of the total decrease in node impurity that results from
# splits over that variable, averaged over all trees. In the case of regression trees, the node
# impurity is measured by the training RSS, and for classification trees by the deviance.
# Plots of these importance measures can be produced using the varImpPlot() function.
# #########################

varImpPlot(rf.boston)

# #########################
# The results indicate that across all of the trees considered in the random forest, the wealth
# level of the community (lstat) and the house size (rm) are by far the two most important
# variables.
# #########################

# #########################
# Boosting
# Here we use the gbm package and within it the gbm() function to fit boosted regression trees
# to the Boston data set. We run gbm() with the option distribution = "gaussian" since this
# is a regression problem; if it were a binary classification problem, we would use
# distribution = "bernoulli". The argument n.trees = 5000 indicates that we want 5000
# trees, and the option interation.depth = 4 limits the depth of each tree.
# #########################

#install.packages('gbm')
library(gbm)
set.seed(1)
boost.boston = gbm(medv ~., data = Boston[train,], distribution = "gaussian",
                   n.trees = 5000, interaction.depth = 4)
summary(boost.boston)

# #########################
# The summary function produces a relative influence plot and also outputs the
# relative influence statistics. We see that lstat and rm are by far the most
# important variables. We can also produce partial dependence plots for these two
# variables. These plots illustrate the marginal effect of the selected variables
# on the response after integrating out the other variables. In this case, as we
# might expect, median house prices are increasing with rm and decreasing with lstat.
# #########################

par(mfrow = c(1,2))
plot(boost.boston, i = 'rm')
plot(boost.boston, i = 'lstat')

# #########################
# We now use the boosted model to predict medv on the test set:
# #########################

yhat.boost = predict(boost.boston, newdata = Boston[-train,],
                     n.trees = 5000)
mean((yhat.boost - boston.test)^2)

# #########################
# The test MSE obtained is 11.8; similar to the test MSE for random forests
# and superior to that for bagging. If we want to, we can perform boosting
# with a different value of the shrinkage parameter lambda. The default
# value is 0.001, but this is easily modified. Here we take lambda = 0.2
# #########################

boost.boston = gbm(medv ~., data = Boston[train,], distribution = "gaussian",
                   n.trees = 5000, interaction.depth = 4, shrinkage = 0.2,
                   verbose = F)
yhat.boost = predict(boost.boston, newdata = Boston[-train,],
                     n.trees = 5000)
mean((yhat.boost - boston.test)^2)

# #########################
# In this case, using lambda = 0.2 leads to a slightly lower test MSE than
# lambda = 0.001
# #########################
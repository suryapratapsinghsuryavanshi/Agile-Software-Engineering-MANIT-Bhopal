# Deep Learning
Deep Learning is a process of machine learning where machine learns from data and experience, and improve its performance. Deep learning is a subset of machine learning, which is a subset of artificial intelligence. Deep learning is inspired by the structure and function of the brain, called artificial neural networks. Deep learning is also known as deep neural learning or deep neural network.

The Deep Learning process is similar to the human brain. The human brain has neurons, which are connected to each other. The connection between neurons is called synapses. The human brain has billions of neurons, and each neuron is connected to thousands of other neurons. The human brain has a complex network of neurons, which is called neural network. The neural network is responsible for all the functions of the human brain, such as thinking, learning, and memory.

## Contents
- K-Nearest Neighbors
- Naive Bayes
- Confusion Matrix
- Gredient Desent
- Dission Tree
- Ginny Index
- Ginny Impurity
- Hyperparameter
- Outlier
- SVM
- Bias-Variance Tradeoff
- Random Forest
- Method Testable Hypothesis
- Linear Regression
- NN or Draw Neural Network for LOGIC Gates.
- Activation Function

## K-Nearest Neighbors
K-Nearest Neighbors is a supervised machine learning algorithm. It is used for both classification and regression problems. K-Nearest Neighbors is a non-parametric algorithm, which means it does not make any assumption on underlying data. It is also called a lazy learner algorithm because it does not learn from the training set immediately instead it stores the dataset and at the time of classification, it performs an action on the dataset. K-Nearest Neighbors is a simple algorithm that stores all available cases and classifies new cases based on a similarity measure. K-Nearest Neighbors algorithm uses feature similarity to predict the values of new datapoints which further means that the new data point will be assigned a value based on how closely it matches the points in the training set.

### K-Nearest Neighbors Algorithm Steps
- Step 1: Choose the number of K neighbors, K should not be even.
- Step 2: Calculate the distance of the new data point with the existing data points.
- Step 3: Find the nearest data points based on the Euclidean distance, Manhattan distance, Minkowski distance, etc.
    - Euclidean distance: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$
    - Manhattan distance: $d = |x_2 - x_1| + |y_2 - y_1|$
    - Minkowski distance: $d = \sqrt[p]{(|x_2 - x_1|)^p + (|y_2 - y_1|)^p}$
- Step 4: Count the the most K nearest neighbors of the new data point.
- Step 5: Assign the new data point to the class where you counted the most neighbors.

## Gradient Descent
Gradient Descent is an optimization algorithm used to minimize some function by iteratively moving in the direction of steepest descent as defined by the negative of the gradient. In machine learning, we use gradient descent to update the parameters of our model. Parameters refer to coefficients in Linear Regression and weights in neural networks. Gradient Descent can be used for both convex and non-convex functions, but often it is used to optimize the parameters of a machine learning model. The objective of any supervised machine learning algorithm is to find the best hypothesis function that maps the input features(x) to the output variable(y). This is achieved by minimizing the cost function (C). The cost function is nothing but a mathematical representation of the error between the actual values and predicted values. The cost function is also known as the loss function or error function.

## Ginny Index
Gini index is a metric to measure how often a randomly chosen element would be incorrectly identified. It means an attribute with lower gini index should be preferred. It works with the categorical target variable “Success” or “Failure”. It performs only Binary splits. The higher the value of Gini higher the homogeneity. It belongs to the CART (Classification and Regression Tree) family where CART’s main focus is to reduce the Gini index value by creating binary splits. CART algorithm can be used for building decision trees suitable for both classification and regression problems.

## Ginny Impurity
Ginny Impurity is a measure of how often a randomly chosen element from the set would be incorrectly labeled if it was randomly labeled according to the distribution of labels in the subset. It is calculated by subtracting the sum of the squared probabilities of each class from one. It favors larger partitions and easy to implement whereas entropy favors smaller partitions with distinct values. It is not recommended when the number of classes is greater than two.

## Hyperparameter
Hyperparameters are the parameters whose values are set before the learning process begins. By contrast, the values of other parameters are derived via training. Different model training algorithms require different hyperparameters, some simple algorithms (such as ordinary least squares regression) require none. Given these hyperparameters, the training algorithm learns the parameters from the data. For instance, LASSO is an algorithm that adds a regularization hyperparameter to ordinary least squares regression, which has to be set before estimating the parameters through the training algorithm.

## Outlier
An outlier is a data point in a data set that is distant from all other observations. A data point that lies outside the overall distribution of the dataset. An outlier may be due to variability in the measurement or it may indicate experimental error; the latter are sometimes excluded from the data set. An outlier can cause serious problems in statistical analyses.

## Bias-Variance Tradeoff
Bias is the simplifying assumptions made by the model to make the target function easier to approximate. Variance is the amount that the estimate of the target function will change given different training data. Trade-Off is tension between the error introduced by the bias and the variance. The bias-variance decomposition essentially decomposes the learning error from any algorithm by adding the bias, the variance and a bit of irreducible error due to noise in the underlying dataset. The bias-variance decomposition can be best understood with the help of an example. Let’s say we make multiple predictions of the same sample with different machine learning algorithms. Now, we know that the actual value for that sample is fixed. So, the difference in the average of all those predictions and the actual value would be the bias of our model. If the predictions for the sample vary a lot from each other, then our model has high variance. The below image will help you understand the bias-variance trade-off better.

## Method Testable Hypothesis
Method Testable Hypothesis is a hypothesis that can be tested by an experiment or observations. In other words, it is an educated guess that can be tested with the help of observation and experimentation. It is a proposed explanation for an observable phenomenon. It is derived from the Greek word “hupotithenai” meaning “to put under” or “to suppose”. It is usually based on a general assumption concerning the research subject and is an important element of the scientific method. It is initially given by the researcher prior to the commencement of the research. It is only considered valid if it can be tested. It is mainly used in experimental quantitative research studies, where its purpose is to test the theory that is generated by the researcher.

## Nurual Network
A neural network is a series of algorithms that endeavors to recognize underlying relationships in a set of data through a process that mimics the way the human brain operates. In this sense, neural networks refer to systems of neurons, either organic or artificial in nature. Neural networks can adapt to changing input; so the network generates the best possible result without needing to redesign the output criteria. The concept of neural networks, which has its roots in artificial intelligence, is swiftly gaining popularity in the development of trading systems. A neural network is a collection of connected nodes called neurons in a similar fashion as the vast network of neurons in a brain. Here, each circular node represents an artificial neuron and an arrow represents a connection from the output of one artificial neuron to the input of another. The input layer collects input patterns. The output layer has classifications or output signals to which input patterns may map. The input signals propagate forward through the network to generate the output signals. The output signals indicate the classification of the input patterns. The input signals propagate forward through the network to generate the output signals. The output signals indicate the classification of the input patterns. The input signals propagate forward through the network to generate the output signals. The output signals indicate the classification of the input patterns.

### Types of Neural Networks
- Feedforward Neural Network
- Convolutional Neural Network
- Recurrent Neural Network
- Modular Neural Network
- Radial Basis Function Neural Network
- Multilayer Perceptron
- Perceptron

## Activation Function
An activation function is a function in a neural network that decides whether the neuron should be activated or not by calculating weighted sum and further adding bias with it. The purpose of the activation function is to introduce non-linearity into the output of a neuron. It squashes the input into a smaller range. It is differentiable, which means it can find the slope of the curve at any two points. It should be monotonic in nature, i.e., its value should be either entirely increasing or decreasing or constant. It should be continuous, i.e., it should be defined for all values of input. It should be computationally efficient to calculate. It should have a derivative that can be calculated. It should produce a consistent output for a given input.

### Types of Activation Functions
- Sigmoid: $f(x) = \frac{1}{1 + e^{-x}}$
- Tanh: $f(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$
- ReLU: $f(x) = max(0, x)$
- Leaky ReLU: $f(x) = max(0.01x, x)$
- Softmax: $f(x) = \frac{e^{x_i}}{\sum_{j=1}^{k} e^{x_j}}$

## Celebrating the Most Popular Deep Learning Terms!

Deep Learning has taken the world by storm, revolutionizing fields like image recognition, natural language processing, and even healthcare. Let's raise a glass to four of the most popular Deep Learning terms and delve into their fascinating worlds:

**1. Artificial Neural Network (ANN)**

![](https://www.researchgate.net/profile/Mahamad-Alam/publication/305325563/figure/fig1/AS:384012620189699@1468567152001/A-typical-artificial-neural-network-ANN.png)

Imagine a brain made of interconnected nodes that process information. That's the essence of an ANN! These networks, inspired by the human brain, learn by adjusting connections between nodes based on data. They can solve complex problems like image classification and speech recognition.

![](https://d14b9ctw0m6fid.cloudfront.net/ugblog/wp-content/uploads/2020/12/1-4.png)

[Image of Convolutional neural network (CNN) diagram]

Ever wondered how computers can recognize objects in images? CNNs are the answer! These specialized networks are like detectives, scanning images with "filters" to identify patterns and features. They excel in tasks like object detection, facial recognition, and medical image analysis.

**3. Recurrent Neural Network (RNN)**

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*3ltsv1uzGR6UBjZ6CUs04A.jpeg)

RNNs have a unique ability: they remember! Unlike traditional ANNs that process one input at a time, RNNs can handle sequences of data, like text or time series. This makes them ideal for tasks like machine translation, sentiment analysis, and natural language generation.

**4. Long Short-Term Memory (LSTM)**

![](https://www.researchgate.net/publication/339120709/figure/fig1/AS:856315459010563@1581172923374/General-scheme-of-an-Long-Short-Term-Memory-neural-networks-LSTM-for-L-p-The.ppm)

LSTMs are like long-distance runners in the world of RNNs. They can remember information for longer periods, making them powerful tools for tasks like language translation and speech recognition. LSTMs are also crucial in advanced Deep Learning models like Generative Adversarial Networks (GANs) and Transformers.

These four terms represent just a small portion of the vibrant and ever-evolving Deep Learning landscape. As researchers continue to push the boundaries of this technology, we can only imagine the incredible applications that await us in the future. So, let's celebrate these groundbreaking terms and their potential to shape the world of tomorrow!


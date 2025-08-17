- [Preprocessing](./data_mining/)

## Support Vector Machine (SVM)
Support Vector Machine (SVM) is a supervised machine learning algorithm used for classification and regression tasks. It works by finding the optimal hyperplane that separates data points of different classes in a high-dimensional space. SVM aims to maximize the margin between the closest data points of each class, known as support vectors.

### Key Concepts
- **Hyperplane**: A decision boundary that separates different classes in the feature space.
- **Support Vectors**: Data points that are closest to the hyperplane and influence its position.
- **Margin**: The distance between the hyperplane and the nearest support vectors from either class. SVM aims to maximize this margin.

### Types of SVM
- **Linear SVM**: Used when data is linearly separable. It finds a linear hyperplane to separate the classes.
- **Non-Linear SVM**: Used when data is not linearly separable. It applies kernel functions to transform the data into a higher-dimensional space where a linear hyperplane can be used.

## Regression
Regression is a supervised learning technique in Machine Learning that is used to predict a continuous numerical value (output) based on input variables (features).

It tries to find the relationship between independent variables (X) and a dependent variable (Y).

**In simple terms:** Regression predicts “how much” or “how many.”

## Apriori Algorithm
The Apriori Algorithm is a data mining and machine learning algorithm used for frequent itemset mining and association rule learning.

It helps discover relationships and patterns among items in large datasets.

**Example:** In a supermarket, finding that “people who buy bread often buy butter too.”

**It is based on the “Apriori property”:**
- If an itemset is frequent, then all of its subsets are also frequent
- If an itemset is infrequent, then all of its supersets will also be infrequent.

This property helps in reducing the search space for itemsets.

## FP-Tree (Frequent Pattern Tree)

The FP-Tree (Frequent Pattern Tree) is a compact data structure used in frequent pattern mining, mainly in the FP-Growth algorithm.

It helps to find frequent itemsets without generating a huge number of candidate itemsets (which Apriori does).

**In short:** FP-Tree is a compressed representation of transactions that makes mining frequent patterns faster and more efficient.

**Instead of repeatedly scanning the database (like Apriori), FP-Tree:**
- Scans the database only twice.
- Builds a tree structure of itemsets.
- Uses this tree to find frequent patterns directly.

## K-Means Algorithm
K-Means is an unsupervised machine learning algorithm used for clustering data.
It groups data points into K clusters, where each cluster has a centroid (center point).

**The goal:** Minimize the distance between points in a cluster and their cluster’s centroid.

### How K-Means Works
- Choose number of clusters (K). Example: K = 3 (we want 3 groups).
- Initialize centroids randomly. Pick K random points as cluster centers.
- Assign data points to nearest centroid. Each point goes to the cluster with the closest center (using distance, e.g., Euclidean distance).
- Update centroids. Recalculate the centroid of each cluster (mean of all points in the cluster).
- Repeat Steps 3 & 4 until centroids stop changing (convergence).

> [SVM](/notes/data_mining/svm.pdf), [Regression](/notes/data_mining/regression.pdf), [Apriori Algorithm - 1](/notes/apriori.pdf), [Apriori Algorithm - 2](/notes/apriori_algo.pdf), FP-Tree, K-Means Algorithm, Numerical PDF: [PDF](/notes/Data_Warehouse_2.pdf)
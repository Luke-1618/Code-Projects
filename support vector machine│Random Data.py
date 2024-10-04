import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.svm import SVC

# Generate synthetic 3D data
X, y = make_classification(n_samples=100, n_features=3, n_classes=2, n_clusters_per_class=1, n_informative=2, n_redundant=0, random_state=42)

# Train the SVM model
svm = SVC(kernel='linear', probability=True)
svm.fit(X, y)

# Plot decision boundary
plt.figure(figsize=(10, 8))
ax = plt.subplot(111, projection='3d')

# Plot points
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap=plt.cm.coolwarm, edgecolors='k')

# Create meshgrid for decision boundary
xx, yy = np.meshgrid(np.linspace(X[:, 0].min(), X[:, 0].max(), 50),
                     np.linspace(X[:, 1].min(), X[:, 1].max(), 50))
zz = (-svm.intercept_[0] - svm.coef_[0][0] * xx - svm.coef_[0][1] * yy) / svm.coef_[0][2]

# Plot decision boundary surface
ax.plot_surface(xx, yy, zz, alpha=0.5)

ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_zlabel('Feature 3')
ax.set_title('Support Vector Machine Decision Boundary')
plt.show()

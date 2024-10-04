import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture
import seaborn as sns

def plot_gmm_3d(X, labels, probs, centers):
    # Define a custom color palette with distinct colors for each cluster
    palette = sns.color_palette("hsv", len(np.unique(labels)))

    # Plot
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')  # Create a 3D subplot

    for i in range(len(centers)):
        # Plot points for each cluster with a different color
        alpha_values = probs[:, i]
        ax.scatter(X[labels == i][:, 0], X[labels == i][:, 1], X[labels == i][:, 2], label=f'Cluster {i+1}', alpha=0.8, s=50,
                   color=palette[i])  # Use color instead of c

        # Calculate the distance from each point to its cluster center
        distances = np.linalg.norm(X[labels == i] - centers[i], axis=1)

        # Use the maximum distance as the radius for the sphere
        radius = np.max(distances)

        # Plot circles at different heights to approximate a sphere
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        for h in np.linspace(-radius, radius, 10):
            x = radius * np.outer(np.cos(u), np.sin(v)) + centers[i][0]
            y = radius * np.outer(np.sin(u), np.sin(v)) + centers[i][1]
            z = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + centers[i][2] + h
            ax.plot_surface(x, y, z, color=palette[i], alpha=0.05)

    ax.set_title('Gaussian Mixture Model with Expectation-Maximization (EM) Algorithm')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_zlabel('Feature 3')
    ax.legend()

    plt.show()

# Generate Random data
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0, n_features=3)  # Generating 3-dimensional data

# Fit GMM using Expectation-Maximization (EM) algorithm
gmm = GaussianMixture(n_components=4, random_state=42)  # Random state for reproducibility
gmm.fit(X)  # EM algorithm is used here for fitting the GMM
labels = gmm.predict(X)
probs = gmm.predict_proba(X)
centers = gmm.means_

plot_gmm_3d(X, labels, probs, centers)

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, davies_bouldin_score

# Load dataset
file_path = "C:/Geospetical/DATA/ML Assignment Dataset.csv"
df = pd.read_csv(file_path, delimiter=";")

df.dropna(inplace=True)  # Drop NaN values if any

# Extract coordinates
X = df[['Longitude', 'Latitude']].values

# Normalize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Define number of clusters for applicable models
k = 5

# Initialize models
models = {
    "K-Means": KMeans(n_clusters=k, random_state=42, n_init=10),
    "DBSCAN": DBSCAN(eps=0.5, min_samples=10),
    "Agglomerative": AgglomerativeClustering(n_clusters=k),
    "GMM": GaussianMixture(n_components=k, random_state=42)
}

# Store evaluation metrics
clustering_results = {
    "Model": [],
    "Silhouette Score": [],
    "Davies-Bouldin Score": []
}

best_model = None
best_score = -1

for name, model in models.items():
    labels = model.fit_predict(X_scaled)
    if len(set(labels)) > 1:  # Ensure valid silhouette score
        silhouette = silhouette_score(X_scaled, labels)
        db_score = davies_bouldin_score(X_scaled, labels)
        clustering_results["Model"].append(name)
        clustering_results["Silhouette Score"].append(silhouette)
        clustering_results["Davies-Bouldin Score"].append(db_score)
        
        if silhouette > best_score:
            best_score = silhouette
            best_model = model
            best_labels = labels

# Save best model results
df["Cluster"] = best_labels
df.to_csv("C:/Geospetical/DATA/cluster_result.csv", index=False)

# Convert results to DataFrame and display
eval_df = pd.DataFrame(clustering_results)
print(eval_df)
print(f"\nBest Model: {type(best_model).__name__} with Silhouette Score: {best_score:.3f}")

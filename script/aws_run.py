import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score, davies_bouldin_score
import logging
import subprocess

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load dataset
file_path = "C:/Geospetical/DATA/ML Assignment Dataset.csv"
df = pd.read_csv(file_path, delimiter=';')
df.columns = ["Longitude", "Latitude"]

# Convert columns to numeric (if needed)
df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")
df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
df.dropna(inplace=True)

# Prepare data
X = df[['Longitude', 'Latitude']].values
k = 5  # Define number of clusters

# Store results
clustering_results = {}

# K-Means Clustering
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
df['KMeans_Cluster'] = kmeans.fit_predict(X)
clustering_results["K-Means"] = {
    "Silhouette": silhouette_score(X, df['KMeans_Cluster']),
    "Davies-Bouldin": davies_bouldin_score(X, df['KMeans_Cluster'])
}

# DBSCAN Clustering
dbscan = DBSCAN(eps=0.5, min_samples=10)
df['DBSCAN_Cluster'] = dbscan.fit_predict(X)
if len(set(dbscan.labels_)) > 1:
    clustering_results["DBSCAN"] = {
        "Silhouette": silhouette_score(X, df['DBSCAN_Cluster']),
        "Davies-Bouldin": davies_bouldin_score(X, df['DBSCAN_Cluster'])
    }

# Agglomerative Clustering
agglo = AgglomerativeClustering(n_clusters=k)
df['Agglo_Cluster'] = agglo.fit_predict(X)
clustering_results["Agglomerative"] = {
    "Silhouette": silhouette_score(X, df['Agglo_Cluster']),
    "Davies-Bouldin": davies_bouldin_score(X, df['Agglo_Cluster'])
}

# Gaussian Mixture Model (GMM)
gmm = GaussianMixture(n_components=k, random_state=42)
df['GMM_Cluster'] = gmm.fit_predict(X)
clustering_results["GMM"] = {
    "Silhouette": silhouette_score(X, df['GMM_Cluster']),
    "Davies-Bouldin": davies_bouldin_score(X, df['GMM_Cluster'])
}

# Select Best Model (higher Silhouette, lower Davies-Bouldin)
best_model = max(clustering_results, key=lambda m: clustering_results[m]["Silhouette"])
df["Final_Cluster"] = df[f"{best_model}_Cluster"]

logging.info(f"Best Clustering Model: {best_model}")
logging.info(f"Performance Scores: {clustering_results[best_model]}")

# Save results
df.to_csv("C:/Geospetical/OUTPUT/clustered_data.csv", index=False)
logging.info("Clustered data saved successfully.")

# Call visualization.py
try:
    subprocess.run(["python", "script/visualization.py"], check=True)
    logging.info("Visualization script executed successfully.")
except subprocess.CalledProcessError as e:
    logging.error(f"Error executing visualization.py: {e}")

import pandas as pd
import folium
import matplotlib.pyplot as plt
import seaborn as sns

# Load clustered data
df = pd.read_csv("C:/Geospetical/DATA/cluster_result.csv")

# Ensure cluster labels are integers
df["Cluster"] = df["Cluster"].astype(int)

# Define a color map
colors = ['red', 'blue', 'green', 'purple', 'orange', 'pink', 'brown']

# Create a Folium map centered at the mean location
m = folium.Map(location=[df["Latitude"].mean(), df["Longitude"].mean()], zoom_start=5)

# Add markers
for _, row in df.iterrows():
    cluster_label = int(row["Cluster"])  # Convert to integer
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=5,
        color=colors[cluster_label % len(colors)],  # Ensure integer index
        fill=True
    ).add_to(m)

# Save the map
m.save("C:/Geospetical/data/clustering_map.html")

# Plot cluster distribution
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="Longitude", y="Latitude", hue="Cluster", palette="Set1")
plt.title("Clustering Results")
plt.savefig("C:/Geospetical/data/cluster_plot.png")
plt.show()

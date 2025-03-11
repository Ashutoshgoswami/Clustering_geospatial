# Geospetical Clustering Project

## Overview
This project focuses on performing geospatial clustering analysis using machine learning techniques. The dataset contains latitude and longitude coordinates, which are grouped into clusters for visualization and further analysis.

## Project Structure
```
Geospetical/
│-- DATA/
│   ├── cluster_plot.png          # Scatter plot of clusters
│   ├── cluster_result.csv        # Clustering results dataset
│   ├── clustering_map.html       # Interactive map of clusters
│   ├── ML Assignment Dataset.csv # Original dataset
│-- Notebook/
│   ├── Geo_cluster.ipynb         # Jupyter notebook for analysis
│-- script/
│   ├── aws_run.py                # AWS-related operations (not working due to account verification issue)
│   ├── clustering.py             # Script for clustering
│   ├── visualization.py          # Script for visualization
│-- venv/                         # Virtual environment (if applicable)
│-- README.md                     # Project documentation
│-- requirements.txt               # Dependencies list
```

## Requirements
Before running the scripts, install the required dependencies using:
```bash
pip install -r requirements.txt
```

## Running the Project

### 1. Clustering the Data
To run the clustering script and generate cluster results, execute:
```bash
python script/clustering.py
```
This will generate `cluster_result.csv` inside the `DATA/` folder.

### Best Model
           Model  Silhouette Score  Davies-Bouldin Score
0        K-Means          0.553212              0.765006
1         DBSCAN          0.330948              0.604316
2  Agglomerative          0.495402              0.800859
3            GMM          0.426726              1.736650

Best Model: KMeans with Silhouette Score: 0.553

### 2. Visualizing the Clusters
To visualize the clustering results using Folium and Matplotlib, run:
```bash
python script/visualization.py
```
This will generate:
- `cluster_plot.png` (Scatter plot of clusters)
- `clustering_map.html` (Interactive cluster map)

### 3. Running on AWS (Currently Not Working)
Due to an account verification issue, running the script on AWS is not possible at the moment. However, all necessary steps for cloud deployment have been outlined in `script/aws_run.py`.

## Jupyter Notebook
For a step-by-step analysis, refer to the Jupyter Notebook:
```
Notebook/Geo_cluster.ipynb
```

## Notes
- Ensure your Python environment is activated (`venv/` if applicable) before running scripts.
- Results are stored inside the `DATA/` folder.
- If AWS verification is resolved, `aws_run.py` can be used for cloud execution.




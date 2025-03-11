
# Geospatial Clustering Project

## Project Overview
This project applies multiple clustering algorithms to geospatial data to identify meaningful groups within a dataset. It includes:
- Data preprocessing and normalization
- Clustering using K-Means, DBSCAN, Agglomerative Clustering, and Gaussian Mixture Model (GMM)
- Evaluation using Silhouette Score and Davies-Bouldin Score
- Visualization of results with scatter plots and interactive maps



## Clustering Algorithms Used
- **K-Means Clustering**
- **DBSCAN (Density-Based Spatial Clustering)**
- **Agglomerative Clustering**
- **Gaussian Mixture Model (GMM)**

## Visualizations
### Clustering Result
![Clustering Result](C:/Geospetical/DATA/cluster_plot.png)

### Interactive Map
![Mapping Result](C:/Geospetical/DATA/MAP.png)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/geospetical-clustering.git
   cd geospetical-clustering
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the clustering script:
   ```bash
   python script/clustering.py
   ```
4. Run visualization:
   ```bash
   python script/visualization.py
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




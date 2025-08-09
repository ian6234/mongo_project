import requests
import sklearn
import numpy as np
import pprint
from collections import defaultdict

data = requests.get('http://localhost:8000/symbols/all').json()

X = []
tickers = []
for document in data:
    prices = np.array(document['close'])
    log_returns = np.diff(np.log(prices))
    tickers.append(document['symbol'])
    X.append(log_returns)

model = sklearn.cluster.KMeans(n_clusters=3)
kmeans = model.fit(X)

labels = kmeans.labels_

# Map tickers -> cluster
cluster_map = dict(zip(tickers, labels))
print(cluster_map)

# Show tickers in each cluster

groups = defaultdict(list)
for t, l in cluster_map.items():
    groups[l].append(t)
for k, members in groups.items():
    print(f"Cluster {k}: {members}")

from sklearn.cluster import DBSCAN
from collections import defaultdict
import numpy as np

def grouping(comments: list, cluster_labels):
    result = []
    for i, label in enumerate(cluster_labels):
    # if label != -1:
        comments[i]['cluster'] = int(label)
        result.append(comments[i])

    # clusterでソート
    result.sort(key=lambda x: x["cluster"], reverse=True) 
    # result.sort(key=lambda x: x["like"], reverse=True)
    return result
from typing import List, Dict, Any

def ranking(grouped_comments: List[Dict[str, Any]]) -> Dict[int, Dict[str, Any]]:
    cluster_data = group_by_cluster(grouped_comments)
    ranked_clusters = calculate_score(cluster_data)
    return ranked_clusters

def group_by_cluster(comments: List[Dict[str, Any]]) -> Dict[int, Dict[str, Any]]:
    cluster_data = {}
    for comment in comments:
        cluster_id = comment['cluster']
        if cluster_id not in cluster_data:
            cluster_data[cluster_id] = {
                'comments': [],
                'total_likes': 0,
                'total_comments': 0
            }
        cluster_data[cluster_id]['comments'].append({"text": comment['text'], "like": comment['like']})
        cluster_data[cluster_id]['total_likes'] += comment['like']
        cluster_data[cluster_id]['total_comments'] += 1
    return cluster_data

def calculate_score(cluster_data: Dict[int, Dict[str, Any]]) -> Dict[int, Dict[str, Any]]:
    cluster_scores = []
    for cluster_id, data in cluster_data.items():
        score = data['total_likes'] / data['total_comments'] if data['total_comments'] > 0 else 0
        data['score'] = score
        cluster_scores.append((cluster_id, data))

    sorted_clusters = sorted(cluster_scores, key=lambda x: x[1]['score'], reverse=True)
    return {cluster_id: data for cluster_id, data in sorted_clusters}

if __name__ == "__main__":
    import json

    with open('app/test/clustered_comments.json', 'r', encoding='utf-8') as f:
        clustered_comments = json.load(f)

    ranked_cluster = ranking(clustered_comments)

    with open('app/test/ranked_cluster.json', 'w', encoding='utf-8') as f:
        json.dump(ranked_cluster, f, ensure_ascii=False, indent=4)

"""
python -m app.analyse.ranking
"""

from sentence_transformers import SentenceTransformer
from sklearn.cluster import DBSCAN
from collections import defaultdict
import numpy as np

def cluster(texts):
    embeddings = into_embeddings(texts)
    cluster_labels = into_clusters(embeddings)
    return cluster_labels

def into_embeddings(texts):
    # モデル：Sentence-BERT
    model = SentenceTransformer('sonoisa/sentence-bert-base-ja-mean-tokens')
    embeddings = model.encode(texts)
    return embeddings

def into_clusters(embeddings):
    # eps = レンジ、min_samples = 最小サンプル数
    dbscan = DBSCAN(eps=0.2, min_samples=2, metric='cosine')
    cluster_labels = dbscan.fit_predict(embeddings)
    return cluster_labels

if __name__ == "__main__":
    cleaned_texts = [
        "マジで神商品だった",                    # ポジティブ
        "買って大正解！",                        # ポジティブ
        "リピ確定です",                          # ポジティブ
        "めっちゃ肌が綺麗になった",              # ポジティブ
        "友達にもおすすめしたい",                # ポジティブ

        "まあまあだったかな",                    # 中立
        "特に効果は感じなかった",                # 中立
        "普通…期待しすぎた",                    # 中立
        "良くも悪くもない",                      # 中立
        "使ってみないとわからない",              # 中立

        "全く効果なし",                          # ネガティブ
        "お金の無駄だった",                      # ネガティブ
        "肌が荒れた",                            # ネガティブ
        "使ってすぐやめた",                      # ネガティブ
        "口コミに騙された",                      # ネガティブ

        "配送が遅かった",                        # クレーム系
        "箱が潰れて届いた",                      # クレーム系
        "問い合わせに返信なし",                  # クレーム系
        "サポートが最悪",                        # クレーム系
        "返品対応が雑すぎる"                      # クレーム系
    ]
    cluster_labels = cluster(cleaned_texts)
    print(cluster_labels)

"""
python -m app.analyse.cluster
"""


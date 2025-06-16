from app.logger_setting.logger import logger

def analyse_cluster(comments):
    texts = []
    liked_comments = []

    for comment in comments:
        if comment['like'] <= 1:
            continue
        if len(comment['text']) <= 15:
            continue
        texts.append(comment['text'])
        liked_comments.append(comment)

    try:
        from app.comment.analyse.clean import clean
        cleaned_texts = clean(texts)
        logger.info(f"success cleaning comments")
    except Exception as e:
        raise RuntimeError(f"cleaning comments: {e}")
    
    try:
        from app.comment.analyse.cluster import cluster
        cluster_labels = cluster(cleaned_texts)
        logger.info(f"success clustering comments")
    except Exception as e:
        raise RuntimeError(f"clustering comments: {e}")
    
    try:
        from app.comment.analyse.grouping import grouping
        grouped_comments = grouping(liked_comments, cluster_labels)
        logger.info(f"success grouping comments")
    except Exception as e:
        raise RuntimeError(f"grouping comments: {e}")
    
    try:
        from app.comment.analyse.ranking import ranking
        ranked_cluster = ranking(grouped_comments)
        logger.info(f"success ranking comments")
    except Exception as e:
        raise RuntimeError(f"ranking comments: {e}")

    return dict(sorted(ranked_cluster.items(), key=lambda x: int(x[0])))

def analyse_likes(comments, video_likes, min_video_likes=500):
    liked_comments = []

    if video_likes <= min_video_likes:
        return []

    for comment in comments:
        if comment['like'] <= 1:
            continue

        comment['score'] = comment['like'] / video_likes
        liked_comments.append(comment)
    
    # スコアを消して、イイネ順に並べ直す

    return sorted(liked_comments, key=lambda x: x['score'], reverse=True)
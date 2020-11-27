import numpy as np
import operator

from sklearn.cluster import DBSCAN


class HeadingCluster:
    def __init__(self):
        self.model = DBSCAN(eps=0.5, min_samples=10)

    def cluster_headings(self, heading_coords, headings):
        clustered_headings = []
        db = self.model.fit(heading_coords)
        labels = db.labels_  # labels of the found clusters
        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)  # number of clusters
        for i in range(n_clusters):
            cluster_indices = np.where(labels == i)[0]
            # sub_headings = np.asarray(headings)[cluster_indices].tolist()
            sub_headings = list(operator.itemgetter(*cluster_indices)(headings))
            clustered_headings.append(sub_headings)

        return clustered_headings


if __name__ == '__main__':
    import pandas as pd
    from src.keyword.grouper import KeywordGrouper
    from settings import GROUPED_KEYWORDS_CSV
    keyword_grouper = KeywordGrouper()
    df = pd.read_csv(GROUPED_KEYWORDS_CSV)
    keywords = df.loc[df["Category"] == "Blue Book", "Keyword"].values.tolist()
    keyword_vectors = []
    for keyword in keywords:
        keyword = keyword.replace("blue", "").replace("book", "")
        k_vec = keyword_grouper.get_bow_vector(keyword=keyword)
        keyword_vectors.append(k_vec)
    HeadingCluster().cluster_headings(heading_coords=keyword_vectors, headings=keywords)

import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity
from src.preprocess.tokenizer import TextPreprocessor
from settings import CORPUS_PATH, KEYWORD_CSV, GROUP_MAIN_KEYS


class KeywordGrouper:
    def __init__(self):
        self.text_processor = TextPreprocessor()
        with (CORPUS_PATH, 'r') as f:
            self.corpus_keys = list(eval(f.read()).keys())
        self.grouped_keys = {}
        self.__get_group_key_feature()

    def __get_group_key_feature(self):
        for g_key in GROUP_MAIN_KEYS:
            self.grouped_keys[g_key] = {"key_vector": [], "keywords": []}
            self.grouped_keys[g_key]["key_vector"] = self.get_bow_vector(keyword=g_key)

    def get_bow_vector(self, keyword):

        token_words = self.text_processor.tokenize_word(sample=keyword)
        key_vec = [0] * len(self.corpus_keys)
        for t_word in token_words:
            if t_word in self.corpus_keys:
                index = self.corpus_keys.index(t_word)
                key_vec[index] = 1

        return key_vec

    def group_keywords(self):
        keywords = pd.read_csv(KEYWORD_CSV)["Keyword"].values.tolist()
        for keyword in keywords:
            k_vec = self.get_bow_vector(keyword=keyword)
            similarities = []
            for g_key in self.grouped_keys.keys():
                g_key_vec = self.grouped_keys[g_key]["key_vector"]
                similarity = cosine_similarity([k_vec], [g_key_vec])
                similarities.append(similarity)
            closet_g_key = list(self.grouped_keys.keys())[similarities.index(min(similarities))]
            self.grouped_keys[closet_g_key]["keywords"].append(keyword)

        return


if __name__ == '__main__':
    KeywordGrouper().group_keywords()

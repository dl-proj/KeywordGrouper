import json
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity
from src.preprocess.tokenizer import TextPreprocessor
from settings import CORPUS_PATH, KEYWORD_CSV, GROUP_KEYS, GROUPED_KEYWORDS_CSV, SPACING_CHECK, SPELL_CHECK


class KeywordGrouper:
    def __init__(self):
        self.text_processor = TextPreprocessor()
        with open(CORPUS_PATH) as f:
            self.corpus_keys = list(json.load(f).keys())
        self.grouped_keys = None

    def __get_group_key_feature(self, group_category):
        self.grouped_keys = {}
        for g_key in group_category:
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

    def group_keywords(self, group_category, output_file_path):
        self.__get_group_key_feature(group_category=group_category)
        info_df = pd.read_csv(KEYWORD_CSV)
        keywords = info_df["Keyword"].values.tolist()
        categories = []
        for keyword in keywords:
            if "edmonds" in keyword:
                keyword = keyword.replace("edmonds", "edmunds")
            elif "apraisal" in keyword:
                keyword = keyword.replace("apraisal", "appraisal")
            for spell_check_key in SPELL_CHECK:
                if spell_check_key in keyword:
                    keyword = keyword.replace(spell_check_key, "auto trader")
            for spacing_check_key in SPACING_CHECK:
                if spacing_check_key in keyword:
                    fst_spacing_index = keyword.find(spacing_check_key) - 1
                    lst_spacing_index = fst_spacing_index + len(spacing_check_key) + 1
                    if fst_spacing_index != " " and fst_spacing_index != -1:
                        keyword = keyword[:fst_spacing_index + 1] + " " + keyword[fst_spacing_index + 1:]
                    elif lst_spacing_index != "" and lst_spacing_index < len(keyword):
                        keyword = keyword[:lst_spacing_index] + " " + keyword[lst_spacing_index:]
            k_vec = self.get_bow_vector(keyword=keyword)
            similarities = []
            for g_key in self.grouped_keys.keys():
                g_key_vec = self.grouped_keys[g_key]["key_vector"]
                similarity = cosine_similarity([k_vec], [g_key_vec])
                similarities.append(similarity)
            if max(similarities) == 0:
                categories.append("")
                continue
            else:
                closet_g_key = list(self.grouped_keys.keys())[similarities.index(max(similarities))]
                categories.append(closet_g_key)
            self.grouped_keys[closet_g_key]["keywords"].append(keyword)

        info_df["Category"] = categories

        # df_list = []
        # for g_key in self.grouped_keys.keys():
        #     df_list.append(self.grouped_keys[g_key]["keywords"])

        info_df.to_csv(output_file_path, index=True, header=True, mode="w")

        # pd.DataFrame(df_list).T.to_csv(output_file_path, index=True, header=list(self.grouped_keys.keys()),
        #                                mode="w")
        print(f"[INFO] Successfully saved in {output_file_path}")

        return

    def run(self):
        self.group_keywords(group_category=GROUP_KEYS, output_file_path=GROUPED_KEYWORDS_CSV)


if __name__ == '__main__':
    KeywordGrouper().run()

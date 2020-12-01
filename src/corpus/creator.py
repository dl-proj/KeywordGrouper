import json
import pandas as pd

from src.preprocess.tokenizer import TextPreprocessor
from utils.folder_file_manager import save_file
from settings import KEYWORD_CSV_FILE_PATH, CORPUS_PATH


def create_corpus():

    text_preprocessor = TextPreprocessor()

    keyword_df = pd.read_csv(KEYWORD_CSV_FILE_PATH)
    keywords = keyword_df["Keyword"].values.tolist()
    word_freq = {}

    for keyword in keywords:
        token_words = text_preprocessor.tokenize_word(sample=keyword)
        for t_word in token_words:
            if t_word == "":
                continue
            if not t_word.isalpha():
                continue
            if t_word not in word_freq.keys():
                word_freq[t_word] = 1
            else:
                word_freq[t_word] += 1

    save_file(filename=CORPUS_PATH, content=json.dumps(word_freq, indent=4), method="w")
    print(f"[INFO] Successfully saved corpus in {CORPUS_PATH}")

    return


if __name__ == '__main__':
    create_corpus()

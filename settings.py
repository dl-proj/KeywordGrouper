import os

from utils.folder_file_manager import make_directory_if_not_exists

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
CORPUS_PATH = os.path.join(CUR_DIR, 'utils', 'corpus.json')
KEYWORD_CSV = os.path.join(CUR_DIR, 'Google_Automotive_KWP_CA.csv')
OUTPUT_DIR = make_directory_if_not_exists(os.path.join(CUR_DIR, 'output'))
GROUPED_KEYWORDS_CSV = os.path.join(OUTPUT_DIR, 'grouped_keyword.csv')

SPELL_CHECK = ["autorader", "aytotrader", "autotader", "autrader", "auotrader", "autotradr", "autotrafer", "aututrader",
               "autotraer", "autrotrader", "autottader", "autotarder", "autotreader", "autptrader", "auottrader",
               "autotradwr", "autotrad", "autotradeer", "autotradee", "aitotrader", "autodrader", "autotradrer",
               "autotrades", "aoutotrader", "auo trader", "autotrder", "auyotrader", "autottrader"]
SPACING_CHECK = ["auto", "trader", "blue", "black", "book", "trade", "value", "nada", "true", "car", "red", "cars"]
GROUP_KEYS = ["Calculator", "Estimator", "Blue Book", "Black Book", "Red Book", "Value", "Appraisal", "Worth",
              "Trade in", "Kelley", "KBB", "NADA", "Carfax", "True Car", "Edmunds", "Haggerty", "Cars com",
              "Auto Trader"]

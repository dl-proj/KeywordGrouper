import os

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
CORPUS_PATH = os.path.join(CUR_DIR, 'utils', 'corpus.json')

KEYWORD_CSV = os.path.join(CUR_DIR, 'Google_Automotive_KWP_CA.csv')

GROUP_MAIN_KEYS = ["Calculator", "Estimator", "Blue Book", "Black Book", "Red Book", "Value", "Appraisal", "worth",
                   "Trade-in"]
GROUP_TERM_KEYS = ["Kelley", "KBB", "NADA", "Carfax", "True Car", "Edmunds", "Haggerty", "cars.com", "Auto Trader"]

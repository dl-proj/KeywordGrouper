# KeywordGrouper

## Overview

This project is to group the keywords according to their own features using NLP technology. In this project, Spacy and 
NLTK libraries are used for creating the corpus and extarction of the features of the keyword.

## Structure

- src

    The main source code for the extraction of the features of keywords and grouping them

- utils

    * The corpus for these keywords
    * The source code for file management

- app

    The main execution file
    
- requirements

    All the dependencies for this project
    
- settings

    Several settings including some file paths and constant values
    
## Installation

- Environment

    Ubuntu 18.04, Python 3.6
    
- Dependency Installation

    Please navigate to this project directory and run the following command in the terminal.
    
    ```
        pip3 install -r requirements.txt
        python3 -m spacy download en_core_web_sm
    ```
      
## Execution

- Please set KEYWORD_CSV_FILE_PATH  in the settings file with the absolute path of the csv file to group the keywords.

- Please run the following command in the terminal.

    ```
        python3 app.py
    ```

- Then the result file will be saved in the output directory.

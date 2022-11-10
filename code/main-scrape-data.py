import pandas as pd
import os
import objects
import utils

def main():

    df_total = pd.read_csv(objects.DOC_DF)

    if os.path.exists(objects.TXT_URL_FILE):
        df_progress = pd.read_csv(objects.TXT_URL_FILE)
        completed = list(df_progress['doi'])
    else:
        completed = []
    
    df = df_total[~df_total['Digital Object Identifier'].isin(completed)]
    df = df.sample(frac=1)
    print('{}% cases already completed'.format(round(len(completed)/len(df_total)*100, 1)))
    print('Scraping {} cases'.format(len(df)))

    urls = list(df['url'])
    dois = list(df['Digital Object Identifier'])
    urls_dois = list(zip(urls, dois))

    utils.scrape_data(urls_dois, objects.TXT_URL_FILE)

    return True

if __name__ == '__main__':
    main()

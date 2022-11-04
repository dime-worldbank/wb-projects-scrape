import pandas as pd
import objects
import utils

def main():

    df_total = pd.read_csv(objects.DOC_DF)

    df_progress = pd.read_csv(objects.TXT_URL_FILE)
    completed = list(df_progress['doi'])
    df = df_total[~df_total['Digital Object Identifier'].isin(completed)]
    df = df.sample(frac=1)
    print('{}% cases already completed'.format(round(len(completed)/len(df_total)*100, 1)))
    print('Scraping {} cases'.format(len(df)))

    urls = list(df['url'])
    dois = list(df['Digital Object Identifier'])
    urls_dois = list(zip(urls, dois))

    utils.get_txt_urls(urls_dois, objects.TXT_URL_FILE)

    return True

if __name__ == '__main__':
    main()

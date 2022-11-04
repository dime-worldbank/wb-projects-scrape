import objects
import utils
import pandas as pd

def main():

    df = pd.read_csv(objects.TXT_URL_FILE)
    dois = list(df['doi'])
    urls = list(df['url'])
    dois_urls = list(zip(dois, urls))

    for i, (doi, url) in enumerate(dois_urls):

        if url != objects.DOC_NOT_AVAILABLE_MSG:
            saved = utils.get_txt_doc(url, doi)
            if not saved:
                print('\tWarning: document for DOI {} could not be downloaded'.format(str(doi)))

        if i % 200 == 0:
            print('Completed {}%'.format(round(i/len(df)*100, 1)))

    return True

if __name__ == '__main__':
    main()

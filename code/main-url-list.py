import pandas as pd
import os
import objects

def main():

    df = pd.DataFrame()
    for file in os.listdir(objects.DOC_DIR):
        if file.endswith('.xlsx'):
            df_temp = pd.read_excel(
                os.path.join(objects.DOC_DIR, file),
                engine='openpyxl'
                )
            df = pd.concat([df, df_temp]).reset_index(drop=True)

    df['url'] = objects.DOC_URL_PREFIX + df['Digital Object Identifier'].astype(str)
    df.to_csv(
        objects.DOC_DF,
        index=False,
        encoding=objects.ENCODING
        )

if __name__ == '__main__':
    main()

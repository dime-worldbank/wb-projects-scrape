import os
import utils
import objects

def main():

    files = os.listdir(objects.TXT_DOC_LOCATION)

    if os.path.exists(objects.PAD_CONTENT):
        os.remove(objects.PAD_CONTENT)

    for i, file in enumerate(files):

        if file.endswith('.txt'):

            with open(os.path.join(objects.TXT_DOC_LOCATION, file), 'r', encoding=objects.ENCODING) as text_file:
                data = text_file.read()

            doi = file.split('.')[0]
            utils.add_rows_to_csv(objects.PAD_CONTENT, ['doi', 'pad_content'], [[doi, data]])

        if i % 200 == 0:
            print('Completed {}%'.format(round(i/len(files)*100, 1)))

    return True


if __name__ == '__main__':
    main()

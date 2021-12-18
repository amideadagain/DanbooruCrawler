import urllib.request
import pandas as pd

artist_name = 'Mona-danbooru'


def url_to_jpg(url, file_path, number):
    file_format = url.split('.')[-1]
    filename = '{}-{}.{}'.format(artist_name, number, file_format)
    full_path = '{}{}'.format(file_path, filename)
    urllib.request.urlretrieve(url, full_path)

    print('{} saved'.format(filename))
    return None


FILENAME = 'img_links.csv'
FILE_PATH = 'images/'

urls = pd.read_csv(FILENAME, encoding='utf-8')

for index, link in enumerate(urls.values):
    url_to_jpg(link[0], FILE_PATH, index)

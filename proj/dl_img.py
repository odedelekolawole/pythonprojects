import urllib.request

def dl_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

link = input('Enter the URL of the download: ')
file_name = input('Enter the name of the download: ')

dl_jpg(link, 'imag/', file_name)



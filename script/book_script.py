import os
from urllib.request import urlretrieve

url = "http://www.cs.cmu.edu/~spok/grimmtmp/"
dir_name = 'stories'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
def maybe_download(filename):
    print('Downloading file: ', dir_name+os.sep + filename)

    if not os.path.exists(dir_name+os.sep+filename):
        filename, _ = urlretrieve(url + filename, dir_name+os.sep+filename)
    else:
        print('File ', filename, 'already exist')
    return filename
num_files  = 100

filenames = [format(i,'03d')+'.txt' for i in range(1,101)]

for fn in filenames:
    maybe_download(fn)

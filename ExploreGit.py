import zlib
import os
from hashlib import sha1  # SHA1 hash algorithm

dir_to_explore = '.git/objects/'
for root, dirs, files in os.walk(dir_to_explore):
     for file in files:
        with open(os.path.join(root, file), 'rb') as compressed_contents:
            read_content = compressed_contents.read()
            decompressed_contents = zlib.decompress(read_content)
            hash_value = sha1(decompressed_contents).hexdigest()
            print(hash_value + ' : Contents in ' + root + '/' + file + ' = ' + str(decompressed_contents))

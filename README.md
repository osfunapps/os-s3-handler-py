Introduction
------------

This module meant to provide intuitive functions to work with AWS's S3 for Python.

## Installation

NOTICE:  
in order to make it work, you would need to install [aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
and run *aws configure* to configure your profile.

Install via pip:

    pip install os-s3-handler


## Usage
Download file example:
```python    
from os_s3_handler import s3_handler

s3_handler.download_file(bucket_name='my_cool_bucket',
                     rel_path_to_search='path/inside/backet',
                     file_name='cool_img.png',
                     dst_dir_path='/Users/home/path/to/dst/img')
```

And more...

[GitHub - osfunappsapps](https://github.com/osfunapps)

## Licence
ISC
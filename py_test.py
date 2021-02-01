from os_s3_handler import s3_handler

s3_handler.download_file(bucket_name='bucket',
                         rel_path_to_search='/a/b/c/d',
                         file_name='file.png',
                         dst_dir_path='/dst/path/for/file')

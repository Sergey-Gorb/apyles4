from pathlib import Path
import hashlib


def get_str_md5(fh):
    for st_r in fh.readlines():
        md5_hex = hashlib.md5(st_r.encode()).hexdigest()
        yield st_r, md5_hex


p = Path('.')
f_name = p.cwd() / 'recipes.txt'
f = open(f_name, 'r', encoding='UTF-8')

for ist_r, imd5_hex in get_str_md5(f):
    print(f'{ist_r} {imd5_hex}')

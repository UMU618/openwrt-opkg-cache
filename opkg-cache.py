#!/usr/bin/env python3

import conf
import os
import ssl
import urllib.request
import urllib.parse

def get_save_path(url, save_dir):
    u = urllib.parse.urlparse(url)
    s = u.path.split('/')
    path = os.sep.join(s[1:])
    return os.path.join(save_dir, path)

def download(url, save_dir):
    save_path = get_save_path(url, save_dir)
    if os.path.isfile(save_path):
        print('File', save_path, 'exists, ignored.')
        return save_path

    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req, context=ssl._create_unverified_context())
    if response.code != 200:
        print('Download', url, 'failed, status code:', response.code)
        return ''

    parent = os.path.dirname(save_path)
    if not os.path.exists(parent):
        print('makedirs:', parent)
        os.makedirs(parent)

    print('Download', url, 'to', save_path)
    with open(save_path, "wb") as f:
        f.write(response.read())

    return save_path

def download_pkgs(url, save_dir):
    path = download(url + 'Packages', save_dir)
    download(url + 'Packages.asc', save_dir)
    download(url + 'Packages.gz', save_dir)
    download(url + 'Packages.manifest', save_dir)
    download(url + 'Packages.sig', save_dir)

    print('open', path, 'for parsing...')
    with open(path, "r") as f:
        for line in f.read().splitlines():
            if line.startswith(conf.PREFIX):
                download(url + line[len(conf.PREFIX):], save_dir)

# s = urllib.parse.urlparse('http://downloads.openwrt.org/releases/18.06.4/targets/ramips/mt7620/')
# base_url = s.scheme + '://' + s.netloc + s.path
# if not base_url.endswith('/'):
#     base_url += '/'
# print('base_url:', base_url)
# download(base_url + 'sha256sums.asc', save_dir)
# path = download(base_url + 'sha256sums', save_dir)
# print('open', path, 'for parsing...')
# with open(path, "r") as f:
#     for line in f.read().splitlines():
#         p2 = line.split(' ')[1]
#         if p2.startswith('*packages'):
#             download(base_url + p2[1:], save_dir)

if __name__ == '__main__':
    cd = os.path.dirname(os.path.abspath(__file__))
    save_dir = os.path.abspath(os.path.join(cd, conf.save_dir))
    print('save_dir:', save_dir)

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for url in conf.urls:
        if not url.endswith('/'):
            url += '/'
        download_pkgs(url, save_dir)

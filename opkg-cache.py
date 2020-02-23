#!/usr/bin/env python3

import argparse
import conf
import os
import ssl
import urllib.request
import urllib.parse
import hashlib


def get_save_path(url, save_dir):
    u = urllib.parse.urlparse(url)
    s = u.path.split('/')
    path = os.sep.join(s[1:])
    return os.path.join(save_dir, path)


def download(url, save_dir, update_exists=False):
    save_path = get_save_path(url, save_dir)
    if not update_exists and os.path.isfile(save_path):
        #print('File', save_path, 'exists, ignored.')
        return save_path

    print('Downloading', url, 'to', save_path)
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(
        req, context=ssl._create_unverified_context())
    if response.code != 200:
        print('Download', url, 'failed, status code:', response.code)
        return ''

    parent = os.path.dirname(save_path)
    if not os.path.exists(parent):
        print('makedirs:', parent)
        os.makedirs(parent)

    with open(save_path, "wb") as f:
        f.write(response.read())

    return save_path


def get_file_hash(path):
    file = open(path, "rb")
    h = hashlib.sha256()
    while True:
        buffer = file.read(4096)
        if len(buffer) < 1:
            break
        h.update(buffer)
    file.close()
    return h.hexdigest()


def download_pkgs(url, save_dir, packages_first, skip_kmod, update):
    path = download(url + 'Packages', save_dir, packages_first and update)
    if packages_first:
        download(url + 'Packages.asc', save_dir, update)
        download(url + 'Packages.gz', save_dir, update)
        download(url + 'Packages.manifest', save_dir, update)
        download(url + 'Packages.sig', save_dir, update)
    else:
        print('open', path, 'for parsing...')
        with open(path, "r") as f:
            last_pkg = ''
            size = 0
            skip = False
            for line in f.read().splitlines():
                if line.startswith(conf.FILENAME):
                    filename = line[len(conf.FILENAME):]
                    if skip_kmod and filename.startswith('kmod-'):
                        skip = True
                        print('Skipping', filename)
                        continue
                    skip = False
                    last_pkg = download(url + filename, save_dir)
                elif line.startswith(conf.SIZE) and not skip:
                    size = int(line[len(conf.SIZE):])
                elif line.startswith(conf.HASH) and not skip:
                    actual_size = os.path.getsize(last_pkg)
                    if size == actual_size:
                        hash = line[len(conf.HASH):]
                        actual_hash = get_file_hash(last_pkg)
                        if hash != actual_hash:
                            print('Hash of', last_pkg, 'is',
                                actual_hash, 'should be', hash)
                            download(url + filename, save_dir, True)
                        #else:
                        #    print('Hash of', last_pkg, 'checked')
                    else:
                        print('Size of', last_pkg, 'is',
                            actual_size, 'should be', size)
                        download(url + filename, save_dir, True)

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
    parser = argparse.ArgumentParser(description='Download packages for opkg')
    parser.add_argument('--skip-kmod', '-k', help='skip kmod', action='store_const', required=False, const=True)
    parser.add_argument('--update', '-u', help='update packages', action='store_const', required=False, const=True)
    args = parser.parse_args()
    if args.skip_kmod:
        print('Skip kmod.')
    if args.update:
        print('Update packages.')

    cd = os.path.dirname(os.path.abspath(__file__))
    save_dir = os.path.abspath(os.path.join(cd, conf.save_dir))
    print('save_dir:', save_dir)

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for url in conf.urls:
        if not url.endswith('/'):
            url += '/'
        download_pkgs(url, save_dir, True, args.skip_kmod, args.update)

    for url in conf.urls:
        if not url.endswith('/'):
            url += '/'
        download_pkgs(url, save_dir, False, args.skip_kmod, args.update)

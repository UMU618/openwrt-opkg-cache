# No need to change normally
FILENAME = 'Filename: '
SIZE = 'Size: '
HASH = 'SHA256sum: '

# newifi d2
urls = [
    'http://downloads.openwrt.org/releases/19.07.1/targets/ramips/mt7621/packages'
    , 'http://downloads.openwrt.org/releases/19.07.1/targets/ramips/mt7621/kmods/4.14.167-1-2e88863ccdd594fb8e842df3c25842ee'
    , 'http://downloads.openwrt.org/releases/19.07.1/packages/mipsel_24kc/base'
    , 'http://downloads.openwrt.org/releases/19.07.1/packages/mipsel_24kc/luci'
    , 'http://downloads.openwrt.org/releases/19.07.1/packages/mipsel_24kc/packages'
    , 'http://downloads.openwrt.org/releases/19.07.1/packages/mipsel_24kc/routing'
    , 'http://downloads.openwrt.org/releases/19.07.1/packages/mipsel_24kc/telephony'
    ]

save_dir = './'

if __name__ == '__main__':
    print('urls:', urls)
    print('save_dir:', save_dir)

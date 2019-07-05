# No need to change normally
PREFIX = 'Filename: '

# newifi y1s
urls = [
    'http://downloads.openwrt.org/releases/18.06.4/targets/ramips/mt7620/packages'
    , 'http://downloads.openwrt.org/releases/18.06.4/targets/ramips/mt7620/kmods/4.14.131-1-f908844d5e5aab0a4b27f7d4c77655d0'
    , 'http://downloads.openwrt.org/releases/18.06.4/packages/mipsel_24kc/base'
    , 'http://downloads.openwrt.org/releases/18.06.4/packages/mipsel_24kc/luci'
    , 'http://downloads.openwrt.org/releases/18.06.4/packages/mipsel_24kc/packages'
    , 'http://downloads.openwrt.org/releases/18.06.4/packages/mipsel_24kc/routing'
    , 'http://downloads.openwrt.org/releases/18.06.4/packages/mipsel_24kc/telephony'
    ]

save_dir = './'

if __name__ == '__main__':
    print('urls:', urls)
    print('save_dir:', save_dir)

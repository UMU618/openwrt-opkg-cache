# Download openwrt packages

## Config

Modify `conf.js` as you need.

## Download

```
./opkg-cache.py
```

## Serve

Into your download directory:

```
python3 -m http.server
```

Edit `/etc/opkg/distfeeds.conf` on your router, modify the line that contains `core`

Original `/etc/opkg/distfeeds.conf` for newifi y1s:

```
src/gz openwrt_core http://downloads.openwrt.org/releases/18.06.4/targets/ramips/mt7620/packages
src/gz openwrt_kmods http://downloads.openwrt.org/releases/18.06.4/targets/ramips/mt7620/kmods/4.14.131-1-f908844d5e5aab0a4b27f7d4c77655d0
src/gz openwrt_base http://downloads.openwrt.org/releases/18.06.4/packages/mipsel_24kc/base
src/gz openwrt_luci http://downloads.openwrt.org/releases/18.06.4/packages/mipsel_24kc/luci
src/gz openwrt_packages http://downloads.openwrt.org/releases/18.06.4/packages/mipsel_24kc/packages
src/gz openwrt_routing http://downloads.openwrt.org/releases/18.06.4/packages/mipsel_24kc/routing
src/gz openwrt_telephony http://downloads.openwrt.org/releases/18.06.4/packages/mipsel_24kc/telephony
```

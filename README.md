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

The others(`base`, `luci`, `packages`, `routing`, `telephony`) is undone.

#!/usr/bin/env sh
echo "Uninstalling speedtest-cn-regular-visit..."
service speedtest-cn-regular-visit stop
service speedtest-cn-regular-visit disable
rm -rf /root/scripts/speedtest_cn_regular_visit.py
#!/usr/bin/env sh
echo "Installing speedtest-cn-regular-visit..."
mkdir -p /root/scripts
cp ./speedtest_cn_regular_visit.py /root/scripts
cp ./speedtest-cn-regular-visit /etc/init.d
chmod +x /root/scripts/speedtest_cn_regular_visit.py
chmod +x /etc/init.d/speedtest-cn-regular-visit
service speedtest-cn-regular-visit enable
service speedtest-cn-regular-visit start

echo "Done!"
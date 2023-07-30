# OpenWrt SpeedTest.cn脚本
## 背景
[测速网](https://speedtest.cn)提供宽带加速服务。但其宽带加速服务并不是永久的。如果运营商分配给你的IP地址发生变化，你家宽带的加速就会失效。此时，重新访问[测速网](https://speedtest.cn)就可恢复加速。

因此，编写此脚本在OpenWrt后台运行，每十分钟访问一次[测速网](https://speedtest.cn)，以保持宽带加速服务的有效性。

## 使用方法
1. 下载本项目至OpenWrt路由器
2. 运行`install.sh`安装并启用脚本

如需卸载，运行`uninstall.sh`即可。
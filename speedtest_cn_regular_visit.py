#! /usr/bin/env python3

import urllib.request
import time
import logging
import json

# speedtest.cn提供宽带加速服务
# 但是宽带加速服务是和公网IP绑定的，当公网IP变化时，需要重新绑定，只需要访问speedtest.cn即可
# 因此，这个脚本定期访问speedtest.cn，以保持宽带加速服务的有效性

WEBSITE_URL = 'https://tisu-api.speedtest.cn/api/v2/speedup/reopen?source=www'
INTERVAL_SECONDS = 10*60  # ten minutes

# 配置logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


if __name__ == '__main__':
    while True:
        try:
            logger.info('Visiting %s' % WEBSITE_URL)
            response = urllib.request.urlopen(WEBSITE_URL)
            if response.code == 200:
                data = response.read().decode('utf-8')
                data = json.loads(data)
                if data['code'] == 0:
                    logger.info('提速成功')
                else:
                    logger.error('提速失败, %s' % data['msg'])
            else:
                logger.error('提速失败, http code: %d' % response.code)
        except Exception as e:
            print(e)
        time.sleep(INTERVAL_SECONDS)

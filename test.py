import time
from datetime import datetime
# 一些脚本
time_now = 1638751912             # 获取当前时间的时间戳
dt_now = datetime.fromtimestamp(time_now)

print(dt_now)
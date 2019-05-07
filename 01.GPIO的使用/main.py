from machine import Pin
import time

p2 = Pin(2, Pin.OUT)    # 创建一个引脚对象p2，使用GPIO2（G2）引脚，输出模式
p2.value(1)             # 设置引脚输出高电平，即板载蓝色LED熄灭

while True:
    p2.value(0)           # 设置引脚输出低电平，即板载蓝色LED点亮
    print(p2.value())     # 读取引脚的电平值，并打印
    time.sleep(3)         # 延时3秒
    p2.value(1)
    print(p2.value())
    time.sleep(3)
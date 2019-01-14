import pyb
import struct
import constants

buf_size = 16 # how much records is stored in single buffer
logging = False # do not write anything by default

def switch_callback():
    global logging
    logging = not logging
    if logging:
        pyb.LED(3).on()
    else:
        pyb.LED(3).off()

def getLogName():
    log_num = pyb.rng()
    while log_num < 100001:
        log_num = pyb.rng()
    log_num = (log_num - (log_num // 10000) * 10000)
    return '/sd/acl' + str(log_num) + '.log'

accel = pyb.Accel()
sw = pyb.Switch()
sw.callback(switch_callback)
buf = bytearray(constants.data_len * buf_size)

while True:
    pyb.wfi()
    if not logging:
        continue
    log_name = getLogName()
    with open(log_name,'wb') as log:
        idx = 0
        while logging:
            a = accel.filtered_xyz()
            buf[idx * constants.data_len:(idx + 1) * constants.data_len] = struct.pack(constants.data_fmt,a[0],a[1],a[2]) #12 bytes
            if idx == buf_size - 1:
                log.write(buf)
                idx = 0
            else:
                idx+=1
                pyb.delay(100)
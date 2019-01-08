import pyb

logging = False

def switch_callback():
    global logging
    logging = not logging
    if logging:
        pyb.LED(3).on()
    else:
        pyb.LED(3).off()

accel = pyb.Accel()
sw = pyb.Switch()
sw.callback(switch_callback)

while True:
    pyb.wfi()
    if not logging:
        continue
    log_num = pyb.rng()
    while log_num < 100001:
        log_num = pyb.rng()
    log_num = (log_num - (log_num // 10000) * 10000)
    log_name = '/sd/acl' + str(log_num) + '.log'
    with open(log_name,'w') as log:
        while logging:
            t = pyb.millis()
            x,y,z = accel.filtered_xyz()
            log.write('{},{},{},{}\n'.format(t,x,y,z))


import pyb

pyb.LED(4).on()
pyb.delay(2000)
switch_value = pyb.Switch()()
pyb.LED(4).off()

pyb.usb_mode('VCP+MSC')

if switch_value:
    pyb.main('main.py')
else:
    pyb.LED(2).on()
    pyb.delay(100)
    pyb.main('empty.py')
    pyb.LED(2).off()

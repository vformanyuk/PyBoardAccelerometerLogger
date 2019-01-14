import matplotlib.pyplot as plt
import numpy as np
import struct
import constants

x_data = []
y_data = []
z_data = []

with open('c:\\Temp\\acl4586.log','rb') as f:
    data = f.read(constants.data_len)
    while len(data) > 0:
        (x,y,z) = struct.unpack(constants.data_fmt,data)
        x_data.append(x)
        y_data.append(y)
        z_data.append(z)
        data = f.read(constants.data_len)

np_time = np.arange(0,len(x_data))
np_x = np.array(x_data)
np_y = np.array(y_data)
np_z = np.array(z_data)

fig, (ax1,ax2,ax3) = plt.subplots(1,3)
ax1.plot(np_time,np_x)
ax1.set_xlabel('time')
ax1.set_ylabel('x data')
ax2.plot(np_time,np_y)
ax2.set_xlabel('time')
ax2.set_ylabel('y data')
ax3.plot(np_time,np_z)
ax3.set_xlabel('time')
ax3.set_ylabel('z data')

plt.show()

















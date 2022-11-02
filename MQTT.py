# coding:utf-8
import codecs
import time
import serial
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import json  
import struct

def read_Main_PowerMeter(PORT,ID,loop):
    loop = loop - 1
    MainPW_meter = [0,0,0,0,0,0,0,0,0]
    try:
        master = modbus_rtu.RtuMaster(serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))
        master.set_timeout(5.0)
        master.set_verbose(True)
        pw_va = master.execute(ID, cst.READ_HOLDING_REGISTERS, 320, 1)
        pw_cur = master.execute(ID, cst.READ_HOLDING_REGISTERS, 321, 6)
        pw_power = master.execute(ID, cst.READ_HOLDING_REGISTERS, 337, 2)
        pw_pf = master.execute(ID, cst.READ_HOLDING_REGISTERS, 358, 1)
        pw_consum = master.execute(ID, cst.READ_HOLDING_REGISTERS, 385, 2)
        pw_DM = master.execute(ID, cst.READ_HOLDING_REGISTERS, 362, 2)
        
        MainPW_meter[0] = round(pw_va[0] * 0.1,1)
        MainPW_meter[1] = round(pw_cur[1] * 0.001,1)
        MainPW_meter[2] = round(pw_cur[3] * 0.001,1)
        MainPW_meter[3] = round(pw_cur[5] * 0.001,1)
        #MainPW_meter[4] = round((pw_power[1]*65536 + pw_power[0]) * 0.001,1)
        MainPW_meter[4] = round((pw_power[1]*65536 + pw_power[0]) * 0.001,1)
        MainPW_meter[5] = round(pw_pf[0]*0.1,1)
        #MainPW_meter[5] = ReadFloat((pw_consum[0],pw_consum[1]))
        MainPW_meter[6] = round((pw_consum[1]* 65536 + pw_consum[0] )*0.1,1)
        #MainPW_meter[6] = round(pw_consum[0],1)
        MainPW_meter[7] = 1
        MainPW_meter[8] = pw_consum[0] + pw_consum[1] * 65536
        master.close()
        #time.sleep(0.5)
        return (MainPW_meter)

    except:
        MainPW_meter[0] = 0
        MainPW_meter[1] = 0
        MainPW_meter[2] = 0
        MainPW_meter[3] = 0
        MainPW_meter[4] = 0
        MainPW_meter[5] = 0
        MainPW_meter[6] = 0
        MainPW_meter[7] = 2
        MainPW_meter[8] = 0
        return (MainPW_meter)
    
    if __name__ == '__main__':
    
        print(read_Main_PowerMeter('/dev/ttyS1',1,1))
        print(read_Main_PowerMeter('/dev/ttyS1',2,1))
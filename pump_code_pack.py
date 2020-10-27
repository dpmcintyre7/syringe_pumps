import serial
import argparse


def write_read(command, bytes = 10):
    print(str.encode(str(address) + command + '\r'))
    serial_port.write(str.encode(str(address) + command + '\r'))
    response = serial_port.read(bytes)
    print(response)
    print(response.decode())
    return response.decode()

def remove_string_extras(string):
    if "." in string:
        string = string.rstrip('0')
    string = string.lstrip('0 ')
    string = string.rstrip(' .')
    return string

def version(type, bytes=60):
    if(type == 0):
        version_pump = write_read('ver', bytes=bytes)
        if(version_pump[-1]=="*"):
            ctv = clear_target_volume(type,bytes=60)
            version_pump = write_read('ver', bytes=bytes)
        if(version_pump[-3:-1] == address):
            print("correct")
        else:
            print("address error")
            raise pumperror("wrong address")
    if(type == 1):
        version_pump = write_read('VER', bytes=bytes)
        if(version_pump[-1]=="*"):
            thing = clear_target_volume(type,bytes=60)
            version_pump = write_read('VER', bytes=bytes)
        if(address[0]== '0'):
            if(version_pump[-2:-1] == address[1]):
                print("correct")
            else:
                print("address error")
                raise pumperror("wrong address")
        else:
            print(address[0])
            if(version_pump[-3:-1] == address):
                print("correct")
            else:
                print("address error")
                raise pumperror("wrong address")
    
class pumperror(Exception):
    pass
    
        
def set_dia(type,diameter,bytes=60):
    if(type == 0):
        if(float(diameter) > 45 or float(diameter) < 0.1):
            raise pumperror("diameter is out of range")
        diam_resp = write_read('diameter', bytes=60) 
        #print(diam_resp)
        dia_response = remove_string_extras(remove_string_extras(diam_resp[-15:-8]))
        #print(diam_resp[-15:-8])
        #print('dia_response')
        #print(dia_response)
        if(dia_response == remove_string_extras(str(diameter))):
            print("No need to change diameter.")
        else:   
            dia = write_read('diameter ' + str(diameter), bytes=60) 
            #print(dia)
            diam = write_read('diameter', bytes=60) 
            #print(diam)
            dia_response = remove_string_extras(remove_string_extras(diam[-15:-8]))
            #print('dia_response')
            #print(dia_response)
            if(dia_response == remove_string_extras(str(diameter))):
                print("correct diameter")
            else:
                raise pumperror("Diameter not updated correctly")
    if(type == 1):
        if(float(diameter) > 45 or float(diameter) < 0.1):
            raise pumperror("diameter is out of range")
        diam_resp = write_read('DIA', bytes=60) 
        diam_response = remove_string_extras(remove_string_extras(diam_resp[3:8]))
        if(diam_response == remove_string_extras(str(diameter))):
            print("No need to change diameter.")
        else:   
            dia = write_read('DIA ' + str(diameter), bytes=60) 
            #print(dia)
            diam = write_read('DIA', bytes=60) 
            #print(diam)
            dia_response = remove_string_extras(remove_string_extras(diam[3:8]))
            #print('dia_response:')
            #print(diam[3:8])
            #print(dia_response)
            if(dia_response == remove_string_extras(str(diameter))):
                print("correct diameter")
            else:
                #print(remove_string_extras(str(diameter)))
                raise pumperror("Diameter not updated correctly")
    


def set_infuse_rate(type,infuse_rate,infuse_rate_units):
    if(type == 0):
        irate = write_read('irate ' + str(infuse_rate) +' ' + infuse_rate_units, bytes=60)
        irate_resp = write_read('irate', bytes=60)
        #print("irate_resp")
        #print(irate_resp)
        #print(irate_resp.split(':')[1])
        irate_respr=irate_resp.split(':')[1]
        #print(irate_respr[0:12])
        if "Out of range" in irate:
            print('infuse rate error...')
            raise pumperror("Infuse rate is out of range")
        if(remove_string_extras(irate_respr[0:12]).split(' ')[0] == str(infuse_rate)):
            print("updated infuse rate")
        else:
            print("didn't update infuse rate...")
            raise pumperror("Infuse Rate not updated correctly")
    if(type == 1):
        #NEED TO FIGURE THIS ONE OUT .... 
        #choices=['ul/hr', 'ul/min', 'ml/hr', 'ml/min']
        if(infuse_rate_units == 'ml/min'):
            irate = write_read('RAT ' + str(infuse_rate) + ' MM', bytes=60)
        elif(infuse_rate_units == 'ul/min'):
            irate = write_read('RAT ' + str(infuse_rate) + ' UM', bytes=60)
        elif(infuse_rate_units == 'ml/hr'):
            irate = write_read('RAT ' + str(infuse_rate) + ' MH', bytes=60)
        elif(infuse_rate_units == 'ul/hr'):
            irate = write_read('RAT ' + str(infuse_rate) + ' UH', bytes=60)
        irate_resp = write_read('RAT', bytes=60)
        if "Out of range" in irate:
            print('infuse rate error...')
            raise pumperror("Infuse rate is out of range")
        if(remove_string_extras(irate_resp[3:9]).split(' ')[0] == str(infuse_rate)):
            print("updated infuse rate")
        else:
            print("didn't update infuse rate...")
            raise pumperror("Infuse Rate not updated correctly")

def set_withdraw_rate(type,withdraw_rate,withdraw_rate_units):
    if(type == 0):
        wrate = write_read('wrate ' + str(withdraw_rate) +' ' + withdraw_rate_units, bytes=60)
        wrate_resp = write_read('wrate', bytes=60)
        wrate_respr=wrate_resp.split(':')[1]
        #print(wrate_respr[0:12])
        if "Out of range" in wrate:
            print('withdraw rate error...')
            raise pumperror("Withdraw rate is out of range")
        if(remove_string_extras(wrate_respr[0:12]).split(' ')[0] == str(withdraw_rate)):
            print("updated withdraw rate")
        else:
            print("didn't update withdraw rate...")
            raise pumperror("Withdraw Rate not updated correctly")
    if(type == 1):
        #choices=['ul/hr', 'ul/min', 'ml/hr', 'ml/min']
        if(withdraw_rate_units == 'ml/min'):
            wrate = write_read('RFR ' + str(withdraw_rate) + ' MM', bytes=60)
        elif(withdraw_rate_units == 'ul/min'):
            wrate = write_read('RFR ' + str(withdraw_rate) + ' UM', bytes=60)
        elif(withdraw_rate_units == 'ml/hr'):
            wrate = write_read('RFR ' + str(withdraw_rate) + ' MH', bytes=60)
        elif(withdraw_rate_units == 'ul/hr'):
            wrate = write_read('RFR ' + str(withdraw_rate) + ' UH', bytes=60)    
        wrate_resp = write_read('RFR', bytes=60)
        #print(wrate_resp)
        #print(wrate_resp[3:9])
        if "Out of range" in wrate:
            print('withdraw rate error...')
            raise pumperror("withdraw rate is out of range")
        if(remove_string_extras(wrate_resp[3:9]).split(' ')[0] == str(withdraw_rate)):
            print("updated withdraw rate")
        else:
            print("didn't update withdraw rate...")
            raise pumperror("Withdraw Rate not updated correctly")


def set_target_volume(type,target_volume,target_volume_units,bytes=60):
    if(type == 0):
        tvolume = write_read('tvolume ' + str(target_volume) + ' ' + target_volume_units, bytes=bytes)
    if(type == 1):
        set_vol_mode = write_read('MOD ' + 'VOL', bytes=bytes)
        if(target_volume_units == 'ul'): #'ul', 'ml
            target_v_ml = float(target_volume)/1000
            tvolume = write_read('TGT ' + str(target_v_ml), bytes=bytes)
        else:
            tvolume = write_read('TGT ' + str(target_volume), bytes=bytes)
    #if model 22 use MLT but model 44 use TGT
   

def set_syringe_volume(type,syringe_volume,syringe_volume_units,bytes=60):
    if(type == 0):
        svolume = write_read('svolume ' + str(syringe_volume) + ' ' + syringe_volume_units, bytes=bytes)
    if(type == 1):
        #no need for this one...
        if(syringe_volume_units == 'ul'): #'ul', 'ml
            syringe_v_ml = float(syringe_volume)/1000
            svolume = write_read('SYR ' + str(syringe_v_ml), bytes=bytes)
        else:
            svolume = write_read('SYR ' + str(syringe_volume), bytes=bytes)


def set_stop(type,bytes=60):
    if(type == 0):
        stop_pump = write_read('stop', bytes=bytes)
        if(stop_pump[-1] == ":"):
            print("pump stopped correctly")
        else: 
            raise pumperror("Incorrect response to stop")
    if(type == 1):
        stop_pump = write_read('STP', bytes=bytes)
        if(stop_pump[-1] == ":" or stop_pump[-1] == "*"):
            print("pump stopped correctly")
        else: 
            raise pumperror("Incorrect response to stop")

def set_irun(type,bytes=60):
    if(type == 0):
        irun_pump = write_read('irun', bytes=bytes)
        if(irun_pump[-1] == ">"):
            print("pump infusing correctly")
        else: 
            raise pumperror("Incorrect response to irun")
    if(type == 1):
        set_dir = write_read('DIR' + ' INF', bytes=bytes)
        irun_pump = write_read('RUN', bytes=bytes)
        if(irun_pump[-1] == ">"):
            print("pump infusing correctly")
        else: 
            raise pumperror("Incorrect response to irun")

def set_wrun(type,bytes=60):
    if(type == 0):
        wrun_pump = write_read('wrun', bytes=bytes)
        if(wrun_pump[-1] == "<"):
            print("pump withdrawing correctly")
        else: 
            raise pumperror("Incorrect response to wrun")
    if(type == 1):
        set_dir = write_read('DIR' + ' REF', bytes=bytes)
        wrun_pump = write_read('RUN', bytes=bytes) #model 22 uses REV
        if(wrun_pump[-1] == "<"):
            print("pump withdrawing correctly")
        else: 
            raise pumperror("Incorrect response to wrun")

def wait_for_target(type,i_or_w,bytes=60):
    if(type == 0):
        if(i_or_w == 0):
            run_pump = write_read('irun', bytes=bytes)
            i=0
            while True: 
                wait_resp = write_read('ivolume',bytes=bytes)
                #print(wait_resp)
                if ":" == wait_resp[-1] and i == 0:
                    raise pumperror("not infusing or withdrawing")
                elif "*"  == wait_resp[-1] and i !=0:
                    print('target volume has been reached')
                    break
                elif i==20:
                    break
                i= i+1
        if(i_or_w == 1):
            run_pump = write_read('wrun', bytes=bytes)
            i=0
            while True: 
                wait_resp = write_read('wvolume',bytes=bytes)
                #print(wait_resp)
                if ":" == wait_resp[-1] and i == 0:
                    raise pumperror("not infusing or withdrawing")
                elif "*"  == wait_resp[-1] and i !=0:
                    print('target volume has been reached')
                    break
                elif i==20:
                    break
                i= i+1
    if(type == 1):
        if(i_or_w == 0):
            irun = set_irun(1,bytes=60) 
            i=0
            while True: 
                wait_resp = write_read('DEL',bytes=bytes)
                #print(wait_resp)
                if ":" == wait_resp[-1] and i == 0:
                    raise pumperror("not infusing or withdrawing")
                elif ":"  == wait_resp[-1] and i !=0:
                    print('target volume has been reached')
                    break
                elif i==20:
                    break
                i= i+1
        if(i_or_w == 1):
            wrun = set_wrun(1,bytes=60) 
            i=0
            while True: 
                wait_resp = write_read('DEL',bytes=bytes)
                #print(wait_resp)
                if ":" == wait_resp[-1] and i == 0:
                    raise pumperror("not infusing or withdrawing")
                elif ":"  == wait_resp[-1] and i !=0:
                    print('target volume has been reached')
                    break
                elif i==20:
                    break
                i= i+1

def set_poll(type,i_or_w,bytes=60):
    if(type == 0):
        if(i_or_w == 0):
            poll_pump = write_read('ivolume', bytes=bytes)
        if(i_or_w == 1):
            poll_pump = write_read('wvolume', bytes=bytes)
        if(poll_pump[-1] == ":"):
            print("pump has stopped")
        elif(poll_pump[-1] == ">"):
            print("PUMP has not reached target volume and is still infusing")
        elif(poll_pump[-1] == "<"):
            print("PUMP has not reached target volume and is still withdrawing")
        else: 
            raise pumperror("Incorrect response to polling")
        
    if(type == 1):
        poll_pump = write_read('DEL', bytes=bytes)
        if(poll_pump[-1] == ":" or poll_pump[-1] == "*"):
            print("PUMP has stopped")
        elif(poll_pump[-1] == ">"):
            print("PUMP has not reached target volume and is still infusing")
        elif(poll_pump[-1] == "<"):
            print("PUMP has not reached target volume and is still withdrawing")
        else: 
            raise pumperror("Incorrect response to polling")

def clear_target_volume(type,bytes=60):
    if(type == 0):
        cv = write_read('cvolume', bytes=bytes)
        # iv = write_read('ivolume', bytes=bytes)
        # sv = write_read('svolume', bytes=bytes)
        # tv = write_read('tvolume', bytes=bytes)
        # wv = write_read('wvolume', bytes=bytes)
        # civ = write_read('civolume', bytes=bytes)
        ctv = write_read('ctvolume', bytes=bytes)
        # cwv = write_read('cwvolume', bytes=bytes)
        # iv = write_read('ivolume', bytes=bytes)
        # sv = write_read('svolume', bytes=bytes)
        # tv = write_read('tvolume', bytes=bytes)
        # wv = write_read('wvolume', bytes=bytes)
    if(type == 1):
        ctv = write_read('CLD', bytes=bytes)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='pump code')
    parser.add_argument('-p', dest='usbport', help = 'serial port')
    parser.add_argument('-a', dest='address', help = 'address')
    parser.add_argument('-d', dest='diameter', help = 'diameter in mm')
    parser.add_argument('-i', dest='infuse_rate', help = 'infuse rate')
    parser.add_argument('-iu', dest='infuse_rate_units', 
                        choices=['ul/hr', 'ul/min', 'ml/hr', 'ml/min'], 
                        help = 'infuse rate units. only choose: ul/hr, ul/min, ml/hr, ml/min ')
    parser.add_argument('-w', dest='withdraw_rate', help = 'withdraw rate')
    parser.add_argument('-wu', dest='withdraw_rate_units', 
                        choices=['ul/hr', 'ul/min', 'ml/hr', 'ml/min'], 
                        help = 'withdraw rate units. only choose: ul/hr, ul/min, ml/hr, ml/min ')
    parser.add_argument('-t', dest='target_volume', help = 'target volume')
    parser.add_argument('-tu', dest='target_volume_units', 
                        choices=['ul', 'ml'], 
                        help = 'target volume units. only choose: ul, ml')
    parser.add_argument('-s', dest='syringe_volume', help = 'syringe volume')
    parser.add_argument('-su', dest='syringe_volume_units', 
                        choices=['ul', 'ml'], 
                        help = 'syringe volume units. only choose: ul, ml')
    #parser.add_argument('-b', dest='pump_baudrate', help = 'target volume')
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-infuse', action='store_true')
    group.add_argument('-withdraw', action="store_true")
    group.add_argument('-stop', action="store_true")
    group.add_argument('-infuse_wait', action="store_true")
    group.add_argument('-withdraw_wait', action="store_true")
    group.add_argument('-poll', action="store_true")
    group.add_argument('-poll_infuse', action="store_true")
    group.add_argument('-poll_withdraw', action="store_true")
    
    
    pumpgroup = parser.add_mutually_exclusive_group()
    pumpgroup.add_argument('-PHD2000', help='To control PHD2000',
                           action='store_true')
    pumpgroup.add_argument('-PHDULTRA', help='To control PHD Ultra',
                           action='store_true')
    args = parser.parse_args()
    
    print("Make sure you have set the address the pump address on the physical pump")
    print("also, make sure you have the correct baud rate on the pump: baud rate = 9600") 
        
    serial_port = serial.Serial(port = args.usbport, baudrate = 9600, stopbits=2,timeout=2)
    serial_port.flushOutput()
    serial_port.flushInput()
    
    address = '{0:02.0f}'.format(int(args.address))
    print('this is address')
    print(address)
    try:
        if args.PHDULTRA:
            vers = version(0,50)
            
            pump_type = 0
            if args.stop:
                stop_pump = set_stop(pump_type,bytes=60)
            elif args.poll:
                poll_pump = set_poll(pump_type,0,bytes=60)
            elif args.poll_infuse:
                poll_pump = set_poll(pump_type,0,bytes=60)
            elif args.poll_withdraw:
                poll_pump = set_poll(pump_type,1,bytes=60)
            else:
                if args.diameter:
                    dia_pump = set_dia(pump_type,args.diameter,bytes=60)
                if args.syringe_volume:
                    sv_pump = set_syringe_volume(pump_type,args.syringe_volume, args.syringe_volume_units,bytes=60)
                if args.target_volume:
                    ctv = clear_target_volume(pump_type,bytes=60)
                    tv_pump = set_target_volume(pump_type,args.target_volume, args.target_volume_units,bytes=60)
                if args.infuse_rate:
                    if args.infuse_rate_units:
                        ir_pump = set_infuse_rate(pump_type,args.infuse_rate, args.infuse_rate_units)
                    else: 
                        raise pumperror("Need infuse rate units")    
                if args.withdraw_rate:
                    if args.withdraw_rate_units:
                        wr_pump = set_withdraw_rate(pump_type,args.withdraw_rate, args.withdraw_rate_units)
                    else: 
                        raise pumperror("Need withdraw rate units")
                if args.infuse:
                    irun = set_irun(pump_type,bytes=60) #runs the pump in the infuse direction 
                if args.withdraw:
                    wrun = set_wrun(pump_type,bytes=60) #runs the pump in the withdraw direction 
                if args.infuse_wait:
                    iw = wait_for_target(pump_type,0,bytes=60) #runs the pump then waits for target 
                if args.withdraw_wait:
                    ww = wait_for_target(pump_type,1,bytes=60) #runs the pump then waits for target 
                
        if args.PHD2000:
            print("You are using a PHD2000, make sure the pump is in Model 44 mode")
            print("To do this, press SET, it'll say...")
            vers = version(1,30)
            pump_type = 1
            if args.stop:
                stop_pump = set_stop(pump_type,bytes=30)
            elif args.poll:
                poll_pump = set_poll(pump_type,0,bytes=30)
            elif args.poll_infuse:
                poll_pump = set_poll(pump_type,0,bytes=30)
            elif args.poll_withdraw:
                poll_pump = set_poll(pump_type,0,bytes=30)
            else:
                if args.diameter:
                    dia_pump = set_dia(pump_type,args.diameter,bytes=30)
                if args.syringe_volume:
                    sv_pump = set_syringe_volume(pump_type,args.syringe_volume, args.syringe_volume_units,bytes=30)
                    #only used for autofill... which isnt really used in phd2000... 
                    # ask more people if this would be useful...
                if args.target_volume:
                    tv_pump = set_target_volume(pump_type,args.target_volume, args.target_volume_units,bytes=30)
                else: 
                    set_pump_mode = write_read('MOD PMP', 30)
                if args.infuse_rate:
                        if args.infuse_rate_units:
                            ir_pump = set_infuse_rate(pump_type,args.infuse_rate, args.infuse_rate_units)
                        else: 
                            raise pumperror("Need infuse rate units")
                if args.infuse:
                    irun = set_irun(pump_type,bytes=30) #runs the pump in the infuse direction    
                if args.withdraw:
                    if args.withdraw_rate:
                        if args.withdraw_rate_units:
                            wr_pump = set_withdraw_rate(pump_type,args.withdraw_rate, args.withdraw_rate_units)
                        else: 
                            raise pumperror("Need withdraw rate units")
                    wrun = set_wrun(pump_type,bytes=30) #runs the pump in the withdraw direction
                if args.infuse_wait:
                    if args.target_volume: 
                        #irun = set_irun(pump_type,bytes=60) #runs the pump in the infuse direction   
                        iw = wait_for_target(pump_type,0,bytes=30) #runs the pump then waits for target 
                    else: 
                        raise pumperror("Need target volume")
                if args.withdraw_wait:
                    if args.target_volume: 
                        if args.withdraw_rate:
                            if args.withdraw_rate_units:
                                wr_pump = set_withdraw_rate(pump_type,args.withdraw_rate, args.withdraw_rate_units)
                            else: 
                                raise pumperror("Need withdraw rate units")
                        #irun = set_irun(pump_type,bytes=60) #runs the pump in the infuse direction   
                        ww = wait_for_target(pump_type,1,bytes=30) #runs the pump then waits for target 
                    else: 
                        raise pumperror("Need target volume")
                
                

    finally:
        serial_port.close()
            
            
    











# Syringe Pump Automation 

## Table of Contents  
1. [Requirements](#reqs)  
2. [Connecting pumps to computer](#connecting) 
   1. [PHD 2000 connections and set up](#phd2000connecting)
   2. [PHD Ultra connections and set up](#phdultraconnecting)
3. [Checking Device Manager](#devicemanager)
4. [Features Summary](#features)
5. [Command Line Usage](#commandline)
6. [Python Script Usage](#pythonscript)

<a name="reqs"></a>
## Requirements 
- Python
- Pyserial 
- Argparse 
- USB-serial adapter
- For PHD2000
  - Serial to RJ-11 adapter
  - RJ-11 to RJ-11 cable
  - For chaining: multiple RJ-11 cables 
- For PHD Ultra
  - For chaining: multiple RS-485 cables
- Cables to connect each pump to power 

<a name="connecting"></a>
## Connecting pumps to computer 
<a name="phd2000connecting"></a>
### PHD 2000 connections and set up
![PHD 2000](https://github.com/CIDARLAB/syringe_pumps/blob/main/pump_connections/phd2000_pic.PNG)
![PHD 2000_back](https://github.com/CIDARLAB/syringe_pumps/blob/main/pump_connections/phd2000_back.jpg)
![PHD 2000_cables](https://github.com/CIDARLAB/syringe_pumps/blob/main/pump_connections/PHD2000_cables.png)
1. Connect USB-serial adapter to computer
2. Connect DB-9 serial to RJ-11 adapter
3. Connect RJ-11 cable to adapter and to the RS-232 IN port of the pump with address 00
4. If chaining, connect second RJ-11 cable to RS-232 OUT port of the pump with address 00 and the RS-232 IN port of the pump with address 01.
5. Continue connecting the RJ-11 cables to the pumps in address order (can only connect max 99 pumps) 
6. Make sure pumps are set to Model 44 Protocol (Press SET key, press 1, press enter once Model 44 is displayed) 
7. Check pump chain configurations:
   1. Press SET key
   2. Use RS232 key to scroll until "Pump Chain" is displayed
   3. When "Pump Chain" is displayed press enter
   4. Type in address and press enter
   5. Type in baud rate (baud rate of 9600 is used for this code) and press enter
   6. Press enter one last time to save input
   7. If chaining, all pumps need to have the same Baud Rate, and the first pump in the chain needs to have address 00

<a name="phdultraconnecting"></a>
### PHD Ultra connections and set up
![PHD Ultra_back](https://github.com/CIDARLAB/syringe_pumps/blob/main/pump_connections/ultra_back.jpg)
![PHD Ultra_cables](https://github.com/CIDARLAB/syringe_pumps/blob/main/pump_connections/PHDULTRA_cables.png)
1. Connect USB-serial adapter to computer (if needed connect to male-to-male gender changer) and the RS-232 IN port of the pump with address 00
2. If chaining, connect IEEE 1394 cable to the RS-485 OUT port of the pump with address 00 and the RS-485 IN port of the pump with address 01.
3. Continue connecting the IEEE 1394 cables to the pumps in address order (can only connect max 99 pumps)
4. Check Pump Chain configurations: 
   1. Go to Settings menu
   2. Choose Pump Address button and enter pump address 
   3. Press Accept to save chages 
   4. From Settings menu, choose Pump Baud Rate and enter baud rate (9600 is used for this code)
   5. If chaining, all pumps need to have the same Baud Rate, and the first pump in the chain needs to have address 00 

<a name="devicemanager"></a>
## Checking Device Manager 
If the computer port connected to the pumps is unkown, check the name of the port. 
1. Open Device Manager, on windows 10, by searching for "Device Manager" on the search field in the taskbar. 
2. Double click on "Ports (COM & LPT)" 
3. Find the "Prolific USB-to-Serial Comm Port" 
4. The name of the port is in parenthesis next to "Prolific USB-to-Serial Comm Port"
5. If the names don't match exactly, look for another a name that is similar to "USB-to-Serial" 

<a name="features"></a>
## Features Summary
- set diameter
- set infuse/withdraw rate
- set target volume
- set syringe volume
- infuse or withdraw indefinitely
- infuse or withdraw to a target volume 
- infuse or withdraw to a target volume and wait until volume has been reached
- check if target volume has been reached (poll) 


<a name="commandline"></a>
## Command Line Usage 
Run ```python pump_code_pack.py --help ``` to see command line options.

### Stop
Run the following, to stop the PHD2000 pump at address 00 using COM4 port
```
python pump_code_pack.py -p COM4 -a 0 -stop -PHD2000
```
### Run indefinitely 
Set the PHD2000 pump at address 00 using COM4 port to infuse indefinitely with the parameters: syringe diameter (12 mm) and infuse rate (1 ml/min)
```
python pump_code_pack.py -p COM4 -a 0 -d 12 -i 1 -iu ml/min -infuse -PHD2000
```
Set the PHD2000 pump at address 00 using COM4 port to withdraw indefinitely with the parameters: syringe diameter (12 mm) and withdraw rate (2 ml/min)
```
python pump_code_pack.py -p COM4 -a 0 -d 12 -w 2 -wu ml/min -withdraw -PHD2000
```
### Run pump and eventually stop once target volume has been reached 
Set the PHD2000 pump at address 00 using COM4 port to infuse (and stop once target volume has been reached) with the parameters: syringe diameter (12 mm), infuse rate (1 ml/min), target volume (1 ml)
```
python pump_code_pack.py -p COM4 -a 0 -d 12 -i 1 -iu ml/min -t 1 -tu ml -infuse -PHD2000
```
Set the PHD2000 pump at address 00 using COM4 port to withdraw (and stop once target volume has been reached) with the parameters: syringe diameter (12 mm), withdraw rate (2 ml/min), target volume (1 ml)
```
python pump_code_pack.py -p COM4 -a 0 -d 12 -w 2 -wu ml/min -t 1 -tu ml -withdraw -PHD2000
```
### Run pump and wait for target volume to be reached 
Set the PHD2000 pump at address 00 using COM4 port to infuse (and wait for target volume to be reached) with the parameters: syringe diameter (12 mm), infuse rate (1 ml/min), target volume (1 ml)
```
python pump_code_pack.py -p COM4 -a 0 -d 12 -i 1 -iu ml/min -t 1 -tu ml -infuse_wait -PHD2000
```
Set the PHD2000 pump at address 00 using COM4 port to withdraw  (and wait for target volume to be reached) with the parameters: syringe diameter (12 mm), withdraw rate (2 ml/min), target volume (1 ml)
```
python pump_code_pack.py -p COM4 -a 0 -d 12 -w 2 -wu ml/min -t 1 -tu ml -withdraw_wait -PHD2000
```
### Check if target volume has been reached (Poll)
First, pump needs to be running (with -infuse or -withdraw and target volume).
Run the following, to poll PHD2000 pump at address 00 using COM4 port
```
python pump_code_pack.py -p COM4 -a 0 -poll -PHD2000
```


<a name="pythonscript"></a>
## Python Script Usage 

### Set Up
Import logging and pump_code_pack
```
import pump_code_pack
import logging
```
To allow logging functionality, add in the following code. Substitute "example.log" the name of the log file you would like to add to
```
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(filename='example.log', level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
```
Define the serial connection and pumps 
```
sc_com4 = pump_code_pack.Serial_connection('COM4')
address = 0
pump_2000_1 = pump_code_pack.Pump2000(sc_com4,address, name='PHD2000_1')
address = 1
pump_2000_2 = pump_code_pack.Pump2000(sc_com4,address, name='PHD2000_2')
```

### Stop 
After the pumps have been defined, run the following to stop pumps
```
pump_2000_1.set_stop()
pump_2000_2.set_stop()
```

### Run Indefinitely  
After the pumps have been defined, run the following to infuse indefinitely with a syringe diameter of 9.52 mm, infuse rate of 10 ul/min. The "set_pump_mode()" command is only used for PHD 2000 pumps to run indefinitely.
```
diameter = 9.52
pump_2000_1.set_dia(diameter)

pump_2000_1.set_pump_mode()

infuse_rate = 10
infuse_rate_units = 'ul/min'
pump_2000_1.set_infuse_rate(infuse_rate, infuse_rate_units)

pump_2000_1.set_irun()
```
After the pumps have been defined, run the following to withdraw indefinitely with a syringe diameter of 9.52 mm, withdraw rate of 12 ul/min. The "set_pump_mode()" command is only used for PHD 2000 pumps to run indefinitely.
```
diameter = 9.52
pump_2000_2.set_dia(diameter)

pump_2000_2.set_pump_mode()

withdraw_rate = 12
withdraw_rate_units = 'ul/min'
pump_2000_2.set_withdraw_rate(withdraw_rate, withdraw_rate_units)

pump_2000_2.set_wrun()
```
### Run pump and eventually stop once target volume has been reached 
After the pumps have been defined, run the following to infuse and stop at target volume with the parameters: syringe diameter (9.52 mm), target volume (1 ml), and infuse rate (10 ul/min). 
```
diameter = 9.52
pump_2000_1.set_dia(diameter)

target_volume = 1
target_volume_units = 'ml'
pump_2000_1.set_target_volume(target_volume, target_volume_units)

infuse_rate = 10
infuse_rate_units = 'ul/min'
pump_2000_1.set_infuse_rate(infuse_rate, infuse_rate_units)

pump_2000_1.set_irun()
```
After the pumps have been defined, run the following to infuse and stop at target volume with the parameters: syringe diameter (9.52 mm), target volume (1 ml), and withdraw rate (10 ul/min). 
```
diameter = 9.52
pump_2000_2.set_dia(diameter)

target_volume = 1
target_volume_units = 'ml'
pump_2000_2.set_target_volume(target_volume, target_volume_units)  # set target volume 

withdraw_rate = 12
withdraw_rate_units = 'ul/min'
pump_2000_2.set_withdraw_rate(withdraw_rate, withdraw_rate_units) # set withdraw rate 

pump_2000_2.set_wrun() # withdraw and wait for target volume
```
### Run pump and wait for target volume to be reached 
After the pumps have been defined, run the following to infuse (and wait for target volume to be reached) with the parameters: syringe diameter (9.52 mm), target volume (1 ml), and infuse rate (10 ul/min). 
```
diameter = 9.52
pump_2000_1.set_dia(diameter)

target_volume = 1
target_volume_units = 'ml'
pump_2000_1.set_target_volume(target_volume, target_volume_units) # set target volume 

infuse_rate = 10
infuse_rate_units = 'ul/min'
pump_2000_1.set_infuse_rate(infuse_rate, infuse_rate_units) # set infuse rate with infuse rate units 

pump_2000_1.wait_for_target(i_or_w="infuse") # infuse and wait for target volume
```
After the pumps have been defined, run the following to withdraw (and wait for target volume to be reached) with the parameters: syringe diameter (9.52 mm), target volume (1 ml), and withdaw rate (12 ul/min). 
```
diameter = 9.52
pump_2000_2.set_dia(diameter) # set syringe diameter

target_volume = 1
target_volume_units = 'ml'
pump_2000_2.set_target_volume(target_volume, target_volume_units) # set target volume

withdraw_rate = 12
withdraw_rate_units = 'ul/min'
pump_2000_2.set_withdraw_rate(withdraw_rate, withdraw_rate_units) # set withdraw rate 

pump_2000_2.wait_for_target(i_or_w="withdraw") # wuthdraw and wait for target volume
```
### Check if target volume has been reached (Poll)
After the pumps have been defined and set to run in either infuse or withdraw, run the following to poll pump (check if target volume has been reached)
```
pump_2000_1.set_poll(i_or_w = "infuse")
pump_2000_2.set_poll(i_or_w = "withdraw")
```

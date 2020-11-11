# syringe_pumps

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

## Connecting pumps to computer 
For PHD2000
![PHD 2000](https://github.com/CIDARLAB/syringe_pumps/blob/main/pump_connections/phd2000_pic.PNG)
1. Connect USB-serial adapter to computer
2. Connect DB-9 serial to serial to RJ-11 adapter
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

For PHD Ultra
1. Connect USB-serial adapter to computer and the RS-485 IN port of the pump with address 00
2. If chaining, connect IEEE 1394 cable to the RS-485 OUT port of the pump with address 00 and the RS-485 IN port of the pump with address 01.
3. Continue connecting the IEEE 1394 cables to the pumps in address order (can only connect max 99 pumps)
4. Check Pump Chain configurations: 
   1. Go to Settings menu
   2. Choose Pump Address button and enter pump address 
   3. Press Accept to save chages 
   4. From Settings menu, choose Pump Baud Rate and enter baud rate (9600 is used for this code)
   5. If chaining, all pumps need to have the same Baud Rate, and the first pump in the chain needs to have address 00 

## Checking Device Manager 
If the computer port connected to the pumps is unkown, check the name of the port. 
1. Open Device Manager, on windows 10, by searching for "Device Manager" on the search field in the taskbar. 
2. Double click on "Ports (COM & LPT)" 
3. Find the "Prolific USB-to-Serial Comm Port" 
4. The name of the port is in parenthesis next to "Prolific USB-to-Serial Comm Port"
5. If the names don't match exactly, look for another a name that is similar to "USB-to-Serial" 

## Features
- set diameter
- set infuse/withdraw rate
- set target volume
- set syringe volume
- infuse or withdraw indefinitely
- infuse or withdraw to a target volume 
- infuse or withdraw to a target volume and wait until volume has been reached
- check if target volume has been reached (poll) 

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




# Belja80
 
TKL keyboard based on the RP2040 microcontroller.

# Flashing instructions
* Plug keyboard into computer, RP2040 drive should appear. It might be necessary to hold down the boot button while plugging in the board for the drive to appear.
* Install Adafruit circuitpython, version 8 or newer. The drive will dissapear and a drive named "CIRCUITPY" will appear.
* Copy the folder named "kmk" from the (https://github.com/KMKfw/kmk_firmware)[kmk_firmware-master repository] to the "CIRCUIUTPY" drive.
* Copy the supplied python files in the "Belja80_firmware" folder to the CIRCUITPY drive.

The keyboard should now work. When plugging in the keyboard next time, the board will not appear as a drive. To let the keyboard appear as a drive, hold in Esc while plugging the keyboard into your computer.

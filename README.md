# Belja80
 
TKL keyboard based on the RP2040 microcontroller.

# Flashing instructions
* Plug the keyboard into a computer and a drive named "RP2040" should appear. It might be necessary to hold down the boot button while plugging in the board for the drive to appear.
* Install [Adafruit circuitpython for the Raspberry Pi Pico](https://circuitpython.org/board/raspberry_pi_pico/), version 8 or newer. This is done by copying the .uf2 file to the RP2040 drive. The drive will dissapear briefly and a drive named "CIRCUITPY" will appear.
* Copy the folder named "kmk" from the [kmk_firmware-master repository](https://github.com/KMKfw/kmk_firmware) to the CIRCUIUTPY drive.
* Copy the supplied python files in the "Belja80_firmware" folder to the CIRCUITPY drive.

The keyboard should now work. When plugging in the keyboard next time, the board will not appear as a drive. To let the keyboard appear as a drive, hold in Esc while plugging the keyboard into your computer.

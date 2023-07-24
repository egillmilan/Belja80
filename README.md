# Belja80
 
TKL keyboard based on the RP2040 microcontroller. Compatible with ANSI and ISO layout.
![78338884-2CD3-49FE-B128-DA2AC7E8922D](https://github.com/egillmilan/Belja80/assets/47427510/cf225241-fcc1-4281-a1d6-e38ac62e8995)
![CA066DF3-226C-4CC9-AC3D-376DD7F449F3](https://github.com/egillmilan/Belja80/assets/47427510/a255aff4-72ce-4c58-a7a9-a3ddc469b0f0)
![207D5793-591D-41C7-A5E0-8D16D3B497DB](https://github.com/egillmilan/Belja80/assets/47427510/e4c6f88b-ae04-4b1a-85b3-5e183c7b0045)


# Flashing instructions
* Plug the keyboard into a computer and a drive named "RP2040" should appear. It might be necessary to hold down the boot button while plugging in the board for the drive to appear.
* Install [Adafruit circuitpython for the Raspberry Pi Pico](https://circuitpython.org/board/raspberry_pi_pico/), version 8 or newer. This is done by copying the .uf2 file to the RP2040 drive. The drive will dissapear briefly and a drive named "CIRCUITPY" will appear.
* Copy the folder named "kmk" from the [kmk_firmware-master repository](https://github.com/KMKfw/kmk_firmware) to the CIRCUIUTPY drive.
* Copy the supplied python files in the "Belja80_firmware" folder to the CIRCUITPY drive.

The keyboard should now work. When plugging in the keyboard next time, the board will not appear as a drive. To let the keyboard appear as a drive, hold in Esc while plugging the keyboard into your computer.

# Simple-Stego
This is my first time using steganography.
I "encrypted" the text by converting every character in the string into an 8-bit binary ASCII code. This was put into a table which is referenced when the code is encoded into the image later on. This can be converted into ASCII letters. I then converted the red and green values of every pixel to binary. I took the last two digits and replaced then in two-digit increments with my 8-digit ASCII code. This difference is almost invisible to the human eye. Therefore, for every two pixel, one character was encoded. The blue value was used soley for determining whether the code had reached its end. This could be further optimized to store a 2 digit portion of ASCII code, but for now it is used for only determining whether the code has reached its end. I did this by making sure that the remainder of the blue value divided by 3 was the number of two-digit ASCII code portions that it carried. For this reason, the blue value of most of the pixels that were encoded were congruent to 2 mod 3. However, at the end of the code, there are two possibilities: if the green value is equivalent to 1 mod 3, the 2 digit ASCII code is taken from the red and the code is deemed complete, but if the green value is equivalent to 0 mod 3, then the code is deemed complete without taking any values from the red or green. Finally, to read the encoded image, the reader simply takes the last two digits of the red and green values and pieces them into 1 byte every two pixels. It makes sure that the blue value is congruent to 2 mod 3, and if it isn't, then the reader knows that it has reached the end. The bytes are then converted into ASCII letters and can be read.

# How to use

The only package you need to install is pygame. Go to cmd.exe, and type: "python -m pip install pygame" to install it. 
The writer takes in a string and creates an encoded image named "coded.png" if it doesn't already exist. If it does, then it overwrites it. The reader reads the "coded.png" file and prints out the encoded string.




# Optimizations
If the resolution of the image was x by y, then the pixels would be xy. Therefore, if I wanted to know the size of the text hidden, I could simply set away log 2 (xy)/6 pixels to print the text size(the R, G, B would change their last 2 digits for the digits of the text size). This not only would optimize the code by 33% by incorporating the use of B as another ASCII code holder, but also make the code less complicated.

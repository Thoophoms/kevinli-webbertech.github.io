# Lab - Image Steganography

## Lab 1 Hidding text into Image using Pixel Tools

### Step 1: Understanding Pixel Data

Every pixel in an image consists of three color values: Red (R), Green (G), and Blue (B). Each of these values is stored as an integer from 0 to 255.

    • Example pixel: (R: 173, G: 201, B: 124)

The least significant bit (LSB) of these values determines tiny changes that are invisible to the human eye. By tweaking these LSBs, we can hide binary data inside an image.

### Step 2: Preparing Your Files

    1. Choose a PNG image
        ◦ Use any small, simple image (less than 500x500 pixels is ideal).
        ◦ Open it in a basic image editor like Microsoft Paint (Windows) or Preview (Mac).
        
        ![stenography-1](../../../../images/computer_forensic/stenography/stenography-1.png)
        
    2. Prepare Your Secret Message
        ◦ Convert your message to binary using an online ASCII to binary converter or a calculator.
        ◦ Example:
            ▪ "NYC" → 01001110 01011001 01000011
        ◦ Add a stop sequence (11111111 11111110) to mark the end.

### Step 3: Hiding the Message

    1. Open the PNG file in an Image Editor
        ◦ Zoom in and select individual pixels for editing.
        ◦ Check the RGB values of a few pixels.

        ![stenography-2](../../../../images/computer_forensic/stenography/stenography-2.png)

    2. Modify the Least Significant Bit (LSB)
        ◦ Convert the pixel values to binary.
        ◦ Example: A pixel with values (62, 80, 90) in binary:
            ▪ 62 → 00111110
            ▪ 80 → 01010000
            ▪ 90 → 01011010

        ![stenography-3.png](../../../../images/computer_forensic/stenography/stenography-3.png)

        ◦ Modify the last bit of each color channel to match the binary message.
        ◦ Example (hiding "NYC" in two pixels):
            ▪ Before: (62, 80, 90) → 00111110 01010000 01011010
            ▪ After: (62, 81, 90) → 00111110 01010001 01011010
            ▪ Since "NYC" requires 8 pixels, the process continues across multiple pixels until the full message is embedded.

        ![stenography-4](../../../../images/computer_forensic/stenography/stenography-4.png)

    3. Save the Image
        ◦ Export the modified image as a new PNG file.

### Step 4: Extracting the Hidden Message

    1. Open the PNG File Again
        ◦ Pick the same pixels you modified.
        ◦ Convert their RGB values back to binary.

    2. Extract the Last Bits
        ◦ Read the LSB from each value and reconstruct the message.
        ◦ Stop when you reach the stop sequence (11111111 11111110).

    3. Convert Back to Text
        ◦ Group the extracted bits into 8-bit segments.
        ◦ Convert them back to characters using an ASCII table.


## Youtube Video

<iframe width="420" height="315" src="https://www.youtube.com/embed/jTxrCDd9sc4"></iframe>

## ref

- https://www.garykessler.net/library/fsc_stego.html

- https://forensicstats.org/steganography/
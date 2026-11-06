# Signed and unsigned number

* binary format bit size and its ranges (such as 4 bits, 8 bits, 16 bits, 32 bits and more)

* signed and unsigned integer (including +0 and -0)

* signed and unsigned real

* overflow (!!)

## Converting from decimal to binary

```shell
To convert \(-13\) to 8-bit binary using the two's complement method, follow these steps:

1. **Convert 13 to binary**:
   - \(13\) in binary (using 8 bits) is `00001101`.

2. **Invert the bits** (flip 0s to 1s and 1s to 0s):
   - `00001101` becomes `11110010`.

3. **Add 1 to the result**:
   - `11110010 + 1` equals `11110011`.

So, \(-13\) in 8-bit two's complement binary is `11110011`.
```

>Hint: from chatGPT

## Converting from binary to decimal

```shell
To convert \(-126\) to 8-bit binary using the two's complement method, follow these steps:

1. **Convert 126 to binary**:
   - \(126\) in binary (using 8 bits) is `01111110`.

2. **Invert the bits** (flip 0s to 1s and 1s to 0s):
   - `01111110` becomes `10000001`.

3. **Add 1 to the result**:
   - `10000001 + 1` equals `10000010`.

So, \(-126\) in 8-bit two's complement binary is `10000010`.
```

>Hint: from chatGPT

## In class lab

**Question:**

`1, -1, 10, -10, 50, -50, 99, -99, 126, -126 in binary format with 8 bits representation`

Please calculate these by hand and paste it in our discussion forum.
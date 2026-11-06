# **🕵️‍♂️ Steganography – Hiding Data in Plain Sight**
Steganography is the practice of **hiding information inside files** (e.g., images, audio, videos, and documents) so that the existence of the hidden data is not apparent.

---

## **📂 Types of Steganography**
1. **Image Steganography** – Hide data in images (`.png, .jpg, .bmp`).
2. **Audio Steganography** – Embed messages in audio files.
3. **Video Steganography** – Conceal information in video files.
4. **Text Steganography** – Hide data within text files (e.g., invisible characters, homoglyphs).
5. **Network Steganography** – Hide data in network packets.

---

## **🔍 1. Image Steganography Using `steghide`**
**`steghide`** is a tool for embedding data inside images and extracting it.

### **🛠 Install `steghide`**
#### **Linux (Debian/Ubuntu)**
```bash
sudo apt install steghide
```
#### **macOS**
```bash
brew install steghide
```
#### **Windows**
Download [Steghide for Windows](https://steghide.sourceforge.net/) and install.

### **🔹 Hide a Secret Message Inside an Image**
```bash
steghide embed -cf image.jpg -ef secret.txt -p password123
```
🔹 **Breakdown**:
- `-cf image.jpg` → Cover file (image)
- `-ef secret.txt` → File to embed
- `-p password123` → Encryption password

### **🔍 Extract Hidden Data from an Image**
```bash
steghide extract -sf image.jpg -p password123
```
🔹 This retrieves `secret.txt` from `image.jpg`.

---

## **🎵 2. Audio Steganography Using `steganography` (Python)**
You can embed messages inside audio files.

### **Install the Python Library**
```bash
pip install steganography
```

### **🔹 Hide a Secret in an Audio File**
```python
from steganography.steganography import Steganography
Steganography.encode("input_audio.wav", "output_audio.wav", "This is a secret message")
```
### **🔍 Extract Hidden Message**
```python
message = Steganography.decode("output_audio.wav")
print("Hidden Message:", message)
```

---

## **📺 3. Video Steganography Using `OpenStego`**
OpenStego supports embedding hidden files into videos.

### **🔹 Hide a Secret in a Video**
```bash
ffmpeg -i input.mp4 -vf "drawtext=text='hidden text':x=100:y=100" output.mp4
```
🔹 This embeds "hidden text" inside the video.

---

## **📜 4. Text Steganography Using `Snow`**
The **`snow`** tool hides messages inside spaces and tabs.

### **Install `snow`**
```bash
sudo apt install snow
```

### **🔹 Hide a Message in Text**
```bash
snow -C -m "This is a secret" -p password -o secret.txt
```
### **🔍 Extract Hidden Message**
```bash
snow -C -p password -o recovered_message.txt secret.txt
```

---

## **🕵️ 5. Detecting Steganography (Steganalysis)**
To **detect hidden messages**, use:
```bash
steghide info image.jpg
```
or
```bash
binwalk -e image.jpg
```
🔹 If a file contains **anomalous metadata or extra bytes**, it may contain hidden data.

---

## Ref

- ChatGPT

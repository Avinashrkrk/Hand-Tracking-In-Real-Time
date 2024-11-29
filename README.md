## Hand-Tracking-In-Real-Time
This repository provides a Python-based implementation for real-time hand tracking using the MediaPipe library. It includes scripts to process live webcam feeds and video files, enabling robust applications like gesture recognition, interactive systems, and more.

## Demo Video
https://github.com/user-attachments/assets/ca682445-74b6-4f16-9959-6ab1ef023c86


https://github.com/user-attachments/assets/9ef59a05-6bd6-4ea7-92e4-d426fc11dc70


## Features
* Real-Time Hand Detection: Tracks hands using a live webcam feed.
* Video File Processing: Tracks hands in pre-recorded video files.
* Output with Overlays: Visualizes tracked hand landmarks in the processed output.

**Installation and Setup**
1. **Clone the Repository**
  Use the following command to clone the repository:
  ```bash
  git clone https://github.com/Avinashrkrk/Hand-Tracking-In-Real-Time.git
  cd Hand-Tracking-In-Real-Time
```
2. **Install Dependencies**
   Install the required Python libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```
3. **Prepare Input Files (Optional)**
   - Place video files in the Input folder for processing.
   - Ensure your webcam is connected for real-time tracking.

## Usage Instructions
1. **Hand Tracking from Live Webcam**
   Run the following command to start hand tracking using a webcam feed:
   ```bash
   python Hand-Tracking-In-Real-Time.py
   ```
2. **Hand Tracking in Video Files**
   To process hand tracking on pre-recorded videos:
   1. Place input videos in the Input_videos folder.
   2. Run the script:
      ```bash
      python HandTracking-from-video.py
      ```
   3. Processed videos with hand landmarks will be saved in the output_videos folder.

## Project Structure
- Hand-Tracking-In-Real-Time.py: Script for real-time hand tracking via webcam.
- HandTracking-from-video.py: Script for processing hand tracking in video files.
- Input_videos/: Folder for storing video files for processing.
- output_videos/: Folder for saving processed videos
- requirements.txt: File specifying required dependencies

## Applications
* Gesture-controlled interfaces
* Augmented and Virtual Reality
* Gaming and interactive systems
* Sign language recognition

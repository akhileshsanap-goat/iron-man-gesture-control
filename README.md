# 🦾 Iron Man Gesture Control System

A Python-based virtual interface that lets you control your computer using hand gestures, inspired by Tony Stark's Iron Man interface!

## ✨ Features

- **Hand Detection & Tracking** - Real-time hand tracking using MediaPipe
- **Gesture Recognition** - Multiple gesture commands (Point, Grab, Palm, Thumbs Up, etc.)
- **Mouse Control** - Move cursor and click using hand gestures
- **Keyboard Simulation** - Trigger keyboard commands with gestures
- **Iron Man UI** - Visual interface inspired by Iron Man's HUD
- **Customizable Gestures** - Easy to add new gesture commands
- **Performance Optimized** - Real-time processing with minimal latency

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Webcam
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/akhileshsanap-goat/iron-man-gesture-control.git
   cd iron-man-gesture-control
   ```

2. **Create virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the system**
   ```bash
   python main.py
   ```

## 🎮 Gesture Commands

| Gesture | Action | Description |
|---------|--------|-------------|
| **Point** | Move Mouse | Index finger pointing moves cursor |
| **Grab** | Left Click | Closed fist clicks |
| **Two Fingers** | Right Click | Index + Middle finger extended |
| **Open Palm** | Double Click | All fingers spread |
| **Thumbs Up** | Screenshot | Thumb pointing up |
| **Peace Sign** | Volume Control | Two fingers in peace gesture |
| **Pinch** | Scroll | Thumb + Index finger pinch |

## 📁 Project Structure

```
iron-man-gesture-control/
├── main.py                 # Main application entry point
├── gesture_detector.py     # Hand gesture detection logic
├── hand_tracker.py         # MediaPipe hand tracking
├── ui_renderer.py          # Iron Man-style UI rendering
├── mouse_controller.py     # Mouse control functions
├── keyboard_controller.py  # Keyboard simulation
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🛠️ Configuration

Edit `config.py` to customize:

```python
# Gesture sensitivity
MIN_CONFIDENCE = 0.7
DETECTION_CONFIDENCE = 0.7
TRACKING_CONFIDENCE = 0.5

# Display settings
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FPS = 30

# Mouse sensitivity
MOUSE_SMOOTHING = 0.3
CLICK_THRESHOLD = 0.2
```

## 📋 Usage Examples

### Basic Usage
```python
from main import GestureControlSystem

# Initialize system
system = GestureControlSystem()

# Run the gesture control
system.run()
```

### Custom Gesture Handler
```python
# Add custom gesture in gesture_detector.py
def detect_custom_gesture(hand_landmarks):
    # Your gesture logic
    return gesture_type
```

## 🎨 UI Features

- **Real-time Hand Visualization** - See hand skeleton and landmarks
- **Gesture Recognition Display** - Shows detected gesture in real-time
- **FPS Counter** - Monitor performance
- **Command Log** - View recent executed commands
- **HUD Elements** - Futuristic Iron Man-style overlay

## ⚙️ System Requirements

- **CPU**: Intel i5 / AMD Ryzen 5 or better
- **RAM**: 4GB minimum (8GB recommended)
- **GPU**: Optional (CPU works fine)
- **Display**: 1280x720 or higher
- **Webcam**: Standard USB webcam or built-in

## 🔧 Troubleshooting

### Low Detection Accuracy
- Improve lighting conditions
- Adjust `MIN_CONFIDENCE` in config.py
- Ensure hands are clearly visible

### High Latency
- Close background applications
- Reduce `WINDOW_WIDTH` and `WINDOW_HEIGHT`
- Update graphics drivers

### Webcam Not Detected
- Check webcam permissions
- Verify device index in `config.py`
- Try `python -c "import cv2; cv2.VideoCapture(0)"`

## 📚 Dependencies

- `opencv-python` - Computer vision
- `mediapipe` - Hand tracking
- `numpy` - Numerical computing
- `pyautogui` - Mouse/keyboard control
- `pynput` - Input control

## 🎯 Roadmap

- [ ] Voice commands integration
- [ ] Full body gesture support
- [ ] Hand pose estimation
- [ ] Machine learning gesture classifier
- [ ] Multi-hand support
- [ ] Gesture recording/playback
- [ ] Virtual keyboard
- [ ] Game integration

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

## 👨‍💻 Author

**Akhilesh Sanap**
- GitHub: [@akhileshsanap-goat](https://github.com/akhileshsanap-goat)

## ⭐ Show Your Support

If you like this project, please give it a star! Your support motivates me to keep improving it.

## 🚀 Let's Build the Future Together!

Feel free to fork, star, and contribute. Let's create something amazing! 🦾

---

**Note:** This is a fun project inspired by Iron Man's interface. It's designed for educational and entertainment purposes.

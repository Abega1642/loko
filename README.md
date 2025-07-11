# 🎨 loko : Real-Time Color Tracking App

**loko** is a modular, object-oriented Python application for real-time color tracking using OpenCV and Pillow. 
It detects user-defined colors in a camera stream, computes their HSV bounds, and draws bounding boxes around detected regions.

---

## 🧠 Features

- 🎯 Track any BGR color with HSV precision
- 🔍 Draw bounding boxes around live objects based on color match
- 🧱 Clean OOP architecture (extensible + testable)
- 🧪 Full `unittest` test coverage per component
- ⚙️ Plug-and-play with your webcam via OpenCV

---

## 🗂️ Project Structure

```bash
.
├── src/
│   ├── app.py                  # Main ColorTrackingApp class
│   ├── main.py                 # Entry point (launches the app)
│   └── utils/
│       ├── color_range_detector.py
│       ├── color_tracker.py
│       ├── visualizer.py
│       ├── video_stream.py
│       └── logger.py           
├── tests/                      # Unit test suite
│   ├── test_color_range_detector.py
│   ├── test_color_tracker.py
│   ├── test_visualizer.py
│   ├── test_video_stream.py
├── requirement.txt             # Dependency list
├── .flake8, .gitignore         # Code style and repo hygiene
└── LICENCE
```

---

## 🚀 Getting Started

### 🔧 Setup

1. **Clone the repo:**
   ```bash
   git clone https://github.com/Abega1642/loko.git
   cd loko
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirement.txt
   ```

### 🎨 Launch the app

Inside your virtual environment:

```bash
└─[$] python src/main.py                                                                                                                                                                                    [19:07:35]

? 🎨 Choose a color to track: (Use arrow keys)
 » yellow
   blue
   red
   orange
   purple
   black

```

### How to quit ?

Press `Q` to quit the video stream at any time.

---

## 🧪 Running Tests

Every module has 10+ secure unit tests in [`tests/`](tests). Run all tests with:

```bash
python -m unittest discover -s tests/
```

Or test a single module:

```bash
python -m unittest tests/test_color_tracker.py
```

Want `pytest` support or coverage metrics? Ask and I’ll guide you in!


## 📄 License

This project is licensed under the terms of the **MIT License** (see [`LICENCE`](LICENCE) file).


> Author: Abegà Razafindratelo

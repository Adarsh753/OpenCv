
# Traffic Light Detection using OpenCV

This project demonstrates how to use **OpenCV** to detect traffic lights in real-time or from a video file. The system identifies **Red**, **Yellow**, and **Green** traffic lights using color detection and contour finding techniques in the HSV color space.

## Key Features

- **Real-Time Detection**: Detects traffic light colors using a live camera feed or video.
- **Color Segmentation**: Strict color ranges for red, yellow, and green lights in HSV space.
- **Bounding Boxes**: Draws bounding boxes around detected traffic lights.
- **No Trackbars**: Hardcoded color ranges for automatic detection.

## Requirements

- Python 3.x
- OpenCV
- NumPy

Install required dependencies using:

```
pip install opencv-python numpy
```

## Usage

1. Clone this repository.
2. Replace the `path_to_traffic_video.mp4` with the path to your traffic video.
3. Run the Python script:

```
python traffic_light_detection.py
```

## Applications

- Autonomous vehicles
- Traffic monitoring systems
- Smart city solutions

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

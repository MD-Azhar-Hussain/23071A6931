# STARK ENGINE v4.0 - Usage Guide

## Table of Contents
1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Controls](#controls)
4. [Configuration](#configuration)
5. [Performance Tuning](#performance-tuning)
6. [Troubleshooting](#troubleshooting)
7. [Advanced Usage](#advanced-usage)

## Installation

### Prerequisites
- Python 3.8 or higher
- Webcam
- 4GB RAM minimum
- OpenGL-capable GPU (recommended)

### Method 1: Automated Setup (Recommended)

```bash
cd StarkEngine
chmod +x setup.sh
./setup.sh
```

### Method 2: Manual Setup

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt
```

### Dependencies Explained

```
opencv-python>=4.8.0      # Camera capture and image processing
numpy>=1.24.0             # High-performance numerical computing
mediapipe>=0.10.0         # Hand tracking and gesture recognition
PyQt6>=6.5.0             # Modern GUI framework
```

## Quick Start

### Running the Application

```bash
# Activate virtual environment (if not already active)
source venv/bin/activate

# Run the engine
python stark_engine_v4_optimized.py
```

### First Launch

1. **Allow Camera Access**: Grant permission when prompted
2. **Position Hands**: Hold hands in front of camera
3. **Test Gestures**: Try pinching thumb and index finger
4. **Rotate Object**: Pinch with right hand and drag
5. **Pan View**: Pinch with left hand and drag
6. **Zoom**: Pinch with both hands and move apart/together

## Controls

### Hand Gestures

#### Right Hand (Cyan Reticle ◎)

**Rotate Object**
```
1. Pinch thumb and index finger together
2. Drag hand left/right/up/down
3. Release to let object spin with momentum
```

**Click UI Buttons**
```
1. Move hand over button
2. Pinch to activate
```

#### Left Hand (Magenta Reticle ◎)

**Pan Camera View**
```
1. Pinch thumb and index finger together
2. Drag hand to move workspace
3. Release to stop panning
```

#### Both Hands Together

**Pinch-to-Zoom**
```
1. Pinch both hands simultaneously
2. Move hands apart → Zoom In
3. Move hands together → Zoom Out
4. Release to lock zoom level
```

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `ESC` | Exit application |
| `F` | Toggle FPS display on/off |
| `Q` | Cycle quality settings (low→medium→high→ultra) |

### UI Buttons

Located on the left side of the screen:

1. **CUBE** - Simple 8-vertex box
2. **SPHERE** - UV sphere with smooth surface
3. **CYLINDER** - Circular cylinder
4. **TORUS** - Donut shape
5. **PYRAMID** - Square pyramid
6. **CONE** - Circular cone
7. **HELIX** - Spiral spring
8. **OCTAHEDRON** - 8-sided polyhedron
9. **ICOSAHEDRON** - 20-sided polyhedron
10. **RESET VIEW** - Reset camera position and zoom
11. **TOGGLE FPS** - Show/hide performance metrics

## Configuration

### Using config.ini

Edit `config.ini` to customize the engine:

```ini
[Display]
resolution_width = 1920      # Screen width
resolution_height = 1080     # Screen height
target_fps = 60             # Target frame rate

[Performance]
vision_process_interval = 2  # Process every Nth frame
default_quality = high       # low/medium/high/ultra
```

### Performance Settings

#### Quality Levels

| Level | Vertex Density | Performance | Visual Quality |
|-------|---------------|-------------|----------------|
| Low | 0.5x | Fastest | Basic |
| Medium | 0.75x | Fast | Good |
| High | 1.0x | Balanced | Great |
| Ultra | 1.5x | Slower | Best |

**When to use each:**
- **Low**: Older hardware, battery saving
- **Medium**: Balanced performance
- **High**: Default, recommended
- **Ultra**: High-end hardware, screenshots

#### Frame Skip Settings

```ini
[Performance]
vision_process_interval = 2  # Default
```

- `1` - Process every frame (highest CPU, lowest latency)
- `2` - Process every 2nd frame (recommended)
- `3` - Process every 3rd frame (lowest CPU, higher latency)

## Performance Tuning

### Optimizing for Your Hardware

#### High-End Systems (Gaming PC)

```ini
[Performance]
vision_process_interval = 1
default_quality = ultra

[Display]
target_fps = 120
```

#### Mid-Range Systems (Typical Laptop)

```ini
[Performance]
vision_process_interval = 2
default_quality = high

[Display]
target_fps = 60
```

#### Low-End Systems (Old Hardware)

```ini
[Performance]
vision_process_interval = 3
default_quality = low

[Display]
target_fps = 30

[Vision]
model_complexity = 0  # Use lightweight model
```

### Monitoring Performance

Press `F` to display real-time metrics:

```
FPS: 60.0 | Frame: 14.2ms
Zoom: 1.50x | Verts: 625
```

**Interpreting Metrics:**
- **FPS > 50**: Excellent performance
- **FPS 30-50**: Acceptable, consider lowering quality
- **FPS < 30**: Poor, reduce quality or increase frame skip
- **Frame Time < 16ms**: Hitting 60 FPS target
- **Frame Time > 16ms**: Dropping frames

## Troubleshooting

### Common Issues

#### "No module named 'cv2'"

```bash
pip install opencv-python
```

#### "Camera not found" or "Failed to open camera"

```bash
# Check available cameras
python -c "import cv2; print([i for i in range(10) if cv2.VideoCapture(i).isOpened()])"

# Try different camera index in config.ini
[Vision]
camera_index = 1  # or 2, 3, etc.
```

#### Hand Tracking Not Working

**Lighting Issues:**
- Ensure good lighting (avoid backlighting)
- Position hands in front of neutral background
- Avoid wearing gloves

**Distance:**
- Keep hands 30-80cm from camera
- Entire hand should be visible

**Confidence Thresholds:**
```ini
[Vision]
min_detection_confidence = 0.6  # Lower = more sensitive
min_tracking_confidence = 0.6   # Lower = more sensitive
```

#### Low FPS / Lag

1. **Lower Quality:**
   - Press `Q` to cycle down
   - Or edit `config.ini`: `default_quality = low`

2. **Increase Frame Skip:**
   ```ini
   [Performance]
   vision_process_interval = 3
   ```

3. **Reduce Resolution:**
   ```ini
   [Vision]
   camera_width = 640
   camera_height = 480
   ```

4. **Close Other Apps:**
   - Close browser tabs
   - Close other camera apps
   - Check task manager for CPU usage

#### Application Freezes

- Try lowering `target_fps`
- Ensure GPU drivers are updated
- Check system memory usage

## Advanced Usage

### Running Benchmarks

```bash
python benchmark.py
```

This will test:
- Mesh generation speed
- Transformation performance
- Projection efficiency
- Full pipeline throughput

### Custom Modifications

#### Adding New Mesh Types

Edit `stark_engine_v4_optimized.py`:

```python
elif shape_type == "MY_SHAPE":
    # Define vertices
    verts = np.array([
        [x1, y1, z1],
        [x2, y2, z2],
        # ...
    ], dtype=np.float32)
    
    # Define edges (pairs of vertex indices)
    edges = [(0, 1), (1, 2), ...]
```

#### Adjusting Physics

```python
[Physics]
rotation_speed = 0.005    # Higher = faster rotation
momentum_ratio = 0.1      # Higher = more momentum
friction = 0.98          # Lower = more friction
```

#### Customizing Colors

```python
# In StarkOverlay.draw_3d_object()
pen = QPen(QColor(R, G, B), thickness)

# Example: Red wireframe
pen = QPen(QColor(255, 0, 0), 2)
```

### Integration with Other Projects

The engine can be integrated into larger applications:

```python
from stark_engine_v4_optimized import WorldEngine, MeshFactory

# Create engine
engine = WorldEngine()

# Load mesh
engine.set_mesh("SPHERE", quality="high")

# Get projection for custom rendering
points_2d, depths = engine.get_projected_points()
```

## Performance Tips

### Best Practices

1. **Good Lighting**: Consistent, front-facing light
2. **Neutral Background**: Avoid busy backgrounds
3. **Clean Hands**: Better detection without jewelry
4. **Steady Camera**: Mount webcam for stability
5. **Close Background Apps**: Free up system resources

### Gesture Tips

1. **Smooth Movements**: Avoid jerky motions
2. **Clear Pinches**: Fully touch thumb to finger
3. **Reset Often**: Use "RESET VIEW" to recenter
4. **Practice**: Gestures become natural with practice

### Power Saving

For laptop use:

```ini
[Performance]
vision_process_interval = 3
default_quality = medium

[Display]
target_fps = 30
```

## Keyboard Shortcuts Summary

```
ESC    - Exit application
F      - Toggle FPS display
Q      - Cycle quality (low/medium/high/ultra)

Tips:
- Hold ESC for emergency exit
- F key works while interacting
- Q cycles through all quality levels
```

## Next Steps

1. **Explore all mesh types** - Try each shape
2. **Master gestures** - Practice smooth control
3. **Optimize performance** - Find your best settings
4. **Read architecture docs** - Understand the system
5. **Run benchmarks** - Test your hardware

## Additional Resources

- **README.md** - Feature overview and introduction
- **ARCHITECTURE.md** - Technical deep dive
- **CHANGELOG.md** - Version history and improvements
- **FEATURES.md** - Visual feature showcase
- **benchmark.py** - Performance testing suite

## Support & Feedback

For issues or questions:
1. Check this usage guide
2. Review troubleshooting section
3. Run benchmark to verify system
4. Check configuration settings

---

**Happy gesture controlling! 🎮**

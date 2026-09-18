# Microscopic Particle Defect Detection & Geometric Profiling

An end-to-end Automated Optical Inspection (AOI) pipeline designed to identify, isolate, and quantitatively measure microscopic foreign contaminant particles on camera sensor dies.

## Overview
Foreign material defects on camera sensor dies introduce severe optical aberrations and field failures. This pipeline couples deep learning for robust region proposal with classical computer vision for precise geometric verification:
1. **Object Detection:** Detects sub-millimeter foreign particles across full-die optical images using Ultralytics YOLOv8s.
2. **Morphological Isolation:** Crops predicted regions of interest (ROI) and applies adaptive Gaussian thresholding.
3. **Geometric Quantification:** Fits minimum bounding circles and executes radial ray tracing to compute physical radius, centroid offsets, and internal pixel density.

## Visual Pipeline Results

### 1. Deep Learning Detection
| Raw Defect Region | YOLOv8s Detection Inference |
| :---: | :---: |
| Microscopic Surface | Bounding Box + Class Label (92% Precision) |

*(Insert your YOLO detection screenshot in `assets/sample_predictions.png`)*

### 2. Multi-Stage Morphological Analysis
The 4-stage visual diagnostic output:
1. **Extracted Object:** Cropped bounding region from YOLO proposal.
2. **Binary Mask:** Inverted Gaussian adaptive threshold isolating defect core.
3. **Boundary Verification:** Fitted enclosing circle with horizontal radial vector.
4. **Centroid Anchor:** Sub-pixel center `(x, y)` coordinate extraction.

![Diagnostic Quad Panel](assets/diagnostic_quad_output.png)

## Metrics Extracted
* **Centroid Coordinates:** Precise $(X, Y)$ focal offset on the die matrix.
* **Bounding Radius:** Minimum circular bounding envelope radius in pixels.
* **Radial Pixel Density:** Ray-intersection verification using `cv2.pointPolygonTest` to differentiate solid particles from diffuse sensor noise.

## Setup & Quickstart
```bash
git clone [https://github.com/your-username/aoi-particle-geometry-profiler.git](https://github.com/your-username/aoi-particle-geometry-profiler.git)
cd aoi-particle-geometry-profiler
pip install -r requirements.txt
python src/particle_profiler.py

# Undergraduate Capstone Research & Industrial Dissertation Dossier

**Candidate:** Vatsla Adhikari | **Application No:** 10081516 | **uni-assist ID:** 3570122  
**Degree Awarded:** Bachelor of Engineering in Computer Science & Engineering, Chandigarh University  
**Academic Module:** Senior Capstone Research & Industrial Dissertation (Semester 7: 15 Credits, Grade A+)  
**Academic Supervision:** Prof. Chau-Yun Hsu (Tatung University, cyhsu@gm.ttu.edu.tw)  
**Industrial Supervision:** Allen Wu (REC Technology Corporation, allenwu@rectech-global.com)  
**Host Program:** Taiwan Experience Education Program (TEEP)  

---

## Project Overview

**Title:** Automated Active Alignment, Optical Sensor Quality Assurance, and Defect Detection using Computer Vision and Deep Learning (YOLOv8/Roboflow)

This research project delivers an end-to-end Automated Optical Inspection (AOI) and telemetry pipeline engineered to solve two critical yield bottlenecks in high-precision automotive optoelectronic camera manufacturing:
1. **Module 1 — Focal Plane Tilt & Active Alignment:** Algorithmic calculation of lens tilt (Delta-Z) using multi-zone Modulation Transfer Function (MTF) spatial peak interpolation.
2. **Module 2 — Microscopic Particle Defect Detection & Geometric Profiling:** Deep learning object proposal coupled with classical sub-pixel morphological verification.

---

## Milestone Defense Presentations (Oral Viva Archive)

The following defense presentations document the phased research milestones evaluated by the academic and industrial assessment committee:
* `Milestone-01-System-Architecture.pptx` — Telemetry pipeline specifications and optoelectronic constraints.
* `Milestone-02-MTF-Spatial-Modeling.pptx` — 5-zone spatial sampling and peak focal extraction curves.
* `Milestone-03-DeltaZ-Optimization.pptx` — Mathematical derivation of Delta-Z and tolerance boundary gating.
* `Milestone-04-Deep-Learning-YOLO.pptx` — YOLOv8 architecture, cleanroom augmentation, and precision/recall evaluation.
* `Milestone-05-Morphological-Solvers.pptx` — Sub-pixel contour extraction and pointPolygonTest geometric verification.
* `Milestone-06-Final-Dissertation-Defense.pptx` — Comprehensive system integration, SQL telemetry histograms, and final viva voce examination.

---

## Module 1: MTF Spatial Analysis & Active Alignment (Delta-Z)

During camera barrel bonding, non-uniform curing shrinkage of UV epoxy tilts the optical axis, leading to peripheral focal blur.

### Mathematical Formulation

* **Center Peak Focus:**
  ```text
  Z1 = argmax_Z (MTF_Center(Z))


* **Peripheral Composite Focus (Average of 4 Corners):**
```text
Z2 = 1/4 * sum_{i in {UL, UR, LL, LR}} (argmax_Z (MTF_i(Z)))

```


* **Focal Plane Offset (Tilt Error):**
```text
Delta-Z = |Z1 - Z2|

```


* **Tolerance Gating Rule:**
* **Pass:** `Delta-Z <= 0.006 mm` (6 micrometers)
* **Fail / Realign:** `Delta-Z > 0.006 mm`



### Database Telemetry Pipeline

Python scripts (`pyodbc`, `pandas`) interface directly with Microsoft SQL Server production tables (`REC_DB`) across operational stations (`RG_AA_IOT`, `RG_AIQT_IOT`, `RG_BIQT_IOT`) to aggregate multi-lot travel cards and generate real-time batch distribution histograms.

---

## Module 2: Microscopic Particle Defect Detection & Geometric Profiling

An automated computer vision pipeline designed to identify, isolate, and quantitatively measure microscopic foreign contaminant particles on active camera sensor dies.

### System Workflow

1. **Object Detection:** Localizes sub-millimeter foreign particles across full-die optical images using Ultralytics YOLOv8s.
2. **Morphological Isolation:** Crops predicted regions of interest (ROI) and applies adaptive Gaussian thresholding.
3. **Geometric Quantification:** Fits minimum bounding circles and executes radial ray tracing to compute physical radius, centroid offsets, and internal pixel density.

### Visual Diagnostic Pipeline

#### 1. Deep Learning Detection

| Raw Defect Region | YOLOv8s Detection Inference |
| --- | --- |
| Microscopic Surface | Bounding Box + Class Label (92% Precision) |

*(Reference: `assets/sample_predictions.png`)*

#### 2. Multi-Stage Morphological Analysis

The 4-stage visual diagnostic output:

1. **Extracted Object:** Cropped bounding region from YOLO proposal.
2. **Binary Mask:** Inverted Gaussian adaptive threshold isolating defect core.
3. **Boundary Verification:** Fitted enclosing circle with horizontal radial vector.
4. **Centroid Anchor:** Sub-pixel center `(X, Y)` coordinate extraction.

*(Reference: `assets/diagnostic_quad_output.png`)*

### Metrics Extracted

* **Centroid Coordinates:** Precise `(X, Y)` focal offset on the die matrix.
* **Bounding Radius:** Minimum circular bounding envelope radius in pixels computed via:
```text
R = max_{p in contour} ||p - (X_c, Y_c)||

```


Implemented using `cv2.minEnclosingCircle`.
* **Radial Pixel Density:** Ray-intersection verification using `cv2.pointPolygonTest` to differentiate solid particles from diffuse sensor noise.

---

## Empirical Results

* **Defect Classification:** 92.0% Precision, 77.0% Recall, and 68.7% mAP@0.5 on microscopic test batches.
* **Inspection Throughput:** End-to-end inference and geometric verification executed in `< 20 ms` per frame.
* **Particle Sizing Accuracy:** Sub-pixel contour resolution detecting contaminants between `1.5` and `25.0 micrometers`.

---

## Setup & Execution

```bash
git clone [https://github.com/vatslaadhikari123/Undergraduate-Capstone-Research-Dossier.git](https://github.com/vatslaadhikari123/Undergraduate-Capstone-Research-Dossier.git)
cd Undergraduate-Capstone-Research-Dossier
pip install -r requirements.txt
python src/particle_profiler.py

```

---

## Proprietary Notice

> *Note: Production database schemas, proprietary hardware interface drivers, and raw factory travel-card datasets are property of REC Technology Corporation and subject to non-disclosure agreements (NDA). Algorithmic formulations, milestone examination slides, and standalone image processing pipelines are published here for academic evaluation and dissertation equivalence verification.*

```

```

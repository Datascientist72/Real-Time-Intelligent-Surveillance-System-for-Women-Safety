# Real-Time Intelligent Surveillance System for Women Safety

## Overview

The **Real-Time Intelligent Surveillance System for Women Safety** is an AI-powered surveillance framework designed to transform traditional CCTV cameras into intelligent safety monitoring systems.

Unlike conventional CCTV systems that only record incidents for later investigation, this system analyzes live video streams in real time, understands human activities, detects potentially dangerous situations, evaluates risk levels, and generates alerts for faster response.

The system combines **Computer Vision, Deep Learning, Human Pose Estimation, Multi-Object Tracking, Behavioral Analysis, and Large Language Models (LLMs)** to provide proactive safety monitoring.


# Problem Statement

Traditional CCTV surveillance systems have several limitations:

- They mainly act as passive recording devices.
- Continuous manual monitoring of multiple cameras is difficult.
- Emergency situations may not be detected immediately.
- Response time after an incident can be delayed.

A smarter surveillance system is required that can automatically understand activities occurring in camera feeds and notify responsible authorities during critical situations.

# Project Objective

The main objective of this project is:

> To develop an AI-based real-time surveillance system capable of detecting safety-threatening events involving women and generating alerts to support faster emergency response.

The system aims to:

- Convert CCTV cameras into intelligent monitoring systems.
- Detect and track individuals in real time.
- Analyze human interactions and movements.
- Identify suspicious and violent activities.
- Generate risk assessments.
- Provide meaningful incident reports.


# System Architecture

The complete pipeline follows:

                CCTV Camera
                     |
                     ↓
                    YOLO
          (Human/Object Detection)
                     |
                     ↓
                 ByteTrack
          (Multi-Person Tracking)
                     |
                     ↓
              Pose Estimation
       (Human Body Keypoint Extraction)
                     |
                     ↓
            Action Recognition Model
          (Temporal Activity Analysis)
                     |
        --------------------------------
        |                              |
        ↓                              ↓
 Following Detection            Violence Detection
(Suspicious Movement)          (Fight Analysis)

        --------------------------------
                     |
                     ↓
             Risk Assessment Model
                     |
                     ↓
              LLM Report Generation
                     |
                     ↓
                 Alert System

# Core Components

## 1. CCTV Video Input

The system receives continuous video streams from surveillance cameras.

Responsibilities:

- Capture real-time frames.
- Provide input for AI processing.

## 2. YOLO Detection

YOLO (You Only Look Once) is used for real-time object and person detection.

Functions:

- Detect individuals in video frames.
- Extract bounding boxes.
- Provide confidence scores.

Output:

Detected objects
Person locations
Detection confidence

## 3. ByteTrack Tracking

ByteTrack performs multi-object tracking.

Purpose:

- Assign unique IDs to individuals.
- Maintain identity across frames.
- Analyze movement patterns.

Example:

Person A → ID 01
Person B → ID 02


Tracking enables the system to understand interactions between individuals.

## 4. Pose Estimation

Pose estimation extracts human body keypoints.

Detected points include:

- Head
- Shoulders
- Arms
- Hands
- Legs

Pose information helps analyze:

- Body movements
- Physical interactions
- Aggressive postures

## 5. Action Recognition Model

A deep learning-based temporal model is used to understand human activities.

Current approach:

Pose Sequence
       |
       ↓
      LSTM
       |
       ↓
Action Prediction

Purpose:

- Recognize activity patterns.
- Identify abnormal movements.

### Current Limitation

The action recognition model requires further improvement due to limited availability of high-quality annotated safety datasets. Additional training data and validation are required for robust real-world deployment.

## 6. Following Detection Model

The following detection module identifies suspicious movement relationships between individuals.

It analyzes:

- Person-to-person distance
- Movement direction
- Duration of interaction

Example:

One individual repeatedly following another individual


## 7. Violence Detection Model

The violence detection module identifies aggressive or harmful activities.

Possible detections:

- Physical fights
- Assault-like movements
- Sudden aggressive actions

Output:

Violence probability score

## 8. Risk Assessment Model

The risk model combines information from different AI modules.

Inputs:

- Action recognition output
- Following behavior score
- Violence detection score
- Movement patterns

Output:
Risk Level:

Low Risk
Medium Risk
High Risk
## 9. LLM Report Generation

A Large Language Model is used to convert AI predictions into understandable incident reports.

Example:

High-risk interaction detected.

Person ID 04 followed Person ID 07
for an extended duration and aggressive
movement patterns were observed.

Immediate attention recommended.

Purpose:

- Provide human-readable explanations.
- Assist security personnel in decision making.
## 10. Alert System

The final stage communicates detected threats.

Possible integrations:

- Security dashboard
- Emergency notification system
- Email/SMS alerts
- Authority communication systems
# Technology Stack

## Programming Language

- Python

## Computer Vision

- OpenCV
- YOLO
- ByteTrack
- Pose Estimation

## Deep Learning

- PyTorch / TensorFlow
- LSTM-based temporal models

## Artificial Intelligence

- Action Recognition
- Behavior Analysis
- Risk Prediction
- Large Language Model Reporting
# Project Structure

community_safety_ai/

│
├── app.py                  # Main application
│
├── core/
│   └── pose.py             # Pose estimation module
│
├── pipelines/
│   └── surveillance_pipeline.py
│                            # Complete AI pipeline
│
├── behavior/
│   ├── following.py
│   ├── violence.py
│   └── risk.py
│
├── training/
│   └── model.py            # Model training code
│
├── data/
│   └── datasets and logs
│
└── README.md
# Installation

## Create Virtual Environment
bash
python -m venv cv_env
Activate environment:

Windows:
bash
cv_env\Scripts\activate
## Install Dependencies
bash
pip install -r requirements.txt
# Running the System

## Webcam Mode
bash
python app.py
## Video Testing Mode
bash
python tests/test_videos.py

# Future Improvements

Future development areas include:

- Improved action recognition with larger datasets.
- Real-world CCTV dataset training.
- Person re-identification across multiple cameras.
- Automated emergency communication.
- Mobile application integration.
- Cloud-based monitoring dashboard.
- Privacy-preserving AI surveillance.
# Current Development Status

The project is currently under active development.

Implemented:

- Video processing pipeline
- Person detection
- Object tracking
- Pose extraction
- Behavioral analysis framework
- Risk scoring framework

Ongoing:

- Improving LSTM-based action recognition performance.
- Expanding training datasets.
- Real-world validation.

# Disclaimer

This system is designed as an AI-assisted safety monitoring tool. Final decisions and actions should always involve human supervision and responsible authorities.

# Author

**Barket Hussain**

MSc Artificial Intelligence and Machine Learning

Project:
**Real-Time Intelligent Surveillance System for Women Safety**

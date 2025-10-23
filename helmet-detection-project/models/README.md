# README for Models in Helmet Detection Project

This directory contains information about the models used in the Helmet Detection Project. The project utilizes machine learning models to detect individuals and verify whether they are wearing helmets (Personal Protective Equipment - PPE).

## Models Overview

1. **Person Detection Model**: This model is responsible for identifying human figures in the video stream. It processes frames from the camera feed and detects the presence of people.

2. **Helmet Classification Model**: Once a person is detected, this model classifies whether the individual is wearing a helmet or not. It analyzes the detected person's head region to make this determination.

## Model Requirements

- The models are trained using datasets that include various scenarios and lighting conditions to ensure robustness.
- Ensure that the models are downloaded and placed in the appropriate directory as specified in the project documentation.

## Usage

The models are integrated into the application through the `src/detectors` package, where the `PersonDetector` and `HelmetClassifier` classes are implemented. These classes are utilized by the `RealtimeMonitor` in the `src/pipelines` package to provide real-time monitoring and alerts.

For detailed instructions on how to run the application and utilize these models, please refer to the main `README.md` file in the project root directory.
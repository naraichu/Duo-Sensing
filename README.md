# Duo-Sensing: 3D Printing Free-form Flexible Devices to Simultaneously Support Touch Input and Stable Deformation Sensing
![Intro_pic](https://github.com/naraichu/Duo-Tactile/assets/67613808/ac059578-8b24-42b1-9b45-dfe2e44dc7b3)

## Note!!
While the current phase of this project is complete for the dissertation, there are still opportunities for further development and extension!

## Introduction
This repository serves as the documentation for the final year dissertation project in Human-Computer Interaction at the University of Bath. Duo-Sensing introduces innovative methods for combining capacitive and resistive sensing into a flexible filament that can be fabricated using an FDM 3D printer equipped with a duo-extrusion print head.

Swept-frequency capacitive sensing (SFCS) represents an advanced capacitive sensing technique supporting dynamic touch interactions across various body configurations, including fingers, palm, and fist. The Wheatstone bridge, on the other hand, is a reliable resistive sensing circuit facilitating tactile interactions such as squeezing, bending, and twisting.

## Overview
This repository contains both the code and documentation necessary for implementing capacitive and resistive sensing on conductive TPU (Thermoplastic Polyurethane) filament. Swept-frequency capacitive sensing entails detecting changes in capacitance across a range of frequencies, enabling precise and dynamic touch or proximity sensing, while resistive sensing enables tactile interactions such as squeezing, bending, and twisting.

## Duo-Sensing circuit
![Circuit_Schematics](https://github.com/naraichu/Duo-Tactile/assets/67613808/03fbf6cd-0c9d-40ed-b8dd-75a2a1b8afe3)

The potentiometer, as seen in the diagram within the Wheatstone Bridge, is the digital integrated circuit (IC) potentiometer [X9C103](https://www.renesas.com/us/en/document/dst/x9c102-x9c103-x9c104-x9c503-datasheet) which has a maximum resistance of 10kΩ and 100 incremental steps, thus providing a resolution of 0.1kΩ. Other X9C ICs can also be used for different ranges of resistance. External resistors (Ext res) can be connected in series next to the X9C103 to increase the resistance range that matches the TPU printwork

## Limitations
Duo-Sensing serial communication is not well implemented, which can lead to occasional interruptions in the bit streams. This has resulted in poor data quality for training the machine learning model.

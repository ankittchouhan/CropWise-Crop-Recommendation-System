# CropWise--Crop-Recommendation-System
 
# CropWise: An Intelligent Crop Recommendation System

**CropWise** is a machine learning-based web application designed to recommend the most suitable crop based on various soil and environmental factors. The system leverages agricultural data to help farmers make data-driven decisions about crop selection, improving yield and sustainability.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Code](#code)
- [Acknowledgments](#acknowledgments)

## Overview
Agricultural productivity is highly dependent on the proper selection of crops based on soil characteristics and climate conditions. **CropWise** aims to simplify this process by using machine learning to predict the best crop for a particular region based on soil nitrogen, phosphorus, potassium content, temperature, humidity, pH level, and rainfall data.

The application is built using Flask for the web interface and a machine learning model trained on crop data to make accurate crop recommendations.

## Features
- User-friendly web interface for farmers and agriculture enthusiasts.
- Input soil and environmental data such as nitrogen, phosphorus, potassium levels, temperature, humidity, pH, and rainfall.
- Accurate crop prediction based on a trained machine learning model.
- Responsive design for easy use on mobile devices.

## Technologies Used
- **Flask**: Backend web framework for Python.
- **Scikit-learn**: Machine learning library for model building.
- **Pandas**: Data manipulation and analysis library.
- **NumPy**: Numerical computations.
- **HTML/CSS**: Frontend web development.
- **Bootstrap**: For responsive web design.

## Setup Instructions

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- Git
- Virtualenv (optional)

### Step 1: Clone the Repository
```bash
git clone https://github.com/ankittchouhan/CropWise-Crop-Recommendation.git
cd CropWise-Crop-Recommendation

### Step 2: Set up the Virtual Environment
python -m venv env
source env/bin/activate 


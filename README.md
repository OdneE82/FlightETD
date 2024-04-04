# Flight Departure Time Prediction
## Overview

This project aims to explore the application of machine learning (ML) and deep learning (DL) models in predicting flight departure times, inspired by the flight tracking and prediction capabilites of platforms like Flightradar24. By leveraging a dataset of Widerøe's flights from Bergen Flesland Airport (BGO) spanning from January 1st 2021, to 2024, this project investigates the accuracy and efficiency of deep learning models compared to traditional machine learning approaches in predicting flight departure times.

## Background
Flight departure time preidction is a complex problem that involves numerious variables, including weather conditions, air traffic, and technical issues. Accurate predictions can significantly enhance operational efficiency and passenger satisfaction. Platforms like Flightradar24 have made remarkable advancements in real-time flight tracking and predictions, likely utilizing advanced ML and DL techniques to process vast amounts of data.
As someone fascinated by the interplay between technology and aviation, I was motivated to uncover the methodologies behind these predictions. This project serves as an exploratory journey into the capabilites of machine learning and deep learning, aiming to understand their application in a domain rich with real-time data and requiring high accuracy.

## Dataset
The dataset includes all recorded flights by Widerøe from Bergen Flesland Airport (BGO) from January 1st, 2024, to 2024. It encompasses various features, such as flight numbers, scheduled and actual departure times, destiantions, aircraft types, and delay codes. This dataset provides a comprehensive foundation for modeling and predictions.

## Methodology
The project employs a two-phase approach:
1. Machine Learning Phase: Utilizes RandomForestRegressor to predict departure times, focusing on feature engineering, data preprocessing, and model optimization to minimize prediction error.
2. Deep Learning Phase: Leverages the fastai library to explore deep learning models' effectiveness in capturing complex patterns without extensive feature engineering. This phase examines wheter DL models can outperform ML models in accuracy and efficiency.

## Findings and Conclusion
TBD

## Future Work
This project opens several avenues for further exploration, including integrating real-time weather data, considering airport congestion levels, and deploying models as a service for real-time predictions.


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
1. Machine Learning Phase: Using RandomForestRegressor to predict departure times, focusing on feature engineering, data preprocessing, and model optimization to minimize prediction error.
2. Deep Learning Phase: Using the fastai library to explore deep learning models' effectiveness in capturing complex patterns without extensive feature engineering. This phase examines wheter DL models can outperform ML models in accuracy and efficiency.

## Findings and Conclusion
This project's investigation into the application of machine learning and deep learning models for predicting flight departure times has yielded insightful outcomes. The deep learning model demonstrated a remarkable capacity for processing the dataset with minimal preprocessing, achieving competitive performance metrics with considerably less effort compared to the traditional machine learning approach. Specifically, the deep learning model outperformed the machine learning models in terms of the Mean Squared Error (MSE) and Root Mean Squared Error (RMSE), achieving a lower MSE of 1831.9388 and a RMSE of 42.801155, thus indicating a higher accuracy in predicting flight departure times. Although the Mean Absolute Error (MAE) was slightly higher in the deep learning model, this is offset by the significant reductions in preprocessing time and complexity. These findings highlight the efficiency and effectiveness of deep learning models in handling complex prediction tasks, such as flight departure times, with minimal data preprocessing. The project underscores the potential of deep learning in enhancing operational efficiency and accuracy in aviation logistics, paving the way for more sophisticated predictive models in the future.

## Future Work
This project opens several avenues for further exploration, including integrating real-time weather data, considering airport congestion levels, and deploying models as a service for real-time predictions. I will also work on a locally ran deployment of the models using Avinor data to give a real-time departure time prediction.

## Links
Kaggle notebook link: https://www.kaggle.com/chondeagle/flightestimations
Avinor flight data: https://avinor.no/en/corporate/services/flydata/flight-data

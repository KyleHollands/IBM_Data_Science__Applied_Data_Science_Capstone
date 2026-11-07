# SpaceX Falcon 9 First Stage Landing Prediction

## Project Overview
The goal of this project is to analyze SpaceX Falcon 9 launch data to predict whether the first stage of the rocket will land successfully. SpaceX's ability to reuse the first stage significantly reduces launch costs, making this prediction crucial for competitive bidding in the space industry. Through exploratory data analysis, machine learning, and interactive visualizations, this project aims to identify key factors influencing landing success and develop predictive models.

## Data Understanding
The project utilizes multiple datasets, including launch records from SpaceX, payload information, and launch site details. Data sources include:

- **SpaceX API**: Historical launch data including rocket versions, payloads, launch sites, and core outcomes.
- **Wikipedia**: Detailed records of Falcon 9 and Falcon Heavy launches, including dates, payloads, and landing outcomes.
- **Interactive Visualizations**: Folium maps for launch site analysis and Plotly Dash for interactive dashboards.

The datasets were cleaned and preprocessed to handle missing values, outliers, and inconsistencies. Categorical variables were one-hot encoded, and numerical features were standardized for modeling.

## Modeling and Evaluation
Several machine learning models were evaluated, including Logistic Regression, Support Vector Machines (SVM), Decision Trees, and K-Nearest Neighbors (KNN). Hyperparameter tuning was performed using GridSearchCV to optimize model performance. Key evaluation metrics included accuracy, precision, recall, and F1 score.

### Key Findings:
- **Feature Importance**: Payload mass, booster version, and launch site were identified as significant predictors of landing success.
- **Best Performing Model**: SVM achieved the highest accuracy (~87%) among the models tested.
- **Confusion Matrix Analysis**: The model effectively distinguished between successful and unsuccessful landings, with minimal false positives.

## Business Understanding
The primary stakeholders for this project are aerospace companies and launch service providers. The predictions can aid in cost estimation and competitive bidding against SpaceX. Understanding the factors influencing landing success can also inform design improvements and operational strategies for reusable rockets.

## Interactive Visualizations
Interactive dashboards were developed using Plotly Dash to visualize launch outcomes, payload mass distributions, and landing success rates across different launch sites and orbits. These tools provide stakeholders with actionable insights and facilitate data-driven decision-making.

### Key Insights:
- **Launch Sites**: Certain launch sites exhibited higher success rates, potentially due to geographic and environmental factors.
- **Payload Mass**: Heavier payloads were associated with lower landing success rates.
- **Orbit Types**: Different orbits showed varying success rates, with Low Earth Orbit (LEO) and Polar orbits being more favorable.

## Conclusion
The analysis revealed that payload mass, booster version, and launch site are critical factors in predicting Falcon 9 first stage landing success. Companies bidding against SpaceX can use these insights to estimate launch costs more accurately and improve their competitive positioning. Further improvements can be achieved through additional feature engineering and advanced modeling techniques.

## Next Steps
Future work will focus on:
- Incorporating additional data sources (e.g., weather conditions, rocket telemetry).
- Developing ensemble models to improve prediction accuracy.
- Creating real-time prediction systems for ongoing launches.
#  Employee Productivity Prediction Using Machine Learning

A complete **Machine Learning + Flask Web Application** that predicts the **productivity of workers** based on operational and behavioral factors.  
This project demonstrates the **end-to-end flow** from **data collection** to **model deployment** using an interactive web interface.

## Project Flow

 **User Input** →  
User interacts with the **Flask-based web UI** and enters required parameters (like SMV, overtime, idle time, etc.)

 **Model Processing** →  
The trained **Machine Learning model** (Linear Regression, Random Forest, and XGBoost) analyzes the inputs and predicts the productivity score.

**Result Display** →  
The **predicted productivity** (e.g., *Low / Medium / High*) is displayed instantly on the UI.

##  Project Components

| Stage | Description |
|--------|-------------|
| **Data Collection** | Collected real-world dataset of garment worker productivity from public repositories and production logs. |
| **Data Visualization & Analysis** | Explored data using Matplotlib & Seaborn — performed correlation, distribution, and trend analysis. |
| **Data Preprocessing** | Cleaned null values, handled date and department columns, encoded categorical variables, and scaled features. |
| **Model Building** | Implemented multiple ML algorithms (Linear Regression, Random Forest, XGBoost) for prediction. |
| **Model Evaluation** | Compared model performance using MAE, MSE, and R² metrics. |
| **Model Deployment** | Saved the best model using Pickle and deployed it using Flask web framework. |
| **UI Development** | Created HTML-based form for user interaction. |
| **Integration** | Connected UI with the backend model for real-time predictions. |

##  Tech Stack

| Category | Tools / Libraries |
|-----------|------------------|
| **Programming Language** | Python 3.x |
| **Data Handling** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Machine Learning** | Scikit-learn, XGBoost |
| **Model Deployment** | Flask, Pickle |
| **Version Control** | Git, GitHub |


##  Dataset Overview

The dataset includes the following important features:

| Feature | Description |
|----------|-------------|
| `date` | Production date |
| `quarter` | Quarter of the year |
| `department` | Department (Sewing / Finishing) |
| `day` | Day of the week |
| `team` | Team ID |
| `targeted_productivity` | Target productivity set by management |
| `smv` | Standard Minute Value (workload measure) |
| `wip` | Work in progress |
| `over_time` | Overtime minutes |
| `incentive` | Additional bonus earned |
| `idle_time` | Unproductive time (minutes) |
| `no_of_workers` | Number of workers in the team |
| `actual_productivity` | Actual productivity achieved (Target variable) |

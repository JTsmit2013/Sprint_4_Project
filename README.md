# Sprint_4_Project
https://sprint-4-project-4f4i.onrender.com

# Car Price Visualization Tool

This project is a Streamlit-based application for visualizing car prices by manufacturer over different model years. Users can interactively select manufacturers and adjust the price and model year ranges to update the scatter plot in real-time.

## Project Description

This tool provides an interactive visualization of car price data, allowing users to explore and compare car prices from different manufacturers. It includes several features such as histograms for visualizing the distribution of vehicle types and conditions, and a scatter plot for comparing prices over model years.

## Features

- **Raw Data Display**: View the raw vehicle data in a table format.
- **Vehicle Types by Manufacturer**: Histogram showing the distribution of vehicle types for each manufacturer.
- **Condition vs Model Year**: Histogram showing the condition of vehicles across different model years.
- **Price Distribution Comparison**: Compare price distributions between two selected manufacturers.
- **Interactive Scatter Plot**: Scatter plot displaying car prices by model year, with filters for manufacturer, price range, and model year range.

## Technologies Used

- **Streamlit**: A fast way to build and share data apps.
- **Plotly**: A graphing library for making interactive, publication-quality graphs.
- **Pandas**: A data manipulation and analysis library for Python.

## How to Run the Project Locally

To run this project on your local machine, follow these steps:

### Prerequisites

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/car-price-visualization.git
   cd car-price-visualization

2.Install the required libraries:
   
   ```bash
   pip install streamlit plotly pandas


3.Ensure you have the 'vehicles_us.csv' file and the 'app.py' file in the same directory 

4.Run the Streamlit application

   ```bash
      streamlit run app.py

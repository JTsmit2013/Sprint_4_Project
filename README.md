# 🚗 Car Price Visualization Tool  
[Live App](https://sprint-4-project-4f4i.onrender.com)

A Streamlit-based web application that lets users explore and compare car prices across different manufacturers and model years.

---

## 📌 Project Description  
This interactive tool visualizes used car pricing data, enabling users to filter by manufacturer, price range, and model year. It helps users understand trends in vehicle condition, pricing, and model distribution through intuitive visualizations.

---

## 🔍 Features  

- **Raw Data Display**: View the complete vehicle dataset in tabular form.  
- **Vehicle Types by Manufacturer**: Histogram of different vehicle types offered by each manufacturer.  
- **Condition vs. Model Year**: Histogram showing how vehicle conditions vary by model year.  
- **Price Distribution Comparison**: Compare price distributions of two selected manufacturers.  
- **Interactive Scatter Plot**: Explore car prices across model years with dynamic filters.

---

## 🛠️ Technologies Used  

- **Streamlit** – For building the interactive web application  
- **Plotly** – For creating interactive charts and plots  
- **Pandas** – For data processing and analysis

---

## 💻 How to Run Locally  

### ✅ Prerequisites  
- Python 3.x installed – [Download Python](https://www.python.org/)

### 🧰 Installation Steps  

## Clone the repository
git clone https://github.com/your-username/car-price-visualization.git
cd car-price-visualization

## Install required libraries
pip install streamlit plotly pandas

## 🚀 Run the App  
 Make sure `vehicles_us.csv` and `app.py` are in the same directory, then launch the app:
streamlit run app.py

## 📁 Data  
 This project uses a dataset of used vehicles in the U.S. (`vehicles_us.csv`), which should be placed in the project directory.  
 Note: This dataset is not included in the repository.

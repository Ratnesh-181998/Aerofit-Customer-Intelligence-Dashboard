# 🏃‍♂️ Aerofit Customer Intelligence Analytics

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

> **Interactive customer analytics dashboard for fitness equipment retail. Built with Python, Streamlit, and Plotly for comprehensive business intelligence.**

![Dashboard Preview](https://img.shields.io/badge/Status-Production_Ready-success?style=for-the-badge)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#️-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Key Insights](#-key-insights)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 Overview

**Aerofit Customer Intelligence Analytics** is a comprehensive data analytics platform designed to identify target audiences and provide product recommendations for Aerofit's treadmill product line. The application leverages advanced statistical analysis, interactive visualizations, and machine learning techniques to deliver actionable business insights.

### Business Problem

Identify the characteristics of the target audience for each type of treadmill offered by Aerofit to provide better recommendations to new customers and optimize marketing strategies.

---

## 🎬 Demo
- **Streamlit Profile** - https://share.streamlit.io/user/ratnesh-181998
- **Project Demo** - https://aerofit-customer-intelligence-dashboard-cmwtx6jamu8lqfvfahzcqt.streamlit.app/

---
### Product Portfolio

- **KP281** - Entry-level treadmill ($1,500)
- **KP481** - Mid-level runners ($1,750)
- **KP781** - Advanced features ($2,500)

---

## ✨ Features

### 📊 Data Overview
- **Interactive Metrics Dashboard** - Real-time KPIs and statistics
- **Product Distribution Analysis** - Sales volume and revenue breakdown
- **Data Filtering** - Multi-dimensional filtering by product, gender, and age
- **Summary Statistics** - Comprehensive descriptive analytics

### 🔍 Interactive EDA
- **Univariate Analysis** - Distribution plots for all variables
- **Bivariate Analysis** - Relationship exploration between features
- **Multivariate Analysis** - 3D visualizations and correlation heatmaps
- **Outlier Detection** - IQR-based outlier identification

### 🎲 Probability Analysis
- **Marginal Probabilities** - Product and demographic distributions
- **Conditional Probabilities** - Cross-tabulation analysis
- **Interactive Heatmaps** - Visual probability distributions
- **Statistical Insights** - Data-driven probability findings

### 💡 Insights & Recommendations
- **Customer Profiling** - Detailed profiles for each product segment
- **Business Recommendations** - Actionable marketing strategies
- **KPI Dashboard** - Key performance indicators
- **Strategic Planning** - Data-driven business decisions

### 📚 Complete Analysis
- **Problem Statement** - Comprehensive business context
- **Data Dictionary** - Complete feature descriptions
- **Methodology** - Step-by-step analysis approach
- **Key Findings** - Statistical insights and patterns
- **Customer Profiles** - Detailed segmentation analysis
- **Recommendations** - Strategic business actions

### 📝 Application Logs
- **Real-time Logging** - Track all user interactions
- **Log Filtering** - Filter by severity level (INFO, WARNING, ERROR)
- **Search Functionality** - Quick log search
- **Download Logs** - Export complete log files
- **Statistics Dashboard** - Log analytics and metrics

---

## 🛠️ Tech Stack

### Core Technologies
- **Python 3.8+** - Primary programming language
- **Streamlit** - Web application framework
- **Plotly** - Interactive visualizations
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Seaborn** - Statistical data visualization
- **Matplotlib** - Plotting library

### Key Libraries
```python
streamlit==1.28.0
pandas==2.0.3
numpy==1.24.3
plotly==5.17.0
seaborn==0.12.2
matplotlib==3.7.2
```

---

## 📥 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/Ratnesh-181998/Aerofit-Customer-Intelligence-Dashboard.git
cd Aerofit-Customer-Intelligence-Dashboard
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

---

## 🚀 Usage

### Quick Start
1. Launch the application using `streamlit run app.py`
2. Navigate through the tabs to explore different analyses
3. Use filters to customize your data view
4. Hover over charts for detailed information
5. Download logs for audit trails

### Data Filters
- **Product Filter** - Select specific treadmill models
- **Gender Filter** - Filter by customer gender
- **Age Range** - Adjust age slider for targeted analysis

### Interactive Features
- **Hover Tooltips** - Detailed information on data points
- **Zoom & Pan** - Interactive chart manipulation
- **Download Charts** - Export visualizations as images
- **Log Search** - Find specific events in application logs

---

## 📁 Project Structure

```
Aerofit-Customer-Intelligence-Dashboard/
│
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── aerofit_treadmill.csv          # Dataset
├── app.log                        # Application logs
│
├── README.md                      # Project documentation
├── LICENSE                        # MIT License
├── .gitignore                     # Git ignore rules
│
└── assets/                        # (Optional) Screenshots and images
    └── screenshots/
```

---

## 🔍 Key Insights

### Customer Segmentation

#### KP281 (Entry-Level)
- **Market Share:** 44.4% (Highest selling)
- **Target:** Budget-conscious beginners
- **Demographics:** Equal gender appeal, all age groups
- **Income:** < $60,000
- **Usage:** 3-4 times/week, 70-90 miles/week

#### KP481 (Mid-Level)
- **Market Share:** 33.3%
- **Target:** Intermediate users
- **Demographics:** Strong female preference (38.15% vs 29.80% male)
- **Income:** $50,000 - $70,000
- **Usage:** 3-4 times/week, 70-130 miles/week

#### KP781 (Advanced)
- **Market Share:** 22.2%
- **Target:** Athletes and high-income individuals
- **Demographics:** Predominantly male (31.73% vs 9.21% female)
- **Income:** > $80,000
- **Usage:** 4-5+ times/week, 120-200+ miles/week
- **Fitness:** 93.5% of "Excellent Shape" customers

### Statistical Findings
- **Fitness & Miles Correlation:** 0.79 (Strong positive)
- **Product Price & Income Correlation:** 0.70 (Strong positive)
- **Usage & Miles Correlation:** 0.76 (Strong positive)

---

## 📸 Screenshots

### Dashboard Overview
![Data Overview](https://via.placeholder.com/800x400?text=Data+Overview+Dashboard)

### Interactive EDA
![EDA Analysis](https://via.placeholder.com/800x400?text=Interactive+EDA)

### Probability Analysis
![Probability](https://via.placeholder.com/800x400?text=Probability+Analysis)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Contact

**Ratnesh Singh**

- GitHub: [@Ratnesh-181998](https://github.com/Ratnesh-181998)
- LinkedIn: [Ratnesh Singh](https://www.linkedin.com/in/ratnesh-singh)
- Email: ratnesh.analytics@gmail.com

---

## 🙏 Acknowledgments

- Aerofit for the business case study
- Streamlit community for excellent documentation
- Plotly for interactive visualization capabilities

---

## 📊 Project Stats

![GitHub repo size](https://img.shields.io/github/repo-size/Ratnesh-181998/Aerofit-Customer-Intelligence-Dashboard)
![GitHub stars](https://img.shields.io/github/stars/Ratnesh-181998/Aerofit-Customer-Intelligence-Dashboard?style=social)
![GitHub forks](https://img.shields.io/github/forks/Ratnesh-181998/Aerofit-Customer-Intelligence-Dashboard?style=social)

---

<div align="center">
  <p>Built with ❤️ using Streamlit & Plotly</p>
  <p>© 2025 Ratnesh Analytics</p>
</div>

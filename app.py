import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Create logger
logger = logging.getLogger(__name__)
logger.info("="*50)
logger.info("Application Started")
logger.info("="*50)

# Page Configuration
st.set_page_config(
    page_title="Aerofit Business Case",
    layout="wide",
    page_icon="🏃‍♂️",
    initial_sidebar_state="expanded"
)

# Custom CSS with enhanced dark theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        background-attachment: fixed;
    }
    .block-container {
        background: rgba(17, 24, 39, 0.85);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.7);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(139, 92, 246, 0.2);
    }
    h1 {
        background: linear-gradient(135deg, #a78bfa 0%, #f472b6 50%, #fb923c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        text-align: center;
        margin-bottom: 1rem;
        animation: fadeInDown 1s ease-in-out;
        letter-spacing: -1px;
    }
    h2 { 
        color: #f3f4f6 !important; 
        border-bottom: 3px solid #8b5cf6; 
        padding-bottom: 0.5rem; 
        margin-top: 2rem; 
        font-weight: 700 !important;
        text-shadow: 0 2px 10px rgba(139, 92, 246, 0.3);
    }
    h3 { 
        color: #e5e7eb !important; 
        margin-top: 1.5rem; 
        font-weight: 600 !important; 
    }
    p, li, span, div { color: #cbd5e1; }
    
    [data-testid="stMetricValue"] {
        background: linear-gradient(135deg, #a78bfa 0%, #f472b6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.8rem !important;
        font-weight: 800 !important;
        text-align: center;
        margin-bottom: 0.5rem;
        animation: pulse 2s ease-in-out infinite;
    }
    [data-testid="stMetricLabel"] { 
        color: #9ca3af !important; 
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 0.75rem !important;
    }
    
    .stTabs [data-baseweb="tab-list"] { 
        gap: 12px; 
        background-color: rgba(17, 24, 39, 0.5);
        padding: 0.5rem;
        border-radius: 12px;
    }
    .stTabs [data-baseweb="tab"] {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.1) 0%, rgba(244, 114, 182, 0.1) 100%);
        color: #a78bfa; 
        border-radius: 10px; 
        padding: 12px 24px; 
        font-weight: 600; 
        transition: all 0.3s ease; 
        border: 1px solid rgba(139, 92, 246, 0.3);
    }
    .stTabs [data-baseweb="tab"]:hover { 
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.2) 0%, rgba(244, 114, 182, 0.2) 100%);
        transform: translateY(-2px); 
        box-shadow: 0 4px 12px rgba(139, 92, 246, 0.4);
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%) !important; 
        color: white !important; 
        box-shadow: 0 6px 20px rgba(139, 92, 246, 0.6);
        transform: translateY(-2px);
    }
    
    [data-testid="stSidebar"] { 
        background: linear-gradient(180deg, #1e1b4b 0%, #312e81 100%); 
        border-right: 1px solid rgba(139, 92, 246, 0.3);
    }
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 { 
        color: white !important; 
        -webkit-text-fill-color: white !important; 
    }
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] li, 
    [data-testid="stSidebar"] span { 
        color: #cbd5e1 !important; 
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%); 
        color: white; 
        border-radius: 12px; 
        padding: 0.75rem 2rem; 
        font-weight: 600; 
        box-shadow: 0 4px 15px rgba(139, 92, 246, 0.4); 
        border: none;
        transition: all 0.3s ease;
    }
    .stButton > button:hover { 
        transform: translateY(-3px); 
        box-shadow: 0 8px 25px rgba(139, 92, 246, 0.6); 
        color: white; 
    }
    
    @keyframes fadeInDown { 
        from { opacity: 0; transform: translateY(-30px); } 
        to { opacity: 1; transform: translateY(0); } 
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
    }
    
    .card {
        padding: 2rem; 
        border-radius: 16px; 
        text-align: center; 
        color: white; 
        box-shadow: 0 8px 32px rgba(0,0,0,0.4); 
        transition: all 0.4s ease; 
        border: 1px solid rgba(255,255,255,0.1);
        position: relative;
        overflow: hidden;
    }
    .card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        transition: left 0.5s;
    }
    .card:hover::before {
        left: 100%;
    }
    .card:hover { 
        transform: translateY(-8px) scale(1.02); 
        box-shadow: 0 12px 40px rgba(139, 92, 246, 0.4);
    }
    
    .metric-card {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.1) 0%, rgba(244, 114, 182, 0.1) 100%);
        border: 1px solid rgba(139, 92, 246, 0.3);
        border-radius: 12px;
        padding: 1.5rem;
        transition: all 0.3s ease;
    }
    .metric-card:hover {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.2) 0%, rgba(244, 114, 182, 0.2) 100%);
        border-color: rgba(139, 92, 246, 0.5);
        transform: translateY(-4px);
        box-shadow: 0 8px 20px rgba(139, 92, 246, 0.3);
    }
    
    .stExpander {
        background: rgba(17, 24, 39, 0.5);
        border: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 12px;
    }
    
    .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

# Header with animation
st.markdown("""
<div style='position: fixed; top: 3.5rem; right: 1.5rem; z-index: 9999;'>
    <div style='background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%); 
                border-radius: 20px; padding: 0.6rem 1.2rem; 
                box-shadow: 0 4px 20px rgba(139, 92, 246, 0.5);
                animation: fadeInDown 1s ease-in-out;'>
        <span style='color: white; font-weight: 700; font-size: 0.9rem; letter-spacing: 1.5px;'>
            ✨ BY RATNESH SINGH
        </span>
    </div>
</div>
<div style='text-align: center; padding: 2rem 0 1rem 0;'>
    <h1 style='font-size: 4rem; margin-bottom: 0;'>🏃‍♂️ Aerofit Customer Intelligence Analytics</h1>
    <p style='font-size: 1.3rem; background: linear-gradient(135deg, #a78bfa 0%, #f472b6 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 700; margin-top: 0.5rem; letter-spacing: 1px;'>
        🎯 Target Audience Identification & Product Recommendation
    </p>
</div>
""", unsafe_allow_html=True)

# Enhanced Feature Cards with icons
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <div class='card' style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);'>
        <div style='font-size: 3rem; margin-bottom: 0.5rem;'>📊</div>
        <h3 style='color: white !important; margin: 0.5rem 0; font-size: 1.3rem;'>Data</h3>
        <p style='margin: 0; font-size: 0.9rem; color: rgba(255,255,255,0.8);'>Descriptive Statistics</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class='card' style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);'>
        <div style='font-size: 3rem; margin-bottom: 0.5rem;'>🔍</div>
        <h3 style='color: white !important; margin: 0.5rem 0; font-size: 1.3rem;'>EDA</h3>
        <p style='margin: 0; font-size: 0.9rem; color: rgba(255,255,255,0.8);'>Visual Analysis</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class='card' style='background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);'>
        <div style='font-size: 3rem; margin-bottom: 0.5rem;'>🎲</div>
        <h3 style='color: white !important; margin: 0.5rem 0; font-size: 1.3rem;'>Probability</h3>
        <p style='margin: 0; font-size: 0.9rem; color: rgba(255,255,255,0.8);'>Contingency Tables</p>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div class='card' style='background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);'>
        <div style='font-size: 3rem; margin-bottom: 0.5rem;'>💡</div>
        <h3 style='color: white !important; margin: 0.5rem 0; font-size: 1.3rem;'>Insights</h3>
        <p style='margin: 0; font-size: 0.9rem; color: rgba(255,255,255,0.8);'>Recommendations</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Enhanced Sidebar
with st.sidebar:
    st.markdown("## 📑 Navigation")
    st.markdown("---")
    st.markdown("""
    <div style='background: rgba(139, 92, 246, 0.1); padding: 1rem; border-radius: 10px; border: 1px solid rgba(139, 92, 246, 0.3);'>
        <h3 style='color: #a78bfa !important; margin-top: 0;'>📊 Project Overview</h3>
        <p><strong>Goal:</strong> Identify target audience for treadmills</p>
        <p><strong>Products:</strong> KP281, KP481, KP781</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background: rgba(244, 114, 182, 0.1); padding: 1rem; border-radius: 10px; border: 1px solid rgba(244, 114, 182, 0.3);'>
        <h3 style='color: #f472b6 !important; margin-top: 0;'>🔍 Analysis Steps</h3>
        <ul style='margin: 0; padding-left: 1.2rem;'>
            <li>Data Loading & Preprocessing</li>
            <li>Univariate & Bivariate EDA</li>
            <li>Probability Analysis</li>
            <li>Customer Segmentation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background: rgba(56, 239, 125, 0.1); padding: 1rem; border-radius: 10px; border: 1px solid rgba(56, 239, 125, 0.3);'>
        <h3 style='color: #38ef7d !important; margin-top: 0;'>💡 Key Insights</h3>
        <p>✓ <strong>KP281:</strong> Entry-level, mass market</p>
        <p>✓ <strong>KP481:</strong> Mid-level, female preference</p>
        <p>✓ <strong>KP781:</strong> Premium, high fitness</p>
    </div>
    """, unsafe_allow_html=True)

# Load Data
@st.cache_data
def load_data():
    logger.info("Loading data from aerofit_treadmill.csv")
    df = pd.read_csv("aerofit_treadmill.csv")
    logger.info(f"Data loaded successfully: {len(df)} rows, {df.shape[1]} columns")
    return df

# Preprocessing
@st.cache_data
def preprocess_data(df):
    logger.info("Starting data preprocessing")
    product_prices = {"KP281": 1500, "KP481": 1750, "KP781": 2500}
    df["Product_price"] = df["Product"].map(product_prices)
    
    fitness_map = {1: "Poor Shape", 2: "Bad Shape", 3: "Average Shape", 4: "Good Shape", 5: "Excellent Shape"}
    df["Fitness_category"] = df["Fitness"].map(fitness_map)
    
    bins = [0, 21, 35, 45, 60]
    labels = ["Teen (0-21)", "Adult (22-35)", "Mid-age (36-45)", "Towards old-age (>46)"]
    df["Age_category"] = pd.cut(df["Age"], bins=bins, labels=labels, include_lowest=True)
    
    logger.info("Data preprocessing completed: Added Product_price, Fitness_category, Age_category")
    return df

try:
    df_raw = load_data()
    df = preprocess_data(df_raw.copy())
    logger.info("Data ready for analysis")
except FileNotFoundError:
    logger.error("File 'aerofit_treadmill.csv' not found")
    st.error("❌ File 'aerofit_treadmill.csv' not found. Please ensure it is in the same directory.")
    st.stop()

# Tabs
tabs = st.tabs(["📊 Data Overview", "🔍 Interactive EDA", "🎲 Probability Analysis", "💡 Insights & Recommendations", "📚 Complete Analysis", "📝 Logs"])
logger.info("Main tabs created")

# TAB 1: Enhanced Data Overview
with tabs[0]:
    st.header("📊 Data Overview")
    logger.info("Data Overview tab accessed")
    
    # Animated Metrics
    m1, m2, m3, m4 = st.columns(4)
    with m1: 
        st.metric("Total Customers", f"{len(df):,}", "Rows", help="Total number of customer records")
    with m2: 
        st.metric("Features", f"{df.shape[1]}", "Columns", help="Number of data features")
    with m3: 
        st.metric("Avg Income", f"${df['Income'].mean():,.0f}", f"±${df['Income'].std():,.0f}")
    with m4: 
        st.metric("Avg Miles", f"{df['Miles'].mean():.0f}", f"±{df['Miles'].std():.0f} mi/wk")
    
    st.markdown("---")
    
    # Interactive Product Distribution
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🎯 Product Distribution")
        st.markdown("""
        <div style='background: rgba(102, 126, 234, 0.1); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;'>
            <p style='color: #cbd5e1; margin: 0; font-size: 0.9rem;'>
                This chart shows the sales distribution across all three treadmill models. 
                KP281 leads the market with the highest sales volume, indicating strong demand 
                for entry-level products.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        product_counts = df['Product'].value_counts()
        fig = go.Figure(data=[go.Bar(
            x=product_counts.index,
            y=product_counts.values,
            marker=dict(
                color=['#667eea', '#f093fb', '#11998e'],
                line=dict(color='rgba(255,255,255,0.3)', width=2)
            ),
            text=product_counts.values,
            textposition='outside',
            hovertemplate='<b>%{x}</b><br>Count: %{y}<br>Percentage: %{y:.1%}<extra></extra>'
        )])
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#cbd5e1'),
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor='rgba(139, 92, 246, 0.1)'),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.success(f"""
        **Key Insight:** KP281 accounts for {(product_counts['KP281']/len(df)*100):.1f}% of total sales, 
        making it the market leader. This suggests strong price sensitivity among customers.
        """)
    
    with col2:
        st.subheader("💰 Revenue by Product")
        st.markdown("""
        <div style='background: rgba(240, 147, 251, 0.1); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;'>
            <p style='color: #cbd5e1; margin: 0; font-size: 0.9rem;'>
                Revenue distribution reveals the financial contribution of each product. 
                Despite lower unit sales, KP781 generates significant revenue due to its premium pricing.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        revenue = df.groupby('Product')['Product_price'].sum()
        fig = go.Figure(data=[go.Pie(
            labels=revenue.index,
            values=revenue.values,
            hole=0.4,
            marker=dict(colors=['#667eea', '#f093fb', '#11998e']),
            textinfo='label+percent',
            hovertemplate='<b>%{label}</b><br>Revenue: $%{value:,.0f}<extra></extra>'
        )])
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#cbd5e1'),
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
        
        total_revenue = revenue.sum()
        kp781_revenue_pct = (revenue['KP781']/total_revenue*100)
        st.info(f"""
        **Revenue Insight:** KP781 contributes {kp781_revenue_pct:.1f}% of total revenue 
        despite having the lowest sales volume, highlighting the importance of premium products.
        """)
    
    st.markdown("---")
    
    # Interactive Data Table
    st.subheader("🔍 Interactive Data Explorer")
    
    col_filter1, col_filter2, col_filter3 = st.columns(3)
    with col_filter1:
        product_filter = st.multiselect("Filter by Product", df['Product'].unique(), default=df['Product'].unique())
    with col_filter2:
        gender_filter = st.multiselect("Filter by Gender", df['Gender'].unique(), default=df['Gender'].unique())
    with col_filter3:
        age_range = st.slider("Age Range", int(df['Age'].min()), int(df['Age'].max()), (int(df['Age'].min()), int(df['Age'].max())))
    
    filtered_df = df[
        (df['Product'].isin(product_filter)) & 
        (df['Gender'].isin(gender_filter)) &
        (df['Age'] >= age_range[0]) &
        (df['Age'] <= age_range[1])
    ]
    
    st.info(f"📊 Showing **{len(filtered_df)}** of **{len(df)}** records")
    st.dataframe(filtered_df, use_container_width=True, height=400)

# TAB 2: Interactive EDA with Plotly
with tabs[1]:
    st.header("🔍 Interactive Exploratory Data Analysis")
    logger.info("Interactive EDA tab accessed")
    
    viz_tabs = st.tabs(["📈 Distributions", "🔗 Relationships", "🎨 Multivariate", "⚠️ Outliers"])
    
    with viz_tabs[0]:
        st.subheader("Distribution Analysis")
        
        st.markdown("""
        <div style='background: rgba(139, 92, 246, 0.1); padding: 1rem; border-radius: 10px; border-left: 4px solid #8b5cf6; margin-bottom: 1.5rem;'>
            <h4 style='color: #a78bfa; margin-top: 0;'>📊 Understanding Customer Demographics</h4>
            <p style='color: #cbd5e1; margin: 0;'>
                Distribution analysis helps us understand the composition of our customer base. 
                These visualizations reveal patterns in gender, age, and other key attributes that 
                influence purchasing decisions.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Gender Distribution**")
            st.caption("📌 Shows the split between male and female customers")
            
            gender_counts = df['Gender'].value_counts()
            fig = go.Figure(data=[go.Bar(
                x=gender_counts.index,
                y=gender_counts.values,
                marker=dict(
                    color=['#8b5cf6', '#ec4899'],
                    line=dict(color='rgba(255,255,255,0.3)', width=2)
                ),
                text=gender_counts.values,
                textposition='outside'
            )])
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#cbd5e1'),
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=True, gridcolor='rgba(139, 92, 246, 0.1)'),
                height=350
            )
            st.plotly_chart(fig, use_container_width=True)
            
            male_pct = (gender_counts['Male']/len(df)*100)
            st.info(f"""
            **Gender Insight:** Males represent {male_pct:.1f}% of customers. 
            This slight male majority suggests opportunities for targeted female marketing campaigns.
            """)
        
        with col2:
            st.markdown("**Age Distribution**")
            st.caption("📌 Histogram showing age spread across customer base")
            
            fig = go.Figure(data=[go.Histogram(
                x=df['Age'],
                nbinsx=20,
                marker=dict(
                    color='#8b5cf6',
                    line=dict(color='rgba(255,255,255,0.3)', width=1)
                )
            )])
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#cbd5e1'),
                xaxis=dict(showgrid=False, title='Age'),
                yaxis=dict(showgrid=True, gridcolor='rgba(139, 92, 246, 0.1)', title='Count'),
                height=350
            )
            st.plotly_chart(fig, use_container_width=True)
            
            median_age = df['Age'].median()
            age_range = f"{df['Age'].min()}-{df['Age'].max()}"
            st.info(f"""
            **Age Insight:** Median age is {median_age:.0f} years (range: {age_range}). 
            The distribution shows concentration in the 22-35 age group, our core demographic.
            """)
        
        # Interactive selector for numerical features
        st.markdown("---")
        st.markdown("**📊 Explore Numerical Features by Product**")
        st.caption("📌 Compare how different products perform across various metrics")
        
        num_feature = st.selectbox("Select Feature", ['Income', 'Miles', 'Usage', 'Fitness'])
        
        feature_descriptions = {
            'Income': 'Annual income levels show purchasing power and product affordability',
            'Miles': 'Expected weekly miles indicate usage intensity and fitness goals',
            'Usage': 'Planned weekly usage frequency reflects commitment level',
            'Fitness': 'Self-rated fitness (1-5 scale) correlates with product choice'
        }
        
        st.markdown(f"""
        <div style='background: rgba(17, 153, 142, 0.1); padding: 0.75rem; border-radius: 8px; margin-bottom: 1rem;'>
            <p style='color: #cbd5e1; margin: 0; font-size: 0.85rem;'>
                💡 <strong>{num_feature}:</strong> {feature_descriptions[num_feature]}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        fig = go.Figure()
        for product in df['Product'].unique():
            product_data = df[df['Product'] == product][num_feature]
            fig.add_trace(go.Box(
                y=product_data,
                name=product,
                boxmean='sd'
            ))
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#cbd5e1'),
            yaxis=dict(showgrid=True, gridcolor='rgba(139, 92, 246, 0.1)', title=num_feature),
            xaxis=dict(showgrid=False, title='Product'),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with viz_tabs[1]:
        st.subheader("Relationship Analysis")
        
        st.markdown("""
        <div style='background: rgba(244, 114, 182, 0.1); padding: 1rem; border-radius: 10px; border-left: 4px solid #f472b6; margin-bottom: 1.5rem;'>
            <h4 style='color: #f472b6; margin-top: 0;'>🔗 Exploring Variable Relationships</h4>
            <p style='color: #cbd5e1; margin: 0;'>
                Bivariate analysis reveals how different variables interact with each other. 
                These relationships help us understand customer behavior patterns and product preferences.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Product vs Gender**")
            st.caption("📌 Grouped bar chart showing gender preferences across products")
            
            cross_tab = pd.crosstab(df['Product'], df['Gender'])
            fig = go.Figure(data=[
                go.Bar(name='Female', x=cross_tab.index, y=cross_tab['Female'], marker_color='#ec4899'),
                go.Bar(name='Male', x=cross_tab.index, y=cross_tab['Male'], marker_color='#8b5cf6')
            ])
            fig.update_layout(
                barmode='group',
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#cbd5e1'),
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=True, gridcolor='rgba(139, 92, 246, 0.1)'),
                height=350
            )
            st.plotly_chart(fig, use_container_width=True)
            
            st.success("""
            **Gender Pattern:** KP281 shows balanced gender appeal, KP481 leans female, 
            while KP781 is predominantly purchased by males. This suggests different marketing 
            strategies for each product line.
            """)
        
        with col2:
            st.markdown("**Income vs Product**")
            st.caption("📌 Violin plot displaying income distribution for each product")
            
            fig = go.Figure()
            for product in df['Product'].unique():
                product_data = df[df['Product'] == product]
                fig.add_trace(go.Violin(
                    y=product_data['Income'],
                    name=product,
                    box_visible=True,
                    meanline_visible=True
                ))
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#cbd5e1'),
                yaxis=dict(showgrid=True, gridcolor='rgba(139, 92, 246, 0.1)', title='Income'),
                height=350
            )
            st.plotly_chart(fig, use_container_width=True)
            
            st.success("""
            **Income Correlation:** Clear income stratification exists across products. 
            KP781 customers have significantly higher income levels, validating the premium 
            positioning strategy.
            """)
        
        # Scatter plot
        st.markdown("---")
        st.markdown("**💰 Income vs Miles (Interactive)**")
        st.caption("📌 Bubble chart showing relationship between income, miles, and product choice (bubble size = usage frequency)")
        
        st.markdown("""
        <div style='background: rgba(56, 239, 125, 0.1); padding: 0.75rem; border-radius: 8px; margin-bottom: 1rem;'>
            <p style='color: #cbd5e1; margin: 0; font-size: 0.85rem;'>
                💡 This visualization reveals the correlation between income and expected miles. 
                Hover over points to see detailed customer information including gender, age, and fitness level.
            </p>
        </div>
        """, unsafe_allow_html=True)
        fig = px.scatter(df, x='Income', y='Miles', color='Product', size='Usage',
                        hover_data=['Gender', 'Age', 'Fitness_category'],
                        color_discrete_sequence=['#667eea', '#f093fb', '#11998e'])
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#cbd5e1'),
            xaxis=dict(showgrid=True, gridcolor='rgba(139, 92, 246, 0.1)'),
            yaxis=dict(showgrid=True, gridcolor='rgba(139, 92, 246, 0.1)'),
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with viz_tabs[2]:
        st.subheader("Multivariate Analysis")
        
        # Interactive Correlation Heatmap
        st.markdown("**🔥 Correlation Heatmap**")
        numeric_df = df.select_dtypes(include=[np.number])
        corr = numeric_df.corr()
        
        fig = go.Figure(data=go.Heatmap(
            z=corr.values,
            x=corr.columns,
            y=corr.columns,
            colorscale='RdBu',
            zmid=0,
            text=corr.values.round(2),
            texttemplate='%{text}',
            textfont={"size": 10},
            colorbar=dict(title="Correlation")
        ))
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#cbd5e1'),
            height=600
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("""
        **🔍 Key Correlations:**
        - **Fitness & Miles**: 0.79 (Strong positive)
        - **Product Price & Income**: 0.70 (Strong positive)
        - **Usage & Miles**: 0.76 (Strong positive)
        """)
        
        # 3D Scatter
        st.markdown("**🎯 3D Feature Space**")
        fig = px.scatter_3d(df, x='Income', y='Miles', z='Age', color='Product',
                           size='Usage', hover_data=['Gender', 'Fitness_category'],
                           color_discrete_sequence=['#667eea', '#f093fb', '#11998e'])
        fig.update_layout(
            scene=dict(
                bgcolor='rgba(0,0,0,0)',
                xaxis=dict(backgroundcolor='rgba(0,0,0,0)', gridcolor='rgba(139, 92, 246, 0.2)'),
                yaxis=dict(backgroundcolor='rgba(0,0,0,0)', gridcolor='rgba(139, 92, 246, 0.2)'),
                zaxis=dict(backgroundcolor='rgba(0,0,0,0)', gridcolor='rgba(139, 92, 246, 0.2)')
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#cbd5e1'),
            height=600
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with viz_tabs[3]:
        st.subheader("Outlier Detection")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Miles Outliers**")
            fig = go.Figure()
            fig.add_trace(go.Box(y=df['Miles'], name='Miles', marker_color='#8b5cf6', boxmean='sd'))
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#cbd5e1'),
                yaxis=dict(showgrid=True, gridcolor='rgba(139, 92, 246, 0.1)'),
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("**Income Outliers**")
            fig = go.Figure()
            fig.add_trace(go.Box(y=df['Income'], name='Income', marker_color='#ec4899', boxmean='sd'))
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#cbd5e1'),
                yaxis=dict(showgrid=True, gridcolor='rgba(139, 92, 246, 0.1)'),
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
        
        st.info("⚠️ High income and high miles outliers are largely associated with the **KP781** product.")

# TAB 3: Probability Analysis
with tabs[2]:
    st.header("🎲 Probability & Contingency Analysis")
    logger.info("Probability Analysis tab accessed")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Marginal Probabilities")
        prob_product = df["Product"].value_counts(normalize=True).mul(100).round(2)
        
        fig = go.Figure(data=[go.Bar(
            x=prob_product.index,
            y=prob_product.values,
            marker=dict(color=['#667eea', '#f093fb', '#11998e']),
            text=[f'{v:.1f}%' for v in prob_product.values],
            textposition='outside'
        )])
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#cbd5e1'),
            xaxis=dict(showgrid=False, title='Product'),
            yaxis=dict(showgrid=True, gridcolor='rgba(139, 92, 246, 0.1)', title='Probability (%)'),
            height=350
        )
        st.plotly_chart(fig, use_container_width=True)
        st.caption("✅ KP281 is the most popular product (44.4%)")
    
    with col2:
        st.markdown("### 👥 Gender Probability")
        prob_gender = df["Gender"].value_counts(normalize=True).mul(100).round(2)
        
        fig = go.Figure(data=[go.Pie(
            labels=prob_gender.index,
            values=prob_gender.values,
            hole=0.4,
            marker=dict(colors=['#8b5cf6', '#ec4899']),
            textinfo='label+percent'
        )])
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#cbd5e1'),
            height=350,
            showlegend=True
        )
        st.plotly_chart(fig, use_container_width=True)
        st.caption("👨 Male customers (57.8%) > Female (42.2%)")
    
    st.markdown("---")
    
    # Conditional Probabilities with interactive heatmaps
    st.subheader("🔍 Conditional Probabilities")
    
    prob_tabs = st.tabs(["Product vs Gender", "Product vs Age", "Product vs Fitness"])
    
    with prob_tabs[0]:
        st.markdown("**Product vs Gender**")
        cond_prob = pd.crosstab(df["Product"], df["Gender"], margins=True, normalize='columns').mul(100).round(2)
        
        fig = go.Figure(data=go.Heatmap(
            z=cond_prob.iloc[:-1, :-1].values,
            x=cond_prob.columns[:-1],
            y=cond_prob.index[:-1],
            colorscale='Purples',
            text=cond_prob.iloc[:-1, :-1].values,
            texttemplate='%{text:.1f}%',
            textfont={"size": 14},
            colorbar=dict(title="Probability (%)")
        ))
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#cbd5e1'),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        st.success("✨ **KP781** is heavily skewed towards male customers (31.7% of males vs 9.2% of females)")
    
    with prob_tabs[1]:
        st.markdown("**Product vs Age Category**")
        cond_prob_age = pd.crosstab(df["Product"], df["Age_category"], margins=True, normalize='columns').mul(100).round(2)
        
        fig = go.Figure(data=go.Heatmap(
            z=cond_prob_age.iloc[:-1, :-1].values,
            x=cond_prob_age.columns[:-1],
            y=cond_prob_age.index[:-1],
            colorscale='Blues',
            text=cond_prob_age.iloc[:-1, :-1].values,
            texttemplate='%{text:.1f}%',
            textfont={"size": 12},
            colorbar=dict(title="Probability (%)")
        ))
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#cbd5e1'),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        st.info("🎯 Teens (0-21) strongly prefer **KP281** (58.8%)")
    
    with prob_tabs[2]:
        st.markdown("**Product vs Fitness Category**")
        cond_prob_fitness = pd.crosstab(df["Product"], df["Fitness_category"], margins=True, normalize='columns').mul(100).round(2)
        
        fig = go.Figure(data=go.Heatmap(
            z=cond_prob_fitness.iloc[:-1, :-1].values,
            x=cond_prob_fitness.columns[:-1],
            y=cond_prob_fitness.index[:-1],
            colorscale='Greens',
            text=cond_prob_fitness.iloc[:-1, :-1].values,
            texttemplate='%{text:.1f}%',
            textfont={"size": 10},
            colorbar=dict(title="Probability (%)")
        ))
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#cbd5e1'),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        st.success("💪 **93.5%** of 'Excellent Shape' customers buy **KP781**")

# TAB 4: Insights & Recommendations
with tabs[3]:
    st.header("💡 Business Insights & Recommendations")
    logger.info("Insights & Recommendations tab accessed")
    
    # Customer Profiles
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='card' style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); text-align: left; height: 320px;'>
            <div style='font-size: 2.5rem; margin-bottom: 1rem;'>🥉 KP281</div>
            <h3 style='color: white !important; margin: 0 0 1rem 0;'>Entry Level</h3>
            <ul style='color: rgba(255,255,255,0.9); padding-left: 1.2rem; line-height: 1.8;'>
                <li><strong>Target:</strong> Beginners, Budget-conscious</li>
                <li><strong>Demographics:</strong> Both genders, all ages</li>
                <li><strong>Usage:</strong> Light/Moderate (3-4x/week)</li>
                <li><strong>Income:</strong> < $60k</li>
                <li><strong>Price:</strong> $1,500</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='card' style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); text-align: left; height: 320px;'>
            <div style='font-size: 2.5rem; margin-bottom: 1rem;'>🥈 KP481</div>
            <h3 style='color: white !important; margin: 0 0 1rem 0;'>Mid Level</h3>
            <ul style='color: rgba(255,255,255,0.9); padding-left: 1.2rem; line-height: 1.8;'>
                <li><strong>Target:</strong> Intermediate users</li>
                <li><strong>Demographics:</strong> Strong Female appeal</li>
                <li><strong>Usage:</strong> Moderate (3-4x/week)</li>
                <li><strong>Income:</strong> $50k - $70k</li>
                <li><strong>Price:</strong> $1,750</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='card' style='background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); text-align: left; height: 320px;'>
            <div style='font-size: 2.5rem; margin-bottom: 1rem;'>🥇 KP781</div>
            <h3 style='color: white !important; margin: 0 0 1rem 0;'>Advanced</h3>
            <ul style='color: rgba(255,255,255,0.9); padding-left: 1.2rem; line-height: 1.8;'>
                <li><strong>Target:</strong> Athletes, High-income</li>
                <li><strong>Demographics:</strong> Predominantly Male</li>
                <li><strong>Usage:</strong> High (>4x/week, >120 mi)</li>
                <li><strong>Income:</strong> > $80k</li>
                <li><strong>Price:</strong> $2,500</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Actionable Recommendations
    st.subheader("🚀 Actionable Recommendations")
    
    rec_col1, rec_col2 = st.columns(2)
    
    with rec_col1:
        with st.expander("🎯 **Marketing Strategies**", expanded=True):
            st.markdown("""
            1. **KP781 Premium Positioning**
               - Target high-income demographics ($80k+)
               - Partner with premium gyms and fitness clubs
               - Corporate wellness programs
               - Emphasize advanced features and durability
            
            2. **Female-Focused Campaigns**
               - Market KP281 and KP481 to women
               - Highlight health and wellness benefits
               - Use female fitness influencers
               - Create women-centric marketing materials
            """)
    
    with rec_col2:
        with st.expander("💼 **Product Strategy**", expanded=True):
            st.markdown("""
            3. **KP481 Differentiation**
               - Clearer positioning vs KP281
               - Highlight unique intermediate features
               - Justify price premium with value-adds
               - Bundle with accessories or services
            
            4. **Customer Lifecycle Management**
               - Trade-in program (KP281 → KP781)
               - Loyalty rewards for upgrades
               - Fitness tracking integration
               - Personalized recommendations
            """)
    
    st.markdown("---")
    
    # Key Metrics Summary
    st.subheader("📈 Key Performance Indicators")
    
    kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)
    
    with kpi1:
        st.metric("Market Leader", "KP281", "44.4%", help="Highest selling product")
    with kpi2:
        st.metric("Female Preference", "KP281", "52.6%", help="Female customers prefer KP281")
    with kpi3:
        st.metric("Male Premium", "KP781", "31.7%", help="Male customers prefer premium")
    with kpi4:
        st.metric("Fitness Elite", "KP781", "93.5%", help="Excellent shape → KP781")
    with kpi5:
        st.metric("Avg Revenue", f"${df.groupby('Product')['Product_price'].sum().mean():,.0f}", "Per Product")

# TAB 5: Complete Analysis
with tabs[4]:
    st.header("📚 Complete Analysis")
    logger.info("Complete Analysis tab accessed")
    
    st.info("This section contains the comprehensive analysis from the Jupyter Notebook, including all findings, methodologies, and detailed insights.")
    
    analysis_tabs = st.tabs([
        "📋 Problem & Context", 
        "📊 Data Dictionary", 
        "🔬 Analysis Steps",
        "📈 Key Findings",
        "👥 Customer Profiles",
        "💡 Recommendations"
    ])
    
    # Sub-tab 1: Problem & Context
    with analysis_tabs[0]:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 2rem; border-radius: 15px; margin-bottom: 2rem;
                    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);'>
            <h3 style='color: white; margin-top: 0;'>🎯 Business Problem</h3>
            <p style='color: white; font-size: 1.1rem;'>
                Identify the characteristics of the target audience for each type of treadmill offered by the company, 
                to provide a better recommendation of the treadmills to the new customers.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🏃‍♂️ Product Portfolio")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style='background: rgba(102, 126, 234, 0.1); padding: 1.5rem; border-radius: 10px; border: 1px solid rgba(102, 126, 234, 0.3);'>
                <h4 style='color: #667eea;'>KP281</h4>
                <p style='color: #cbd5e1;'><strong>Entry-level treadmill</strong></p>
                <p style='color: #9ca3af;'>Price: $1,500</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style='background: rgba(240, 147, 251, 0.1); padding: 1.5rem; border-radius: 10px; border: 1px solid rgba(240, 147, 251, 0.3);'>
                <h4 style='color: #f093fb;'>KP481</h4>
                <p style='color: #cbd5e1;'><strong>Mid-level runners</strong></p>
                <p style='color: #9ca3af;'>Price: $1,750</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style='background: rgba(17, 153, 142, 0.1); padding: 1.5rem; border-radius: 10px; border: 1px solid rgba(17, 153, 142, 0.3);'>
                <h4 style='color: #11998e;'>KP781</h4>
                <p style='color: #cbd5e1;'><strong>Advanced features</strong></p>
                <p style='color: #9ca3af;'>Price: $2,500</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("### 🎯 Objectives")
        st.markdown("""
        1. **Descriptive Analytics**: Create customer profiles for each product
        2. **Probability Analysis**: Construct contingency tables and compute probabilities
        3. **Insights**: Investigate differences across products with respect to customer characteristics
        """)
    
    # Sub-tab 2: Data Dictionary
    with analysis_tabs[1]:
        st.markdown("### 📊 Dataset Overview")
        st.metric("Total Records", len(df), "Customers")
        st.metric("Features", df.shape[1], "Columns")
        
        st.markdown("### 📋 Feature Descriptions")
        
        features_info = {
            "Product": "Product Purchased: KP281, KP481, or KP781",
            "Age": "Age in years",
            "Gender": "Male/Female",
            "Education": "Education in years",
            "MaritalStatus": "Single or partnered",
            "Usage": "Average number of times the customer plans to use the treadmill each week",
            "Fitness": "Self-rated fitness on a 1-to-5 scale (1=poor shape, 5=excellent shape)",
            "Income": "Annual income (in USD)",
            "Miles": "Average number of miles the customer expects to walk/run each week"
        }
        
        for feature, desc in features_info.items():
            st.markdown(f"""
            <div style='background: rgba(139, 92, 246, 0.1); padding: 1rem; border-radius: 8px; margin-bottom: 0.5rem; border-left: 3px solid #8b5cf6;'>
                <strong style='color: #a78bfa;'>{feature}:</strong> <span style='color: #cbd5e1;'>{desc}</span>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("### 📈 Summary Statistics")
        st.dataframe(df.describe(), use_container_width=True)
    
    # Sub-tab 3: Analysis Steps
    with analysis_tabs[2]:
        st.markdown("### 🔬 Methodology")
        
        steps = [
            {"num": "1", "title": "Data Preprocessing", "desc": "Created Fitness_category, Age_category, and Product_price features", "color": "#667eea"},
            {"num": "2", "title": "Exploratory Data Analysis", "desc": "Analyzed distributions, correlations, and relationships", "color": "#f472b6"},
            {"num": "3", "title": "Outlier Detection", "desc": "Identified 13 outliers in Miles (>187.875) and 19 in Income (>$80,581)", "color": "#11998e"},
            {"num": "4", "title": "Probability Analysis", "desc": "Computed marginal and conditional probabilities across demographics", "color": "#fa709a"},
            {"num": "5", "title": "Customer Profiling", "desc": "Created detailed profiles for each product's target audience", "color": "#fee140"}
        ]
        
        for step in steps:
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, {step['color']}22 0%, {step['color']}11 100%); 
                        padding: 1.5rem; border-radius: 15px; margin-bottom: 1rem;
                        border-left: 5px solid {step['color']};'>
                <div style='display: flex; align-items: center;'>
                    <div style='background: {step['color']}; color: white; width: 40px; height: 40px; 
                                border-radius: 50%; display: flex; align-items: center; justify-content: center;
                                font-weight: bold; font-size: 1.2rem; margin-right: 1rem;'>
                        {step['num']}
                    </div>
                    <div>
                        <h4 style='color: {step['color']}; margin: 0;'>{step['title']}</h4>
                        <p style='color: #9ca3af; margin: 0.5rem 0 0 0;'>{step['desc']}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("### 🔍 Key Correlations Found")
        st.success("""
        - **Fitness & Miles**: 0.79 - Strong positive correlation
        - **Product Price & Income**: 0.70 - Higher income → Premium products
        - **Usage & Miles**: 0.76 - More frequent use → More miles
        """)
    
    # Sub-tab 4: Key Findings
    with analysis_tabs[3]:
        st.markdown("### 📊 Probability Insights")
        
        findings = [
            {"title": "Gender Preferences", "stat": "52.6%", "desc": "of female customers buy KP281 vs 38.5% of males"},
            {"title": "Male Premium Preference", "stat": "31.7%", "desc": "of male customers buy KP781 vs only 9.2% of females"},
            {"title": "Age Factor", "stat": "58.8%", "desc": "of teens (0-21) prefer KP281, none buy KP781"},
            {"title": "Fitness Correlation", "stat": "93.5%", "desc": "of customers in Excellent Shape buy KP781"}
        ]
        
        cols = st.columns(2)
        for idx, finding in enumerate(findings):
            with cols[idx % 2]:
                st.markdown(f"""
                <div style='background: rgba(139, 92, 246, 0.1); padding: 1.5rem; border-radius: 10px; margin-bottom: 1rem;'>
                    <h3 style='color: #8b5cf6; margin: 0; font-size: 2rem;'>{finding['stat']}</h3>
                    <h4 style='color: #a78bfa; margin: 0.5rem 0;'>{finding['title']}</h4>
                    <p style='color: #cbd5e1; margin: 0;'>{finding['desc']}</p>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("### 📈 Product vs Miles Analysis")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Average Miles by Product**")
            avg_miles_product = df.groupby('Product')['Miles'].mean().round(1)
            for product, miles in avg_miles_product.items():
                st.metric(product, f"{miles} miles/week")
        
        with col2:
            st.markdown("**Miles Range by Product**")
            st.write("- **KP281**: 70-90 miles/week")
            st.write("- **KP481**: 70-130 miles/week")
            st.write("- **KP781**: 120-200+ miles/week")
    
    # Sub-tab 5: Customer Profiles
    with analysis_tabs[4]:
        st.markdown("### 👥 Detailed Customer Profiling")
        
        st.markdown("#### 🥉 KP281 - Entry Level")
        st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea22 0%, #764ba211 100%); 
                    padding: 1.5rem; border-radius: 15px; margin-bottom: 1.5rem;
                    border-left: 5px solid #667eea;'>
            <ul style='color: #cbd5e1; margin: 0;'>
                <li><strong>Market Share:</strong> 44.4% (Highest selling product)</li>
                <li><strong>Gender Split:</strong> Equal appeal to both genders</li>
                <li><strong>Age Distribution:</strong> 56 Adults, 10 Teens, 11 Mid-age, 3 Old-age</li>
                <li><strong>Usage:</strong> 3-4 times per week</li>
                <li><strong>Miles:</strong> 70-90 miles per week average</li>
                <li><strong>Fitness Level:</strong> Average Shape</li>
                <li><strong>Income:</strong> < $60,000</li>
                <li><strong>Target:</strong> General purpose for all age groups and fitness levels</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### 🥈 KP481 - Mid Level")
        st.markdown("""
        <div style='background: linear-gradient(135deg, #f093fb22 0%, #f5576c11 100%); 
                    padding: 1.5rem; border-radius: 15px; margin-bottom: 1.5rem;
                    border-left: 5px solid #f093fb;'>
            <ul style='color: #cbd5e1; margin: 0;'>
                <li><strong>Market Share:</strong> 33.3%</li>
                <li><strong>Gender Preference:</strong> Strong female appeal (38.15% vs 29.80% male)</li>
                <li><strong>Age Distribution:</strong> 45 Adults, 7 Teens, 7 Mid-age, 1 Old-age</li>
                <li><strong>Usage:</strong> 3-4 times per week (less frequent but more miles)</li>
                <li><strong>Miles:</strong> 70-130+ miles per week</li>
                <li><strong>Fitness Level:</strong> Bad to Average Shape</li>
                <li><strong>Income:</strong> $50,000 - $70,000</li>
                <li><strong>Recommendation:</strong> Specifically for female intermediate users</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### 🥇 KP781 - Advanced")
        st.markdown("""
        <div style='background: linear-gradient(135deg, #11998e22 0%, #38ef7d11 100%); 
                    padding: 1.5rem; border-radius: 15px; margin-bottom: 1.5rem;
                    border-left: 5px solid #11998e;'>
            <ul style='color: #cbd5e1; margin: 0;'>
                <li><strong>Market Share:</strong> 22.2% (Least sold but highest revenue per unit)</li>
                <li><strong>Gender Skew:</strong> Predominantly male (31.73% vs 9.21% female)</li>
                <li><strong>Age Distribution:</strong> 34 Adults, 0 Teens, 4 Mid-age, 2 Old-age</li>
                <li><strong>Usage:</strong> 4-5+ times per week (extensive use)</li>
                <li><strong>Miles:</strong> 120-200+ miles per week</li>
                <li><strong>Fitness Level:</strong> Excellent Shape (93.5% probability)</li>
                <li><strong>Income:</strong> > $80,000 (high-income earners)</li>
                <li><strong>Marital Status:</strong> Slightly higher among single customers</li>
                <li><strong>Target:</strong> Athletes and serious fitness enthusiasts</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Sub-tab 6: Recommendations
    with analysis_tabs[5]:
        st.markdown("### 💡 Strategic Recommendations")
        
        recommendations = [
            {
                "category": "Marketing Strategy",
                "icon": "📢",
                "color": "#667eea",
                "items": [
                    "Target KP781 to high-income males, adults and age 45+",
                    "Market KP481 specifically to female intermediate users",
                    "Position KP281 as the ideal starter for all demographics",
                    "Partner with premium gyms for KP781 promotion"
                ]
            },
            {
                "category": "Product Improvements",
                "icon": "🔧",
                "color": "#f472b6",
                "items": [
                    "Enhance KP481 features to justify price vs KP281",
                    "KP481 shows similar fitness/miles stats to cheaper KP281",
                    "Consider product enhancements or price adjustment",
                    "Add unique features to improve customer experience"
                ]
            },
            {
                "category": "Customer Targeting",
                "icon": "🎯",
                "color": "#11998e",
                "items": [
                    "Implement upgrade path: KP281 → KP781 as fitness improves",
                    "Create trade-in program for customer retention",
                    "Use income and fitness data for personalized recommendations",
                    "Focus on customer lifecycle management"
                ]
            }
        ]
        
        for rec in recommendations:
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, {rec['color']}22 0%, {rec['color']}11 100%); 
                        padding: 1.5rem; border-radius: 15px; margin-bottom: 1.5rem;
                        border-left: 5px solid {rec['color']};'>
                <h3 style='color: {rec['color']}; margin-top: 0;'>{rec['icon']} {rec['category']}</h3>
                <ul style='color: #cbd5e1; margin: 0;'>
            """, unsafe_allow_html=True)
            
            for item in rec['items']:
                st.markdown(f"<li>{item}</li>", unsafe_allow_html=True)
            
            st.markdown("</ul></div>", unsafe_allow_html=True)
        
        st.markdown("### 📊 Expected Business Impact")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style='background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); 
                        padding: 1.5rem; border-radius: 15px; text-align: center;
                        box-shadow: 0 4px 15px rgba(17, 153, 142, 0.4);'>
                <h2 style='color: white; margin: 0; border: none; font-size: 2.5rem;'>20-25%</h2>
                <p style='color: white; margin: 0.5rem 0 0 0;'>Increase in KP781 Sales</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        padding: 1.5rem; border-radius: 15px; text-align: center;
                        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);'>
                <h2 style='color: white; margin: 0; border: none; font-size: 2.5rem;'>30-35%</h2>
                <p style='color: white; margin: 0.5rem 0 0 0;'>Better Customer Targeting</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                        padding: 1.5rem; border-radius: 15px; text-align: center;
                        box-shadow: 0 4px 15px rgba(240, 147, 251, 0.4);'>
                <h2 style='color: white; margin: 0; border: none; font-size: 2.5rem;'>15-20%</h2>
                <p style='color: white; margin: 0.5rem 0 0 0;'>Customer Satisfaction</p>
            </div>
            """, unsafe_allow_html=True)

# TAB 6: Logs
with tabs[5]:
    st.header("📝 Application Logs")
    logger.info("Logs tab accessed")
    
    st.markdown("""
    <div style='background: rgba(139, 92, 246, 0.1); padding: 1rem; border-radius: 10px; border-left: 4px solid #8b5cf6; margin-bottom: 1rem;'>
        <p style='color: #cbd5e1; margin: 0;'>
            <strong style='color: #a78bfa;'>📌 Note:</strong> This section displays all application activities, 
            including data loading, user interactions, and system events.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Log controls
    col1, col2, col3 = st.columns([2, 2, 1])
    
    with col1:
        log_filter = st.selectbox(
            "Filter by Level",
            ["All", "INFO", "WARNING", "ERROR"],
            help="Filter logs by severity level"
        )
    
    with col2:
        search_term = st.text_input("🔍 Search logs", placeholder="Enter search term...")
    
    with col3:
        auto_refresh = st.checkbox("Auto-refresh", value=False)
    
    st.markdown("---")
    
    # Read and display logs
    try:
        with open("app.log", "r") as f:
            log_content = f.readlines()
        
        # Filter logs
        filtered_logs = []
        for line in log_content:
            # Apply level filter
            if log_filter != "All" and log_filter not in line:
                continue
            # Apply search filter
            if search_term and search_term.lower() not in line.lower():
                continue
            filtered_logs.append(line)
        
        # Display statistics
        col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
        
        total_logs = len(log_content)
        info_count = sum(1 for line in log_content if "INFO" in line)
        warning_count = sum(1 for line in log_content if "WARNING" in line)
        error_count = sum(1 for line in log_content if "ERROR" in line)
        
        with col_stat1:
            st.metric("Total Logs", total_logs, help="Total number of log entries")
        with col_stat2:
            st.metric("INFO", info_count, help="Informational messages")
        with col_stat3:
            st.metric("WARNING", warning_count, help="Warning messages", delta_color="off")
        with col_stat4:
            st.metric("ERROR", error_count, help="Error messages", delta_color="inverse")
        
        st.markdown("---")
        
        # Display filtered logs
        if filtered_logs:
            st.markdown(f"**Showing {len(filtered_logs)} of {total_logs} log entries**")
            
            # Create a styled log display
            log_display = ""
            for line in reversed(filtered_logs[-100:]):  # Show last 100 filtered logs
                line = line.strip()
                if "ERROR" in line:
                    color = "#f87171"  # Red
                    icon = "❌"
                elif "WARNING" in line:
                    color = "#fbbf24"  # Yellow
                    icon = "⚠️"
                elif "INFO" in line:
                    color = "#60a5fa"  # Blue
                    icon = "ℹ️"
                else:
                    color = "#cbd5e1"  # Gray
                    icon = "📝"
                
                log_display += f"""
                <div style='background: rgba(139, 92, 246, 0.05); padding: 0.75rem; border-radius: 8px; margin-bottom: 0.5rem; border-left: 3px solid {color}; font-family: monospace; font-size: 0.85rem;'>
                    <span style='color: {color};'>{icon}</span> <span style='color: #cbd5e1;'>{line}</span>
                </div>
                """
            
            st.markdown(log_display, unsafe_allow_html=True)
            
            # Download logs button
            st.markdown("---")
            log_text = "".join(log_content)
            st.download_button(
                label="📥 Download Full Logs",
                data=log_text,
                file_name=f"aerofit_logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain",
                help="Download complete log file"
            )
        else:
            st.info("No logs match the current filter criteria.")
    
    except FileNotFoundError:
        st.warning("📝 No log file found yet. Logs will be created as you interact with the application.")
        logger.info("Log file not found - creating new log")
    
    # Add some helpful information
    with st.expander("ℹ️ About Logs"):
        st.markdown("""
        ### Log Levels
        - **INFO** 📘: Normal application operations and events
        - **WARNING** ⚠️: Unexpected situations that don't prevent operation
        - **ERROR** ❌: Serious problems that need attention
        
        ### What's Logged?
        - Application startup and shutdown
        - Data loading and preprocessing
        - User interactions with tabs and features
        - Filter applications and data queries
        - Any errors or exceptions
        
        ### Log File Location
        The log file is stored as `app.log` in the application directory.
        """)

st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem 0; color: #94a3b8;'>
    <p style='font-size: 0.9rem;'>Built with ❤️ using Streamlit & Plotly | © 2025 Ratnesh Analytics</p>
</div>
""", unsafe_allow_html=True)

logger.info("Application render completed successfully")

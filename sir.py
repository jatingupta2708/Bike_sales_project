
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
st.set_page_config(page_title='bike_sales_india.csv',layout='wide')
# st.title('Covid 19')
df = pd.read_csv('bike_sales_india.csv')
# st.dataframe(df)
with st.sidebar:
    opt = option_menu('Menu',['Home','Dataset','Pre-Processing','Visualization','About'],icons=["house", "table", "gear", "bar-chart", "person"])
    c= st.multiselect('Select Continent',options=df['Continent'].unique())

if c :
    filtered = df[df['Continent'].isin(c)]
else:
    filtered= df



if opt=='Home':
    st.title('🏠 Covid-19 Dashboard')
    st.markdown("### Welcome! Explore global COVID‑19 data with interactive charts.")
    total_countries = filtered['Country/Region'].nunique()
    total_cases= filtered['TotalCases'].sum()
    total_deaths= filtered['TotalDeaths'].sum()
    total_recovered= filtered['TotalRecovered'].sum()
    avg_cases= total_cases/total_countries if total_cases else 0













    st.markdown("""
    <style>
    .kpi-card {
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        padding: 16px 10px;
        background-color: #ffffff;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        text-align: center;
        transition: transform 0.1s;
        margin: 6px 0;
    }
    .kpi-card:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 16px rgba(0,0,0,0.1);
    }
    .kpi-label {
        font-size: 1rem;
        color: #6c757d;
        font-weight: 500;
        letter-spacing: 0.5px;
    }
    .kpi-value {
        font-size: 2rem;
        font-weight: 700;
        color: #1f2937;
        line-height: 1.2;
        margin-top: 4px;
    }
    .kpi-delta {
        font-size: 0.9rem;
        color: #28a745;
        margin-top: 2px;
    }
    </style>
    """, unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">🌍 Countries</div>
            <div class="kpi-value">{total_countries:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">📈 Total Cases</div>
            <div class="kpi-value">{total_cases:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">💀 Total Deaths</div>
            <div class="kpi-value">{total_deaths:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">❤️‍🩹 Recovered</div>
            <div class="kpi-value">{total_recovered:.0f}</div>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">📊 Avg Cases / Country</div>
            <div class="kpi-value">{avg_cases:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)

elif opt=='Dataset':
    st.title('📊 Dataset Explorer')
    # st.write(filtered.shape)
    rows = filtered.shape[0]
    cols = filtered.shape[1]
    st.markdown("""
    <style>
    .dataset-info {
        background-color: #f8f9fa;
        padding: 12px 16px;
        border-radius: 10px;
        border-left: 4px solid #2c7be5;
        margin-bottom: 20px;
        display: flex;
        gap: 24px;
        flex-wrap: wrap;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .dataset-info-item {
        font-size: 0.95rem;
        color: #1f2937;
    }
    .dataset-info-item strong {
        color: #2c7be5;
        font-weight: 600;
    }
    .stDataFrame {
        border-radius: 12px !important;
        overflow: hidden !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class='dataset-info'>
            <span class ="dataset-info-item"> <strong>Rows: </strong>{rows}</span>        
            <span class ="dataset-info-item"> <strong>Columns: </strong>{cols}</span>        
            <span class ="dataset-info-item"> <strong>Continents: </strong>{filtered['Continent'].nunique()}</span>        
            <span class ="dataset-info-item"> <strong>Countries: </strong>{filtered['Country/Region'].nunique()}</span>              
""",unsafe_allow_html=True)


    t1,t2,t3 = st.tabs(['Dataset','Null Values','Summary'])
    with t1:
        # code
        pass
    with t2:
        # code
        pass
    with t3:
        # code
        pass
Displaying s4.py.
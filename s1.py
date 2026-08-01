import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import numpy as np
import plotly.express as px


st.set_page_config(
    page_title='Moto Vision India',
    page_icon='🏍️',
    layout='wide',
)


df= pd.read_csv('../bike_sales_india.csv')


with st.sidebar:
    st.image('../bike logo 2 BackgroundRemover.png.png')
    with st.sidebar:
        st.markdown('### Menu')

        opt= option_menu(
            menu_title=None,
            options=['Dashboard','Data Overview','Brand Analysis','Model Analysis','Price Analysis','Resale Analysis','Fuel & Ownership','State Analysis','Advanced Analytics','About Project'],
             icons=[
        "house",
        "bar-chart",
        "building",
        "cpu",
        "currency-dollar",
        "graph-up",
        "fuel-pump",
        "geo-alt",
        "pie-chart",
        "info-circle"
    ],
        )

    

if opt=='Dashboard':
    c= st.multiselect('Select Brand',options=df['Brand'].unique())
    if c :
        filtered = df[df['Brand'].isin(c)]
    else:
        filtered= df

    
    col_text,col_image= st.columns([5,2])

    with col_text:
        st.title("Bike Sales Analytics")

    with col_image:
        st.image('../bike logo 2.png')

    st.markdown("""
    <style>

    /* Main Background */
    .stApp{
        background: linear-gradient(135deg,#050816,#13133d,#30145b);
    }

    /* Sidebar */
    [data-testid="stSidebar"]{
        background:#0f172a;
        border-right:1px solid rgba(255,255,255,0.08);
    }

    /* Heading */
    .main-title{
        font-size:48px;
        font-weight:800;
        color:white;
        margin-bottom:0px;
    }

    .sub-title{
        color:#cbd5e1;
        font-size:18px;
        margin-bottom:35px;
    }

    /* KPI Cards */

    .kpi-card{
        background:rgba(255,255,255,0.06);
        padding:20px;
        border-radius:18px;
        border:1px solid rgba(255,255,255,0.08);
        backdrop-filter: blur(12px);
        transition:0.4s;
    }

    .kpi-card:hover{
        transform:translateY(-6px);
        box-shadow:0px 0px 25px rgba(147,51,234,.45);
    }

    .kpi-title{
        color:#94a3b8;
        font-size:15px;
        font-weight:600;
    }

    .kpi-value{
        font-size:34px;
        font-weight:bold;
        color:white;
    }

    .kpi-footer{
        color:#22c55e;
        font-size:13px;
    }

    /* Dropdown */

    .stSelectbox div[data-baseweb="select"]{
        border-radius:12px;
    }

    /* Metric */

    div[data-testid="metric-container"]{
        background:rgba(255,255,255,.05);
        border-radius:18px;
        border:1px solid rgba(255,255,255,.07);
        padding:20px;
    }

    /* Table */

    thead tr th{
        background:#1e293b !important;
        color:white !important;
    }

    tbody{
        color:white;
    }

    /* Scrollbar */

    ::-webkit-scrollbar{
    width:10px;
    }

    ::-webkit-scrollbar-thumb{
    background:#7c3aed;
    border-radius:20px;
    }

    </style>
    """,unsafe_allow_html=True)









    st.title('Bike Sales Analysis')
    st.markdown("### Interactive Used Bike Sales Analysis Dashboard.")
    total_bikes = len(filtered)
    Average_price= filtered['Price (INR)'].mean()
    Average_resale_price= filtered['Resale Price (INR)'].mean()
    Average_mileage= filtered['Mileage (km/l)'].mean()






    st.markdown("""
    <style>

    .kpi-box {
        display: flex;
        gap: 20px;
        width: 100%;
    }

    .card {
        flex: 1;
        padding: 25px;
        border-radius: 22px;
        color: white;
        text-align: center;
        transition: all 0.4s ease;
        cursor: pointer;
        box-shadow: 0 0 25px rgba(255,255,255,0.15);
    }

    /* Blur all cards when container is active */
    .kpi-box:hover .card {
        filter: blur(4px);
        opacity: 0.55;
    }

    /* Highlight selected card */
    .kpi-box .card:hover {
        filter: blur(0px);
        opacity: 1;
        transform: translateY(-12px) scale(1.08);
        box-shadow: 
            0 0 25px rgba(255,255,255,0.5),
            0 0 50px rgba(0,255,255,0.4);
    }


    .blue {
        background: linear-gradient(135deg,#2563eb,#06b6d4);
    }

    .green {
        background: linear-gradient(135deg,#059669,#34d399);
    }

    .orange {
        background: linear-gradient(135deg,#ea580c,#fbbf24);
    }

    .purple {
        background: linear-gradient(135deg,#7c3aed,#ec4899);
    }


    .icon {
        font-size:35px;
    }

    .title {
        font-size:16px;
        margin-top:10px;
    }

    .value {
        font-size:30px;
        font-weight:800;
    }

    </style>


    """, unsafe_allow_html=True)






    # Custom CSS Inject
    st.markdown(
        """
        <style>
        /* Metric Card Styling */
        .kpi-card {
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #334155;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            text-align: center;
            color: white;
        }
        .kpi-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.3);
            border-color: #3b82f6;
        }
        .kpi-title {
            font-size: 0.9rem;
            color: #94a3b8;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 8px;
        }
        .kpi-value {
            font-size: 1.8rem;
            font-weight: 700;
            color: #f8fafc;
        }
        .kpi-subtitle {
            font-size: 0.8rem;
            color: #10b981;
            margin-top: 4px;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(f"""
    <div class="kpi-box">

    <div class="card blue">
        <div class="icon">🏍️</div>
        <div class="title">Total Bikes</div>
        <div class="value">{total_bikes:,}</div>
    </div>

    <div class="card green">
        <div class="icon">💰</div>
        <div class="title">Average Price</div>
        <div class="value">₹{Average_price:,.0f}</div>
    </div>

    <div class="card orange">
        <div class="icon">💵</div>
        <div class="title">Average Resale Price</div>
        <div class="value">₹{Average_resale_price:,.0f}</div>
    </div>

    <div class="card purple">
        <div class="icon">⛽</div>
        <div class="title">Average Mileage</div>
        <div class="value">{Average_mileage:.1f} km/l</div>
    </div>

    </div>
    """, unsafe_allow_html=True)

    

    st.markdown("""
    <style>
    .stApp {
        background:
        radial-gradient(circle at top left,#1e3a8a,transparent 35%),
        radial-gradient(circle at bottom right,#7c3aed,transparent 35%),
        #020617;
    }
    </style>
    """, unsafe_allow_html=True)




    #2nd kpi card of highest price or highest resale
    highest_price_brand = (
        df.groupby("Brand")["Price (INR)"]
        .mean()
        .idxmax()
    )


    highest_resale_brand = (
        df.groupby("Brand")["Resale Price (INR)"]
        .mean()
        .idxmax()
    )



    best_mileage_brand = (
        df.groupby("Brand")["Mileage (km/l)"]
        .mean()
        .idxmax()
    )



    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.markdown(f"""
        <div class="tag-card">
            <div class="tag-title">🏆 Highest Price Brand</div>
            <div class="tag-value">{highest_price_brand}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="tag-card">
            <div class="tag-title">💰 Highest Resale Brand</div>
            <div class="tag-value">{highest_resale_brand}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="tag-card">
            <div class="tag-title">⛽ Best Mileage Brand</div>
            <div class="tag-value">{best_mileage_brand}</div>
        </div>
        """, unsafe_allow_html=True)


    st.markdown("""
    <style>

    .tag-card{
        background:#1e293b;
        border-radius:15px;
        padding:18px;
        text-align:center;
        border:1px solid #334155;
        height:120px;
        transition:0.3s;
    }

    .tag-card:hover{
        border:1px solid #8b5cf6;
        transform:translateY(-4px);
        box-shadow:0px 8px 20px rgba(139,92,246,.35);
    }

    .tag-title{
        color:#94a3b8;
        font-size:15px;
        font-weight:600;
        margin-bottom:10px;
    }

    .tag-value{
        color:white;
        font-size:26px;
        font-weight:700;
    }

    </style>
    """, unsafe_allow_html=True
    )





    col_1,col_2= st.columns(2)

    with col_1:

        top_brands = (
            filtered["Brand"]
            .value_counts()
            .head(10)
            .reset_index()
        )

    top_brands.columns = ["Brand", "Count"]

    fig = px.bar(
            top_brands,
            x="Brand",
            y="Count",
            color="Count",
            title="Top 8 Brands",
            text="Count",
            color_continuous_scale="Blues"
        )

    fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            title_x=0.5,
            showlegend=False,
            height=420,
        
        )
    title={
                    'text': "<b><span style='color:#FFFF00 ;'>Top 8 Brands</span></b>",
                    'x': 0.5,
                    'xanchor': 'center',
                    'font': dict(size=30, family='Arial Black')
                },
        

    st.plotly_chart(fig, use_container_width=True)



    with col_2:

        fuel = filtered["Fuel Type"].value_counts().reset_index()
        fuel.columns = ["Fuel Type", "Count"]

    fig = px.pie(
            fuel,
            names="Fuel Type",
            values="Count",
            hole=0.5,
            title="Fuel Type Distribution"
        )
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        title_x=0.5,
        margin=dict(l=20, r=20, t=60, b=20),
        height=420
        )

    st.plotly_chart(fig, use_container_width=True)




elif opt=='Data Overview':
    st.title('Overview')


    # [ Price Distribution ]        [ Price vs Resale ]

    # --------------------------------------------------------

    # Latest Dataset

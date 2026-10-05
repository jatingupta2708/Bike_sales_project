import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import numpy as np
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title='Moto Vision India',
    page_icon='🏍️',
    layout='wide',
)


df= pd.read_csv('bike_sales_india.csv')


with st.sidebar:
    st.image("new logo-Picsart-BackgroundRemover.PNG", width=1200)
    st.markdown("---")
    st.caption("Developed by Jatin Gupta")
    st.markdown("### Menu")

    opt= option_menu(
            menu_title=None,
            options=['Dashboard','Data Overview','Brand Analysis','Model Analysis','Price Analysis','Resale Analysis','State Analysis','About Project'],
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

    
if opt == 'Dashboard':
    # ---------------------------------------------------------
    # 1. Glossy & Glassmorphism CSS Styling
    # ---------------------------------------------------------
    st.markdown("""
        <style>
        /* Modern Obsidian Glossy Background */
        .stApp {
            background: radial-gradient(circle at 20% 20%, #1e1b4b 0%, #0f172a 50%, #030712 100%);
            color: #f8fafc;
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
        }

        /* Sidebar Glass Effect */
        [data-testid="stSidebar"] {
            background: rgba(15, 23, 42, 0.6) !important;
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-right: 1px solid rgba(255, 255, 255, 0.08);
        }

        /* ==================== GLOSSY GLASS KPI CARDS ==================== */
        .kpi-card-glossy {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-radius: 20px;
            padding: 22px 24px;
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.15);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        /* Glass Surface Reflection (Gloss Effect) */
        .kpi-card-glossy::before {
            content: '';
            position: absolute;
            top: 0;
            left: -50%;
            width: 200%;
            height: 50%;
            background: linear-gradient(
                180deg, 
                rgba(255, 255, 255, 0.15) 0%, 
                rgba(255, 255, 255, 0) 100%
            );
            transform: rotate(-10deg);
            pointer-events: none;
        }

        /* Glossy Card Variants with Soft Neon Tint */
        .card-blue {
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.12) 0%, rgba(15, 23, 42, 0.6) 100%);
            border-color: rgba(96, 165, 250, 0.3);
        }
        .card-green {
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.12) 0%, rgba(15, 23, 42, 0.6) 100%);
            border-color: rgba(52, 211, 153, 0.3);
        }
        .card-amber {
            background: linear-gradient(135deg, rgba(245, 158, 11, 0.12) 0%, rgba(15, 23, 42, 0.6) 100%);
            border-color: rgba(251, 191, 36, 0.3);
        }
        .card-purple {
            background: linear-gradient(135deg, rgba(139, 92, 246, 0.12) 0%, rgba(15, 23, 42, 0.6) 100%);
            border-color: rgba(192, 132, 252, 0.3);
        }

        /* Hover Lift & Dynamic Glow Effect */
        .card-blue:hover {
            transform: translateY(-8px);
            border-color: rgba(96, 165, 250, 0.6);
            box-shadow: 0 12px 30px rgba(59, 130, 246, 0.3);
        }
        .card-green:hover {
            transform: translateY(-8px);
            border-color: rgba(52, 211, 153, 0.6);
            box-shadow: 0 12px 30px rgba(16, 185, 129, 0.3);
        }
        .card-amber:hover {
            transform: translateY(-8px);
            border-color: rgba(251, 191, 36, 0.6);
            box-shadow: 0 12px 30px rgba(245, 158, 11, 0.3);
        }
        .card-purple:hover {
            transform: translateY(-8px);
            border-color: rgba(192, 132, 252, 0.6);
            box-shadow: 0 12px 30px rgba(139, 92, 246, 0.3);
        }

        .kpi-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: #cbd5e1;
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .kpi-number {
            font-size: 30px;
            font-weight: 800;
            color: #ffffff;
            margin-top: 10px;
            letter-spacing: -0.5px;
            text-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
        }

        /* Glossy Highlight Cards */
        .tag-card-glossy {
            background: rgba(30, 41, 59, 0.3);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-radius: 16px;
            padding: 16px;
            text-align: center;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
        }

        .tag-card-glossy:hover {
            border-color: rgba(168, 85, 247, 0.5);
            transform: translateY(-4px);
            box-shadow: 0 8px 25px rgba(168, 85, 247, 0.25);
            background: rgba(30, 41, 59, 0.5);
        }

        .tag-title-glossy {
            color: #94a3b8;
            font-size: 12px;
            font-weight: 600;
            margin-bottom: 6px;
            text-transform: uppercase;
        }

        .tag-value-glossy {
            color: #c084fc;
            font-size: 20px;
            font-weight: 700;
        }
        </style>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # 2. Header Section
    # ---------------------------------------------------------
    col_text, col_image = st.columns([5, 2])

    with col_text:
        st.title("🏍️ MOTO VISION INDIA")
        st.markdown("<p style='color:#94a3b8; font-size:18px;'>Smart Analytics & Market Intelligence for Indian Two-Wheelers</p>", unsafe_allow_html=True)

    with col_image:
        st.image('The journey is the.jpg', use_container_width=True)

    st.markdown("<hr style='border:0; height:1px; background:linear-gradient(90deg, #38bdf8, #a855f7, #ec4899); margin:20px 0;'>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    
    st.markdown("### 📊 Market Overview")
    c = st.multiselect('Select Brand Filter', options=df['Brand'].unique())
    
    filtered = df[df['Brand'].isin(c)] if c else df

    total_bikes = len(filtered)
    Average_price = filtered['Price (INR)'].mean() 
    Average_resale_price = filtered['Resale Price (INR)'].mean()
    Average_mileage = filtered['Mileage (km/l)'].mean() 

    # ---------------------------------------------------------
    # 4.  KPI Cards
    # ---------------------------------------------------------
    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.markdown(f"""
            <div class="kpi-card-glossy card-blue">
                <div class="kpi-header"><span>Total Inventory</span> <span style="font-size:18px;">🏍️</span></div>
                <div class="kpi-number">{total_bikes:,}</div>
            </div>
        """, unsafe_allow_html=True)

    with k2:
        st.markdown(f"""
            <div class="kpi-card-glossy card-green">
                <div class="kpi-header"><span>Average Price</span> <span style="font-size:18px;">💰</span></div>
                <div class="kpi-number">₹{Average_price:,.0f}</div>
            </div>
        """, unsafe_allow_html=True)

    with k3:
        st.markdown(f"""
            <div class="kpi-card-glossy card-amber">
                <div class="kpi-header"><span>Avg Resale Value</span> <span style="font-size:18px;">💵</span></div>
                <div class="kpi-number">₹{Average_resale_price:,.0f}</div>
            </div>
        """, unsafe_allow_html=True)

    with k4:
        st.markdown(f"""
            <div class="kpi-card-glossy card-purple">
                <div class="kpi-header"><span>Avg Mileage</span> <span style="font-size:18px;">⛽</span></div>
                <div class="kpi-number">{Average_mileage:.1f} <span style="font-size:16px; color:#cbd5e1;">km/l</span></div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # 5. Highlight Glossy Cards Row
    # ---------------------------------------------------------
    highest_price_brand = df.groupby("Brand")["Price (INR)"].mean().idxmax() if not df.empty else "N/A"
    highest_resale_brand = df.groupby("Brand")["Resale Price (INR)"].mean().idxmax() if not df.empty else "N/A"
    best_mileage_brand = df.groupby("Brand")["Mileage (km/l)"].mean().idxmax() if not df.empty else "N/A"

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
            <div class="tag-card-glossy">
                <div class="tag-title-glossy">🏆 Most Premium Brand</div>
                <div class="tag-value-glossy">{highest_price_brand}</div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div class="tag-card-glossy">
                <div class="tag-title-glossy">💎 Highest Resale Brand</div>
                <div class="tag-value-glossy">{highest_resale_brand}</div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
            <div class="tag-card-glossy">
                <div class="tag-title-glossy">⛽ Best Mileage Brand</div>
                <div class="tag-value-glossy">{best_mileage_brand}</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # 6. Balanced Plotly Charts
    # ---------------------------------------------------------
    custom_palette = ["#38bdf8", "#34d399", "#c084fc", "#f43f5e", "#fbbf24", "#22d3ee", "#818cf8", "#f472b6"]

    col_1, col_2 = st.columns(2)

    with col_1:
        top_brands = filtered["Brand"].value_counts().head(8).reset_index()
        top_brands.columns = ["Brand", "Count"]

        fig_bar = px.bar(
            top_brands, x="Brand", y="Count", color="Brand",
            title="<b>Top 8 Bike Brands by Count</b>", text="Count",
            color_discrete_sequence=custom_palette
        )
        fig_bar.update_layout(
            template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)", title_x=0.5, showlegend=False, height=380
        )
        st.plotly_chart(fig_bar, use_container_width=True, key="dashboard_top_brands")

    with col_2:
        fuel = filtered["Fuel Type"].value_counts().reset_index()
        fuel.columns = ["Fuel Type", "Count"]

        fig_pie = px.pie(
            fuel, names="Fuel Type", values="Count", hole=0.5,
            title="<b>Fuel Type Distribution</b>",
            color_discrete_sequence=["#38bdf8", "#34d399", "#c084fc", "#fbbf24"]
        )
        fig_pie.update_layout(
            template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)", title_x=0.5, height=380
        )
        st.plotly_chart(fig_pie, use_container_width=True, key="dashboard_fuel_dist")

    col_3, col_4 = st.columns(2)

    with col_3:
        fig_hist = px.histogram(
            filtered, x='Price (INR)', nbins=25,
            title='<b>Market Price Distribution</b>',
            color_discrete_sequence=["#818cf8"]
        )
        fig_hist.update_traces(
            marker_line_color='rgba(255, 255, 255, 0.6)',
            marker_line_width=1.2
        )
        fig_hist.update_layout(
            template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)", title_x=0.5, height=380
        )
        st.plotly_chart(fig_hist, use_container_width=True, key="dashboard_price_hist")

    with col_4:
        fig_scatter = px.scatter(
            filtered, 
            x="Mileage (km/l)", 
            y="Price (INR)", 
            color="Brand",
            title="<b>Price vs Mileage Correlation (Grouped by Brand)</b>",
            hover_data=["Model"],
            color_discrete_sequence=custom_palette
        )
        fig_scatter.update_traces(marker=dict(size=9, opacity=0.85, line=dict(width=1, color='white')))
        fig_scatter.update_layout(
            template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)", title_x=0.5, height=380
        )
        st.plotly_chart(fig_scatter, use_container_width=True, key="dashboard_price_mileage")


# #..................................................................................................




































elif opt == 'Data Overview':

    rows = df.shape[0]
    cols = df.shape[1]

    # ============================================================
    # DATA OVERVIEW CSS
    # ============================================================

    st.markdown(
        """
        <style>

        /* =========================
           MAIN BACKGROUND
        ========================= */

        [data-testid="stAppViewContainer"] {
            background: radial-gradient(
                circle at top,
                #172033 0%,
                #0f172a 45%,
                #020617 100%
            ) !important;
        }

        [data-testid="stHeader"] {
            background: transparent !important;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1400px;
        }

        h1, h2, h3 {
            color: #f8fafc !important;
            font-weight: 700 !important;
        }

        /* =========================
           HEADER
        ========================= */

        .overview-header {
            background: linear-gradient(
                135deg,
                rgba(16, 185, 129, 0.20),
                rgba(6, 182, 212, 0.14)
            );

            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 18px;
            padding: 24px 28px;
            margin-bottom: 22px;

            box-shadow:
                0 10px 30px rgba(0, 0, 0, 0.40),
                inset 0 1px 1px rgba(255, 255, 255, 0.15);
        }

        .overview-header h1 {
            margin: 0;
            color: #ffffff;
            font-size: 2.2rem;
            font-weight: 800;
        }

        .overview-header p {
            margin-top: 7px;
            margin-bottom: 0;
            color: #cbd5e1;
            font-size: 0.95rem;
        }

        /* =========================
           DATASET CARDS
        ========================= */

        .dataset-info {
            display: flex;
            gap: 16px;
            flex-wrap: wrap;
            margin-bottom: 26px;
        }

        .dataset-info-item {
            flex: 1;
            min-width: 180px;

            background: linear-gradient(
                145deg,
                rgba(30, 41, 59, 0.95),
                rgba(15, 23, 42, 0.95)
            );

            border: 1px solid rgba(255, 255, 255, 0.10);
            border-radius: 16px;

            padding: 18px;
            text-align: center;

            color: #f8fafc;

            box-shadow:
                0 8px 24px rgba(0, 0, 0, 0.35),
                inset 0 1px 1px rgba(255, 255, 255, 0.05);

            transition: 0.25s ease;
        }

        .dataset-info-item:hover {
            transform: translateY(-4px);

            border-color: rgba(16, 185, 129, 0.35);

            box-shadow:
                0 12px 28px rgba(0, 0, 0, 0.45),
                0 0 18px rgba(16, 185, 129, 0.18);
        }

        .dataset-info-item strong {
            display: block;
            color: #10b981;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            margin-bottom: 8px;
        }

        /* =========================
           TABS
        ========================= */

        button[data-baseweb="tab"] {
            color: #cbd5e1 !important;
            background: rgba(30, 41, 59, 0.75) !important;

            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-radius: 10px !important;

            padding: 9px 16px !important;
            margin-right: 6px;

            font-weight: 600 !important;
        }

        button[data-baseweb="tab"]:hover {
            color: #ffffff !important;
            background: rgba(16, 185, 129, 0.18) !important;
        }

        button[aria-selected="true"] {
            background: #10b981 !important;
            color: #ffffff !important;
            border-color: #10b981 !important;

            box-shadow:
                0 6px 18px rgba(16, 185, 129, 0.25);
        }

        /* =========================
           DATAFRAME
        ========================= */

        div[data-testid="stDataFrame"] {
            border-radius: 14px !important;
            overflow: hidden !important;

            border: 1px solid rgba(255, 255, 255, 0.08) !important;

            box-shadow:
                0 8px 22px rgba(0, 0, 0, 0.30);
        }

        /* =========================
           SLIDER
        ========================= */

        div[data-testid="stSlider"] {
            padding-top: 8px;
            padding-bottom: 4px;
        }

        /* =========================
           DOWNLOAD BUTTON
        ========================= */

        .stDownloadButton button {
            width: 100%;

            background: linear-gradient(
                135deg,
                #10b981,
                #06b6d4
            ) !important;

            color: #ffffff !important;

            border: none !important;
            border-radius: 10px !important;

            font-weight: 700 !important;

            transition: 0.25s ease;
        }

        .stDownloadButton button:hover {
            transform: translateY(-2px);

            box-shadow:
                0 8px 20px rgba(16, 185, 129, 0.28);
        }

        /* =========================
           EXPANDER
        ========================= */

        details {
            background: rgba(30, 41, 59, 0.85) !important;

            border: 1px solid rgba(255, 255, 255, 0.08) !important;

            border-radius: 12px !important;

            box-shadow:
                0 6px 18px rgba(0, 0, 0, 0.20);
        }

        details summary {
            color: #f8fafc !important;
            font-weight: 600 !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # ============================================================
    # HEADER
    # ============================================================

    st.markdown(
        """
<div class="overview-header">
    <h1>📊 Dataset Overview</h1>
    <p>
        Explore, inspect and understand the Bike Sales India dataset.
    </p>
</div>
        """,
        unsafe_allow_html=True,
    )

    # ============================================================
    # DATASET INFORMATION CARDS
    # ============================================================

    st.markdown(
f"""
<div class="dataset-info">
    <div class="dataset-info-item">
        <strong>Rows</strong>
        {rows}
    </div>

    <div class="dataset-info-item">
        <strong>Columns</strong>
        {cols}
    </div>

    <div class="dataset-info-item">
        <strong>Brands</strong>
        {df['Brand'].nunique()}
    </div>

    <div class="dataset-info-item">
        <strong>Models</strong>
        {df['Model'].nunique()}
    </div>
</div>
""",
        unsafe_allow_html=True
    )

    # ============================================================
    # TABS
    # ============================================================

    tab1, tab2, tab3 = st.tabs(
        [
            "📄 Data Preview",
            "🔍 Column Details",
            "📈 Summary"
        ]
    )

    # ============================================================
    # TAB 1 - DATA PREVIEW
    # ============================================================

    with tab1:

        col_left, col_right = st.columns([3, 1])

        with col_left:
            st.subheader("Preview Filtered Data")

        with col_right:
            n_rows = st.slider(
                "Rows to show",
                min_value=10,
                max_value=200,
                value=20,
                step=10
            )

        st.dataframe(
            df.head(n_rows),
            use_container_width=True
        )

        with st.expander("Show last rows"):

            st.dataframe(
                df.tail(10),
                use_container_width=True
            )

        # Download button
        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download filtered data as CSV",
            data=csv,
            file_name="bike_sales_india.csv",
            mime="text/csv",
            use_container_width=True,
        )

    # ============================================================
    # TAB 2 - COLUMN DETAILS
    # ============================================================

    with tab2:

        missing_df = (
            df.isna()
            .sum()
            .reset_index(name="Missing Count")
        )

        missing_df.rename(
            columns={
                "index": "Column Name"
            },
            inplace=True
        )

        st.dataframe(
            missing_df,
            use_container_width=True,
            height=400
        )

        dtype_df = pd.DataFrame(
            {
                "Column": df.columns,
                "Data Type": df.dtypes.astype(str)
            }
        )

        st.dataframe(
            dtype_df,
            use_container_width=True
        )

    # ============================================================
    # TAB 3 - SUMMARY
    # ============================================================

    with tab3:

        st.subheader("Statistical Summary")

        # Numeric columns
        num_cols = df.select_dtypes(
            include=["int64", "float64"]
        ).columns.tolist()

        # Categorical columns
        cat_cols = df.select_dtypes(
            include=["object", "category"]
        ).columns.tolist()

        if num_cols:

            st.markdown("#### 📊 Numeric Columns")

            st.dataframe(
                df[num_cols].describe(),
                use_container_width=True
            )

        if cat_cols:

            st.markdown("#### 🏷️ Categorical Columns")

            for col in cat_cols[:4]:

                with st.expander(
                    f"Top values in '{col}'"
                ):

                    st.dataframe(
                        df[col]
                        .value_counts()
                        .reset_index()
                        .head(10),
                        use_container_width=True,
                        hide_index=True
                    )

        if len(cat_cols) > 4:

            st.info(
                f"Showing top 4 categorical columns. "
                f"There are {len(cat_cols)} in total."
            )




# elif opt=='Data Overview':

#     rows = df.shape[0]
#     cols = df.shape[1]

#     st.markdown("""
#     <div style="
#     background:linear-gradient(135deg,#2563EB,#1E3A8A);
#     padding:25px;
#     border-radius:18px;
#     box-shadow:0 8px 25px rgba(37,99,235,.3);
#     margin-bottom:20px;">

#     <h1 style="color:white;margin:0;">
#     📊 Dataset Overview
#     </h1>

#     <p style="color:#E2E8F0;margin-top:8px;">
#     Explore, inspect and understand the Bike Sales India dataset.
#     </p>

#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("""
#     <style>
#     .stApp {
#         background:
#         radial-gradient(circle at top left,#1e3a8a,transparent 35%),
#         radial-gradient(circle at bottom right,#7c3aed,transparent 35%),
#         #020617;
#     }
#     </style>
#     """, unsafe_allow_html=True)



# #========================================
# #  KPI CARDS
# #======================================
#     st.markdown("""
#         <style>

#         /* ==============================
#         Global Theme
#         ============================== */

#         .stApp{
#             background: linear-gradient(180deg, #0b1220 0%, #111827 100%);
#         }

#         h1, h2, h3{
#             color: #ffffff;
#             font-family: "Inter", sans-serif;
#             font-weight: 700;
#             letter-spacing: -0.3px;
#         }

#         /* ==============================
#         Dataset Info Cards
#         ============================== */

#         .dataset-info{
#             display:flex;
#             gap:18px;
#             flex-wrap:wrap;
#             margin-bottom:28px;
#         }

#         .dataset-info-item{
#             flex:1;
#             min-width:180px;
#             background: linear-gradient(145deg, #1e293b 0%, #0f172a 100%);
#             padding:22px 18px;
#             border-radius:18px;
#             color:#ffffff;
#             text-align:center;
#             border:1px solid rgba(255,255,255,0.08);
#             box-shadow:
#                 0 10px 25px rgba(0,0,0,0.35),
#                 inset 0 1px 0 rgba(255,255,255,0.04);
#             transition: all .35s ease;
#             font-size:16px;
#             font-weight:500;
#             position:relative;
#             overflow:hidden;
#             backdrop-filter: blur(6px);
#         }

#         .dataset-info-item::before{
#             content:"";
#             position:absolute;
#             top:0;
#             left:-120%;
#             width:100%;
#             height:100%;
#             background: linear-gradient(
#                 120deg,
#                 transparent,
#                 rgba(255,255,255,0.08),
#                 transparent
#             );
#             transition: left .6s ease;
#         }

#         .dataset-info-item:hover::before{
#             left:120%;
#         }

#         .dataset-info-item:hover{
#             transform: translateY(-6px);
#             border-color: rgba(255,255,0,0.35);
#             box-shadow:
#                 0 18px 35px rgba(0,0,0,0.45),
#                 0 0 20px rgba(255,255,0,0.08);
#         }

#         .dataset-info-item strong{
#             display:block;
#             color:#FFFF00;
#             font-size:14px;
#             text-transform: uppercase;
#             letter-spacing: .8px;
#             margin-bottom:10px;
#             opacity: .95;
#         }

#         /* ==============================
#         Dataframe
#         ============================== */

#         div[data-testid="stDataFrame"]{
#             border-radius:20px !important;
#             overflow:hidden !important;
#             border:1px solid rgba(255,255,255,.08);
#             box-shadow:
#                 0 10px 28px rgba(0,0,0,.35),
#                 inset 0 1px 0 rgba(255,255,255,.03);
#             background:#111827;
#         }

#         /* ==============================
#         Tabs
#         ============================== */

#         button[data-baseweb="tab"]{
#             background: rgba(30,41,59,0.9);
#             color: #e5e7eb;
#             border: 1px solid rgba(255,255,255,0.06);
#             border-radius:12px;
#             margin-right:8px;
#             padding:10px 18px;
#             font-weight:600;
#             transition: all .3s ease;
#             box-shadow: 0 2px 8px rgba(0,0,0,.18);
#         }

#         button[data-baseweb="tab"]:hover{
#             background:#2563eb;
#             color:#ffffff;
#             transform: translateY(-2px);
#             box-shadow: 0 8px 18px rgba(37,99,235,.35);
#         }

#         /* Active Tab */

#         button[aria-selected="true"]{
#             background:#2563eb !important;
#             color:#ffffff !important;
#             border-color:#3b82f6 !important;
#             box-shadow: 0 10px 22px rgba(37,99,235,.38);
#         }

#         /* ==============================
#         Slider
#         ============================== */

#         div[data-testid="stSlider"]{
#             padding-top:12px;
#             padding-bottom:4px;
#         }

#         /* ==============================
#         Download Button
#         ============================== */

#         .stDownloadButton button{
#             width:100%;
#             background: linear-gradient(135deg, #2563eb, #1d4ed8);
#             color:#ffffff;
#             border:none;
#             border-radius:12px;
#             font-weight:700;
#             padding:0.65rem 1rem;
#             transition: all .3s ease;
#             box-shadow: 0 10px 22px rgba(37,99,235,.28);
#         }

#         .stDownloadButton button:hover{
#             background: linear-gradient(135deg, #1d4ed8, #1e40af);
#             transform: translateY(-2px);
#             box-shadow: 0 14px 26px rgba(37,99,235,.36);
#         }

#         /* ==============================
#         Expander
#         ============================== */

#         details{
#             background: rgba(30,41,59,0.92);
#             border-radius:14px;
#             border:1px solid rgba(255,255,255,.08);
#             padding:10px 12px;
#             box-shadow:
#                 0 6px 18px rgba(0,0,0,.22),
#                 inset 0 1px 0 rgba(255,255,255,.03);
#         }

#         details summary{
#             color:#ffffff;
#             font-weight:600;
#             cursor:pointer;
#         }

#         /* ==============================
#         Extra Polishing
#         ============================== */

#         .block-container{
#             padding-top: 2rem;
#             padding-bottom: 2rem;
#         }

#         section[data-testid="stSidebar"]{
#             background: #0f172a;
#             border-right: 1px solid rgba(255,255,255,.06);
#         }

#         </style>
#     """, unsafe_allow_html=True)





#     st.markdown(f"""
#     <div class='dataset-info'>
#         <span class="dataset-info-item"><strong>Rows:</strong> {rows}</span>
#         <span class="dataset-info-item"><strong>Columns:</strong> {cols}</span>
#         <span class="dataset-info-item"><strong>Brands:</strong> {df['Brand'].nunique()}</span>
#         <span class="dataset-info-item"><strong>Models:</strong> {df['Model'].nunique()}</span>
#     </div>
#     """, unsafe_allow_html=True)




    



#     tab1, tab2, tab3 = st.tabs(["📄 Data Preview", "🔍 Column Details", "📈 Summary"])

#     # ======================== TAB 1: DATA Preview ========================
#     with tab1:
#         col_left, col_right = st.columns([3, 1])
#         with col_left:
#             st.subheader("Preview Filtered Data")
#         with col_right:
#             # Slider to choose number of rows to display
#             n_rows = st.slider("Rows to show", min_value=10, max_value=200, value=20, step=10)

#         # Display the first n rows
#         st.dataframe(df.head(n_rows), use_container_width=True)

#         # Optionally show the last few rows
#         with st.expander("Show last rows"):
#              st.dataframe(df.tail(10), use_container_width=True)

#         # Download button for the filtered data
#         csv = df.to_csv(index=False).encode('utf-8')
#         st.download_button(
#             label="📥 Download filtered data as CSV",
#             data=csv,
#             file_name="bike_sales_india.csv",
#             mime="text/csv",
#             use_container_width=True,
#         )

#     # ======================== TAB 2: COLUMN DETAILS ========================
#     with tab2:

#         # Display as a styled table
#         # Compute missing values and give the column a clear name
#         missing_df = df.isna().sum().reset_index(name='Missing Count')

# # Optionally rename the first column as well
#         missing_df.rename(columns={'index': 'Column Name'}, inplace=True)

#         # Display with styling
#         st.dataframe(
#             missing_df,
#             use_container_width=True,
#             height=400
#         )
#         dtype_df = pd.DataFrame({
#             "Column": df.columns,
#             "Data Type": df.dtypes.astype(str)
#             })
        
#         st.dataframe(dtype_df, use_container_width=True)
#     # ======================== TAB 3: SUMMARY ========================
#     with tab3:
#         st.subheader("Statistical Summary")

#         # Separate numeric and categorical columns
#         num_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
#         cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

#         if num_cols:
#             st.markdown("#### 📊 Numeric Columns")
#             st.dataframe(df[num_cols].describe(), use_container_width=True)

#         if cat_cols:
#             st.markdown("#### 🏷️ Categorical Columns")
#             # Show top 3 categories for each categorical column
#             for col in cat_cols[:4]:  # Limit to first 4 to keep layout clean
#                 with st.expander(f"Top values in '{col}'"):
#                     st.dataframe(
#                         df[col].value_counts().reset_index().head(10),
#                         use_container_width=True,
#                         hide_index=True
#                     )
#         if len(cat_cols) > 4:
#                 st.info(f"Showing top 4 categorical columns. There are {len(cat_cols)} in total.")


    

























elif opt == 'Brand Analysis':
   
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');

        /* 1. Deep Carbon Mesh Background with Neon Glow */
        .stApp {
            background-color: #030509 !important;
            background-image: 
                radial-gradient(at 0% 0%, rgba(14, 165, 233, 0.18) 0px, transparent 50%),
                radial-gradient(at 100% 0%, rgba(139, 92, 246, 0.18) 0px, transparent 50%),
                radial-gradient(at 50% 100%, rgba(236, 72, 153, 0.12) 0px, transparent 50%),
                radial-gradient(at 10% 80%, rgba(16, 185, 129, 0.08) 0px, transparent 40%) !important;
            background-attachment: fixed !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }

        /* 2. Sidebar Customization */
        section[data-testid="stSidebar"] {
            background-color: #020306 !important;
            border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
        }

        /* 3. Hero Glass Header Banner */
        .hero-banner-3d {
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.8) 0%, rgba(30, 41, 59, 0.5) 100%);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 24px;
            padding: 28px 36px;
            margin-bottom: 30px;
            box-shadow: 
                0 20px 50px rgba(0, 0, 0, 0.8),
                inset 0 1px 0 rgba(255, 255, 255, 0.2);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        /* 4. TRUE 3D KPI CARDS WITH NEON GLOW & ACCENTS */
        .kpi-card-real {
            background: linear-gradient(145deg, rgba(20, 29, 47, 0.9) 0%, rgba(11, 17, 30, 0.95) 100%);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 22px;
            position: relative;
            overflow: hidden;
            box-shadow: 
                0 12px 30px -5px rgba(0, 0, 0, 0.8),
                inset 0 1px 1px rgba(255, 255, 255, 0.15),
                inset 0 -2px 5px rgba(0, 0, 0, 0.6);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            backdrop-filter: blur(16px);
        }

        .kpi-card-real:hover {
            transform: translateY(-8px) scale(1.02);
            border-color: rgba(14, 165, 233, 0.6);
            box-shadow: 
                0 20px 40px -10px rgba(0, 0, 0, 0.9),
                0 0 30px rgba(14, 165, 233, 0.3),
                inset 0 1px 2px rgba(255, 255, 255, 0.4);
        }

        /* Top Accent Bars on KPI Cards */
        .accent-blue::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, #38bdf8, #818cf8); }
        .accent-purple::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, #c084fc, #e879f9); }
        .accent-green::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, #34d399, #10b981); }
        .accent-amber::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, #fbbf24, #f59e0b); }

        .kpi-header-flex {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
        }

        .kpi-tag {
            font-size: 11px;
            font-weight: 700;
            padding: 3px 10px;
            border-radius: 20px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #94a3b8;
        }

        .kpi-title-text {
            color: #94a3b8;
            font-size: 13px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }

        .kpi-val-text {
            color: #ffffff;
            font-family: 'Space Grotesk', sans-serif;
            font-size: 32px;
            font-weight: 700;
            letter-spacing: -0.02em;
            margin: 6px 0;
            text-shadow: 0 4px 12px rgba(0, 0, 0, 0.6);
        }

        .kpi-sub-text {
            color: #64748b;
            font-size: 12px;
            font-weight: 500;
        }

        /* 5. FLOATING GLASS CHART CONTAINERS */
        .chart-box-3d {
            background: linear-gradient(145deg, rgba(15, 23, 42, 0.75) 0%, rgba(10, 15, 26, 0.85) 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 24px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 
                0 15px 35px -10px rgba(0, 0, 0, 0.7),
                inset 0 1px 1px rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(14px);
            transition: all 0.3s ease;
        }

        .chart-box-3d:hover {
            border-color: rgba(255, 255, 255, 0.18);
            box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.85);
        }

        .chart-head-title {
            color: #f8fafc;
            font-family: 'Space Grotesk', sans-serif;
            font-size: 17px;
            font-weight: 700;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        /* 6. SELECTBOX CUSTOMIZATION */
        div[data-baseweb="select"] > div {
            background-color: #0b0f19 !important;
            border: 1px solid rgba(255, 255, 255, 0.18) !important;
            border-radius: 14px !important;
            color: white !important;
            box-shadow: 0 4px 15px rgba(0,0,0,0.4) !important;
        }

        /* Smooth Scrollbar */
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: #030509; }
        ::-webkit-scrollbar-thumb { background: #0ea5e9; border-radius: 10px; }
        </style>
    """, unsafe_allow_html=True)

    # ==========================================
    # HEADER
    # ==========================================
    st.markdown("""
        <div class="hero-banner-3d">
            <div>
                <h1 style="color:#ffffff; font-family:'Space Grotesk', sans-serif; font-size:34px; font-weight:700; margin:0; letter-spacing:-0.03em;">
                    ⚡ BRAND ANALYSIS 
                </h1>
                <p style="color:#94a3b8; font-size:15px; margin:6px 0 0 0; font-weight:500;">
                    Enterprise Brand Intelligence • Resale Valuation • Performance Benchmarks
                </p>
            </div>
            
        </div>
    """, unsafe_allow_html=True)

    # ==========================================
    # BRAND FILTER
    # ==========================================
    col_f1, col_f2 = st.columns([1, 2])
    with col_f1:
        brand = st.selectbox(
            "🔍 Select Brand Focus",
            ["All Brands"] + sorted(df["Brand"].unique())
        )

    
    if brand != "All Brands":
        df_filtered = df[df["Brand"] == brand].copy()
        
        group_col = "Model" if "Model" in df_filtered.columns else "Brand"
    else:
        df_filtered = df.copy()
        group_col = "Brand"

    st.markdown("<div style='margin-bottom: 25px;'></div>", unsafe_allow_html=True)

    # ==========================================
    # 3D  KPI CARDS
    # ==========================================
    avg_resale = df_filtered['Resale Price (INR)'].mean() 
    max_price = df_filtered['Price (INR)'].max() 
    min_price = df_filtered['Price (INR)'].min() 
    avg_engine = df_filtered['Engine Capacity (cc)'].mean()

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
            <div class="kpi-card-real accent-blue">
                <div class="kpi-header-flex">
                    <span class="kpi-title-text">Avg Resale</span>
                    <span class="kpi-tag" style="color:#38bdf8;">Valuation</span>
                </div>
                <div class="kpi-val-text">₹{avg_resale:,.0f}</div>
                <div class="kpi-sub-text">Estimated market mean</div>
            </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
            <div class="kpi-card-real accent-purple">
                <div class="kpi-header-flex">
                    <span class="kpi-title-text">Highest Price</span>
                    <span class="kpi-tag" style="color:#c084fc;">Flagship</span>
                </div>
                <div class="kpi-val-text">₹{max_price:,.0f}</div>
                <div class="kpi-sub-text">Top-tier brand pricing</div>
            </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
            <div class="kpi-card-real accent-green">
                <div class="kpi-header-flex">
                    <span class="kpi-title-text">Lowest Price</span>
                    <span class="kpi-tag" style="color:#34d399;">Entry</span>
                </div>
                <div class="kpi-val-text">₹{min_price:,.0f}</div>
                <div class="kpi-sub-text">Most accessible model</div>
            </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
            <div class="kpi-card-real accent-amber">
                <div class="kpi-header-flex">
                    <span class="kpi-title-text">Avg Displacement</span>
                    <span class="kpi-tag" style="color:#fbbf24;">Capacity</span>
                </div>
                <div class="kpi-val-text">{avg_engine:.0f} <span style="font-size:18px; color:#94a3b8;">cc</span></div>
                <div class="kpi-sub-text">Engine power benchmark</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 30px;'></div>", unsafe_allow_html=True)

    # Plotly Transparent Theme Helper
    def apply_pro_plotly_theme(fig):
        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Plus Jakarta Sans, sans-serif", color="#94a3b8", size=12),
            margin=dict(t=15, b=15, l=15, r=15),
            coloraxis_showscale=False
        )
        return fig

    # ==========================================
    # CHARTS SECTION 1
    # ==========================================
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f'<div class="chart-box-3d"><div class="chart-head-title">💰 Price Spectrum by {group_col}</div>', unsafe_allow_html=True)
        brand_price = df_filtered.groupby(group_col)["Price (INR)"].mean().reset_index()
        fig1 = px.treemap(
            brand_price,
            path=[group_col],
            values="Price (INR)",
            color="Price (INR)",
            color_continuous_scale="Viridis"
        )
        st.plotly_chart(apply_pro_plotly_theme(fig1), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown(f'<div class="chart-box-3d"><div class="chart-head-title">⛽ Mileage & Efficiency Scatter</div>', unsafe_allow_html=True)
        brand_mileage = df_filtered.groupby(group_col)["Mileage (km/l)"].mean().reset_index()
        fig2 = px.scatter(
            brand_mileage,
            x=group_col,
            y="Mileage (km/l)",
            size="Mileage (km/l)",
            color="Mileage (km/l)",
            hover_name=group_col,
            color_continuous_scale="Tealgrn"
        )
        st.plotly_chart(apply_pro_plotly_theme(fig2), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ==========================================
    # CHARTS SECTION 2
    # ==========================================
    col3, col4 = st.columns(2)

    with col3:
        st.markdown(f'<div class="chart-box-3d"><div class="chart-head-title">📈 Resale Valuation Trend</div>', unsafe_allow_html=True)
        resale = df_filtered.groupby(group_col)["Resale Price (INR)"].mean().reset_index()
        fig3 = px.line(
            resale,
            x=group_col,
            y="Resale Price (INR)",
            markers=True,
            line_shape='spline'
        )
        fig3.update_traces(line_color="#0ea5e9", line_width=4, marker=dict(size=10, color="#a855f7"))
        st.plotly_chart(apply_pro_plotly_theme(fig3), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:

        
        st.markdown('<div class="chart-box-3d"><div class="chart-head-title">⚙️ Engine vs Fuel Type Hierarchy</div>', unsafe_allow_html=True)
        # Dynamic Sunburst Path Handling to prevent blank graph
        sunburst_path = ["Fuel Type", "Brand"] if brand == "All Brands" else ["Fuel Type", group_col]
        fig4 = px.sunburst(
            df_filtered,
            path=sunburst_path,
            values="Engine Capacity (cc)",
            color="Engine Capacity (cc)",
            color_continuous_scale="Plasma"
        )
        st.plotly_chart(apply_pro_plotly_theme(fig4), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ==========================================
    # CHARTS SECTION 3
    # ==========================================
    col5, col6 = st.columns(2)

    with col6:
        st.markdown('<div class="chart-box-3d"><div class="chart-head-title">👥 Bike Ownership Distribution</div>', unsafe_allow_html=True)
        owner = df_filtered["Owner Type"].value_counts().reset_index()
        owner.columns = ["Owner Type", "Count"]
        fig5 = px.pie(
            owner,
            names="Owner Type",
            values="Count",
            hole=0.6,
            color_discrete_sequence=['#0ea5e9', '#6366f1', '#a855f7', '#ec4899']
        )
        st.plotly_chart(apply_pro_plotly_theme(fig5), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)




#4444444Model AnALYSIS ..............................................................................................



























































elif opt == "Model Analysis":

    # ============================================================
    # MODEL ANALYSIS - SIMPLE PROFESSIONAL CSS
    # ============================================================
    st.markdown(
        """
        <style>

        /* Main Background */
        [data-testid="stAppViewContainer"] {
            background: #080d18 !important;
        }

        [data-testid="stHeader"] {
            background: transparent !important;
        }

        .block-container {
            max-width: 1400px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        /* Header */
        .model-header {
            background: linear-gradient(
                135deg,
                #123d4a,
                #102b43
            );
            border: 1px solid rgba(96, 165, 250, 0.35);
            border-radius: 18px;
            padding: 24px 28px;
            margin-bottom: 25px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.25);
        }

        .model-header h1 {
            color: #ffffff !important;
            margin: 0;
            font-size: 2.2rem;
            font-weight: 800;
        }

        .model-header p {
            color: #cbd5e1;
            margin: 7px 0 0 0;
            font-size: 0.95rem;
        }

        /* KPI Card */
        .model-kpi {
            background: #111827;
            border: 1px solid rgba(148, 163, 184, 0.20);
            border-radius: 15px;
            padding: 20px 16px;
            text-align: center;
            min-height: 165px;
            transition: 0.25s ease;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.25);
        }

        .model-kpi:hover {
            transform: translateY(-4px);
            border-color: rgba(96, 165, 250, 0.55);
            box-shadow: 0 10px 25px rgba(59, 130, 246, 0.18);
        }

        .model-kpi-icon {
            font-size: 25px;
            margin-bottom: 7px;
        }

        .model-kpi-title {
            color: #94a3b8;
            font-size: 0.76rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .model-kpi-value {
            color: #f8fafc;
            font-size: 1.35rem;
            font-weight: 800;
            margin-top: 8px;
        }

        .model-kpi-sub {
            color: #94a3b8;
            font-size: 0.75rem;
            margin-top: 7px;
        }

        /* Section Headings */
        .section-title {
            color: #f8fafc;
            font-size: 1.45rem;
            font-weight: 750;
            margin-top: 10px;
            margin-bottom: 12px;
        }

        /* Insight Card */
        .model-insight {
            background: #111827;
            border: 1px solid rgba(148, 163, 184, 0.18);
            border-left: 4px solid #38bdf8;
            border-radius: 12px;
            padding: 16px 18px;
            margin-bottom: 12px;
        }

        .model-insight-title {
            color: #38bdf8;
            font-weight: 700;
            font-size: 0.95rem;
            margin-bottom: 4px;
        }

        .model-insight-text {
            color: #cbd5e1;
            font-size: 0.88rem;
            line-height: 1.5;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


    # ============================================================
    # HEADER
    # ============================================================
    st.markdown(
        """
        <div class="model-header">
            <h1>🏍️ Model Analysis</h1>
            <p>
                Explore bike models and compare price, mileage,
                engine capacity and resale performance.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


    # ============================================================
    # MODEL SELECTOR
    # ============================================================
    st.subheader("🔎 Select Bike Model")

    model = st.selectbox(
        "Choose Model",
        options=sorted(df["Model"].dropna().unique()),
        key="model_analysis_select",
    )

    selected_data = df[df["Model"] == model]


    # ============================================================
    # KPI CALCULATIONS
    # ============================================================
    avg_price = selected_data["Price (INR)"].mean()
    avg_mileage = selected_data["Mileage (km/l)"].mean()
    avg_engine = selected_data["Engine Capacity (cc)"].mean()
    avg_resale = selected_data["Resale Price (INR)"].mean()

    resale_percentage = (
        (avg_resale / avg_price) * 100
        if avg_price > 0
        else 0
    )


    # ============================================================
    # KPI CARDS
    # ============================================================
    st.markdown(
        '<div class="section-title">📊 Model Overview</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div class="model-kpi"
                 style="border-bottom: 3px solid #38bdf8;">
                <div class="model-kpi-icon">💰</div>
                <div class="model-kpi-title">Avg Price</div>
                <div class="model-kpi-value">
                    ₹{avg_price:,.0f}
                </div>
                <div class="model-kpi-sub">
                    Average MSRP
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div class="model-kpi"
                 style="border-bottom: 3px solid #34d399;">
                <div class="model-kpi-icon">⛽</div>
                <div class="model-kpi-title">Avg Mileage</div>
                <div class="model-kpi-value">
                    {avg_mileage:.1f}
                    <span style="font-size:0.8rem;">km/l</span>
                </div>
                <div class="model-kpi-sub">
                    Fuel Economy
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
            <div class="model-kpi"
                 style="border-bottom: 3px solid #c084fc;">
                <div class="model-kpi-icon">⚙️</div>
                <div class="model-kpi-title">Avg Engine</div>
                <div class="model-kpi-value">
                    {avg_engine:,.0f}
                    <span style="font-size:0.8rem;">cc</span>
                </div>
                <div class="model-kpi-sub">
                    Engine Capacity
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            f"""
            <div class="model-kpi"
                 style="border-bottom: 3px solid #fbbf24;">
                <div class="model-kpi-icon">♻️</div>
                <div class="model-kpi-title">Avg Resale</div>
                <div class="model-kpi-value">
                    ₹{avg_resale:,.0f}
                </div>
                <div class="model-kpi-sub">
                    {resale_percentage:.1f}% Retained
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


    st.divider()


    # ============================================================
    # PRICE & RESALE CHART
    # ============================================================
    st.markdown(
        '<div class="section-title">💰 Price & Resale Analysis</div>',
        unsafe_allow_html=True,
    )

    price_resale = selected_data[
        ["Year of Manufacture", "Price (INR)", "Resale Price (INR)"]
    ].copy()

    price_resale = (
        price_resale
        .groupby("Year of Manufacture")
        .mean()
        .reset_index()
    )

    fig1 = px.line(
        price_resale,
        x="Year of Manufacture",
        y=["Price (INR)", "Resale Price (INR)"],
        markers=True,
        title=f"{model} - Price vs Resale Price",
    )

    fig1.update_layout(
        template="plotly_dark",
        title_x=0.5,
        hovermode="x unified",
        margin=dict(l=20, r=20, t=60, b=20),
        legend_title_text="",
    )

    st.plotly_chart(
        fig1,
        use_container_width=True,
        config={
            "displayModeBar": False,
            "scrollZoom": False,
            "doubleClick": False,
        },
    )


    # ============================================================
    # MILEAGE & ENGINE CHARTS
    # ============================================================
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:

        st.markdown(
            '<div class="section-title">⛽ Mileage Analysis</div>',
            unsafe_allow_html=True,
        )

        mileage_df = selected_data[
            ["Year of Manufacture", "Mileage (km/l)"]
        ].groupby(
            "Year of Manufacture"
        ).mean().reset_index()

        fig2 = px.bar(
            mileage_df,
            x="Year of Manufacture",
            y="Mileage (km/l)",
            title=f"{model} - Mileage by Year",
            color_discrete_sequence=["#34d399"],
        )

        fig2.update_layout(
            template="plotly_dark",
            title_x=0.5,
            margin=dict(l=20, r=20, t=60, b=20),
        )

        st.plotly_chart(
            fig2,
            use_container_width=True,
            config={
                "displayModeBar": False,
                "scrollZoom": False,
                "doubleClick": False,
            },
        )


    with chart_col2:

        st.markdown(
            '<div class="section-title">⚙️ Engine Analysis</div>',
            unsafe_allow_html=True,
        )

        engine_df = selected_data[
            ["Year of Manufacture", "Engine Capacity (cc)"]
        ].groupby(
            "Year of Manufacture"
        ).mean().reset_index()

        fig3 = px.bar(
            engine_df,
            x="Year of Manufacture",
            y="Engine Capacity (cc)",
            title=f"{model} - Engine Capacity by Year",
            color_discrete_sequence=["#c084fc"],
        )

        fig3.update_layout(
            template="plotly_dark",
            title_x=0.5,
            margin=dict(l=20, r=20, t=60, b=20),
        )

        st.plotly_chart(
            fig3,
            use_container_width=True,
            config={
                "displayModeBar": False,
                "scrollZoom": False,
                "doubleClick": False,
            },
        )


    st.divider()


    # ============================================================
    # MODEL INFORMATION
    # ============================================================
    st.markdown(
        '<div class="section-title">📋 Model Information</div>',
        unsafe_allow_html=True,
    )

    info_col1, info_col2 = st.columns(2)

    with info_col1:

        if "Brand" in selected_data.columns:
            brand_name = selected_data["Brand"].mode().iloc[0]
        else:
            brand_name = "N/A"

        st.markdown(
            f"""
            <div class="model-insight">
                <div class="model-insight-title">🏷️ Brand</div>
                <div class="model-insight-text">
                    {brand_name}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="model-insight">
                <div class="model-insight-title">📅 Manufacturing Years</div>
                <div class="model-insight-text">
                    {selected_data["Year of Manufacture"].min():.0f}
                    -
                    {selected_data["Year of Manufacture"].max():.0f}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with info_col2:

        st.markdown(
            f"""
            <div class="model-insight"
                 style="border-left-color:#fbbf24;">
                <div class="model-insight-title"
                     style="color:#fbbf24;">
                    ♻️ Resale Retention
                </div>
                <div class="model-insight-text">
                    This model retains approximately
                    <b>{resale_percentage:.1f}%</b>
                    of its average original price.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="model-insight"
                 style="border-left-color:#34d399;">
                <div class="model-insight-title"
                     style="color:#34d399;">
                    🏍️ Records Available
                </div>
                <div class="model-insight-text">
                    Analysis is based on
                    <b>{len(selected_data)}</b>
                    available records for this model.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


    # ============================================================
    # KEY INSIGHT
    # ============================================================
    st.markdown(
        '<div class="section-title">💡 Key Model Insight</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="model-insight"
             style="border-left-color:#38bdf8;">
            <div class="model-insight-title">
                📌 {model}
            </div>
            <div class="model-insight-text">
                The selected model has an average price of
                <b>₹{avg_price:,.0f}</b>, average resale value of
                <b>₹{avg_resale:,.0f}</b>, mileage of
                <b>{avg_mileage:.1f} km/l</b> and engine capacity of
                <b>{avg_engine:,.0f} cc</b>.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )



# elif opt == 'Model Analysis':
#     # ---------------------------------------------------------
#     #  CSS Styling
#     # ---------------------------------------------------------
#     st.markdown("""
#         <style>
#         /* Main Colorful Cosmic Background */
#         .stApp {
#             background: radial-gradient(circle at 20% 20%, #1e1b4b 0%, #0f172a 40%, #030712 100%);
#             color: #f8fafc;
#             font-family: 'Inter', system-ui, -apple-system, sans-serif;
#         }

#         /* Vibrant Hero Header Banner */
#         .hero-3d-header {
#             background: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
#             padding: 30px 34px;
#             border-radius: 24px;
#             box-shadow: 
#                 0 20px 40px -10px rgba(168, 85, 247, 0.45),
#                 inset 0 1px 2px rgba(255, 255, 255, 0.4);
#             margin-bottom: 32px;
#             border: 1px solid rgba(255, 255, 255, 0.25);
#         }

#         /* ==================== VIBRANT COLORFUL 3D KPI CARDS ==================== */
#         .kpi-3d-wrapper {
#             perspective: 1000px;
#             margin-bottom: 20px;
#         }

#         .kpi-3d-card {
#             border-radius: 22px;
#             padding: 22px 24px;
#             position: relative;
#             overflow: hidden;
#             border: 1px solid rgba(255, 255, 255, 0.2);
#             transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
#             transform-style: preserve-3d;
#             box-shadow: 
#                 0 20px 30px -10px rgba(0, 0, 0, 0.7),
#                 inset 0 2px 3px rgba(255, 255, 255, 0.3),
#                 inset 0 -3px 6px rgba(0, 0, 0, 0.6);
#         }

#         /* UNIQUE VIBRANT GRADIENTS FOR EACH CARD */
#         .card-cyan {
#             background: linear-gradient(135deg, rgba(14, 165, 233, 0.25) 0%, rgba(15, 23, 42, 0.9) 100%);
#             border-color: rgba(56, 189, 248, 0.4);
#         }
#         .card-emerald {
#             background: linear-gradient(135deg, rgba(16, 185, 129, 0.25) 0%, rgba(15, 23, 42, 0.9) 100%);
#             border-color: rgba(52, 211, 153, 0.4);
#         }
#         .card-purple {
#             background: linear-gradient(135deg, rgba(168, 85, 247, 0.25) 0%, rgba(15, 23, 42, 0.9) 100%);
#             border-color: rgba(192, 132, 252, 0.4);
#         }
#         .card-amber {
#             background: linear-gradient(135deg, rgba(245, 158, 11, 0.25) 0%, rgba(15, 23, 42, 0.9) 100%);
#             border-color: rgba(251, 191, 36, 0.4);
#         }

#         /* 3D Glossy Light Reflection Overlay */
#         .kpi-3d-card::before {
#             content: '';
#             position: absolute;
#             top: 0;
#             left: 0;
#             right: 0;
#             height: 45%;
#             background: linear-gradient(180deg, rgba(255, 255, 255, 0.15) 0%, rgba(255, 255, 255, 0) 100%);
#             border-radius: 22px 22px 0 0;
#             pointer-events: none;
#         }

#         /* VIBRANT HOVER LIFT-OFF EFFECT */
#         .card-cyan:hover {
#             transform: translateY(-10px) rotateX(6deg) scale(1.02);
#             box-shadow: 0 25px 35px -10px rgba(56, 189, 248, 0.5), inset 0 2px 4px rgba(255, 255, 255, 0.5);
#             border-color: #38bdf8;
#         }
#         .card-emerald:hover {
#             transform: translateY(-10px) rotateX(6deg) scale(1.02);
#             box-shadow: 0 25px 35px -10px rgba(52, 211, 153, 0.5), inset 0 2px 4px rgba(255, 255, 255, 0.5);
#             border-color: #34d399;
#         }
#         .card-purple:hover {
#             transform: translateY(-10px) rotateX(6deg) scale(1.02);
#             box-shadow: 0 25px 35px -10px rgba(192, 132, 252, 0.5), inset 0 2px 4px rgba(255, 255, 255, 0.5);
#             border-color: #c084fc;
#         }
#         .card-amber:hover {
#             transform: translateY(-10px) rotateX(6deg) scale(1.02);
#             box-shadow: 0 25px 35px -10px rgba(251, 191, 36, 0.5), inset 0 2px 4px rgba(255, 255, 255, 0.5);
#             border-color: #fbbf24;
#         }

#         .kpi-3d-top {
#             display: flex;
#             justify-content: space-between;
#             align-items: center;
#             margin-bottom: 14px;
#         }

#         .kpi-3d-title {
#             color: #cbd5e1;
#             font-size: 12px;
#             font-weight: 700;
#             text-transform: uppercase;
#             letter-spacing: 1px;
#         }

#         /* Colorful Glowing Badge Icons */
#         .icon-cyan { background: linear-gradient(135deg, #0284c7, #38bdf8); box-shadow: 0 0 15px rgba(56, 189, 248, 0.6); }
#         .icon-emerald { background: linear-gradient(135deg, #059669, #34d399); box-shadow: 0 0 15px rgba(52, 211, 153, 0.6); }
#         .icon-purple { background: linear-gradient(135deg, #7c3aed, #c084fc); box-shadow: 0 0 15px rgba(192, 132, 252, 0.6); }
#         .icon-amber { background: linear-gradient(135deg, #d97706, #fbbf24); box-shadow: 0 0 15px rgba(251, 191, 36, 0.6); }

#         .kpi-3d-icon {
#             width: 44px;
#             height: 44px;
#             border-radius: 14px;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             font-size: 22px;
#             border: 1px solid rgba(255, 255, 255, 0.4);
#             color: white;
#         }

#         .kpi-3d-value {
#             color: #ffffff;
#             font-size: 32px;
#             font-weight: 800;
#             letter-spacing: -0.5px;
#             text-shadow: 0 4px 12px rgba(0, 0, 0, 0.6);
#         }

#         .kpi-3d-subtext {
#             font-size: 13px;
#             font-weight: 600;
#             margin-top: 6px;
#             display: flex;
#             align-items: center;
#             gap: 4px;
#         }

#         /* 3D Colorful Insight Boxes */
#         .insight-3d-box {
#             background: linear-gradient(135deg, rgba(30, 41, 59, 0.7), rgba(15, 23, 42, 0.8));
#             border-left: 5px solid #a855f7;
#             padding: 18px 22px;
#             border-radius: 16px;
#             margin-bottom: 14px;
#             box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
#             border-top: 1px solid rgba(255, 255, 255, 0.1);
#             border-right: 1px solid rgba(255, 255, 255, 0.1);
#             border-bottom: 1px solid rgba(255, 255, 255, 0.1);
#             backdrop-filter: blur(12px);
#         }
#         </style>
#     """, unsafe_allow_html=True)

#     # ---------------------------------------------------------
#     # 2.  Header
#     # ---------------------------------------------------------
#     st.markdown("""
#         <div class="hero-3d-header">
#             <h1 style="color: white; margin: 0; font-size: 34px; font-weight: 800; letter-spacing: -0.5px;">
#                 🚲 Model Analysis Analytics
#             </h1>
#             <p style="color: #f1f5f9; margin-top: 6px; font-size: 16px; margin-bottom: 0;">
#                 Vibrant 3D metrics, market trends & model performance matrix.
#             </p>
#         </div>
#     """, unsafe_allow_html=True)

#     # ---------------------------------------------------------
#     # 3. Filter data preview
#     # ---------------------------------------------------------
#     col_filter, col_slider = st.columns([1, 1])

#     with col_filter:
#         brand = st.selectbox(
#             "🔍 Select Brand Filter",
#             ["All"] + sorted(df["Brand"].dropna().unique().tolist())
#         )

#     with col_slider:
#         n_rows = st.slider("📄 Preview Data Rows", min_value=5, max_value=50, value=10, step=5)

#     filtered_df = df if brand == "All" else df[df["Brand"] == brand]

#     with st.expander("📊 View Raw Filtered Data Table", expanded=False):
#         st.dataframe(filtered_df.head(n_rows), use_container_width=True)

#     st.markdown("<hr style='border:0; height:1px; background:linear-gradient(90deg, #38bdf8, #a855f7, #ec4899); margin:25px 0;'>", unsafe_allow_html=True)

#     # ---------------------------------------------------------
#     # 4.  KPI CARDS
#     # ---------------------------------------------------------
#     st.markdown("### ⚡ Performance Overview")

#     if not filtered_df.empty:
#         avg_price = filtered_df["Price (INR)"].mean()
#         avg_mileage = filtered_df["Mileage (km/l)"].mean()
#         avg_engine = filtered_df["Engine Capacity (cc)"].mean()
#         avg_resale = filtered_df["Resale Price (INR)"].mean()
        
#         retention_rate = (avg_resale / avg_price * 100) if avg_price > 0 else 0

#         k1, k2, k3, k4 = st.columns(4)

#         with k1:
#             st.markdown(f"""
#                 <div class="kpi-3d-wrapper">
#                     <div class="kpi-3d-card card-cyan">
#                         <div class="kpi-3d-top">
#                             <span class="kpi-3d-title">Avg Price</span>
#                             <div class="kpi-3d-icon icon-cyan">💰</div>
#                         </div>
#                         <div class="kpi-3d-value">₹{avg_price:,.0f}</div>
#                         <div class="kpi-3d-subtext" style="color:#38bdf8;">🏷️ Average MSRP</div>
#                     </div>
#                 </div>
#             """, unsafe_allow_html=True)

#         with k2:
#             st.markdown(f"""
#                 <div class="kpi-3d-wrapper">
#                     <div class="kpi-3d-card card-emerald">
#                         <div class="kpi-3d-top">
#                             <span class="kpi-3d-title">Avg Mileage</span>
#                             <div class="kpi-3d-icon icon-emerald">⛽</div>
#                         </div>
#                         <div class="kpi-3d-value">{avg_mileage:.1f} <span style="font-size:16px; font-weight:500;">km/l</span></div>
#                         <div class="kpi-3d-subtext" style="color:#34d399;">⚡ Fuel Economy</div>
#                     </div>
#                 </div>
#             """, unsafe_allow_html=True)

#         with k3:
#             st.markdown(f"""
#                 <div class="kpi-3d-wrapper">
#                     <div class="kpi-3d-card card-purple">
#                         <div class="kpi-3d-top">
#                             <span class="kpi-3d-title">Avg Engine</span>
#                             <div class="kpi-3d-icon icon-purple">⚙️</div>
#                         </div>
#                         <div class="kpi-3d-value">{avg_engine:.0f} <span style="font-size:16px; font-weight:500;">cc</span></div>
#                         <div class="kpi-3d-subtext" style="color:#c084fc;">🚀 Displacement Size</div>
#                     </div>
#                 </div>
#             """, unsafe_allow_html=True)

#         with k4:
#             st.markdown(f"""
#                 <div class="kpi-3d-wrapper">
#                     <div class="kpi-3d-card card-amber">
#                         <div class="kpi-3d-top">
#                             <span class="kpi-3d-title">Avg Resale</span>
#                             <div class="kpi-3d-icon icon-amber">♻️</div>
#                         </div>
#                         <div class="kpi-3d-value">₹{avg_resale:,.0f}</div>
#                         <div class="kpi-3d-subtext" style="color:#fbbf24;">📈 {retention_rate:.1f}% Retained</div>
#                     </div>
#                 </div>
#             """, unsafe_allow_html=True)

    

#     st.markdown("<hr style='border:0; height:1px; background:linear-gradient(90deg, #ec4899, #a855f7, #38bdf8); margin:25px 0;'>", unsafe_allow_html=True)

#     # ---------------------------------------------------------
#     # 5. SCATTER PLOTS
#     # ---------------------------------------------------------
#     st.markdown("### 📊 Data Visualization")

#     chart_col1, chart_col2 = st.columns(2)

#     with chart_col1:
#         st.markdown("**Price vs Resale Price**")
#         st.line_chart(
#             filtered_df,
#             x="Price (INR)",
#             y="Resale Price (INR)",
#             use_container_width=True
#         )

#     with chart_col2:
#         st.markdown("**Brand-wise Average Price**")
#         bar_data = filtered_df.groupby("Brand")["Price (INR)"].mean()

#         st.bar_chart(
#             bar_data,
#             use_container_width=True
#         )

#     # ---------------------------------------------------------
#     # 6. Highlights & Quick Insights
#     # ---------------------------------------------------------
#     st.markdown("### 💡 Market Highlights")

#     most_popular = df["Model"].mode()[0]
#     highest_price = df.loc[df["Price (INR)"].idxmax(), "Model"]
#     highest_mileage = df.loc[df["Mileage (km/l)"].idxmax(), "Model"]
#     highest_resale = df.loc[df["Resale Price (INR)"].idxmax(), "Model"]

#     i1, i2 = st.columns(2)

#     with i1:
#         st.markdown(f"""
#             <div class="insight-3d-box">
#                 🏆 <b>Most Popular Model:</b>
#                 <span style="color:#38bdf8; font-weight:700;">{most_popular}</span>
#             </div>

#             <div class="insight-3d-box">
#                 💎 <b>Highest Price Model:</b>
#                 <span style="color:#c084fc; font-weight:700;">{highest_price}</span>
#             </div>
#         """, unsafe_allow_html=True)

#     with i2:
#         st.markdown(f"""
#             <div class="insight-3d-box">
#                 ⛽ <b>Highest Mileage Model:</b>
#                 <span style="color:#34d399; font-weight:700;">{highest_mileage}</span>
#             </div>

#             <div class="insight-3d-box">
#                 📈 <b>Highest Resale Model:</b>
#                 <span style="color:#fbbf24; font-weight:700;">{highest_resale}</span>
#             </div>
#         """, unsafe_allow_html=True)









































# 555555555555555555555555555555555555555555555555555555555555



elif opt== 'Price Analyse':
# ==========================================
#  CSS for STYLING 
# ==========================================   
    st.markdown(
    """
    <style>
    /* 🌊 Moving Animated Background */
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: linear-gradient(-45deg, #0f172a, #1e1b4b, #2e1065, #020617);
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
        color: #f8fafc;
    }

    /* 💎 Modern Glass Header */
    .header-box {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(168, 85, 247, 0.2));
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5), inset 0 1px 1px rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(16px);
        border-radius: 20px;
        padding: 24px;
        margin-bottom: 25px;
        text-align: center;
    }

    /* 🚀 3D Glossy KPI Cards with Pop Hover */
    .kpi-card {
        background: rgba(15, 23, 42, 0.65);
        border-radius: 16px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.12);
        text-align: center;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4), inset 0 1px 2px rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(12px);
        transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
    }

    .kpi-card:hover {
        transform: translateY(-8px) scale(1.02);
        border-color: rgba(168, 85, 247, 0.6);
        box-shadow: 0 15px 30px rgba(168, 85, 247, 0.35), inset 0 1px 2px rgba(255, 255, 255, 0.4);
    }

    .kpi-title {
        color: #94a3b8;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .kpi-value {
        font-size: 1.8rem;
        font-weight: 800;
        margin: 8px 0 4px 0;
        text-shadow: 0 0 12px currentColor;
    }

    .kpi-sub {
        color: #cbd5e1;
        font-size: 0.78rem;
    }

    /* 💡 Glossy Insight Card */
    .insight-card {
        background: rgba(15, 23, 42, 0.55);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-left: 4px solid #a855f7;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(10px);
        border-radius: 14px;
        padding: 16px 20px;
        margin-bottom: 12px;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )





































# ==========================================
# 💰 OPTION 1: PRICE ANALYSIS
# ==========================================
if opt == "Price Analysis":

    # ============================================================
    # PROFESSIONAL PRICE ANALYSIS CSS
    # ============================================================
    st.markdown(
        """
<style>

.header-box {
    background: linear-gradient(135deg, #123b43 0%, #0d3040 50%, #10253b 100%);
    border: 1px solid rgba(96, 165, 250, 0.38);
    border-radius: 20px;
    padding: 30px 34px;
    margin-bottom: 30px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.28), inset 0 1px 0 rgba(255,255,255,0.06);
    position: relative;
    overflow: hidden;
}

.header-box::before {
    content: "";
    position: absolute;
    width: 180px;
    height: 180px;
    background: rgba(59,130,246,0.10);
    border-radius: 50%;
    top: -90px;
    right: 40px;
    filter: blur(5px);
}

.header-box h1 {
    color: #ffffff !important;
    margin: 0 !important;
    font-size: 2.25rem !important;
    font-weight: 800 !important;
    letter-spacing: -0.5px;
    position: relative;
}

.header-box p {
    color: #cbd5e1 !important;
    margin-top: 8px !important;
    font-size: 0.98rem !important;
    position: relative;
}

.price-section-title {
    display: flex;
    align-items: center;
    background: linear-gradient(90deg, rgba(30,64,175,0.18), rgba(15,23,42,0.02));
    border-left: 4px solid #60a5fa;
    border-radius: 10px;
    padding: 13px 18px;
    margin: 30px 0 17px 0;
    color: #f8fafc;
    font-size: 21px;
    font-weight: 800;
    letter-spacing: 0.2px;
    box-shadow: 0 5px 18px rgba(0,0,0,0.12);
}

.price-section-title::before {
    content: "";
    width: 7px;
    height: 7px;
    background: #60a5fa;
    border-radius: 50%;
    margin-right: 10px;
    box-shadow: 0 0 8px rgba(96,165,250,0.9);
}

.price-kpi {
    background: linear-gradient(145deg, #1a2538 0%, #111a2b 100%);
    border: 1px solid rgba(148,163,184,0.16);
    border-radius: 17px;
    padding: 21px 18px;
    min-height: 116px;
    text-align: center;
    box-shadow: 0 8px 25px rgba(0,0,0,0.25);
    transition: transform 0.25s ease, box-shadow 0.25s ease,
                border-color 0.25s ease, background 0.25s ease;
    position: relative;
    overflow: hidden;
}

.price-kpi::after {
    content: "";
    position: absolute;
    width: 150px;
    height: 150px;
    background: rgba(96,165,250,0.13);
    border-radius: 50%;
    top: -95px;
    right: -65px;
    filter: blur(8px);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.price-kpi:hover {
    transform: translateY(-5px);
    border-color: rgba(96,165,250,0.65);
    background: linear-gradient(145deg, #1d2b43 0%, #121d31 100%);
    box-shadow: 0 14px 32px rgba(0,0,0,0.32),
                0 0 22px rgba(59,130,246,0.16);
}

.price-kpi:hover::after {
    opacity: 1;
}

.kpi-icon {
    font-size: 25px;
    margin-bottom: 6px;
    transition: transform 0.25s ease, filter 0.25s ease;
}

.price-kpi:hover .kpi-icon {
    transform: scale(1.12);
    filter: drop-shadow(0 0 7px rgba(96,165,250,0.55));
}

.kpi-label {
    color: #94a3b8;
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    transition: color 0.25s ease;
}

.price-kpi:hover .kpi-label {
    color: #cbd5e1;
}

.kpi-number {
    color: #f8fafc;
    font-size: 23px;
    font-weight: 850;
    margin-top: 5px;
    letter-spacing: -0.3px;
    transition: color 0.25s ease, text-shadow 0.25s ease;
}

.price-kpi:hover .kpi-number {
    color: #ffffff;
    text-shadow: 0 0 12px rgba(96,165,250,0.35);
}

.insight-card {
    background: linear-gradient(145deg, #121d30, #0f172a);
    border: 1px solid rgba(96,165,250,0.20);
    border-left: 4px solid #60a5fa;
    border-radius: 13px;
    padding: 17px 20px;
    margin: 12px 0;
    color: #cbd5e1;
    font-size: 15px;
    line-height: 1.6;
    box-shadow: 0 7px 22px rgba(0,0,0,0.18);
    transition: transform 0.25s ease, border-color 0.25s ease,
                box-shadow 0.25s ease;
}

.insight-card:hover {
    transform: translateX(4px);
    border-left-color: #93c5fd;
    box-shadow: 0 9px 26px rgba(37,99,235,0.15);
}

hr {
    border-color: rgba(148,163,184,0.16) !important;
}

</style>
        """,
        unsafe_allow_html=True
    )


    # ============================================================
    # HEADER
    # ============================================================

    st.markdown(
        """
<div class="header-box">
<h1>💰 Price Analysis</h1>
<p>Analyze bike pricing trends, brand values, and market distribution.</p>
</div>
        """,
        unsafe_allow_html=True
    )


    # ============================================================
    # CALCULATIONS
    # ============================================================

    avg_price = df["Price (INR)"].mean()
    avg_resale = df["Resale Price (INR)"].mean()
    highest_price = df["Price (INR)"].max()
    lowest_price = df["Price (INR)"].min()
    price_gap = highest_price - lowest_price
    retention_pct = (avg_resale / avg_price) * 100


    # ============================================================
    # KPI CARDS
    # ============================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
<div class="price-kpi">
<div class="kpi-icon">💰</div>
<div class="kpi-label">Average Price</div>
<div class="kpi-number">₹{avg_price:,.0f}</div>
</div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
<div class="price-kpi">
<div class="kpi-icon">💵</div>
<div class="kpi-label">Average Resale</div>
<div class="kpi-number">₹{avg_resale:,.0f}</div>
</div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
<div class="price-kpi">
<div class="kpi-icon">📈</div>
<div class="kpi-label">Highest Price</div>
<div class="kpi-number">₹{highest_price:,.0f}</div>
</div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
<div class="price-kpi">
<div class="kpi-icon">📊</div>
<div class="kpi-label">Price Range Gap</div>
<div class="kpi-number">₹{price_gap:,.0f}</div>
</div>
            """,
            unsafe_allow_html=True
        )


    st.divider()


    # ============================================================
    # PRICE DISTRIBUTION
    # ============================================================

    st.markdown(
        '<div class="price-section-title">📊 Price Distribution</div>',
        unsafe_allow_html=True
    )

    fig1 = px.histogram(
        df,
        x="Price (INR)",
        nbins=30,
        title="Distribution of Bike Prices",
        color_discrete_sequence=["#6366f1"]
    )

    fig1.update_traces(
        marker_line_color="#0f172a",
        marker_line_width=1.5
    )

    fig1.update_layout(
        template="plotly_dark",
        title_x=0.5,
        title_font_size=18,
        title_font_color="#f8fafc",
        paper_bgcolor="#0d1422",
        plot_bgcolor="#0d1422",
        font=dict(color="#cbd5e1")
    )

    st.plotly_chart(fig1, use_container_width=True)


    # ============================================================
    # AVERAGE PRICE BY BRAND
    # ============================================================

    st.markdown(
        '<div class="price-section-title">🏍️ Average Price by Brand</div>',
        unsafe_allow_html=True
    )

    brand_price = (
        df.groupby("Brand")["Price (INR)"]
        .mean()
        .reset_index()
    )

    fig2 = px.bar(
        brand_price,
        x="Brand",
        y="Price (INR)",
        color="Brand",
        title="Average Price by Brand"
    )

    fig2.update_layout(
        template="plotly_dark",
        title_x=0.5,
        title_font_size=18,
        title_font_color="#f8fafc",
        paper_bgcolor="#0d1422",
        plot_bgcolor="#0d1422",
        font=dict(color="#cbd5e1")
    )

    st.plotly_chart(fig2, use_container_width=True)


    # ============================================================
    # PRICE VS MILEAGE
    # ============================================================

    st.markdown(
        '<div class="price-section-title">⛽ Price vs Mileage</div>',
        unsafe_allow_html=True
    )

    mileage_data = df.groupby("Brand")[
        ["Mileage (km/l)", "Price (INR)"]
    ].mean().reset_index()

    fig3 = px.scatter(
        mileage_data,
        x="Mileage (km/l)",
        y="Price (INR)",
        color="Brand",
        title="Average Price vs Average Mileage by Brand"
    )

    fig3.update_layout(
        template="plotly_dark",
        title_x=0.5,
        title_font_size=18,
        title_font_color="#f8fafc",
        paper_bgcolor="#0d1422",
        plot_bgcolor="#0d1422",
        font=dict(color="#cbd5e1")
    )

    st.plotly_chart(fig3, use_container_width=True)


    # ============================================================
    # PRICE VS RESALE
    # ============================================================

    st.markdown(
        '<div class="price-section-title">♻️ Price vs Resale Price</div>',
        unsafe_allow_html=True
    )

    brand_resale_data = df.groupby("Brand")[
        ["Price (INR)", "Resale Price (INR)"]
    ].mean().reset_index()

    fig4 = px.scatter(
        brand_resale_data,
        x="Price (INR)",
        y="Resale Price (INR)",
        color="Brand",
        title="Average Price vs Average Resale Price by Brand"
    )

    fig4.update_layout(
        template="plotly_dark",
        title_x=0.5,
        title_font_size=18,
        title_font_color="#f8fafc",
        paper_bgcolor="#0d1422",
        plot_bgcolor="#0d1422",
        font=dict(color="#cbd5e1")
    )

    st.plotly_chart(fig4, use_container_width=True)


    # ============================================================
    # AVERAGE PRICE TREND
    # ============================================================

    st.markdown(
        '<div class="price-section-title">📅 Average Price Trend</div>',
        unsafe_allow_html=True
    )

    year_price = df.groupby("Year of Manufacture")[
        "Price (INR)"
    ].mean().reset_index()

    fig5 = px.line(
        year_price,
        x="Year of Manufacture",
        y="Price (INR)",
        markers=True,
        title="Average Price by Manufacturing Year"
    )

    fig5.update_layout(
        template="plotly_dark",
        title_x=0.5,
        title_font_size=18,
        title_font_color="#f8fafc",
        paper_bgcolor="#0d1422",
        plot_bgcolor="#0d1422",
        font=dict(color="#cbd5e1")
    )

    st.plotly_chart(fig5, use_container_width=True)


    # ============================================================
    # KEY INSIGHTS
    # ============================================================

    st.markdown(
        '<div class="price-section-title">💡 Key Insights</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
<div class="insight-card">
📍 <b>Market Price Range:</b>
Bikes range from ₹{lowest_price:,.0f} to ₹{highest_price:,.0f}.
</div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
<div class="insight-card">
📊 <b>Average Valuation:</b>
The average bike price is ₹{avg_price:,.0f}.
</div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
<div class="insight-card">
♻️ <b>Resale Value:</b>
The average resale price is ₹{avg_resale:,.0f},
which is about {retention_pct:.1f}% of the average price.
</div>
        """,
        unsafe_allow_html=True
    )

































# if opt == "Price Analysis":

#     st.markdown(
#         """
#         <div class="header-box">
#             <h1 style="color: #ffffff; margin: 0; font-size: 2.2rem;">💰 Price Analysis</h1>
#             <p style="color: #cbd5e1; margin-top: 5px; font-size: 0.95rem;">
#                 Analyze bike pricing trends, brand values, and market distribution.
#             </p>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

#     avg_price = df["Price (INR)"].mean()
#     avg_resale = df["Resale Price (INR)"].mean()
#     highest_price = df["Price (INR)"].max()
#     lowest_price = df["Price (INR)"].min()
#     price_gap = highest_price - lowest_price
#     retention_pct = (avg_resale / avg_price) * 100

#     # KPI Cards
#     col1, col2, col3, col4 = st.columns(4)

#     with col1:
#         st.metric("💰 Average Price", f"₹{avg_price:,.0f}")

#     with col2:
#         st.metric("💵 Average Resale", f"₹{avg_resale:,.0f}")

#     with col3:
#         st.metric("📈 Highest Price", f"₹{highest_price:,.0f}")

#     with col4:
#         st.metric("📊 Price Range Gap", f"₹{price_gap:,.0f}")

#     st.divider()

#     # Histogram
#     st.subheader("📊 Price Distribution")

#     fig1 = px.histogram(
#         df,
#         x="Price (INR)",
#         nbins=30,
#         title="Distribution of Bike Prices",
#         color_discrete_sequence=["#6366f1"]
#     )

#     fig1.update_traces(
#         marker_line_color="#0f172a",
#         marker_line_width=1.5
#     )

#     fig1.update_layout(
#         template="plotly_dark",
#         title_x=0.5
#     )

#     st.plotly_chart(fig1, use_container_width=True)

#     # Bar Chart
#     st.subheader("🏍 Average Price by Brand")

#     brand_price = df.groupby("Brand")["Price (INR)"].mean().reset_index()

#     fig2 = px.bar(
#         brand_price,
#         x="Brand",
#         y="Price (INR)",
#         color="Brand",
#         title="Average Price by Brand"
#     )

#     fig2.update_layout(
#         template="plotly_dark",
#         title_x=0.5
#     )

#     st.plotly_chart(fig2, use_container_width=True)

#     # Price vs Mileage
#     st.subheader("⛽ Price vs Mileage")

#     mileage_data = df.groupby("Brand")[
#         ["Mileage (km/l)", "Price (INR)"]
#     ].mean().reset_index()

#     fig3 = px.scatter(
#         mileage_data,
#         x="Mileage (km/l)",
#         y="Price (INR)",
#         color="Brand",
#         title="Average Price vs Average Mileage by Brand"
#     )

#     st.plotly_chart(fig3, use_container_width=True)

#     # Price vs Resale
#     st.subheader("♻️ Price vs Resale Price")

#     brand_resale_data = df.groupby("Brand")[
#         ["Price (INR)", "Resale Price (INR)"]
#     ].mean().reset_index()

#     fig4 = px.scatter(
#         brand_resale_data,
#         x="Price (INR)",
#         y="Resale Price (INR)",
#         color="Brand",
#         title="Average Price vs Average Resale Price by Brand"
#     )

#     st.plotly_chart(fig4, use_container_width=True)

#     # Line Chart
#     st.subheader("📅 Average Price Trend")

#     year_price = df.groupby("Year of Manufacture")[
#         "Price (INR)"
#     ].mean().reset_index()

#     fig5 = px.line(
#         year_price,
#         x="Year of Manufacture",
#         y="Price (INR)",
#         markers=True,
#         title="Average Price by Manufacturing Year"
#     )

#     st.plotly_chart(fig5, use_container_width=True)

#     # Key Insights
#     st.subheader("💡 Key Insights")

#     st.markdown(
#         f"""
#         <div class="insight-card">
#             📍 <b>Market Price Range:</b>
#             Bikes range from ₹{lowest_price:,.0f} to ₹{highest_price:,.0f}.
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

#     st.markdown(
#         f"""
#         <div class="insight-card">
#             📊 <b>Average Valuation:</b>
#             The average bike price is ₹{avg_price:,.0f}.
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

#     st.markdown(
#         f"""
#         <div class="insight-card">
#             ♻️ <b>Resale Value:</b>
#             The average resale price is ₹{avg_resale:,.0f},
#             which is about {retention_pct:.1f}% of the average price.
#         </div>
#         """,
#         unsafe_allow_html=True
#     )














elif opt == "Resale Analysis":
    st.markdown(
        """
        <style>
        /* 🌌 Deep Dark Ambient Glow Background for Main Container & Page */
        [data-testid="stAppViewContainer"] {
            background: radial-gradient(circle at 50% -10%, #1e293b 0%, #0f172a 45%, #020617 100%) !important;
        }

        [data-testid="stHeader"] {
            background: transparent !important;
        }

        /* 🌟 Glossy Header */
        .glossy-header {
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(6, 182, 212, 0.15));
            border: 1px solid rgba(255, 255, 255, 0.18);
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6), inset 0 1px 2px rgba(255, 255, 255, 0.3);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 24px;
            text-align: center;
            margin-bottom: 20px;
        }

        /* 💎 Glossy KPI Card with Smooth Hover Pop-Up Effect */
        .glossy-kpi-card {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.08), rgba(255, 255, 255, 0.02));
            border-radius: 16px;
            padding: 20px;
            text-align: center;
            border: 1px solid rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), inset 0 1px 1px rgba(255, 255, 255, 0.2);
            transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s ease, border-color 0.3s ease;
            cursor: pointer;
        }

        /* 🚀 Pop-Up Effect on Hover */
        .glossy-kpi-card:hover {
            transform: translateY(-10px) scale(1.03);
            box-shadow: 0 20px 40px rgba(16, 185, 129, 0.4), inset 0 1px 2px rgba(255, 255, 255, 0.5);
            border-color: rgba(255, 255, 255, 0.45);
        }

        /* 💡 Glossy Insight Cards */
        .glossy-insight-card {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.06), rgba(255, 255, 255, 0.01));
            border: 1px solid rgba(255, 255, 255, 0.12);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-radius: 14px;
            padding: 18px;
            margin-bottom: 14px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
            transition: all 0.3s ease;
        }

        .glossy-insight-card:hover {
            border-color: rgba(255, 255, 255, 0.35);
            transform: translateX(5px);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # 2. Header Block
    st.markdown(
        """
        <div class="glossy-header">
            <h1 style="color: #ffffff; margin: 0; font-size: 2.3rem; font-weight: 800;">⚡ Bike Resale Analytics </h1>
            <p style="color: #cbd5e1; margin-top: 6px; font-size: 0.95rem;">Interactive market analytics with real-time category grouping.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 3. 🎯 TOP SELECT BOX 
    selected_group = st.selectbox(
    "🎛️ Select Category",
    ["Brand", "Fuel Type", "Year of Manufacture", "Owner Type"]
    )

    current_year = 2026
    df["Bike Age"] = current_year - df["Year of Manufacture"]

    grouped_df = df.groupby(selected_group)["Resale Price (INR)"].mean().reset_index()

    grouped_df = grouped_df.sort_values(
        "Resale Price (INR)",
        ascending=False
    )

    top_group_item = grouped_df.iloc[0][selected_group]
    top_group_val = grouped_df.iloc[0]["Resale Price (INR)"]

    lowest_group_item = grouped_df.iloc[-1][selected_group]
    lowest_group_val = grouped_df.iloc[-1]["Resale Price (INR)"]

    avg_resale = df["Resale Price (INR)"].mean()

    total_categories = df[selected_group].nunique()


    # 4. Dynamic Glossy Pop-Up KPI Cards Row (Changes with Select Box)
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div class="glossy-kpi-card" style="border-bottom: 3px solid #10b981;">
                <div style="color: #9ca3af; font-size: 0.75rem; font-weight: 700; text-transform: uppercase;">Top {selected_group}</div>
                <div style="font-size: 1.5rem; font-weight: 900; color: #10b981; margin: 6px 0;">{top_group_item}</div>
                <div style="color: #cbd5e1; font-size: 0.75rem;">Avg: ₹{top_group_val:,.0f}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div class="glossy-kpi-card" style="border-bottom: 3px solid #38bdf8;">
                <div style="color: #9ca3af; font-size: 0.75rem; font-weight: 700; text-transform: uppercase;">Lowest {selected_group}</div>
                <div style="font-size: 1.5rem; font-weight: 900; color: #38bdf8; margin: 6px 0;">{lowest_group_item}</div>
                <div style="color: #cbd5e1; font-size: 0.75rem;">Avg: ₹{lowest_group_val:,.0f}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
            <div class="glossy-kpi-card" style="border-bottom: 3px solid #f43f5e;">
                <div style="color: #9ca3af; font-size: 0.75rem; font-weight: 700; text-transform: uppercase;">Overall Avg Resale</div>
                <div style="font-size: 1.5rem; font-weight: 900; color: #f43f5e; margin: 6px 0;">₹{avg_resale:,.0f}</div>
                <div style="color: #cbd5e1; font-size: 0.75rem;">All Bikes Mean</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            f"""
            <div class="glossy-kpi-card" style="border-bottom: 3px solid #f59e0b;">
                <div style="color: #9ca3af; font-size: 0.75rem; font-weight: 700; text-transform: uppercase;">Total {selected_group}s</div>
                <div style="font-size: 1.5rem; font-weight: 900; color: #f59e0b; margin: 6px 0;">{total_categories}</div>
                <div style="color: #cbd5e1; font-size: 0.75rem;">Unique Groups</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    # 5. Dynamic Charts Section
    st.subheader(f"📊 Average Resale Price by {selected_group}")

    fig_bar = px.bar(
    grouped_df,
    x=selected_group,
    y="Resale Price (INR)",
    title=f"Average Resale Price Grouped by {selected_group}",
    color="Resale Price (INR)",
    color_continuous_scale="Mint",
    text_auto=".0f"
    )

    st.plotly_chart(fig_bar, use_container_width=True)

    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        st.subheader(f"⛽ Resale Share by {selected_group}")

        fig_pie = px.pie(
            grouped_df,
            names=selected_group,
            values="Resale Price (INR)",
            title=f"Resale Price Breakdown ({selected_group})",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Dark24
        )

        st.plotly_chart(fig_pie, use_container_width=True)


    with col_chart2:
        st.subheader(f"📉 Resale vs Bike Age (Grouped by {selected_group})")

        fig_scatter = px.scatter(
            df,
            x="Bike Age",
            y="Resale Price (INR)",
            color=selected_group,
            size="Engine Capacity (cc)",
            title=f"Bike Age vs Resale Price Scatter ({selected_group})",
            color_discrete_sequence=px.colors.qualitative.Bold
        )

        st.plotly_chart(fig_scatter, use_container_width=True)

    # 6. Dynamic Glossy Insights
    st.subheader("💡 Dynamic Resale Insights")

    st.markdown(
        f"""
        <div class="glossy-insight-card" style="border-left: 5px solid #10b981;">
            <div style="font-weight: bold; color: #10b981; font-size: 1rem;">🏆 Top Performance in {selected_group}</div>
            <div style="color: #cbd5e1; margin-top: 4px; font-size: 0.9rem;">
                <b>{top_group_item}</b> leads this category with the highest average resale price of <b>₹{top_group_val:,.0f}</b>.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="glossy-insight-card" style="border-left: 5px solid #38bdf8;">
            <div style="font-weight: bold; color: #38bdf8; font-size: 1rem;">📉 Budget Category in {selected_group}</div>
            <div style="color: #cbd5e1; margin-top: 4px; font-size: 0.9rem;">
                <b>{lowest_group_item}</b> sits at the lower end of the resale market with an average valuation of <b>₹{lowest_group_val:,.0f}</b>.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
            

# #staaaaatttttteeeeeeeee anallysissssssss..................................................................

























elif opt == "State Analysis":

    # ============================================================
    # CSS STYLING - PROFESSIONAL DARK BLUE THEME
    # ============================================================
    st.markdown(
        """
<style>
.stApp {
    background: linear-gradient(180deg, #0b1120 0%, #080d1a 100%) !important;
}

.block-container {
    max-width: 1400px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

/* MAIN HEADINGS */
h1, h2, h3 {
    color: #f8fafc !important;
    font-weight: 750 !important;
}

[data-testid="stCaptionContainer"] {
    color: #60a5fa !important;
    font-size: 13px !important;
    font-weight: 700 !important;
    letter-spacing: 0.6px;
}

/* DIVIDER */
hr {
    border-color: rgba(148, 163, 184, 0.20) !important;
}

/* ============================================================
   KPI CARDS
   ============================================================ */

.kpi-card {
    background: linear-gradient(145deg, #172033, #111827);
    border: 1px solid rgba(96, 165, 250, 0.18);
    border-radius: 16px;
    padding: 19px;
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 10px;
    min-height: 72px;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.25);
    transition: all 0.25s ease;
}

.kpi-card:hover {
    transform: translateY(-3px);
    border-color: rgba(96, 165, 250, 0.55);
    box-shadow: 0 12px 30px rgba(37, 99, 235, 0.16);
}

/* BLUE CIRCLE ICON */
.kpi-icon-circle {
    width: 52px;
    height: 52px;
    min-width: 52px;
    border-radius: 50%;
    background: radial-gradient(
        circle,
        rgba(59, 130, 246, 0.35) 0%,
        rgba(30, 64, 175, 0.12) 100%
    );
    border: 1.5px solid #3b82f6;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 23px;
    box-shadow: 0 0 15px rgba(59, 130, 246, 0.30);
}

.kpi-content {
    display: flex;
    flex-direction: column;
}

.kpi-title {
    color: #94a3b8;
    font-size: 12px;
    font-weight: 650;
    margin: 0;
    text-transform: uppercase;
    letter-spacing: 0.7px;
}

.kpi-value {
    color: #f8fafc;
    font-size: 20px;
    font-weight: 800;
    margin-top: 3px;
}

/* ============================================================
   BUTTONS
   ============================================================ */

div.stButton > button {
    width: 100%;
    min-height: 38px;
    border-radius: 9px;
    background: #111c30;
    color: #93c5fd;
    border: 1px solid rgba(96, 165, 250, 0.25);
    font-weight: 600;
    transition: all 0.25s ease;
}

div.stButton > button:hover {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: #ffffff;
    border-color: #3b82f6;
    box-shadow: 0 5px 18px rgba(37, 99, 235, 0.25);
}

/* ============================================================
   SELECTBOX
   ============================================================ */

div[data-baseweb="select"] > div {
    background: #111827;
    border: 1px solid #29364a;
    border-radius: 10px;
}

div[data-baseweb="select"] > div:hover {
    border-color: #3b82f6;
}

/* ============================================================
   DATAFRAME
   ============================================================ */

[data-testid="stDataFrame"] {
    border: 1px solid #263449;
    border-radius: 12px;
    overflow: hidden;
}

/* ============================================================
   INFO BOXES
   ============================================================ */

div[data-testid="stAlert"] {
    background: linear-gradient(145deg, #111c30, #0f172a);
    border: 1px solid rgba(96, 165, 250, 0.20);
    border-radius: 12px;
}

/* ============================================================
   TEXT
   ============================================================ */

p {
    color: #b8c4d6;
}

label {
    color: #cbd5e1 !important;
    font-weight: 600 !important;
}
</style>
""",
        unsafe_allow_html=True,
    )


    # ============================================================
    # POP-UP MODAL FUNCTION
    # ============================================================
    @st.dialog("📍 State Breakdown & Insights")
    def show_state_popup(target_state_name, category_type):

        st.subheader(f"{category_type}: {target_state_name}")

        st.write(
            f"Detailed market snapshot for **{target_state_name}**:"
        )

        state_df = df[df["State"] == target_state_name]

        if not state_df.empty:

            p_col1, p_col2 = st.columns(2)

            with p_col1:
                st.metric(
                    "Avg Price",
                    f"₹{state_df['Price (INR)'].mean():,.0f}"
                )

                st.metric(
                    "Avg Mileage",
                    f"{state_df['Mileage (km/l)'].mean():.1f} km/l"
                )

            with p_col2:
                st.metric(
                    "Avg Resale",
                    f"₹{state_df['Resale Price (INR)'].mean():,.0f}"
                )

                st.metric(
                    "Avg Engine",
                    f"{state_df['Engine Capacity (cc)'].mean():.0f} cc"
                )

            st.markdown("---")

            st.markdown("**🏍️ Top Models in this State:**")

            top_models = (
                state_df["Model"]
                .value_counts()
                .head(3)
                .index
                .tolist()
            )

            for m in top_models:
                st.markdown(f"- **{m}**")

        else:
            st.info("No detailed records found for this state.")


    # ============================================================
    # KPI CARD FUNCTION
    # ============================================================
    def render_kpi_card(icon, title, value):

        st.markdown(
            f"""
<div class="kpi-card">
<div class="kpi-icon-circle">{icon}</div>

<div class="kpi-content">
<div class="kpi-title">{title}</div>
<div class="kpi-value">{value}</div>
</div>
</div>
""",
            unsafe_allow_html=True,
        )


    # ============================================================
    # TITLE SECTION
    # ============================================================
    st.title("🗺️ State Analysis")

    st.caption(
        "REGIONAL MARKET INTELLIGENCE • INDIAN BIKE MARKET"
    )

    st.write(
        "Analyze bike sales across different Indian states. "
        "Compare average prices, resale values, mileage and "
        "fuel preferences to identify regional market trends."
    )

    st.divider()


    # ============================================================
    # KPI CALCULATIONS
    # ============================================================
    total_states = df["State"].nunique()

    top_state = df["State"].value_counts().idxmax()

    highest_price_state = (
        df.groupby("State")["Price (INR)"]
        .mean()
        .idxmax()
    )

    highest_resale_state = (
        df.groupby("State")["Resale Price (INR)"]
        .mean()
        .idxmax()
    )

    best_mileage_state = (
        df.groupby("State")["Mileage (km/l)"]
        .mean()
        .idxmax()
    )

    highest_engine_state = (
        df.groupby("State")["Engine Capacity (cc)"]
        .mean()
        .idxmax()
    )


    # ============================================================
    # REGIONAL OVERVIEW
    # ============================================================
    st.subheader("📊 Regional Market Overview")


    col1, col2, col3 = st.columns(3)


    with col1:

        render_kpi_card(
            "🗺️",
            "Total States",
            total_states
        )

        if st.button(
            "View Overview 🔍",
            key="btn_total_states"
        ):
            show_state_popup(
                top_state,
                "Top Active State Overview"
            )


    with col2:

        render_kpi_card(
            "🏆",
            "Top Selling State",
            top_state
        )

        if st.button(
            "View Details 🔍",
            key="btn_top_state"
        ):
            show_state_popup(
                top_state,
                "Top Selling Market"
            )


    with col3:

        render_kpi_card(
            "💰",
            "Highest Avg Price",
            highest_price_state
        )

        if st.button(
            "View Details 🔍",
            key="btn_high_price"
        ):
            show_state_popup(
                highest_price_state,
                "Highest Avg Price Market"
            )


    col4, col5, col6 = st.columns(3)


    with col4:

        render_kpi_card(
            "♻️",
            "Highest Resale",
            highest_resale_state
        )

        if st.button(
            "View Details 🔍",
            key="btn_high_resale"
        ):
            show_state_popup(
                highest_resale_state,
                "Highest Resale Market"
            )


    with col5:

        render_kpi_card(
            "⛽",
            "Best Mileage",
            best_mileage_state
        )

        if st.button(
            "View Details 🔍",
            key="btn_best_mileage"
        ):
            show_state_popup(
                best_mileage_state,
                "Best Mileage Market"
            )


    with col6:

        render_kpi_card(
            "⚙️",
            "Highest Engine",
            highest_engine_state
        )

        if st.button(
            "View Details 🔍",
            key="btn_high_engine"
        ):
            show_state_popup(
                highest_engine_state,
                "Highest Engine Capacity Market"
            )


    st.divider()


    # ============================================================
    # STATE SELECTOR
    # ============================================================
    st.subheader("🔎 Explore Specific State")


    state = st.selectbox(
        "Select State",
        options=sorted(df["State"].unique()),
        key="state_analysis_select",
    )


    selected_data = df[df["State"] == state]


    st.subheader(
        f"📍 {state} — Market Performance"
    )


    sc1, sc2, sc3, sc4 = st.columns(4)


    with sc1:

        render_kpi_card(
            "💰",
            "Avg Price",
            f"₹{selected_data['Price (INR)'].mean():,.0f}"
        )


    with sc2:

        render_kpi_card(
            "♻️",
            "Avg Resale",
            f"₹{selected_data['Resale Price (INR)'].mean():,.0f}"
        )


    with sc3:

        render_kpi_card(
            "⛽",
            "Avg Mileage",
            f"{selected_data['Mileage (km/l)'].mean():.1f} km/l"
        )


    with sc4:

        render_kpi_card(
            "⚙️",
            "Avg Engine",
            f"{selected_data['Engine Capacity (cc)'].mean():.0f} cc"
        )


    st.divider()


    # ============================================================
    # STATE-WISE SUMMARY TABLE
    # ============================================================
    st.subheader("📋 State-wise Market Summary")


    state_summary = (
        df.groupby("State")
        .agg({
            "Price (INR)": "mean",
            "Resale Price (INR)": "mean",
            "Mileage (km/l)": "mean",
        })
        .round(2)
        .reset_index()
    )


    state_summary = state_summary.rename(
        columns={
            "Price (INR)": "Average Price (INR)",
            "Resale Price (INR)": "Average Resale (INR)",
            "Mileage (km/l)": "Average Mileage (km/l)",
        }
    )


    st.dataframe(
        state_summary,
        use_container_width=True,
        hide_index=True
    )


    st.divider()


    # ============================================================
    # KEY MARKET INSIGHTS
    # ============================================================
    st.subheader("📌 Key Market Insights")


    insight_col1, insight_col2 = st.columns(2)


    with insight_col1:

        st.info(
            f"🏆 **Top Selling State**\n\n"
            f"### {top_state}"
        )

        st.info(
            f"💰 **Highest Average Price**\n\n"
            f"### {highest_price_state}"
        )

        st.info(
            f"♻️ **Highest Resale Value**\n\n"
            f"### {highest_resale_state}"
        )


    with insight_col2:

        st.info(
            f"⛽ **Best Mileage**\n\n"
            f"### {best_mileage_state}"
        )

        st.info(
            f"⚙️ **Highest Engine Capacity**\n\n"
            f"### {highest_engine_state}"
        )

        st.success(
            f"📍 **Currently Selected State**\n\n"
            f"### {state}"
        )

























elif opt == "About Project":

    st.markdown("""
<style>
.stApp {
    background: #0b1120;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* PAGE TITLE */
.about-heading {
    color: #ffffff;
    font-size: 38px;
    font-weight: 800;
    margin-bottom: 4px;
    letter-spacing: -0.5px;
}

.about-subtitle {
    color: #94a3b8;
    font-size: 16px;
    margin-bottom: 22px;
}

/* HERO CARD */
.about-box {
    background: linear-gradient(135deg, #172554 0%, #0f172a 100%);
    border: 1px solid #31518f;
    border-radius: 18px;
    padding: 32px;
    margin: 22px 0 28px 0;
    box-shadow: 0 12px 30px rgba(0,0,0,0.28);
    transition: 0.25s ease;
}

.about-box:hover {
    border-color: #4f7edb;
    transform: translateY(-2px);
}

.about-title {
    color: #ffffff;
    font-size: 30px;
    font-weight: 800;
    margin-bottom: 12px;
}

.about-text {
    color: #cbd5e1;
    font-size: 16px;
    line-height: 1.8;
}

/* INFORMATION CARDS */
.info-box {
    background: linear-gradient(145deg, #111827, #0f172a);
    border: 1px solid #263449;
    border-radius: 16px;
    padding: 25px;
    margin: 18px 0;
    box-shadow: 0 7px 20px rgba(0,0,0,0.18);
    transition: 0.25s ease;
}

.info-box:hover {
    border-color: #3b82f6;
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
}

.info-title {
    color: #ffffff;
    font-size: 21px;
    font-weight: 750;
    margin-bottom: 14px;
}

.info-text {
    color: #b8c4d6;
    font-size: 15px;
    line-height: 1.8;
}

/* TECHNOLOGY CARDS */
.tech-box {
    background: linear-gradient(145deg, #111827, #0f172a);
    border: 1px solid #29364a;
    border-radius: 14px;
    padding: 22px 10px;
    text-align: center;
    min-height: 90px;
    transition: 0.25s ease;
    box-shadow: 0 6px 18px rgba(0,0,0,0.15);
}

.tech-box:hover {
    border-color: #60a5fa;
    transform: translateY(-4px);
    box-shadow: 0 10px 24px rgba(0,0,0,0.25);
}

.tech-name {
    color: #60a5fa;
    font-size: 17px;
    font-weight: 750;
}

.tech-text {
    color: #94a3b8;
    font-size: 13px;
    margin-top: 7px;
}

/* SMALL ACCENT LINE */
.accent-line {
    width: 55px;
    height: 3px;
    background: linear-gradient(90deg, #3b82f6, #60a5fa);
    border-radius: 10px;
    margin: 8px 0 18px 0;
}
</style>
""", unsafe_allow_html=True)


    # PAGE HEADER

    st.markdown(
        '<div class="about-heading">📌 About Project</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="about-subtitle">Bike Sales India – Data Analysis & Visualization Dashboard</div>',
        unsafe_allow_html=True
    )

    st.divider()


    # HERO SECTION

    st.markdown("""
<div class="about-box">
<div class="about-title">🏍️ Bike Sales India</div>

<div class="accent-line"></div>

<div class="about-text">
An interactive data analysis and visualization dashboard
created to explore and understand the Indian bike market.
The project transforms raw bike data into meaningful
insights using statistics, charts and comparisons.
</div>
</div>
""", unsafe_allow_html=True)


    # ABOUT PROJECT

    st.markdown("""
<div class="info-box">
<div class="info-title">📖 About the Project</div>

<div class="accent-line"></div>

<div class="info-text">
<b>Bike Sales India</b> is a data analysis project focused on
understanding the Indian bike market.
<br><br>
The dashboard allows users to explore different bike brands,
models, prices, resale values, mileage, engine capacity and
state-wise data.
<br><br>
The main goal is to present bike data in a simple,
interactive and easy-to-understand format.
</div>
</div>
""", unsafe_allow_html=True)


    # PROJECT OBJECTIVE

    st.markdown("""
<div class="info-box">
<div class="info-title">🎯 Project Objective</div>

<div class="accent-line"></div>

<div class="info-text">
• Compare different bike brands<br>
• Analyze different bike models<br>
• Understand bike price ranges<br>
• Analyze resale values<br>
• Compare mileage and engine capacity<br>
• Explore state-wise bike data<br>
• Understand market trends through charts
</div>
</div>
""", unsafe_allow_html=True)


    # TECHNOLOGIES

    st.markdown("""
<div class="info-box">
<div class="info-title">🛠️ Technologies Used</div>

<div class="accent-line"></div>
</div>
""", unsafe_allow_html=True)


    t1, t2, t3, t4 = st.columns(4)


    with t1:
        st.markdown("""
<div class="tech-box">
<div class="tech-name">🐍 Python</div>
<div class="tech-text">Programming</div>
</div>
""", unsafe_allow_html=True)


    with t2:
        st.markdown("""
<div class="tech-box">
<div class="tech-name">🐼 Pandas</div>
<div class="tech-text">Data Analysis</div>
</div>
""", unsafe_allow_html=True)


    with t3:
        st.markdown("""
<div class="tech-box">
<div class="tech-name">📈 Plotly</div>
<div class="tech-text">Visualization</div>
</div>
""", unsafe_allow_html=True)


    with t4:
        st.markdown("""
<div class="tech-box">
<div class="tech-name">📊 Streamlit</div>
<div class="tech-text">Dashboard</div>
</div>
""", unsafe_allow_html=True)

# elif opt == "About Project":

#     # ============================================================
#     # 1. PROFESSIONAL GLOWY CSS STYLING
#     # ============================================================

#     st.markdown(
#         """
#         <style>

#         /* ========================================================
#            MAIN BACKGROUND
#            ======================================================== */

#         .stApp {
#             background:
#                 radial-gradient(
#                     circle at 10% 0%,
#                     rgba(37, 99, 235, 0.09),
#                     transparent 25%
#                 ),
#                 radial-gradient(
#                     circle at 95% 10%,
#                     rgba(124, 58, 237, 0.07),
#                     transparent 25%
#                 ),
#                 #060a12;

#             color: #e5e7eb;
#         }


#         /* ========================================================
#            MAIN CONTENT
#            ======================================================== */

#         .block-container {
#             padding-top: 2.2rem;
#             padding-bottom: 2rem;
#             max-width: 1250px;
#         }


#         /* ========================================================
#            PAGE TITLE
#            ======================================================== */

#         h1 {
#             color: #f8fafc !important;
#             font-size: 34px !important;
#             font-weight: 800 !important;
#             letter-spacing: -0.6px;

#             text-shadow:
#                 0 0 18px rgba(59, 130, 246, 0.18);
#         }


#         h2 {
#             color: #f1f5f9 !important;
#             font-size: 23px !important;
#             font-weight: 750 !important;
#             letter-spacing: -0.2px;
#         }


#         h3 {
#             color: #f8fafc !important;
#             font-size: 17px !important;
#             font-weight: 700 !important;
#         }


#         /* ========================================================
#            NORMAL TEXT
#            ======================================================== */

#         .stMarkdown p {
#             color: #9ca8ba;
#             font-size: 14.5px;
#             line-height: 1.75;
#         }


#         /* ========================================================
#            DIVIDER
#            ======================================================== */

#         hr {
#             border: none !important;
#             height: 1px !important;

#             background: linear-gradient(
#                 90deg,
#                 rgba(37, 99, 235, 0),
#                 rgba(59, 130, 246, 0.55),
#                 rgba(124, 58, 237, 0.40),
#                 rgba(37, 99, 235, 0)
#             ) !important;

#             box-shadow:
#                 0 0 8px rgba(59, 130, 246, 0.18);
#         }


#         /* ========================================================
#            PREMIUM CARDS
#            ======================================================== */

#         div[data-testid="stVerticalBlockBorderWrapper"] {

#             background:
#                 linear-gradient(
#                     145deg,
#                     rgba(15, 23, 42, 0.96),
#                     rgba(9, 14, 25, 0.98)
#                 );

#             border: 1px solid rgba(71, 85, 105, 0.38);

#             border-radius: 14px;

#             padding: 20px;

#             box-shadow:
#                 0 8px 25px rgba(0, 0, 0, 0.25),
#                 inset 0 1px 0 rgba(255, 255, 255, 0.025);

#             transition:
#                 transform 0.22s ease,
#                 border-color 0.22s ease,
#                 box-shadow 0.22s ease;
#         }


#         /* Card hover */

#         div[data-testid="stVerticalBlockBorderWrapper"]:hover {

#             transform: translateY(-2px);

#             border-color: rgba(59, 130, 246, 0.42);

#             box-shadow:
#                 0 12px 30px rgba(0, 0, 0, 0.34),
#                 0 0 18px rgba(37, 99, 235, 0.09),
#                 inset 0 1px 0 rgba(255, 255, 255, 0.035);
#         }


#         /* ========================================================
#            CARD HEADINGS
#            ======================================================== */

#         div[data-testid="stVerticalBlockBorderWrapper"] h3 {

#             color: #f8fafc !important;

#             margin-bottom: 7px !important;

#             text-shadow:
#                 0 0 10px rgba(96, 165, 250, 0.12);
#         }


#         /* ========================================================
#            METRIC CARDS
#            ======================================================== */

#         [data-testid="stMetric"] {

#             background:
#                 linear-gradient(
#                     145deg,
#                     #101827,
#                     #0a101d
#                 );

#             border: 1px solid rgba(51, 65, 85, 0.55);

#             border-radius: 12px;

#             padding: 16px 17px;

#             box-shadow:
#                 0 6px 18px rgba(0, 0, 0, 0.24);

#             transition:
#                 transform 0.2s ease,
#                 border-color 0.2s ease,
#                 box-shadow 0.2s ease;
#         }


#         [data-testid="stMetric"]:hover {

#             transform: translateY(-2px);

#             border-color: rgba(59, 130, 246, 0.45);

#             box-shadow:
#                 0 8px 22px rgba(0, 0, 0, 0.30),
#                 0 0 14px rgba(37, 99, 235, 0.10);
#         }


#         [data-testid="stMetricLabel"] {

#             color: #8b98ab !important;

#             font-size: 12px !important;

#             font-weight: 600 !important;

#             letter-spacing: 0.3px;
#         }


#         [data-testid="stMetricValue"] {

#             color: #f8fafc !important;

#             font-size: 22px !important;

#             font-weight: 800 !important;

#             letter-spacing: -0.3px;
#         }


#         /* ========================================================
#            BUTTONS
#            ======================================================== */

#         .stButton > button {

#             background:
#                 linear-gradient(
#                     135deg,
#                     #1d4ed8,
#                     #4338ca
#                 );

#             color: #ffffff;

#             border: 1px solid rgba(96, 165, 250, 0.30);

#             border-radius: 8px;

#             font-size: 13px;

#             font-weight: 650;

#             padding: 8px 17px;

#             box-shadow:
#                 0 4px 14px rgba(37, 99, 235, 0.16);

#             transition: all 0.2s ease;
#         }


#         .stButton > button:hover {

#             background:
#                 linear-gradient(
#                     135deg,
#                     #2563eb,
#                     #4f46e5
#                 );

#             border-color: rgba(96, 165, 250, 0.55);

#             transform: translateY(-1px);

#             box-shadow:
#                 0 6px 18px rgba(37, 99, 235, 0.25);

#             color: #ffffff;
#         }


#         /* ========================================================
#            SIDEBAR
#            ======================================================== */

#         section[data-testid="stSidebar"] {

#             background:
#                 linear-gradient(
#                     180deg,
#                     #11141d 0%,
#                     #0d1018 100%
#                 ) !important;

#             border-right: 1px solid rgba(51, 65, 85, 0.35);

#             box-shadow:
#                 5px 0 25px rgba(0, 0, 0, 0.15);
#         }


#         /* Sidebar links */

#         section[data-testid="stSidebar"] .nav-link {

#             color: #aab4c3 !important;

#             border-radius: 8px !important;

#             transition:
#                 background 0.2s ease,
#                 color 0.2s ease;
#         }


#         /* Sidebar hover */

#         section[data-testid="stSidebar"] .nav-link:hover {

#             background: rgba(59, 130, 246, 0.08) !important;

#             color: #ffffff !important;
#         }


#         /* Selected sidebar */

#         section[data-testid="stSidebar"] .nav-link-selected {

#             background:
#                 linear-gradient(
#                     90deg,
#                     #ef4444,
#                     #dc2626
#                 ) !important;

#             color: #ffffff !important;

#             font-weight: 700 !important;

#             box-shadow:
#                 0 4px 14px rgba(239, 68, 68, 0.20);

#             border: 1px solid rgba(248, 113, 113, 0.18);
#         }


#         /* ========================================================
#            SCROLLBAR
#            ======================================================== */

#         ::-webkit-scrollbar {
#             width: 7px;
#         }

#         ::-webkit-scrollbar-track {
#             background: #060a12;
#         }

#         ::-webkit-scrollbar-thumb {

#             background:
#                 linear-gradient(
#                     #334155,
#                     #475569
#                 );

#             border-radius: 10px;
#         }

#         ::-webkit-scrollbar-thumb:hover {
#             background: #64748b;
#         }


#         /* ========================================================
#            FOOTER / CAPTION
#            ======================================================== */

#         .stCaption {

#             color: #64748b !important;

#             font-size: 12px !important;

#             text-align: center;

#             letter-spacing: 0.2px;
#         }


#         /* ========================================================
#            MOBILE / SMALL SCREEN
#            ======================================================== */

#         @media (max-width: 900px) {

#             h1 {
#                 font-size: 28px !important;
#             }

#             h2 {
#                 font-size: 21px !important;
#             }

#             .block-container {
#                 padding-left: 1rem;
#                 padding-right: 1rem;
#             }
#         }

#         </style>
#         """,
#         unsafe_allow_html=True,
#     )


#     # ============================================================
#     # 2. PAGE TITLE
#     # ============================================================

#     st.title("📌 About Project")

#     st.write(
#         "Bike Sales India – Data Analysis & Visualization Dashboard"
#     )

#     st.divider()


#     # ============================================================
#     # 3. PROJECT INTRODUCTION
#     # ============================================================

#     with st.container(border=True):

#         st.subheader("🏍️ MotoVision India")

#         st.write(
#             "Bike Sales India is an interactive data analysis and "
#             "visualization project developed to explore the Indian "
#             "bike market."
#         )

#         st.write(
#             "The dashboard converts raw bike data into meaningful "
#             "insights using statistics, charts and comparisons."
#         )


#     # ============================================================
#     # 4. ABOUT THE PROJECT
#     # ============================================================

#     st.subheader("📖 About the Project")

#     with st.container(border=True):

#         st.write(
#             "This project focuses on analyzing different aspects of "
#             "the Indian bike market."
#         )

#         st.write(
#             "Users can explore brands, models, prices, resale values, "
#             "mileage, engine capacity and state-wise bike data."
#         )

#         st.write(
#             "The main purpose is to make large amounts of bike data "
#             "easy to understand through an interactive dashboard."
#         )


#     # ============================================================
#     # 5. PROJECT OBJECTIVE
#     # ============================================================

#     st.subheader("🎯 Project Objective")

#     with st.container(border=True):

#         st.write(
#             "The main objective of this project is to identify useful "
#             "patterns and trends in the Indian bike market."
#         )

#         st.write("The dashboard helps users to:")

#         st.write(
#             """
#             • Compare different bike brands and models  
#             • Analyze bike prices and price ranges  
#             • Study resale values  
#             • Compare mileage and engine capacity  
#             • Explore state-wise bike data  
#             • Understand market trends through visualizations
#             """
#         )


#     # ============================================================
#     # 6. DASHBOARD MODULES
#     # ============================================================

#     st.subheader("📊 Dashboard Modules")

#     c1, c2, c3 = st.columns(3)


#     with c1:

#         with st.container(border=True):

#             st.subheader("📊 Data Overview")

#             st.write(
#                 "Provides an overall summary of the bike dataset "
#                 "with important statistics and visualizations."
#             )


#     with c2:

#         with st.container(border=True):

#             st.subheader("🏢 Brand Analysis")

#             st.write(
#                 "Compare different bike brands and understand "
#                 "their market performance."
#             )


#     with c3:

#         with st.container(border=True):

#             st.subheader("⚙️ Model Analysis")

#             st.write(
#                 "Analyze and compare different bike models "
#                 "using important parameters."
#             )


#     c4, c5, c6 = st.columns(3)


#     with c4:

#         with st.container(border=True):

#             st.subheader("💰 Price Analysis")

#             st.write(
#                 "Explore bike prices and understand different "
#                 "price segments."
#             )


#     with c5:

#         with st.container(border=True):

#             st.subheader("♻️ Resale Analysis")

#             st.write(
#                 "Analyze resale prices and understand the "
#                 "value of different bikes."
#             )


#     with c6:

#         with st.container(border=True):

#             st.subheader("📍 State Analysis")

#             st.write(
#                 "Explore state-wise bike data and identify "
#                 "regional market patterns."
#             )


#     # ============================================================
#     # 7. TECHNOLOGIES USED
#     # ============================================================

#     st.subheader("🛠️ Technologies Used")

#     t1, t2, t3, t4, t5 = st.columns(5)


#     with t1:
#         st.metric(
#             "Language",
#             "Python"
#         )


#     with t2:
#         st.metric(
#             "Dashboard",
#             "Streamlit"
#         )


#     with t3:
#         st.metric(
#             "Charts",
#             "Plotly"
#         )


#     with t4:
#         st.metric(
#             "Data",
#             "NumPy"
#         )


#     with t5:
#         st.metric(
#             "Image",
#             "PIL"
#         )


#     # ============================================================
#     # 8. PROJECT OUTCOME
#     # ============================================================

#     st.subheader("🚀 Project Outcome")

#     with st.container(border=True):

#         st.write(
#             "This dashboard provides a simple and interactive way "
#             "to understand the Indian bike market."
#         )

#         st.write(
#             "Instead of manually analyzing raw data, users can "
#             "quickly compare brands, models, prices, resale values "
#             "and state-wise trends."
#         )

#         st.write(
#             "The project demonstrates how Python and Streamlit can "
#             "be used to convert raw data into useful visual insights."
#         )


#     # ============================================================
#     # 9. PROJECT HIGHLIGHTS
#     # ============================================================

#     st.subheader("✨ Project Highlights")

#     h1, h2, h3, h4 = st.columns(4)


#     with h1:

#         with st.container(border=True):

#             st.metric(
#                 "Analysis",
#                 "6+"
#             )

#             st.caption(
#                 "Major analytical sections"
#             )


#     with h2:

#         with st.container(border=True):

#             st.metric(
#                 "Visualization",
#                 "Interactive"
#             )

#             st.caption(
#                 "Charts and comparisons"
#             )


#     with h3:

#         with st.container(border=True):

#             st.metric(
#                 "Platform",
#                 "Web"
#             )

#             st.caption(
#                 "Streamlit dashboard"
#             )


#     with h4:

#         with st.container(border=True):

#             st.metric(
#                 "Focus",
#                 "India"
#             )

#             st.caption(
#                 "Indian bike market"
#             )


    # ============================================================
    # 10. DEVELOPER
    # ============================================================

    st.divider()

    st.caption(
        "👨‍💻 Developed by Jatin Gupta  |  "
        "Bike Sales India – Data Analysis & Visualization Project"
    )















#############llllllllaaaaasttttttttttt liiiiiinnnnneeeeeee........................
st.markdown("""
<hr>
<div style="text-align:center; color:#94A3B8; padding:15px;">
<h5>🏍 MotoVision India - Bike Sales India</h5>
<p>Developed by Jatin Gupta | BTECH CSE AI/ML 1st Year Project</p>
<p>© 2026 All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)

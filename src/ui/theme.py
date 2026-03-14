def apply_theme():

    import streamlit as st

    st.markdown(
        """
        <style>

        /* MAIN APP BACKGROUND */
        .stApp {
            background: linear-gradient(180deg,#0f172a,#020617);
            color: #e2e8f0;
        }

        /* SIDEBAR */
        section[data-testid="stSidebar"] {
            background: #020617;
            border-right: 1px solid #1e293b;
        }

        /* SIDEBAR TEXT */
        section[data-testid="stSidebar"] * {
            color: #e2e8f0;
        }

        /* METRIC CARDS */
        div[data-testid="metric-container"] {
            background: #1e293b;
            border: 1px solid #334155;
            padding: 15px;
            border-radius: 12px;
            box-shadow: 0px 4px 14px rgba(0,0,0,0.4);
            transition: transform 0.2s ease;
        }

        div[data-testid="metric-container"]:hover {
            transform: translateY(-3px);
            border: 1px solid #6366f1;
        }

        /* BUTTON STYLE */
        .stButton button {
            background: linear-gradient(135deg,#6366f1,#4f46e5);
            color: white;
            border-radius: 10px;
            height: 3em;
            font-weight: 600;
            border: none;
            transition: all 0.2s ease;
        }

        .stButton button:hover {
            transform: translateY(-2px);
            box-shadow: 0px 4px 12px rgba(79,70,229,0.4);
        }

        /* INPUT BOX */
        .stTextInput input {
            background-color: #1e293b;
            color: #e2e8f0;
            border-radius: 8px;
            border: 1px solid #334155;
        }

        /* SELECT BOX */
        .stSelectbox div[data-baseweb="select"] {
            background-color: #1e293b;
            border-radius: 8px;
        }

        /* DATAFRAME STYLE */
        .stDataFrame {
            background-color: #1e293b;
            border-radius: 10px;
            border: 1px solid #334155;
        }

        /* HEADINGS */
        h1, h2, h3, h4 {
            color: #f8fafc;
            font-weight: 600;
        }

        /* DIVIDERS */
        hr {
            border-color: #1e293b;
        }

        /* SCROLLBAR */
        ::-webkit-scrollbar {
            width: 8px;
        }

        ::-webkit-scrollbar-thumb {
            background: #475569;
            border-radius: 4px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
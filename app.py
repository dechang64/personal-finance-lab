"""
Personal Finance Teaching Lab
==============================
Interactive Streamlit app for teaching personal finance concepts.
10 modules designed for classroom use.

Deployment:
    streamlit run app.py --server.port 8502 --server.headless true

Author: Dechang/Eileen collaboration
"""

import streamlit as st
import pandas as pd
import numpy as np
import sys, os

# ── Page Config ──
st.set_page_config(
    page_title="Personal Finance Teaching Lab",
    page_icon="💰",
    layout="wide",
)

# ── CSS ──
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem 2rem; border-radius: 12px; color: white;
        margin-bottom: 1.5rem;
    }
    .main-header h1 { margin: 0; font-size: 2rem; font-weight: 700; }
    .main-header p { margin: 0.5rem 0 0; opacity: 0.9; }
    .metric-card {
        background: white; border-radius: 8px; padding: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1); border-left: 4px solid #667eea;
    }
    .metric-card h3 { margin: 0; font-size: 0.9rem; color: #64748b; }
    .metric-card p { margin: 0.3rem 0 0; font-size: 1.8rem; font-weight: 700; color: #0f172a; }
    .stSlider > div > div > div { background: #667eea; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──
st.sidebar.title("💰 Personal Finance Lab")
st.sidebar.markdown("**Teaching tools for personal finance**")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Modules",
    [
        "🏠 Home",
        "📊 Budget Planner",
        "✨ Compound Interest",
        "👴 Retirement Planner",
        "🏠 Buy vs Rent",
        "📈 Portfolio Optimization",
        "💳 Credit Card Payoff",
        "🧾 Tax Calculator",
        "🎓 Student Loan Planner",
        "🏆 FICO Score Simulator",
        "🛡️ Insurance Needs",
    ],
    label_visibility="collapsed",
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**📚 Teaching Guide**\n
- Each module has a concept explanation + interactive calculator
- Suitable for undergrad / grad personal finance courses
- Students can export results as PDF (browser print)
- No installation required — runs in browser
""")

# ── Route to Pages ──
if page == "🏠 Home":
    from modules import home
    home.render()
elif page == "📊 Budget Planner":
    from modules import budget_planner
    budget_planner.render()
elif page == "✨ Compound Interest":
    from modules import compound_interest_mod
    compound_interest_mod.render()
elif page == "👴 Retirement Planner":
    from modules import retirement_planner
    retirement_planner.render()
elif page == "🏠 Buy vs Rent":
    from modules import buy_vs_rent_mod
    buy_vs_rent_mod.render()
elif page == "📈 Portfolio Optimization":
    from modules import portfolio_opt
    portfolio_opt.render()
elif page == "💳 Credit Card Payoff":
    from modules import credit_card
    credit_card.render()
elif page == "🧾 Tax Calculator":
    from modules import tax_calculator
    tax_calculator.render()
elif page == "🎓 Student Loan Planner":
    from modules import student_loan
    student_loan.render()
elif page == "🏆 FICO Score Simulator":
    from modules import fico_simulator
    fico_simulator.render()
elif page == "🛡️ Insurance Needs":
    from modules import insurance_needs
    insurance_needs.render()

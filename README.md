# 💰 Personal Finance Teaching Lab

Interactive Streamlit app for teaching personal finance concepts. 10 modules designed for classroom use.

## 🚀 Quick Start

```bash
pip install -r requirements.txt
streamlit run app.py
```

App opens at `http://localhost:8501`.

## 📋 Modules

| # | Module | Key Concept |
|---|--------|-------------|
| 1 | 📊 Budget Planner | 50/30/20 rule, cash flow tracking |
| 2 | ✨ Compound Interest | Time value of money, early-start advantage |
| 3 | 👴 Retirement Planner | Monte Carlo simulation, 4% rule |
| 4 | 🏠 Buy vs Rent | NPV comparison, opportunity cost |
| 5 | 📈 Portfolio Optimization | Markowitz efficient frontier, diversification |
| 6 | 💳 Credit Card Payoff | True cost of minimum payments |
| 7 | 🧾 Tax Calculator | Progressive brackets, marginal vs effective rate |
| 8 | 🎓 Student Loan Planner | Standard vs income-driven repayment |
| 9 | 🏆 FICO Score Simulator | 5 credit score factors, what-if scenarios |
| 10 | 🛡️ Insurance Needs | DIME method, term vs whole life |

## 🏗️ Architecture

```
personal-finance-lab/
├── app.py                  # Main Streamlit entry point
├── requirements.txt
├── .gitignore
├── utils/
│   ├── constants.py         # Tax brackets, asset returns, FICO factors
│   └── calculators.py       # 8 financial calculator functions
└── modules/
    ├── home.py
    ├── budget_planner.py
    ├── compound_interest_mod.py
    ├── retirement_planner.py
    ├── buy_vs_rent_mod.py
    ├── portfolio_opt.py
    ├── credit_card.py
    ├── tax_calculator.py
    ├── student_loan.py
    ├── fico_simulator.py
    └── insurance_needs.py
```

## ☁️ Deployment

### Streamlit Community Cloud (Free)
1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Select repo → deploy
4. App live at `https://[app-name].streamlit.app`

### Self-hosted
```bash
streamlit run app.py --server.port 8501 --server.headless true
```

## 📚 Teaching Flow

| Week | Modules | Topic |
|------|--------|-------|
| 1-2 | Budget + Compound Interest | Foundations |
| 3-4 | Credit Card + FICO | Credit fundamentals |
| 5-6 | Student Loan + Tax | Real-world obligations |
| 7-8 | Buy vs Rent + Portfolio | Investment decisions |
| 9-10 | Retirement + Insurance | Long-term planning |

Each module includes **Discussion Questions** for classroom engagement.

## 📄 License

MIT

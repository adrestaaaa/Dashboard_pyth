import streamlit as st

st.set_page_config(
    page_title = "Demo Dashboard",
    page_icon = "📌", #windows + titik untuk input emoji
    layout = 'wide'
)
import pandas as pd
import plotly.express as px


loan = pd.read_pickle('data_input/loan_clean')
loan['purpose'] = loan['purpose'].str.replace("_", " ")


st.markdown("<h1 style='text-align: center;'>Financial Insights Dashboard: Loan Performance & Trends</h1>", unsafe_allow_html=True)
st.divider()
st.header('Financial Analysis')
option = st.selectbox(
    "Select Loan Condition",("Good Loan", "Bad Loan"))
loan_condition = loan[loan['loan_condition'] == option]
#untuk pilihan good loan
if option ==  "Good Loan" :
 
    with st.container(border = True):
        tab_titles2 =[
            "Loans Amount Distribution",
            "Loans Amount Distribution by Purpose"
            
        ]
        tabs2 = st.tabs(tab_titles2)

        with tabs2[0] :
            st.header("Number of Loan Issued Over Time")
            fig = px.histogram(
                loan_condition, 
                x='loan_amount',  # Kolom yang akan digunakan untuk histogram
                color = 'term',
                nbins=30,   # Jumlah bin dalam histogram
                template='seaborn'
                )

            st.plotly_chart(fig)
        with tabs2[1] :
            st.header("Loan Amount Distribution by Purpose")
            fig = px.box(
            loan_condition,
                x ='purpose',
                y = 'loan_amount',
                color = 'term',
                template= 'seaborn',
                labels= {
                    'term' : 'Loan Term',
                    'loan_amount' : 'Loan Amount',
                    'purpose' : 'Purpose'
                }
            )

            st.plotly_chart(fig)
            
#untuk pilihan bad loan            
if option ==  "Bad Loan" :

    
    with st.container(border = True):
        tab_titles2 =[
            "Loans Amount Distribution",
            "Loans Amount Distribution by Purpose"
            
        ]
        tabs2 = st.tabs(tab_titles2)

        with tabs2[0] :
            st.header("Number of Loan Issued Over Time")
            fig = px.histogram(
                loan_condition, 
                x='loan_amount',  # Kolom yang akan digunakan untuk histogram
                color = 'term',
                nbins=30,   # Jumlah bin dalam histogram
                template='seaborn'
                )

            st.plotly_chart(fig)
        with tabs2[1] :
            st.header("Loan Amount Distribution by Purpose")
            fig = px.box(
            loan_condition,
                x ='purpose',
                y = 'loan_amount',
                color = 'term',
                template= 'seaborn',
                labels= {
                    'term' : 'Loan Term',
                    'loan_amount' : 'Loan Amount',
                    'purpose' : 'Purpose'
                }
            )

            st.plotly_chart(fig)



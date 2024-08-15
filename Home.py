import streamlit as st

st.set_page_config(
    page_title = "Demo Dashboard",
    page_icon = "📌", #windows + titik untuk input emoji
    layout = 'wide'
)

#st.title("Financial Insights Dashboard: Loan Performance & Trends") #untuk membuat title
st.markdown("<h1 style='text-align: center;'>Financial Insights Dashboard: Loan Performance & Trends</h1>", unsafe_allow_html=True)
st.divider()

st.sidebar.header("Dashboard Filters and Features") #untuk menuliskan pada sidebar
#dibawah untuk menuliskan dengan format markdown
st.sidebar.markdown(
    '''
    ### Features
- **Overview**: Provides a summary of key loan metrics.
- **Time-Based Analysis**: Shows trends over time and loan amounts.
- **Loan Performance**: Analyzes loan conditions and distributions.
- **Financial Analysis**: Examines loan amounts and distributions based on conditions.'''
    ) #untuk menuliskan pada sidebar

#st.header("Ini Adalah Header") #untuk membuat header


#st.text("Halo Gais !")
#st.text("halo lagi")

import pandas as pd
import plotly.express as px


loan = pd.read_pickle('data_input/loan_clean')
loan['purpose'] = loan['purpose'].str.replace("_", " ") #untuk inin sebaiknya diletakkan persis di bawah baca data
loan_head = loan.head(10)
#st.table(loan_head)

#ini untuk membuat bagian dibawah title 

container2 = st.container(border=True)
with st.container(height = 200):
    col1, col2 = st.columns(2)

    col1.metric('Total Loans',f"{loan['id'].count():,.0f}", help = "Total Number of Loans")
    col1.metric('Total Loan Amount',f"$ {loan['loan_amount'].sum():,.0f}", help = "Sum of All Loan Amount" )
    col2.metric('Average Interest Rate',f"{loan['interest_rate'].mean().round()} %" , help = "Percentage of the Loan Amount that the Borrower has to Pay")
    col2.metric('Average Loan Amount',f"$ {loan['loan_amount'].mean():,.0f}", help = "Average Interest Rate Accross All Loans")

#ini untuk deklarasi data
loan_date_count = loan.groupby(loan['issue_date'].dt.date)['loan_amount'].count()
loan_date_sum = loan.groupby('issue_date')['loan_amount'].sum()
loan_day_count = loan.groupby('issue_weekday')['loan_amount'].count()

#ini membuat line chart  yang loan issued over time dan total loan amount dan distribution of week (baris chart pertama)

with st.container(border = True):
    tab_titles =[
        "Loans Issued Over Time",
        "Loan Amount Over Time",
        "Issue Date Analysis"
    ]
    tabs = st.tabs(tab_titles)

#fig harus digunakan untuk memanggil chart plotly (gak harus fig, bisa ganti nama var)

    with tabs[0] :
        st.header("Number of Loan Issued Over Time")
        fig = px.line(
            loan_date_count,
            markers=True,
            title='Number of Loans Issued Over Time',
            labels={
                'issue_date': 'Issue Date',
                'value' : 'Number of Loans' #ubah Id menjadi value
                #'id': 'Number of Loans'
            }
             ).update_traces(marker={'color' :'purple'})
        st.plotly_chart(fig)
        

    with tabs[1] :
        st.header("Total Loan Amount Over Time")
        fig = px.line(
            loan_date_sum,
            markers=True,
            labels={
                'issue_date': 'Issue Date',
                'value' : 'Total Loan Amount' #ubah Id menjadi value
                #'id': 'Number of Loans'
            }
            ).update_traces(marker={'color' :'black'})
        st.plotly_chart(fig)

    with tabs[2] :
        st.header("Distribution of Loans by Day of Week")
        fig = px.bar(
            loan_day_count, 
            category_orders= {#mengatur urutan kategori (hari)
            'issue_weekday':['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']},
            title='Distribution of Loans by Day of the Week',
            labels={
                'value':'Number of Loans',
                'issue_weekday':'day of week'
            },
            template='seaborn'
            ).update_layout(showlegend=False) #menghilangkan Legend
        st.plotly_chart(fig)

# untuk chart baris ke dua
st.header("Loan Performance")
grade = loan['grade'].value_counts().sort_index()
reversed_colors = ['#046ccc','red']
with st.expander(""):
     col1, col2 = st.columns(2)
     with col1 :
        #pie chart
        fig = px.pie(
            loan,
            names='loan_condition',
            values='loan_amount',
            hole=0.3,  # Membuat donut chart
            template='seaborn'  # Menggunakan template warna
        )
        st.header("Distribution of Loans by Condition")
        
        st.plotly_chart(fig)
    

     with col2 :
        st.header("Distribution of Loans by Grade")
        fig = px.bar(
            grade,
            labels ={
                'value':'Number of loan',
            },
            template='seaborn',
            ).update_layout(showlegend=False)
        st.plotly_chart(fig)
st.divider()

#Chart Baris Ke tiga

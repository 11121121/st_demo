import streamlit as st
import numpy as numpy
import pandas as pd
import ploty.express as px

st.title('📈運動數據分析展示🏀')

data = pd.read_csv('sbdv_mid_exam.csv')

df = data[['weekly_training_hours', 'fitness_score']]

st.write('運動數據：')
st.dataframe(df)
st.write('線圖展示')
st.line_chart(df)
st.write('長條圖')
st.bar_chart(df)

st.title('Expender:')
with st.expander('點擊展開更多說明'):\
     st.write('這裡的資訊內容要點擊才能展開！')
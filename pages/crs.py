# streamlit_app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 경로 설정
csv_file_path = 'CRS_2022_data_partial.csv'

# 데이터 로드
@st.cache
def load_data():
    data = pd.read_csv(csv_file_path)
    return data

# 데이터 불러오기
data = load_data()

# 페이지 제목 설정
st.title('기부 국가 및 기관별 국제 원조 분석 대시보드')

# 사이드바 필터 설정
countries = st.sidebar.multiselect('국가 선택', options=data['DonorName'].unique(), default=data['DonorName'].unique()[:5])
years = st.sidebar.multiselect('연도 선택', options=data['Year'].unique(), default=data['Year'].unique())

# 데이터 필터링
filtered_data = data[(data['DonorName'].isin(countries)) & (data['Year'].isin(years))]

# 원조 금액 시각화
st.header('국가별 원조 금액 비교')
if not filtered_data.empty:
    donor_summary = filtered_data.groupby('DonorName')['USD_Commitment'].sum().sort_values(ascending=False)
    st.bar_chart(donor_summary)
else:
    st.write("선택한 조건에 해당하는 데이터가 없습니다.")

# 연도별 원조 추이 시각화
st.header('연도별 원조 금액 추이')
if not filtered_data.empty:
    year_summary = filtered_data.groupby('Year')['USD_Commitment'].sum()
    st.line_chart(year_summary)
else:
    st.write("선택한 조건에 해당하는 데이터가 없습니다.")

# 데이터 세부 정보 표시
st.header('프로젝트 세부 정보')
st.dataframe(filtered_data[['Year', 'DonorName', 'RecipientName', 'USD_Commitment', 'ProjectTitle']])


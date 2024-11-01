import streamlit as st
st.title('나의 첫 스트림릿 웹앱')
name = st.text_input('이름을 입력해주세요 : ')
mbti = st.selectbox('MBTI를 선택해주세요', ['ENTJ','INTP'])

if st.button('확인!') and name and mbti : 
  st.write(name+'님은 정말 '+mbti+' 같아보이시네요!')

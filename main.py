import streamlit as st

# 제목과 설명 추가
st.title('나의 첫 스트림릿 웹앱 🌟')
st.markdown("여러분의 MBTI 유형을 알아보고 그에 따른 성격 특징을 함께 알아보세요! 😄")

# 사용자 입력 받기
name = st.text_input('이름을 입력해주세요 👇:')
mbti = st.selectbox(
    'MBTI를 선택해주세요 🧠',
    ['ENTJ', 'INTP', 'INTJ', 'ENTP', 'INFJ', 'ENFJ', 'INFP', 'ENFP', 
     'ISTJ', 'ESTJ', 'ISFJ', 'ESFJ', 'ISTP', 'ESTP', 'ISFP', 'ESFP']
)

# MBTI에 대한 설명 데이터
mbti_descriptions = {
    'ENTJ': "ENTJ (대담한 통솔자)는 리더십과 전략적 사고의 대가! 🏆 "
            "조직을 효율적으로 이끌고 목표를 달성하는 데 집중합니다. "
            "이 유형은 다른 사람들을 격려하고 높은 기대치를 세워 도전하게 합니다.",
    'INTP': "INTP (논리적 사색가)는 창의적이고 독립적인 사고의 소유자입니다. 💡 "
            "그들은 복잡한 아이디어와 패턴을 탐구하며, 호기심 많고 탐구적입니다.",
    'INTJ': "INTJ (전략가)는 미래 지향적이고 매우 논리적인 유형입니다. 🧐 "
            "전략적으로 계획하며 자신의 목표를 실현시키기 위해 철저하게 준비합니다.",
    'ENTP': "ENTP (토론가)는 대담하고 논쟁을 즐기며 새로운 아이디어에 열려 있습니다. 🤔 "
            "기존의 사고방식을 뒤집어 보는 것을 즐기고 독창적인 해결책을 찾는 데 능숙합니다.",
    'INFJ': "INFJ (선의의 옹호자)는 이상주의적이고 매우 통찰력 있는 유형입니다. 🌱 "
            "타인의 필요를 잘 이해하며 따뜻한 마음으로 공감합니다.",
    'ENFJ': "ENFJ (정의로운 사회운동가)는 사교적이며 다른 사람들을 이끄는 힘이 있습니다. 🤝 "
            "타인에게 영감을 주고, 더 나은 사회를 만드는 것을 목표로 합니다.",
    'INFP': "INFP (중재자)는 깊은 감정을 가진 이상주의자입니다. 🌈 "
            "자신의 가치에 따라 행동하며 창의적이고 예술적인 표현을 좋아합니다.",
    'ENFP': "ENFP (활동가)는 열정적이고 자유로운 영혼입니다. 🌟 "
            "다양한 아이디어와 경험을 통해 세상을 탐구하고 사람들과 강하게 연결됩니다.",
    'ISTJ': "ISTJ (청렴한 관리자)는 성실하고 책임감이 강합니다. 📚 "
            "논리적이며 체계적인 접근으로 자신의 일을 꾸준히 수행합니다.",
    'ESTJ': "ESTJ (엄격한 경영자)는 조직적이고 계획적입니다. 📊 "
            "높은 생산성을 유지하며, 사람들을 이끌어 질서 정연하게 일을 처리합니다.",
    'ISFJ': "ISFJ (용감한 수호자)는 헌신적이고 세심합니다. 🛡️ "
            "타인을 돕는 것을 좋아하며, 차분하고 조용히 그들의 책임을 완수합니다.",
    'ESFJ': "ESFJ (배려심 깊은 호스트)는 사교적이고 협력적입니다. 🍀 "
            "다른 사람들과의 관계를 중요시하며, 주위 사람들을 돌보는 데에 탁월합니다.",
    'ISTP': "ISTP (만능 재주꾼)는 문제 해결을 즐기며 기술적 도전에 강합니다. 🔧 "
            "자유롭고 즉흥적인 성향으로 현장에서 행동하는 것을 좋아합니다.",
    'ESTP': "ESTP (모험을 즐기는 사업가)는 활동적이고 열정적입니다. 🚀 "
            "즉각적인 반응과 대담한 행동을 선호하며, 삶을 무대처럼 살아갑니다.",
    'ISFP': "ISFP (호기심 많은 예술가)는 부드럽고 창의적인 영혼입니다. 🎨 "
            "자연과 예술에 대한 감수성이 뛰어나고 따뜻한 마음을 가지고 있습니다.",
    'ESFP': "ESFP (자유로운 영혼의 연예인)는 에너지가 넘치고 사교적입니다. 🎉 "
            "순간을 즐기며, 사람들과 함께 있을 때 가장 행복합니다."
}

# 확인 버튼 및 결과 출력
if st.button('확인!') and name and mbti:
    st.success(f"{name}님은 정말 {mbti} 같아보이시네요! 🥳")
    st.markdown(f"### {mbti} 유형에 대한 설명")
    st.write(mbti_descriptions[mbti])

    # 추가적인 흥미 요소
    st.balloons()  # 성공 메시지와 함께 풍선 애니메이션
    st.snow()  # 화면에 눈 애니메이션 효과 추가 (시즌에 맞게 조절 가능)

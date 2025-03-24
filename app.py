import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import koreanize_matplotlib

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 페이지 설정
st.set_page_config(
    page_title="이력서 분석 시스템",
    page_icon="📊",
    layout="wide"
)

# 제목
st.title("📊 이력서 분석 및 처우 분석 시스템")

# 사이드바
st.sidebar.header("분석 옵션")
analysis_type = st.sidebar.selectbox(
    "분석 유형 선택",
    ["이력서 분석", "처우 분석"]
)

if analysis_type == "이력서 분석":
    st.header("이력서 분석")
    
    # 파일 업로드
    uploaded_file = st.file_uploader("이력서 데이터 파일을 업로드하세요 (CSV)", type=['csv'])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        # 데이터 미리보기
        st.subheader("데이터 미리보기")
        st.dataframe(df.head())
        
        # 기본 통계
        st.subheader("기본 통계")
        st.write(df.describe())
        
        # 시각화
        st.subheader("데이터 시각화")
        col1, col2 = st.columns(2)
        
        with col1:
            # 경력 분포
            if '경력' in df.columns:
                fig1 = plt.figure(figsize=(10, 6))
                sns.histplot(data=df, x='경력', bins=20)
                plt.title("경력 분포")
                st.pyplot(fig1)
        
        with col2:
            # 학력 분포
            if '학력' in df.columns:
                fig2 = plt.figure(figsize=(10, 6))
                df['학력'].value_counts().plot(kind='bar')
                plt.title("학력 분포")
                plt.xticks(rotation=45)
                st.pyplot(fig2)

else:
    st.header("처우 분석")
    
    # 샘플 데이터 생성
    np.random.seed(42)
    n_samples = 100
    data = {
        '연령': np.random.normal(35, 8, n_samples),
        '경력': np.random.normal(8, 4, n_samples),
        '연봉': np.random.normal(5000, 1000, n_samples)
    }
    df = pd.DataFrame(data)
    
    # 처우 분석 시각화
    st.subheader("연령대별 평균 연봉")
    fig = plt.figure(figsize=(10, 6))
    df['연령대'] = pd.cut(df['연령'], bins=[20, 30, 40, 50, 60], labels=['20-30', '31-40', '41-50', '51-60'])
    sns.boxplot(data=df, x='연령대', y='연봉')
    plt.title("연령대별 평균 연봉 분포")
    st.pyplot(fig)
    
    # 경력과 연봉의 상관관계
    st.subheader("경력과 연봉의 상관관계")
    fig = plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='경력', y='연봉')
    plt.title("경력과 연봉의 상관관계")
    st.pyplot(fig) 
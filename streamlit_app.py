streamlit
numpy
plotly
pandas
scipy
matplotlib
xarray
netCDF4
cartopy
shapely
pyproj
pydap
seaborn
pydeck
requests>=2.32
pyecharts>=2.0.5
streamlit-echarts>=0.4.0
Pillow
kaggle
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -----------------------------
# 앱 기본 설정
# -----------------------------
st.set_page_config(page_title="해수면 상승 통합 대시보드", layout="wide")
st.title("🌊 해수면 상승 통합 대시보드")

st.markdown("""
이 대시보드는 전세계 및 한국 해수면 상승 현황을 시각화하고, 
해수면 상승으로 인한 피해 사례를 정리하여 보여줍니다.

데이터 출처:
- NASA/JPL Global Mean Sea Level (GMSL)
- NOAA Tide Gauge Data
- 국립해양조사원 한국 연안 해수면 데이터
""")

# -----------------------------
# 데이터 로딩 (예시용: 랜덤 데이터)
# 실제 구현시 NASA/NOAA/국립해양조사원 데이터 API 또는 CSV 연결
# -----------------------------
dates = pd.date_range(start="1993", end="2025", freq="Y")
gmsl = np.cumsum(np.random.normal(0.3, 0.1, len(dates)))  # 전세계 평균 해수면 상승 (mm)
korea_sea = np.cumsum(np.random.normal(0.25, 0.1, len(dates)))  # 한국 연안 해수면 상승 (mm)

# 데이터프레임 생성
df_global = pd.DataFrame({"연도": dates.year, "전세계 해수면(mm)": gmsl})
df_korea = pd.DataFrame({"연도": dates.year, "한국 해수면(mm)": korea_sea})

# -----------------------------
# 레이아웃 구성
# -----------------------------
tab1, tab2, tab3 = st.tabs(["🌍 전세계 현황", "🇰🇷 한국 현황", "📑 피해 사례 보고서"])

# -----------------------------
# 탭 1: 전세계 해수면 상승
# -----------------------------
with tab1:
    st.subheader("전세계 평균 해수면 상승 추세")
    fig_global = px.line(df_global, x="연도", y="전세계 해수면(mm)", title="전세계 해수면 상승 (NASA/JPL)")
    st.plotly_chart(fig_global, use_container_width=True)

    st.info("1993년 이후 전세계 평균 해수면은 꾸준히 상승하고 있습니다. (예시 데이터)")

# -----------------------------
# 탭 2: 한국 해수면 상승
# -----------------------------
with tab2:
    st.subheader("한국 연안 해수면 상승 추세")
    fig_korea = px.line(df_korea, x="연도", y="한국 해수면(mm)", title="한국 해수면 상승 (국립해양조사원)")
    st.plotly_chart(fig_korea, use_container_width=True)

    st.warning("한국 연안 역시 전세계 평균과 유사한 상승 추세를 보이고 있습니다. (예시 데이터)")

# -----------------------------
# 탭 3: 피해 사례 보고서
# -----------------------------
with tab3:
    st.subheader("해수면 상승으로 인한 피해 사례")

    st.markdown("""
    ### 📌 대표적 피해 사례
    - **방글라데시**: 해수면 상승으로 인한 대규모 홍수 및 농경지 손실
    - **몰디브**: 국토의 상당 부분이 침수 위험에 노출
    - **한국 인천/부산 연안**: 항만, 해안가 저지대 침수 가능성 증가

    ### 🌍 영향 요약
    - 연안 도시 인프라 침수 위험
    - 농업 및 식수 자원 위협
    - 해안 생태계 변화 및 생물 다양성 감소

    ### 🔮 시사점
    기후변화 대응 및 연안 방재 인프라 강화가 필요합니다.
    """)


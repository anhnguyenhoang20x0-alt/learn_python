import streamlit as st
import pandas as pd

#1 tạo bẳng
st.title(" Dashboard Phân Tích Nhân Sự")

#2 khai báo dữ liệu
data = [
    {"name": "anh" ,"lương": 20000, "phòng ban":"IT"},
    {"name": "duy" ,"lương": 28000, "phòng ban":"HC"},
    {"name": "linh" ,"lương": 10000, "phòng ban":"VC"},
    {"name": "tâm" ,"lương": 26000, "phòng ban":"AC"},
    {"name": "trân" ,"lương": 12000, "phòng ban":"H1"},
]

# gan du lieu
df = pd.DataFrame(data)

#logic 

def clau_bonus(row):
    if row["lương"] >20000:
        return row["lương"] * 0.1
    elif row["phòng ban"] == "IT":
        return row["lương"] *0.15
    else:
        return row["lương"] *0.05

df["bonus"] = df.apply(clau_bonus, axis=1)

#muc luong chọn
st.sidebar.header("bộ lọc")
muc_luong_chon = st.sidebar.slider("chọn mức luong: ", 0 , 50000, 10000) 
chon_phong_ban = st.sidebar.selectbox("chọn phòng ban", ["all","IT","HC","VC","AC","H1"])

if chon_phong_ban == "all":
    df_loc = df[(df["lương"] >= muc_luong_chon)]
else: 
    df_loc = df[(df["lương"] >= muc_luong_chon) & (df["phòng ban"] == chon_phong_ban)]

#4 hiển thị dashboard
st.subheader("bảng tính")
st.dataframe(df_loc)

st.subheader("biểu đồ")
st.bar_chart(df_loc, x="name" ,y="lương")

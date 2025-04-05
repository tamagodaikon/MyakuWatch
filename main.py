import streamlit as st
import pandas as pd

# タイトルと説明
st.title("MyakuWatch - 万博アプリ監視テスト")
st.write("これはStreamlitアプリのテスト画面です。")

# サンプルデータ（疑似的な検索結果）
data = [
    {"アプリ名": "EXPO 2025 Visitors", "開発者": "EXPO協会", "危険度": "安全"},
    {"アプリ名": "EXPO Guide 2025", "開発者": "unknown_dev", "危険度": "注意"},
    {"アプリ名": "Osaka EXPO", "開発者": "怪しい開発者", "危険度": "危険"},
]

# データフレーム化して表示
df = pd.DataFrame(data)
st.dataframe(df)

# フィルター付きセレクトボックス
option = st.selectbox("危険度でフィルター", ["すべて", "安全", "注意", "危険"])

if option != "すべて":
    filtered = df[df["危険度"] == option]
else:
    filtered = df

st.subheader("フィルター結果")
st.table(filtered)

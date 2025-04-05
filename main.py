import streamlit as st
from google_play_scraper import search

# タイトル
st.title("MyakuWatch - 万博アプリ監視ツール")
st.write("万博関連アプリを検索し、不審なものを検出します。")

# キーワード検索（固定 or 入力可能）
query = st.text_input("検索キーワード", "expo 2025")

# 検索ボタン
if st.button("アプリを検索"):
    results = search(query, lang="ja", country="jp", n=10)

    for app in results:
        st.markdown(f"### {app['title']}")
        st.write(f"📦 パッケージ名：{app['appId']}")
        st.write(f"🧑‍💻 開発者：{app['developer']}")
        st.write(f"⭐ 評価：{app['score']}")
        st.write(f"📝 説明：{app['description'][:150]}...")
        st.write("---")

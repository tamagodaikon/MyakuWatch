import streamlit as st
from google_play_scraper import search
import pandas as pd

st.set_page_config(page_title="万博アプリ監視", layout="wide")
st.title("🔍 万博関連アプリ検索ツール")
st.write("キーワードに基づき、Google Playから万博関連アプリを検索して一覧表示します。")

# キーワード入力
query = st.text_input("検索キーワードを入力", value="expo 2025")

# 検索実行
if st.button("検索する"):
    with st.spinner("Google Playを検索中…"):
        try:
            results = search(query, lang="ja", country="jp")
            results = results[:10]  # 上位10件に制限

            apps = []
            for app in results:
                app_id = app["appId"]
                play_url = f"https://play.google.com/store/apps/details?id={app_id}"
                apk_url = f"https://apkcombo.com/installer/?package={app_id}"

                apps.append({
                    "アプリ名": app["title"],
                    "パッケージ名": app_id,
                    "開発者": app["developer"],
                    "評価": app.get("score", "不明"),
                    "Google Playリンク": play_url,
                    "APKダウンロードリンク": apk_url
                })

            df = pd.DataFrame(apps)

            st.subheader("検索結果")
            st.dataframe(df, use_container_width=True)

            st.caption("※ APKComboのリンクから非公式にAPKを取得できます。自己責任でご利用ください。")

        except Exception as e:
            st.error(f"検索中にエラーが発生しました：{e}")

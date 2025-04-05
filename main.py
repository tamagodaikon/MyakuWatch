import streamlit as st
from google_play_scraper import search
import pandas as pd

st.title("万博関連アプリ監視＋APKダウンロード")

query = st.text_input("検索キーワードを入力", value="expo 2025")

if st.button("検索する"):
    with st.spinner("検索中..."):
        try:
            results = search(query, lang="ja", country="jp")
            results = results[:10]  # 上位10件

            data = []
            for app in results:
                app_id = app["appId"]
                google_url = f"https://play.google.com/store/apps/details?id={app_id}"
                apkcombo_url = f"https://apkcombo.com/installer/?package={app_id}"

                data.append({
                    "アプリ名": app["title"],
                    "パッケージ名": app_id,
                    "開発者": app["developer"],
                    "評価": app.get("score", "不明"),
                    "Google Play": f"[リンク]({google_url})",
                    "APKダウンロード": f"[📥 ダウンロード]({apkcombo_url})"
                })

            df = pd.DataFrame(data)
            st.markdown("### 検索結果（リンク付き）")
            st.write("APKCombo を経由した非公式ダウンロードリンクが含まれます。自己責任でご利用ください。")
            st.write(df.to_markdown(index=False), unsafe_allow_html=True)

        except Exception as e:
            st.error(f"エラー：{e}")

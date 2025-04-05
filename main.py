import streamlit as st
from google_play_scraper import search
import pandas as pd

# --- UI部 ---
st.set_page_config(page_title="万博アプリ検索", layout="wide")
st.title("🔍 万博関連アプリ検索ツール（Google Play）")
st.write("Google Playから『expo』『万博』『2025』などのキーワードでアプリを自動検索します。")

# --- 検索キーワード入力（初期値あり） ---
keywords = st.text_input("検索キーワード", "expo 2025")

# --- 検索ボタン ---
if st.button("検索する"):
    with st.spinner("検索中..."):
        try:
            # アプリ検索（最大20件取得）
            results = search(
                keywords,
                lang="ja",
                country="jp"
            )

            # 情報を整形してDataFrame化
            data = []
            for app in results:
                data.append({
                    "アプリ名": app["title"],
                    "パッケージ名": app["appId"],
                    "開発者": app["developer"],
                    "評価": app.get("score", "不明"),
                    "インストール数": app.get("installs", "不明"),
                    "Google Playリンク": f"https://play.google.com/store/apps/details?id={app['appId']}"
                })

            df = pd.DataFrame(data)

            # 表示
            st.success(f"{len(df)} 件のアプリが見つかりました。")
            st.dataframe(df, use_container_width=True)

            # CSVダウンロード
            csv = df.to_csv(index=False)
            st.download_button("📥 CSVでダウンロード", data=csv, file_name="expo_apps.csv", mime="text/csv")

        except Exception as e:
            st.error(f"検索中にエラーが発生しました：{e}")

"""
下载完整 Superstore 数据的示例脚本（仅示例：尝试从公开位置下载）。
如果你有本地数据来源，请替换 URL 或直接上传数据到 data/ 目录。
"""
import os
import requests

URL = "https://github.com/plotly/datasets/raw/master/superstore.csv"  # 示例公开 mirror
OUT = os.path.join(os.path.dirname(__file__), "superstore_full.csv")

def download():
    print(f"Downloading from {URL} ...")
    r = requests.get(URL, stream=True)
    r.raise_for_status()
    with open(OUT, "wb") as f:
        for chunk in r.iter_content(1024*16):
            f.write(chunk)
    print("Saved to", OUT)

if __name__ == "__main__":
    download()

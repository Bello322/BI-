# BI 数据可视化（Superstore 示例）

## 项目简介
这是一个面向数据分析师与 BI 工程师的示例项目，使用公开的 Superstore 销售数据，演示从数据清洗、探索性分析（EDA）、可视化生成到为 Power BI 准备数据的一整套工作流程。主要使用 Python 的 pandas 进行数据处理，Pyecharts 与 Matplotlib 用于生成可视化（HTML/PNG），并提供在 Power BI 中复现报表的详细指南。

该项目适合用于：
- 简历/作品集示例：展示数据分析能力、可视化设计与商业洞察；
- 面试演示：快速展示你对数据处理、KPI 构建与报表产出的流程理解；
- 学习材料：学习如何将 Python 可视化输出与 Power BI 报表结合。

## 关键特性
- 数据清洗与指标计算的 Jupyter Notebook（notebooks/analysis.ipynb）；
- 可生成的静态可视化报表（Pyecharts 渲染为 HTML）；
- 支持将清洗后的 CSV 导入 Power BI 并提供 DAX 示例；
- 提供示例脚本 scripts/generate_reports.py 用于批量渲染与导出；
- 小样本数据（data/superstore_sample.csv）与下载脚本（data/download_data.py）。

## 目录结构
- README.md — 本文档（详细使用说明）；
- requirements.txt — Python 依赖；
- data/
  - superstore_sample.csv — 小样本数据（用于快速演示）；
  - download_data.py — 下载完整 Superstore 数据的脚本（可选）；
- notebooks/
  - analysis.ipynb — 数据清洗、EDA、可视化示例；
- scripts/
  - generate_reports.py — 生成 HTML 报表并导出筛选后的 CSV；
- docs/
  - powerbi_guide.md — Power BI 导入、建模与 DAX 指南；
- .gitignore — 忽略规则。

## 依赖库与用途（详细说明）
下面列出本项目中使用的主要 Python 库，并说明它们在项目中的作用以及常见用法示例。

- pandas（用于数据加载、清洗与聚合）
  - 作用：高效读写 CSV/Excel，进行数据清洗、处理缺失值、类型转换、按时间/分类分组聚合（groupby）以及计算 KPI（如总销售、总利润）。
  - 在项目中的使用点：notebooks/analysis.ipynb、scripts/generate_reports.py 用 pandas 读取数据、转换 Order Date 为 datetime、按月/分类汇总销售金额。
  - 示例：
    ```python
    import pandas as pd
    df = pd.read_csv('data/superstore_sample.csv')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    monthly_sales = df.groupby(pd.Grouper(key='Order Date', freq='M'))['Sales'].sum()
    ```

- pyecharts（用于生成交互式 HTML 可视化）
  - 作用：创建交互式图表（折线图、柱状图、饼图、地图等），并渲染为独立的 HTML 页面，便于分享与嵌入网页。支持丰富的交互配置（tooltip、legend、数据缩放等）。
  - 在项目中的使用点：scripts/generate_reports.py 与 notebooks 中生成 monthly_sales.html、sales_by_category.html 等交互可视化文件。
  - 示例：
    ```python
    from pyecharts.charts import Line
    from pyecharts import options as opts
    line = (Line().add_xaxis(months).add_yaxis('Monthly Sales', values)
            .set_global_opts(title_opts=opts.TitleOpts(title='Monthly Sales')))
    line.render('monthly_sales.html')
    ```

- matplotlib（用于静态图与图片导出）
  - 作用：生成高质量的静态图像（PNG/SVG），适合放入报告或作为备选静态快照。对细节自定义能力强（字体、图片大小、子图布局）。
  - 在项目中的使用点：notebooks/analysis.ipynb 演示如何使用 matplotlib 绘制静态图并保存为 PNG（作为报告或面试展示用图）。
  - 示例：
    ```python
    import matplotlib.pyplot as plt
    plt.plot(x, y)
    plt.title('Monthly Sales')
    plt.savefig('monthly_sales.png', dpi=300)
    ```

- jupyter（Notebook 环境）
  - 作用：交互式数据分析环境，方便逐步展示数据清洗、可视化与分析结论，易于分享（.ipynb）并重现实验步骤。
  - 在项目中的使用点：notebooks/analysis.ipynb 为主要教学与演示稿，用于展示数据处理步骤和可视化结果。

- openpyxl（读写 Excel）
  - 作用：读写 Excel 文件（.xlsx），在需要将分析结果导出为 Excel 报表或从 Excel 导入数据时使用。
  - 在项目中的使用点：可以在 Notebook 中把聚合结果导出为 Excel 以便于业务团队打开与再加工。
  - 示例：
    ```python
    df_agg.to_excel('summary.xlsx', index=False)
    ```

- requests（用于下载外部数据）
  - 作用：通过 HTTP 请求下载远程数据文件（CSV/ZIP 等）。
  - 在项目中的使用点：data/download_data.py 使用 requests 从公开镜像下载完整 Superstore 数据。
  - 示例：
    ```python
    import requests
    r = requests.get(url)
    open('superstore_full.csv', 'wb').write(r.content)
    ```

- 其他说明
  - 本项目的 requirements.txt 明确列出了主依赖：pandas、pyecharts、matplotlib、jupyter、openpyxl。pandas 等库会隐式依赖 numpy 等常用科学计算库（会随 pip install 自动安装）。
  - 若你扩展项目（例如加入地理可视化或机器学习），可能还需要安装 geopandas、scikit-learn、folium、plotly 或 streamlit 等库。

## 环境与依赖安装
建议使用虚拟环境：

macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 快速上手
1. 克隆仓库并进入目录：

```bash
git clone https://github.com/Bello322/BI-.git
cd BI-
```

2. 安装依赖并打开 Notebook：

```bash
pip install -r requirements.txt
jupyter notebook notebooks/analysis.ipynb
```

3. 或运行脚本生成报表：

```bash
python scripts/generate_reports.py --input data/superstore_sample.csv --output reports/
```

## 贡献与下一步
如果你需要我把 README 同步为英文/双语版本、在 README 中加入示例图片或把 requirements.txt 固定为特定版本号（如 pandas==1.5.3），我可以继续更新并提交。

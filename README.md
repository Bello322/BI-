# BI 数据可视化（Superstore 示例）

简介
- 一个基于 Python（Pyecharts + Matplotlib）的 BI 可视化示例项目，提供数据清洗、交互式报表导出（HTML/PNG）以及 Power BI 导入指南。

目录结构
- data/：示例数据与下载脚本
- notebooks/：Jupyter Notebook（EDA 与可视化示例）
- scripts/：渲染/导出脚本
- docs/：Power BI 使用指南
- requirements.txt：依赖
- README.md：本文件

快速开始（本地）
1. 创建并激活虚拟环境（推荐）
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate     # Windows

2. 安装依赖
   pip install -r requirements.txt

3. 运行 Notebook（可视化探索）
   jupyter notebook notebooks/analysis.ipynb

4. 生成 HTML 报表示例
   python scripts/generate_reports.py --input data/superstore_sample.csv --output reports/

Power BI
- docs/powerbi_guide.md 包含将 CSV 导入 Power BI、建立模型与示例 DAX。

数据
- data/superstore_sample.csv 为小样本（用于快速演示），如需完整数据请运行 data/download_data.py。

许可证
- MIT

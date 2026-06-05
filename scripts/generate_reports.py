"""
基于 Pyecharts + Matplotlib 生成 HTML 报表与导出筛选后的 CSV。
用法:
    python scripts/generate_reports.py --input data/superstore_sample.csv --output reports/
"""
import os
import argparse
import pandas as pd
from pyecharts.charts import Line, Bar, Pie
from pyecharts import options as opts

def ensure_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)

def sales_time_series(df, out_html):
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    ts = df.groupby(pd.Grouper(key='Order Date', freq='M'))['Sales'].sum().reset_index()
    x = ts['Order Date'].dt.strftime('%Y-%m')
    y = ts['Sales'].round(2).tolist()

    line = (
        Line()
        .add_xaxis(x.tolist())
        .add_yaxis("Monthly Sales", y)
        .set_global_opts(title_opts=opts.TitleOpts(title="Monthly Sales"))
    )
    line.render(out_html)
    print("Wrote", out_html)

def category_bar(df, out_html):
    cat = df.groupby('Category')['Sales'].sum().reset_index()
    bar = (
        Bar()
        .add_xaxis(cat['Category'].tolist())
        .add_yaxis("Sales", cat['Sales'].round(2).tolist())
        .set_global_opts(title_opts=opts.TitleOpts(title="Sales by Category"))
    )
    bar.render(out_html)
    print("Wrote", out_html)

def export_filtered_csv(df, out_csv):
    df.to_csv(out_csv, index=False)
    print("Exported CSV:", out_csv)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    ensure_dir(args.output)
    df = pd.read_csv(args.input)
    # 示例：生成月度销售与类别条形图
    sales_time_series(df, os.path.join(args.output, "monthly_sales.html"))
    category_bar(df, os.path.join(args.output, "sales_by_category.html"))
    export_filtered_csv(df, os.path.join(args.output, "filtered_data.csv"))

if __name__ == "__main__":
    main()

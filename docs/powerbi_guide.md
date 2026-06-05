# Power BI 导入与可视化指南（Superstore）

1) 准备数据
- 使用 data/filtered_data.csv（或 data/superstore_full.csv 若已下载）。
- 在 Power BI Desktop 中选择「Get Data」-> CSV -> 选择文件。

2) 建模建议
- 将 Order Date 设置为 Date 类型，创建 Calendar 表（按月/季度/年汇总）。
- 关系：Calendar[Date] -> Orders[Order Date]（一对多）。

3) 推荐度量 (DAX)
- Total Sales =
    SUM('Orders'[Sales])

- Total Profit =
    SUM('Orders'[Profit])

- Sales YoY =
    CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Calendar'[Date]))

- Profit Margin =
    DIVIDE([Total Profit], [Total Sales], 0)

4) 可视化建议
- KPI 卡：Total Sales、Total Profit、Profit Margin
- 折线图：按月 Sales 与 YoY 比较
- 条形图：Category / Sub-Category 的 Sales 排序
- 地图：按 State 或 City 可视化（需要经纬/或内置地理解析）

5) 交互与下钻
- 使用切片器（Slicers）按 Region / Category / Segment 过滤。
- 使用 Drill Down 在 Region -> State -> City 之间下钻。

6) 导出
- 可以直接从 Power BI 导出报表页面为 PDF 或图像；也可将筛选后的明细导出为 CSV（右键表格 -> Export data）。

7) 进一步自动化
- 若你使用 Power BI Service，可配置刷新计划（需将数据放到可访问位置，如 Azure Blob / OneDrive）。

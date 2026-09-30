# 三环集团模型 v2 生成脚本

`三环集团_财务估值模型_v2_20260930.xlsx` 由本目录脚本生成，所有公式都写在 Excel 里。只有需要重算“敏感性分析”和“情景对比”两张静态表时，才需要运行这些脚本。

- `pipeline.sh`：依次执行标定 → 构建 → LibreOffice 重算 → 敏感性引擎 → 最终构建 → 重算。
- `build_v2.py`：生成各明细表与三表；`assumptions_v2.py`：生成假设表；`extras_v2.py`：生成估值、校验、封面等表；`sens_render.py`：把敏感性结果写入表格。
- `sens_v2.py`：通过 LibreOffice UNO 逐项改变冲击单元、整表重算，输出 `sens_results.json`。
- `hist_detail.py`：从 `extract/` 读取已核实的年报、半年报附注数据（金额单位为元）。
- `calibrate.py`：标定毛利率假设所隐含的生产人工与生产折旧。

运行前需要：Python 3（openpyxl），LibreOffice（含 Python UNO）；另外需把 Wind 导出的利润表、资产负债表、现金流量表和单季利润表放在 `src/e66ff817-____/`。

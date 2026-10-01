# -*- coding: utf-8 -*-
"""Render the 财务汇总 / Summary_EN sheets of the recalculated model as chart-style HTML tables (CN and EN)."""
import sys, openpyxl
sys.path.insert(0, '.')
from gen import frame as frame_cn
import importlib.util
spec = importlib.util.spec_from_file_location('gen_en', 'gen_en.py'); 
W = 1440
MODEL = sys.argv[1]
wb = openpyxl.load_workbook(MODEL, data_only=True)
wbf = openpyxl.load_workbook(MODEL)

def fmtv(v, nf):
    if v is None or v == '':
        return ''
    if isinstance(v, str):
        return v
    if abs(v) < 0.05 and '%' not in nf:
        return '–'
    if '%' in nf:
        return f"{v*100:.1f}%"
    if 'x' in nf:
        return f"{v:.1f}x"
    if nf.startswith('0.00') or nf.startswith('#,##0.00'):
        return f"{v:.2f}"
    if nf.startswith('0;') or nf.startswith('#,##0;'):
        return f"{v:,.0f}"
    return f"{v:,.0f}" if abs(v) >= 100 else f"{v:,.1f}"

def table_html(sheet, lang):
    ws, wf = wb[sheet], wbf[sheet]
    cols = list(range(3, 11))
    head = [ws.cell(4, c).value for c in cols]
    css = """
.tb{position:absolute;left:46px;top:150px;width:1348px;border-collapse:collapse;font-size:14.5px}
.tb th{background:#1F3864;color:#fff;font-weight:700;padding:6px 4px;text-align:right}
.tb th.l{text-align:left;padding-left:10px}
.tb td{padding:3.2px 5px;text-align:right;border-bottom:1px solid #E3E7EF;white-space:nowrap}
.tb td.l{text-align:left;padding-left:10px;color:#1F2933}
.tb td.e{background:#F4F5FB}
.tb td.sp,.tb th.sp{background:#fff;width:8px;padding:0;border:none}
.tb tr.sec td{background:#E8EAF7;color:#2E2A9A;font-weight:700;text-align:left;padding:5px 10px;border-bottom:2px solid #3B2FB8}
.tb tr.b td{font-weight:700}
.tb td.ind{padding-left:24px;color:#4A5563}
.grp{position:absolute;top:126px;font-size:14px;font-weight:700;color:#2E2A9A}
"""
    h = ['<table class="tb"><tr><th class="l" style="width:420px">%s</th>' % head_lab(lang)]
    for i, c in enumerate(cols):
        h.append(f'<th>{head[i]}</th>')
    h.append('</tr>')
    for r in range(5, ws.max_row + 1):
        lab = ws.cell(r, 1).value
        if lab is None:
            continue
        if ws.cell(r, 1).fill.fgColor.rgb in ('FFD9E1F2', '00D9E1F2') or (isinstance(lab, str) and lab[:2] in ('一、', '二、', '三、', '四、', '五、', 'I.', 'II', 'IV', 'V.') and ws.cell(r, 3).value is None and ws.cell(r, 12).value is None):
            lab = lab.split('（季度')[0].split(' (quarterly')[0]
            h.append(f'<tr class="sec"><td colspan="9">{lab}</td></tr>'); continue
        if lab.startswith('注') or lab.startswith('Note:') or lab.startswith("'Core") or lab.startswith('“') or lab.startswith('Sales volume') or lab.startswith('销售量'):
            continue
        ind = lab.startswith('  ')
        cls = 'b' if (not ind and r in ()) else ''
        tds = [f'<td class="l{" ind" if ind else ""}">{lab.strip()}</td>']
        for i, c in enumerate(cols):
            v = ws.cell(r, c).value
            nf = wf.cell(r, c).number_format or ''
            e = ' e' if (c >= 6 and c <= 10) else ''
            tds.append(f'<td class="{e.strip()}">{fmtv(v, nf)}</td>')
        h.append(f'<tr class="{cls}">' + ''.join(tds) + '</tr>')
    h.append('</table>')
    return css, ''.join(h)

def head_lab(lang):
    return '项目（百万元，另注明除外）' if lang == 'cn' else 'RMB mn unless stated'

for sheet, lang, out in (('财务汇总', 'cn', 'chart7.html'), ('Summary_EN', 'en', 'chart7_en.html')):
    css, tab = table_html(sheet, lang)
    nrows = tab.count('<tr')
    H = 150 + 30 + nrows * 21.6 + 110
    H = int(H)
    if lang == 'cn':
        fr = frame_cn
        title_ = '三环集团财务模型汇总：三表、业务经营与关键指标（年度）'
        sub_ = '2023A-2030E；2023A-2025A为报告值，2026E起为基准情景预测（灰底）'
        src = ['资料来源：公司年报、半年报与季报，Wind；预测为本报告模型基准情景。',
               '注：“电子、通信元件及材料”为2026年半年报口径（电子元件+通信器件+电子及陶瓷材料+设备组件）；SOFC隔膜片历史值为第一大客户销售额代理。']
        grp = ('', '')
    else:
        import runpy
        g = runpy.run_path('gen_en.py', run_name='x')
        fr = g['frame']
        title_ = 'CCTC model summary: statements, operations and key metrics (annual)'
        sub_ = '2023A-2030E; 2023A-2025A reported, 2026E onward base-case forecast (shaded)'
        src = ['Sources: company annual, interim and quarterly reports, Wind; forecasts are the base case of the author\'s model.',
               'Note: "core components & materials" follows the 2026 interim basis (electronic + communication components + materials + equipment); SOFC history is a top-customer sales proxy.']
        grp = ('Annual', 'Quarterly')
    body = f'<style>{css}</style>' + tab
    html = fr(H, title_, sub_, body, src)
    open(out, 'w', encoding='utf8').write(html)
    print(out, H, nrows)

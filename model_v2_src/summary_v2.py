# -*- coding: utf-8 -*-
"""Bilingual one-page financial summary (财务汇总 / Summary_EN): annual 2023A-2030E and quarterly 2025Q1-2026Q2, all live formulas."""
import json, os
from openpyxl.styles import Font, Alignment, PatternFill
from engine import *

HERE = os.path.dirname(os.path.abspath(__file__))
ANN = [('2023A', 'E'), ('2024A', 'F'), ('2025A', 'G'), ('2026E', 'H'), ('2027E', 'I'), ('2028E', 'J'), ('2029E', 'K'), ('2030E', 'L')]
QTR = [('2025Q1', 'G', 'C'), ('2025Q2', 'H', 'D'), ('2025Q3', 'I', 'E'), ('2025Q4', 'J', 'F'), ('2026Q1', 'K', 'G'), ('2026Q2', 'L', 'H')]
ACOL = {y: CL(3 + i) for i, (y, _) in enumerate(ANN)}            # C..J
QCOL = {q: CL(12 + i) for i, (q, _, _) in enumerate(QTR)}          # L..Q (K is a spacer)
BS_Q = {'2025Q2': '2025H1', '2026Q2': '2026H1'}                   # balance sheet only at half-year ends (+ 2025Q4 = 2025A)


def build_summary(wb, g):
    S_REV, S_COST, S_OPEX, S_CAP, S_WC, S_FIN, S_TAX, S_M, S_SH, S_RET = (g[k] for k in (
        'S_REV', 'S_COST', 'S_OPEX', 'S_CAP', 'S_WC', 'S_FIN', 'S_TAX', 'S_M', 'S_SH', 'S_RET'))
    RAW, RAWS, HB = g['RAW'], g['RAWS'], g['HB']
    Q = '季度数据'

    def q(lab, c):
        return f"'{Q}'!{c}{REG[(Q, lab)]}"

    def m(sh, k, c):
        return X(sh, k, c)

    # one-year-plus deposits at the half-year ends (verified note data, 元 -> 百万元)
    d2 = json.load(open(os.path.join(HERE, 'extract', 'D2_financing_cash.json')))
    onca = [t for t in d2['tables'] if t['id'] == 'other_noncurrent_assets'][0]
    tdrow = [r for r in onca['rows'] if r['label'].startswith('到期日一年以上')][0]
    TDH = {c: v / 1e6 for c, v in zip(onca['columns'], tdrow['values']) if v is not None}

    def raws_q(labels, period):
        return RAWS(HB, labels, period)[1:]

    # row spec: (key, cn, en, fmt, annual(col)->formula|None, quarter(qcol, yago_col, qname)->formula|None)
    R = []
    sec = lambda cn, en: R.append(('#', cn, en))
    row = lambda *a: R.append(a)

    sec('一、利润表', 'I. Income statement')
    row('rev', '营业收入', 'Revenue', NUM, lambda c: f"={m(S_M,'rev',c)}", lambda qc, yc, n: f"={q('营业收入',qc)}")
    row('rev_g', '  同比', '  YoY', PCT, lambda c: f"={m(S_M,'rev_g',c)}", lambda qc, yc, n: f"=IFERROR({q('营业收入',qc)}/{q('营业收入',yc)}-1,0)")
    row('gp', '毛利', 'Gross profit', NUM, lambda c: f"={m(S_M,'gp',c)}", lambda qc, yc, n: f"={q('营业收入',qc)}-{q('营业成本',qc)}")
    row('gm', '  毛利率', '  Gross margin', PCT, lambda c: f"={m(S_M,'gm',c)}", lambda qc, yc, n: f"=IFERROR(1-{q('营业成本',qc)}/{q('营业收入',qc)},0)")
    row('sell', '销售费用', 'Selling expenses', NUM, lambda c: f"={m(S_M,'sell',c)}", lambda qc, yc, n: f"={q('销售费用',qc)}")
    row('adm', '管理费用', 'G&A expenses', NUM, lambda c: f"={m(S_M,'adm',c)}", lambda qc, yc, n: f"={q('管理费用',qc)}")
    row('rd', '研发费用', 'R&D expenses', NUM, lambda c: f"={m(S_M,'rd',c)}", lambda qc, yc, n: f"={q('研发费用',qc)}")
    row('opex_r', '  期间费用率', '  Opex / revenue', PCT, lambda c: f"=IFERROR(({m(S_M,'sell',c)}+{m(S_M,'adm',c)}+{m(S_M,'rd',c)})/{m(S_M,'rev',c)},0)",
        lambda qc, yc, n: f"=IFERROR(({q('销售费用',qc)}+{q('管理费用',qc)}+{q('研发费用',qc)})/{q('营业收入',qc)},0)")
    row('fin', '财务费用（负数为净收益）', 'Net finance cost (negative = income)', NUM, lambda c: f"={m(S_M,'fin',c)}", lambda qc, yc, n: f"={q('财务费用',qc)}")
    row('oi', '其他收益', 'Other income', NUM, lambda c: f"={m(S_M,'oi',c)}", lambda qc, yc, n: f"={q('其他收益',qc)}")
    row('op', '营业利润', 'Operating profit', NUM, lambda c: f"={m(S_M,'op',c)}", lambda qc, yc, n: f"={q('营业利润',qc)}")
    row('opm', '  营业利润率', '  Operating margin', PCT, lambda c: f"=IFERROR({m(S_M,'op',c)}/{m(S_M,'rev',c)},0)", lambda qc, yc, n: f"=IFERROR({q('营业利润',qc)}/{q('营业收入',qc)},0)")
    row('pbt', '利润总额', 'Profit before tax', NUM, lambda c: f"={m(S_M,'pbt',c)}", lambda qc, yc, n: f"={q('利润总额',qc)}")
    row('etr', '  实际税率', '  Effective tax rate', PCT, lambda c: f"={m(S_TAX,'etr',c)}", lambda qc, yc, n: f"=IFERROR({q('所得税',qc)}/{q('利润总额',qc)},0)")
    row('np', '归母净利润', 'Net profit attributable', NUM, lambda c: f"={m(S_M,'np',c)}", lambda qc, yc, n: f"={q('归母净利润',qc)}")
    row('np_g', '  同比', '  YoY', PCT, lambda c: f"={m(S_M,'np_g',c)}", lambda qc, yc, n: f"=IFERROR({q('归母净利润',qc)}/{q('归母净利润',yc)}-1,0)")
    row('npm', '  归母净利率', '  Net margin', PCT, lambda c: f"={m(S_M,'npm',c)}", lambda qc, yc, n: f"=IFERROR({q('归母净利润',qc)}/{q('营业收入',qc)},0)")
    row('eps', 'EPS（元，期末流通股本）', 'EPS (RMB, period-end shares)', PS, lambda c: f"={m(S_M,'eps',c)}", None)
    row('ebitda', 'EBITDA', 'EBITDA', NUM, lambda c: f"={m(S_M,'ebitda',c)}", None)
    row('ebitda_m', '  EBITDA利润率', '  EBITDA margin', PCT, lambda c: f"={m(S_M,'ebitda_m',c)}", None)

    sec('二、业务经营', 'II. Operations')
    row('ec', '电子元件收入', 'Electronic components revenue', NUM, lambda c: (f"={m(S_REV,'ec_rev',c)}" if c != 'E' else None), None)
    row('cd', '通信器件收入', 'Communication components revenue', NUM, lambda c: (f"={m(S_REV,'cd_rev',c)}" if c != 'E' else None), None)
    row('cm', '电子及陶瓷材料收入', 'Electronic & ceramic materials revenue', NUM, lambda c: (f"={m(S_REV,'cm_rev',c)}" if c != 'E' else None), None)
    row('sofc', '  其中SOFC隔膜片（历史为第一大客户代理）', '  of which SOFC separators (hist.: top-customer proxy)', NUM, lambda c: f"={m(S_REV,'sofc_rev',c)}", None)
    row('eq', '设备组件收入', 'Equipment components revenue', NUM, lambda c: (f"={m(S_REV,'eq_rev',c)}" if c != 'E' else None), None)
    row('oth', '其他主营及其他业务收入', 'Other revenue', NUM, lambda c: (f"={m(S_REV,'ot_rev',c)}+{m(S_REV,'ob_rev',c)}" if c != 'E' else None), None)
    row('core', '电子、通信元件及材料（半年报口径）', 'Core components & materials (interim basis)', NUM,
        lambda c: (f"={m(S_REV,'ec_rev',c)}+{m(S_REV,'cd_rev',c)}+{m(S_REV,'cm_rev',c)}+{m(S_REV,'eq_rev',c)}" if c != 'E' else None),
        None)
    row('vol', '销售量（亿只/片，公司口径）', 'Sales volume (100 mn units, company basis)', NUM, lambda c: (f"={m(S_REV,'vol_sales',c)}" if c in 'EFG' else None), None)
    row('hc', '员工人数（期末）', 'Headcount (period-end)', NUM0, lambda c: f"={m(S_OPEX,'hc_tot',c)}", None)
    row('pay', '人均薪酬（万元）', 'Pay per employee (RMB 10k)', NUM, lambda c: (f"={m(S_OPEX,'comp_pc',c)}" if c != 'E' else None), None)
    row('capex', '资本开支', 'Capex', NUM, lambda c: f"={m(S_CAP,'capex_tot',c)}", lambda qc, yc, n: f"={q('购建长期资产支付的现金',qc)}")
    row('da', '折旧与摊销', 'D&A', NUM, lambda c: f"={m(S_CAP,'da_tot',c)}", None)
    row('dso', '应收周转天数（票据+账款+融资）', 'Receivable days', DAYS, lambda c: f"={m(S_WC,'dso',c)}", None)
    row('dio', '存货周转天数', 'Inventory days', DAYS, lambda c: f"={m(S_WC,'dio',c)}", None)
    row('dpo', '应付周转天数（票据+账款）', 'Payable days', DAYS, lambda c: f"={m(S_WC,'dpo',c)}", None)
    row('ccc', '现金转换周期', 'Cash conversion cycle (days)', DAYS, lambda c: f"={m(S_WC,'ccc',c)}", None)

    sec('三、资产负债表（季度列仅半年末与年末）', 'III. Balance sheet (quarterly: half-year and year-ends only)')
    BSR = [('cash', '货币资金', 'Cash', 'cash', ['货币资金']), ('tfa', '交易性金融资产（理财）', 'Wealth-management products', 'tfa', ['交易性金融资产']),
           ('td', '一年以上定期存款及大额存单', 'Deposits over one year', None, None),
           ('rec', '应收票据、账款及应收款项融资', 'Notes, accounts receivable & receivables financing', None, ['应收票据', '应收账款', '应收款项融资']),
           ('inv', '存货', 'Inventories', 'invt', ['存货']), ('ppe', '固定资产及在建工程', 'PP&E incl. construction in progress', 'ppe', ['固定资产(合计)', '在建工程(合计)']),
           ('ta', '资产总计', 'Total assets', 'ta', ['资产总计']), ('debt', '有息负债', 'Interest-bearing debt', None, ['短期借款', '长期借款', '一年内到期的非流动负债']),
           ('tl', '负债合计', 'Total liabilities', 'tl', ['负债合计']), ('eq', '归母所有者权益', "Shareholders' equity", 'eq_p', ['归属于母公司所有者权益合计'])]
    for k, cn, en, mk, labs in BSR:
        if k == 'td':
            af = lambda c: f"={m(S_FIN,'td',c)}"
            qf = lambda qc, yc, n: (TDH.get(BS_Q[n]) if n in BS_Q else (f"={m(S_FIN,'td','G')}" if n == '2025Q4' else None))
        elif k == 'rec':
            af = lambda c: f"={m(S_M,'nrec',c)}+{m(S_M,'ar',c)}+{m(S_M,'rfin',c)}"
            qf = lambda qc, yc, n, labs=labs: (f"={raws_q(labs, BS_Q[n])}" if n in BS_Q else (f"={m(S_M,'nrec','G')}+{m(S_M,'ar','G')}+{m(S_M,'rfin','G')}" if n == '2025Q4' else None))
        elif k == 'debt':
            af = lambda c: f"={m(S_FIN,'debt',c)}"
            qf = lambda qc, yc, n, labs=labs: (f"={raws_q(labs, BS_Q[n])}" if n in BS_Q else (f"={m(S_FIN,'debt','G')}" if n == '2025Q4' else None))
        else:
            af = lambda c, mk=mk: f"={m(S_M,mk,c)}"
            qf = lambda qc, yc, n, labs=labs, mk=mk: (f"={raws_q(labs, BS_Q[n])}" if n in BS_Q else (f"={m(S_M,mk,'G')}" if n == '2025Q4' else None))
        row(k, cn, en, NUM, af, qf)
    row('netcash', '净现金（含一年以上定期存款）', 'Net cash (incl. deposits over one year)', NUM, lambda c: f"={m(S_FIN,'netcash',c)}",
        lambda qc, yc, n: (f"={{cash}}+{{tfa}}+{{td}}-{{debt}}-N({raws_q(['租赁负债'], BS_Q[n])})" if n in BS_Q else (f"={m(S_FIN,'netcash','G')}" if n == '2025Q4' else None)))
    row('lev', '  资产负债率', '  Liabilities / assets', PCT, lambda c: f"=IFERROR({{tl}}/{{ta}},0)", lambda qc, yc, n: (f"=IFERROR({{tl}}/{{ta}},0)" if n in BS_Q or n == '2025Q4' else None))

    sec('四、现金流量', 'IV. Cash flow')
    row('cfo', '经营活动现金流量净额', 'Operating cash flow', NUM, lambda c: f"={m(S_M,'cfo',c)}", lambda qc, yc, n: f"={q('经营活动现金流量净额',qc)}")
    row('capex2', '资本开支（流出为负）', 'Capex (outflow negative)', NUM, lambda c: f"={m(S_M,'capex',c)}", lambda qc, yc, n: f"=-{q('购建长期资产支付的现金',qc)}")
    row('fcf', '自由现金流（经营现金流-资本开支）', 'Free cash flow (OCF - capex)', NUM, lambda c: f"={{cfo}}+{{capex2}}", lambda qc, yc, n: f"={{cfo}}+{{capex2}}")
    row('div', '现金分红（历史含利息支付）', 'Dividends paid (hist. incl. interest)', NUM, lambda c: f"=-{m(S_M,'cf_div',c)}", lambda qc, yc, n: f"={q('分配股利、利润或偿付利息支付的现金',qc)}")
    row('bb', '股份回购', 'Share buybacks', NUM, lambda c: f"=-{m(S_M,'cf_bb',c)}", None)

    sec('五、关键指标', 'V. Key metrics')
    row('roe', 'ROE（平均权益）', 'ROE (average equity)', PCT, lambda c: (f"={m(S_RET,'roe',c)}" if c != 'E' or True else None), None)
    row('roic', 'ROIC', 'ROIC', PCT, lambda c: f"={m(S_RET,'roic',c)}", None)
    row('bvps', '每股净资产（元）', 'Book value per share (RMB)', PS, lambda c: f"=IFERROR({m(S_M,'eq_p',c)}/{m(S_SH,'out',c)},0)", None)
    row('dps', '每股股利（元，当年派发）', 'DPS paid in year (RMB)', PS, lambda c: (f"={m(S_SH,'dps_d',c)}" if c not in 'EF' else None), None)
    row('pe', 'PE（当前股价）', 'P/E (current price)', MULT, lambda c: f"={m(S_RET,'pe',c)}", None)
    row('pb', 'PB（当前股价）', 'P/B (current price)', MULT, lambda c: f"={m(S_RET,'pb',c)}", None)
    row('evx', 'EV/EBITDA（当前股价）', 'EV/EBITDA (current price)', MULT, lambda c: (f"={m(S_RET,'ev_ebitda',c)}" if c in 'HIJKL' else None), None)

    for lang, name in (('cn', '财务汇总'), ('en', 'Summary_EN')):
        ws = wb.create_sheet(name); CUR[0] = name
        if lang == 'cn':
            title(ws, '三环集团（300408.SZ / 06951.HK）财务模型汇总', '单位：百万元人民币（另注明除外）｜年度：2023A-2025A为报告值，2026E-2030E为基准情景（随“假设”C5切换）｜季度：单季报告值｜全部为链接公式')
            hdr = ['项目', '']
        else:
            title(ws, 'Sanhuan Group (CCTC, 300408.SZ / 06951.HK) - Financial model summary',
                  'RMB mn unless stated | Annual: 2023A-2025A reported, 2026E-2030E model (scenario per 假设!C5) | Quarterly: single-quarter reported | All cells are live links')
            hdr = ['Item', '']
        header_row(ws, 4, hdr + [y for y, _ in ANN] + [''] + [qn for qn, _, _ in QTR])
        put(ws, 'C3', '年度 / Annual' if lang == 'cn' else 'Annual', bold=True, color='1F3864')
        put(ws, 'L3', '季度（单季）/ Quarterly' if lang == 'cn' else 'Quarterly (single quarter)', bold=True, color='1F3864')
        r = 5
        rows_at = {}
        for spec in R:                        # first pass: register rows for {key} tokens
            if spec[0] != '#':
                rows_at[spec[0]] = r
            r += 1
        r = 5
        for spec in R:
            if spec[0] == '#':
                section(ws, r, spec[1] if lang == 'cn' else spec[2], 17); r += 1; continue
            k, cn, en, fmt, af, qf = spec
            lab = cn if lang == 'cn' else en
            put(ws, f'A{r}', lab, bold=not lab.startswith('  '))
            for y, mc in ANN:
                f = af(mc)
                if f is None:
                    continue
                for kk, rr in rows_at.items():
                    f = f.replace('{' + kk + '}', f'{ACOL[y]}{rr}')
                put(ws, f'{ACOL[y]}{r}', f, fmt, fill=FC_FILL if y.endswith('E') else None)
            if qf:
                for qn, qc, yc in QTR:
                    f = qf(qc, yc, qn)
                    if f is None:
                        continue
                    if isinstance(f, str):
                        for kk, rr in rows_at.items():
                            f = f.replace('{' + kk + '}', f'{QCOL[qn]}{rr}')
                    put(ws, f'{QCOL[qn]}{r}', f, fmt)
            REG[(name, k)] = r
            r += 1
        r += 1
        note_cn = ['注：季度资产负债表仅在半年末（2025Q2、2026Q2）与年末（2025Q4=2025A）可得；季度“资本开支”为购建长期资产支付的现金。',
                   '“电子、通信元件及材料”为2026年半年报口径（电子元件+通信器件+电子及陶瓷材料+设备组件），2026H1为6,080.7（同比+55.0%）；季度分部收入未披露。']
        note_en = ['Note: quarterly balance-sheet data are available only at half-year ends (2025Q2, 2026Q2) and year-end (2025Q4 = 2025A); quarterly capex is cash paid for long-term assets.',
                   "'Core components & materials' follows the 2026 interim-report basis (electronic + communication components + materials + equipment); 2026H1 was 6,080.7 (+55.0% YoY). Quarterly segment revenue is not disclosed."]
        for t_ in (note_cn if lang == 'cn' else note_en):
            put(ws, f'A{r}', t_, italic=True, color='595959'); r += 1
        ws.column_dimensions['A'].width = 46 if lang == 'cn' else 52
        ws.column_dimensions['B'].width = 2
        for col in list(ACOL.values()) + list(QCOL.values()):
            ws.column_dimensions[col].width = 11
        ws.column_dimensions['K'].width = 2
        ws.freeze_panes = 'C5'
        ws.sheet_view.showGridLines = False

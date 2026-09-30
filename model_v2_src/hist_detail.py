# -*- coding: utf-8 -*-
"""Historical note-level detail (百万元) built from the extraction JSONs of the annual/interim reports."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
EXT = os.path.join(HERE, 'extract')


def _load(domain):
    for pref in ('', 'raw_'):          # verified file (extract/<domain>.json) first, raw extraction as fallback
        p = os.path.join(EXT, f'{pref}{domain}.json')
        if os.path.exists(p):
            return {t['id']: t for t in json.load(open(p))['tables']}
    return {}


D1 = _load('D1_fixed_assets')
D2 = _load('D2_financing_cash')
D3 = _load('D3_revenue_cost')
D4 = _load('D4_working_capital')
D5 = _load('D5_tax_other_pl')

M = 1e6


def row(tab, label, scale=M, cols=None):
    """{column: value/scale} for a row of a table (None dropped)."""
    if not tab:
        return {}
    for r in tab['rows']:
        if r['label'] == label:
            out = {}
            for c, v in zip(tab['columns'], r['values']):
                if v is not None and (cols is None or c in cols):
                    out[c] = round(v / scale, 6)
            return out
    MISSING.append((tab.get('id'), label))
    return {}


MISSING = []


def annual(d):
    return {k: v for k, v in d.items() if k.startswith('FY')}


DATA = {}

# ---------------------------------------------------------------- volumes (万只/万片, kept in original unit)
DATA['volume'] = {k: annual(row(D3.get('D3_volumes'), k, 1)) for k in ('销售量', '生产量', '库存量')}

# ---------------------------------------------------------------- region (annual report 2022-2023; H-share prospectus 2024-2025)
DATA['region'] = {'os_share': {'FY2022': 0.2112, 'FY2023': 0.2011, 'FY2024': 0.179, 'FY2025': 0.174}}

# ---------------------------------------------------------------- COGS by nature
DATA['cogs_nature'] = {k: annual(row(D3.get('D3_cogs_composition'), f'工业|{k}')) for k in ('原材料', '人工费用', '制造费用')}

# ---------------------------------------------------------------- headcount / payroll
DATA['hc'] = {k: annual(row(D3.get('D3_employees'), f'专业构成|{k}', 1)) for k in ('生产人员', '销售人员', '技术人员', '财务人员', '行政人员')}
DATA['comp_total'] = annual(row(D3.get('D3_payroll_cost_additions'), '应付职工薪酬本期增加总计'))

# ---------------------------------------------------------------- opex by nature
sell = D3.get('D3_selling_expense_detail')
adm23 = D3.get('D3_admin_expense_detail_FY2023rpt')
adm = D3.get('D3_admin_expense_detail_FY2024_25rpt')
rd = D3.get('D3_rnd_expense_detail')
adm_staff = annual(row(adm23, '工资、社保、福利'))
adm_staff.update(annual(row(adm, '职工薪酬')))
adm_da = {}
for tab in (adm23, adm):
    for lab in ('固定资产折旧', '无形资产摊销', '使用权资产折旧'):
        for k, v in annual(row(tab, lab)).items():
            adm_da.setdefault(k, {})[lab] = v
adm_da = {k: round(sum(v.values()), 6) for k, v in adm_da.items()}
DATA['opex_nature'] = {
    '销售费用': {'职工薪酬': annual(row(sell, '职工薪酬（FY2022-23原称：工资、社保、福利）'))},
    '管理费用': {'职工薪酬': adm_staff, '折旧摊销': adm_da},
    '研发费用': {'职工薪酬': annual(row(rd, '人员人工费用')), '折旧摊销': annual(row(rd, '折旧摊销费用')),
               '直接投入/材料': annual(row(rd, '直接投入费用'))},
}

# ---------------------------------------------------------------- fixed assets by category
CATMAP = {'房屋建筑物': '房屋及建筑物', '运输工具': '运输设备', '其他工具': '电子设备及其他'}
fa = {}
fa_total = {'add_purchase': {}, 'add_cip': {}, 'imp_close': {}}
for fy in ('FY2023', 'FY2024', 'FY2025'):
    t = D1.get(f'D1_ppe_rf_{fy}')
    if not t:
        continue
    cols = t['columns']
    rows = {r['label']: r['values'] for r in t['rows']}
    def g(lab, i):
        v = rows.get(lab, [None] * len(cols))[i]
        return 0.0 if v is None else v / M
    for i, c in enumerate(cols):
        nm = CATMAP.get(c, c)
        rec = {
            'gross_open': g('原值|期初余额', i),
            'add_purchase': g('原值|增加:购置', i),
            'add_cip': g('原值|增加:在建工程转入', i),
            'gross_close': g('原值|期末余额', i),
            'disp_gross': g('原值|减少:处置或报废', i),
            'ad_open': g('累计折旧|期初余额', i),
            'dep': g('累计折旧|增加:计提', i),
            'ad_disp': g('累计折旧|减少:处置或报废', i),
            'ad_close': g('累计折旧|期末余额', i),
            'imp_close': g('减值准备|期末余额', i),
        }
        rec['add_other'] = g('原值|本期增加金额', i) - rec['add_purchase'] - rec['add_cip']
        rec['red_other'] = g('原值|本期减少金额', i) - rec['disp_gross']
        rec['ad_other_net'] = (g('累计折旧|本期减少金额', i) - rec['ad_disp']) - (g('累计折旧|本期增加金额', i) - rec['dep'])
        rec = {k: round(v, 6) for k, v in rec.items()}
        if nm == '合计':
            fa_total['add_purchase'][fy] = rec['add_purchase']
            fa_total['add_cip'][fy] = rec['add_cip']
            fa_total['imp_close'][fy] = rec['imp_close']
            if fy == 'FY2023':
                fa_total['imp_close']['FY2022'] = round(g('减值准备|期初余额', i), 6)
            continue
        for k, v in rec.items():
            fa.setdefault(nm, {}).setdefault(k, {})[fy] = v
        if fy == 'FY2023':   # FY2022 closing balances = FY2023 opening
            fa[nm].setdefault('gross_close', {})['FY2022'] = rec['gross_open']
            fa[nm].setdefault('ad_close', {})['FY2022'] = rec['ad_open']
DATA['fa'] = fa
DATA['fa_total'] = fa_total
DATA['fa_clear'] = {'FY2023': 1.924903}   # 固定资产清理 (FY2023 only)

# ---------------------------------------------------------------- cash / deposits
DATA['cash'] = {'受限资金': annual(row(D2.get('cash_composition'), '受限货币资金合计')),
                '三个月以上定期存款（货币资金内）': annual(row(D2.get('cash_composition'), '到期日超过3个月的大额存单及定期存款本息（在货币资金内，不作为现金等价物）'))}
td = annual(row(D2.get('other_noncurrent_assets'), '到期日一年以上的定期存款及大额存单'))
td.setdefault('FY2022', 0.0)
DATA['onca'] = {'定期存款及大额存单': td}

# ---------------------------------------------------------------- inventory (gross by class, provision)
ig, ip = D4.get('inventory_gross'), D4.get('inventory_provision')
def _sum(*ds):
    keys = set().union(*[d.keys() for d in ds])
    return {k: round(sum(d.get(k, 0) for d in ds), 6) for k in keys}
DATA['inv'] = {
    '原材料': annual(row(ig, '原材料')),
    '在产品': annual(_sum(row(ig, '在产品'), row(ig, '半成品'))),
    '库存商品及发出商品': annual(_sum(row(ig, '库存商品'), row(ig, '发出商品'))),
    '其他': {k: 0.0 for k in annual(row(ig, '合计'))},
    '跌价准备': annual(row(ip, '合计')),
}

# ---------------------------------------------------------------- other income / tax bridge
oi = D5.get('D5_other_income')
DATA['oi'] = {'与资产相关的政府补助': annual(row(oi, '  其中：与资产相关')),
              '增值税加计抵减': annual(row(oi, "  其中：增值税加计抵减（非经常性损益节，界定为经常性损益）"))}
tr = D5.get('D5_tax_reconciliation')
DATA['tax'] = {'子公司适用不同税率的影响': annual(row(tr, '子公司适用不同税率的影响')),
               '研发费用加计扣除的影响': annual(row(tr, '研发费用加计扣除'))}

if __name__ == '__main__':
    import pprint
    pprint.pprint(DATA, width=160)
    print('MISSING lookups:', MISSING)

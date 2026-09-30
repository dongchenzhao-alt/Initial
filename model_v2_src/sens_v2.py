# -*- coding: utf-8 -*-
"""Drive the recalculated v2 model through LibreOffice UNO: tornado, 2-D grids, scenarios, reverse-DCF solves.
Usage: python3 sens_v2.py model_v2.xlsx  -> writes sens_results.json"""
import sys, json, time
from uno_runner import Calc

PATH = sys.argv[1]
REG = json.load(open(PATH.rsplit('.', 1)[0] + '_reg.json'))


def rr(sheet, key):
    return REG[f'{sheet}|{key}']


c = Calc(PATH, port=2041)
M = '三表预测'


def cell_np(col):
    return (M, f'{col}{rr(M, "np")}')


OUT = {
    'np26': cell_np('H'), 'np27': cell_np('I'), 'np28': cell_np('J'), 'np30': cell_np('L'),
    'rev27': (M, f'I{rr(M, "rev")}'), 'gm27': (M, f'I{rr(M, "gm")}'), 'eps27': (M, f'I{rr(M, "eps")}'),
    'fcf27': (M, f'I{rr(M, "fcf")}'), 'vps': ('DCF估值', f'C{rr("DCF", "vps")}'), 'vps_now': ('DCF估值', f'C{rr("DCF", "vps_now")}'),
    'up': ('DCF估值', f'C{rr("DCF", "up")}'), 'wacc': ('DCF估值', f'C{rr("DCF", "wacc")}'), 'g_imp': ('DCF估值', f'C{rr("DCF", "g_imp")}'),
    'chk': ('校验', f'C{rr("校验", "sum")}'),
}
for yc, y in zip('HIJKL', ['2026E', '2027E', '2028E', '2029E', '2030E']):
    OUT[f'fcf_{y}'] = (M, f'{yc}{rr(M, "fcf")}')


MAXCHK = [0.0]


def read():
    c.recalc()
    out = {k: c.val(s, a) for k, (s, a) in OUT.items()}
    MAXCHK[0] = max(MAXCHK[0], abs(out['chk']))
    return out


def A1(key):
    return ('假设', f'C{rr("假设1", key)}')


c.set(*A1('scen'), 1)          # static results are base-case by design
for k_ in [k.split('|')[1] for k in REG if k.startswith('假设1|s_')]:
    c.set(*A1(k_), 0)
base = read()
print('base', {k: round(v, 3) for k, v in base.items() if k in ('np26', 'np27', 'vps', 'vps_now', 'chk')})
assert abs(base['chk']) < 1e-6, 'model checks not zero at base'


def with_inputs(pairs):
    """pairs: list of ((sheet, ref), value). Sets, reads, restores."""
    old = [(sa, c.val(*sa)) for sa, _ in pairs]
    for sa, v in pairs:
        c.set(*sa, v)
    out = read()
    for sa, v in old:
        c.set(*sa, v)
    return out


# ---------------------------------------------------------------- tornado
TORNADO = [
    ('s_ec_vol', '电子元件销量增速（逐年±5pp）', -0.05, 0.05, 'pp'),
    ('s_ec_px', '电子元件单价变动（逐年±3pp）', -0.03, 0.03, 'pp'),
    ('s_cd_vol', '通信器件销量增速（逐年±5pp）', -0.05, 0.05, 'pp'),
    ('s_cd_px', '通信器件单价变动（逐年±2pp）', -0.02, 0.02, 'pp'),
    ('s_cm', '其他电子及陶瓷材料增速（逐年±5pp）', -0.05, 0.05, 'pp'),
    ('s_gm', '全部分部毛利率（±2pp）', -0.02, 0.02, 'pp'),
    ('s_sofc_gw', 'Bloom电池片层需求（±30%）', -0.30, 0.30, '%'),
    ('s_sofc_sh', '三环隔膜片份额（±15pp）', -0.15, 0.15, 'pp'),
    ('s_sofc_px', '隔膜片单价（±15%）', -0.15, 0.15, '%'),
    ('s_wage', '人均薪酬增速（逐年±3pp）', 0.03, -0.03, 'pp'),
    ('s_hc', '员工人数增速（逐年±3pp）', 0.03, -0.03, 'pp'),
    ('s_opex', '管理费用其他项占收入（±0.3pp）', 0.003, -0.003, 'pp'),
    ('s_grant', '政府补助占收入（±0.3pp）', -0.003, 0.003, 'pp'),
    ('s_capex', '资本开支（±25%）', 0.25, -0.25, '%'),
    ('s_dep', '折旧率（±10%；估值影响主要来自第二阶段与永续期NOPAT）', 0.10, -0.10, '%'),
    ('s_wcdays', '应收与产成品周转天数（±15天）', 15, -15, '天'),
    ('s_yield', '存款及理财收益率（±0.5pp）', -0.005, 0.005, 'pp'),
    ('s_tax', '实际税率（±2pp）', 0.02, -0.02, 'pp'),
    ('rf', '无风险利率（±0.5pp）', 0.005, -0.005, 'val'),
    ('erp', '股权风险溢价（±1pp）', 0.01, -0.01, 'val'),
    ('beta', 'Beta（±0.2）', 0.2, -0.2, 'val'),
    ('g', '永续增长率（±0.5pp）', -0.005, 0.005, 'val'),
    ('g2s', '第二阶段起点增速溢价（±4pp）', -0.04, 0.04, 'val'),
    ('ronic', '新增投资资本回报率RONIC（±10pp）', -0.10, 0.10, 'val'),
]
tornado = []
t0 = time.time()
for key, lab, lo, hi, kind in TORNADO:
    sa = A1(key)
    b = c.val(*sa)
    lo_v, hi_v = (b + lo, b + hi) if kind == 'val' else (lo, hi)
    rlo = with_inputs([(sa, lo_v)])
    rhi = with_inputs([(sa, hi_v)])
    tornado.append({'key': key, 'label': lab, 'lo_in': lo_v, 'hi_in': hi_v, 'kind': kind,
                    'lo': {k: rlo[k] for k in ('np27', 'np30', 'vps', 'fcf27')}, 'hi': {k: rhi[k] for k in ('np27', 'np30', 'vps', 'fcf27')}})
print('tornado', len(tornado), 'in', round(time.time() - t0, 1), 's')

# ---------------------------------------------------------------- 2-D grids
GRIDS = [
    ('sofc', 'SOFC：Bloom电池片层需求冲击（行）× 三环份额冲击（列）', 's_sofc_gw', [-0.4, -0.2, 0, 0.2, 0.4], '%', 's_sofc_sh', [-0.2, -0.1, 0, 0.1, 0.2], 'pp', ['np27', 'vps']),
    ('ec', '电子元件：单价变动冲击（行）× 销量增速冲击（列）', 's_ec_px', [-0.06, -0.03, 0, 0.03, 0.06], 'pp', 's_ec_vol', [-0.10, -0.05, 0, 0.05, 0.10], 'pp', ['np27', 'vps']),
    ('gm', '毛利率冲击（行）× 通信器件销量增速冲击（列）', 's_gm', [-0.03, -0.015, 0, 0.015, 0.03], 'pp', 's_cd_vol', [-0.10, -0.05, 0, 0.05, 0.10], 'pp', ['np27', 'vps']),
    ('cash', '资本开支冲击（行）× 周转天数冲击（列）', 's_capex', [-0.3, -0.15, 0, 0.15, 0.3], '%', 's_wcdays', [-20, -10, 0, 10, 20], '天', ['fcf27', 'vps']),
    ('staff', '人均薪酬增速冲击（行）× 员工人数增速冲击（列）', 's_wage', [-0.03, -0.015, 0, 0.015, 0.03], 'pp', 's_hc', [-0.04, -0.02, 0, 0.02, 0.04], 'pp', ['np27', 'vps']),
]
grids = []
for gid, ttl, rk, rvals, ru, ck, cvals, cu, outs in GRIDS:
    res = {o: [] for o in outs}
    for rv_ in rvals:
        rowvals = {o: [] for o in outs}
        for cv_ in cvals:
            r = with_inputs([(A1(rk), rv_), (A1(ck), cv_)])
            for o in outs:
                rowvals[o].append(r[o])
        for o in outs:
            res[o].append(rowvals[o])
    grids.append({'id': gid, 'title': ttl, 'rk': rk, 'rvals': rvals, 'ru': ru, 'ck': ck, 'cvals': cvals, 'cu': cu, 'res': res})
print('grids done', round(time.time() - t0, 1), 's')

# ---------------------------------------------------------------- scenarios
SC_OUT = {}
for yc, y in zip('GHIJKL', ['2025A', '2026E', '2027E', '2028E', '2029E', '2030E']):
    for k in ('rev', 'rev_g', 'gm', 'np', 'np_g', 'eps', 'fcf', 'capex', 'ebitda'):
        SC_OUT[f'{k}|{y}'] = (M, f'{yc}{rr(M, k)}')
    SC_OUT[f'sofc|{y}'] = ('收入拆解', f'{yc}{rr("收入拆解", "sofc_rev")}')
    SC_OUT[f'roic|{y}'] = ('回报分析', f'{yc}{rr("回报分析", "roic")}')
    SC_OUT[f'netcash|{y}'] = ('融资与资金', f'{yc}{rr("融资与资金", "netcash")}')
for k in ('vps', 'vps_now', 'up', 'g_imp', 'pe_imp', 'ev_ebitda'):
    SC_OUT[f'{k}|'] = ('DCF估值', f'C{rr("DCF", k)}')
SC_OUT['chk|'] = ('校验', f'C{rr("校验", "sum")}')
scen = {}
sc_cell = A1('scen')
for sn in (1, 2, 3):
    c.set(*sc_cell, sn); c.recalc()
    scen[sn] = {k: c.val(s, a) for k, (s, a) in SC_OUT.items()}
    MAXCHK[0] = max(MAXCHK[0], abs(scen[sn]['chk|']))
c.set(*sc_cell, 1); c.recalc()
print('scenarios', {sn: round(scen[sn]['np|2027E'], 1) for sn in scen}, {sn: round(scen[sn]['vps|'], 2) for sn in scen})


# ---------------------------------------------------------------- reverse DCF solves (vps_now == price)
price = c.val(*A1('price'))


def solve(key, lo, hi, target_key='vps_now', target=None, it=60):
    target = price if target is None else target
    sa = A1(key); b = c.val(*sa)
    f = lambda x: with_inputs([(sa, x)])[target_key] - target
    flo, fhi = f(lo), f(hi)
    if flo * fhi > 0:
        return {'key': key, 'solved': False, 'base': b, 'lo': lo, 'hi': hi, 'f_lo': flo, 'f_hi': fhi}
    for _ in range(it):
        mid = (lo + hi) / 2; fm = f(mid)
        if abs(fm) < 1e-4:
            break
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    x = (lo + hi) / 2
    c.set(*sa, x); out = read(); c.set(*sa, b); c.recalc()
    return {'key': key, 'solved': True, 'x': x, 'base': b, 'out': out}


rev = {}
rev['beta'] = solve('beta', 0.5, 1.5)
rev['g2s'] = solve('g2s', 0.0, 0.18)          # premium capped so stage-2 reinvestment stays below 100% of NOPAT
rev['s_ec_vol'] = solve('s_ec_vol', 0.0, 0.6)
rev['s_gm'] = solve('s_gm', 0.0, 0.3)
rev['s_sofc_gw'] = solve('s_sofc_gw', 0.0, 2.0)    # up to 3x base Bloom demand
# SOFC value contribution: zero SOFC demand
zero_sofc = with_inputs([(A1('s_sofc_gw'), -1.0)])
print('reverse', {k: (round(v['x'], 4) if v['solved'] else 'nb') for k, v in rev.items()})
print('max |check| across all runs:', MAXCHK[0])
assert MAXCHK[0] < 0.01, 'integrity check failed in a shocked run'
c.close()

json.dump({'maxchk': MAXCHK[0], 'base': base, 'tornado': tornado, 'grids': grids, 'scen': scen, 'rev': rev, 'zero_sofc': zero_sofc, 'price': price},
          open('sens_results.json', 'w'), ensure_ascii=False, indent=1)
print('saved sens_results.json')

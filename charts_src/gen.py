# -*- coding: utf-8 -*-
# 生成6张图表的HTML（1440px逻辑宽度），由render.js按5120px宽渲染
import os
W = 1440
SERIF = "'Noto Serif CJK SC','Noto Serif CJK JP',serif"
SANS = "'DejaVu Sans','Noto Sans CJK SC',sans-serif"
INK = "#1F2933"; GRAY = "#6B7580"; LIGHT = "#9AA3AE"; GRID = "#D9DEE8"
ORANGE = "#C2610F"

def frame(H, title, subtitle, body, sources):
    src = "".join(f'<div>{s}</div>' for s in sources)
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;background:#fff;overflow:hidden}}
body{{position:relative;font-family:{SANS};color:{INK}}}
.bar{{position:absolute;left:0;right:0;height:11px}}
.top{{top:0;background:linear-gradient(90deg,#1E3A8A,#4C1D95 55%,#9B6BF0);border-radius:10px 10px 0 0}}
.bot{{bottom:0;background:linear-gradient(90deg,#9B6BF0,#4C1D95 45%,#1E3A8A);border-radius:0 0 10px 10px}}
.logo{{position:absolute;left:46px;top:47px;height:29px}}
.title{{position:absolute;right:47px;top:40px;font-family:{SERIF};font-weight:700;font-size:29px;color:{INK};text-align:right;white-space:nowrap}}
.sub{{position:absolute;right:47px;top:88px;font-family:{SANS};font-size:20px;color:{LIGHT};text-align:right;white-space:nowrap}}
.src{{position:absolute;right:57px;bottom:30px;font-size:15px;line-height:22px;color:{GRAY};text-align:right}}
svg text{{font-family:{SANS}}}
</style></head><body>
<div class="bar top"></div>
<img class="logo" src="logo.png">
<div class="title">{title}</div>
<div class="sub">{subtitle}</div>
{body}
<div class="src">{src}</div>
<div class="bar bot"></div>
</body></html>"""

DEFS = f"""<defs>
<linearGradient id="gBlue" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6D6BE3"/><stop offset="1" stop-color="#2A2A95"/></linearGradient>
<linearGradient id="gPurp" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#A15CDB"/><stop offset="1" stop-color="#4A0F7E"/></linearGradient>
<linearGradient id="gGray" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C3CAD6"/><stop offset="1" stop-color="#6B7896"/></linearGradient>
<linearGradient id="gHGray" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#6B7896"/><stop offset="1" stop-color="#C3CAD6"/></linearGradient>
<linearGradient id="gHBlue" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2A2A95"/><stop offset="1" stop-color="#6D6BE3"/></linearGradient>
<linearGradient id="gHPurp" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#3B1F8F"/><stop offset="1" stop-color="#8157D6"/></linearGradient>
<linearGradient id="gHPurp2" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#4A0F7E"/><stop offset="1" stop-color="#A15CDB"/></linearGradient>
<pattern id="hatch" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="12" stroke="#6B7896" stroke-width="3"/></pattern>
<marker id="arr" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#8A93A6"/></marker>
</defs>"""

def svg(H, inner, top=0):
    return f'<svg style="position:absolute;left:0;top:{top}px" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{DEFS}{inner}</svg>'

def t(x, y, s, size=18, fill=INK, anchor="middle", weight=400, fam=None, extra=""):
    f = f' style="font-family:{fam}"' if fam else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}"{f} {extra}>{s}</text>'

charts = {}

# ---------- 图表1 三道换算 ----------
H = 621
inner = ""
boxes = [(73, "Bloom验收", "约500MW", "系统层，按合约确认收入", ("#4F8FEA", "#1B4AA0"), "#1B3F99"),
         (414, "电池片层产量", "约0.65到0.8GW", "含翻新约25%到30%", ("#6A5FE0", "#2E2A9A"), "#2E2A9A"),
         (757, "隔膜片采购", "约2,000万到3,200万片", "含备货或消化", ("#8E5BEA", "#4A1B9C"), "#4A1B9C"),
         (1099, "三环收入", "3.31亿元", "片数×单价", ("#A45BDB", "#56137F"), "#56137F")]
defs1 = ""
for i, (x, lab, val, desc, (c1, c2), vc) in enumerate(boxes):
    defs1 += f'<linearGradient id="b{i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>'
    inner += f'<rect x="{x}" y="180" width="268" height="97" rx="6" fill="url(#b{i})"/>'
    inner += t(x+134, 235, lab, 20, "#fff", weight=700)
    inner += t(x+134, 330, val, 19, vc, weight=700)
    inner += t(x+134, 387, desc, 17, GRAY)
    if i < 3:
        inner += f'<line x1="{x+280}" y1="228" x2="{x+338}" y2="228" stroke="#8A93A6" stroke-width="3" marker-end="url(#arr)"/>'
inner = f"<defs>{defs1}</defs>" + inner
inner += f'<rect x="73" y="428" width="1294" height="72" rx="6" fill="none" stroke="#6B7580" stroke-width="2" stroke-dasharray="8 6"/>'
inner += t(720, 470, "三道换算：翻新占比约25%到30%｜采购与验收之间的库存时差｜单片25W到32.5W，每GW约3,080万到4,000万片", 17, INK)
charts[1] = frame(H, "Bloom的放量要过三道换算，才会变成三环的隔膜片收入",
                  "验收量→电池片层→隔膜片采购→三环收入，以2025年为例", svg(H, inner),
                  ["资料来源：Bloom Energy年报与公告，三环集团H股招股章程，产业链调研；本报告整理。"])

# ---------- 图表2 存货与销售额 ----------
H = 938
x0, x1, yb, yt = 140, 1302, 758, 196   # 左轴0..10
def yl(v): return yb - (yb - yt) * v / 10
def yr(v): return yb - (yb - yt) * v / 5
inner = ""
for v in range(0, 11, 2):
    inner += f'<line x1="{x0}" y1="{yl(v)}" x2="{x1}" y2="{yl(v)}" stroke="{GRID}" stroke-width="1.2"/>'
    inner += t(x0-12, yl(v)+6, v, 18, INK, "end")
for v in range(0, 6):
    inner += t(x1+14, yr(v)+6, v, 18, ORANGE, "start")
inner += f'<line x1="{x0}" y1="{yt-30}" x2="{x0}" y2="{yb}" stroke="#AEB5C2" stroke-width="1.5"/>'
inner += f'<line x1="{x1}" y1="{yt-30}" x2="{x1}" y2="{yb}" stroke="{ORANGE}" stroke-width="2"/>'
inner += f'<line x1="{x0}" y1="{yb}" x2="{x1}" y2="{yb}" stroke="#AEB5C2" stroke-width="1.5"/>'
inner += t(92, 462, "亿美元", 18, INK, extra='transform="rotate(-90 92 462)"')
inner += t(1352, 462, "亿元", 18, ORANGE, extra='transform="rotate(90 1352 462)"')
cats = ["2022年末", "2023年末", "2024年末", "2025年末", "2026年|一季度末", "2026年|二季度末"]
base = [2.10, 3.21, 3.95, 4.77, 5.06, 5.34]
fg = [0.58, 1.81, 1.49, 1.67, 2.27, 2.24]
step = (x1 - x0) / 6; bw = 93
pts = {}
for i in range(6):
    cx = x0 + step * (i + 0.5); bx = cx - bw/2
    inner += f'<path d="M{bx},{yl(base[i])} h{bw} V{yb} h{-bw} z" fill="url(#gGray)"/>'
    top = yl(base[i]+fg[i])
    inner += f'<path d="M{bx},{yl(base[i])} V{top+6} q0,-6 6,-6 h{bw-12} q6,0 6,6 V{yl(base[i])} z" fill="url(#gPurp)"/>'
    if fg[i] < 1:
        inner += t(cx, top-16, f"{fg[i]:.2f}", 18, "#4A0F7E", weight=700)
    else:
        inner += t(cx, (top+yl(base[i]))/2+7, f"{fg[i]:.2f}", 18, "#fff", weight=700)
    lines = cats[i].split("|")
    for k, ln in enumerate(lines):
        inner += t(cx, yb+24+k*22, ln, 18, INK)
    pts[i] = cx
sales = {1: 4.49, 2: 3.24, 3: 3.31}
path = " ".join(f"{'M' if k==1 else 'L'}{pts[k]},{yr(v)}" for k, v in sales.items())
inner += f'<path d="{path}" fill="none" stroke="#D2711A" stroke-width="5" stroke-linejoin="round"/>'
for k, v in sales.items():
    inner += f'<circle cx="{pts[k]}" cy="{yr(v)}" r="8" fill="{ORANGE}"/>'
    inner += t(pts[k], yr(v)-26, f"{v:.2f}", 18, ORANGE, weight=700)
lx, ly = 978, 172
inner += f'<rect x="{lx}" y="{ly}" width="30" height="16" fill="#6B7896"/>' + t(lx+44, ly+14, "原材料与在制品", 17, INK, "start")
inner += f'<rect x="{lx}" y="{ly+27}" width="30" height="16" fill="#4A0F7E"/>' + t(lx+44, ly+41, "成品", 17, INK, "start")
inner += f'<line x1="{lx-4}" y1="{ly+62}" x2="{lx+34}" y2="{ly+62}" stroke="#D2711A" stroke-width="5"/><circle cx="{lx+15}" cy="{ly+62}" r="7" fill="{ORANGE}"/>' + t(lx+44, ly+68, "三环对第一大客户销售额（右轴）", 17, INK, "start")
charts[2] = frame(H, "Bloom的成品存货在2023年增至约三倍，三环销售额随后回落",
                  "Bloom存货（亿美元，左轴）与三环对第一大客户销售额（亿元，右轴）", svg(H, inner),
                  ["资料来源：Bloom Energy年报与季报，三环集团H股招股章程；本报告整理。", "注：三环为年度数据，标在对应年末。"])

# ---------- 图表3 覆盖率与每GW价值量 ----------
H = 874
inner = t(46, 188, "覆盖率（2025年）", 19, LIGHT, "start")
inner += t(767, 188, "每GW隔膜片价值量（亿元）", 19, LIGHT, "start")
cols = [(238, "单片25W"), (458, "单片32.5W")]
rows = [(309, "单价20元", ["52%到64%", "67%到83%"], [0.58, 0.75]),
        (421, "单价25元", ["41%到51%", "54%到66%"], [0.46, 0.60]),
        (533, "单价30元", ["34%到42%", "45%到55%"], [0.38, 0.50])]
for cx, lab in cols:
    inner += t(cx+103, 283, lab, 19, INK, weight=700)
def mix(c1, c2, f): return "#%02X%02X%02X" % tuple(int(a+(b-a)*f) for a, b in zip(c1, c2))
for ry, lab, vals, fs in rows:
    inner += t(224, ry+56, lab, 19, INK, "end", 700)
    for (cx, _), v, f in zip(cols, vals, fs):
        f2 = (f-0.38)/(0.75-0.38)
        c1 = mix((188, 192, 214), (155, 82, 214), f2); c2 = mix((105, 116, 146), (75, 12, 125), f2)
        gid = f"h{ry}{cx}"
        inner += f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs>'
        inner += f'<rect x="{cx}" y="{ry}" width="207" height="101" rx="5" fill="url(#{gid})"/>'
        inner += t(cx+103, ry+58, v, 19, "#fff", weight=700)
inner += f'<rect x="453" y="304" width="217" height="111" rx="8" fill="none" stroke="{ORANGE}" stroke-width="3.5"/>'
inner += t(238, 688, "橙框：唯一接近市场所说约八成的组合", 18, ORANGE, "start", 700)
ax0, ax1, amax = 766, 1395, 17.5
def xv(v): return ax0 + (ax1-ax0)*v/amax
for v in (0, 5, 10, 15):
    inner += f'<line x1="{xv(v)}" y1="205" x2="{xv(v)}" y2="714" stroke="{GRID}" stroke-width="1.2"/>'
    inner += t(xv(v), 740, v, 18, INK)
inner += f'<line x1="{ax0}" y1="714" x2="{ax1}" y2="714" stroke="#AEB5C2" stroke-width="1.5"/>'
bars = [(250, "市场口径：单片25W，单价30到37.5元", 12, 15, "url(#gHGray)", "12到15", "#6B7896"),
        (370, "单片25W，单价25元", 10.0, None, "url(#gHBlue)", "10.0", "#2A2A95"),
        (490, "单片32.5W，单价25元", 7.7, None, "url(#gHPurp)", "7.7", "#3B1F8F"),
        (610, "单片32.5W，单价20元", 6.2, None, "url(#gHPurp2)", "6.2", "#4A0F7E")]
for y, lab, v, v2, fill, vl, vc in bars:
    inner += t(ax0+2, y+18, lab, 17, INK, "start", 700)
    inner += f'<rect x="{ax0}" y="{y+30}" width="{xv(v)-ax0}" height="43" rx="4" fill="{fill}"/>'
    endx = xv(v)
    if v2:
        inner += f'<rect x="{xv(v)}" y="{y+31}" width="{xv(v2)-xv(v)}" height="41" fill="url(#hatch)" stroke="#6B7896" stroke-width="2"/>'
        endx = xv(v2)
    inner += t(endx+14, y+58, vl, 18, vc, "start", 700)
charts[3] = frame(H, "三环2025年的覆盖率随单价与单片功率在三成到八成之间摆动",
                  "左：三环片数÷Bloom电池片需求；右：每GW隔膜片价值量", svg(H, inner),
                  ["资料来源：三环集团H股招股章程，Bloom Energy年报，Hunterbrook，产业链调研；本报告测算。",
                   "注：Bloom电池片需求取0.65到0.8GW；单片25W与32.5W分别对应每GW约4,000万片与3,080万片。"])

# ---------- 图表4 Amosense占比 ----------
H = 838
px0, px1, pb, pt = 170, 1395, 678, 168
def yp(v): return pb - (pb-pt)*v/25
inner = ""
for v in range(0, 26, 5):
    inner += f'<line x1="{px0}" y1="{yp(v)}" x2="{px1}" y2="{yp(v)}" stroke="{GRID}" stroke-width="1.2"/>'
    inner += t(px0-12, yp(v)+6, f"{v}%", 18, INK, "end")
inner += f'<line x1="{px0}" y1="{pt}" x2="{px0}" y2="{pb}" stroke="#AEB5C2" stroke-width="1.5"/><line x1="{px0}" y1="{pb}" x2="{px1}" y2="{pb}" stroke="#AEB5C2" stroke-width="1.5"/>'
inner += t(104, 423, "占Bloom电池片需求的比例", 18, INK, extra='transform="rotate(-90 104 423)"')
inner += f'<line x1="{px0}" y1="{yp(20)}" x2="{px1}" y2="{yp(20)}" stroke="{ORANGE}" stroke-width="3" stroke-dasharray="14 9"/>'
inner += t(px1-20, yp(20)-20, "两成份额：2027年需要月产约100万到200万片", 18, ORANGE, "end", 700)
for cx, lo, hi, fill, lab, lc, dem, xl in [(527, 11.25, 18, "url(#gBlue)", "11%到18%", "#2A2A95", "需求约4,000万到6,400万片", "2026年（全年折算）"),
                                            (1037, 6.0, 11.7, "url(#gPurp)", "6%到12%", "#4A0F7E", "需求约6,150万到1.2亿片", "2027年")]:
    inner += f'<rect x="{cx-92}" y="{yp(hi)}" width="184" height="{yp(lo)-yp(hi)}" rx="6" fill="{fill}"/>'
    inner += t(cx+113, (yp(hi)+yp(lo))/2+7, lab, 18, lc, "start", 700)
    inner += t(cx, yp(lo)+32, dem, 17, GRAY)
    inner += t(cx, pb+30, xl, 19, INK)
charts[4] = frame(H, "月产60万片的Amosense，只够Bloom在2027年需求的一成左右",
                  "按月产60万片满产年化720万片，占Bloom电池片需求的比例", svg(H, inner),
                  ["资料来源：首尔经济新闻，Daily Invest，Bloom Energy年报，产业链调研；本报告测算。",
                   "注：区间两端对应单片25W与32.5W及需求高低；2026年按全年折算，实际占比低于区间。"])

# ---------- 图表5 情景表 ----------
H = 601
heads = ["情景", "电池片层需求", "每GW片数", "三环份额", "单价", "隔膜片收入"]
xs = [57, 272, 488, 716, 905, 1094]
rowsd = [["2026年悲观", "1.3GW", "约3,080万片", "70%", "20元", "约5.6亿元"],
         ["2026年基准", "1.45GW", "约3,330万片", "80%", "23元", "约8.9亿元"],
         ["2026年乐观", "1.6GW", "4,000万片", "90%", "25元", "约14.4亿元"],
         ["2027年悲观", "2.0GW", "约3,080万片", "55%", "19元", "约6.4亿元"],
         ["2027年基准", "2.5GW", "约3,330万片", "70%", "21.5元", "约12.5亿元"],
         ["2027年乐观", "3.0GW", "4,000万片", "80%", "23.5元", "约22.6亿元"]]
inner = f'<rect x="46" y="168" width="1348" height="44" fill="#E8EAF7"/><line x1="46" y1="168" x2="1394" y2="168" stroke="#3B2FB8" stroke-width="3"/>'
for x, h in zip(xs, heads):
    inner += t(x, 197, h, 18, INK, "start", 700, SERIF)
for r, row in enumerate(rowsd):
    y = 212 + r*44.8
    for x, c in zip(xs, row):
        inner += t(x, y+30, c, 18, INK, "start")
    inner += f'<line x1="46" y1="{y+44.8}" x2="1394" y2="{y+44.8}" stroke="{"#3B2FB8" if r==5 else "#D5DBEA"}" stroke-width="{3 if r==5 else 1.5}"/>'
charts[5] = frame(H, "2027年三环隔膜片收入的区间明显变宽，份额与节奏同时起作用",
                  "隔膜片收入＝电池片层需求×每GW片数×三环份额×单价", svg(H, inner),
                  ["资料来源：本报告测算。",
                   "注：每GW片数约3,080万、3,330万与4,000万片分别对应单片32.5W、30W与25W；悲观情景未计入采购低于消耗的消化效应。"])

# ---------- 图表6 时间线（V2内容） ----------
H = 589
nodes = [(158, "10月下旬", "三环三季报", "#123E96", ["看隔膜片或所属", "分部的环比"], ["Bloom环比升而三环降，", "替代型份额流失提前"]),
         (383, "10月29日", "Bloom三季报", "#1E3490", ["看原材料存货与", "供应商预付款"], ["继续快于产品收入，", "采购节奏风险上升"]),
         (608, "11月10日", "稀土管制暂停到期", "#282B8B", ["看中方是否公告续期"], ["美方称已延至1月10日", "钪的出口许可照常执行"]),
         (832, "11月中旬", "Amosense三季报", "#35207F", ["看SOFC收入与扩产公告"], ["月产能达100万片以上，", "二供转为替代"]),
         (1057, "12月31日前", "美国安全港表", "#3F1880", ["看是否覆盖燃料电池"], ["纳入后，合规成本", "将按统一口径核算"]),
         (1282, "2028年前后", "Bloom新一代产品", "#4A0E7A", ["看单片功率与规格"], ["规格变更即打开", "重新认证窗口"])]
inner = f'<line x1="62" y1="325" x2="1148" y2="325" stroke="#C9CFDC" stroke-width="5"/><line x1="1190" y1="325" x2="1378" y2="325" stroke="#C9CFDC" stroke-width="5"/>'
inner += '<line x1="1152" y1="336" x2="1166" y2="314" stroke="#5A6478" stroke-width="3"/><line x1="1172" y1="336" x2="1186" y2="314" stroke="#5A6478" stroke-width="3"/>'
for cx, d, ev, col, watch, impl in nodes:
    inner += t(cx, 197, d, 18, INK, weight=700)
    inner += t(cx, 248, ev, 19, col, weight=700, fam=SERIF)
    inner += f'<circle cx="{cx}" cy="325" r="10.5" fill="{col}"/>'
    y = 375
    for ln in watch:
        inner += t(cx, y, ln, 17.5, "#434D57"); y += 25
    y += 12
    for ln in impl:
        inner += t(cx, y, ln, 17.5, "#6E788C"); y += 26
charts[6] = frame(H, "验证顺序：先看两份三季报，再看二供是否启动下一轮扩产",
                  "各节点的读法与对应的修正条件", svg(H, inner),
                  ["资料来源：各公司公告与监管文件；本报告整理。",
                   "注：横轴为事件先后，非真实时间刻度；12月31日与2028年之间为断轴；日期以公司公告为准。"])

HEIGHTS = {1: 621, 2: 938, 3: 874, 4: 838, 5: 601, 6: 589}
for k, html in charts.items():
    open(f"chart{k}.html", "w", encoding="utf8").write(html)
open("heights.txt", "w").write(" ".join(f"{k}:{v}" for k, v in HEIGHTS.items()))
print("ok")

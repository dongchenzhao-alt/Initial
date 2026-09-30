# OCS 深度研究题目清单（关联热搜关键词优先）

> 信息截至 2026-09-30，不构成投资建议。
> 置信度标注：【H】本轮对照一手原文核实（仅限可以打开的 cloud.google.com 和 anthropic.com）；【M】来自公司公告、电话会纪要，或两个以上互相独立的二手来源，本轮未能重开原文；【L】单一二手来源、摘要级信息、传闻，或存在口径冲突。经 GitHub 快讯存档、财联社、36氪等转引的内容，最高只标【M】。
> 推算：凡写“推算”的数字，都是本文依据公开拓扑或公开数字做的算术，不是公司披露，括号内写明依据。
> 核实条件受限：本轮 WebSearch 配额已用尽，除 cloud.google.com 和 anthropic.com 外，多数站点被出口代理拦截。凡标【M】【L】的内容，引用前都应再核一次原文。

## 一句话结论

OCS 目前只有一个经一手资料确认的规模需求方，即 Google（TPU ICI 加 Jupiter DCN）。Lumentum 有 3 家 OCS 客户、Coherent 已向 7 家客户出货、H+S 拿到一家超大规模客户的订单，但这些客户可能经 Broadcom、Celestica 等渠道指向同一个终端。**商用供应商的多客户数，不等于多个终端需求方。**

所以最值得下功夫的题目围绕四点展开：**TPU 出货 × 每芯片 OCS 端口 × 外采比例 × $/port**；**Google 自研与外采的份额，以及 MEMS 等供给瓶颈**；**中国供应链里哪些收入能被验证**；**OCS 对光模块和交换机究竟是替代还是放大**。

按与 OCS 的关联强度分组：

- 强：TPU。
- 中：光模块（按网络层分，有的层替代，有的层增量）、CPO、存储、国内 CSP。
- 弱至中：PCB/CCL。Google 用 OCS 替代 spine 已是存量，增量只取决于非 Google 客户，证据不足，整体偏弱。
- FCC：对光模块为中，对 OCS 为弱。
- 弱或基本无关：MUSE、WORKBUDDY、SOFC、电池、宁德时代、TEC、保偏光纤、MLCC、RCC、石墨烯。这些题目的主要价值是证伪。

题目排序遵循“关联榜单其他关键词优先”：第一梯队（T1-T5）每题与 ≥2 个其他关键词强/中关联；第二梯队（T6-T11）是 OCS 本体核心问题或中等关联；第三梯队（T12-T15）是弱关联、证伪型题目。

## 关键词释义（本语境）

| 关键词 | 本语境含义 | 与 OCS 的关系 |
|---|---|---|
| OCS | Optical Circuit Switch，光路交换机（A 股常称“全光交换”）。在光层直连端口，不做光电光转换。注意区分运营商传输网的 OXC/ROADM；美股代码 OCS 是眼科药企 Oculis，不相关 | 本体 |
| TPU | Google 张量处理器：Ironwood（第七代），TPU 8t/8i（2026-04-22 发布）。材料领域的 TPU（热塑性聚氨酯）这一歧义不能完全排除，但与 OCS、光模块同榜时可能性低 | 强：OCS 最大需求源 |
| 光模块 | 800G/1.6T 可插拔模块。OCS 链路需要能容纳额外插损、配环形器实现单纤双向的定制模块 | 中：按网络层分，有的层替代，有的层增量 |
| CPO | 共封装光学（光引擎加外置激光源 ELS） | 中：GPU scale-up 光化时可能与 OCS 互补，也可能分流预算（集中在 T6 讨论） |
| PCB / CCL | AI 交换机板、计算托盘、midplane 及其覆铜板（M8/M9） | 弱至中：Google 用 OCS 替代 spine 已是存量；增量只取决于非 Google 客户，证据不足，整体偏弱。OCS 整机本身的 PCB 价值量很小 |
| RCC | 涂树脂铜箔（Resin Coated Copper），用于 HDI 增层 | 弱：没有已知传导链，AI 板上的批量应用也未核实 |
| MLCC | 多层陶瓷电容，AI 服务器供电链用量大 | 弱：OCS 电子 BOM 很小 |
| 存储 | DRAM/HBM/NAND 超级周期 | 中：通过 capex 价格效应和 HBM 数量约束，影响 TPU 与 OCS 出货 |
| MUSE | 大概率指 Meta 于 2026-09-08 发布的个人 AI Agent “Muse”【M】，底座为 2026-04 发布的 Muse Spark 模型【M】 | 弱：没有证据显示 Meta 部署 OCS，也没有证据显示 Muse 使用 TPU |
| WORKBUDDY | 腾讯全场景办公 AI Agent：2026-02-06 内测、2026-03-09 正式发布【L】，2026-05-29 面向海外用户上线【L】 | 弱：只有股价层面的情绪联动 |
| FCC | 美国联邦通信委员会：Covered List 组件级新规【M】，以及据报在起草的中国产新型号光收发器进口限制【M】 | 对光模块：中；对 OCS：弱（新规针对 Covered List 实体的含逻辑组件，中国光模块厂和纯无源光学件都不在范围内） |
| 国内CSP | 阿里、腾讯、字节、百度，以及运营商云 | 中：潜在的第二需求池，但尚无公开的批量采购 |
| SOFC | 固体氧化物燃料电池（Bloom 为代表），AI 数据中心“表后”快速上电电源 | 弱：只影响上电节奏（推断），可作电价锚 |
| 电池 / 宁德时代 | AIDC 储能（机柜 BBU、园区 BESS），宁德时代 | 弱：与 OCS 没有产业传导。GB300 的功率平滑可能主要靠电容，而非锂电池【L，未核实】 |
| TEC | 热电制冷器，用于激光器和光模块温控 | 弱：“OCS→WDM→TEC”不成立（CWDM 可用非制冷方案） |
| 保偏光纤 | PMF，用于 CPO 外置光源到硅光引擎的连接 | 弱：MEMS OCS 用标准单模光纤，液晶 OCS 在内部用双折射晶体处理偏振 |
| 石墨烯 | 2026 年 A 股材料题材（德尔未来等） | 无可投资传导 |

## OCS 基线速览

- **已落地的部署（均为 Google）**
  - OCS 于 2013 年首次投产【H】。此后 Jupiter 演进为以 OCS 取代 spine 的直连拓扑（2022 年披露），到 2022 年已成为 Google 绝大多数数据中心网络的基础【H】。与已知最佳替代方案相比，功耗低 40%、成本低 30%。这是 OCS、直连拓扑和 SDN 流量与拓扑工程整体架构的收益，不是 OCS 单独带来的【H】。
  - TPU v4 用 OCS 互联 4,096 颗芯片。Google 博客称 OCS 及光器件占系统成本不到 5%、功耗不到 5%【H】；论文摘要写的是功耗不到 3%，并称用 48 台 OCS【M，论文本轮未重开】。
  - Ironwood 由 144 个 64 芯片 cube 经 OCS 组成 9,216 芯片的 superpod，OCS 负责旁路故障 cube 和切片；多个 superpod 之间经 Google 所称的“标准 DCN”互联【H】。这个标准 DCN 就是 Jupiter，而 Jupiter 本身以 OCS 为骨干。
  - TPU 8i 的 Boardfly 拓扑中，36 个组之间经 OCS 互联【H】。
  - **反向证据与未知项**：TPU 8t（9,600 芯片 3D torus）的官方文章没有提到 OCS；新的 scale-out 网络 Virgo 是高 radix 电交换组成的两层结构，同样没有提到 OCS【H】。Google 称借 Virgo 可以把超过 100 万颗 TPU 跨多个数据中心站点组成一个训练集群，跨站点这一层用什么交换，没有披露【H】。“没提”不等于“没用”。
- **每芯片端口数（推算值，不是官方披露；均假设每条双向链路占 1 个 OCS 端口）**
  - v4 约 1.5（48 台 × 128 口 = 6,144 个端点，对 4,096 颗芯片）。
  - Ironwood 约 1.5（144 个 cube × 每 cube 96 条光链路 = 13,824 个端点）。
  - TPU 8i 约 1.25（36 组 × 8 板 × 每板 5 条组外链路 = 1,440 条，对 1,152 颗芯片）。
- **端口与台数口径冲突（本文统一按端口数和 $/port 建模，台数只作派生指标）**
  - Google Palomar 为 136×136、128 口可用【M】。
  - 若 Ironwood 的 13,824 个端点仍只用约 48 台 OCS（SemiAnalysis 转述【M】），单台需约 288 口，与 136 口的 Palomar 不兼容；若用 Palomar，约需 108 台（推算）。
  - “N×N”按单侧还是双侧计、是否用环形器，会让台数和单价口径相差约 2 倍。
  - Ironwood 和 TPU 8t 用的是什么规格的 OCS，没有披露。
- **技术路线**：MEMS（Google Palomar，Lumentum R300/R64）、液晶（Coherent DLX）、压电（H+S Polatis）、硅光（iPronics、nEye）、机器人配线（Telescent）。插损大致为：压电约 1dB，MEMS/液晶约 2-3dB，硅光约 6dB【M】。
- **市场预测**
  - Cignal AI：2025-12 预测 2029 年外部市场至少 25 亿美元；2026-02 因 TPU 部署加速上调；2026-07 预测 2030 年超过 80 亿美元，上调主要来自 GPU scale-up 假设【M，原文本轮未重开，各来源对发布日期的口径不一】。
  - 其他口径：Redburn 预测 2030 年 62 亿美元【L】；Coherent 把 OCS 可寻址市场上调至 40 亿美元以上【M】。
- **商用玩家**
  - Lumentum
    - FY26 OCS 收入超过 9,000 万美元（业绩发布 2026-08-11，10-K 提交 2026-08-17）【M】。
    - 指引 FY27 Q1（2026 年 7-9 月）为首个单季超 1 亿美元的季度【M】。
    - OCS 在手订单约 4 亿美元，来自 3 家客户（FQ2 FY26 电话会，2026-02-03）【M】。
    - CY26 下半年 OCS 出货约 4 亿美元的目标【M，二手汇总】；CEO 称 2027 年初成为 OCS 第一大供应商【M，电话会纪要转述】。
    - 德银科技会议称 OCS 出货环比翻倍、OCS TAM 高于约 80 亿美元【L，摘要级，会议日期口径不一】。
    - “2027 年初出货超过最大客户的自研量”“实际上是唯一的商用供应商”【L，单一二手】。
  - Coherent：已向 7 家客户出货（FQ1 FY26 电话会，2025-11-06），接洽超过 10 家（FQ2，2026-02-04）【M】；未单独披露 OCS 收入。
  - H+S：2025 年拿到一家全球超大规模客户的 Polatis 大订单；波兰新工厂目标 OCS 产能提升 5 倍以上；因提前投入，Communication 分部利润承压【M】。
  - Silex（MEMS 代工）：2026-05-07 在斯德哥尔摩上市，二季度称数据中心光开关需求强、正在扩产【M】。为 Google 代工只是市场普遍看法。
  - 英伟达 2026-03 分别投资 Lumentum 和 Coherent 各约 20 亿美元，但协议未明确包含 OCS【M】。
- **中国产业链的位置**
  - 已有公告支撑的收入或订单：腾景（二维准直器）、炬光（微透镜阵列已量产）、罗博特科/ficonTEC（封装整线）【M】。
  - 整机厂多处于样机或展示阶段：光迅 320×320、旭创 TeraHop 300×300、新易盛 NX300【M】。
  - 德科立公告称硅基 OCS 未计入未来 2-3 年营收规划【M】。
  - 赛微北京 MEMS-OCS 仍在试产【M】。

## 关键词关联矩阵

●强　○中　·弱　（空白表示无关联）

| 题目 | PCB | MUSE | 存储 | MLCC | 光模块 | RCC | SOFC | CPO | WORKBUDDY | 电池 | 宁德时代 | FCC | CCL | TEC | TPU | 石墨烯 | 国内CSP | 保偏光纤 | 关联数 | 其中强/中 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T1 光模块净效应 | · |  |  |  | ● |  |  | ○ |  |  |  |  | · |  | ● |  |  |  | 5 | 3 |
| T2 需求弹性 |  | · | · |  | ○ |  |  |  |  |  |  |  |  |  | ● |  |  |  | 4 | 2 |
| T3 中国链真伪 |  |  |  |  | ○ |  |  |  |  |  |  | · |  |  | ● |  | ○ |  | 4 | 3 |
| T4 存储约束 |  |  | ● |  | ○ |  |  | · |  |  |  |  |  |  | ● |  | · |  | 5 | 3 |
| T5 国内CSP/全光交换 |  |  | ○ |  | ○ |  |  |  | · |  |  | · |  |  |  |  | ● |  | 5 | 3 |
| T6 英伟达scale-up | · |  |  |  | ○ |  |  | ○ |  |  |  |  | · |  | · |  |  |  | 5 | 2 |
| T7 交换机PCB/CCL | ○ |  |  |  |  |  |  | · |  |  |  |  | ○ |  | ○ |  |  |  | 4 | 3 |
| T8 供给与份额 |  |  |  |  | · |  |  |  |  |  |  |  |  |  | ● |  |  |  | 2 | 1 |
| T9 路线与$/port |  |  | · |  | ○ |  |  | · |  |  |  |  |  |  | ○ |  |  |  | 4 | 2 |
| T10 TPU外部化 |  | · |  |  | · |  |  |  |  |  |  |  |  |  | ● |  |  |  | 3 | 1 |
| T11 美中管制 |  |  |  |  | ○ |  |  |  |  |  |  | · |  |  | · |  |  |  | 3 | 1 |
| T12 Agent推理证伪 |  | · | ○ |  | · |  |  |  | · |  |  |  |  |  |  |  | ○ |  | 5 | 2 |
| T13 保偏/TEC证伪 |  |  |  |  | ○ |  |  | ○ |  |  |  |  |  | · |  |  |  | · | 4 | 2 |
| T14 电力节奏 |  |  |  | · | · |  | · |  |  | · | · |  |  |  | ○ |  |  |  | 6 | 1 |
| T15 电子BOM/RCC/石墨烯 | · |  |  | · |  | · |  |  |  |  |  |  | · |  |  | · |  |  | 5 | 0 |

说明：
- **排序规则**：先看与榜单其他关键词的强/中关联数（末列），再看投资者关注度。只有弱关联撑起来的题目，一律放第三梯队。
- 关联数多，不代表关联强。T12 到 T15 覆盖的关键词不少，但几乎都是弱关联，所以排在第三梯队。
- T8（供给与份额）和 T9（技术路线与 $/port）是 OCS 本体的核心估值问题，只是关联关键词少，按规则排在第二梯队。从估值角度，它们应与 T2 一起做（见“研究优先级建议”）。
- 每题的“关联关键词”与本矩阵逐行一致。

---

## 第一梯队：与 ≥2 个其他关键词强/中关联，且投资者高度关注

### T1｜分 ICI、DCN、scale-out 三层看，OCS 对每颗 TPU 的光模块数量和价值量，净效应是增加还是减少？

- **关联关键词**：光模块●、TPU●、CPO○、PCB·、CCL·
- **核心问题**
  - ICI 层：每条 OCS 链路都需要 OCS 兼容模块，要容纳约 2-3dB 额外插损、配环形器，是增量。
  - DCN 层（Jupiter）：去掉 spine，理论上该层模块最多减半，是替代；同时挤出该层交换机板（PCB/CCL 的影响见 T7）。
  - Virgo scale-out 层：电交换，光模块需求与 OCS 无关。
  - 三层合计后，每颗 TPU 对应的净变化是多少？
- **为什么重要**
  - 光模块是 A 股市值最大的 AI 硬件板块。“OCS 去 spine、利空光模块”的说法只适用于 DCN 层，直接套到 AI 集群会得出错误结论。
  - TrendForce 称约 400 万颗 TPU 带动 800G 以上模块需求超过 600 万只【L】，隐含每芯片约 1.5 只。这个数与拓扑推算不一致：接 OCS 的 TPU 仅 ICI 一层就约 1.25-1.5 只/芯片（假设一个链路端点对应一只模块），再加 DCN 和 Virgo（每芯片带宽为上一代的 4 倍【H】）的模块，总数应明显高于 1.5；而且 400 万颗里还包括不接 OCS 的 v5e/v6e。所以这个 1.5 要么没计入 ICI，要么把 1.6T 按一只承载两条链路计，要么两边口径根本不同，或者存在低估。它不能当校验锚点，只能列为需要拆解的子问题。
- **研究子问题**
  1. 拆解 TrendForce“每芯片约 1.5 只”的口径：计了哪些网络层，速率怎么折算，是否包含 v5e/v6e。
  2. ICI 每条链路的速率是多少？按每芯片 1.2TBps 双向、6 个端口粗算，每端口约 800G。卖方“每 pod 13,824 只 1.6T”的说法是否重复计算（如果一只 1.6T 模块承载两条链路，只数应减半）【L】？
  3. 环形器让 OCS 端口数和光纤数减半。环形器放在模块内还是外置，决定模块只数和单价（价值归属见 T9）。
  4. OCS 兼容模块比标准 DR 模块贵多少？可以从供应商的毛利率和产品结构倒推。
  5. Virgo 称每颗 TPU 8t 的带宽为上一代的 4 倍，这部分与 OCS 无关的模块拉动有多大？
  6. LPO 能否用在 OCS 路径上？OCS 和环形器的插损会压缩链路预算。
  7. 与英伟达 GB300/Rubin（铜 scale-up 加光 scale-out）相比，每个 XPU 的光模块价值量谁更高？
- **跟踪指标与数据源**：Google Cloud TPU 文档（ICI 端口和带宽）；LightCounting 按客户拆分的数据；中际旭创、新易盛的季度收入、1.6T 占比和毛利率；Coherent OCS 专用模块的相关表述【M】。
- **多空分歧**
  - 多方：OCS 让万卡级光学 scale-up 在经济上可行，ICI 层是纯增量；OCS 专用模块单价更高；Virgo 带宽 4 倍。
  - 空方：DCN 层减少模块数量；cube 变大后配比下降；如果 1.6T 是一只模块承载两条链路，只数减半；Google 定制化让价值集中在少数供应商手里。
- **相关标的**（统一按光模块业务的 Google 链暴露度分类）
  - 核心受益（Google 链暴露为卖方普遍口径，均未经一手核实【L】）：中际旭创 300308、新易盛 300502、Coherent (COHR，另有 OCS 专用模块产品【M】)
  - 验证中：Lumentum (LITE，光模块业务的 Google 链暴露未见公开证据，其 OCS 业务见 T2、T8)、福晶科技 002222（环形器晶体，与 Google 链的对应关系未核实）
  - 概念：无

### T2｜2026-2028 年，“OCS 互连的 TPU 出货 × 每芯片端口 × 外采比例 × $/port”能否支撑 Lumentum/Coherent 的 OCS 收入跃升？

- **关联关键词**：TPU●、光模块○、MUSE·、存储·
- **核心问题**：把商用 OCS 收入的增量拆成四个来源：Google 端口总需求扩张；Google 外采比例提升（供给侧见 T8）；TPU 部署到 Google 以外的机房（见 T10）；Google 以外的新终端客户（GPU 见 T6，国内见 T5）。本题负责总框架，统一以端口数和 $/port 建模，台数只作派生指标。
- **为什么重要**
  - Lumentum 已给出密集的 OCS 指引（均待对照原文）：FY26 收入超过 9,000 万美元【M】；FY27 Q1 首个单季超 1 亿美元【M】；CY26 下半年出货约 4 亿美元【M】；CEO 称 2027 年初成为第一大供应商【M】；德银会议称出货环比翻倍、TAM 高于约 80 亿美元【L】。市场对 LITE 的定价已高度依赖 OCS 放量（分析判断，本文未做估值拆分）。
  - 官方确认 Ironwood 和 TPU 8i 都用 OCS【H】，“新一代 TPU 弃用 OCS”这一空头逻辑暂时没有证据支持。但 TPU 8t 和 Virgo 的官方文章都没写 OCS。如果 8t 不用，按训练 torus 线性外推的 TAM 会被高估。
  - 端口量级：约 400 万颗 TPU（TrendForce 2026 年口径【L】）× 每芯片 1.25-1.5 个端口，端口需求上限约 500-600 万个（推算，未扣除不接 OCS 的 v5e/v6e）。二手台数口径（2026 年 Google 需 1.5 万台、其中 3,000 台外采；或需 2 万台以上【L】）按 300 口折算为 450-600 万个端口，量级落在上限内，但完全依赖“单台 300 口”的假设，见基线中的口径冲突。
  - 多客户数不等于多终端：Lumentum 的 3 家、Coherent 的 7 家、H+S 的 1 家超大规模客户，可能都指向 Google。
- **研究子问题**
  1. TPU 8t 的 9,600 芯片 superpod 是否沿用“64 芯片 cube + OCS”？若沿用，150 个 cube × 96 = 14,400 个端点（推算）。ISCA 2026（6 月）和 Hot Chips 2026（8 月下旬）已经开过，先查有无 TPU 8 拓扑披露（本轮未能核实）。
  2. v5e/v6e 这类不接 OCS 的 TPU 在 2026-2027 年出货中占多少？这是附着率的扣减项。
  3. 各代所用 OCS 的规格与计数口径：Palomar 136×136、300×300 级、SemiAnalysis 转述的 144×144；N×N 按单侧还是双侧计。据此由端点数派生台数。
  4. 统一 $/port 锚点：128 口 MEMS 从 5-6 万美元降到 3-4 万美元，折合约 390-470 美元/端口降到约 230-310 美元/端口【L】；“300 口级每台 10-12 万美元”折合约 330-400 美元/端口【L，推算】；国内卖方另有每台 15-20 万美元的假设【L】，按 300 口折合约 500-670 美元/端口。再用 Lumentum FY27 Q1 超 1 亿美元倒推：按 230-470 美元/端口，约对应每季 21-43 万个端口；对照端口上限（季均约 125-150 万个），隐含 Lumentum 份额约 14-35%（均为推算，只作量级检验）。
  5. 客户映射：把 Lumentum 的 3 家客户（其中 2 家贡献主要量【L】）、Coherent 的 7 家出货客户、H+S 的超大规模客户，逐一映射到终端客户。是 Google 直采，经 Broadcom（TPU 整机柜）或 Celestica（据报代工 Palomar【L】）等渠道下单，还是 Meta、微软的评估订单（Cignal 称两者仍在评估【L】）？
  6. Lumentum 2026-03 所谓“数十亿美元级多年期 OCS 协议”，交易对手是谁？是否与英伟达的投资协议被混为一谈【L】？
- **FY27 Q1 财报的检验标准（Lumentum、Coherent 约 2026-11 上旬发布）**
  - Lumentum OCS 收入是否超过 1 亿美元。若低于指引，要分清是需求问题还是供给问题（见 T8）。
  - 若 CY26 下半年约 4 亿美元的出货目标成立，而 FY27 Q1 落在 1-1.5 亿美元，则 FY27 Q2（10-12 月）需要约 2.5-3 亿美元（推算；出货与收入确认的口径可能不同）。看 Q2 指引能否匹配。
  - 客户数是否从 3 家增加，是否出现可识别的非 Google 终端；在手订单和毛利率的表述。
  - Coherent 是否首次单独披露 OCS 收入，7 家出货客户中有几家转入量产。
- **跟踪指标与数据源**
  - Lumentum、Coherent FY27 Q1 财报：OCS 收入、在手订单、客户数
  - Google Cloud 技术博客；后续 Hot Chips 2027、ISCA、SIGCOMM 上的拓扑披露
  - 博通 AI 收入；Alphabet capex（2026 年指引已上调至 1,950-2,050 亿美元【M】）
  - Cignal 季度 OCS 报告（port/XPU 配比、$/port）
- **多空分歧**
  - 多方：OCS 在 Ironwood 和 8i 中是标配【H】；Anthropic 计划使用最多 100 万颗 TPU，2027 年起还有数 GW 下一代 TPU 容量【H】；Lumentum 在手订单约 4 亿美元【M】。
  - 空方：需求几乎只来自 Google 一家，多家“客户”可能是同一终端；8i 每芯片端口数略低于 Ironwood；8t 和 Virgo 都没提 OCS；价格下降可能快于端口增长；TPU 出货上限还受 HBM 约束（见 T4）。
- **相关标的**
  - 核心受益：Lumentum (LITE)、Coherent (COHR)、Alphabet (GOOGL)
  - 验证中：Broadcom (AVGO)、Celestica (CLS)、Silex Microsystems、赛微电子 300456（持有 Silex 约 45% 股权，IPO 后比例待核）
  - 概念：无

### T3｜A 股“OCS 概念股”中，哪些有公告层面可验证的 OCS 订单或收入？它们在哪个 BOM 环节，单台价值量和议价权如何？

- **关联关键词**：TPU●、光模块○、国内CSP○、FCC·
- **核心问题**：逐家核对 OCS 相关的订单、收入和客户，把真实收入和概念分开，再按 MEMS、准直器、透镜、整机、封装设备等环节做价值分配。
- **为什么重要**
  - 2026-04-02 工信部发文后，次日 OCS 概念全板块大涨，德科立 20cm 涨停【M】。但德科立当晚公告称：硅基 OCS 未计入未来 2-3 年营收规划，没有海外主流厂商批量订单，32×32 产品只有样品订单【M】。
  - 腾景的 OCS 订单累计约 1.76 亿元【M】；罗博特科两条 OCS 封装整线合计约 1,716 万欧元【M】。
  - 自媒体流传的“光库代工 Google OCS 超 70% 份额”没有依据【L】。
  - FCC 新规对无源光学件基本没有直接影响；整体管制风险见 T11。
- **研究子问题**
  1. 腾景 1,280 万美元二维准直器订单来自“某客户子公司”，客户是谁、对应哪条技术路线？公司称液晶路线已批量交付，客户是否为 Coherent？2027 年订单可见度如何？
  2. 炬光称 OCS 用 N×N 微透镜阵列已在主要客户处量产，对应哪家客户？收入占比多少？有没有锁量或提价？
  3. 罗博特科两条整线对应多少台/年的 OCS 产能？客户“瑞士头部公司 C”是否为 H+S？会不会有复购？
  4. 赛微的 look-through 估值：Silex IPO（2026-05-07）后持股比例是否被稀释？按 Silex 市值折算的持股价值，与赛微自身市值相比如何？赛微北京 MEMS-OCS 何时量产？
  5. 待证伪名单：太辰光、福晶、仕佳光子、天孚通信、东田微、光库。在公司层面确认 OCS 供货之前，一律归为概念。
  6. 国内供应商所在的环节，是不是 T8 所说的供给瓶颈？只有处在瓶颈环节，才谈得上议价权。
  7. 把海外链订单与国内运营商、CSP 订单分开统计。国内目前没有公开的数据中心 OCS 批量采购，国内需求池见 T5。
- **跟踪指标与数据源**：巨潮资讯的重大合同公告和异动公告；互动易、上证 e 互动；定期报告中光交换业务的收入和合同负债；Silex 季报和股东结构；Lumentum、Coherent 10-K 中的供应商风险披露；减持公告（炬光已有股东减持【M】）。
- **多空分歧**
  - 多方：精密无源光学是中国供应链的强项，已有三家有公告层面的订单或量产；瓶颈环节有定价权。
  - 空方：多数公司 OCS 收入占比很小；客户签保密协议，外界难以验证；国产 MEMS 尚未量产；大股东借题材减持。
- **相关标的**
  - 核心受益（有公告支撑）：腾景科技 688195、炬光科技 688167、罗博特科 300757
  - 验证中：赛微电子 300456、德科立 688205、光迅科技 002281、中际旭创 300308、新易盛 300502、光库科技 300620、啟碁 6285.TW（相关报道为【L】）
  - 概念：太辰光、福晶科技、仕佳光子、天孚通信、东田微（在 OCS 环节）

### T4｜存储涨价和 HBM 分配，会不会在 2027 年从价格和数量两个方向压低 TPU 出货和 OCS 端口需求？

- **关联关键词**：存储●、TPU●、光模块○、CPO·、国内CSP·
- **核心问题**
  - 价格层：capex 上修中已出现“内存税”。据二手转述，微软称约 250 亿美元 capex 增量来自组件和内存涨价【L，单一转述，待对照纪要】；亚马逊把 2026 年 capex 上调至约 2,200 亿美元【M】，管理层部分归因于内存成本【L，二手转述】。
  - 数量层：HBM 2026 年已全部签约，据报 2027 年更紧，HBM3E/HBM4E 每片晶圆挤占 3-4 片常规 DRAM【L】。
  - 两者会不会共同封顶加速器出货，进而封顶 OCS 需求？
- **为什么重要**
  - 存储和光通信是最拥挤的两条 AI 硬件主线，共用同一个 capex 预算池。
  - DRAM 合约价环比：1Q26 约 +93~98%，2Q26 +58~63%，3Q26 预测 +13~18%【L，经单一二手数据集转引 TrendForce，待对照原稿】。涨价放缓后，预算可能释放给数量。
  - OCS 只占系统成本不到 5%（TPU v4 口径【H】）。按理它对预算的敏感度应低于可插拔模块，但出货与 pod 部署同步。国内 CSP 同样受存储涨价挤压（见 T5）。
- **研究子问题**
  1. GOOGL、MSFT、AMZN、META 在 3Q26 电话会中对“component pricing/memory”有没有量化表述？
  2. 2027 年 HBM 在 NVIDIA、博通/Google、AMD、Trainium 之间如何分配？TPU 8t 每颗 216GB、8i 每颗 288GB【H】，乘以出货预期后缺口有多大？
  3. TPU 8t 的 HBM 带宽（约 6.5TB/s）低于 Ironwood（7.4TB/s）【H】，这是成本或供给约束下的取舍吗？
  4. 每 GW capex 中光互联（光模块、CPO、OCS）的价值量能升多少？TPU 出货若因 HBM 约束下修 10%，OCS 指引的弹性有多大？
  5. 供给何时放松？长鑫 2026-07-27 上市、募资 579 亿元【M】，以及 2027-28 年海外新厂。
- **跟踪指标与数据源**：美光 FQ4'26（2026-09-30 盘后发布，本文未纳入）及 FQ1'27 指引（此前 FQ3'26 营收 414.6 亿美元、FQ4 指引 500 亿美元【M】）；TrendForce 合约价；SK 海力士、三星的 HBM 客户结构；TSMC CoWoS 分配；韩国出口数据。
- **多空分歧**
  - 多方：2026 年的价格效应是在 capex 上做加法，没有证据显示挤出光互联；2027 年涨价放缓会释放数量；HBM 稀缺时，客户更看重 OCS 带来的集群可用性。
  - 空方：2027 年 capex 增速放缓而 LTA 锁定高价，加速器数量受压；HBM 分配向 NVIDIA 倾斜，TPU 出货低于需求。
- **相关标的**
  - 驱动变量（存储侧）：美光 (MU)、SK 海力士、三星
  - 受约束方（OCS 侧）：Alphabet (GOOGL)、Broadcom (AVGO)、Lumentum (LITE)
  - 概念：把存储股直接视为“OCS 受益股”

### T5｜国内 CSP 能否在 2027-2028 年形成 OCS 第二需求池？政策里的“全光交换”指的是 OCS 还是 OXC？

- **关联关键词**：国内CSP●、存储○、光模块○、WORKBUDDY·、FCC·
- **核心问题**
  - 国产超节点之间用直连拓扑还是交换式 fabric？只有前者对 OCS 有刚性需求。Google TPU 8i 说明，非 torus 的直连拓扑同样会用 OCS【H】。
  - HBM 受管制后，国内走“以光补存”路线：CM384 用 6,912 个 400G LPO 模块，每卡约 18 个，其中 scale-up 约 14 个【M】。这种架构是光模块加电交换，不是 OCS。
- **为什么重要**
  - 这是 A 股 OCS 的第二条估值逻辑，也是最容易被高估的一环。
  - 初步判断：工信部 2026-04-02 文件的措辞是“推动全光交换等技术应用部署，降低算力应用终端到服务器的网络时延”（普惠算力场景）【M】，指向接入和城域网络，更像运营商全光网或 OXC，不是数据中心内部的 OCS。这一判断待原文确认。它是证伪 2026-04 行情成本最低的一步。
  - 2026-06-10 的《“人工智能+信息通信”创新发展实施意见》（工信部通信〔2026〕121号）提出全光交换器件和光电共封装器件的“研发验证”，以及“光电混合组网试验”【M，经财联社摘录转引】。两份文件都不是部署配额。
  - 阿里云和中国移动研究院在 2026-07-23 的论坛上介绍了 OCS 演进思路，移动云考虑用 OCS 替代 super spine；目前没有公开集采【M】。
  - WorkBuddy 等 Agent 应用对国内推理集群规模的拉动，见 T12。
- **研究子问题**
  1. 核实 2026-04-02 文件的文号和原文全文：用的是“全光交叉/OXC”还是“光路交换/OCS”？
  2. 三大运营商集采里有没有数据中心 OCS 标包？
  3. Atlas 950（8,192 卡）和 960（15,488 卡）扩展为 SuperCluster 时，超节点之间用 UB/以太网电交换还是 OCS？
  4. 阿里 HPN 下一代架构、腾讯星脉、字节网络的论文和专利中，有没有 OCS？
  5. 国产 MEMS（赛微北京、光迅自研）在良率和价格上与 Silex 差多少？美中管制（T11）会不会推动国内 CSP 更快导入国产 OCS？
  6. 长鑫上市扩产、国产 HBM 改善后，超节点规模和每卡光模块用量会不会下降？
- **跟踪指标与数据源**：工信部政策原文；中国移动、中国电信的招标网；阿里、腾讯、百度的季度 capex；华为全联接大会；SIGCOMM、OFC 论文；德科立、光迅的投资者关系活动记录。
- **多空分歧**
  - 多方：国产超节点规模大、功耗约束紧，OCS 在容错和分期扩容上的价值更突出；国产链条完整。
  - 空方：公开架构都是以太网电交换，没有批量采购；政策语义偏运营商 OXC；国内 capex 首先受芯片供给约束。
- **相关标的**
  - 核心受益：无
  - 验证中：光迅科技 002281、德科立 688205、中兴通讯 000063、赛微电子 300456
  - 概念：把“全光交换”政策直接等同于数据中心 OCS 订单

---

## 第二梯队：OCS 本体核心问题（关联关键词较少）或中等关联

### T6｜英伟达 GPU scale-up 会在 2028 年前引入 OCS 吗？CPO 与 OCS 是先后关系还是替代关系？

- **关联关键词**：光模块○、CPO○、PCB·、CCL·、TPU·
- **核心问题**：Cignal 2026-07 的上调主要来自 GPU scale-up【M】。其依据是“英伟达计划在 Rubin Ultra NVL576 引入 OCS、2028 年放量”，这只是 Cignal 的说法，英伟达没有公开确认【L】。Cignal 在 2026-02 的报告里还写过 2029 年前 GPU scale-up 采用有限【M】。CPO 与 OCS 的关系集中在本题讨论。
- **为什么重要**
  - 如果 GPU 部分被证伪，可以用 Cignal 2025-12 的口径（2029 年外部 OCS 市场至少 25 亿美元【M】）近似“以 Google 为主”的情景。两者年份和口径都不同，只能作量级参照（推算）。
  - 据 SemiAnalysis（经 CNBC 转述，2026-07-06）报道，Kyber 机柜因 PCB 中板制造问题推迟到 2028 年；英伟达回应称“路线图不变”【M】。
- **研究子问题**
  1. NVL576 指哪种形态？GTC 2025 的口径是 576 个 die，另一种说法是 8 个 Oberon 机柜。OCS 在其中用于机柜间重构、容错，还是作为主干？
  2. 英伟达分别投资 Lumentum、Coherent 各约 20 亿美元，协议附件（8-K、10-K）里有没有 OCS 条款？
  3. 英伟达据报参投 iPronics 1.25 亿美元 B 轮（2026-09-02）【M】，是否说明它偏好微秒级切换的硅光路线？硅光约 6dB 的插损能否满足 scale-up？
  4. 如果 scale-up 引入 OCS，每颗 GPU 对应多少端口？以 TPU 每芯片 1.25-1.5 个端口为锚点做情景测算。
  5. CPO 与 OCS 在 scale-up 中是先后关系（先有光口才能插 OCS），还是替代关系（高 radix CPO 交换减少重构需求）？CPO 外置光源的功率预算能否穿过 OCS 和两个环形器的插损（对保偏光纤、TEC 的影响见 T13）？另据二手转述，Google 以可靠性为由暂不采用 CPO【L】。
- **跟踪指标与数据源**：GTC 2027 和 OFC 2027（约 2027-03）；Cignal 季度模型的修订；Lumentum、Coherent 电话会中关于 GPU 客户的表述；iPronics、nEye 的客户公告；SemiAnalysis 对 Kyber 进度的跟踪。
- **多空分歧**
  - 多方：铜缆的距离和带宽有物理极限，scale-up 光化难以避免；英伟达在光学领域投资密集；一旦起量，端口规模会远超 TPU。
  - 空方：英伟达从未公开提过 OCS；Cignal 的假设半年内剧烈变化；Kyber 可能延迟；MEMS 的毫秒级切换未必满足 GPU 的容错需求；高 radix CPO 交换可能直接绕开 OCS。
- **相关标的**
  - 核心受益：无（尚未验证）
  - 验证中：NVIDIA (NVDA)、Lumentum (LITE)、Coherent (COHR)、iPronics（未上市）、nEye（未上市）
  - A 股：没有经确认的 OCS 暴露。天孚通信（英伟达 CPO 伙伴名单中的 TFC【M】）属于 CPO 链，不等同于 OCS 受益。
  - 概念：把 PCB/CCL 股纳入 OCS 研究（例如因 Kyber 中板）。中板问题只是时间表的风险指标。

### T7｜OCS 取代 spine 以后，AI 交换机的 PCB/CCL 需求是被“削量”，还是被 TH6/1.6T 的“升规”对冲？

- **关联关键词**：PCB○、CCL○、TPU○、CPO·
- **核心问题**：Google 对 spine 的替代属于存量：OCS 2013 年投产，2022 年已构成其“绝大多数数据中心网络”的基础【H】。新增变化只可能来自其他超大规模厂商。按拓扑推算，替代上限为两层 Clos 交换机台数的约 1/3、三层的约 1/5（推算）。
- **为什么重要**：这是“OCS 利空交换机 PCB”的叙事能否成立的问题，目前证据不足以下结论。
  - Ironwood 多个 superpod 之间经 Google 所称的“标准 DCN”互联【H】。Google 的标准 DCN 就是 Jupiter，而 Jupiter 本身已用 OCS 取代 spine【H】。所以这条事实不能说明电交换没有被 OCS 替代。
  - TPU 8t 的 scale-out 网络 Virgo 公开描述为高 radix 电交换两层结构，没有提到 OCS【H】。这是唯一可用的反证，但“没提”不等于“没用”，只算弱反证。
  - 结论：Google 内部已有的替代不产生增量；非 Google 客户会不会在 AI 集群 spine 层采用 OCS，没有公开数据。
- **研究子问题**
  1. Meta、微软、英伟达 Spectrum-X 客户分别在哪一层部署 OCS（DCI、spine、跨柜 scale-up）？部署了多少端口？
  2. 建一个换算模型：1 个 OCS 端口替代多少 spine 交换端口，对应多少台交换机、多少平方米高多层板、多少张 M8/M9 CCL；同时计入 spine 侧光模块的减少和 OCS 兼容模块单价的上升（见 T1）。
  3. Virgo 的两层是否都是电分组交换？跟踪 Google 在 SIGCOMM、OFC、OCP 的后续披露。
  4. TPU 系统没有类似 NVSwitch 的交换托盘，每颗加速器对应的交换板价值量是否结构性偏低？这是推断，目前没有 BOM 数据。
  5. 英伟达计算托盘 midplane 与 Kyber 正交背板要分开看。二者都在柜内，与跨柜 OCS 基本是互补关系。
  6. CPO 交换机（TH6-Davisson、Spectrum-X Photonics）的交换机 PCB 和基板价值量，相对可插拔方案是升还是降？
  （RCC 的证伪放在 T15。）
- **跟踪指标与数据源**：Arista、Celestica、智邦的交换机收入；沪电股份企业通讯板收入；台光电月营收和 M8/M9 占比；Dell'Oro 交换机端口数据；Google 网络论文与博客。
- **多空分歧**
  - 多方：Google 的替代是存量；Google 的 AI 后端横向网络（Virgo）公开描述仍为电交换，且每加速器带宽提升到 4 倍【H】；CPO 交换机带来更大尺寸的板。
  - 空方：如果非 Google 客户在 2027-28 年把 OCS 推进到 AI 集群的 spine 层，交换机台数增速会被削减（理论上限 20-33%，推算）；如果日后披露 Virgo 的某一层使用 OCS，对冲逻辑会被削弱。
- **相关标的**
  - 核心受益：无（本题主要用于识别风险）
  - 验证中：沪电股份 002463、生益科技 600183、台光电 2383.TW、Arista (ANET，被挤出一方)
  - 概念：把 OCS 叙事直接套到全部 AI PCB 标的上

### T8｜OCS 供给侧：Google 自研 Palomar 与外采的份额怎么变？MEMS 良率、代工产能和交期会不会卡住放量，谁有议价权？

- **关联关键词**：TPU●、光模块·
- **核心问题**：TPU 带动的 OCS 需求中，Google 自研体系（Palomar，据报由 Celestica 代工【L】）、Lumentum（MEMS）、Coherent（液晶）、H+S（压电）各拿多少？外采是为了补自研产能的缺口（周期性），还是 Google 转向商用产品（结构性）？供给瓶颈在 MEMS 晶圆和大阵列良率、准直器与光纤阵列，还是组装耦合？瓶颈环节有没有议价权？
- **为什么重要**
  - 这是 LITE 估值的核心分歧。Lumentum 称到 2027 年初，其 OCS 出货将超过最大客户（按公开信息应为 Google）的自研量，并自称实际上是唯一的商用 OCS 供应商【L，单一二手】。后一种说法与 Coherent 已向 7 家客户出货【M】、H+S 拿到超大规模客户订单【M】相冲突，需要先厘清“商用供应商”的口径。
  - 二手调研称 2026 年 Google 约 1.2 万台自研、约 3,000 台外采【L】；Cignal 称 Google 开始从自研转向采购商用产品【L，原文未重开】。
  - 供给侧信号：Lumentum 称爬坡受供应链限制【L】；Silex 称数据中心光开关需求强、正在扩产【M】；H+S 波兰新工厂目标产能提升 5 倍以上【M】；Coherent FQ4 FY26 称 OCS 收入环比增长【M】。如果 2027-2028 年多家同时扩产，而需求仍集中在 Google，瓶颈可能在两年内从“缺货”变成“过剩”。
- **研究子问题**
  1. 可证伪命题：Lumentum 称“2027 年初出货超过最大客户自研量”【L】。检验方法是用 T2 的端口模型估算 Google 的年端口需求，减去由 Lumentum 季度收入 ÷ $/port 推出的端口数，看剩下的自研量是否合理；同时看 FY27 Q2-Q3 的 OCS 收入是否继续高速增长。
  2. Google 自研产能上限：Celestica HPS 分部收入和 Google 相关表述，能否反映 Palomar 的产量？自研产能补上以后，外采比例会不会回落？
  3. MEMS 代工：Silex 季报中“数据中心光开关”的增速和扩产节奏【M】；为 Google 代工只是市场普遍看法。赛微北京的 MEMS-OCS 仍在试产【M】。
  4. MEMS 大阵列良率：Palomar 出于良率只使用部分微镜【M】；300×300 级阵列的良率曲线怎么走；国产“416 镜良率超 90%”的说法待验证【L】。
  5. 瓶颈在哪一环：MEMS、二维准直器与光纤阵列（腾景、炬光），还是自动耦合封装（罗博特科/ficonTEC 整线）？炬光称部分产能已被锁定【L】。
  6. 交期与议价：多年期协议的价格条款（“数十亿美元协议”为【L】）、交期长短，以及供应商毛利率能否守住。
  7. 新进入者：模块厂的 OCS 整机（光迅 320×320、旭创 TeraHop 300×300、新易盛 NX300，均为样机或展示【M】）；硅光路线 iPronics（B 轮 1.25 亿美元【M】）、nEye（C 轮 8,000 万美元【M】）何时量产。
- **跟踪指标与数据源**：Lumentum、Coherent 季报中的 OCS 收入、交期、产能和毛利率；Silex 季报；Celestica HPS 分部；H+S 半年报和年报；腾景、炬光、罗博特科的订单公告；Cignal 的供应商份额数据。
- **多空分歧**
  - 多方：Google 自研产能跟不上，外采比例结构性上升；瓶颈环节有定价权；TPU 外部化（T10）带来不经 Google 体系的采购。
  - 空方：外采只是补缺口，自研产能补上后就会回落；Lumentum、Coherent、H+S 和模块厂同时扩产，2027-2028 年价格承压（见 T9）；“唯一商用供应商”一说与多家同时出货的事实冲突。
- **相关标的**
  - 核心受益：Lumentum (LITE)、Coherent (COHR)、Huber+Suhner (HUBN.SW)
  - 验证中：Silex Microsystems、赛微电子 300456、Celestica (CLS)、腾景科技 688195、炬光科技 688167、罗博特科 300757、模块厂 OCS 整机（光迅科技、中际旭创、新易盛）
  - 概念：无

### T9｜2027-2030 年，MEMS、液晶、压电、硅光各会拿下哪些场景？$/port 的下降会不会侵蚀利润池？scale-across/DCI 和控制面标准化会怎样改变格局？

- **关联关键词**：光模块○、TPU○、存储·、CPO·
- **核心问题**：不同路线在端口规模、插损、切换时间、可靠性上各有取舍，决定哪家在哪个场景胜出：TPU ICI、DCN spine、园区 DCI/scale-across、GPU scale-up，以及更远期的资源池化。$/port 的下降速度能否被出货量的增长覆盖？价值最终留在整机，还是留在 MEMS、晶体等上游，或者留在控制面软件？
- **为什么重要**
  - 这一题决定 LITE、COHR、H+S 的利润，也决定 A 股器件厂的议价空间（T3），是买方最常问的问题。路线还决定上游谁受益：MEMS 代工（Silex），还是与 CPO 同源的硅光代工。
  - 价格：二手数据显示 128 口 MEMS OCS 从 5-6 万美元降到 3-4 万美元，折合约 390-470 美元/端口降到约 230-310 美元/端口【L】。H+S 因提前投入 OCS 产能，分部利润承压【M】。Coherent 以“非机械可靠性”为卖点，液晶寿命优于 MEMS 的说法只是分析机构观点【L】。
  - scale-across/DCI：Cignal 已把园区 DCI 列为 OCS 的应用方向【M】。Google 称借 Virgo 可以把超过 100 万颗 TPU 跨多个数据中心站点组成一个训练集群【H】，跨站点层用什么交换没有披露。这可能是 TPU ICI 之外的新场景。
  - 控制面：OCS 的价值离不开软件。Jupiter 靠 SDN 做流量与拓扑工程【H】，Ironwood 靠 OCS fabric manager 旁路故障 cube 并切片【H】。Google 称正推动 OCS 标准化【H】，OCP 已设 OCS 项目，其 GitHub 仓库含北向 connection-management 接口规范【M】。北向接口能否标准化，决定多供应商能否互换，也决定价格。
- **研究子问题**
  1. 插损（压电约 1dB，MEMS/液晶约 2-3dB，硅光约 6dB）、端口规模、切换时间（硅光微秒级、MEMS 毫秒级、机器人配线分钟级）【M】，分别卡住哪些场景？
  2. $/port 曲线：按 T2 统一的锚点，价格降幅和出货量增长在哪里交叉？Lumentum 的 OCS 毛利率能否守住“高于公司平均”？
  3. scale-across/DCI：Virgo 跨站点层用不用 OCS？液晶、压电或机器人配线是否更适合重构频率低的 DCI（假设，待验证）？微软的空芯光纤主要用于 DCI【M】，与 DCI OCS 是否争夺同一预算？
  4. 控制面与标准化：OCP 北向接口规范进展到哪一步，哪些厂商参与？外部部署的 TPU（T10）是否随 pod 一起交付控制面软件？标准化以后，整机的价格压力有多大？
  5. Coherent 出货 7 家客户，却没有单独披露收入，这个落差能否说明客户是否愿意为液晶的可靠性付溢价？
  6. 晶体与环形器的价值归属：液晶路线要用 YVO4 等双折射晶体做偏振分集，单机用量是多少？腾景自称是主要供应商【L】。环形器（法拉第旋光片、YVO4）放在模块内还是外置，新增价值归模块厂、无源器件厂还是整机厂？
  7. 国产厂商进入后，会不会引发价格战？
- **跟踪指标与数据源**：OFC 2027 产品参数；OCP OCS 白皮书和 GitHub 规范的提交记录；Cignal 报告中的 $/port 和路线份额；H+S 年报；iPronics、nEye 的量产公告；Google Cloud 技术博客。
- **多空分歧**
  - 多方：多条路线并存，ICI 之外还有 DCI/scale-across，扩大了 TAM；价格下降推动渗透；控制面软件的壁垒保护头部厂商。
  - 空方：价格降得比量涨得快；标准化后整机同质化；硅光一旦在插损和端口规模上突破，MEMS 产能面临被颠覆的风险。
- **相关标的**
  - 核心受益：Lumentum (LITE)、Coherent (COHR)、Huber+Suhner (HUBN.SW)
  - 验证中：Silex Microsystems、赛微电子 300456、腾景科技 688195、福晶科技 002222（与 Google 链的对应关系未核实）、iPronics 和 nEye（未上市）
  - 概念：无

### T10｜TPU 走出 Google 机房时，OCS 会随整 pod 一起交付吗？由谁供货、由谁运维？

- **关联关键词**：TPU●、MUSE·、光模块·
- **核心问题**
  - Anthropic 已知的部署方式有两种：约 40 万颗经博通以整机柜交付（SemiAnalysis 估算【L】）；拟从 Stream Data Centers 租赁最高 1GW 并自部署博通与 Google 设计的 TPU（初步谈判【M】）。Meta 在自有机房部署 TPU，目前只有 2025-11 的洽谈报道【L】。
  - 这些部署是否沿用“cube + OCS”架构？OCS 由 Google 体系供应，还是客户向 Lumentum、Coherent 采购？
  - Fluidstack 线索单独列出：Google 为 Fluidstack 与矿企（TeraWulf、Cipher Mining、Hut 8）的园区租约提供担保，据报用于托管 TPU 算力，客户与 Anthropic 相关【L，媒体报道，本轮未回源】。Anthropic 与 Fluidstack 在美国建设数据中心的 500 亿美元公告只写了“快速交付 GW 级电力”，没有披露芯片类型【H】，不能据此认定为 TPU 部署。
- **为什么重要**：Ironwood 每个机柜就是一个 64 芯片 cube，要组成 256 芯片以上的 pod，必须经过 OCS 或其他光互联（依据 Google 官方拓扑【H】）。如果外部部署带出商用 OCS 采购，“单一终端”的折价就能修复；如果外部客户只是经 Google Cloud 租用，OCS 仍计入 Google 的 capex。
- **研究子问题**
  1. 博通交付给 Anthropic 的 Ironwood 整机柜，是否包含 OCS 和 ICI 光模块？
  2. Anthropic 2027 年起的“数 GW”，按 3.5GW（博通披露，媒体转述【M】）还是 5GW（业绩会摘要【L】）计？两个口径冲突。8t 和 8i 各占多少？
  3. 外部部署的 OCS 由谁运维，控制面软件是否随 pod 交付（标准化问题见 T9）？
  4. Meta 通过 Google Cloud 租用 TPU 时，OCS 计入 Google 的 capex，不构成新增采购；自建机房才会形成新的采购主体。两者比例如何？
  5. Stream 的 1GW 租赁如果落地，部署的是整 pod 还是小切片？
  6. Fluidstack 矿企园区托管的芯片类型，能否从 TeraWulf、Cipher、Hut 8 的公告或 Google 担保文件中确认？
- **跟踪指标与数据源**：博通季度 AI 收入和 GW 口径；Alphabet 10-Q 中的 TPU 硬件销售；Lumentum、Coherent 新增客户数；OCP Global Summit；Anthropic、Meta 和 Stream 的公告。
- **多空分歧**
  - 多方：外部 TPU 沿用 OCS 架构，并直接采购商用 OCS。
  - 空方：外部部署以小切片加以太网为主，或 OCS 由 Google 封闭供应；Meta 转向 MTIA（与博通的协议为 1GW 起【M】）；Stream 租赁停留在谈判阶段。
- **相关标的**
  - 核心受益：Alphabet (GOOGL)、Broadcom (AVGO)
  - 验证中：Lumentum (LITE)、Coherent (COHR)、Celestica (CLS)
  - 概念：Meta（MUSE）作为 OCS 需求方

### T11｜美中双向管制下，OCS 物料中的中国环节有多大风险敞口？FCC 只是其中一项

- **关联关键词**：光模块○、FCC·、TPU·
- **核心问题**：Google（TPU 链）、Lumentum、Coherent 的 OCS 物料中，中国无源件（二维准直器、双折射晶体、微透镜阵列等）占多少，没有公开数据。已知的中国环节有腾景（二维准直器订单，客户未披露）、炬光（微透镜阵列量产）、福晶（晶体，与 Google 链的对应关系未核实）。在多条管制线并存的情况下，这些环节会不会被迫转产，转产要多久？
  - FCC 组件级 Covered List 新规：2026-07-22 表决，2026-09-11 刊登联邦公报，据律所解读 2026-10-13 生效（生效日未能复核）。它针对 Covered List 实体生产的“含逻辑的硬件组件”；中国光模块厂不在名单上，纯无源光学件不在范围内【M，据律所解读和 SCMP】。
  - 光模块准入线（与 OCS 间接相关，因为 OCS 链路要配 OCS 兼容模块）：路透社 2026-08-04 和 Tom's Hardware 2026-08-11 报道，美方起草禁止中国产新型号光收发器进口【M】，中际旭创回应称 FCC 尚未出台文件；2026-09-25 四名参议员提出法案，禁止联邦敏感系统使用中际旭创、新易盛的光模块【M】。
  - BIS 关联方规则的暂停期约到 2026-11-09【L】；中方镓锗锑对美禁令的暂停期约到 2026-11-27【L】；铟的许可管制仍然有效【L】，影响的是 InP 激光器和光模块，不是 OCS 的无源件。
  - 关税：美国最高法院 2026-02-20 裁定 IEEPA 不授权加征关税，其后 122 条款临时关税约在 2026 年 7 月到期【L】，截至 9 月底光器件的实际税率需要按 301、232 条款重新确认。
- **为什么重要**：OCS 的主力供应商是美系（Lumentum、Coherent），在管制中相对受益；但如果它们的物料高度依赖中国无源件，转产的成本和交期会反过来影响供给（连到 T8）。报道称中国约占全球光模块市场 56%【M】，光模块准入的条款细节决定中资龙头的折价。
- **研究子问题**
  1. OCS 物料中国件占比：从 Lumentum、Coherent 10-K 的供应商风险披露，腾景、炬光、福晶的客户与海外收入，以及海关 HS 9001、9013 对美国、泰国、马来西亚的出口数据反推。
  2. FCC 2026-09-11 规则原文中“逻辑组件”的清单是什么？OCS 整机里的 MEMS 驱动 ASIC 和控制板会不会被覆盖？生效日和过渡期如何？
  3. 光收发器进口禁令草案有没有进入 NPRM？“新型号”如何定义？泰国、马来西亚产能是否被纳入？对 OCS 兼容模块的供应有什么影响？
  4. 参议院法案在委员会的进度，会不会被并入 NDAA？
  5. 11 月两个到期窗口（BIS 约 11-09，中方约 11-27）之后是续期还是升级？
  6. 腾景、炬光、福晶、中际旭创的东南亚产能占比和转产节奏。
- **跟踪指标与数据源**：FCC ECFS 和联邦公报；BIS 实体清单；USTR 的 301 条款；商务部、海关总署出口管制公告；中国海关光学部件和光模块出口（分目的地）；Lumentum、Coherent、Fabrinet 10-K 风险因素；A 股公司海外产能公告。
- **多空分歧**
  - 多方（中资）：FCC 新规不涉及无源光学件和光模块；精密无源光学的成本、良率和产能短期难以替代；海外产能可以缓冲。
  - 空方：规则沿“整机、模组、芯片、部件”一路扩张，叠加“外国对手控制”审查、立法和 11 月到期窗口，风险事件密集；海外 OCS 链加速去中国化，订单转到东南亚。
- **相关标的**
  - 相对受益：OCS 侧 Lumentum (LITE)、Coherent (COHR)；光模块准入侧另有 AAOI、Fabrinet (FN)
  - 验证中（风险方）：腾景科技 688195、炬光科技 688167、福晶科技 002222、中际旭创 300308、新易盛 300502
  - 概念：无。电池、宁德时代与 FCC 或 OCS 都无关，已从本题剔除。

---

## 第三梯队：弱关联或证伪型题目

### T12｜Agent 推理（MUSE、WORKBUDDY）能否一环一环传导到国内外 CSP 的 capex、光互联，最后到 OCS？

- **关联关键词**：存储○、国内CSP○、MUSE·、光模块·、WORKBUDDY·
- **核心问题**：Muse 于 2026-09-08 发布【M】。摩根大通在 2026-09-10 上调 Meta 评级，依据之一是 Muse 上线第二天在美区 App Store 最高升到第 3 位【M】；另有单一来源称 Muse “登顶”、两周约 280 万下载（Sensor Tower）【L，未核实】。腾讯港股在 2026-09-22 涨 5%，被归因于 C 端 Agent 生态重估【M】。这些能否转化为 capex 和网络订单？
- **为什么弱**
  - 没有证据显示 Muse 使用 TPU（Meta 自有算力以 GPU 和自研 MTIA 为主）；Meta 也没有任何部署 OCS 的公开证据。
  - Meta 2026 年 Q2 自由现金流只有 7.84 亿美元【M】，capex 斜率受约束。
  - 腾讯 2025 年 capex 逐季下降，被归因于芯片供给【L】。WorkBuddy 只有访问量一类的数据：据单一二手来源，2026-06 PC 端月访问量约 2,097 万次，居国内 AI 办公 Agent 首位【L】；花旗认为它降低了 AI 使用门槛【L】。这些都不是 token 量或算力采购数据。
  - 节点本地的 KV cache 分层（Google GKE 方案）主要利好 DRAM/SSD，对 OCS 基本没有拉动【H】。
  - 反方向的事实：Google 专为推理和 Agent 设计的 TPU 8i 在 pod 内用 OCS【H】，推理并非不需要 OCS。但这是 Google 的架构选择，不能外推到 Meta 或腾讯。
- **什么证据会让关联变强**：Meta 采购含 OCS 的 TPU 整系统，或在 OCP 公开 OCS 部署；推理 pod（如 8i Boardfly）成为主流部署形态；国内 CSP 在推理集群招标中出现 OCS 标包。
- **研究子问题**
  1. Muse 的真实 DAU 和付费转化：用 Sensor Tower、Similarweb 数据核对“不足百万 DAU”这一标题【L】和摩根大通的口径。
  2. Meta 2027 年算力翻倍计划【M】中，GPU、MTIA、TPU 各占多少？
  3. 跟踪 vLLM、LMCache、NVIDIA Dynamo 的默认部署形态，以及 Google 推理产品文档中的 KV 分层方式，判断 KV 流量是留在节点内还是跨节点。
  4. 腾讯、阿里 2026 年 capex 指引。
- **跟踪指标与数据源**：Meta Q3 财报（2026-10 下旬）；腾讯、阿里季报；国家数据局 token 数据。
- **多空分歧**：多方认为 Agent 让 token 非线性增长，光模块和存储先受益，OCS 远期跟进；空方认为这只是情绪联动，与 OCS 之间没有可测量的传导。
- **相关标的**
  - 核心受益：无
  - 验证中：Meta (META)、腾讯控股 0700.HK（作为需求侧变量）
  - 概念：以“Muse 概念”交易 OCS 标的

### T13｜保偏光纤和 TEC 的需求，是 CPO 外置光源驱动的，还是 OCS 驱动的？

- **关联关键词**：光模块○、CPO○、TEC·、保偏光纤·
- **核心问题**：OIF 的 ELSFP 规范按保偏规格定义输出（定义了偏振消光比 PER）【M】，所以 CPO 与保偏光纤之间的技术因果成立。但 MEMS OCS 用标准单模光纤，液晶 OCS 在内部用晶体做偏振分集，两者都不需要保偏光纤。TEC 方面，CWDM 本来就是为非制冷激光器设计的，“OCS→WDM→TEC”不能当作强逻辑。CPO 与 OCS 是先后还是替代，放在 T6 讨论。
- **为什么弱**：长盈通两次风险提示称，保偏相关收入占比不足 1%，未用于 CPO【M，经 36氪、财联社快讯转引】；长飞所说“1-2 年需求增长 10-20 倍”出自利益相关方【M】；2026 年英伟达 CPO 交换机出货约 1-1.5 万台（二手转述 SemiAnalysis【L】）。
- **什么证据会让关联变强**：OCS 与 CPO 的组合在 scale-up 中量产（见 T6），并因 OCS 插损迫使外置光源提高功率；拆机资料证明 Google OCS 定制模块使用制冷激光器。
- **研究子问题**：(1) 单台 102.4T CPO 交换机需要多少个 ELSFP、多少米保偏光纤；(2) 保偏 FAU 的对轴良率；(3) 按方案拆分 TEC 渗透率（EML 对比硅光+CW）；(4) 富信科技通信 TEC 收入。
- **跟踪指标与数据源**：长盈通、长飞的定期报告和风险提示公告；NVIDIA 和 Broadcom 的 CPO 出货；富信科技季报。
- **多空分歧**：多方认为 CPO 在 2027 年放量会带来量价齐升；空方认为用量绝对值小，片上集成激光会绕开保偏链路。
- **相关标的**
  - 核心受益：无
  - 验证中：长飞光纤 601869、富信科技 688662（CPO 主线）
  - 概念：长盈通 688143，以及“OCS 带动保偏光纤”的相关标的

### T14｜电力上线节奏能否作为 OCS 拉货的时间指标？SOFC、储能和宁德时代只能作电价锚与节奏变量

- **关联关键词**：TPU○、MLCC·、光模块·、SOFC·、电池·、宁德时代·
- **核心问题**：美国并网排队约 5 年【L】。SOFC、燃机、储能这类表后电源决定园区的上电时点，也就决定 TPU 容量何时转化为 OCS 和光模块拉货。这是时间上的传导，不是需求量的传导，而且“电力 → TPU → OCS”这座桥目前只是推断：Anthropic 选择 Fluidstack 的理由是它能“快速交付 GW 级电力”【H】，但公告没有披露芯片类型【H】；Anthropic 新增的下一代 TPU 容量从 2027 年起上线【H】，这与 Fluidstack 站点是两件事。
- **为什么弱**
  - OCS 自身只占 TPU v4 系统功耗不到 5%（博客）或不到 3%（论文摘要）；Google 所说约 40% 的节能是 DCN 整体架构的效果。“OCS 省电”对 SOFC 订单没有可感知的影响。
  - SOFC 的大单（AEP 最高 1GW、Oracle、Brookfield 最多 50 亿美元【均为 L，本轮未回源】）决定表后电源每瓦的边际成本，但不构成 OCS 需求。
  - OCS 不产生也不消除功率瞬变，对 BBU 和储能配置没有一阶影响。GB300 的功率平滑可能主要靠电源架内的电容，而不是锂电池【L，未核实】。美国 AIDC 储能受 FEOC 和 301 关税约束【L】，宁德时代难以直接受益。
  - 三环集团同时生产 SOFC 隔膜片、MLCC 和光纤陶瓷插芯，只是一家公司的共同暴露；它为 Bloom 供货未经公司确认【L】。
- **什么证据会让关联变强**：Google 或 Anthropic 披露的具体 TPU 园区依赖表后电源，且园区上电时点能与 OCS 供应商的出货节奏对上。
- **研究子问题**（不做统计回归：OCS 只有约 4 个季度的收入历史）
  1. 逐个跟踪 Google、Anthropic、Meta 披露的具体园区上电时点，对照 Lumentum 存货和合同负债的变化。
  2. 哪些园区依赖桥接电源？Bloom 季度出货的 MW 能否和这些园区对上？
  3. SB6、PJM 大负荷规则下，配储或柔性负荷能把并网时间提前多少？
  4. 光器件厂商有没有出现客户推迟收货、存货天数上升的信号？
  5. 宁德时代面向 AIDC 的订单能否验证？三环 SOFC 收入占比是多少？
- **跟踪指标与数据源**：超大规模厂商的 MW/GW 指引；Bloom 10-Q；PJM 容量价（2026/27 年度出清价 329.17 美元/MW-日【L】）；Lumentum、中际旭创的存货和合同负债；宁德时代储能出货。
- **多空分歧**
  - 多方：2028 年前电力是硬约束，表后电源加速上电，TPU 容量集中上线，拉货超预期。
  - 空方：电力不是瓶颈时，这个指标就失效；变压器、燃机交付期拖慢上线，订单后移；SOFC、电池本身与 OCS 无关。
- **相关标的**
  - 核心受益：无（本题只提供指标）
  - 验证中：Bloom Energy（仅作电价锚和节奏指标）、Lumentum (LITE)、中际旭创 300308
  - 概念：宁德时代 300750、三环集团 300408、Bloom (BE)（放在 OCS 语境下）

### T15｜OCS 整机的电子 BOM（PCB、MLCC、RCC）和石墨烯，有没有可计量的 OCS 收入？

- **关联关键词**：PCB·、MLCC·、RCC·、CCL·、石墨烯·
- **核心问题**
  - OCS 整机的价值主要在 MEMS、光学件和光纤阵列。国内卖方拆解称，MEMS 阵列约占 BOM 的 35-50%，无源器件约 25%【L】，电子部件占比很低。
  - RCC 在 AI 板上的批量应用，没有找到一手证据。本清单只在这一题做 RCC 证伪。
  - 石墨烯在 2026 年的热度来自射频晶体管科研（中科院金属所，2026-06-06【M】）、德尔未来的题材和国际标准（2026-09-17【M】），与 OCS 的各技术路线都无关。德尔未来的石墨烯收入占营收仅 0.05%，没有在手订单【M，公司半年报口径，经财联社快讯存档转引】。
- **为什么弱**：没有已知的传导链。即使 OCS 的 TAM 达到 80 亿美元，拉动的 PCB/MLCC 规模也很有限。
- **什么证据会让关联变强**：OCS 拆机报告显示高压驱动 ASIC、MLCC、高可靠 PCB 形成独立料号，并有明确供应商；出现石墨烯光子器件进入 OCS 或 CPO 的量产公告。
- **研究子问题**
  1. 交易所问询函或互动易里，自称“OCS 配套”的 PCB/MLCC 公司有没有收入披露？
  2. 从 Apollo 论文和 OCP OCS 白皮书查 MEMS 静电驱动电压的量级，判断是否会形成高压 MLCC、高可靠 PCB 的独立料号。
  3. RCC 证伪：有没有 AI 板批量使用的一手证据（郭明錤 2024 年关于苹果 iPhone 采用 RCC 的说法未复核【L】）？如果没有，应从 AI PCB 主题中剔除。
  4. A 股异动公告和问询函回复中披露的石墨烯、RCC 真实收入。
- **跟踪指标与数据源**：交易所问询函回复和互动易；A 股异动公告；OFC、ECOC 上的石墨烯光子进展。
- **多空分歧**：多方认为高压、高可靠料号可以形成利基市场；空方认为这纯粹是题材，结论倾向证伪。
- **相关标的**
  - 核心受益：无
  - 概念：德尔未来 002631；自称“OCS 配套 PCB/MLCC”但没有收入证据的公司；以 RCC 名义挂靠 OCS 的标的

---

## 跨题目的核心分歧

1. **OCS 对光模块是替代还是放大（T1、T5、T6）**：DCN 层是替代，ICI 层是增量，Virgo scale-out 层与 OCS 无关。净效应取决于网络层结构，以及每条链路是 800G 还是 1.6T。TrendForce 隐含的每芯片约 1.5 只与拓扑推算不一致，需要先拆口径。国内“以光补存”的路线（CM384）是光模块密集、但不用 OCS 的反例。
2. **Google 专属，还是行业标准（T2、T6、T8、T9、T10）**：支持“行业标准”的证据有 OCP OCS 项目和北向接口规范、Coherent 出货 7 家客户、Lumentum 有 3 家客户、H+S 的超大规模订单、TPU 外部化。反向证据是这些客户可能指向同一个终端；Meta、微软仍停留在评估阶段【L】；英伟达没有官方表态。Cignal 80 亿美元中 GPU 那部分，是整个行业最大的可证伪变量。
3. **OCS 对交换机和 PCB/CCL：削量还是升规（T1、T7）**：Google 的替代是存量。Ironwood 超节点之间走 Jupiter DCN，这一层本身有 OCS；TPU 8t 的 Virgo 公开描述是电交换、未提 OCS，只是弱反证，“没提”不等于“没用”。现有证据不足以判断 OCS 会不会进一步削减 AI 交换机 PCB。只有非 Google 客户在 AI 集群 spine 层采用 OCS，或光进入柜内，才会形成实质削量。
4. **国产链：出口受益还是出口风险（T3、T5、T11）**：精密无源光学是中国的强项，但 FCC、立法、BIS 和关键矿产反制在 2026-10 到 11 月密集生效或到期；OCS 的价值又大量被 Google 自研和 Lumentum、Coherent 锁定。
5. **TPU 与 OCS 出货的上限由谁决定（T2、T4、T8、T14）**：需求（Anthropic 的 GW 级协议）、HBM/CoWoS 分配、OCS 自身的供给（MEMS 良率与产能）、电力上线。四者决定 OCS 收入能否按“TPU 出货 × 端口数”线性外推。

## 研究优先级建议（只有两周时）

这里按估值重要性和时间窗口排序，不按关键词关联度排序，所以和上面的梯队顺序不同。

1. **T2 需求弹性模型加 T8 供给侧**：这是所有 OCS 估值的底座。Lumentum 和 Coherent 的 FY27 Q1 财报约在 2026-11 上旬发布，两周正好用来准备。先搭好“TPU 出货 × 每芯片端口 × 附着率 × $/port”的端口模型，按 T2 列出的检验标准备好预期；同时把 Lumentum“唯一商用供应商”“超过客户自研量”的说法与 Coherent、H+S 的出货事实对齐。核心未知数是 TPU 8t 是否用 OCS，第一步先查已经开过的 Hot Chips 2026、ISCA 2026 有没有披露。
2. **T3 中国链真伪鉴别，顺带做 T5 的一步证伪**：对 A 股投资者最直接，工作量可控，主要是逐家读公告、问询回复和互动易。同时核实工信部 2026-04-02 文件的文号和原文。按目前措辞，初步判断偏运营商 OXC，这是证伪 2026-04 行情成本最低的一步。
3. **T1 光模块净效应**：影响市值最大的板块，并且可以复用 T2 的拓扑模型，重点是拆解 TrendForce 的口径。若时间有余，把 T11 作为事件跟踪加进来：FCC 新规据报 2026-10-13 生效（未能复核），BIS 暂停期约在 11-09 到期。

**一个月内（至 2026-10-30）的外部节点**
- 美光 FQ4'26（2026-09-30 盘后，影响 T4）
- FCC 组件级新规据报 2026-10-13 生效（未能复核，影响 T11）
- OCP Global Summit（通常在 10 月中旬，2026 年具体日期未核实，影响 T9、T10）
- Meta、Alphabet Q3 财报（10 月下旬，具体日期以公司公告为准，影响 T2、T4、T12）

**11 月的节点**
- Lumentum、Coherent FY27 Q1 财报（约 11 月上旬，影响 T2、T8）
- BIS 关联方规则暂停期约 11-09 到期；中方镓锗锑对美禁令暂停期约 11-27 到期（均为【L】，影响 T11）
- 阿里、腾讯、百度季报（影响 T5、T12）

**已发生、待查有无披露**：ISCA 2026（6 月）、Hot Chips 2026（8 月下旬）、SIGCOMM 2026（8 月）上有没有 TPU 8 拓扑或 OCS 的披露，本轮未能核实。

**后续技术节点**：OFC 2027 和 GTC 2027（约 2027-03）、Hot Chips 2027、Google Cloud 技术博客。

---

## 附录：关键事实与来源

置信度：【H】一手原文核实；【M】公告、纪要或两个以上独立二手来源，本轮未重开原文；【L】单一二手来源、摘要级信息、传闻或口径冲突。每条链接都标明是本轮实际读到的页面，还是原站未打开、经存档或二手汇总转读。

**Google 与 Anthropic（一手，本轮打开原文）**
- 【H】2022-08-23：Jupiter 引入 OCS 取消 spine，改为直连拓扑；Apollo OCS 构成 Google 绝大多数数据中心网络的基础；与最佳替代方案相比功耗低 40%、成本低 30%、停机少 50 倍（整体架构收益）。[Google Cloud 博客](https://cloud.google.com/blog/topics/systems/the-evolution-of-googles-jupiter-data-center-network)
- 【H】2024-10-30：OCS 于 2013 年首次投产。[Google Cloud 博客](https://cloud.google.com/blog/products/networking/speed-scale-reliability-25-years-of-data-center-networking)
- 【H】2023-04-05：TPU v4 的 OCS 及光器件占系统成本不到 5%、功耗不到 5%。[Google Cloud 博客](https://cloud.google.com/blog/topics/systems/tpu-v4-enables-performance-energy-and-co2e-efficiency-gains)
- 【M】2023-04：TPU v4 论文摘要称功耗不到 3%，并用 48 台 OCS 互联（arXiv 本轮被拦截，未重开）。[arXiv 2304.01433](https://arxiv.org/abs/2304.01433)
- 【H】2025-11-06：Ironwood 由 144 个 64 芯片 cube 经 OCS 组成 9,216 芯片 superpod，OCS 负责旁路故障 cube；多个 superpod 经“standard DCN”互联。[Inside Ironwood](https://cloud.google.com/blog/products/compute/inside-the-ironwood-tpu-codesigned-ai-stack)
- 【H】2026-04-22：TPU 8i 的 36 个 Boardfly 组经 OCS 互联（最多 1,152 颗芯片）；TPU 8t 为 9,600 芯片 3D torus，文中未提 OCS；TPUDirect RDMA/Storage 属于 8t。[TPU 8t/8i deep dive](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)
- 【H】2026-04-22：Virgo 单一 fabric 可连 13.4 万颗 TPU 8t，为高 radix 两层电交换，文中未提 OCS。[Introducing Virgo](https://cloud.google.com/blog/products/networking/introducing-virgo-megascale-data-center-fabric)
- 【H】2026-04-22：Google 称借 Virgo 和 TPU 8t，可“connect more than one million TPUs across multiple data center sites into a training cluster”；文中未提 OCS。[AI infrastructure at Next '26](https://cloud.google.com/blog/products/compute/ai-infrastructure-at-next26)
- 【H】2025-10-14：Google 称“a new effort is underway to standardize Optical Circuit Switching (OCS)”，并链接到 OCP 的 OCS 项目。[Google Cloud 博客](https://cloud.google.com/blog/topics/systems/agile-data-centers-and-systems-to-enable-ai-innovations)
- 【H】2025-10-23：Anthropic 计划使用最多 100 万颗 TPU，2026 年上线远超 1GW。[Anthropic](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services)
- 【H】2026-04-06：Anthropic 获得数 GW 下一代 TPU 容量，2027 年起上线。[Anthropic](https://www.anthropic.com/news/google-broadcom-partnership-compute)
- 【H】2025-11-12：Anthropic 与 Fluidstack 在美国投资 500 亿美元建设数据中心，理由是“rapid delivery of gigawatts of power”；公告未披露芯片类型。[Anthropic](https://www.anthropic.com/news/anthropic-invests-50-billion-in-american-ai-infrastructure)

**市场与商用供应商**
- 【M】2025-12：Cignal 预测 2029 年外部 OCS 市场至少 25 亿美元（原站被拦截，未打开）。[Cignal AI](https://cignal.ai/2025/12/optical-circuit-switching-market-to-exceed-2-5b-in-2029/)
- 【M】2026-02-02：Cignal 因 TPU 部署加速上调预测，并称 2029 年前 GPU scale-up 采用有限（原站未打开）。[Cignal AI](https://cignal.ai/2026/02/googles-ai-buildout-drives-higher-optical-circuit-switching-forecast/)
- 【M】2026-07：Cignal 预测 2030 年超过 80 亿美元；“英伟达 NVL576 引入 OCS、2028 年放量”是 Cignal 的说法，未获英伟达确认（【L】）（原站未打开）。[Cignal AI](https://cignal.ai/2026/07/ocs-market-to-top-8-billion-by-2030/)
- 【M】业绩发布 2026-08-11，10-K 提交 2026-08-17：Lumentum FY26 OCS 收入超过 9,000 万美元，指引 FY27 Q1 为首个单季超 1 亿美元的季度（以下两个页面本轮均未打开，经二手汇总核对）。[SEC 10-K](https://www.sec.gov/Archives/edgar/data/0001633978/000162828026057358/lite-20260627.htm)；[Q4 电话会纪要（页面 2026-08-18 发布，对应 08-11 电话会）](https://www.fool.com/earnings/call-transcripts/2026/08/18/lumentum-lite-q4-2026-earnings-call-transcript/)
- 【M】2026-02-03：Lumentum FQ2 FY26 电话会，OCS 在手订单约 4 亿美元，来自 3 家客户。纪要全文经 GitHub 存档读取；MarketBeat 对 2026-05-05 Q3 电话会的摘要称在手订单超过 4 亿美元，口径一致；待对照 IR 原稿。[GitHub 存档纪要](https://github.com/Ngafney/garda-spring26/blob/main/amir/transcripts/lumentum/2026/Q2/LITE_2026-02-03_Q2.txt)；[MarketBeat 摘要（2026-05-05，原站未打开）](https://www.marketbeat.com/instant-alerts/lumentum-q3-earnings-call-highlights-2026-05-05/)
- 【M】2026-08：Lumentum CY26 下半年 OCS 出货约 4 亿美元的目标；CEO 称 2027 年初成为 OCS 第一大供应商。来源为电话会纪要转述和 GitHub 二手汇总（fbmonteiro07/wiki-empresas 的 OCS-CPO 仪表板，具体文件路径未记录），原站未打开。[Q4 电话会纪要](https://www.fool.com/earnings/call-transcripts/2026/08/18/lumentum-lite-q4-2026-earnings-call-transcript/)
- 【L】2026-08 下旬至 09 月（会议日期口径不一）：Lumentum 在德银科技会议上称 OCS 出货环比翻倍、TAM 高于约 80 亿美元。摘要级，原站未打开。[Investing.com 纪要摘要](https://www.investing.com/news/transcripts/lumentum-at-deutsche-bank-2026-technology-conference-optics-gains-pace-93CH-4880293)
- 【L】2026-08：Lumentum 称 2027 年初出货将超过最大客户的自研量，并自称实际上是唯一的商用 OCS 供应商。单一二手来源：GitHub 仓库 jameswong2011/InvestmentVault 中的 FQ4 2026 业绩分析笔记。[GitHub 仓库](https://github.com/jameswong2011/InvestmentVault)
- 【L】“2027 年 OCS 收入超过 10 亿美元”：卖方和社区说法，也有转述称来自 CFO，口径冲突，不能当作公司指引。[Q3 电话会纪要](https://www.fool.com/earnings/call-transcripts/2026/05/06/lumentum-lite-q3-2026-earnings-transcript/)
- 【M】2025-11-06 与 2026-02-04：Coherent 液晶 OCS 已向 7 家客户出货，接洽超过 10 家。纪要全文经 GitHub 存档读取。[FQ1 纪要存档](https://github.com/Ngafney/garda-spring26/blob/main/amir/transcripts/coherent/2026/Q1/COHR_2025-11-06_Q1.txt)；[FQ2 纪要存档](https://github.com/Ngafney/garda-spring26/blob/main/amir/transcripts/coherent/2026/Q2/COHR_2026-02-04_Q2.txt)
- 【M】2026-05：Coherent 把 OCS 可寻址市场上调至 40 亿美元以上（原站未打开）。[Futurum](https://futurumgroup.com/insights/coherent-q3-fy-2026-ai-data-center-demand-accelerates-optical-growth/)
- 【M】2025 年至 2026-08：H+S 获一家全球超大规模客户的 Polatis 大订单，波兰新工厂目标产能提升 5 倍以上（原站未打开）。[H+S 订单公告](https://www.hubersuhner.com/en/newsroom/company-news/news-ad-hoc-news/hubersuhner-receives-major-orders-for-polatis-optical-circuit-switches)；[H+S 新工厂公告](https://www.hubersuhner.com/en/newsroom/company-news/news-ad-hoc-news/new-optical-circuit-switch-production-site)
- 【M】2026-05-07 / 2026-07-17：Silex 在斯德哥尔摩上市；二季度称数据中心光开关需求强、正在扩产（原站未打开）。[Silex 二季报](https://mfn.se/a/silex-microsystems/silex-microsystems-interim-report-for-the-second-quarter-2026-strong-growth-and-profitability)
- 【M】2026-03：英伟达分别投资 Lumentum、Coherent 各约 20 亿美元，协议未明确包含 OCS（原站未打开）。[NVIDIA](https://nvidianews.nvidia.com/news/nvidia-announces-strategic-partnership-with-lumentum-to-develop-state-of-the-art-optics-technology)
- 【M】2026-09-02：iPronics 完成 1.25 亿美元 B 轮，据报英伟达参投（原站未打开）。[The Register](https://www.theregister.com/networks/2026/09/02/nvidia-joins-investment-into-ipronics-to-build-out-optical-circuit-switching-ocs-tech/5293764)
- 【M】2026-04：nEye 完成 8,000 万美元 C 轮（原站未打开）。[BusinessWire](https://www.businesswire.com/news/home/20260414407496/en/nEye.ai-Secures-$80-Million-Series-C-to-Scale-Optical-Circuit-Switching-for-AI-Infrastructure)
- 【M】2026-04：OCP 发布 OCS 白皮书（原站未打开）；OCP 的 OCS GitHub 仓库含北向 connection-management 接口规范（仓库页面）。[OCP 白皮书](https://www.opencompute.org/documents/ocp-ocs-white-paper-april-2026-final-pdf)；[OCP GitHub 仓库](https://github.com/opencomputeproject/ocp-net-optical-circuit-switching)
- 【M】2026-07-06：据报 Kyber 因 PCB 中板问题推迟到 2028 年，英伟达称路线图不变（原站未打开）。[CNBC](https://www.cnbc.com/2026/07/06/nvidia-kyber-rack-system-delays-manufacturing-taiwan-rubin-chips-.html)
- 【M】2026-09-24 至 26：Anthropic 初步谈判从 Stream Data Centers 租赁最高 1GW，并自部署博通与 Google 设计的 TPU。[GitHub 快讯存档](https://github.com/qjlxg/wei/issues/2968)
- 【L】2025 年：Google 为 Fluidstack 与矿企的园区租约提供担保，据报用于托管 TPU，客户与 Anthropic 相关（原站未打开）。[Forbes Colombia](https://forbes.co/2026/09/03/negocios/fluidstack-startup-ia-google-nvidia-18000-millones/)
- 【L】价格：128 口 MEMS OCS 从 5-6 万美元降到 3-4 万美元（原站未打开）。[Substack](https://semifundamental.substack.com/p/optical-circuit-switches-ocs-fundamentals)

**中国产业链与政策**
- 【M】2026-04-03：德科立公告称硅基 OCS 未计入 2-3 年营收规划，没有海外批量订单（原站未打开，经二手核对）。[同花顺](https://stock.10jqka.com.cn/20260404/c675770951.shtml)
- 【M】2026-01-22：腾景科技获 1,280 万美元二维准直器订单，OCS 相关订单累计约 1.76 亿元（原站未打开）。[上海证券报](https://paper.cnstock.com/html/2026-01/22/content_2172807.htm)
- 【M】2026-01：罗博特科/ficonTEC 两条 OCS 封装整线订单，合计约 1,716 万欧元（原站未打开）。[每日经济新闻](https://www.nbd.com.cn/articles/2026-01-29/4239848.html)
- 【M】2026-08-14：炬光科技 OCS 用微透镜阵列已在主要客户处量产（原站未打开）。[同花顺](https://stock.10jqka.com.cn/20260814/c678964129.shtml)
- 【M】2026-01-27：赛微电子持有 Silex 约 45.24%（IPO 前比例），北京 MEMS-OCS 尚未量产（原站未打开）。[同花顺](https://news.10jqka.com.cn/20260127/c674347390.shtml)
- 【M】2026-04-02：工信部办公厅文件提出“推动全光交换等技术应用部署，降低算力应用终端到服务器的网络时延”（普惠算力场景）；文号和全文未核实（原站未打开）。[21 世纪经济报道](https://www.21jingji.com/article/20260404/herald/3492d988269f60c2d5aa468fdcc0cd6a.html)
- 【M】2026-06-10：《“人工智能+信息通信”创新发展实施意见》（工信部通信〔2026〕121号）提出全光交换器件“研发验证”。财联社摘录，经存档转读，原站未直接打开。[财联社](https://www.cls.cn/detail/2395873)
- 【M】2026-07-23：阿里云、中国移动研究院在论坛上介绍 OCS 演进，未见公开集采（原站未打开）。[C114](https://m.c114.com.cn/w5472-1314558.html)
- 【M】2026-06-03 / 06-29：长盈通风险提示称保偏光纤相关收入占比不足 1%，未用于 CPO。36氪和财联社快讯，经存档转读。[36氪](https://www.36kr.com/newsflashes/3874132470600706)
- 【M】2025-04-16：CloudMatrix 384 使用 6,912 个 400G LPO 光模块（电交换方案，不是 OCS）。经原文剪藏读取。[SemiAnalysis](https://semianalysis.com/2025/04/16/huawei-ai-cloudmatrix-384-chinas-answer-to-nvidia-gb200-nvl72/)

**FCC 与管制**
- 【M】2026-07-22 表决、2026-09-11 刊登：FCC 组件级 Covered List 新规，中国光模块厂商不在名单上；据律所解读 2026-10-13 生效，生效日未能复核（原站均未打开）。[Cooley](https://www.cooley.com/news/insight/2026/2026-07-29-fcc-expands-restrictions-on-covered-list-equipment-and-supply-chains)；[SCMP](https://www.scmp.com/tech/big-tech/article/3367219/chinese-optical-transceiver-makers-dodge-us-ban-now-fcc-updates-rules)
- 【M】2026-08-04/11：美方起草禁止中国产新型号光收发器进口（原站未打开）。[Reuters](https://www.reuters.com/world/trump-administration-drafting-ban-chinese-data-center-devices-sources-say-2026-08-04)；[Tom's Hardware](https://www.tomshardware.com/tech-industry/fcc-proposes-import-ban-on-chinese-optical-transceivers-blockade-targets-key-ai-interconnects-as-china-holds-56-percent-global-market-share)
- 【M】2026-09-25：参议员提出法案，禁止联邦敏感系统使用中际旭创、新易盛产品（原站未打开）。[Reuters](https://www.reuters.com/legal/litigation/us-lawmakers-aim-keep-chinas-datacenter-tech-out-sensitive-government-systems-2026-09-25/)
- 【L】BIS 关联方规则 2025-11-10 起暂停一年（约至 2026-11-09）；中方镓锗锑对美禁令暂停至约 2026-11-27；铟许可管制未暂停；美国最高法院 2026-02-20 裁定 IEEPA 不授权加征关税。以上本轮均未回源（bis.gov、mofcom.gov.cn、supremecourt.gov 被拦截）。

**存储与 capex**
- 【L】2026：TrendForce DRAM 合约价环比，1Q26 约 +93~98%，2Q26 +58~63%，3Q26 预测 +13~18%。经单一二手数据集转引，待对照原稿。[GitHub 数据集](https://github.com/yhwang55/memory-pricing-simulator)
- 【L】2026-04-29：微软称约 250 亿美元 capex 增量来自组件和内存涨价。单一二手转述，待对照纪要。[GitHub 存档](https://github.com/prajwalgajakesari/the-vault-ai/blob/main/editions/2026/04/29/stories/01-microsoft-q3-2026-earnings-ai-surge.md)
- 【M】2026-07-30 前后：亚马逊把 2026 年 capex 上调至约 2,200 亿美元；管理层把部分原因归于内存成本（【L】）。[GitHub 存档](https://github.com/prajwalgajakesari/the-vault-ai/blob/main/editions/2026/08/03/stories/01-amazon-aws-q2-2026-earnings.html)
- 【M】2026-07-22：Alphabet 2026 年 capex 指引上调至 1,950-2,050 亿美元（原站未打开，经二手汇编核对）。[CNBC](https://www.cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html)
- 【M】2026-06-24：美光 FQ3'26 营收 414.56 亿美元，FQ4 指引 500 亿美元。经二手汇编读取。[GitHub 存档](https://github.com/Supwils/swil-news/blob/main/NEWS/finance/en/2026-06-25_finance-digest.md)
- 【M】2026-07-27：长鑫科技在科创板上市（688825.SH），募资 579.19 亿元（原站未打开，经二手汇编核对）。[证券时报](https://www.stcn.com/article/detail/4042363.html)
- 【L】2026-08：美光称 HBM3E/HBM4E 每片晶圆挤占 3-4 片常规 DRAM，2027 年 HBM 更紧（二手，原站未打开）。[ad-hoc-news](https://ad-hoc-news.de/boerse/news/unternehmensnachrichten/micron-s-memory-squeeze-when-physics-becomes-the-business-plan/69936908)

**MUSE / Meta**
- 【M】2026-09-08：Meta 发布个人 AI 智能体 Muse。两个 GitHub 存档互相印证，Meta 自有站点被拦截。[快讯存档](https://github.com/qjlxg/wei/issues/2860)；[paper_notes 存档](https://github.com/AkihikoWatanabe/paper_notes/issues/6538)
- 【M】2026-09-10：摩根大通上调 Meta 至增持，称 Muse 上线第二天在美区 App Store 最高排名第 3。[快讯存档](https://github.com/qjlxg/wei/issues/2873)
- 【L】2026-09：单一来源称 Muse “登顶”、两周约 280 万下载（Sensor Tower），与摩根大通口径冲突，未核实（原站未打开）。[TechCrunch](https://techcrunch.com/2026/09/08/meta-debuts-its-muse-ai-agent-will-consumers-trust-it/)
- 【M】2026-07-29/30：Meta 2026 年 capex 指引 1,300-1,450 亿美元，Q2 自由现金流 7.84 亿美元。[快讯存档](https://github.com/qjlxg/wei/issues/2159)
- 【L】2025-11：Meta 洽谈 2027 年起在自有机房部署 TPU，2026 年未见落地证据（原站未打开）。[TrendForce](https://www.trendforce.com/news/2025/11/25/news-meta-reportedly-weighs-google-tpu-deployment-in-2027-boosting-broadcom-taiwans-guc/)

**石墨烯**
- 【M】2026-09-16/17：德尔未来石墨烯收入占营收约 0.05%（2026 年半年度口径），没有在手订单。公司口径，经财联社快讯 GitHub 存档转引。[快讯存档](https://github.com/qjlxg/wei/issues/2912)
- 【M】2026-06-06：中科院金属所硅-石墨烯-锗势垒晶体管发表于 Nature Communications（射频方向）。[快讯存档](https://github.com/qjlxg/wei/issues/1615)

**WORKBUDDY / 腾讯**
- 【L】2026-02-06 内测、2026-03-09 正式发布、2026-06 PC 端月访问量约 2,097 万次。单一二手百科页，原文未打开。[AI-indeed](https://www.ai-indeed.com/encyclopedia/17907.html)
- 【L】2026-05-29：WorkBuddy 面向海外用户上线（原文未打开）。[TechNode](https://technode.com/2026/05/29/tencent-launches-workbuddy-productivity-ai-agent-for-global-users/)
- 【L】花旗认为 WorkBuddy 降低 AI 使用门槛，可能是国内 AI Agent 的转折点（原文未打开）。[老虎证券资讯](https://www.itiger.com/news/1125565486)

**未能核实、不得写成确定语气的内容**：WorkBuddy 的发布细节和用量（仅有单一二手来源）；Bloom 与 AEP 的 26.5 亿美元合同；Google 2026 年 OCS 台数（1.5 万台还是 2 万台）；Ironwood 和 TPU 8t 所用 OCS 的规格；TPU 8t 是否用 OCS；ISCA 2026、Hot Chips 2026、SIGCOMM 2026 上有无 TPU 8 拓扑或 OCS 披露；Virgo 跨站点层用何种交换；光库“代工占比 70%”；德科立与 iPronics 的合作；“6D Torus”的出处；各代 TPU 的 HBM 供应商份额；GB300 功率平滑用电容还是电池；FCC 新规生效日；OCP Global Summit 2026 具体日期；Fluidstack 矿企园区托管的芯片类型。

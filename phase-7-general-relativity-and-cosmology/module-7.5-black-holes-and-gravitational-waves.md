# Module 7.5 — Black Holes & Gravitational Waves ⭐
**模块 7.5 — 黑洞与引力波 ⭐**

> **Phase 7 — [General Relativity & Cosmology](./README.md)** · Format: Definition → Demonstration → Application
> **第 7 阶段 — 广义相对论与宇宙学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-7.5-black-holes-and-gravitational-waves-derivations.md)

---

## 1. Black Holes: Schwarzschild, Event Horizons, and Kerr · 黑洞：史瓦西解、事件视界与克尔解

**Definition.** The simplest exact solution to the vacuum Einstein equations ($R_{\mu\nu} = 0$, Module 7.4) for a static, spherically symmetric spacetime is the *Schwarzschild metric* (1916):

**定义。** 静态球对称时空的真空爱因斯坦方程（$R_{\mu\nu} = 0$，模块 7.4）最简单的精确解是*史瓦西度规*（1916 年）：

$$ ds^2 = -(1 - r_s/r)\, c^2 dt^2 + (1 - r_s/r)^{-1} dr^2 + r^2 d\Omega^2 $$

where $d\Omega^2 = d\theta^2 + \sin^2\theta\, d\varphi^2$ is the metric on the unit 2-sphere, and the *Schwarzschild radius* is $r_s = 2GM/c^2$. At $r = r_s$, the coefficient $g_{00}$ vanishes and $g_{rr}$ diverges — but this is a *coordinate singularity*: in Kruskal–Szekeres coordinates the metric is smooth there. At $r = 0$ the curvature invariant $R_{\mu\nu\rho\sigma} R^{\mu\nu\rho\sigma}$ diverges — a genuine *physical singularity* signalling the breakdown of classical GR.

其中 $d\Omega^2 = d\theta^2 + \sin^2\theta\, d\varphi^2$ 是单位二维球面的度规，*史瓦西半径*为 $r_s = 2GM/c^2$。在 $r = r_s$ 处，系数 $g_{00}$ 为零而 $g_{rr}$ 发散——但这是*坐标奇点*：在克鲁斯卡尔-塞凯赖什坐标下度规在此处光滑。在 $r = 0$ 处，曲率不变量 $R_{\mu\nu\rho\sigma} R^{\mu\nu\rho\sigma}$ 发散——这是真正的*物理奇点*，标志着经典广义相对论的失效。

The surface $r = r_s$ is the *event horizon*: a null hypersurface from which no causal signal (including light) can escape to $r \to \infty$. An observer freely falling through the horizon notices nothing locally (by the equivalence principle; Module 7.1), but a distant observer sees the infalling observer's signals redshift and freeze at the horizon.

曲面 $r = r_s$ 是*事件视界*：一个零超曲面，任何因果信号（包括光）都无法从中逃逸至 $r \to \infty$。自由穿越视界的观察者在局域上感受不到任何异常（根据等效原理；模块 7.1），而远处的观察者则看到下落观察者的信号红移并在视界处"冻结"。

For a rotating mass (angular momentum $J$), the unique vacuum solution is the *Kerr metric* (1963), characterised by $M$ and the spin parameter $a = J/(Mc)$. It introduces an *ergosphere* — a region outside the horizon where spacetime is dragged so severely that no observer can remain stationary — enabling the Penrose process to extract rotational energy.

对于旋转质量（角动量 $J$），唯一的真空解是*克尔度规*（1963 年），由质量 $M$ 和自旋参数 $a = J/(Mc)$ 表征。它引入了*能层*——一个位于视界之外、时空被拖拽极为剧烈以至于没有观察者能静止的区域——从而使彭罗斯过程能够提取转动能量。

**Demonstration.** The Schwarzschild radius for the Sun: $r_s = 2GM_\odot/c^2 \approx 2 \times (6.67 \times 10^{-11})(2 \times 10^{30})/(9 \times 10^{16}) \approx 2.95$ km. The Sun would have to be compressed to under 3 km radius to form a black hole. For a stellar-mass black hole ($M \approx 10\, M_\odot$), $r_s \approx 30$ km; for the supermassive black hole at the centre of M87 ($M \approx 6.5 \times 10^9\, M_\odot$), $r_s \approx 19$ billion km $\approx 19$ AU.

**演示。** 太阳的史瓦西半径：$r_s = 2GM_\odot/c^2 \approx 2 \times (6.67 \times 10^{-11})(2 \times 10^{30})/(9 \times 10^{16}) \approx 2.95$ km。太阳必须被压缩到 3 km 以下的半径才能形成黑洞。对于恒星级黑洞（$M \approx 10\, M_\odot$），$r_s \approx 30$ km；对于 M87 中心的超大质量黑洞（$M \approx 6.5 \times 10^9\, M_\odot$），$r_s \approx 190$ 亿 km $\approx 19$ AU。

The geodesic equation (Module 7.3) applied to the Schwarzschild metric yields the innermost stable circular orbit (ISCO) at $r = 3r_s = 6GM/c^2$ — inside this radius, no stable circular orbit exists and matter spirals inward. Photon orbits are at $r = (3/2)r_s$ (the photon sphere). These results follow purely from the metric; no additional physics is needed.

将测地线方程（模块 7.3）应用于史瓦西度规，得到最内稳定圆轨道（ISCO）在 $r = 3r_s = 6GM/c^2$ 处——在此半径以内不存在稳定圆轨道，物质向内螺旋。光子轨道在 $r = (3/2)r_s$ 处（光子球）。这些结果纯粹来自度规，无需额外物理。

**Application.** Astrophysical black holes are observed across a wide mass range:
- *Stellar-mass* ($5$–$100\, M_\odot$): endpoints of massive-star collapse, detected in X-ray binaries and via gravitational waves.
- *Supermassive* ($10^6$–$10^{10}\, M_\odot$): reside in galactic nuclei; directly imaged by the Event Horizon Telescope (M87*, 2019; Sgr A*, 2022).
- Hawking radiation (semiclassical GR, not covered here) predicts black holes slowly evaporate with temperature $T_H = \hbar c^3/(8\pi GM k_B)$, relevant only for primordial or microscopic black holes.

**应用。** 天体物理黑洞在宽广的质量范围内被观测到：
- *恒星级*（$5$–$100\, M_\odot$）：大质量恒星坍缩的终态，通过 X 射线双星和引力波探测。
- *超大质量*（$10^6$–$10^{10}\, M_\odot$）：位于星系核心；由事件视界望远镜直接成像（M87*，2019 年；Sgr A*，2022 年）。
- 霍金辐射（半经典广义相对论，此处不作详述）预言黑洞以温度 $T_H = \hbar c^3/(8\pi GM k_B)$ 缓慢蒸发，仅对原初或微观黑洞有意义。

---

## 2. Linearized Gravity and Gravitational Waves · 线性化引力与引力波

**Definition.** Far from sources or for weak fields, write $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ with $|h_{\mu\nu}| \ll 1$. Expanding the EFE to first order in $h_{\mu\nu}$ and choosing *Lorenz gauge* ($\partial^\mu \bar{h}_{\mu\nu} = 0$, where $\bar{h}_{\mu\nu} = h_{\mu\nu} - \tfrac12 \eta_{\mu\nu} h$ is the trace-reversed perturbation) gives:

**定义。** 在远离源或弱场情况下，令 $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$，其中 $|h_{\mu\nu}| \ll 1$。将 EFE 对 $h_{\mu\nu}$ 展开至一阶，并选取*洛伦兹规范*（$\partial^\mu \bar{h}_{\mu\nu} = 0$，其中 $\bar{h}_{\mu\nu} = h_{\mu\nu} - \tfrac12 \eta_{\mu\nu} h$ 为迹反转微扰），得：

$$ \Box\, \bar{h}_{\mu\nu} = -\frac{16\pi G}{c^4} T_{\mu\nu} $$

where $\Box = -(1/c^2)\partial_t^2 + \nabla^2$ is the flat-space d'Alembertian. In vacuum ($T_{\mu\nu} = 0$) this is a wave equation: gravitational perturbations propagate at speed $c$. These are *gravitational waves* (GWs).

其中 $\Box = -(1/c^2)\partial_t^2 + \nabla^2$ 是平坦时空的达朗贝尔算符。在真空（$T_{\mu\nu} = 0$）中，这是一个波动方程：引力扰动以速度 $c$ 传播。这就是*引力波*（GW）。

In transverse-traceless (TT) gauge (the radiation gauge), only the spatial transverse components survive. A wave propagating in the $z$-direction has two independent polarizations:

在横向无迹（TT）规范（辐射规范）下，只有空间横向分量存在。沿 $z$ 方向传播的波有两个独立偏振态：

$$ h_{\mu\nu}^{\text{TT}} = \left[ h_+ (\hat{x}\otimes\hat{x} - \hat{y}\otimes\hat{y}) + h_\times (\hat{x}\otimes\hat{y} + \hat{y}\otimes\hat{x}) \right] \cos(kz - \omega t) $$

The $+$ polarization stretches space in $x$ and squeezes in $y$ (and vice versa); the $\times$ polarization does the same at $45^\circ$. The strain $h = \Delta L/L$ measures the fractional change in proper distance between free-falling test masses — the observable quantity.

$+$ 偏振在 $x$ 方向拉伸时空、在 $y$ 方向压缩（反之亦然）；$\times$ 偏振在 $45^\circ$ 方向做同样的事。应变 $h = \Delta L/L$ 测量自由下落检验质量之间固有距离的分数变化——这是可观测量。

**Demonstration.** The *quadrupole formula* gives the leading GW power emitted by a source with time-varying quadrupole moment $Q_{ij}$:

**演示。** *四极矩公式*给出四极矩 $Q_{ij}$ 随时间变化的源辐射的主导引力波功率：

$$ P = \frac{G}{5c^5} \left\langle \frac{d^3 Q_{ij}}{dt^3} \cdot \frac{d^3 Q^{ij}}{dt^3} \right\rangle $$

For two equal masses $M$ in circular orbit of separation $2r$ and orbital frequency $\Omega$: $P = (32 G^4 M^5)/(5 c^5 r^5)$. As energy is radiated the orbit decays — the *inspiral*. For the Hulse–Taylor binary pulsar (1974), this orbital decay matched the quadrupole prediction to $\approx 0.1\%$, providing indirect evidence for GWs 40 years before direct detection.

对于两个等质量 $M$ 在间距 $2r$、轨道频率 $\Omega$ 的圆轨道上运行：$P = (32 G^4 M^5)/(5 c^5 r^5)$。随着能量辐射，轨道衰减——即*旋近*。赫尔斯-泰勒双脉冲星（1974 年）的轨道衰减与四极矩预测吻合至约 $0.1\%$，在直接探测前 40 年提供了引力波的间接证据。

LIGO's first detection (GW150914, September 2015) observed $h \sim 10^{-21}$ from a binary black hole merger ($\approx 36\, M_\odot + 29\, M_\odot$ at $\approx 410$ Mpc). The strain implied $\Delta L \sim 10^{-18}$ m — a thousandth of a proton radius — over a 4 km baseline, detected by laser interferometry.

LIGO 的首次探测（GW150914，2015 年 9 月）观测到来自双黑洞并合（约 $36\, M_\odot + 29\, M_\odot$，距离约 410 Mpc）的 $h \sim 10^{-21}$。该应变意味着在 4 km 基线上 $\Delta L \sim 10^{-18}$ m——质子半径的千分之一——由激光干涉仪探测。

**Application.**
- *Multi-messenger astronomy*: GW170817 (2017) detected GWs from a binary neutron star merger simultaneously with a short gamma-ray burst and optical/X-ray/radio afterglow — the first multi-messenger GW event. It constrained the neutron star equation of state and the Hubble constant.
- *Parameter estimation*: GW signals encode the chirp mass $M_c = (M_1 M_2)^{3/5}/(M_1+M_2)^{1/5}$, luminosity distance, and spin parameters — allowing population studies of compact objects.
- *Future detectors*: LISA (space-based, launch ~2035) will access millihertz GWs from supermassive black hole mergers and galactic binaries; Einstein Telescope will improve sensitivity by an order of magnitude.

**应用。**
- *多信使天文学*：GW170817（2017 年）同时探测到双中子星并合产生的引力波、短伽马射线暴和光学/X 射线/射电余辉——首个多信使引力波事件。它约束了中子星状态方程和哈勃常数。
- *参数估计*：引力波信号编码了啁啾质量 $M_c = (M_1 M_2)^{3/5}/(M_1+M_2)^{1/5}$、光度距离和自旋参数——允许对致密天体进行总体统计研究。
- *未来探测器*：LISA（空间基线，约 2035 年发射）将探测来自超大质量黑洞并合和银河系双星的毫赫兹引力波；爱因斯坦望远镜将灵敏度提升一个量级。

---

**Self-test (blank page)**

1. Derive the Schwarzschild radius $r_s = 2GM/c^2$ from dimensional analysis and the condition that the escape velocity equals $c$. Why is $r_s = r_s(M)$ a coordinate singularity rather than a physical one?
2. A gravitational wave passes Earth with strain $h = 5 \times 10^{-22}$. What is the fractional change in distance between two free-falling mirrors separated by $L = 4$ km? How does LIGO's Fabry–Pérot cavity improve sensitivity?
3. State the two GW polarizations in TT gauge. How does a ring of free-falling test particles respond to each polarization over one GW cycle?

**自测（空白页）**

1. 利用量纲分析和逃逸速度等于 $c$ 的条件推导史瓦西半径 $r_s = 2GM/c^2$。为何 $r_s$ 处是坐标奇点而非物理奇点？
2. 一列应变为 $h = 5 \times 10^{-22}$ 的引力波经过地球。间距 $L = 4$ km 的两个自由下落反射镜之间距离的分数变化是多少？LIGO 的法布里-珀罗腔如何提升灵敏度？
3. 陈述 TT 规范下两种引力波偏振态。一圈自由下落检验粒子在经历一个引力波周期时，对每种偏振态分别如何响应？

---

← Previous: [Module 7.4 — Einstein's Field Equations](./module-7.4-einsteins-field-equations.md) · [Phase 7 index](./README.md) · Next: [Module 7.6 — Cosmology](./module-7.6-cosmology.md) →

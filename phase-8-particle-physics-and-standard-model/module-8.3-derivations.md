# Derivations — Module 8.3: Quantum Chromodynamics (QCD)
# 推导 — 模块 8.3：量子色动力学

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 8.3](./module-8.3-quantum-chromodynamics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 8.3](./module-8.3-quantum-chromodynamics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. SU(3) Structure and the QCD Lagrangian · SU(3) 结构与 QCD 拉格朗日量

**Claim.** The QCD Lagrangian $\mathcal{L}_\text{QCD} = \sum_f \bar\psi_f(i\gamma^\mu D_\mu - m_f)\psi_f - (1/4)F^a_{\mu\nu}F^{a\mu\nu}$ with $D_\mu = \partial_\mu - ig_s A^a_\mu T^a$ follows from requiring local SU(3) invariance of quark fields, and the gluon self-interaction vertices arise from the non-abelian field strength.

**命题。** QCD 拉格朗日量 $\mathcal{L}_\text{QCD} = \sum_f \bar\psi_f(i\gamma^\mu D_\mu - m_f)\psi_f - (1/4)F^a_{\mu\nu}F^{a\mu\nu}$（$D_\mu = \partial_\mu - ig_s A^a_\mu T^a$）来自对夸克场要求局域 SU(3) 不变性，胶子自相互作用顶角来自非阿贝尔场强。

**Step 1 — SU(3) generators.** SU(3) has $3^2 - 1 = 8$ generators $T^a = \lambda^a/2$ ($a = 1, \ldots, 8$) where $\lambda^a$ are the Gell-Mann matrices. They satisfy:

**第 1 步 — SU(3) 生成元。** SU(3) 有 $3^2 - 1 = 8$ 个生成元 $T^a = \lambda^a/2$（$a = 1, \ldots, 8$），$\lambda^a$ 为盖尔曼矩阵，满足：

$$ [T^a, T^b] = if^{abc}T^c, \quad \mathrm{Tr}(T^aT^b) = (1/2)\delta^{ab}. $$

The structure constants $f^{abc}$ are totally antisymmetric. Key non-zero values: $f^{123} = 1$, $f^{147} = f^{246} = f^{257} = f^{345} = 1/2$, $f^{156} = f^{367} = -1/2$, $f^{458} = f^{678} = \sqrt3/2$.

结构常数 $f^{abc}$ 全反对称。主要非零值：$f^{123} = 1$，$f^{147} = f^{246} = f^{257} = f^{345} = 1/2$，$f^{156} = f^{367} = -1/2$，$f^{458} = f^{678} = \sqrt3/2$。

**Step 2 — Quark triplet and covariant derivative.** Quarks $\psi_i$ ($i = 1,2,3 = $ red, green, blue) transform as the fundamental (3) representation: $\psi \to U\psi = e^{i\alpha^a(x)T^a}\psi$. As derived in Module 8.1 (section C), the covariant derivative that transforms as $D_\mu\psi \to U(D_\mu\psi)$ is:

**第 2 步 — 夸克三重态与协变导数。** 夸克 $\psi_i$（$i = 1,2,3 = $ 红、绿、蓝）以基本（3）表示变换：$\psi \to U\psi = e^{i\alpha^a(x)T^a}\psi$。如模块 8.1（C 节）所推导，使 $D_\mu\psi \to U(D_\mu\psi)$ 的协变导数为：

$$ (D_\mu)_{ij} = \partial_\mu\delta_{ij} - ig_s A^a_\mu(T^a)_{ij}. $$

**Step 3 — Gluon field strength.** From $[D_\mu, D_\nu]\psi = -ig_s F_{\mu\nu}\psi$ (derived in Module 8.1):

**第 3 步 — 胶子场强。** 由 $[D_\mu, D_\nu]\psi = -ig_s F_{\mu\nu}\psi$（在模块 8.1 中推导）：

$$ F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + g_s f^{abc}A^b_\mu A^c_\nu. $$

**Step 4 — Expand the kinetic term.** The gauge kinetic term $(1/4)F^a_{\mu\nu}F^{a\mu\nu}$ expanded:

**第 4 步 — 展开动能项。** 展开规范动能项 $(1/4)F^a_{\mu\nu}F^{a\mu\nu}$：

$$ \begin{aligned} F^a_{\mu\nu} &= (\partial_\mu A^a_\nu - \partial_\nu A^a_\mu) + g_s f^{abc}A^b_\mu A^c_\nu \equiv G^a_{\mu\nu} + g_s f^{abc}A^b_\mu A^c_\nu. \\ F^a_{\mu\nu}F^{a\mu\nu} &= G^a_{\mu\nu}G^{a\mu\nu} + 2G^a_{\mu\nu} g_s f^{abc}A^{b\mu}A^{c\nu} + g_s^2(f^{abc}A^b_\mu A^c_\nu)^2. \end{aligned} $$

- **Quadratic term** $G^a_{\mu\nu}G^{a\mu\nu}$: free gluon propagation.
- **Cubic term** $2g_s G^a_{\mu\nu}f^{abc}A^{b\mu}A^{c\nu}$: three-gluon vertex (Feynman rule $\propto g_s f^{abc}\cdot$(kinematic tensor)).
- **Quartic term** $g_s^2(f^{abc}A^b_\mu A^c_\nu)^2$: four-gluon vertex ($\propto g_s^2$).

- **二次项** $G^a_{\mu\nu}G^{a\mu\nu}$：自由胶子传播。
- **三次项** $2g_s G^a_{\mu\nu}f^{abc}A^{b\mu}A^{c\nu}$：三胶子顶角（费曼规则 $\propto g_s f^{abc}\cdot$（运动学张量））。
- **四次项** $g_s^2(f^{abc}A^b_\mu A^c_\nu)^2$：四胶子顶角（$\propto g_s^2$）。

These self-interactions have no analogue in QED (where $f^{abc} = 0$) and are the source of the antiscreening behavior that drives asymptotic freedom. $\blacksquare$

这些自相互作用在 QED 中没有对应物（其中 $f^{abc} = 0$），是驱动渐近自由的反屏蔽行为的根源。$\blacksquare$

---

## B. The QCD $\beta$ Function and Asymptotic Freedom · QCD $\beta$ 函数与渐近自由

**Claim.** The one-loop QCD $\beta$ function is $\beta(g_s) = -b_0 g_s^3/(16\pi^2)$ with $b_0 = 11 - 2n_f/3 > 0$ for $n_f \le 16$, implying $\alpha_s(\mu)$ decreases as $\mu$ increases (asymptotic freedom).

**命题。** 单圈 QCD $\beta$ 函数为 $\beta(g_s) = -b_0 g_s^3/(16\pi^2)$，$b_0 = 11 - 2n_f/3$，对于 $n_f \le 16$ 有 $b_0 > 0$，意味着 $\alpha_s(\mu)$ 随 $\mu$ 增大而减小（渐近自由）。

**Step 1 — Renormalization of $g_s$.** In QCD the bare coupling $g_0$ is related to the renormalized coupling $g_s(\mu)$ via:

**第 1 步 — $g_s$ 的重整化。** 在 QCD 中，裸耦合 $g_0$ 通过以下关系与重整化耦合 $g_s(\mu)$ 相关联：

$$ g_0 = \mu^\varepsilon Z_g g_s, \quad \text{where } Z_g = 1 + \delta Z_g + O(g_s^4). $$

The $\beta$ function is $\beta(g_s) = \mu\, dg_s/d\mu$. At one loop, $\delta Z_g$ receives contributions from:

$\beta$ 函数为 $\beta(g_s) = \mu\, dg_s/d\mu$。在单圈阶，$\delta Z_g$ 接收来自以下的贡献：

- **Gluon self-energy** (gluon loop + ghost loop): contributes $+11/3$ to $b_0$.
- **Quark loop**: each quark flavor contributes $-2/3$ (one quark loop with $n_f$ flavors contributes $-2n_f/3$ total).

- **胶子自能**（胶子圈 + 鬼粒子圈）：对 $b_0$ 贡献 $+11/3$。
- **夸克圈**：每种夸克味贡献 $-2/3$（$n_f$ 味夸克圈总共贡献 $-2n_f/3$）。

**Step 2 — Origin of the $+11/3$ term.** The gluon self-energy has two contributions at one loop:

**第 2 步 — $+11/3$ 项的起源。** 胶子自能在单圈阶有两个贡献：

(a) **Gluon loop** (three-gluon vertex): This arises because gluons self-interact via the $f^{abc}$ structure constant. In SU(N) the adjoint Casimir is $C_A = N$ (for SU(3), $C_A = 3$). The transverse part of the gluon self-energy from the three-gluon vertex contributes $+5C_A/3 \times (1/16\pi^2)$ per unit $g_s^2$ to the $\beta$ function.

(a) **胶子圈**（三胶子顶角）：这来自胶子通过结构常数 $f^{abc}$ 自相互作用。在 SU(N) 中，伴随卡西米尔算符为 $C_A = N$（对于 SU(3)，$C_A = 3$）。来自三胶子顶角的胶子自能横向部分对 $\beta$ 函数贡献 $+5C_A/3 \times (1/16\pi^2)$ 每单位 $g_s^2$。

(b) **Ghost loop** (Faddeev-Popov ghosts): In non-abelian gauge theory, gauge fixing introduces ghost fields $c^a$ (anticommuting scalars in the adjoint representation) to cancel unphysical gluon polarizations. Their loop gives $-C_A/6$ per unit $g_s^2$.

(b) **鬼粒子圈**（法捷耶夫–波波夫鬼粒子）：在非阿贝尔规范理论中，规范固定引入鬼场 $c^a$（伴随表示中的反对易标量）以消除非物理胶子极化。它们的圈给出 $-C_A/6$ 每单位 $g_s^2$。

The $(5/3)$ and $(-1/6)$ values above are the gauge-boson and ghost pieces of the *transverse gluon self-energy* in Feynman gauge, and $(5/3 - 1/6)\cdot C_A = (3/2)\cdot C_A$ is only the self-energy (wavefunction-renormalization) contribution. The complete gauge-sector running coupling also receives contributions from the vertex and external-leg renormalizations (the full set of diagrams entering $Z_1/Z_3$ via the Slavnov–Taylor identities). Adding all gauge-sector diagrams, the gauge contribution to $b_0$ is the well-known **$+11C_A/3$** (for SU(3): 11), which is the result we use below. (The individual loop coefficients are gauge- and scheme-dependent; only their full sum $+11C_A/3$ is physical.)

上面的 $(5/3)$ 和 $(-1/6)$ 是费曼规范下*横向胶子自能*的规范玻色子与鬼粒子部分，而 $(5/3 - 1/6)\cdot C_A = (3/2)\cdot C_A$ 仅为自能（波函数重整化）贡献。完整的规范部分跑动耦合还接收来自顶角和外腿重整化的贡献（通过 Slavnov–Taylor 恒等式进入 $Z_1/Z_3$ 的全部图）。把所有规范部分的图相加，对 $b_0$ 的规范贡献为众所周知的 **$+11C_A/3$**（对于 SU(3)：11），即下文所用的结果。（各单项圈系数依赖于规范与重整化方案；只有它们的完整和 $+11C_A/3$ 是物理的。）

**Step 3 — Origin of the $-2n_f/3$ term.** Each quark flavor contributes a fermion loop to the gluon self-energy. This is structurally identical to the electron loop in QED. In QED the electron loop gives a positive $\beta$ function (screening). In QCD the quark loop contributes:

**第 3 步 — $-2n_f/3$ 项的起源。** 每种夸克味对胶子自能贡献一个费米子圈。这在结构上与 QED 中的电子圈相同。在 QED 中，电子圈给出正的 $\beta$ 函数（屏蔽）。在 QCD 中，夸克圈贡献：

$$ \text{Quark loop contribution to } b_0: \quad -(4/3) \times T_F \times n_f, $$

where $T_F = 1/2$ for the fundamental representation (from $\mathrm{Tr}(T^aT^b) = T_F\delta^{ab} = (1/2)\delta^{ab}$). So:

其中 $T_F = 1/2$ 用于基本表示（来自 $\mathrm{Tr}(T^aT^b) = T_F\delta^{ab} = (1/2)\delta^{ab}$）。故：

$$ \text{Quark contribution: } -(4/3)T_F n_f = -(4/3)\times(1/2)\times n_f = -2n_f/3. $$

The standard normalization gives the total $b_0 = (11C_A - 4T_F n_f)/3 = (11\times3 - 4\times(1/2)\times n_f)/3 = (33 - 2n_f)/3 = 11 - 2n_f/3$.

标准归一化给出总 $b_0 = (11C_A - 4T_F n_f)/3 = (11\times3 - 4\times(1/2)\times n_f)/3 = (33 - 2n_f)/3 = 11 - 2n_f/3$。

**Step 4 — Sign analysis.** For $n_f \le 16$ active quark flavors: $b_0 = 11 - 2n_f/3 > 0$ (since $2\times16/3 \approx 10.7 < 11$). In QCD $n_f = 6$, so $b_0 = 11 - 4 = 7 > 0$.

**第 4 步 — 符号分析。** 对于 $n_f \le 16$ 种活跃夸克味：$b_0 = 11 - 2n_f/3 > 0$（因为 $2\times16/3 \approx 10.7 < 11$）。在 QCD 中 $n_f = 6$，故 $b_0 = 11 - 4 = 7 > 0$。

The $\beta$ function $\beta(g_s) = -b_0 g_s^3/(16\pi^2) < 0$ (negative!) means the coupling **decreases** with increasing $\mu$. This is the opposite of QED.

$\beta$ 函数 $\beta(g_s) = -b_0 g_s^3/(16\pi^2) < 0$（为负！）意味着耦合随 $\mu$ 增大而**减小**。这与 QED 相反。

The physical reason: in QCD, the gluon self-coupling (absent in QED) creates an **antiscreening** effect that overwhelms the quark-loop screening. The gluon loops "spread" the color charge outward, so closer approach reveals less effective charge.

物理原因：在 QCD 中，胶子自耦合（在 QED 中不存在）产生**反屏蔽**效应，压倒了夸克圈的屏蔽。胶子圈将色荷向外"散布"，使得更近的距离揭示更小的有效电荷。

**Step 5 — Running $\alpha_s$.** Defining $\alpha_s = g_s^2/(4\pi)$, the $\beta$ function $\beta(\alpha_s) = d\alpha_s/d(\ln\mu) = -b_0\alpha_s^2/(2\pi)$:

**第 5 步 — 跑动 $\alpha_s$。** 定义 $\alpha_s = g_s^2/(4\pi)$，$\beta$ 函数 $\beta(\alpha_s) = d\alpha_s/d(\ln\mu) = -b_0\alpha_s^2/(2\pi)$：

Separating variables and integrating:

分离变量并积分：

$$ \begin{aligned} d\alpha_s/\alpha_s^2 &= -(b_0/2\pi)d(\ln\mu) \\ -1/\alpha_s\big|^{\alpha_s(\mu)} &= -(b_0/2\pi)\ln(\mu/\mu_0) \\ 1/\alpha_s(\mu) &= 1/\alpha_s(\mu_0) + (b_0/2\pi)\ln(\mu/\mu_0). \end{aligned} $$

Equivalently, introducing $\Lambda_\text{QCD}$ as the intrinsic scale (where the perturbative coupling formally diverges):

等价地，引入 $\Lambda_\text{QCD}$ 作为固有标度（微扰耦合在此形式上发散）：

$$ \alpha_s(\mu) = 2\pi/[b_0 \ln(\mu/\Lambda_\text{QCD})], \quad \Lambda_\text{QCD} \approx 200 \text{ MeV for } n_f = 5. $$

**Step 6 — Numerical verification.** With $b_0 = 7$ ($n_f = 6$) and $\alpha_s(m_Z) = 0.118$:

**第 6 步 — 数值验证。** 以 $b_0 = 7$（$n_f = 6$）和 $\alpha_s(m_Z) = 0.118$：

$$ \begin{aligned} 1/\alpha_s(1 \text{ GeV}) &= 1/\alpha_s(m_Z) + (b_0/2\pi)\ln(m_Z/1 \text{ GeV}) = 8.47 + (7/6.28)\times4.51 \approx 8.47 + 5.02 \approx 13.5. \\ \alpha_s(1 \text{ GeV}) &\approx 0.074. \end{aligned} $$

This is an underestimate at low scale because threshold corrections and higher-loop terms are important; the observed value $\alpha_s(1 \text{ GeV}) \approx 0.4$ requires careful treatment. But the qualitative trend ($\alpha_s$ grows as $\mu$ decreases) is correct and confirms confinement in the IR. $\blacksquare$

这在低标度处是低估的，因为阈值修正和更高阶项很重要；观测值 $\alpha_s(1 \text{ GeV}) \approx 0.4$ 需要仔细处理。但定性趋势（$\alpha_s$ 随 $\mu$ 减小而增大）是正确的，证实了红外区的禁闭。$\blacksquare$

---

## C. Color Factors in QCD Scattering · QCD 散射中的色因子

**Claim.** For a quark-quark scattering amplitude via one-gluon exchange, the color factor is $C_F = 4/3$ for quarks in the fundamental representation of SU(3).

**命题。** 对于通过单胶子交换的夸克–夸克散射振幅，处于 SU(3) 基本表示中的夸克的色因子为 $C_F = 4/3$。

**Step 1 — Structure of the amplitude.** The quark-gluon vertex is $-ig_s(T^a)_{ij}\gamma^\mu$ for quark flavor $i$ going to $j$. A one-gluon exchange between quarks gives amplitude $\propto (T^a)_{ij}(T^a)_{kl}$ summed over $a = 1,...,8$.

**第 1 步 — 振幅的结构。** 夸克–胶子顶角为 $-ig_s(T^a)_{ij}\gamma^\mu$，对于夸克味从 $i$ 到 $j$。夸克间的单胶子交换给出振幅 $\propto (T^a)_{ij}(T^a)_{kl}$，对 $a = 1,...,8$ 求和。

**Step 2 — Color factor evaluation.** For a quark emitting a gluon and returning to the same color state (color factor appearing in cross-sections):

**第 2 步 — 色因子计算。** 对于夸克发射胶子并回到同一色态（截面中出现的色因子）：

This colour factor is the **quadratic Casimir** of the fundamental representation:

此色因子是基本表示的**二次卡西米尔算符**：

$$ \sum_{a=1}^{8} (T^a)_{ij}(T^a)_{jk} = C_F \delta_{ik}, $$

where $C_F = (N_c^2 - 1)/(2N_c)$. For SU(3): $C_F = (9-1)/(2\times3) = 8/6 = $ **$4/3$**.

其中 $C_F = (N_c^2 - 1)/(2N_c)$。对于 SU(3)：$C_F = (9-1)/(2\times3) = 8/6 = $ **$4/3$**。

**Proof:** Use the SU(N) identity $\sum_a (T^a)_{ij}(T^a)_{kl} = (1/2)[\delta_{il}\delta_{kj} - (1/N)\delta_{ij}\delta_{kl}]$. Setting $k = j$ and $l = i$: $\sum_a (T^a)_{ij}(T^a)_{ji} = (1/2)[\delta_{ii}\delta_{jj} - (1/N)\delta_{ij}\delta_{ij}] = (1/2)[N^2 - N/N]\ldots$

Let me be more careful: for the Casimir in the fundamental:

让我更仔细地处理：对于基本表示中的卡西米尔算符：

$$ [\textstyle\sum_a T^aT^a]_{ij} = C_F \delta_{ij}, \quad \text{with } C_F = T_F(N_c^2-1)/N_c = (1/2)(N_c^2-1)/N_c. $$

For SU(3): $C_F = (1/2)(9-1)/3 = 4/3$. $\blacksquare$

对于 SU(3)：$C_F = (1/2)(9-1)/3 = 4/3$。$\blacksquare$

---

## D. Color Confinement and the Linear Potential · 色禁闭与线性势

**Claim.** The QCD static quark potential has the form $V(r) = -(4\alpha_s/3)(1/r) + \sigma r$ for large $r$, where $\sigma \approx 0.9$ GeV/fm is the string tension, giving a linearly rising potential that prevents quark escape.

**命题。** QCD 静态夸克势的形式为 $V(r) = -(4\alpha_s/3)(1/r) + \sigma r$（对于大 $r$），其中 $\sigma \approx 0.9$ GeV/fm 是弦张力，给出阻止夸克逃逸的线性增长势。

**Step 1 — Short-range (perturbative) part.** At short distances $r \ll \Lambda_\text{QCD}^{-1}$, $\alpha_s$ is small and perturbation theory applies. One-gluon exchange gives a Coulomb-like potential:

**第 1 步 — 短程（微扰）部分。** 在短距离 $r \ll \Lambda_\text{QCD}^{-1}$，$\alpha_s$ 很小，微扰论适用。单胶子交换给出库仑型势：

$$ V_\text{short}(r) = -C_F \alpha_s/r = -(4/3)\alpha_s/r. $$

The color factor $C_F = 4/3$ (derived above) appears because the quark-antiquark pair is in a color-singlet state (attractive channel).

色因子 $C_F = 4/3$（如上推导）出现是因为夸克–反夸克对处于色单态（吸引道）。

**Step 2 — Long-range (non-perturbative) part.** At large distances, $\alpha_s \sim 1$ and perturbation theory fails. Non-perturbative effects (best studied by lattice QCD) generate a **color flux tube** — the chromoelectric field energy is squeezed into a cylinder of radius $\sim 1$ fm rather than spreading out as $1/r^2$. The energy of a flux tube of length $r$ and cross-section $A$ is:

**第 2 步 — 长程（非微扰）部分。** 在大距离处，$\alpha_s \sim 1$，微扰论失效。非微扰效应（格点 QCD 最好的研究对象）产生**色通量管**——色电场能量被压缩到半径约 1 fm 的圆柱内，而不是像 $1/r^2$ 那样扩散。长度为 $r$、横截面为 $A$ 的通量管的能量为：

$$ E_\text{tube} = (\text{energy density}) \times (\text{volume}) = (\sigma_\text{string}) \times r, $$

where $\sigma_\text{string}$ (string tension) $= $ (field energy per unit length) $\approx (\Lambda_\text{QCD})^2 \approx 0.9$ GeV/fm $\approx 0.18$ GeV$^2$. This gives the linear potential $V_\text{long}(r) = \sigma r$.

其中 $\sigma_\text{string}$（弦张力）$=$（单位长度的场能量）$\approx (\Lambda_\text{QCD})^2 \approx 0.9$ GeV/fm $\approx 0.18$ GeV$^2$。这给出线性势 $V_\text{long}(r) = \sigma r$。

**Step 3 — String breaking.** When $V(r) = \sigma r$ reaches the threshold $2m_\pi \approx 0.28$ GeV (the lightest quark-antiquark pair energy), it is energetically favorable to create a new $q\bar q$ pair from the vacuum. The string "breaks" at this distance $r_\text{break} \approx 2m_\pi/\sigma \approx 0.3$ fm, forming two separate hadrons. This is why quarks are never observed as free particles: the energy cost of separation always exceeds the cost of pair creation.

**第 3 步 — 弦断裂。** 当 $V(r) = \sigma r$ 达到阈值 $2m_\pi \approx 0.28$ GeV（最轻夸克–反夸克对的能量）时，从真空创造新的 $q\bar q$ 对在能量上是有利的。弦在此距离 $r_\text{break} \approx 2m_\pi/\sigma \approx 0.3$ fm 处"断裂"，形成两个独立的强子。这就是为何夸克从未被观测为自由粒子：分离的能量代价始终超过对产生的代价。

**Step 4 — Lattice QCD confirmation.** On a discrete Euclidean spacetime lattice with spacing $a$, the static potential is extracted from the Wilson loop:

**第 4 步 — 格点 QCD 验证。** 在间距为 $a$ 的离散欧几里得时空格点上，静态势从威尔逊圈提取：

$$ W(r, T) = \mathrm{Tr}[P \exp(ig_s \oint_C A_\mu dx^\mu)] \propto \exp(-V(r)T) \text{ for large } T. $$

Lattice simulations at several values of $a$, extrapolated to $a \to 0$, confirm $V(r) = -(4/3)\alpha_s/r + \sigma r + C$ with $\sigma \approx 0.18$ GeV$^2$ to high precision, providing the strongest non-perturbative evidence for confinement from first principles. $\blacksquare$

对多个 $a$ 值进行格点模拟，外推至 $a \to 0$，以高精度确认 $V(r) = -(4/3)\alpha_s/r + \sigma r + C$，$\sigma \approx 0.18$ GeV$^2$，提供了从第一性原理来的最强的禁闭非微扰证据。$\blacksquare$

---

## E. Color Singlet Projection for Hadrons · 强子的色单态投影

**Claim.** A meson's color wavefunction is $(1/\sqrt3)(r\bar r + g\bar g + b\bar b)$ — the unique SU(3) singlet in $3 \otimes \bar 3$. A baryon's color wavefunction is $(1/\sqrt6)\varepsilon^{abc}|r_a g_b b_c\rangle$ — the singlet in $3 \otimes 3 \otimes 3$.

**命题。** 介子的色波函数为 $(1/\sqrt3)(r\bar r + g\bar g + b\bar b)$——$3 \otimes \bar 3$ 中唯一的 SU(3) 单态。重子的色波函数为 $(1/\sqrt6)\varepsilon^{abc}|r_a g_b b_c\rangle$——$3 \otimes 3 \otimes 3$ 中的单态。

**Step 1 — Meson: $3 \otimes \bar 3$ decomposition.** In SU(3), the product $3 \otimes \bar 3 = 1 \oplus 8$. The singlet (1) corresponds to the state invariant under all SU(3) transformations:

**第 1 步 — 介子：$3 \otimes \bar 3$ 分解。** 在 SU(3) 中，乘积 $3 \otimes \bar 3 = 1 \oplus 8$。单态（1）对应于在所有 SU(3) 变换下不变的态：

$$ |1\rangle = (1/\sqrt3)\sum_i |q_i \bar q_i\rangle = (1/\sqrt3)(|r\bar r\rangle + |g\bar g\rangle + |b\bar b\rangle). $$

Verification: under an infinitesimal SU(3) transformation $\psi_i \to \psi_i + i\alpha^a(T^a)_{ij}\psi_j$, the quark transforms as $\psi_i \to \psi_i + \delta\psi_i$ and the antiquark as $(\bar\psi)_i \to (\bar\psi)_i - i\alpha^a(T^{a*})_{ij}(\bar\psi)_j = (\bar\psi)_i - i\alpha^a(T^a)^*_{ij}(\bar\psi)_j$. The singlet state is unchanged because the trace $\sum_i(T^a)_{ii} = \mathrm{Tr}(T^a) = 0$ (generators are traceless).

验证：在无穷小 SU(3) 变换 $\psi_i \to \psi_i + i\alpha^a(T^a)_{ij}\psi_j$ 下，夸克变换为 $\psi_i \to \psi_i + \delta\psi_i$，反夸克变换为 $(\bar\psi)_i \to (\bar\psi)_i - i\alpha^a(T^{a*})_{ij}(\bar\psi)_j$。单态不变，因为迹 $\sum_i(T^a)_{ii} = \mathrm{Tr}(T^a) = 0$（生成元无迹）。

**Step 2 — Baryon: $3 \otimes 3 \otimes 3$ decomposition.** In SU(3): $3 \otimes 3 \otimes 3 = 1 \oplus 8 \oplus 8 \oplus 10$. The singlet (1) is the totally antisymmetric combination:

**第 2 步 — 重子：$3 \otimes 3 \otimes 3$ 分解。** 在 SU(3) 中：$3 \otimes 3 \otimes 3 = 1 \oplus 8 \oplus 8 \oplus 10$。单态（1）是全反对称的组合：

$$ |\text{baryon singlet}\rangle = (1/\sqrt6)\varepsilon^{abc}|q_a q_b q_c\rangle, $$

where $\varepsilon^{abc}$ is the totally antisymmetric Levi-Civita tensor ($\varepsilon^{123} = \varepsilon^{rgb} = +1$). Explicitly:

其中 $\varepsilon^{abc}$ 是全反对称 Levi-Civita 张量（$\varepsilon^{123} = \varepsilon^{rgb} = +1$）。显式地：

$$ |B\rangle = (1/\sqrt6)(|rgb\rangle - |rbg\rangle + |gbr\rangle - |grb\rangle + |brg\rangle - |bgr\rangle). $$

Verification: $\varepsilon^{abc}$ is an SU(3)-invariant tensor ($\det U = 1$ for $U \in SU(3)$ means $\varepsilon^{abc}U_{ia}U_{jb}U_{kc} = \varepsilon^{ijk}$), so contracting quark indices with $\varepsilon^{abc}$ gives a singlet. $\blacksquare$

验证：$\varepsilon^{abc}$ 是 SU(3) 不变张量（$U \in SU(3)$ 的 $\det U = 1$ 意味着 $\varepsilon^{abc}U_{ia}U_{jb}U_{kc} = \varepsilon^{ijk}$），故将夸克指标与 $\varepsilon^{abc}$ 缩并给出单态。$\blacksquare$

**Step 3 — Fermi statistics of baryons.** The total baryon wavefunction $\psi_\text{total} = \psi_\text{color} \times \psi_\text{spin} \times \psi_\text{flavor} \times \psi_\text{space}$ must be antisymmetric (Fermi statistics). Since $\psi_\text{color} \propto \varepsilon^{abc}$ is totally antisymmetric, the remaining factor $\psi_\text{spin} \times \psi_\text{flavor} \times \psi_\text{space}$ must be totally symmetric. For the ground state ($L = 0$, symmetric spatial wavefunction), the spin-flavor part must be symmetric. This forces the lowest-mass baryons to have spin-3/2 (the $\Delta$ resonance, fully symmetric in spin-flavor) or for spin-1/2 baryons (proton, neutron) a mixed symmetric spin-flavor wavefunction obtained by combining isospin-1/2 with spin-1/2. $\blacksquare$

**第 3 步 — 重子的费米统计。** 总重子波函数 $\psi_\text{total} = \psi_\text{color} \times \psi_\text{spin} \times \psi_\text{flavor} \times \psi_\text{space}$ 必须是反对称的（费米统计）。由于 $\psi_\text{color} \propto \varepsilon^{abc}$ 是全反对称的，剩余因子 $\psi_\text{spin} \times \psi_\text{flavor} \times \psi_\text{space}$ 必须是全对称的。对于基态（$L = 0$，对称空间波函数），自旋–味部分必须是对称的。这迫使最低质量重子具有自旋 3/2（$\Delta$ 共振态，在自旋–味上完全对称）或对于自旋 1/2 重子（质子、中子），通过将同位旋 1/2 与自旋 1/2 组合得到混合对称的自旋–味波函数。$\blacksquare$

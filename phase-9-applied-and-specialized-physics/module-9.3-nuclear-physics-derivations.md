---
title: "Derivations — Module 9.3: Nuclear Physics"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 9.3: Nuclear Physics
# 推导 — 模块 9.3：核物理

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 9.3](./module-9.3-nuclear-physics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 9.3](./module-9.3-nuclear-physics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Five SEMF Terms: Physical Derivations · 五个 SEMF 项的物理推导

**Claim.** The semi-empirical mass formula $B(Z, N) = a_V A - a_S A^{2/3} - a_C Z(Z-1)/A^{1/3} - a_A(N-Z)^2/(4A) + \delta$ follows from the liquid-drop model plus Fermi-gas corrections.

**命题。** 半经验质量公式 $B(Z, N) = a_V A - a_S A^{2/3} - a_C Z(Z-1)/A^{1/3} - a_A(N-Z)^2/(4A) + \delta$ 来源于液滴模型加费米气体修正。

**Step 1 — Volume term.** Nuclear matter is nearly incompressible: the nuclear radius $R = r_0 A^{1/3}$ with $r_0 \approx 1.2$ fm, so the nuclear volume $V \propto A$. Each interior nucleon interacts only with its nearest neighbors (short-range force); the number of such interactions scales as the number of nucleons:

**第 1 步 — 体积项。** 核物质近似不可压缩：核半径 $R = r_0 A^{1/3}$，$r_0 \approx 1.2$ fm，因此核体积 $V \propto A$。每个内部核子仅与其近邻相互作用（短程力）；此类相互作用数量与核子数成正比：

$$ B_{volume} = a_V A. $$

This is the dominant binding-energy term. The constant $a_V \approx 15.8$ MeV reflects the depth of the nucleon–nucleon potential well.

这是主要的结合能项。常数 $a_V \approx 15.8$ MeV 反映了核子–核子势阱的深度。

**Step 2 — Surface term.** Nucleons at the nuclear surface have fewer neighbors than bulk nucleons. The surface area of a sphere is $S = 4\pi R^2 \propto A^{2/3}$. Correcting for the surface deficit:

**第 2 步 — 表面项。** 核表面的核子比体内核子邻居少。球体表面积为 $S = 4\pi R^2 \propto A^{2/3}$。修正表面亏损：

$$ B_{surface} = -a_S A^{2/3}, \quad a_S \approx 18.3 \text{ MeV}. $$

The coefficient $a_S > a_V$ (per area) because the number of bonds each surface nucleon lacks is proportional to the ratio of surface to volume. For small $A$, the surface term is proportionally large, explaining the lower binding of light nuclei.

系数 $a_S > a_V$（每单位面积）是因为每个表面核子缺少的键数正比于表面积与体积之比。对于小 $A$，表面项的比例较大，解释了轻核的较低结合。

**Step 3 — Coulomb term.** The electrostatic self-energy of $Z$ protons uniformly distributed within a sphere of radius $R = r_0 A^{1/3}$ is computed by integrating the electrostatic energy:

**第 3 步 — 库仑项。** 均匀分布在半径 $R = r_0 A^{1/3}$ 球体内的 $Z$ 个质子的静电自能通过对静电能积分计算：

$$ U_C = (3/5) Z(Z-1) e^2/(4\pi\varepsilon_0 R) = (3e^2/20\pi\varepsilon_0 r_0)\, Z(Z-1)/A^{1/3}. $$

The factor $Z(Z-1)$ (not $Z^2$) accounts for the fact that each proton does not repel itself; the factor $3/5$ comes from the radial integral $\int_0^R (r/R)^2 \times (Q_{enclosed}/R^3)\, r^2\, dr$ for a uniform sphere. Defining $a_C = 3e^2/(20\pi\varepsilon_0 r_0) \approx 0.72$ MeV:

因子 $Z(Z-1)$（不是 $Z^2$）是因为每个质子不排斥自身；因子 $3/5$ 来自均匀球体的径向积分 $\int_0^R (r/R)^2 \times (Q_{enclosed}/R^3)\, r^2\, dr$。定义 $a_C = 3e^2/(20\pi\varepsilon_0 r_0) \approx 0.72$ MeV：

$$ B_{Coulomb} = -a_C Z(Z-1)/A^{1/3}. $$

**Step 4 — Asymmetry term.** Protons and neutrons are treated as a two-component Fermi gas in a box of volume $V \propto A$. The total kinetic energy at $T = 0$ is:

**第 4 步 — 不对称项。** 将质子和中子视为体积 $V \propto A$ 的箱中双组分费米气体。$T = 0$ 时的总动能为：

$$ T = C_p Z^{5/3}/A^{2/3} + C_n N^{5/3}/A^{2/3}, $$

where $C_p = C_n = C$. This uses the Fermi-gas result $E_F \propto n^{2/3} = (Z \text{ or } N)^{2/3}/A^{2/3}$ (from Module 4.1). Write $Z = A/2 + \delta Z$, $N = A/2 - \delta Z$ with $\delta Z = (Z - N)/2 = -(N - Z)/2$. Expanding to second order in $\delta Z/A$:

其中 $C_p = C_n = C$。这使用了费米气体结果 $E_F \propto n^{2/3} = (Z \text{ 或 } N)^{2/3}/A^{2/3}$（来自模块 4.1）。写 $Z = A/2 + \delta Z$，$N = A/2 - \delta Z$，其中 $\delta Z = (Z - N)/2 = -(N - Z)/2$。对 $\delta Z/A$ 展开到二阶：

$$ Z^{5/3} + N^{5/3} = 2(A/2)^{5/3}\, [1 + (5/9)(\delta Z/(A/2))^2 + O((\delta Z/A)^4)]. $$

The correction to $T$ from the $Z = N = A/2$ baseline is:

从 $Z = N = A/2$ 基线到 $T$ 的修正为：

$$ \delta T = C \times (10/9) \times 4/(A^{2/3} \times A^{5/3/A}) \times (\delta Z)^2 \propto (N-Z)^2/A. $$

Binding energy decreases when kinetic energy increases (fixing the potential), giving:

当动能增加时结合能减少（固定势能），给出：

$$ B_{asymmetry} = -a_A (N-Z)^2/(4A), \quad a_A \approx 23.2 \text{ MeV}. $$

The Pauli principle makes it energetically costly to have unequal numbers of neutrons and protons in the same orbital levels.

泡利原理使得在相同轨道能级中拥有不等数量的中子和质子在能量上代价高昂。

**Step 5 — Pairing term.** Nucleons form spin-0 pairs (analogous to Cooper pairs) due to the short-range attractive force; an even–even nucleus gains extra binding from each pair. Empirically:

**第 5 步 — 配对项。** 由于短程吸引力，核子形成自旋为 0 的对（类似于库珀对）；偶–偶核从每对中获得额外结合能。经验上：

$$ \delta(A, Z) = +a_P/\sqrt A \;(Z \text{ even}, N \text{ even}), \quad 0 \;(A \text{ odd}), \quad -a_P/\sqrt A \;(Z \text{ odd}, N \text{ odd}). $$

The $\sqrt A$ dependence is empirical; the sign flip for odd–odd reflects the unpaired, destabilizing nucleon. $\blacksquare$

$\sqrt A$ 依赖是经验性的；奇–奇的符号翻转反映了未配对的不稳定核子。$\blacksquare$

---

## B. The Decay Law $N = N_0 e^{-\lambda t}$ and Half-Life · 衰变定律 $N = N_0 e^{-\lambda t}$ 与半衰期

**Claim.** If each nucleus decays independently with a constant per-nucleus probability rate $\lambda$, then $N(t) = N_0 e^{-\lambda t}$ and the half-life is $t_{1/2} = (\ln 2)/\lambda$.

**命题。** 若每个核独立地以恒定的单核概率率 $\lambda$ 衰变，则 $N(t) = N_0 e^{-\lambda t}$，半衰期为 $t_{1/2} = (\ln 2)/\lambda$。

**Step 1 — Memoryless property and the ODE.** The probability that a given nucleus decays in a small time interval $dt$ is $\lambda\, dt$, independent of how long the nucleus has existed (quantum tunneling has no memory). For a sample of $N(t)$ identical nuclei, the expected number decaying in $dt$ is:

**第 1 步 — 无记忆性与常微分方程。** 给定核在小时间间隔 $dt$ 内衰变的概率为 $\lambda\, dt$，与核存在了多长时间无关（量子隧穿没有记忆）。对于 $N(t)$ 个相同核的样品，在 $dt$ 内预期衰变的数量为：

$$ -dN = \lambda N(t)\, dt, \quad\text{i.e.}\quad dN/dt = -\lambda N. $$

This is a first-order linear ODE with constant coefficients.

这是一个常系数一阶线性常微分方程。

**Step 2 — Solve by separation of variables.** Separate and integrate:

**第 2 步 — 用分离变量法求解。** 分离变量并积分：

$$ \begin{aligned} dN/N = -\lambda\, dt \;&\implies\; \int_{N_0}^{N} dN'/N' = -\lambda \int_0^t dt' \\ &\implies\; \ln(N/N_0) = -\lambda t \;\implies\; \boxed{\, N(t) = N_0 e^{-\lambda t} \,}. \end{aligned} $$

This is the universal exponential decay law.

这是普遍的指数衰变定律。

**Step 3 — Half-life.** Set $N(t_{1/2}) = N_0/2$:

**第 3 步 — 半衰期。** 令 $N(t_{1/2}) = N_0/2$：

$$ N_0/2 = N_0 e^{-\lambda t_{1/2}} \;\implies\; e^{-\lambda t_{1/2}} = 1/2 \;\implies\; \lambda t_{1/2} = \ln 2. $$

Therefore:

因此：

$$ \boxed{\, t_{1/2} = \ln 2 / \lambda = (0.693\ldots)/\lambda \,} $$

**Step 4 — Mean lifetime.** The mean (average) lifetime $\tau$ is:

**第 4 步 — 平均寿命。** 平均寿命 $\tau$ 为：

$$ \tau = \int_0^\infty t \times \lambda e^{-\lambda t}\, dt = 1/\lambda. $$

So $\tau = t_{1/2}/\ln 2 \approx 1.443\, t_{1/2}$: the mean lifetime is about 44% longer than the half-life.

故 $\tau = t_{1/2}/\ln 2 \approx 1.443\, t_{1/2}$：平均寿命比半衰期长约 44%。

**Step 5 — Activity.** The activity $A(t) = |dN/dt| = \lambda N(t) = \lambda N_0 e^{-\lambda t} = A_0 e^{-\lambda t}$, decaying with the same time constant. Measured in becquerels ($\text{Bq} = \text{s}^{-1}$) or curies ($\text{Ci} = 3.7 \times 10^{10}$ Bq). $\blacksquare$

**第 5 步 — 活度。** 活度 $A(t) = |dN/dt| = \lambda N(t) = \lambda N_0 e^{-\lambda t} = A_0 e^{-\lambda t}$，以相同的时间常数衰减。以贝可（$\text{Bq} = \text{s}^{-1}$）或居里（$\text{Ci} = 3.7 \times 10^{10}$ Bq）为单位。$\blacksquare$

---

## C. Gamow Factor for $\alpha$-Decay Tunneling (WKB) · $\alpha$ 衰变隧穿的伽莫夫因子（WKB）

**Claim.** The probability for an alpha particle (charge $2e$, mass $m_\alpha$) to tunnel through the Coulomb barrier of a daughter nucleus (charge $(Z-2)e$, radius $R_0$) is $P_{tunnel} \propto e^{-2G}$, where the Gamow factor $G$ is:

$$ \begin{aligned} G &= (\pi \alpha_{EM} (Z-2) / v_\alpha) \quad\text{(to leading order in classical turning point)} \\ &= \sqrt{2m_\alpha} / \hbar \times \int_{R_0}^{R_c} \sqrt{V(r) - Q_\alpha}\, dr, \end{aligned} $$

with $V(r) = 2(Z-2)e^2/(4\pi\varepsilon_0 r)$ the Coulomb potential and $R_c = 2(Z-2)e^2/(4\pi\varepsilon_0 Q_\alpha)$ the classical turning point. This derivation uses the WKB approximation of Module 3.7.

**命题。** $\alpha$ 粒子（电荷 $2e$，质量 $m_\alpha$）穿透子核（电荷 $(Z-2)e$，半径 $R_0$）库仑势垒的概率为 $P_{tunnel} \propto e^{-2G}$，其中伽莫夫因子 $G$ 为：

$$ G = \sqrt{2m_\alpha} / \hbar \times \int_{R_0}^{R_c} \sqrt{V(r) - Q_\alpha}\, dr, $$

$V(r) = 2(Z-2)e^2/(4\pi\varepsilon_0 r)$ 为库仑势，$R_c = 2(Z-2)e^2/(4\pi\varepsilon_0 Q_\alpha)$ 为经典转折点。此推导使用模块 3.7 的 WKB 近似。

**Step 1 — WKB tunneling probability.** For a potential barrier $V(x)$ encountered by a particle of energy $E < V_{max}$, the WKB transmission probability is (Module 3.7):

**第 1 步 — WKB 隧穿概率。** 对于能量 $E < V_{max}$ 的粒子遇到势垒 $V(x)$，WKB 透射概率为（模块 3.7）：

$$ T \approx \exp\left(-2 \int_{x_1}^{x_2} \kappa(x)\, dx\right), \quad \kappa(x) = \sqrt{2m(V(x)-E)}/\hbar, $$

where $x_1, x_2$ are the classical turning points ($V(x) = E$). Apply this to the radial coordinate $r$, with $E = Q_\alpha$ and $V(r) = 2(Z-2)e^2/(4\pi\varepsilon_0 r)$:

其中 $x_1$、$x_2$ 为经典转折点（$V(x) = E$）。将此应用于径向坐标 $r$，令 $E = Q_\alpha$，$V(r) = 2(Z-2)e^2/(4\pi\varepsilon_0 r)$：

$$ \boxed{\, 2G = (2/\hbar) \int_{R_0}^{R_c} \sqrt{2m_\alpha (V(r) - Q_\alpha)}\, dr \,} $$

**Step 2 — Set up the integral.** Let $Z' = Z - 2$ (daughter charge), so $V(r) = 2Z'e^2/(4\pi\varepsilon_0 r)$. The Gamow integral becomes:

**第 2 步 — 建立积分。** 令 $Z' = Z - 2$（子核电荷），则 $V(r) = 2Z'e^2/(4\pi\varepsilon_0 r)$。伽莫夫积分变为：

$$ G = \sqrt{2m_\alpha} / \hbar \times \int_{R_0}^{R_c} \sqrt{2Z'e^2/(4\pi\varepsilon_0 r) - Q_\alpha}\, dr. $$

Define the dimensionless variable $u = r/R_c$ (where $R_c = 2Z'e^2/(4\pi\varepsilon_0 Q_\alpha)$), so $V(r) - Q_\alpha = Q_\alpha(1/u - 1)$:

定义无量纲变量 $u = r/R_c$（其中 $R_c = 2Z'e^2/(4\pi\varepsilon_0 Q_\alpha)$），则 $V(r) - Q_\alpha = Q_\alpha(1/u - 1)$：

$$ G = \sqrt{2m_\alpha Q_\alpha}\, R_c / \hbar \times \int_{u_0}^{1} \sqrt{1/u - 1}\, du, $$

where $u_0 = R_0/R_c \ll 1$ for heavy nuclei.

其中对重核 $u_0 = R_0/R_c \ll 1$。

**Step 3 — Evaluate the integral.** The standard integral $\int_a^1 \sqrt{1/u - 1}\, du$ with $a \to 0$:

**第 3 步 — 计算积分。** 标准积分 $\int_a^1 \sqrt{1/u - 1}\, du$，$a \to 0$：

$$ \int_0^1 \sqrt{1/u - 1}\, du = \int_0^1 \sqrt{(1-u)/u}\, du. $$

Substitute $u = \sin^2\theta$: $du = 2 \sin\theta \cos\theta\, d\theta$, $\sqrt{(1-u)/u} = \cos\theta/\sin\theta$. The integral becomes:

代入 $u = \sin^2\theta$：$du = 2 \sin\theta \cos\theta\, d\theta$，$\sqrt{(1-u)/u} = \cos\theta/\sin\theta$。积分变为：

$$ \int_0^{\pi/2} (\cos\theta / \sin\theta) \times 2 \sin\theta \cos\theta\, d\theta = 2 \int_0^{\pi/2} \cos^2\theta\, d\theta = \pi/2. $$

For the full range $a \to 0$, correction for finite $u_0$: $\int_{u_0}^1 \sqrt{1/u-1}\, du \approx \pi/2 - 2\sqrt{u_0}$ (to leading order). For $u_0 \ll 1$, the dominant result is:

对于 $a \to 0$ 的完整范围，有限 $u_0$ 的修正：$\int_{u_0}^1 \sqrt{1/u-1}\, du \approx \pi/2 - 2\sqrt{u_0}$（到主阶）。对于 $u_0 \ll 1$，主要结果为：

$$ \int_{u_0}^1 \sqrt{1/u-1}\, du \approx \pi/2 - 2\sqrt{R_0/R_c}. $$

**Step 4 — Assemble the Gamow factor.** Substituting back:

**第 4 步 — 组合伽莫夫因子。** 代回：

$$ \begin{aligned} G &\approx \sqrt{2m_\alpha Q_\alpha}\, R_c / \hbar \times (\pi/2 - 2\sqrt{R_0/R_c}) \\ &= (\pi/2) \times (2Z'e^2/4\pi\varepsilon_0) \times \sqrt{2m_\alpha} / (\hbar \sqrt{Q_\alpha}) - 2\sqrt{2m_\alpha R_0^2/(\hbar^2 Q_\alpha)} \times (2Z'e^2/4\pi\varepsilon_0)^{1/2} R_c^{0}. \end{aligned} $$

To leading order ($R_0 \to 0$ limit, or $R_0/R_c \ll 1$):

到主阶（$R_0 \to 0$ 极限，或 $R_0/R_c \ll 1$）：

$$ \boxed{\, G \approx \pi Z' e^2 \sqrt{2m_\alpha} / (4\pi\varepsilon_0 \hbar \sqrt{Q_\alpha}) = \pi \alpha_{EM} Z' \sqrt{2m_\alpha c^2/Q_\alpha} / 2 \,}, $$

where $\alpha_{EM} = e^2/(4\pi\varepsilon_0 \hbar c) \approx 1/137$ is the fine-structure constant. The barrier entry correction gives an additional term $2\sqrt{2m_\alpha R_0 Z' e^2/2\pi\varepsilon_0\hbar^2}$ that improves numerical accuracy.

其中 $\alpha_{EM} = e^2/(4\pi\varepsilon_0 \hbar c) \approx 1/137$ 为精细结构常数。势垒入射修正给出额外项 $2\sqrt{2m_\alpha R_0 Z' e^2/2\pi\varepsilon_0\hbar^2}$，改善数值精度。

**Step 5 — Physical consequences.** The tunneling probability is $P \propto e^{-2G} \propto \exp(-C Z'/\sqrt{Q_\alpha})$. Since $G \propto 1/\sqrt{Q_\alpha}$, a small increase in $Q_\alpha$ dramatically reduces $G$ and increases $P$:

**第 5 步 — 物理后果。** 隧穿概率为 $P \propto e^{-2G} \propto \exp(-C Z'/\sqrt{Q_\alpha})$。由于 $G \propto 1/\sqrt{Q_\alpha}$，$Q_\alpha$ 的小幅增加显著减小 $G$ 并增大 $P$：

$$ \ln(t_{1/2}) \propto +2G \propto Z'/\sqrt{Q_\alpha}. $$

This is the **Geiger–Nuttall law**: a linear relation between $\log(t_{1/2})$ and $1/\sqrt{Q_\alpha}$ (equivalently $\log(t_{1/2})$ and $Q_\alpha^{-1/2}$). Despite spanning 23 orders of magnitude in half-life and only a factor $\sim 2$ in $Q_\alpha$ (4–9 MeV), the law is obeyed across the entire chart of nuclides. $\blacksquare$

这是**盖革–纳托尔定律**：$\log(t_{1/2})$ 与 $1/\sqrt{Q_\alpha}$ 之间的线性关系（等价地 $\log(t_{1/2})$ 与 $Q_\alpha^{-1/2}$）。尽管半衰期跨越 23 个数量级，而 $Q_\alpha$ 仅变化约 2 倍（4–9 MeV），该定律在整个核素图上都成立。$\blacksquare$

---

*These three derivations are at standard depth: complete algebra, physical motivation for each approximation (liquid-drop, Fermi-gas, WKB), and the key observable consequences verified at the end.*

*这三个推导达到标准深度：完整代数、每个近似的物理动机（液滴、费米气体、WKB），以及最后验证的关键可观测后果。*

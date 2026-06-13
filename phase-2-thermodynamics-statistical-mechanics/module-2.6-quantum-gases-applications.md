# Module 2.6 — Quantum Gases & Applications
**模块 2.6 — 量子气体与应用**

> **Phase 2 — [Thermodynamics & Statistical Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 2 阶段 — 热力学与统计力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-2.6-derivations.md)

---

## 1. The Degenerate Fermi Gas and Black-Body Radiation · 简并费米气体与黑体辐射

**Definition.** A **quantum gas** is one where quantum statistics — not classical phase-space counting — determines the thermodynamic properties. Two limiting cases dominate applications:

**定义。** **量子气体**是指热力学性质由量子统计——而非经典相空间计数——决定的气体。两种极限情形在应用中占主导地位：

**Degenerate Fermi gas** ($T \ll T_F = E_F/k_B$): electrons in a metal at room temperature satisfy $k_B T \ll E_F$, so the Fermi–Dirac distribution is nearly a step function. The density of states in 3D is $g(\varepsilon) \propto \varepsilon^{1/2}$, so the total energy and heat capacity follow from the Sommerfeld expansion (Module 2.5):

**简并费米气体**（$T \ll T_F = E_F/k_B$）：室温下金属中的电子满足 $k_B T \ll E_F$，故费米–狄拉克分布近似为阶跃函数。三维态密度为 $g(\varepsilon) \propto \varepsilon^{1/2}$，故总能量和热容由索末菲展开（模块 2.5）得出：

$$ C_\text{el} = \frac{\pi^2}{2} N k_B \frac{k_B T}{E_F} \propto T. $$

This linear-$T$ electronic heat capacity is far below the classical equipartition value, explaining why the electron gas does not swamp the lattice contribution at low temperatures.

这个与 $T$ 成正比的电子热容远低于经典能均分值，解释了为什么电子气在低温下不会淹没晶格的贡献。

**Black-body radiation** (photon gas): photons are massless spin-1 bosons with $\mu = 0$ (photon number is not conserved). The mean occupation of a mode at frequency $\nu$ is the **Planck distribution**:

**黑体辐射**（光子气）：光子是质量为零的自旋-1 玻色子，$\mu = 0$（光子数不守恒）。频率为 $\nu$ 的模式的平均占据数为**普朗克分布**：

$$ n(\nu) = \frac{1}{e^{h\nu/k_B T} - 1}. $$

Summing over all modes in a cavity gives the spectral energy density

对腔体中所有模式求和给出谱能量密度

$$ u(\nu, T) = \frac{8\pi h}{c^3} \frac{\nu^3}{e^{h\nu/k_B T} - 1}, $$

and integrating over $\nu$ gives the Stefan–Boltzmann law: total radiated power $\propto T^4$. The Rayleigh–Jeans law (classical equipartition) predicts $u \propto \nu^2 T$ with no cut-off — the ultraviolet catastrophe — which Planck's quantized modes resolve.

对 $\nu$ 积分给出斯特藩–玻尔兹曼定律：总辐射功率 $\propto T^4$。瑞利–金斯定律（经典能均分）预测 $u \propto \nu^2 T$ 且无截止——即紫外灾变——普朗克的量子化模式解决了这一问题。

**Demonstration.** The electronic heat capacity is extracted from total measured $C(T) = \gamma T + A T^3$ at low temperature: the linear term isolates $C_\text{el} = \gamma T$ with $\gamma = \frac{\pi^2}{3} k_B^2 g(E_F)$, directly measuring the density of states at the Fermi level. For copper, $E_F \approx 7$ eV gives $T_F \approx 81\,000$ K, so at 300 K the ratio $k_B T/E_F \approx 0.004$ — confirming deep degeneracy and explaining why only $\sim 0.4\%$ of electrons are thermally active.

**演示。** 电子热容从低温总测量热容 $C(T) = \gamma T + A T^3$ 中提取：线性项分离出 $C_\text{el} = \gamma T$，其中 $\gamma = \frac{\pi^2}{3} k_B^2 g(E_F)$，直接测量费米能级处的态密度。对于铜，$E_F \approx 7$ eV 给出 $T_F \approx 81\,000$ K，故在 300 K 时 $k_B T/E_F \approx 0.004$——证实了深度简并，并解释了为什么只有约 0.4% 的电子是热活跃的。

**Application.** The $T$-linear electronic heat capacity (Module 4.1) and the Fermi surface structure (Module 4.5) are the direct experimental fingerprints of Fermi statistics. The Planck distribution underpins astrophysics (cosmic microwave background), photovoltaics, and the calibration of all thermal radiation detectors.

**应用。** 与 T 成正比的电子热容（模块 4.1）和费米面结构（模块 4.5）是费米统计的直接实验指纹。普朗克分布支撑着天体物理学（宇宙微波背景）、光伏技术以及所有热辐射探测器的标定。

---

## 2. Bose–Einstein Condensation and Lattice Heat Capacity · 玻色–爱因斯坦凝聚与晶格热容

**Definition.** For a gas of $N$ non-interacting bosons in 3D with a fixed number (e.g., $^{87}$Rb atoms), the chemical potential $\mu$ increases toward the ground-state energy $\varepsilon_0$ as $T$ decreases. At the **condensation temperature**

**定义。** 对于三维空间中 $N$ 个粒子数固定的非相互作用玻色子气体（例如 $^{87}$Rb 原子），化学势 $\mu$ 随温度降低而趋近基态能量 $\varepsilon_0$。在**凝聚温度**

$$ T_\text{BEC} = \frac{2\pi\hbar^2}{m k_B} \left(\frac{n}{\zeta(3/2)}\right)^{2/3}, $$

where $\zeta(3/2) \approx 2.612$, the normal states are saturated — they can hold no more bosons — and any additional particles macroscopically occupy the single ground state. Below $T_\text{BEC}$, the condensate fraction is

其中 $\zeta(3/2) \approx 2.612$，正常态饱和——不能再容纳更多玻色子——任何额外的粒子宏观地占据单一基态。在 $T_\text{BEC}$ 以下，凝聚体分数为

$$ N_0/N = 1 - (T/T_\text{BEC})^{3/2} \qquad \text{(uniform 3D gas)}. $$

The **Debye model** treats lattice vibrations (phonons) as a gas of bosons with $\mu = 0$ (like photons, phonons are not conserved). The key modification over the Einstein model is a realistic linear dispersion $\omega \propto k$ up to a cut-off frequency $\omega_D$ set by the condition that the total mode count equals $3N$ (three degrees of freedom per atom). The resulting heat capacity at low $T$ is the **Debye $T^3$ law**:

**德拜模型**将晶格振动（声子）视为 $\mu = 0$ 的玻色子气体（如同光子，声子不守恒）。相对于爱因斯坦模型的关键改进是采用实际的线性色散关系 $\omega \propto k$，直到截止频率 $\omega_D$，该截止频率由总模式数等于 $3N$（每个原子三个自由度）的条件确定。低温下的热容结果为**德拜 $T^3$ 定律**：

$$ C_\text{Debye} \approx \frac{12\pi^4}{5} N k_B (T/T_D)^3 \qquad (T \ll T_D), $$

where $T_D = \hbar\omega_D/k_B$ is the Debye temperature ($\sim 100$–$1000$ K for typical solids).

其中 $T_D = \hbar\omega_D/k_B$ 为德拜温度（典型固体约为 100–1000 K）。

**Demonstration.** At very low temperatures, the total heat capacity of a metal is

**演示。** 在极低温度下，金属的总热容为

$$ C(T) = \gamma T + \beta T^3, $$

where the first term is electronic (Fermi gas) and the second is phononic (Debye). Plotting $C/T$ vs $T^2$ gives a straight line with intercept $\gamma$ and slope $\beta$ — a standard cryogenic measurement that independently determines both the Fermi-level density of states and the Debye temperature. The Debye $T^3$ law arises because low-energy phonons obey Bose–Einstein statistics and their number scales as $T^3$, dominating at $T \ll T_D$.

其中第一项为电子贡献（费米气体），第二项为声子贡献（德拜）。画出 $C/T$ 与 $T^2$ 的关系图，得到截距为 $\gamma$、斜率为 $\beta$ 的直线——这是一种标准的低温测量，可独立确定费米能级态密度和德拜温度。德拜 $T^3$ 定律的出现是因为低能声子服从玻色–爱因斯坦统计，其数目随 $T^3$ 增长，在 $T \ll T_D$ 时占主导。

**Application.** These results directly feed into Module 4.1 (heat capacity of solids): the Debye model supersedes the classical Dulong–Petit value $C = 3 N k_B$ (correct only at high $T$ where every mode is classically active) and explains the observed fall-off at low temperatures. Module 4.3 (phonons) extends this to the full phonon dispersion and phonon–phonon interactions. Bose–Einstein condensation, first achieved with dilute alkali gases in 1995, has become a laboratory for quantum many-body physics, superfluidity, and precision measurement.

**应用。** 这些结果直接进入模块 4.1（固体热容）：德拜模型取代了经典的杜隆–珀蒂值 $C = 3 N k_B$（仅在高温下所有模式均经典激活时才正确），并解释了低温下观察到的热容下降。模块 4.3（声子）将此推广到完整声子色散和声子–声子相互作用。玻色–爱因斯坦凝聚于 1995 年首次在稀薄碱金属气体中实现，已成为研究量子多体物理、超流性和精密测量的实验室。

## Key results · 核心结果

- Degenerate Fermi gas $C_\text{el}=\tfrac{\pi^2}{2}Nk_B\,\dfrac{k_BT}{E_F}\propto T$ · 简并费米气体热容
- Planck $u(\nu,T)=\dfrac{8\pi h}{c^3}\dfrac{\nu^3}{e^{h\nu/k_BT}-1}$ · 普朗克分布
- BEC $T_\text{BEC}=\dfrac{2\pi\hbar^2}{mk_B}\big(\tfrac{n}{\zeta(3/2)}\big)^{2/3}$, $N_0/N=1-(T/T_\text{BEC})^{3/2}$ · 玻色–爱因斯坦凝聚
- Debye $C\propto T^3$ at low $T$ · 德拜 $T^3$ 律

---

## Self-test (blank page) · 自测（空白页）

1. Sketch the Planck distribution $u(\nu, T)$ and identify where the Rayleigh–Jeans and Wien limits apply. What quantity does integrating $u$ over $\nu$ give?
2. Explain why the electronic heat capacity of a metal is $\propto T$ rather than constant, and estimate the ratio $C_\text{el} / C_\text{classical}$ for copper at 300 K (use $E_F \approx 7$ eV).
3. State the condition for Bose–Einstein condensation and explain physically why macroscopic ground-state occupation occurs below $T_\text{BEC}$.
4. How does the Debye model improve on the Einstein model for lattice heat capacity? What is the low-$T$ prediction, and which experimental measurement confirms it?

**自测（空白页）**

1. 画出普朗克分布 $u(\nu, T)$ 的草图，并指出瑞利–金斯极限和维恩极限分别适用于哪里。对 $u$ 关于 $\nu$ 积分给出什么量？
2. 解释为什么金属的电子热容 $\propto T$ 而非常数，并估算铜在 300 K 时的比值 $C_\text{el} / C_\text{classical}$（使用 $E_F \approx 7$ eV）。
3. 陈述玻色–爱因斯坦凝聚的条件，并从物理上解释为什么在 $T_\text{BEC}$ 以下会出现宏观的基态占据。
4. 德拜模型在晶格热容方面比爱因斯坦模型有何改进？低温预测是什么，哪种实验测量证实了它？

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** Rayleigh–Jeans ($h\nu\ll k_BT$, $u\propto\nu^2 T$) at low $\nu$; Wien (exponential cutoff) at high $\nu$. $\int u\,d\nu\propto T^4$ (Stefan–Boltzmann). · 两极限;积分给 $T^4$。
**2.** $C_\text{el}\propto T$ because only $\sim k_BT/E_F$ of electrons are active (Pauli). Cu at 300 K: $C_\text{el}/C_\text{class}\sim k_BT/E_F\sim0.026/7\approx0.004$. · 电子热容线性,Cu 约 0.4%。
**3.** BEC when the thermal de Broglie wavelength $\sim$ interparticle spacing ($n\lambda_T^3\sim1$); below $T_\text{BEC}$ the excited states saturate so the ground state is macroscopically occupied. · 凝聚条件与机制。
**4.** Debye includes the full acoustic spectrum ($\omega\propto k$) → $C\propto T^3$ at low $T$ (Einstein gives an exponential, wrong). Confirmed by low-$T$ heat-capacity data. · 德拜给 $T^3$,实验证实。

</details>

---

← Previous: [Module 2.5 — Quantum Statistics](./module-2.5-quantum-statistics.md) · [Phase 2 index](./README.md) · Next: [Module 2.7 — Kinetic Theory & Transport](./module-2.7-kinetic-theory-and-transport.md) →

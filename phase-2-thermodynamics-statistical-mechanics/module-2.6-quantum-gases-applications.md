# Module 2.6 — Quantum Gases & Applications
**模块 2.6 — 量子气体与应用**

> **Phase 2 — [Thermodynamics & Statistical Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 2 阶段 — 热力学与统计力学 · 格式：定义 → 演示 → 应用**

---

## 1. The Degenerate Fermi Gas and Black-Body Radiation · 简并费米气体与黑体辐射

**Definition.** A **quantum gas** is one where quantum statistics — not classical phase-space counting — determines the thermodynamic properties. Two limiting cases dominate applications:

**定义。** **量子气体**是指热力学性质由量子统计——而非经典相空间计数——决定的气体。两种极限情形在应用中占主导地位：

**Degenerate Fermi gas** (T ≪ T_F = E_F/k_B): electrons in a metal at room temperature satisfy k_BT ≪ E_F, so the Fermi–Dirac distribution is nearly a step function. The density of states in 3D is g(ε) ∝ ε^{1/2}, so the total energy and heat capacity follow from the Sommerfeld expansion (Module 2.5):

**简并费米气体**（T ≪ T_F = E_F/k_B）：室温下金属中的电子满足 k_BT ≪ E_F，故费米–狄拉克分布近似为阶跃函数。三维态密度为 g(ε) ∝ ε^{1/2}，故总能量和热容由索末菲展开（模块 2.5）得出：

C_el = (π²/2) N k_B (k_BT/E_F) ∝ T.

This linear-T electronic heat capacity is far below the classical equipartition value, explaining why the electron gas does not swamp the lattice contribution at low temperatures.

这个与 T 成正比的电子热容远低于经典能均分值，解释了为什么电子气在低温下不会淹没晶格的贡献。

**Black-body radiation** (photon gas): photons are massless spin-1 bosons with μ = 0 (photon number is not conserved). The mean occupation of a mode at frequency ν is the **Planck distribution**:

**黑体辐射**（光子气）：光子是质量为零的自旋-1 玻色子，μ = 0（光子数不守恒）。频率为 ν 的模式的平均占据数为**普朗克分布**：

n(ν) = 1 / (e^{hν/k_BT} − 1).

Summing over all modes in a cavity gives the spectral energy density

对腔体中所有模式求和给出谱能量密度

u(ν, T) = (8πh/c³) ν³ / (e^{hν/k_BT} − 1),

and integrating over ν gives the Stefan–Boltzmann law: total radiated power ∝ T⁴. The Rayleigh–Jeans law (classical equipartition) predicts u ∝ ν²T with no cut-off — the ultraviolet catastrophe — which Planck's quantized modes resolve.

对 ν 积分给出斯特藩–玻尔兹曼定律：总辐射功率 ∝ T⁴。瑞利–金斯定律（经典能均分）预测 u ∝ ν²T 且无截止——即紫外灾变——普朗克的量子化模式解决了这一问题。

**Demonstration.** The electronic heat capacity is extracted from total measured C(T) = γT + AT³ at low temperature: the linear term isolates C_el = γT with γ = (π²/3) k_B² g(E_F), directly measuring the density of states at the Fermi level. For copper, E_F ≈ 7 eV gives T_F ≈ 81 000 K, so at 300 K the ratio k_BT/E_F ≈ 0.004 — confirming deep degeneracy and explaining why only ∼ 0.4% of electrons are thermally active.

**演示。** 电子热容从低温总测量热容 C(T) = γT + AT³ 中提取：线性项分离出 C_el = γT，其中 γ = (π²/3) k_B² g(E_F)，直接测量费米能级处的态密度。对于铜，E_F ≈ 7 eV 给出 T_F ≈ 81 000 K，故在 300 K 时 k_BT/E_F ≈ 0.004——证实了深度简并，并解释了为什么只有约 0.4% 的电子是热活跃的。

**Application.** The T-linear electronic heat capacity (Module 4.1) and the Fermi surface structure (Module 4.5) are the direct experimental fingerprints of Fermi statistics. The Planck distribution underpins astrophysics (cosmic microwave background), photovoltaics, and the calibration of all thermal radiation detectors.

**应用。** 与 T 成正比的电子热容（模块 4.1）和费米面结构（模块 4.5）是费米统计的直接实验指纹。普朗克分布支撑着天体物理学（宇宙微波背景）、光伏技术以及所有热辐射探测器的标定。

---

## 2. Bose–Einstein Condensation and Lattice Heat Capacity · 玻色–爱因斯坦凝聚与晶格热容

**Definition.** For a gas of N non-interacting bosons in 3D with a fixed number (e.g., ⁸⁷Rb atoms), the chemical potential μ increases toward the ground-state energy ε_0 as T decreases. At the **condensation temperature**

**定义。** 对于三维空间中 N 个粒子数固定的非相互作用玻色子气体（例如 ⁸⁷Rb 原子），化学势 μ 随温度降低而趋近基态能量 ε_0。在**凝聚温度**

T_BEC = (2πℏ²/mk_B) (n / ζ(3/2))^{2/3},

where ζ(3/2) ≈ 2.612, the normal states are saturated — they can hold no more bosons — and any additional particles macroscopically occupy the single ground state. Below T_BEC, the condensate fraction is

其中 ζ(3/2) ≈ 2.612，正常态饱和——不能再容纳更多玻色子——任何额外的粒子宏观地占据单一基态。在 T_BEC 以下，凝聚体分数为

N_0/N = 1 − (T/T_BEC)³.

The **Debye model** treats lattice vibrations (phonons) as a gas of bosons with μ = 0 (like photons, phonons are not conserved). The key modification over the Einstein model is a realistic linear dispersion ω ∝ k up to a cut-off frequency ω_D set by the condition that the total mode count equals 3N (three degrees of freedom per atom). The resulting heat capacity at low T is the **Debye T³ law**:

**德拜模型**将晶格振动（声子）视为 μ = 0 的玻色子气体（如同光子，声子不守恒）。相对于爱因斯坦模型的关键改进是采用实际的线性色散关系 ω ∝ k，直到截止频率 ω_D，该截止频率由总模式数等于 3N（每个原子三个自由度）的条件确定。低温下的热容结果为**德拜 T³ 定律**：

C_Debye ≈ (12π⁴/5) N k_B (T/T_D)³     (T ≪ T_D),

where T_D = ℏω_D/k_B is the Debye temperature (∼ 100–1000 K for typical solids).

其中 T_D = ℏω_D/k_B 为德拜温度（典型固体约为 100–1000 K）。

**Demonstration.** At very low temperatures, the total heat capacity of a metal is

**演示。** 在极低温度下，金属的总热容为

C(T) = γT + βT³,

where the first term is electronic (Fermi gas) and the second is phononic (Debye). Plotting C/T vs T² gives a straight line with intercept γ and slope β — a standard cryogenic measurement that independently determines both the Fermi-level density of states and the Debye temperature. The Debye T³ law arises because low-energy phonons obey Bose–Einstein statistics and their number scales as T³, dominating at T ≪ T_D.

其中第一项为电子贡献（费米气体），第二项为声子贡献（德拜）。画出 C/T 与 T² 的关系图，得到截距为 γ、斜率为 β 的直线——这是一种标准的低温测量，可独立确定费米能级态密度和德拜温度。德拜 T³ 定律的出现是因为低能声子服从玻色–爱因斯坦统计，其数目随 T³ 增长，在 T ≪ T_D 时占主导。

**Application.** These results directly feed into Module 4.1 (heat capacity of solids): the Debye model supersedes the classical Dulong–Petit value C = 3Nk_B (correct only at high T where every mode is classically active) and explains the observed fall-off at low temperatures. Module 4.3 (phonons) extends this to the full phonon dispersion and phonon–phonon interactions. Bose–Einstein condensation, first achieved with dilute alkali gases in 1995, has become a laboratory for quantum many-body physics, superfluidity, and precision measurement.

**应用。** 这些结果直接进入模块 4.1（固体热容）：德拜模型取代了经典的杜隆–珀蒂值 C = 3Nk_B（仅在高温下所有模式均经典激活时才正确），并解释了低温下观察到的热容下降。模块 4.3（声子）将此推广到完整声子色散和声子–声子相互作用。玻色–爱因斯坦凝聚于 1995 年首次在稀薄碱金属气体中实现，已成为研究量子多体物理、超流性和精密测量的实验室。

---

## Self-test (blank page) · 自测（空白页）

1. Sketch the Planck distribution u(ν, T) and identify where the Rayleigh–Jeans and Wien limits apply. What quantity does integrating u over ν give?
2. Explain why the electronic heat capacity of a metal is ∝ T rather than constant, and estimate the ratio C_el / C_classical for copper at 300 K (use E_F ≈ 7 eV).
3. State the condition for Bose–Einstein condensation and explain physically why macroscopic ground-state occupation occurs below T_BEC.
4. How does the Debye model improve on the Einstein model for lattice heat capacity? What is the low-T prediction, and which experimental measurement confirms it?

**自测（空白页）**

1. 画出普朗克分布 u(ν, T) 的草图，并指出瑞利–金斯极限和维恩极限分别适用于哪里。对 u 关于 ν 积分给出什么量？
2. 解释为什么金属的电子热容 ∝ T 而非常数，并估算铜在 300 K 时的比值 C_el / C_classical（使用 E_F ≈ 7 eV）。
3. 陈述玻色–爱因斯坦凝聚的条件，并从物理上解释为什么在 T_BEC 以下会出现宏观的基态占据。
4. 德拜模型在晶格热容方面比爱因斯坦模型有何改进？低温预测是什么，哪种实验测量证实了它？

---

← Previous: [Module 2.5 — Quantum Statistics](./module-2.5-quantum-statistics.md) · [Phase 2 index](./README.md) · Next: [Module 2.7 — Kinetic Theory & Transport](./module-2.7-kinetic-theory-and-transport.md) →

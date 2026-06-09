# Module 4.10 — Landau Fermi-Liquid Theory
**模块 4.10 — 朗道费米液体理论**

> **Phase 4 — [Condensed Matter / Solid State](./README.md)** · Format: Definition → Demonstration → Application
> **第 4 阶段 — 凝聚态 / 固体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-4.10-landau-fermi-liquid-theory-derivations.md)

---

## 1. Quasiparticles & Adiabatic Continuity · 准粒子与绝热连续性

**Definition.** A **Fermi liquid** is the interacting analogue of the free Fermi gas (Module 2.5, 4.1): a system of fermions in which strong interactions do **not** destroy the qualitative picture of the non-interacting gas. Landau's central postulate is **adiabatic continuity** — if one imagines turning on the interactions slowly (adiabatically) starting from the free Fermi gas, each free-particle eigenstate evolves smoothly into an eigenstate of the interacting system. The image of a free electron of momentum **k** becomes a **quasiparticle**: a dressed excitation carrying the same charge, spin, and momentum label **k**, but with a renormalized energy and an enhanced effective mass m*. The ground state still has a **sharp Fermi surface** at the same k_F.

**定义。** **费米液体**是自由费米气体（模块 2.5、4.1）的相互作用类比：一个强相互作用并**不**破坏无相互作用气体定性图像的费米子系统。朗道的核心假设是**绝热连续性**——若设想从自由费米气体出发缓慢（绝热地）开启相互作用，每个自由粒子本征态将平滑演化为相互作用系统的本征态。动量 **k** 的自由电子的对应物成为**准粒子**：携带相同电荷、自旋和动量标记 **k** 的"穿衣"激发，但能量重整化、有效质量增大为 m*。基态在同一 k_F 处仍有一个**锐利的费米面**。

**Demonstration — Luttinger's theorem.** Because the adiabatic mapping is one-to-one and preserves the quantum numbers and the count of occupied states, the **volume enclosed by the Fermi surface is unchanged** by interactions (**Luttinger's theorem**):

  V_FS = (2π)³ n / g_s   (g_s = spin degeneracy),

i.e. the same k_F as the free gas at density n. Interactions deform the *shape* and renormalize the *energy* of the Fermi surface, but never its enclosed volume. This is what makes the free-gas results of Module 4.1 (and the Fermi-surface concept of Module 4.5) survive into the interacting world.

**演示——拉廷格定理。** 由于绝热映射是一一对应且保持量子数与占据态计数，相互作用使**费米面所围的体积保持不变**（**拉廷格定理**）：

  V_FS = (2π)³ n / g_s   （g_s = 自旋简并度），

即与密度 n 下自由气体相同的 k_F。相互作用使费米面的*形状*变形、能量*重整化*，但绝不改变其所围体积。正是这一点使模块 4.1 的自由气体结果（以及模块 4.5 的费米面概念）在相互作用世界中得以保留。

**Application — Quasiparticle lifetime and why the picture works.** A quasiparticle is only useful if it is long-lived. A quasiparticle at energy ε above the Fermi sea decays by scattering off another fermion, creating a particle–hole pair. Pauli blocking restricts both the available initial occupied states and the available final empty states to a thin shell of width (ε − ε_F) around E_F; phase-space counting then gives a decay rate (see Derivations A)

  1/τ ∝ (ε − ε_F)²   (or, at finite temperature, 1/τ ∝ (k_B T)²).

The crucial consequence: the level width ℏ/τ ∝ (ε − ε_F)² vanishes **faster** than the excitation energy (ε − ε_F) itself as ε → ε_F, so

  (width)/(energy) ∝ (ε − ε_F) → 0.

Quasiparticles near the Fermi surface are therefore arbitrarily well-defined — sharp poles in the single-particle Green's function with weight Z (Module 6.2) — which is precisely why the whole construction is self-consistent.

**应用——准粒子寿命及该图像为何成立。** 准粒子只有长寿命才有用。费米海上方能量 ε 处的准粒子通过与另一费米子散射、产生一个粒子–空穴对而衰变。泡利阻塞将可用的初始占据态与最终空态都限制在 E_F 周围宽度为 (ε − ε_F) 的薄壳内；相空间计数由此给出衰变率（见推导 A）

  1/τ ∝ (ε − ε_F)²   （或在有限温度下，1/τ ∝ (k_B T)²）。

关键结论：能级宽度 ℏ/τ ∝ (ε − ε_F)² 在 ε → ε_F 时比激发能 (ε − ε_F) 本身衰减得**更快**，故

  （宽度）/（能量）∝ (ε − ε_F) → 0。

因此费米面附近的准粒子任意良好定义——单粒子格林函数中权重为 Z 的锐利极点（模块 6.2）——这正是整个构造自洽的原因。

---

## 2. The Landau Energy Functional & Effective Mass · 朗道能量泛函与有效质量

**Definition — Energy functional and the f-function.** The total energy is not a sum of independent quasiparticle energies; quasiparticles interact. Landau writes the energy as a **functional** of the quasiparticle distribution deviation δn_k = n_k − n_k⁰ (the change relative to the ground-state occupation):

  E = E₀ + Σ_k ε_k⁰ δn_k + (1/2V) Σ_{k k'} f_{k k'} δn_k δn_{k'} + …

The first correction is the bare quasiparticle energy ε_k⁰; the quadratic term encodes the **interaction between quasiparticles** through the **Landau f-function** f_{k k'}. Including spin, decompose into spin-symmetric and spin-antisymmetric parts:

  f_{k k', σσ'} = f^s_{k k'} + f^a_{k k'} **σ**·**σ'**.

Because only quasiparticles on the Fermi surface matter, take |**k**| = |**k'**| = k_F and let θ be the angle between them; expand in Legendre polynomials and define the **dimensionless Landau parameters**:

  f^{s,a}(θ) = Σ_l f_l^{s,a} P_l(cos θ),   **F_l^{s,a} = N(0) f_l^{s,a}**,

where N(0) is the density of states at E_F (per spin, summed over spins as appropriate). The dimensionless F_l^{s,a} are the experimentally meaningful parameters.

**定义——能量泛函与 f 函数。** 总能量并非各独立准粒子能量之和；准粒子之间相互作用。朗道将能量写为准粒子分布偏离 δn_k = n_k − n_k⁰（相对于基态占据的变化）的**泛函**：

  E = E₀ + Σ_k ε_k⁰ δn_k + (1/2V) Σ_{k k'} f_{k k'} δn_k δn_{k'} + …

第一项修正是裸准粒子能量 ε_k⁰；二次项通过**朗道 f 函数** f_{k k'} 编码了**准粒子之间的相互作用**。计入自旋后，分解为自旋对称与自旋反对称部分：

  f_{k k', σσ'} = f^s_{k k'} + f^a_{k k'} **σ**·**σ'**。

由于只有费米面上的准粒子重要，取 |**k**| = |**k'**| = k_F，令 θ 为二者夹角；用勒让德多项式展开并定义**无量纲朗道参数**：

  f^{s,a}(θ) = Σ_l f_l^{s,a} P_l(cos θ)，**F_l^{s,a} = N(0) f_l^{s,a}**，

其中 N(0) 是 E_F 处的态密度。无量纲的 F_l^{s,a} 是具有实验意义的参数。

**Demonstration — Effective mass from Galilean invariance.** When a quasiparticle of momentum **k** is added, it drags a **backflow** of the surrounding medium through the f-function, so its true momentum current differs from its group velocity. **Galilean invariance** demands that the total momentum of a quasiparticle equal the bare value m**v** (the f-interaction cannot change the total momentum of a closed system). Imposing this self-consistency (see Derivations C) yields the celebrated relation

  **m*/m = 1 + F_1^s/3.**

Only the l = 1 symmetric channel renormalizes the mass, because the effective mass couples to the current (a vector, l = 1) and the spin-symmetric channel.

**演示——伽利略不变性给出有效质量。** 当加入动量 **k** 的准粒子时，它通过 f 函数拖曳出周围介质的**回流**，故其真实动量流不同于其群速度。**伽利略不变性**要求准粒子总动量等于裸值 m**v**（f 相互作用不能改变封闭系统的总动量）。施加这一自洽条件（见推导 C）给出著名关系

  **m*/m = 1 + F_1^s/3。**

只有 l = 1 的对称通道重整化质量，因为有效质量耦合于电流（一个矢量，l = 1）和自旋对称通道。

---

## 3. Thermodynamic Renormalizations & Collective Modes · 热力学重整化与集体模式

**Application — Thermodynamics.** Because the low-energy density of states is set by the effective mass, define the renormalized DOS N*(0) = (m*/m) N(0). The measurable thermodynamic responses are then enhanced (or suppressed) by the Landau parameters:

- **Specific heat.** The linear-in-T Sommerfeld coefficient (Module 4.1) is renormalized purely by the effective mass:

  **C_V = (m*/m) C_V^{free}**,   γ = (m*/m) γ_free.

  The f-interaction does not appear here because at fixed entropy the quasiparticle counting is identical to the free gas; only the DOS at E_F changes. Heavy-fermion compounds (m*/m ~ 100–1000) show enormously enhanced γ.

- **Compressibility.** κ ∝ N*(0) / (1 + F_0^s). The l = 0 symmetric channel stiffens (F_0^s > 0) or softens the response to a uniform density change.

- **Spin susceptibility.** The Pauli susceptibility (Module 4.1) becomes

  **χ ∝ N*(0) / (1 + F_0^a)**   (Stoner-like enhancement).

  The denominator 1 + F_0^a is the Fermi-liquid analogue of the Stoner factor: as F_0^a → −1⁺ the susceptibility diverges, signalling the **ferromagnetic (Stoner) instability** — the Fermi liquid is about to spontaneously spin-polarize (connecting to Module 4.6).

**应用——热力学。** 由于低能态密度由有效质量决定，定义重整化态密度 N*(0) = (m*/m) N(0)。可测的热力学响应于是被朗道参数增强（或抑制）：

- **比热。** 线性温度依赖的索末菲系数（模块 4.1）纯由有效质量重整化：

  **C_V = (m*/m) C_V^{free}**，γ = (m*/m) γ_free。

  f 相互作用在此不出现，因为在固定熵下准粒子计数与自由气体相同；只有 E_F 处的态密度改变。重费米子化合物（m*/m ~ 100–1000）表现出极大增强的 γ。

- **压缩率。** κ ∝ N*(0) / (1 + F_0^s)。l = 0 对称通道使对均匀密度变化的响应变硬（F_0^s > 0）或变软。

- **自旋磁化率。** 泡利磁化率（模块 4.1）变为

  **χ ∝ N*(0) / (1 + F_0^a)**   （斯通纳型增强）。

  分母 1 + F_0^a 是斯通纳因子的费米液体类比：当 F_0^a → −1⁺ 时磁化率发散，标志**铁磁（斯通纳）不稳定性**——费米液体即将自发自旋极化（连接模块 4.6）。

**Application — Zero sound and the breakdown of Fermi-liquid theory.** The quasiparticle distribution obeys the **Landau kinetic (Boltzmann) equation**, whose collisionless (collective) solutions are propagating modes. Two distinct regimes appear:

- **First sound** (collisional, hydrodynamic, ωτ ≪ 1): an ordinary density-pressure wave, requiring local equilibrium maintained by collisions.
- **Zero sound** (collisionless, ωτ ≫ 1): a **collective mode** of the Fermi surface itself, sustained not by collisions but by the f-interaction. Writing the dimensionless phase velocity s = ω/(q v_F), the simplest (F_0^s only) dispersion condition is

  (s/2) ln[(s+1)/(s−1)] − 1 = 1/F_0^s,

which admits an undamped solution with s > 1 (a velocity slightly above v_F) for F_0^s > 0. Zero sound is the high-frequency analogue of first sound; the two have *different* speeds, and the crossover between them as ωτ passes through 1 is a direct experimental fingerprint of Fermi-liquid behaviour (seen in liquid ³He).

**Breakdown.** Fermi-liquid theory fails when quasiparticles are no longer well-defined: in **one dimension** interactions destroy the quasiparticle pole entirely and the system becomes a **Luttinger liquid** (spin–charge separation, no sharp Fermi-surface step); near a **quantum critical point** the (ε − ε_F)² lifetime law is violated and one finds non-Fermi-liquid (e.g. "strange metal") behaviour. The Fermi liquid is also the **normal state** out of which BCS superconductivity (Phase 5) pairs.

**应用——零声与费米液体理论的失效。** 准粒子分布服从**朗道动理学（玻尔兹曼）方程**，其无碰撞（集体）解是传播模式。出现两个截然不同的区域：

- **第一声**（碰撞型、流体力学型，ωτ ≪ 1）：普通的密度–压强波，需要碰撞维持局域平衡。
- **零声**（无碰撞型，ωτ ≫ 1）：费米面本身的**集体模式**，不靠碰撞而靠 f 相互作用维持。记无量纲相速度 s = ω/(q v_F)，最简单的（仅 F_0^s）色散条件为

  (s/2) ln[(s+1)/(s−1)] − 1 = 1/F_0^s，

当 F_0^s > 0 时存在 s > 1（速度略高于 v_F）的无阻尼解。零声是第一声的高频类比；二者速度*不同*，且当 ωτ 越过 1 时二者之间的交叉是费米液体行为的直接实验指纹（见于液态 ³He）。

**失效。** 当准粒子不再良好定义时，费米液体理论失效：在**一维**中相互作用彻底破坏准粒子极点，系统成为**拉廷格液体**（自旋–电荷分离，无锐利费米面台阶）；在**量子临界点**附近，(ε − ε_F)² 寿命定律被违反，出现非费米液体（如"奇异金属"）行为。费米液体也是 BCS 超导（第 5 阶段）配对所源出的**正常态**。

---

**Self-test (blank page)**

1. State the principle of adiabatic continuity and explain what a quasiparticle is. What is Luttinger's theorem, and why does it matter?
2. Derive (by phase-space counting) why the quasiparticle decay rate scales as 1/τ ∝ (ε − ε_F)², and explain why this guarantees well-defined quasiparticles near the Fermi surface.
3. Write the Landau energy functional and define the Landau parameters F_l^{s,a}. Why does one expand on the Fermi surface in Legendre polynomials?
4. State the effective-mass relation m*/m = 1 + F_1^s/3 and explain the physical role of Galilean invariance and backflow in deriving it.

**自测（空白页）**

1. 陈述绝热连续性原理并解释何为准粒子。拉廷格定理是什么，为何重要？
2. （用相空间计数）推导准粒子衰变率为何标度为 1/τ ∝ (ε − ε_F)²，并解释为何这保证了费米面附近准粒子良好定义。
3. 写出朗道能量泛函并定义朗道参数 F_l^{s,a}。为何要在费米面上用勒让德多项式展开？
4. 陈述有效质量关系 m*/m = 1 + F_1^s/3，并解释伽利略不变性与回流在推导中的物理作用。

5. How are C_V, χ, and κ renormalized in a Fermi liquid? What does F_0^a → −1 signal physically?
6. Contrast zero sound with first sound (regime, mechanism, speed). When does Fermi-liquid theory break down?
7. Why is the specific heat renormalized only by m*/m and not by the f-interaction directly, whereas χ involves F_0^a?
8. Sketch the relation between the Fermi liquid, the Green's-function quasiparticle pole weight Z (Module 6.2), and the BCS normal state (Phase 5).

5. 费米液体中 C_V、χ、κ 如何重整化？F_0^a → −1 在物理上标志什么？
6. 对比零声与第一声（区域、机制、速度）。费米液体理论何时失效？
7. 为何比热只被 m*/m 重整化而非直接被 f 相互作用重整化，而 χ 却涉及 F_0^a？
8. 勾画费米液体、格林函数准粒子极点权重 Z（模块 6.2）与 BCS 正常态（第 5 阶段）之间的关系。

---

← Previous: [Module 4.9 — Topological Matter & Berry Phase](./module-4.9-topological-matter-and-berry-phase.md) · [Phase 4 index](./README.md) · Next: [Module 4.11 — Linear Response & Transport](./module-4.11-linear-response-and-transport.md) →

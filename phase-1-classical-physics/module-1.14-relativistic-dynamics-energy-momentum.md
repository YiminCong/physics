# Module 1.14 — Relativistic Dynamics & E = mc² ⭐
**模块 1.14 — 相对论动力学与 E = mc² ⭐**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**

---

## 1. Four-Vectors and Relativistic Momentum · 四矢量与相对论动量

**Definition.** A **four-vector** is a set of four quantities that transforms under a Lorentz boost exactly like (ct, x, y, z). The **proper time** τ is the Lorentz-invariant time measured by a co-moving clock, related to coordinate time by dτ = dt/γ. The **four-velocity** is U^μ = dx^μ/dτ = γ(c, v), with U^μ U_μ = c² (constant). The **four-momentum** is:

**定义。** **四矢量**是在洛伦兹变换下与 (ct, x, y, z) 完全相同变换的四个量的集合。**固有时** τ 是由共动时钟测量的洛伦兹不变时间，与坐标时的关系为 dτ = dt/γ。**四速度**为 U^μ = dx^μ/dτ = γ(c, v)，满足 U^μ U_μ = c²（常数）。**四动量**为：

p^μ = m U^μ = (E/c, p_x, p_y, p_z),

where m is the **rest mass** (Lorentz scalar), the spatial part is the relativistic momentum p = γmv, and the time component gives the **relativistic energy** E = γmc². The invariant magnitude is:

其中 m 为**静止质量**（洛伦兹标量），空间部分为相对论动量 p = γmv，时间分量给出**相对论能量** E = γmc²。不变模长为：

p^μ p_μ = (E/c)² − |p|² = (mc)²,

or equivalently **E² = (pc)² + (mc²)²**. For a photon m = 0, so E = pc = hν (with the quantum relation, Module 3.1).

或等价地 **E² = (pc)² + (mc²)²**。对于光子 m = 0，故 E = pc = hν（配合量子关系，模块 3.1）。

**Demonstration.** Low-velocity limit: E = γmc² = mc² + ½mv² + O(v⁴/c²). The first term is the **rest energy** E₀ = mc², the second is the familiar kinetic energy. At v = 0 the energy is not zero but mc² — a prediction with no classical counterpart. For an ultra-relativistic particle (v → c, pc ≫ mc²), E ≈ pc: the particle behaves like a massless particle.

**演示。** 低速极限：E = γmc² = mc² + ½mv² + O(v⁴/c²)。第一项是**静止能量** E₀ = mc²，第二项是熟悉的动能。在 v = 0 时能量不为零，而是 mc²——这是经典力学没有对应的预言。对于超相对论粒子（v → c，pc ≫ mc²），E ≈ pc：粒子表现得像无质量粒子。

**Application.** Mass–energy equivalence E = mc² quantifies the energy released in nuclear reactions and particle–antiparticle annihilation. In fission of ²³⁵U, roughly 0.1% of rest mass converts to energy — the basis of nuclear power. The four-momentum is the fundamental kinematic quantity in all of particle physics (Phase 8): invariant mass m² = (Σ p_i)² / c² identifies particles, and four-momentum conservation (replacing the separate non-relativistic conservation laws for mass, momentum, and energy) constrains every scattering and decay process.

**应用。** 质能等价 E = mc² 量化了核反应和粒子–反粒子湮灭中释放的能量。在 ²³⁵U 裂变中，约 0.1% 的静止质量转化为能量——核能的基础。四动量是所有粒子物理（第 8 阶段）中基本的运动学量：不变质量 m² = (Σ p_i)² / c² 鉴别粒子，四动量守恒（取代非相对论的质量、动量、能量三个独立守恒定律）约束每个散射和衰变过程。

## 2. Relativistic Dynamics and Force · 相对论动力学与力

**Definition.** The relativistic equation of motion is **f^μ = dp^μ/dτ**, where f^μ is the **four-force**. The spatial part gives dp/dt = F (three-force), with p = γmv; the time component gives dE/dt = F · v (power). For a particle in an electromagnetic field, the four-force is f^μ = q F^{μν} U_ν (the Lorentz force in covariant form, linking to Module 1.15). Newton's three laws are recovered in the limit v ≪ c: F = dp/dt ≈ ma.

**定义。** 相对论运动方程为 **f^μ = dp^μ/dτ**，其中 f^μ 是**四力**。空间部分给出 dp/dt = F（三维力），p = γmv；时间分量给出 dE/dt = F · v（功率）。对于电磁场中的粒子，四力为 f^μ = q F^{μν} U_ν（协变形式的洛伦兹力，与模块 1.15 相联系）。在 v ≪ c 极限下恢复牛顿三定律：F = dp/dt ≈ ma。

**Demonstration.** A particle accelerated from rest through potential difference V gains kinetic energy K = qV = (γ − 1)mc². For an electron (mc² = 0.511 MeV) accelerated through V = 1 MV, γ = 1 + 1/0.511 ≈ 2.96, v/c = √(1 − 1/γ²) ≈ 0.94c. Non-relativistic treatment would give v/c ≈ 1.98 — faster than light, which is impossible. Relativistic treatment is mandatory.

**演示。** 粒子从静止通过电位差 V 加速，获得动能 K = qV = (γ − 1)mc²。对于通过 V = 1 MV 加速的电子（mc² = 0.511 MeV），γ = 1 + 1/0.511 ≈ 2.96，v/c = √(1 − 1/γ²) ≈ 0.94c。非相对论处理给出 v/c ≈ 1.98——超过光速，这是不可能的。相对论处理是必须的。

**Application.** Relativistic kinematics underpins every calculation in high-energy physics. The threshold energy for particle production (e.g. e⁺e⁻ → μ⁺μ⁻ requires E_cm ≥ 2m_μ c²), invariant mass reconstruction of short-lived particles, and the kinematics of particle decays all use E² = (pc)² + (mc²)² and four-momentum conservation. The Lorentz-covariant formulation connects directly to quantum field theory (Phase 6) and the Standard Model (Phase 8).

**应用。** 相对论运动学支撑着高能物理中的每一个计算。粒子产生的阈能（例如 e⁺e⁻ → μ⁺μ⁻ 要求 E_cm ≥ 2m_μ c²）、短寿命粒子的不变质量重建以及粒子衰变运动学，都使用 E² = (pc)² + (mc²)² 和四动量守恒。洛伦兹协变形式直接连接到量子场论（第 6 阶段）和标准模型（第 8 阶段）。

---

**Self-test (blank page)**

1. Show that the four-momentum p^μ p_μ = m²c² is Lorentz-invariant, and derive E² = (pc)² + (mc²)² from this relation.
2. A pion (m = 135 MeV/c²) at rest decays to two photons. Using four-momentum conservation, find the energy and momentum of each photon in the pion rest frame.
3. An electron is accelerated from rest through 2 MV. Find its final γ, speed v/c, and kinetic energy. Compare the relativistic and non-relativistic results.
4. Explain why "F = ma" must be modified in special relativity. Write the correct relativistic equation of motion and recover Newton's law in the non-relativistic limit.

**自测（空白页）**

1. 证明四动量 p^μ p_μ = m²c² 是洛伦兹不变的，并由此推导 E² = (pc)² + (mc²)²。
2. 静止的 π 介子（m = 135 MeV/c²）衰变为两个光子。利用四动量守恒，求 π 介子静止系中每个光子的能量和动量。
3. 电子从静止通过 2 MV 加速。求其末态 γ、速度 v/c 和动能。比较相对论结果与非相对论结果。
4. 解释为什么"F = ma"在狭义相对论中必须修改。写出正确的相对论运动方程，并在非相对论极限下恢复牛顿定律。

---

← Previous: [Module 1.13 — Special Relativity — Kinematics](./module-1.13-special-relativity-kinematics.md) · [Phase 1 index](./README.md) · Next: [Module 1.15 — Covariant Electromagnetism](./module-1.15-covariant-electromagnetism.md) →

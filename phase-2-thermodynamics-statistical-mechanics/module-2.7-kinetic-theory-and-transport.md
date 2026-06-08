# Module 2.7 — Kinetic Theory & Transport
**模块 2.7 — 动理论与输运**

> **Phase 2 — [Thermodynamics & Statistical Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 2 阶段 — 热力学与统计力学 · 格式：定义 → 演示 → 应用**

---

## 1. The Maxwell–Boltzmann Distribution & Mean Free Path · 麦克斯韦–玻尔兹曼分布与平均自由程

**Definition.** Kinetic theory derives the macroscopic properties of a gas from the statistics of its molecules. In equilibrium, molecular speeds follow the **Maxwell–Boltzmann distribution** f(v) ∝ v² e^{−mv²/2k_BT} (the Boltzmann factor of Module 2.4 applied to kinetic energy). The **mean free path** ℓ = 1/(√2 n σ) is the average distance between collisions (n = number density, σ = collision cross-section).

**定义。** 动理论从分子的统计出发推导气体的宏观性质。在平衡态，分子速率服从**麦克斯韦–玻尔兹曼分布** f(v) ∝ v² e^{−mv²/2k_BT}（模块 2.4 的玻尔兹曼因子应用于动能）。**平均自由程** ℓ = 1/(√2 n σ) 是碰撞之间的平均距离（n = 数密度，σ = 碰撞截面）。

**Demonstration.** Averaging molecular momentum transfer to the walls reproduces the **ideal gas law** PV = N k_BT and identifies temperature with mean kinetic energy: ½m⟨v²⟩ = (3/2)k_BT. The rms speed is v_rms = √(3k_BT/m) — hundreds of m/s for air at room temperature.

**演示。** 对分子向壁面传递的动量取平均，可重现**理想气体定律** PV = N k_BT，并将温度与平均动能联系起来：½m⟨v²⟩ = (3/2)k_BT。均方根速率为 v_rms = √(3k_BT/m)——室温下空气分子约为数百 m/s。

**Application.** Kinetic theory is the microscopic justification of thermodynamics for dilute gases, and it fixes the equipartition result C_V = (3/2)Nk_B for a monatomic gas (Module 2.4).

**应用。** 动理论是稀薄气体热力学的微观理论基础，并确定了单原子气体的能均分结果 C_V = (3/2)Nk_B（模块 2.4）。

## 2. The Boltzmann Equation & Transport Coefficients · 玻尔兹曼方程与输运系数

**Definition.** Out of equilibrium, the distribution f(r,v,t) evolves by the **Boltzmann transport equation** ∂f/∂t + **v**·∇_r f + **F**/m·∇_v f = (∂f/∂t)_coll. In the **relaxation-time approximation** the collision term is −(f − f₀)/τ, which linearizes the problem and yields the **transport coefficients**.

**定义。** 偏离平衡态时，分布函数 f(r,v,t) 遵循**玻尔兹曼输运方程** ∂f/∂t + **v**·∇_r f + **F**/m·∇_v f = (∂f/∂t)_coll。在**弛豫时间近似**中，碰撞项为 −(f − f₀)/τ，使问题线性化并给出**输运系数**。

**Demonstration.** A gradient drives a flux proportional to it: **diffusion** (Fick's law, flux ∝ −∇n), **viscosity** (momentum transport, giving the η of Navier–Stokes, Module 1.17), and **thermal conductivity** (heat flux ∝ −∇T). Each coefficient comes out ∝ n v̄ ℓ ∝ √T for a classical gas. Applied to the electron gas in a metal with a relaxation time τ, the same logic gives the **Drude conductivity** σ = ne²τ/m and Ohm's law (Module 4.1).

**演示。** 梯度驱动与之成正比的通量：**扩散**（菲克定律，通量 ∝ −∇n）、**粘度**（动量输运，给出纳维–斯托克斯方程中的 η，模块 1.17）以及**热导率**（热流 ∝ −∇T）。对于经典气体，每个系数均正比于 n v̄ ℓ ∝ √T。将同样的逻辑应用于弛豫时间为 τ 的金属电子气，得到**德鲁德电导率** σ = ne²τ/m 和欧姆定律（模块 4.1）。

**Application.** Transport theory connects equilibrium statistical mechanics to the *dynamics* of real materials — electrical and thermal conductivity, diffusion, and viscosity. The Boltzmann equation remains the workhorse for electron and phonon transport in solids (Phase 4) and for plasmas, and it supplies the dissipative coefficients that the macroscopic Navier–Stokes equation (Module 1.17) takes as inputs.

**应用。** 输运理论将平衡态统计力学与真实材料的*动力学*联系起来——包括电导率、热导率、扩散和粘度。玻尔兹曼方程至今仍是固体中电子和声子输运（第 4 阶段）以及等离子体研究的主要工具，它还提供宏观纳维–斯托克斯方程（模块 1.17）所需的耗散系数。

---

**Self-test (blank page)**

1. Sketch the Maxwell–Boltzmann speed distribution and mark v_rms; explain how it shifts as T increases.
2. Derive PV = N k_BT by computing the momentum flux of molecules onto a wall.
3. Define the mean free path and explain how it enters the transport coefficients.
4. Starting from the relaxation-time Boltzmann equation, sketch how the Drude conductivity σ = ne²τ/m arises.

**自测（空白页）**

1. 画出麦克斯韦–玻尔兹曼速率分布草图并标出 v_rms；解释随 T 增大分布如何移动。
2. 通过计算分子对壁面的动量通量推导 PV = N k_BT。
3. 定义平均自由程，并解释它如何进入输运系数。
4. 从弛豫时间玻尔兹曼方程出发，概述德鲁德电导率 σ = ne²τ/m 是如何得出的。

---

← Previous: [Module 2.6 — Quantum Gases & Applications](./module-2.6-quantum-gases-applications.md) · [Phase 2 index](./README.md) · Next: [Module 2.8 — Brownian Motion & the Einstein Relation](./module-2.8-brownian-motion-and-the-einstein-relation.md) →

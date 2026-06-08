# Module 1.9 — Magnetostatics
**模块 1.9 — 静磁学**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.9-magnetostatics-derivations.md)

---

## 1. Biot–Savart Law, Ampère's Law, and the Vector Potential · 毕奥–萨伐尔定律、安培定律与矢量势

**Definition.** A steady current density J(r) produces a magnetic field B(r) given by the **Biot–Savart law**:

**定义。** 稳恒电流密度 J(r) 产生由**毕奥–萨伐尔定律**给出的磁场 B(r)：

B(r) = (μ₀/4π) ∫ J(r′) × (r − r′) / |r − r′|³ dV′.

The static Maxwell equations for B are:

B 的静磁麦克斯韦方程为：

∇ · B = 0   (no magnetic monopoles),
∇ × B = μ₀ J   (Ampère's law, static).

Because ∇ · B = 0, one can always write **B = ∇ × A**, where A is the **magnetic vector potential**. A is not unique — the gauge transformation A → A + ∇χ leaves B unchanged. In the **Coulomb gauge** ∇ · A = 0, Ampère's law reduces to ∇²A = −μ₀ J, a vector Poisson equation solved by the same Green's function as electrostatics.

由于 ∇ · B = 0，总可以写成 **B = ∇ × A**，其中 A 是**磁矢量势**。A 不是唯一的——规范变换 A → A + ∇χ 不改变 B。在**库仑规范** ∇ · A = 0 下，安培定律化为 ∇²A = −μ₀ J，这是一个用与静电学相同的格林函数求解的矢量泊松方程。

**Demonstration.** For an infinite straight wire carrying current I along the z-axis, Ampère's law applied to a circular loop of radius r gives B = μ₀ I / (2πr) φ̂. The same calculation in integral form demonstrates the power of symmetry: the field is tangential and constant on the loop, making the line integral trivial.

**演示。** 对于沿 z 轴流过电流 I 的无限长直导线，将安培定律应用于半径为 r 的圆形回路，得 B = μ₀ I / (2πr) φ̂。用积分形式进行同样的计算展示了对称性的力量：场在回路上是切向且恒定的，使线积分变得简单。

**Application.** The vector potential A is not merely a mathematical convenience — in quantum mechanics it enters the Hamiltonian directly as (p − qA)²/2m (the minimal coupling prescription), and the Aharonov–Bohm effect shows that A has physical consequences even where B = 0. This gauge freedom is the classical seed of gauge field theory (Phase 8). The magnetic dipole moment m = ½ ∫ r × J dV appears in NMR, magnetism, and the interaction of particles with external fields.

**应用。** 矢量势 A 不仅仅是数学上的便利——在量子力学中它直接以 (p − qA)²/2m 进入哈密顿量（最小耦合方案），阿哈罗诺夫–玻姆效应表明即使在 B = 0 处 A 也有物理后果。这种规范自由度是规范场论（第 8 阶段）的经典萌芽。磁偶极矩 m = ½ ∫ r × J dV 出现在核磁共振、磁学以及粒子与外场的相互作用中。

## 2. Magnetic Dipoles and Magnetic Materials · 磁偶极子与磁性材料

**Definition.** A small current loop of area a carrying current I has a **magnetic dipole moment** m = I a n̂. At large distances r ≫ loop size, the field is a magnetic dipole: B_dip = (μ₀/4π r³)(2m cos θ r̂ + m sin θ θ̂). The energy of a dipole in an external field is U = −m · B, and the torque is τ = m × B. For a magnetic medium, the macroscopic fields H and B are related by B = μ₀(H + M), where M is the magnetisation density.

**定义。** 面积为 a、载流 I 的小电流环具有**磁偶极矩** m = I a n̂。在远处（r ≫ 环尺寸），场为磁偶极子：B_dip = (μ₀/4π r³)(2m cos θ r̂ + m sin θ θ̂)。偶极子在外场中的能量为 U = −m · B，力矩为 τ = m × B。对于磁性介质，宏观场 H 和 B 通过 B = μ₀(H + M) 相联系，其中 M 为磁化密度。

**Demonstration.** A proton in a magnetic field B₀ ẑ has a magnetic moment m = γ_p L (where γ_p is the gyromagnetic ratio). In equilibrium it precesses about ẑ at the **Larmor frequency** ω_L = γ_p B₀. Driving with a transverse oscillating field at ω_L produces magnetic resonance — the basis of NMR and MRI.

**演示。** 磁场 B₀ ẑ 中的质子具有磁矩 m = γ_p L（其中 γ_p 为旋磁比）。在平衡时它以**拉莫尔频率** ω_L = γ_p B₀ 绕 ẑ 进动。以横向振荡场在 ω_L 处驱动产生磁共振——核磁共振和核磁共振成像的基础。

**Application.** Magnetostatics feeds directly into electrodynamics (Module 1.10): Faraday's law of induction is the time-varying generalisation of the static Biot–Savart/Ampère framework. The gauge structure of A prefigures the four-potential A^μ in covariant electromagnetism (Module 1.15) and QED (Phase 8).

**应用。** 静磁学直接进入电动力学（模块 1.10）：法拉第电磁感应定律是静态毕奥–萨伐尔/安培框架的时变推广。A 的规范结构预示了协变电磁学（模块 1.15）和量子电动力学（第 8 阶段）中的四矢量势 A^μ。

---

**Self-test (blank page)**

1. Use Ampère's law to find B inside and outside a long solenoid of n turns per unit length carrying current I.
2. Define the magnetic vector potential A. Show that the gauge transformation A → A + ∇χ leaves B unchanged. What is the Coulomb gauge condition?
3. A circular loop of radius R carries current I. Find the magnetic field on the axis at distance z from the centre using the Biot–Savart law.
4. What is the Aharonov–Bohm effect, and why does it demonstrate that A (not just B) is physically meaningful in quantum mechanics?

**自测（空白页）**

1. 用安培定律求每单位长度 n 匝、载流 I 的长螺线管内外的 B。
2. 定义磁矢量势 A。证明规范变换 A → A + ∇χ 不改变 B。库仑规范条件是什么？
3. 半径为 R 的圆形线圈载流 I。用毕奥–萨伐尔定律求轴线上距中心 z 处的磁场。
4. 阿哈罗诺夫–玻姆效应是什么？它为什么证明了 A（而不仅仅是 B）在量子力学中具有物理意义？

---

← Previous: [Module 1.8 — Electrostatics & Boundary-Value Problems](./module-1.8-electrostatics-boundary-value-problems.md) · [Phase 1 index](./README.md) · Next: [Module 1.10 — Electrodynamics & Maxwell's Equations](./module-1.10-electrodynamics-maxwell-equations.md) →

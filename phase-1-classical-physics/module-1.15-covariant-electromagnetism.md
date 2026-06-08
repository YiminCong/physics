# Module 1.15 — Covariant Electromagnetism
**模块 1.15 — 协变电磁学**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.15-covariant-electromagnetism-derivations.md)

---

## 1. The Four-Potential and the Field Tensor · 四矢量势与场张量

**Definition.** The scalar potential φ and vector potential A (Module 1.10) combine into the **four-potential**:

**定义。** 标量势 φ 和矢量势 A（模块 1.10）合并为**四矢量势**：

A^μ = (φ/c, A_x, A_y, A_z).

The **gauge transformation** A^μ → A^μ + ∂^μ χ (where ∂^μ = (∂_t/c, −∇)) leaves all physical fields unchanged — the covariant statement of gauge invariance. From A^μ one constructs the **electromagnetic field tensor** (an antisymmetric rank-2 tensor):

**规范变换** A^μ → A^μ + ∂^μ χ（其中 ∂^μ = (∂_t/c, −∇)）不改变任何物理场——这是规范不变性的协变表述。由 A^μ 构造**电磁场张量**（反对称 2 阶张量）：

F^{μν} = ∂^μ A^ν − ∂^ν A^μ.

Its components are: F^{0i} = E_i/c and F^{ij} = −ε_{ijk} B_k. Explicitly, the six independent components of F^{μν} encode all three components of E and all three of B — the electric and magnetic fields are not separate objects but two faces of a single relativistic entity.

其分量为：F^{0i} = E_i/c，F^{ij} = −ε_{ijk} B_k。具体地，F^{μν} 的六个独立分量编码了 E 的全部三个分量和 B 的全部三个分量——电场和磁场不是独立的对象，而是单一相对论实体的两个侧面。

**Demonstration.** Under a Lorentz boost with velocity v along the x-axis, the field tensor transforms as F^{μν} → Λ^μ_α Λ^ν_β F^{αβ}. Reading off the components: E_x′ = E_x (parallel component unchanged), E_y′ = γ(E_y − vB_z), E_z′ = γ(E_z + vB_y), B_x′ = B_x, B_y′ = γ(B_y + vE_z/c²), B_z′ = γ(B_z − vE_y/c²). A purely electric field in one frame (e.g. the Coulomb field of a charge at rest) acquires a magnetic component in a frame where the charge is moving — magnetism is a relativistic effect of electricity.

**演示。** 在沿 x 轴以速度 v 的洛伦兹变换下，场张量变换为 F^{μν} → Λ^μ_α Λ^ν_β F^{αβ}。读出各分量：E_x′ = E_x（平行分量不变），E_y′ = γ(E_y − vB_z)，E_z′ = γ(E_z + vB_y)，B_x′ = B_x，B_y′ = γ(B_y + vE_z/c²)，B_z′ = γ(B_z − vE_y/c²)。在某参考系中纯粹的电场（例如静止电荷的库仑场），在电荷运动的参考系中获得磁场分量——磁性是电性的相对论效应。

**Application.** Two Lorentz scalars are built from F^{μν}: F^{μν} F_{μν} = 2(B² − E²/c²) and ε_{μνρσ} F^{μν} F^{ρσ} ∝ E · B. These are invariant under all Lorentz transformations and appear in the electromagnetic Lagrangian density L_EM = −(1/4μ₀) F^{μν} F_{μν}, which quantised gives QED (Phase 8).

**应用。** 由 F^{μν} 构造两个洛伦兹标量：F^{μν} F_{μν} = 2(B² − E²/c²) 和 ε_{μνρσ} F^{μν} F^{ρσ} ∝ E · B。它们在所有洛伦兹变换下不变，出现在电磁拉格朗日密度 L_EM = −(1/4μ₀) F^{μν} F_{μν} 中，量子化后给出量子电动力学（第 8 阶段）。

## 2. Maxwell's Equations in Covariant Form · 协变形式的麦克斯韦方程组

**Definition.** The full set of Maxwell's equations compresses into two covariant equations. The **inhomogeneous equations** (Gauss electric + Ampère–Maxwell) become:

**定义。** 完整的麦克斯韦方程组压缩为两个协变方程。**非齐次方程**（高斯电场方程 + 安培–麦克斯韦方程）变为：

∂_μ F^{μν} = μ₀ J^ν,

where J^ν = (cρ, J) is the **four-current** and ∂_μ = (∂_t/c, ∇). The **homogeneous equations** (Gauss magnetic + Faraday), which follow automatically from F^{μν} = ∂^μ A^ν − ∂^ν A^μ, are:

其中 J^ν = (cρ, J) 是**四电流**，∂_μ = (∂_t/c, ∇)。**齐次方程**（高斯磁场方程 + 法拉第方程）由 F^{μν} = ∂^μ A^ν − ∂^ν A^μ 自动得出：

∂_μ F̃^{μν} = 0,   where F̃^{μν} = ½ ε^{μνρσ} F_{ρσ} is the dual tensor.

Charge conservation ∂_μ J^μ = 0 follows from the antisymmetry of F^{μν}: ∂_ν ∂_μ F^{μν} = 0 automatically. In the Lorenz gauge ∂_μ A^μ = 0, the inhomogeneous Maxwell equation becomes □² A^ν = μ₀ J^ν.

电荷守恒 ∂_μ J^μ = 0 由 F^{μν} 的反对称性自动得出：∂_ν ∂_μ F^{μν} = 0。在洛伦兹规范 ∂_μ A^μ = 0 下，非齐次麦克斯韦方程变为 □² A^ν = μ₀ J^ν。

**Demonstration.** In a region with J^ν = 0, the equation ∂_μ F^{μν} = 0 with Lorenz gauge gives □²A^ν = 0 — the wave equation for each component of the four-potential. The solution A^ν ∝ ε^ν e^{ik_μ x^μ} with k^μ k_μ = 0 (null four-vector) represents a photon with polarisation four-vector ε^μ. The condition k · ε = 0 (from the Lorenz gauge) removes one polarisation degree of freedom; a further gauge freedom removes a second, leaving the two physical transverse polarisations of Module 1.11.

**演示。** 在 J^ν = 0 的区域，方程 ∂_μ F^{μν} = 0 配合洛伦兹规范给出 □²A^ν = 0——四矢量势各分量的波动方程。解 A^ν ∝ ε^ν e^{ik_μ x^μ}（其中 k^μ k_μ = 0，零四矢量）代表具有偏振四矢量 ε^μ 的光子。条件 k · ε = 0（来自洛伦兹规范）去掉一个偏振自由度；进一步的规范自由度再去掉一个，保留模块 1.11 的两个物理横向偏振。

**Application.** Covariant electromagnetism is the prototype of a **relativistic gauge field theory**. The pattern — an antisymmetric field tensor F^{μν} derived from a gauge potential A^μ, with field equations ∂_μ F^{μν} = J^ν — is the template for: QED (replace U(1) gauge group, add quantum fields, Phase 8.2); the Yang–Mills theories of the weak and strong force (replace U(1) with SU(2) and SU(3), Phase 8.1); and canonical field quantisation (Module 6.5). The electromagnetic field tensor Fμν and its action −¼ F^{μν} F_{μν} are the starting point that the entire Standard Model generalises.

**应用。** 协变电磁学是**相对论规范场论**的原型。其模式——由规范势 A^μ 推导出反对称场张量 F^{μν}，场方程为 ∂_μ F^{μν} = J^ν——是以下理论的模板：量子电动力学（替换 U(1) 规范群，加入量子场，第 8.2 阶段）；弱力和强力的杨–米尔斯理论（将 U(1) 替换为 SU(2) 和 SU(3)，第 8.1 阶段）；以及正则场量子化（模块 6.5）。电磁场张量 Fμν 及其作用量 −¼ F^{μν} F_{μν} 是整个标准模型推广的出发点。

---

**Self-test (blank page)**

1. Write down the four-potential A^μ and the field tensor F^{μν} = ∂^μ A^ν − ∂^ν A^μ. Show how E and B are encoded in the components of F^{μν}.
2. Apply the Lorentz transformation of F^{μν} to find E′ and B′ for a charge q at rest in frame S. Verify that in frame S′ (moving at velocity v relative to S), the transformed B′ matches the Biot–Savart result for a moving charge.
3. Write Maxwell's inhomogeneous equations in covariant form ∂_μ F^{μν} = μ₀ J^ν and expand the ν = 0 and ν = 1 components explicitly to recover the familiar 3D Maxwell equations.
4. What are the two independent Lorentz scalars constructed from F^{μν}? What are their physical meanings, and why must they be invariant?

**自测（空白页）**

1. 写出四矢量势 A^μ 和场张量 F^{μν} = ∂^μ A^ν − ∂^ν A^μ。展示 E 和 B 如何编码在 F^{μν} 的分量中。
2. 对静止在 S 系中的电荷 q，应用 F^{μν} 的洛伦兹变换求 E′ 和 B′。验证在 S′ 系（相对 S 以速度 v 运动）中，变换后的 B′ 与运动电荷的毕奥–萨伐尔结果一致。
3. 写出协变形式的麦克斯韦非齐次方程 ∂_μ F^{μν} = μ₀ J^ν，并展开 ν = 0 和 ν = 1 分量以恢复熟悉的三维麦克斯韦方程。
4. 由 F^{μν} 构造的两个独立洛伦兹标量是什么？它们的物理意义是什么？为什么它们必须是不变的？

---

← Previous: [Module 1.14 — Relativistic Dynamics & E = mc²](./module-1.14-relativistic-dynamics-energy-momentum.md) · [Phase 1 index](./README.md) · Next: [Module 1.16 — Mechanical Waves & Acoustics](./module-1.16-mechanical-waves-acoustics.md) →

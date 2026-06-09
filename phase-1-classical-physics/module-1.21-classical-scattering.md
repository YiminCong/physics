# Module 1.21 — Classical Scattering Theory
**模块 1.21 — 经典散射理论**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.21-classical-scattering-derivations.md)

---

## 1. Cross Section, Impact Parameter & the Scattering Angle · 截面、瞄准距离与散射角

**Definition.** In a scattering experiment a uniform beam of particles, each of energy E, is fired at a fixed central potential U(r). A particle's trajectory is labelled by its **impact parameter** b — the perpendicular distance from the target of the incoming asymptote. The interaction deflects it by a **scattering angle** θ. The **differential cross section** dσ/dΩ is defined so that (dσ/dΩ) dΩ is the effective target area sending particles into solid angle dΩ about θ. For a central potential the angle depends only on b, and conservation of particle number gives **dσ/dΩ = (b/sin θ)|db/dθ|** (Module 1.5 supplies the central-force orbits behind b(θ)).

**定义。** 在散射实验中，一束均匀的、每个粒子能量为 E 的粒子，射向固定的中心势 U(r)。粒子轨迹由其**瞄准距离** b 标记——入射渐近线到靶点的垂直距离。相互作用使其偏转一个**散射角** θ。**微分散射截面** dσ/dΩ 的定义使得 (dσ/dΩ) dΩ 是把粒子送入 θ 附近立体角 dΩ 的有效靶面积。对中心势，角度只依赖于 b，粒子数守恒给出 **dσ/dΩ = (b/sin θ)|db/dθ|**（模块 1.5 提供了 b(θ) 背后的中心力轨道）。

**Demonstration.** A ring of incident area dσ = 2πb db maps onto an annulus of solid angle dΩ = 2π sin θ dθ on the detector sphere. Equating the particle flux through both (the beam flux is uniform) gives dσ = (b/sin θ)|db/dθ| dΩ; the absolute value appears because a more central particle (smaller b) typically scatters through a larger angle, so db/dθ < 0. Knowing the function b(θ) for a given U(r) thus fixes the entire angular distribution.

**演示。** 入射面积为 dσ = 2πb db 的环，映射到探测球面上立体角为 dΩ = 2π sin θ dθ 的圆环带。令穿过两者的粒子通量相等（束流通量均匀），得 dσ = (b/sin θ)|db/dθ| dΩ；绝对值的出现是因为更靠中心的粒子（较小的 b）通常散射到更大的角度，故 db/dθ < 0。因此，对给定 U(r) 知道函数 b(θ) 就确定了整个角分布。

**Application.** The cross section is the bridge between the unobservable microscopic potential and the measurable count rate dN/dΩ = (incident flux) × (dσ/dΩ). Inverting measured angular distributions to infer the underlying force is the working principle of every scattering experiment, from Rutherford's gold foil to the LHC. The quantum version (Module 3.8, Born approximation) keeps the very same definition of dσ/dΩ.

**应用。** 散射截面是不可观测的微观势与可测的计数率 dN/dΩ = （入射通量）×（dσ/dΩ）之间的桥梁。把测得的角分布反演以推断背后的作用力，是从卢瑟福金箔到大型强子对撞机的每个散射实验的工作原理。量子版本（模块 3.8，玻恩近似）保留了完全相同的 dσ/dΩ 定义。

## 2. The Rutherford Formula · 卢瑟福公式

**Definition.** For the repulsive Coulomb potential U(r) = k/r with k = q₁q₂/(4πε₀), the central-force orbit is a hyperbola, and the impact parameter relates to the scattering angle by **b = (k/2E) cot(θ/2)**. Substituting into dσ/dΩ = (b/sin θ)|db/dθ| yields the **Rutherford differential cross section**: dσ/dΩ = (k/4E)²/sin⁴(θ/2) = [q₁q₂/(16πε₀E)]²/sin⁴(θ/2).

**定义。** 对排斥性库仑势 U(r) = k/r，其中 k = q₁q₂/(4πε₀)，中心力轨道是双曲线，瞄准距离与散射角的关系为 **b = (k/2E) cot(θ/2)**。代入 dσ/dΩ = (b/sin θ)|db/dθ| 给出**卢瑟福微分散射截面**：dσ/dΩ = (k/4E)²/sin⁴(θ/2) = [q₁q₂/(16πε₀E)]²/sin⁴(θ/2)。

**Demonstration.** Differentiating b = (k/2E) cot(θ/2) gives db/dθ = −(k/4E) csc²(θ/2). With sin θ = 2 sin(θ/2) cos(θ/2), the product (b/sin θ)|db/dθ| collapses cleanly: the cot(θ/2) and the two sin(θ/2) cos(θ/2) factors combine into 1/sin⁴(θ/2), leaving the prefactor (k/4E)². The cross section diverges as θ → 0 (sin⁴(θ/2) → 0), so the **total cross section ∫(dσ/dΩ) dΩ is infinite** — a direct fingerprint of the infinite range of the Coulomb force; a screened or finite-range potential restores a finite total cross section.

**演示。** 对 b = (k/2E) cot(θ/2) 求导得 db/dθ = −(k/4E) csc²(θ/2)。利用 sin θ = 2 sin(θ/2) cos(θ/2)，乘积 (b/sin θ)|db/dθ| 干净地化简：cot(θ/2) 与两个 sin(θ/2) cos(θ/2) 因子合并为 1/sin⁴(θ/2)，剩下前因子 (k/4E)²。当 θ → 0（sin⁴(θ/2) → 0）时截面发散，故**总截面 ∫(dσ/dΩ) dΩ 无穷大**——这是库仑力无穷力程的直接印记；屏蔽势或有限力程势可恢复有限的总截面。

**Application.** Rutherford's 1911 analysis of α-particles scattered off gold foil (Module 9.3) revealed the rare large-angle deflections that demanded a tiny massive nucleus, overturning the plum-pudding atom. Remarkably the **quantum** calculation (Module 3.8, Born approximation) gives the *identical* formula — the 1/sin⁴(θ/2) law survives the transition to wave mechanics. The same logic, scaled to GeV energies, underlies deep inelastic scattering (Module 8.9), whose large-angle excess revealed pointlike quarks inside the proton.

**应用。** 卢瑟福 1911 年对 α 粒子散射金箔（模块 9.3）的分析揭示了罕见的大角度偏转，这要求存在一个微小而致密的原子核，推翻了枣糕模型原子。值得注意的是，**量子**计算（模块 3.8，玻恩近似）给出*完全相同*的公式——1/sin⁴(θ/2) 定律在过渡到波动力学时依然成立。同样的逻辑放大到 GeV 能标，构成了深度非弹性散射（模块 8.9）的基础，其大角度的超出揭示了质子内部点状的夸克。

---

**Self-test (blank page)**

1. Define the impact parameter and the differential cross section, and derive dσ/dΩ = (b/sin θ)|db/dθ| from number conservation.
2. Explain physically why db/dθ < 0 for a repulsive potential and why the absolute value is needed.
3. Starting from b = (k/2E) cot(θ/2), reproduce the Rutherford cross section dσ/dΩ = (k/4E)²/sin⁴(θ/2).
4. Why does the Coulomb total cross section diverge, and what changes for a screened (finite-range) potential?

**自测（空白页）**

1. 定义瞄准距离和微分散射截面，并由粒子数守恒推导 dσ/dΩ = (b/sin θ)|db/dθ|。
2. 从物理上解释为何排斥势下 db/dθ < 0，以及为何需要绝对值。
3. 从 b = (k/2E) cot(θ/2) 出发，复现卢瑟福截面 dσ/dΩ = (k/4E)²/sin⁴(θ/2)。
4. 为何库仑总截面发散？对屏蔽（有限力程）势又有何变化？

---

← Previous: [Module 1.20 — Canonical Transformations & Hamilton–Jacobi](./module-1.20-canonical-transformations-hamilton-jacobi.md) · [Phase 1 index](./README.md) · Next: [Module 1.22 — Retarded Potentials & Radiation Reaction](./module-1.22-retarded-potentials-radiation-reaction.md) →

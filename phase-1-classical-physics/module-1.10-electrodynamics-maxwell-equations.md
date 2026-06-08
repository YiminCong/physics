# Module 1.10 — Electrodynamics & Maxwell's Equations ⭐
**模块 1.10 — 电动力学与麦克斯韦方程组 ⭐**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.10-electrodynamics-maxwell-equations-derivations.md)

---

## 1. Faraday's Law, Displacement Current, and the Full Maxwell Set · 法拉第定律、位移电流与完整麦克斯韦方程组

**Definition.** Two additional laws complete electromagnetism from the static picture. **Faraday's law of induction**: a time-varying magnetic flux through a loop induces an EMF, or in differential form:

**定义。** 两条附加定律使电磁学从静态图像趋于完整。**法拉第电磁感应定律**：穿过回路的时变磁通量感生电动势，或以微分形式：

∇ × E = −∂B/∂t.

This breaks the electrostatic condition ∇ × E = 0. Maxwell observed that Ampère's static law ∇ × B = μ₀ J is inconsistent with charge conservation (∇ · J = −∂ρ/∂t ≠ 0 in general) and added the **displacement current** ε₀ ∂E/∂t. The complete **Maxwell's equations** in differential form are:

这打破了静电条件 ∇ × E = 0。麦克斯韦注意到安培静态定律 ∇ × B = μ₀ J 与电荷守恒（一般情况下 ∇ · J = −∂ρ/∂t ≠ 0）不一致，并补充了**位移电流** ε₀ ∂E/∂t。完整的**麦克斯韦方程组**微分形式为：

∇ · E = ρ / ε₀             (Gauss — electric),
∇ · B = 0                  (Gauss — magnetic, no monopoles),
∇ × E = −∂B/∂t            (Faraday),
∇ × B = μ₀ J + μ₀ε₀ ∂E/∂t  (Ampère–Maxwell).

Charge continuity ∂ρ/∂t + ∇ · J = 0 follows automatically from the curl equations — it is not an independent law but a consistency condition.

电荷连续性方程 ∂ρ/∂t + ∇ · J = 0 从旋度方程自动得出——它不是独立的定律，而是一个自洽条件。

**Demonstration.** Taking the curl of Faraday's law and substituting Ampère–Maxwell (in vacuum, ρ = J = 0):

**演示。** 对法拉第定律取旋度，并代入安培–麦克斯韦方程（在真空中 ρ = J = 0）：

∇ × (∇ × E) = −∂/∂t (∇ × B) = −μ₀ε₀ ∂²E/∂t².

Using the vector identity ∇ × (∇ × E) = ∇(∇ · E) − ∇²E and ∇ · E = 0, this gives the wave equation:

利用矢量恒等式 ∇ × (∇ × E) = ∇(∇ · E) − ∇²E 和 ∇ · E = 0，得到波动方程：

∇²E − μ₀ε₀ ∂²E/∂t² = 0.

An identical equation holds for B. This is derived more fully in Module 1.11.

B 满足相同的方程。模块 1.11 中有更完整的推导。

**Application.** Maxwell's equations unify electricity, magnetism, and optics — one of the great syntheses in physics. They predict electromagnetic waves propagating at speed c = 1/√(μ₀ε₀), identified immediately with light. Written in covariant form (Module 1.15), they are manifestly Lorentz-invariant and the prototype for all relativistic gauge field theories. Their quantisation produces photons and quantum electrodynamics (Phase 6, Phase 8).

**应用。** 麦克斯韦方程组统一了电、磁和光——物理学上最伟大的综合之一。它们预言了以速度 c = 1/√(μ₀ε₀) 传播的电磁波，即刻被认同为光。用协变形式写出（模块 1.15），它们明显洛伦兹不变，并且是所有相对论规范场论的原型。对其量子化产生光子和量子电动力学（第 6、8 阶段）。

## 2. The Electromagnetic Potentials · 电磁势

**Definition.** From ∇ · B = 0 write B = ∇ × A. Faraday's law then gives ∇ × (E + ∂A/∂t) = 0, so E + ∂A/∂t = −∇φ, i.e.

**定义。** 由 ∇ · B = 0 写 B = ∇ × A。法拉第定律则给出 ∇ × (E + ∂A/∂t) = 0，故 E + ∂A/∂t = −∇φ，即

E = −∇φ − ∂A/∂t,   B = ∇ × A.

The gauge transformations φ → φ − ∂χ/∂t, A → A + ∇χ leave E and B unchanged. The **Lorenz gauge** ∇ · A + (1/c²) ∂φ/∂t = 0 decouples the potentials into two wave equations: □²φ = −ρ/ε₀ and □²A = −μ₀ J, where □² = ∇² − (1/c²)∂²/∂t² is the d'Alembertian.

规范变换 φ → φ − ∂χ/∂t，A → A + ∇χ 不改变 E 和 B。**洛伦兹规范** ∇ · A + (1/c²) ∂φ/∂t = 0 将势解耦为两个波动方程：□²φ = −ρ/ε₀ 和 □²A = −μ₀ J，其中 □² = ∇² − (1/c²)∂²/∂t² 是达朗贝尔算符。

**Application.** The potentials (φ, A) unify naturally into the four-potential A^μ of special relativity (Module 1.15), making gauge invariance manifestly covariant. They enter quantum mechanics directly — the canonical momentum of a charged particle is p − qA — and are the fundamental objects of gauge field theory (Phase 8).

**应用。** 势 (φ, A) 自然地统一为狭义相对论中的四矢量势 A^μ（模块 1.15），使规范不变性明显协变。它们直接进入量子力学——带电粒子的正则动量为 p − qA——并且是规范场论（第 8 阶段）的基本对象。

---

**Self-test (blank page)**

1. Write all four Maxwell equations in differential form. Identify which two are "source equations" and which two are "curl equations." Derive the continuity equation ∂ρ/∂t + ∇ · J = 0 from them.
2. Why did Maxwell add the displacement current term ε₀ ∂E/∂t to Ampère's law? Show that without it, charge conservation would be violated.
3. Show that E = −∇φ − ∂A/∂t and B = ∇ × A satisfy Faraday's law and the no-monopole condition identically.
4. In the Lorenz gauge, write the wave equations for φ and A. What is the d'Alembertian □²?

**自测（空白页）**

1. 写出微分形式的全部四个麦克斯韦方程。指出哪两个是"源方程"，哪两个是"旋度方程"。从中推导连续性方程 ∂ρ/∂t + ∇ · J = 0。
2. 麦克斯韦为什么在安培定律中添加位移电流项 ε₀ ∂E/∂t？证明若没有它，电荷守恒将被破坏。
3. 证明 E = −∇φ − ∂A/∂t 和 B = ∇ × A 恒等地满足法拉第定律和无磁单极条件。
4. 在洛伦兹规范中，写出 φ 和 A 的波动方程。达朗贝尔算符 □² 是什么？

---

← Previous: [Module 1.9 — Magnetostatics](./module-1.9-magnetostatics.md) · [Phase 1 index](./README.md) · Next: [Module 1.11 — Electromagnetic Waves & Radiation](./module-1.11-em-waves-radiation.md) →

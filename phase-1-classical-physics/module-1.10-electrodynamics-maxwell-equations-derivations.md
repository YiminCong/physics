# Derivations — Module 1.10: Electrodynamics & Maxwell's Equations
# 推导 — 模块 1.10：电动力学与麦克斯韦方程组

> Companion to [Module 1.10](./module-1.10-electrodynamics-maxwell-equations.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.10](./module-1.10-electrodynamics-maxwell-equations.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Displacement Current from Charge Continuity · 从电荷连续性推导位移电流

**Claim.** The static Ampère law ∇ × B = μ₀ J is inconsistent with the continuity equation ∂ρ/∂t + ∇ · J = 0. Adding the displacement current term μ₀ε₀ ∂E/∂t restores consistency.

**命题。** 静态安培定律 ∇ × B = μ₀ J 与连续性方程 ∂ρ/∂t + ∇ · J = 0 不一致。添加位移电流项 μ₀ε₀ ∂E/∂t 恢复了自洽性。

**Step 1 — The inconsistency of static Ampère's law.** Take the divergence of the static Ampère law ∇ × B = μ₀ J:

**第 1 步 — 静态安培定律的不自洽性。** 对静态安培定律 ∇ × B = μ₀ J 取散度：

  ∇ · (∇ × B) = μ₀ ∇ · J.

The left side is identically zero (divergence of a curl): ∇ · (∇ × B) ≡ 0. Therefore the static law requires:

左边恒为零（旋度的散度）：∇ · (∇ × B) ≡ 0。因此静态定律要求：

  0 = μ₀ ∇ · J,   i.e.   ∇ · J = 0.

But the continuity equation (which is a fundamental consequence of charge conservation) states ∂ρ/∂t + ∇ · J = 0. In general ∂ρ/∂t ≠ 0 (e.g., a capacitor being charged), so ∇ · J ≠ 0. **Contradiction.**

但连续性方程（电荷守恒的根本推论）指出 ∂ρ/∂t + ∇ · J = 0。一般情况下 ∂ρ/∂t ≠ 0（例如正在充电的电容器），故 ∇ · J ≠ 0。**矛盾。**

**Step 2 — Maxwell's fix: identify the missing term.** We need to add a term X to Ampère's law: ∇ × B = μ₀ J + X, such that taking the divergence gives 0 = μ₀ ∇ · J + ∇ · X. This requires ∇ · X = −μ₀ ∇ · J = μ₀ ∂ρ/∂t.

**第 2 步 — 麦克斯韦的修正：识别缺失项。** 我们需要在安培定律中添加一项 X：∇ × B = μ₀ J + X，使得取散度后得 0 = μ₀ ∇ · J + ∇ · X。这要求 ∇ · X = −μ₀ ∇ · J = μ₀ ∂ρ/∂t。

**Step 3 — Use Gauss's law to find X.** From Gauss's law ∇ · E = ρ/ε₀, we have ∂ρ/∂t = ε₀ ∂(∇ · E)/∂t = ε₀ ∇ · (∂E/∂t) (the time derivative and spatial divergence commute for smooth fields). Therefore:

**第 3 步 — 用高斯定律求 X。** 由高斯定律 ∇ · E = ρ/ε₀，我们有 ∂ρ/∂t = ε₀ ∂(∇ · E)/∂t = ε₀ ∇ · (∂E/∂t)（对光滑场，时间导数与空间散度可交换次序）。因此：

  ∇ · X = μ₀ ∂ρ/∂t = μ₀ε₀ ∇ · (∂E/∂t).

The simplest choice (and the correct one, confirmed by experiment) is:

最简单的选择（也是正确的，由实验证实）为：

  **X = μ₀ε₀ ∂E/∂t**,   the **displacement current density**.

**第 3 步补充。** X = μ₀ε₀ ∂E/∂t 被称为**位移电流密度**。

**Step 4 — Modified Ampère–Maxwell law.** The full Ampère–Maxwell equation is:

**第 4 步 — 修正后的安培–麦克斯韦定律。** 完整的安培–麦克斯韦方程为：

  **∇ × B = μ₀ J + μ₀ε₀ ∂E/∂t.**

Verification: ∇ · (∇ × B) = μ₀ ∇ · J + μ₀ε₀ ∇ · (∂E/∂t) = μ₀ ∇ · J + μ₀ ∂ρ/∂t = μ₀(∇ · J + ∂ρ/∂t) = 0 by the continuity equation. ∎

验证：∇ · (∇ × B) = μ₀ ∇ · J + μ₀ε₀ ∇ · (∂E/∂t) = μ₀ ∇ · J + μ₀ ∂ρ/∂t = μ₀(∇ · J + ∂ρ/∂t) = 0（由连续性方程）。∎

---

## B. Assembly of the Complete Maxwell Equations · 完整麦克斯韦方程组的组装

**Claim.** The four Maxwell equations, assembled from electrostatics (Gauss's law), absence of monopoles (∇·B=0), Faraday's induction law, and the Ampère–Maxwell law, form a complete and self-consistent set.

**命题。** 从静电学（高斯定律）、无磁单极（∇·B=0）、法拉第感应定律和安培–麦克斯韦定律组装而来的四个麦克斯韦方程，构成完整且自洽的方程组。

**Step 1 — Faraday's law from the induction experiments.** Faraday (1831) observed that a changing magnetic flux through a loop induces an EMF. In differential form (using Stokes' theorem to convert the integral law ∮ E · dℓ = −d/dt ∫_S B · dA):

**第 1 步 — 从感应实验得到法拉第定律。** 法拉第（1831 年）观察到穿过回路的变化磁通量感生电动势。用微分形式（用斯托克斯定理将积分定律 ∮ E · dℓ = −d/dt ∫_S B · dA 转换）：

  ∮_C E · dℓ = −d/dt ∫_S B · dA
  ∫_S (∇ × E) · dA = −∫_S (∂B/∂t) · dA.

Since this holds for any surface S, equating integrands:

由于这对任意曲面 S 成立，令被积函数相等：

  **∇ × E = −∂B/∂t.**

This replaces the static ∇ × E = 0. In electrostatics, ∂B/∂t = 0 recovers the earlier result.

这取代了静电学中的 ∇ × E = 0。在静电学中，∂B/∂t = 0 恢复了之前的结果。

**Step 2 — The complete four Maxwell equations.** Combining all laws:

**第 2 步 — 完整的四个麦克斯韦方程。** 综合所有定律：

  (I)   ∇ · E = ρ / ε₀                         (Gauss — electric / 高斯—电场)
  (II)  ∇ · B = 0                               (Gauss — magnetic / 高斯—磁场)
  (III) ∇ × E = −∂B/∂t                         (Faraday / 法拉第)
  (IV)  ∇ × B = μ₀ J + μ₀ε₀ ∂E/∂t             (Ampère–Maxwell / 安培–麦克斯韦)

These four equations, together with the Lorentz force law F = q(E + v × B), completely describe all classical electromagnetic phenomena.

这四个方程，连同洛伦兹力定律 F = q(E + v × B)，完整描述了所有经典电磁现象。

**Step 3 — Integral forms via Stokes and Gauss.** The integral forms follow by applying Stokes' theorem (for equations III, IV) and the divergence theorem (for equations I, II):

**第 3 步 — 经斯托克斯和高斯定理得积分形式。** 积分形式通过对方程 III、IV 应用斯托克斯定理，对方程 I、II 应用散度定理得到：

  (I)   ∮_S E · dA = Q_enc / ε₀
  (II)  ∮_S B · dA = 0
  (III) ∮_C E · dℓ = −d/dt ∫_S B · dA   (Faraday's law of induction)
  (IV)  ∮_C B · dℓ = μ₀ I_enc + μ₀ε₀ d/dt ∫_S E · dA.

---

## C. Charge Conservation Is Built Into Maxwell's Equations · 电荷守恒内置于麦克斯韦方程组中

**Claim.** The continuity equation ∂ρ/∂t + ∇ · J = 0 is a mathematical consequence of the Maxwell equations; it is not an independent assumption.

**命题。** 连续性方程 ∂ρ/∂t + ∇ · J = 0 是麦克斯韦方程组的数学推论，不是独立假设。

**Step 1 — Take the divergence of Ampère–Maxwell.** Apply ∇ · to equation (IV):

**第 1 步 — 对安培–麦克斯韦方程取散度。** 对方程 (IV) 施用 ∇ ·：

  ∇ · (∇ × B) = μ₀ ∇ · J + μ₀ε₀ ∂(∇ · E)/∂t.

Left side: ∇ · (∇ × B) ≡ 0. Right side: use equation (I), ∇ · E = ρ/ε₀, so ∂(∇ · E)/∂t = ∂ρ/(ε₀ ∂t):

左边：∇ · (∇ × B) ≡ 0。右边：利用方程 (I)，∇ · E = ρ/ε₀，故 ∂(∇ · E)/∂t = ∂ρ/(ε₀ ∂t)：

  0 = μ₀ ∇ · J + μ₀ε₀ · ∂ρ/(ε₀ ∂t) = μ₀ ∇ · J + μ₀ ∂ρ/∂t.

Dividing by μ₀:

除以 μ₀：

  **∂ρ/∂t + ∇ · J = 0.** ∎

This is the local statement of charge conservation: the rate of decrease of charge in a volume equals the outward current flux through its surface. Maxwell's equations are internally consistent precisely because they contain this conservation law automatically.

这是电荷守恒的局域表述：体积内电荷的减少率等于穿过其表面的向外电流通量。麦克斯韦方程组在内部是自洽的，正是因为它们自动包含了这一守恒定律。

---

## D. Electromagnetic Potentials and Gauge Invariance · 电磁势与规范不变性

**Claim.** The equations ∇ · B = 0 and ∇ × E = −∂B/∂t are satisfied identically by E = −∇φ − ∂A/∂t, B = ∇ × A, for any smooth φ and A. The transformation φ → φ − ∂χ/∂t, A → A + ∇χ (for any χ) leaves E and B unchanged.

**命题。** 对任意光滑 φ 和 A，方程 ∇ · B = 0 和 ∇ × E = −∂B/∂t 被 E = −∇φ − ∂A/∂t，B = ∇ × A 恒等满足。变换 φ → φ − ∂χ/∂t，A → A + ∇χ（对任意 χ）不改变 E 和 B。

**Step 1 — B = ∇ × A satisfies ∇ · B = 0.** Immediately: ∇ · B = ∇ · (∇ × A) ≡ 0. ✓

**第 1 步 — B = ∇ × A 满足 ∇ · B = 0。** 直接得：∇ · B = ∇ · (∇ × A) ≡ 0。✓

**Step 2 — E = −∇φ − ∂A/∂t satisfies Faraday's law.** Compute ∇ × E:

**第 2 步 — E = −∇φ − ∂A/∂t 满足法拉第定律。** 计算 ∇ × E：

  ∇ × E = ∇ × (−∇φ − ∂A/∂t) = −∇ × (∇φ) − ∂(∇ × A)/∂t = 0 − ∂B/∂t = −∂B/∂t. ✓

(using ∇ × (∇φ) ≡ 0 and the commutativity of ∂/∂t and ∇×.)

（利用 ∇ × (∇φ) ≡ 0 和 ∂/∂t 与 ∇× 的可交换性。）

**Step 3 — Gauge invariance.** Under the gauge transformation A′ = A + ∇χ, φ′ = φ − ∂χ/∂t:

**第 3 步 — 规范不变性。** 在规范变换 A′ = A + ∇χ，φ′ = φ − ∂χ/∂t 下：

  B′ = ∇ × A′ = ∇ × (A + ∇χ) = ∇ × A + ∇ × (∇χ) = B + 0 = B. ✓
  E′ = −∇φ′ − ∂A′/∂t = −∇(φ − ∂χ/∂t) − ∂(A + ∇χ)/∂t
      = −∇φ + ∇(∂χ/∂t) − ∂A/∂t − ∂(∇χ)/∂t
      = −∇φ − ∂A/∂t + (∇(∂χ/∂t) − ∂(∇χ)/∂t) = E + 0 = E. ✓

The two terms cancel because ∂/∂t and ∇ commute for smooth χ: ∇(∂χ/∂t) = ∂(∇χ)/∂t. ∎

两项相消是因为对光滑 χ，∂/∂t 与 ∇ 可交换：∇(∂χ/∂t) = ∂(∇χ)/∂t。∎

---

*The displacement current is the lynchpin of electromagnetic wave propagation (Module 1.11); gauge invariance becomes the organising principle of QED and all Standard Model forces (Phase 8).*

*位移电流是电磁波传播的关键（模块 1.11）；规范不变性成为量子电动力学和标准模型所有力的组织原理（第 8 阶段）。*

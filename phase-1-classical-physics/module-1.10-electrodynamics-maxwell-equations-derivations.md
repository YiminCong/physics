---
title: "Derivations — Module 1.10: Electrodynamics & Maxwell's Equations"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 1.10: Electrodynamics & Maxwell's Equations
# 推导 — 模块 1.10：电动力学与麦克斯韦方程组

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.10](./module-1.10-electrodynamics-maxwell-equations.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.10](./module-1.10-electrodynamics-maxwell-equations.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Displacement Current from Charge Continuity · 从电荷连续性推导位移电流

**Claim.** The static Ampère law $\nabla\times\mathbf{B} = \mu_0\mathbf{J}$ is inconsistent with the continuity equation $\partial\rho/\partial t + \nabla\cdot\mathbf{J} = 0$. Adding the displacement current term $\mu_0\epsilon_0\,\partial\mathbf{E}/\partial t$ restores consistency.

**命题。** 静态安培定律 $\nabla\times\mathbf{B} = \mu_0\mathbf{J}$ 与连续性方程 $\partial\rho/\partial t + \nabla\cdot\mathbf{J} = 0$ 不一致。添加位移电流项 $\mu_0\epsilon_0\,\partial\mathbf{E}/\partial t$ 恢复了自洽性。

**Step 1 — The inconsistency of static Ampère's law.** Take the divergence of the static Ampère law $\nabla\times\mathbf{B} = \mu_0\mathbf{J}$:

**第 1 步 — 静态安培定律的不自洽性。** 对静态安培定律 $\nabla\times\mathbf{B} = \mu_0\mathbf{J}$ 取散度：

$$ \nabla\cdot(\nabla\times\mathbf{B}) = \mu_0\,\nabla\cdot\mathbf{J}. $$

The left side is identically zero (divergence of a curl): $\nabla\cdot(\nabla\times\mathbf{B})\equiv 0$. Therefore the static law requires:

左边恒为零（旋度的散度）：$\nabla\cdot(\nabla\times\mathbf{B})\equiv 0$。因此静态定律要求：

$$ 0 = \mu_0\,\nabla\cdot\mathbf{J}, \qquad \text{i.e.}\quad \nabla\cdot\mathbf{J} = 0. $$

But the continuity equation (which is a fundamental consequence of charge conservation) states $\partial\rho/\partial t + \nabla\cdot\mathbf{J} = 0$. In general $\partial\rho/\partial t\ne 0$ (e.g., a capacitor being charged), so $\nabla\cdot\mathbf{J}\ne 0$. **Contradiction.**

但连续性方程（电荷守恒的根本推论）指出 $\partial\rho/\partial t + \nabla\cdot\mathbf{J} = 0$。一般情况下 $\partial\rho/\partial t\ne 0$（例如正在充电的电容器），故 $\nabla\cdot\mathbf{J}\ne 0$。**矛盾。**

**Step 2 — Maxwell's fix: identify the missing term.** We need to add a term $\mathbf{X}$ to Ampère's law: $\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mathbf{X}$, such that taking the divergence gives $0 = \mu_0\,\nabla\cdot\mathbf{J} + \nabla\cdot\mathbf{X}$. This requires $\nabla\cdot\mathbf{X} = -\mu_0\,\nabla\cdot\mathbf{J} = \mu_0\,\partial\rho/\partial t$.

**第 2 步 — 麦克斯韦的修正：识别缺失项。** 我们需要在安培定律中添加一项 $\mathbf{X}$：$\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mathbf{X}$，使得取散度后得 $0 = \mu_0\,\nabla\cdot\mathbf{J} + \nabla\cdot\mathbf{X}$。这要求 $\nabla\cdot\mathbf{X} = -\mu_0\,\nabla\cdot\mathbf{J} = \mu_0\,\partial\rho/\partial t$。

**Step 3 — Use Gauss's law to find $\mathbf{X}$.** From Gauss's law $\nabla\cdot\mathbf{E} = \rho/\epsilon_0$, we have $\partial\rho/\partial t = \epsilon_0\,\partial(\nabla\cdot\mathbf{E})/\partial t = \epsilon_0\,\nabla\cdot(\partial\mathbf{E}/\partial t)$ (the time derivative and spatial divergence commute for smooth fields). Therefore:

**第 3 步 — 用高斯定律求 $\mathbf{X}$。** 由高斯定律 $\nabla\cdot\mathbf{E} = \rho/\epsilon_0$，我们有 $\partial\rho/\partial t = \epsilon_0\,\partial(\nabla\cdot\mathbf{E})/\partial t = \epsilon_0\,\nabla\cdot(\partial\mathbf{E}/\partial t)$（对光滑场，时间导数与空间散度可交换次序）。因此：

$$ \nabla\cdot\mathbf{X} = \mu_0\,\frac{\partial\rho}{\partial t} = \mu_0\epsilon_0\,\nabla\cdot\!\left(\frac{\partial\mathbf{E}}{\partial t}\right). $$

The simplest choice (and the correct one, confirmed by experiment) is:

最简单的选择（也是正确的，由实验证实）为：

$$ \boxed{\,\mathbf{X} = \mu_0\epsilon_0\,\frac{\partial\mathbf{E}}{\partial t}\,}, \qquad \text{the \textbf{displacement current density}.} $$

**第 3 步补充。** $\mathbf{X} = \mu_0\epsilon_0\,\partial\mathbf{E}/\partial t$ 被称为**位移电流密度**。

**Step 4 — Modified Ampère–Maxwell law.** The full Ampère–Maxwell equation is:

**第 4 步 — 修正后的安培–麦克斯韦定律。** 完整的安培–麦克斯韦方程为：

$$ \boxed{\, \nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\epsilon_0\,\frac{\partial\mathbf{E}}{\partial t} \,} $$

Verification: $\nabla\cdot(\nabla\times\mathbf{B}) = \mu_0\,\nabla\cdot\mathbf{J} + \mu_0\epsilon_0\,\nabla\cdot(\partial\mathbf{E}/\partial t) = \mu_0\,\nabla\cdot\mathbf{J} + \mu_0\,\partial\rho/\partial t = \mu_0(\nabla\cdot\mathbf{J} + \partial\rho/\partial t) = 0$ by the continuity equation. $\blacksquare$

验证：$\nabla\cdot(\nabla\times\mathbf{B}) = \mu_0\,\nabla\cdot\mathbf{J} + \mu_0\epsilon_0\,\nabla\cdot(\partial\mathbf{E}/\partial t) = \mu_0\,\nabla\cdot\mathbf{J} + \mu_0\,\partial\rho/\partial t = \mu_0(\nabla\cdot\mathbf{J} + \partial\rho/\partial t) = 0$（由连续性方程）。$\blacksquare$

---

## B. Assembly of the Complete Maxwell Equations · 完整麦克斯韦方程组的组装

**Claim.** The four Maxwell equations, assembled from electrostatics (Gauss's law), absence of monopoles ($\nabla\cdot\mathbf{B}=0$), Faraday's induction law, and the Ampère–Maxwell law, form a complete and self-consistent set.

**命题。** 从静电学（高斯定律）、无磁单极（$\nabla\cdot\mathbf{B}=0$）、法拉第感应定律和安培–麦克斯韦定律组装而来的四个麦克斯韦方程，构成完整且自洽的方程组。

**Step 1 — Faraday's law from the induction experiments.** Faraday (1831) observed that a changing magnetic flux through a loop induces an EMF. In differential form (using Stokes' theorem to convert the integral law $\oint \mathbf{E}\cdot d\boldsymbol{\ell} = -d/dt\int_S \mathbf{B}\cdot d\mathbf{A}$):

**第 1 步 — 从感应实验得到法拉第定律。** 法拉第（1831 年）观察到穿过回路的变化磁通量感生电动势。用微分形式（用斯托克斯定理将积分定律 $\oint \mathbf{E}\cdot d\boldsymbol{\ell} = -d/dt\int_S \mathbf{B}\cdot d\mathbf{A}$ 转换）：

$$ \begin{aligned}
\oint_C \mathbf{E}\cdot d\boldsymbol{\ell} &= -\frac{d}{dt}\int_S \mathbf{B}\cdot d\mathbf{A} \\
\int_S (\nabla\times\mathbf{E})\cdot d\mathbf{A} &= -\int_S \frac{\partial\mathbf{B}}{\partial t}\cdot d\mathbf{A}.
\end{aligned} $$

Since this holds for any surface $S$, equating integrands:

由于这对任意曲面 $S$ 成立，令被积函数相等：

$$ \boxed{\,\nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t}\,} $$

This replaces the static $\nabla\times\mathbf{E} = 0$. In electrostatics, $\partial\mathbf{B}/\partial t = 0$ recovers the earlier result.

这取代了静电学中的 $\nabla\times\mathbf{E} = 0$。在静电学中，$\partial\mathbf{B}/\partial t = 0$ 恢复了之前的结果。

**Step 2 — The complete four Maxwell equations.** Combining all laws:

**第 2 步 — 完整的四个麦克斯韦方程。** 综合所有定律：

$$ \begin{aligned}
\text{(I)}\quad & \nabla\cdot\mathbf{E} = \frac{\rho}{\epsilon_0} && \text{(Gauss — electric / 高斯—电场)} \\
\text{(II)}\quad & \nabla\cdot\mathbf{B} = 0 && \text{(Gauss — magnetic / 高斯—磁场)} \\
\text{(III)}\quad & \nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t} && \text{(Faraday / 法拉第)} \\
\text{(IV)}\quad & \nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\epsilon_0\,\frac{\partial\mathbf{E}}{\partial t} && \text{(Ampère–Maxwell / 安培–麦克斯韦)}
\end{aligned} $$

These four equations, together with the Lorentz force law $\mathbf{F} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$, completely describe all classical electromagnetic phenomena.

这四个方程，连同洛伦兹力定律 $\mathbf{F} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$，完整描述了所有经典电磁现象。

**Step 3 — Integral forms via Stokes and Gauss.** The integral forms follow by applying Stokes' theorem (for equations III, IV) and the divergence theorem (for equations I, II):

**第 3 步 — 经斯托克斯和高斯定理得积分形式。** 积分形式通过对方程 III、IV 应用斯托克斯定理，对方程 I、II 应用散度定理得到：

$$ \begin{aligned}
\text{(I)}\quad & \oint_S \mathbf{E}\cdot d\mathbf{A} = \frac{Q_\text{enc}}{\epsilon_0} \\
\text{(II)}\quad & \oint_S \mathbf{B}\cdot d\mathbf{A} = 0 \\
\text{(III)}\quad & \oint_C \mathbf{E}\cdot d\boldsymbol{\ell} = -\frac{d}{dt}\int_S \mathbf{B}\cdot d\mathbf{A} && \text{(Faraday's law of induction)} \\
\text{(IV)}\quad & \oint_C \mathbf{B}\cdot d\boldsymbol{\ell} = \mu_0 I_\text{enc} + \mu_0\epsilon_0\,\frac{d}{dt}\int_S \mathbf{E}\cdot d\mathbf{A}.
\end{aligned} $$

---

## C. Charge Conservation Is Built Into Maxwell's Equations · 电荷守恒内置于麦克斯韦方程组中

**Claim.** The continuity equation $\partial\rho/\partial t + \nabla\cdot\mathbf{J} = 0$ is a mathematical consequence of the Maxwell equations; it is not an independent assumption.

**命题。** 连续性方程 $\partial\rho/\partial t + \nabla\cdot\mathbf{J} = 0$ 是麦克斯韦方程组的数学推论，不是独立假设。

**Step 1 — Take the divergence of Ampère–Maxwell.** Apply $\nabla\cdot$ to equation (IV):

**第 1 步 — 对安培–麦克斯韦方程取散度。** 对方程 (IV) 施用 $\nabla\cdot$：

$$ \nabla\cdot(\nabla\times\mathbf{B}) = \mu_0\,\nabla\cdot\mathbf{J} + \mu_0\epsilon_0\,\frac{\partial(\nabla\cdot\mathbf{E})}{\partial t}. $$

Left side: $\nabla\cdot(\nabla\times\mathbf{B})\equiv 0$. Right side: use equation (I), $\nabla\cdot\mathbf{E} = \rho/\epsilon_0$, so $\partial(\nabla\cdot\mathbf{E})/\partial t = \partial\rho/(\epsilon_0\,\partial t)$:

左边：$\nabla\cdot(\nabla\times\mathbf{B})\equiv 0$。右边：利用方程 (I)，$\nabla\cdot\mathbf{E} = \rho/\epsilon_0$，故 $\partial(\nabla\cdot\mathbf{E})/\partial t = \partial\rho/(\epsilon_0\,\partial t)$：

$$ 0 = \mu_0\,\nabla\cdot\mathbf{J} + \mu_0\epsilon_0\cdot\frac{\partial\rho}{\epsilon_0\,\partial t} = \mu_0\,\nabla\cdot\mathbf{J} + \mu_0\,\frac{\partial\rho}{\partial t}. $$

Dividing by $\mu_0$:

除以 $\mu_0$：

$$ \boxed{\,\frac{\partial\rho}{\partial t} + \nabla\cdot\mathbf{J} = 0\,} \qquad \blacksquare $$

This is the local statement of charge conservation: the rate of decrease of charge in a volume equals the outward current flux through its surface. Maxwell's equations are internally consistent precisely because they contain this conservation law automatically.

这是电荷守恒的局域表述：体积内电荷的减少率等于穿过其表面的向外电流通量。麦克斯韦方程组在内部是自洽的，正是因为它们自动包含了这一守恒定律。

---

## D. Electromagnetic Potentials and Gauge Invariance · 电磁势与规范不变性

**Claim.** The equations $\nabla\cdot\mathbf{B} = 0$ and $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$ are satisfied identically by $\mathbf{E} = -\nabla\varphi - \partial\mathbf{A}/\partial t$, $\mathbf{B} = \nabla\times\mathbf{A}$, for any smooth $\varphi$ and $\mathbf{A}$. The transformation $\varphi\to\varphi - \partial\chi/\partial t$, $\mathbf{A}\to\mathbf{A} + \nabla\chi$ (for any $\chi$) leaves $\mathbf{E}$ and $\mathbf{B}$ unchanged.

**命题。** 对任意光滑 $\varphi$ 和 $\mathbf{A}$，方程 $\nabla\cdot\mathbf{B} = 0$ 和 $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$ 被 $\mathbf{E} = -\nabla\varphi - \partial\mathbf{A}/\partial t$，$\mathbf{B} = \nabla\times\mathbf{A}$ 恒等满足。变换 $\varphi\to\varphi - \partial\chi/\partial t$，$\mathbf{A}\to\mathbf{A} + \nabla\chi$（对任意 $\chi$）不改变 $\mathbf{E}$ 和 $\mathbf{B}$。

**Step 1 — $\mathbf{B} = \nabla\times\mathbf{A}$ satisfies $\nabla\cdot\mathbf{B} = 0$.** Immediately: $\nabla\cdot\mathbf{B} = \nabla\cdot(\nabla\times\mathbf{A})\equiv 0$. ✓

**第 1 步 — $\mathbf{B} = \nabla\times\mathbf{A}$ 满足 $\nabla\cdot\mathbf{B} = 0$。** 直接得：$\nabla\cdot\mathbf{B} = \nabla\cdot(\nabla\times\mathbf{A})\equiv 0$。✓

**Step 2 — $\mathbf{E} = -\nabla\varphi - \partial\mathbf{A}/\partial t$ satisfies Faraday's law.** Compute $\nabla\times\mathbf{E}$:

**第 2 步 — $\mathbf{E} = -\nabla\varphi - \partial\mathbf{A}/\partial t$ 满足法拉第定律。** 计算 $\nabla\times\mathbf{E}$：

$$ \nabla\times\mathbf{E} = \nabla\times\!\left(-\nabla\varphi - \frac{\partial\mathbf{A}}{\partial t}\right) = -\nabla\times(\nabla\varphi) - \frac{\partial(\nabla\times\mathbf{A})}{\partial t} = 0 - \frac{\partial\mathbf{B}}{\partial t} = -\frac{\partial\mathbf{B}}{\partial t}. \;\checkmark $$

(using $\nabla\times(\nabla\varphi)\equiv 0$ and the commutativity of $\partial/\partial t$ and $\nabla\times$.)

（利用 $\nabla\times(\nabla\varphi)\equiv 0$ 和 $\partial/\partial t$ 与 $\nabla\times$ 的可交换性。）

**Step 3 — Gauge invariance.** Under the gauge transformation $\mathbf{A}' = \mathbf{A} + \nabla\chi$, $\varphi' = \varphi - \partial\chi/\partial t$:

**第 3 步 — 规范不变性。** 在规范变换 $\mathbf{A}' = \mathbf{A} + \nabla\chi$，$\varphi' = \varphi - \partial\chi/\partial t$ 下：

$$ \begin{aligned}
\mathbf{B}' &= \nabla\times\mathbf{A}' = \nabla\times(\mathbf{A} + \nabla\chi) = \nabla\times\mathbf{A} + \nabla\times(\nabla\chi) = \mathbf{B} + 0 = \mathbf{B}. \;\checkmark \\
\mathbf{E}' &= -\nabla\varphi' - \frac{\partial\mathbf{A}'}{\partial t} = -\nabla\!\left(\varphi - \frac{\partial\chi}{\partial t}\right) - \frac{\partial(\mathbf{A} + \nabla\chi)}{\partial t} \\
&= -\nabla\varphi + \nabla\!\left(\frac{\partial\chi}{\partial t}\right) - \frac{\partial\mathbf{A}}{\partial t} - \frac{\partial(\nabla\chi)}{\partial t} \\
&= -\nabla\varphi - \frac{\partial\mathbf{A}}{\partial t} + \left(\nabla\frac{\partial\chi}{\partial t} - \frac{\partial(\nabla\chi)}{\partial t}\right) = \mathbf{E} + 0 = \mathbf{E}. \;\checkmark
\end{aligned} $$

The two terms cancel because $\partial/\partial t$ and $\nabla$ commute for smooth $\chi$: $\nabla(\partial\chi/\partial t) = \partial(\nabla\chi)/\partial t$. $\blacksquare$

两项相消是因为对光滑 $\chi$，$\partial/\partial t$ 与 $\nabla$ 可交换：$\nabla(\partial\chi/\partial t) = \partial(\nabla\chi)/\partial t$。$\blacksquare$

---

*The displacement current is the lynchpin of electromagnetic wave propagation (Module 1.11); gauge invariance becomes the organising principle of QED and all Standard Model forces (Phase 8).*

*位移电流是电磁波传播的关键（模块 1.11）；规范不变性成为量子电动力学和标准模型所有力的组织原理（第 8 阶段）。*

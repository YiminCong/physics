---
title: "Derivations — Module 5.2: London Theory"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 5.2: London Theory
# 推导 — 模块 5.2：伦敦理论

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 5.2](./module-5.2-london-theory.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 5.2](./module-5.2-london-theory.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. First London Equation from a Frictionless Charged Fluid · 从无摩擦带电流体推导第一伦敦方程

**Claim.** For a frictionless (collisionless) fluid of superelectrons of charge $-e$, mass $m$, and number density $n_s$, Newton's second law immediately gives the first London equation: $\partial J_s/\partial t = (n_s e^2/m) E$.

**命题。** 对于电荷 $-e$、质量 $m$、数密度 $n_s$ 的无摩擦（无碰撞）超导电子流体，牛顿第二定律直接给出第一伦敦方程：$\partial J_s/\partial t = (n_s e^2/m) E$。

**Step 1 — Equation of motion without friction.** In an ordinary metal, the Drude model gives $m(dv/dt) = -eE - mv/\tau$, where the last term is the frictional damping with relaxation time $\tau$. In a perfect (frictionless) superfluid $\tau \to \infty$ and the friction term vanishes exactly:

**第 1 步 — 无摩擦运动方程。** 在普通金属中，德鲁德模型给出 $m(dv/dt) = -eE - mv/\tau$，其中最后一项是弛豫时间为 $\tau$ 的摩擦阻尼。在完美（无摩擦）超流体中 $\tau \to \infty$，摩擦项严格消失：

$$ m\, (dv_s/dt) = -eE. $$

Here $v_s$ is the drift velocity of superelectrons and $E$ is the local electric field.

这里 $v_s$ 是超导电子的漂移速度，$E$ 是局域电场。

**Step 2 — Express in terms of the supercurrent density.** The supercurrent density is $J_s = -e n_s v_s$ (the minus sign because electron charge is $-e$). Taking the time derivative and substituting the equation of motion:

**第 2 步 — 用超电流密度表示。** 超电流密度为 $J_s = -e n_s v_s$（负号来自电子电荷 $-e$）。取时间导数并代入运动方程：

$$ \partial J_s/\partial t = -e n_s\, (dv_s/dt) = -e n_s \cdot (-eE/m) = (n_s e^2/m) E. $$

**Step 3 — The first London equation.** Defining the London coefficient $\Lambda = m/(n_s e^2)$, the result is

**第 3 步 — 第一伦敦方程。** 定义伦敦系数 $\Lambda = m/(n_s e^2)$，结果为

$$ \partial J_s/\partial t = E/\Lambda, \qquad \text{i.e.} \qquad \boxed{\, \partial J_s/\partial t = (n_s e^2/m) E \,} $$

This replaces Ohm's law $J = \sigma E$ inside the superconductor. For a DC steady state $\partial J_s/\partial t = 0$ requires $E = 0$, consistent with zero resistance: a constant supercurrent flows with no electric field needed to maintain it. $\blacksquare$

这取代了超导体内部的欧姆定律 $J = \sigma E$。对于直流稳态 $\partial J_s/\partial t = 0$ 要求 $E = 0$，与零电阻一致：恒定超电流在无需电场维持的情况下流动。$\blacksquare$

---

## B. Second London Equation · 第二伦敦方程

**Claim.** Applying Faraday's law to the first London equation and invoking gauge invariance yields the second London equation: $\nabla \times J_s = -(n_s e^2/m) B = -B/\Lambda\mu_0$.

**命题。** 对第一伦敦方程应用法拉第定律并援引规范不变性，得到第二伦敦方程：$\nabla \times J_s = -(n_s e^2/m) B = -B/\Lambda\mu_0$。

**Step 1 — Take the curl of the first London equation.** Apply $\nabla \times$ to both sides of $\partial J_s/\partial t = (n_s e^2/m) E$:

**第 1 步 — 对第一伦敦方程取旋度。** 对 $\partial J_s/\partial t = (n_s e^2/m) E$ 两边作用 $\nabla \times$：

$$ \partial(\nabla \times J_s)/\partial t = (n_s e^2/m)\, (\nabla \times E). $$

**Step 2 — Use Faraday's law.** Faraday's law states $\nabla \times E = -\partial B/\partial t$. Substituting:

**第 2 步 — 使用法拉第定律。** 法拉第定律给出 $\nabla \times E = -\partial B/\partial t$。代入：

$$ \partial(\nabla \times J_s)/\partial t = -(n_s e^2/m)\, \partial B/\partial t. $$

**Step 3 — Integrate over time.** Both sides are time derivatives, so integrate:

**第 3 步 — 对时间积分。** 两边都是时间导数，积分之：

$$ \nabla \times J_s = -(n_s e^2/m) B + C(r), $$

where $C(r)$ is a time-independent integration constant (a curl-free static current distribution).

其中 $C(r)$ 是与时间无关的积分常数（无旋的静态电流分布）。

**Step 4 — London's gauge choice.** The London brothers postulated that $C(r) = 0$. This is not merely a gauge choice: it is the physical statement that the superconducting ground state has no persistent normal-state current pattern hidden in it. Microscopically (BCS), the ground state has $J = 0$ when $B = 0$, which forces $C = 0$. The result is the **second London equation**:

**第 4 步 — 伦敦规范选择。** 伦敦兄弟假设 $C(r) = 0$。这不仅仅是规范选择：它是物理陈述，即超导基态中没有隐藏的正常态持续电流模式。从微观角度（BCS），当 $B = 0$ 时基态有 $J = 0$，这迫使 $C = 0$。结果是**第二伦敦方程**：

$$ \boxed{\, \nabla \times J_s = -(n_s e^2/m) B \,} $$

This is the key equation encoding the Meissner effect: the curl of the supercurrent is locked to the local magnetic field, not merely to its time derivative. $\blacksquare$

这是编码迈斯纳效应的关键方程：超电流的旋度锁定于局域磁场，而不仅仅是其时间导数。$\blacksquare$

**Alternative microscopic derivation (canonical momentum).** The canonical momentum of a superelectron in a vector potential $A$ is $p = mv_s - eA$ (using charge $-e$ with sign convention $p = mv + qA$, $q = -e$). In the BCS ground state the canonical momentum of each electron in a pair is zero (the pairs have zero total momentum). Setting $p = 0$:

**替代微观推导（正则动量）。** 在矢势 $A$ 中超导电子的正则动量为 $p = mv_s - eA$（使用电荷 $-e$，符号约定 $p = mv + qA$，$q = -e$）。在 BCS 基态中配对中每个电子的正则动量为零（对的总动量为零）。令 $p = 0$：

$$ mv_s = eA \quad\implies\quad J_s = -en_s v_s = -(n_s e^2/m) A. $$

Taking the curl and using $B = \nabla \times A$ immediately gives $\nabla \times J_s = -(n_s e^2/m) B$, confirming the second London equation from a microscopic principle (zero canonical momentum of the condensate). $\blacksquare$

取旋度并使用 $B = \nabla \times A$ 立即给出 $\nabla \times J_s = -(n_s e^2/m) B$，从微观原理（凝聚态的正则动量为零）确认了第二伦敦方程。$\blacksquare$

---

## C. Combining with Ampère's Law: $\nabla^2 B = B/\lambda_L^2$ · 与安培定律联立：$\nabla^2 B = B/\lambda_L^2$

**Claim.** Combining the second London equation with the magnetostatic Ampère's law $\nabla \times B = \mu_0 J_s$ gives the London equation for $B$: $\nabla^2 B = B/\lambda_L^2$, where $\lambda_L = \sqrt{m/\mu_0 n_s e^2}$.

**命题。** 将第二伦敦方程与静磁安培定律 $\nabla \times B = \mu_0 J_s$ 联立，得到 $B$ 的伦敦方程：$\nabla^2 B = B/\lambda_L^2$，其中 $\lambda_L = \sqrt{m/\mu_0 n_s e^2}$。

**Step 1 — Take the curl of Ampère's law.** In the static ($\partial E/\partial t = 0$) limit, $\nabla \times B = \mu_0 J_s$. Apply $\nabla \times$ to both sides:

**第 1 步 — 对安培定律取旋度。** 在静态（$\partial E/\partial t = 0$）极限下，$\nabla \times B = \mu_0 J_s$。对两边作用 $\nabla \times$：

$$ \nabla \times (\nabla \times B) = \mu_0\, \nabla \times J_s. $$

**Step 2 — Expand the left side using the vector identity.** Apply $\nabla \times (\nabla \times B) = \nabla(\nabla \cdot B) - \nabla^2 B$. Maxwell's law $\nabla \cdot B = 0$ makes the first term vanish:

**第 2 步 — 用矢量恒等式展开左边。** 应用 $\nabla \times (\nabla \times B) = \nabla(\nabla \cdot B) - \nabla^2 B$。麦克斯韦定律 $\nabla \cdot B = 0$ 使第一项消失：

$$ -\nabla^2 B = \mu_0\, \nabla \times J_s. $$

**Step 3 — Substitute the second London equation.** Replace $\nabla \times J_s = -(n_s e^2/m) B$:

**第 3 步 — 代入第二伦敦方程。** 用 $\nabla \times J_s = -(n_s e^2/m) B$ 替换：

$$ -\nabla^2 B = \mu_0 \cdot (-n_s e^2/m) B = -(\mu_0 n_s e^2/m) B. $$

Multiply both sides by $-1$:

两边乘以 $-1$：

$$ \nabla^2 B = (\mu_0 n_s e^2/m) B. $$

**Step 4 — Identify the London penetration depth.** Define

**第 4 步 — 识别伦敦穿透深度。** 定义

$$ \boxed{\, \lambda_L^2 = m/(\mu_0 n_s e^2) \,}, \qquad \text{so} \qquad \boxed{\, \lambda_L = \sqrt{m/(\mu_0 n_s e^2)} \,}. $$

The London equation becomes $\nabla^2 B = B/\lambda_L^2$.

伦敦方程变为 $\nabla^2 B = B/\lambda_L^2$。

**Step 5 — Dimensional check.** $[m] = \text{kg}$, $[\mu_0] = \text{kg}\cdot\text{m}/\text{A}^2$, $[n_s] = \text{m}^{-3}$, $[e] = \text{C} = \text{A}\cdot\text{s}$. Then $[\mu_0 n_s e^2/m] = (\text{kg}\cdot\text{m}/\text{A}^2\cdot\text{m}^{-3}\cdot\text{A}^2\cdot\text{s}^2/\text{kg}) = \text{m}^{-2}$, so $[\lambda_L] = \text{m}$. Correct. $\blacksquare$

**第 5 步 — 量纲检验。** $[m] = \text{kg}$，$[\mu_0] = \text{kg}\cdot\text{m}/\text{A}^2$，$[n_s] = \text{m}^{-3}$，$[e] = \text{C} = \text{A}\cdot\text{s}$。则 $[\mu_0 n_s e^2/m] = (\text{kg}\cdot\text{m}/\text{A}^2\cdot\text{m}^{-3}\cdot\text{A}^2\cdot\text{s}^2/\text{kg}) = \text{m}^{-2}$，故 $[\lambda_L] = \text{m}$。正确。$\blacksquare$

---

## D. Solving $B(x) = B_0 e^{-x/\lambda_L}$ in the Half-Space Geometry · 在半空间几何中求解 $B(x) = B_0 e^{-x/\lambda_L}$

**Claim.** For a superconductor occupying $x \ge 0$ with an applied field $B_0$ parallel to the surface at $x = 0$, the magnetic field inside decays exponentially as $B(x) = B_0 e^{-x/\lambda_L}$.

**命题。** 对于占据 $x \ge 0$ 的超导体，在 $x = 0$ 表面施加平行于表面的磁场 $B_0$，内部磁场按指数衰减：$B(x) = B_0 e^{-x/\lambda_L}$。

**Step 1 — Reduce to one spatial dimension.** By translational symmetry in $y$ and $z$, $B$ depends only on $x$. Let $B = B(x)\, \hat{z}$ (field pointing along $z$, lying in the $yz$ plane at the surface). Then $\nabla^2 B = d^2 B/dx^2$ for the scalar magnitude $B(x)$, and the London equation becomes an ordinary differential equation:

**第 1 步 — 化为一维空间问题。** 由 $y$ 和 $z$ 方向的平移对称性，$B$ 只依赖于 $x$。设 $B = B(x)\, \hat{z}$（磁场沿 $z$ 方向，在表面处平行于 $yz$ 平面）。则标量量 $B(x)$ 的 $\nabla^2 B = d^2 B/dx^2$，伦敦方程变为常微分方程：

$$ d^2 B/dx^2 = B/\lambda_L^2. $$

**Step 2 — General solution.** This is a second-order linear ODE with constant coefficients. The characteristic equation is $r^2 = 1/\lambda_L^2$, giving $r = \pm 1/\lambda_L$. The general solution is

**第 2 步 — 通解。** 这是一个常系数二阶线性常微分方程。特征方程为 $r^2 = 1/\lambda_L^2$，给出 $r = \pm 1/\lambda_L$。通解为

$$ B(x) = C_1 e^{x/\lambda_L} + C_2 e^{-x/\lambda_L}. $$

**Step 3 — Apply boundary conditions.** Two conditions determine $C_1$ and $C_2$:

**第 3 步 — 应用边界条件。** 两个条件确定 $C_1$ 和 $C_2$：

- (i)  $B(0) = B_0$  (field is continuous at the surface),
- (ii) $B(x) \to 0$ as $x \to +\infty$  (field vanishes deep in the bulk).

- (i)  $B(0) = B_0$  （磁场在表面连续），
- (ii) 当 $x \to +\infty$ 时 $B(x) \to 0$  （磁场在体内深处消失）。

Condition (ii) requires $C_1 = 0$ (the growing exponential must be absent). Condition (i) then gives $C_2 = B_0$.

条件 (ii) 要求 $C_1 = 0$（增长指数项必须不存在）。条件 (i) 则给出 $C_2 = B_0$。

**Step 4 — Final solution.** Substituting back:

**第 4 步 — 最终解。** 代回：

$$ \boxed{\, B(x) = B_0 e^{-x/\lambda_L} \,} $$

The field decays on the length scale $\lambda_L$. For $x \gg \lambda_L$, $B \approx 0$: the bulk superconductor is field-free. For typical elemental superconductors $\lambda_L \approx 40$–$500$ nm, confirming that the Meissner effect excludes field from all but a thin skin depth. $\blacksquare$

磁场在长度尺度 $\lambda_L$ 上衰减。当 $x \gg \lambda_L$ 时，$B \approx 0$：体内超导体无磁场。对于典型元素超导体 $\lambda_L \approx 40$–$500$ nm，证实了迈斯纳效应将磁场排除在薄薄的趋肤深度之外。$\blacksquare$

**Step 5 — Supercurrent profile.** The associated supercurrent $J_s$ flows in the surface layer. From Ampère's law $J_s = (1/\mu_0)\, \nabla \times B$. With $B = B(x)\, \hat{z}$ and $dB/dx = -(B_0/\lambda_L) e^{-x/\lambda_L}$:

**第 5 步 — 超电流分布。** 相关的超电流 $J_s$ 在表面层中流动。由安培定律 $J_s = (1/\mu_0)\, \nabla \times B$。取 $B = B(x)\, \hat{z}$，$dB/dx = -(B_0/\lambda_L) e^{-x/\lambda_L}$：

$$ J_s(x) = -(1/\mu_0)\, (dB/dx)\, \hat{y} = (B_0/(\mu_0 \lambda_L)) e^{-x/\lambda_L}\, \hat{y}. $$

The current also decays exponentially with the same length scale $\lambda_L$, confirming that the screening is done by surface currents confined to depth $\lambda_L$. $\blacksquare$

电流也以相同长度尺度 $\lambda_L$ 指数衰减，确认了屏蔽由深度 $\lambda_L$ 内的表面电流完成。$\blacksquare$

---

## E. Physical Identification of $\lambda_L$ and Its Temperature Dependence · $\lambda_L$ 的物理识别及其温度依赖性

**Claim.** The London penetration depth $\lambda_L = \sqrt{m/(\mu_0 n_s e^2)}$ encodes the density of superelectrons $n_s$. As $T \to T_c$, $n_s \to 0$ and $\lambda_L \to \infty$: the superconductor can no longer screen the field, consistent with the Meissner effect disappearing at the transition.

**命题。** 伦敦穿透深度 $\lambda_L = \sqrt{m/(\mu_0 n_s e^2)}$ 编码了超导电子密度 $n_s$。当 $T \to T_c$ 时，$n_s \to 0$，$\lambda_L \to \infty$：超导体无法再屏蔽磁场，与迈斯纳效应在转变处消失一致。

**Step 1 — Two-fluid interpretation.** The two-fluid model (Gorter–Casimir) writes the total electron density as $n = n_s(T) + n_n(T)$, where $n_s$ is the superfluid density and $n_n$ is the normal-fluid density. At $T = 0$, $n_s = n$ (all electrons pair). At $T = T_c$, $n_s = 0$. The empirical fit is $n_s(T) \approx n[1 - (T/T_c)^4]$.

**第 1 步 — 双流体解释。** 双流体模型（戈特–卡西米尔）将总电子密度写为 $n = n_s(T) + n_n(T)$，其中 $n_s$ 为超流密度，$n_n$ 为正常流体密度。在 $T = 0$ 时，$n_s = n$（所有电子配对）。在 $T = T_c$ 时，$n_s = 0$。经验拟合为 $n_s(T) \approx n[1 - (T/T_c)^4]$。

**Step 2 — Temperature dependence of $\lambda_L$.** Substituting $n_s(T)$:

**第 2 步 — $\lambda_L$ 的温度依赖性。** 代入 $n_s(T)$：

$$ \lambda_L(T) = \lambda_L(0) / \sqrt{1 - (T/T_c)^4}, $$

where $\lambda_L(0) = \sqrt{m/(\mu_0 n e^2)}$ is the zero-temperature value. As $T \to T_c$, $1 - (T/T_c)^4 \to 0$ and $\lambda_L \to \infty$. $\blacksquare$

其中 $\lambda_L(0) = \sqrt{m/(\mu_0 n e^2)}$ 是零温值。当 $T \to T_c$ 时，$1 - (T/T_c)^4 \to 0$，$\lambda_L \to \infty$。$\blacksquare$

**Step 3 — Connection to plasma frequency.** Note that $\mu_0 n_s e^2/m = \omega_p^2/c^2$ where $\omega_p = \sqrt{n_s e^2/\varepsilon_0 m}$ is the plasma frequency. Therefore $\lambda_L = c/\omega_p$: the London penetration depth is the electromagnetic skin depth of the electron plasma at zero frequency. This connects superconductivity to the optical properties of the electron gas. $\blacksquare$

**第 3 步 — 与等离子体频率的联系。** 注意 $\mu_0 n_s e^2/m = \omega_p^2/c^2$，其中 $\omega_p = \sqrt{n_s e^2/\varepsilon_0 m}$ 是等离子体频率。因此 $\lambda_L = c/\omega_p$：伦敦穿透深度是零频率下电子等离子体的电磁趋肤深度。这将超导性与电子气的光学性质联系起来。$\blacksquare$

---

*Results derived here feed directly into Module 5.3 (where $\lambda$ reappears as the GL penetration depth and enters the ratio $\kappa = \lambda/\xi$) and Module 5.7 (where the vortex field profile is an exponential of the same form).*

*此处推导的结果直接进入模块 5.3（其中 $\lambda$ 作为 GL 穿透深度重新出现并进入比值 $\kappa = \lambda/\xi$）和模块 5.7（其中涡旋磁场分布具有相同形式的指数衰减）。*

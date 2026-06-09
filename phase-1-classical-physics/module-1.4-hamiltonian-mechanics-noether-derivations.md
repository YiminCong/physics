---
title: "Derivations — Module 1.4: Hamiltonian Mechanics & Noether's Theorem"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 1.4: Hamiltonian Mechanics & Noether's Theorem
# 推导 — 模块 1.4：哈密顿力学与诺特定理

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.4](./module-1.4-hamiltonian-mechanics-noether.md). Full step-by-step proofs of every result quoted there. English first, then 中文.
> [模块 1.4](./module-1.4-hamiltonian-mechanics-noether.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Legendre Transform and Hamilton's Equations · 勒让德变换与哈密顿方程

**Claim.** Starting from the Lagrangian $L(q, \dot{q}, t)$, define the conjugate momentum $p = \partial L/\partial \dot{q}$ and the Hamiltonian $H(q, p, t) = p\dot{q} - L$ (Legendre transform). Then Hamilton's equations hold:

$$ \dot{q} = \frac{\partial H}{\partial p}, \qquad \dot{p} = -\frac{\partial H}{\partial q}. $$

(Single degree of freedom for clarity; $N$-dimensional case follows by index repetition.)

**命题。** 从拉格朗日量 $L(q, \dot{q}, t)$ 出发，定义共轭动量 $p = \partial L/\partial \dot{q}$ 和哈密顿量 $H(q, p, t) = p\dot{q} - L$（勒让德变换）。则哈密顿方程成立：

$$ \dot{q} = \frac{\partial H}{\partial p}, \qquad \dot{p} = -\frac{\partial H}{\partial q}. $$

（为清晰起见处理单自由度；$N$ 维情形通过指标重复得到。）

**Step 1 — Compute the total differential of $H$.** Since $H = p\dot{q} - L$:

**第 1 步 — 计算 $H$ 的全微分。** 由于 $H = p\dot{q} - L$：

$$ dH = \dot{q}\,dp + p\,d\dot{q} - \Big(\frac{\partial L}{\partial q}\,dq + \frac{\partial L}{\partial \dot{q}}\,d\dot{q} + \frac{\partial L}{\partial t}\,dt\Big). $$

**Step 2 — Use the definition of $p$.** Since $p = \partial L/\partial \dot{q}$, the terms $p\,d\dot{q}$ and $-(\partial L/\partial \dot{q})\,d\dot{q}$ cancel exactly:

**第 2 步 — 利用 $p$ 的定义。** 由于 $p = \partial L/\partial \dot{q}$，项 $p\,d\dot{q}$ 与 $-(\partial L/\partial \dot{q})\,d\dot{q}$ 恰好相消：

$$ p\,d\dot{q} - \frac{\partial L}{\partial \dot{q}}\,d\dot{q} = p\,d\dot{q} - p\,d\dot{q} = 0. $$

Therefore:

因此：

$$ dH = \dot{q}\,dp - \frac{\partial L}{\partial q}\,dq - \frac{\partial L}{\partial t}\,dt. $$

**Step 3 — Read off the partial derivatives of $H$.** Comparing with the general expression $dH = (\partial H/\partial p)\,dp + (\partial H/\partial q)\,dq + (\partial H/\partial t)\,dt$:

**第 3 步 — 读出 $H$ 的偏导数。** 与一般表达式 $dH = (\partial H/\partial p)\,dp + (\partial H/\partial q)\,dq + (\partial H/\partial t)\,dt$ 比较：

$$ \frac{\partial H}{\partial p} = \dot{q}, \qquad \frac{\partial H}{\partial q} = -\frac{\partial L}{\partial q}. $$

The first equation gives the first Hamilton equation: $\boxed{\,\dot{q} = \partial H/\partial p\,}$ $\blacksquare_1$

第一式给出第一个哈密顿方程：$\boxed{\,\dot{q} = \partial H/\partial p\,}$ $\blacksquare_1$

**Step 4 — Apply the Euler–Lagrange equation to get the second Hamilton equation.** From the Euler–Lagrange equation (proved in Module 1.3 derivations):

**第 4 步 — 应用欧拉–拉格朗日方程得第二个哈密顿方程。** 由欧拉–拉格朗日方程（在模块 1.3 推导中证明）：

$$ \frac{d}{dt}\Big(\frac{\partial L}{\partial \dot{q}}\Big) = \frac{\partial L}{\partial q} \quad\implies\quad \dot{p} = \frac{\partial L}{\partial q}. $$

Substituting Step 3's result $\partial H/\partial q = -\partial L/\partial q$:

代入第 3 步的结果 $\partial H/\partial q = -\partial L/\partial q$：

$$ \boxed{\, \dot{p} = \frac{\partial L}{\partial q} = -\frac{\partial H}{\partial q} \,} \qquad \blacksquare_2 $$

**Remark — $H$ equals $T + V$.** For a standard mechanical system with $L = T(\dot{q}) - V(q)$, the conjugate momentum is $p = \partial T/\partial \dot{q}$. Then $H = p\dot{q} - L = p\dot{q} - T + V$. If $T$ is quadratic in $\dot{q}$ ($T = \tfrac12 m\dot{q}^2$), then $p\dot{q} = m\dot{q} \cdot \dot{q} = 2T$ by Euler's theorem on homogeneous functions. Therefore $H = 2T - T + V = T + V = $ total energy.

**注——$H$ 等于 $T + V$。** 对于标准力学系统 $L = T(\dot{q}) - V(q)$，共轭动量 $p = \partial T/\partial \dot{q}$。则 $H = p\dot{q} - L = p\dot{q} - T + V$。若 $T$ 关于 $\dot{q}$ 是二次型（$T = \tfrac12 m\dot{q}^2$），由欧拉关于齐次函数的定理得 $p\dot{q} = m\dot{q} \cdot \dot{q} = 2T$。因此 $H = 2T - T + V = T + V = $ 总能量。

---

## B. Poisson Brackets and the Fundamental Bracket $\{q, p\} = 1$ · 泊松括号与基本括号 $\{q, p\} = 1$

**Claim.** The Poisson bracket of two functions $f(q, p)$ and $g(q, p)$ is defined as:

$$ \{f, g\} = \frac{\partial f}{\partial q}\frac{\partial g}{\partial p} - \frac{\partial f}{\partial p}\frac{\partial g}{\partial q}. $$

For canonical coordinates and momenta, $\{q, p\} = 1$.

**命题。** 两个函数 $f(q, p)$ 和 $g(q, p)$ 的泊松括号定义为：

$$ \{f, g\} = \frac{\partial f}{\partial q}\frac{\partial g}{\partial p} - \frac{\partial f}{\partial p}\frac{\partial g}{\partial q}. $$

对于正则坐标和动量，$\{q, p\} = 1$。

**Proof.** Set $f = q$ and $g = p$. Then:

**证明。** 令 $f = q$，$g = p$，则：

$$ \frac{\partial q}{\partial q} = 1, \quad \frac{\partial q}{\partial p} = 0, \quad \frac{\partial p}{\partial q} = 0, \quad \frac{\partial p}{\partial p} = 1. $$

Therefore $\{q, p\} = (1)(1) - (0)(0) = 1$. $\blacksquare$

因此 $\{q, p\} = (1)(1) - (0)(0) = 1$。$\blacksquare$

**Hamilton's equation in Poisson-bracket form.** For any observable $f(q, p, t)$:

**泊松括号形式的哈密顿方程。** 对任意可观测量 $f(q, p, t)$：

$$ \begin{aligned}
\frac{df}{dt} &= \frac{\partial f}{\partial q}\dot{q} + \frac{\partial f}{\partial p}\dot{p} + \frac{\partial f}{\partial t} \\
&= \frac{\partial f}{\partial q}\frac{\partial H}{\partial p} - \frac{\partial f}{\partial p}\frac{\partial H}{\partial q} + \frac{\partial f}{\partial t} \\
&= \{f, H\} + \frac{\partial f}{\partial t}.
\end{aligned} $$

In particular: $\dot{q} = \{q, H\}$ (using $\{q, H\} = \partial H/\partial p = \dot{q}$ from Hamilton's equations) and $\dot{p} = \{p, H\} = -\partial H/\partial q = \dot{p}$, both consistent.

特别地：$\dot{q} = \{q, H\}$（由 $\{q, H\} = \partial H/\partial p = \dot{q}$，与哈密顿方程一致）；$\dot{p} = \{p, H\} = -\partial H/\partial q$，同样一致。

---

## C. Noether's Theorem — Full Proof · 诺特定理——完整证明

**Claim.** If the Lagrangian $L(q, \dot{q}, t)$ is invariant (to first order in $\varepsilon$) under the one-parameter family of transformations $q \to q + \varepsilon K(q, t)$, where $K$ is a smooth generator, then the quantity

$$ Q = \frac{\partial L}{\partial \dot{q}}\,K $$

is conserved along any solution of the Euler–Lagrange equations: $dQ/dt = 0$.

**命题。** 若拉格朗日量 $L(q, \dot{q}, t)$ 在单参数变换族 $q \to q + \varepsilon K(q, t)$（$K$ 为光滑生成元）下（对 $\varepsilon$ 一阶）不变，则量

$$ Q = \frac{\partial L}{\partial \dot{q}}\,K $$

沿欧拉–拉格朗日方程的任意解守恒：$dQ/dt = 0$。

**Step 1 — Express the invariance condition.** Under $q \to q + \varepsilon K$, the velocity transforms as $\dot{q} \to \dot{q} + \varepsilon \dot{K}$ (where $\dot{K} = dK/dt$ along the motion). The first-order change in $L$ is:

**第 1 步 — 表达不变性条件。** 在 $q \to q + \varepsilon K$ 下，速度变换为 $\dot{q} \to \dot{q} + \varepsilon \dot{K}$（其中 $\dot{K} = dK/dt$ 沿运动方向）。$L$ 的一阶变化为：

$$ \delta L = \frac{\partial L}{\partial q}\,\varepsilon K + \frac{\partial L}{\partial \dot{q}}\,\varepsilon \dot{K} = 0. $$

Dividing by $\varepsilon$, the invariance condition is:

除以 $\varepsilon$，不变性条件为：

$$ \frac{\partial L}{\partial q}\,K + \frac{\partial L}{\partial \dot{q}}\,\dot{K} = 0. \qquad (*) $$

**Step 2 — Use the Euler–Lagrange equation.** On the physical trajectory, the E-L equation holds:

**第 2 步 — 利用欧拉–拉格朗日方程。** 在物理轨迹上，欧拉–拉格朗日方程成立：

$$ \frac{\partial L}{\partial q} = \frac{d}{dt}\Big(\frac{\partial L}{\partial \dot{q}}\Big). $$

Substitute into $(*)$:

代入 $(*)$：

$$ \frac{d}{dt}\Big(\frac{\partial L}{\partial \dot{q}}\Big)\cdot K + \frac{\partial L}{\partial \dot{q}}\cdot \dot{K} = 0. $$

**Step 3 — Recognise the product rule.** The left side is exactly the time derivative of the product $(\partial L/\partial \dot{q})\,K$:

**第 3 步 — 识别乘积法则。** 左侧恰好是乘积 $(\partial L/\partial \dot{q})\,K$ 的时间导数：

$$ \frac{d}{dt}\Big[\frac{\partial L}{\partial \dot{q}}\,K\Big] = \frac{d}{dt}\Big(\frac{\partial L}{\partial \dot{q}}\Big)\cdot K + \frac{\partial L}{\partial \dot{q}}\cdot \dot{K} = 0. $$

Therefore:

因此：

$$ \frac{dQ}{dt} = \frac{d}{dt}\Big[\frac{\partial L}{\partial \dot{q}}\,K\Big] = 0, \quad\text{i.e.}\quad \boxed{\, Q = \frac{\partial L}{\partial \dot{q}}\,K = \text{const} \,} \qquad \blacksquare $$

---

## D. Three Canonical Applications of Noether's Theorem · 诺特定理的三个典型应用

### D.1 Time Translation $\to$ Energy Conservation · 时间平移 $\to$ 能量守恒

**Step 1 — Identify the symmetry.** If $L$ has no explicit time dependence ($\partial L/\partial t = 0$), then $L$ is invariant under $t \to t + \varepsilon$, which induces $q(t) \to q(t + \varepsilon) \approx q(t) + \varepsilon \dot{q}(t)$. So the generator is $K = \dot{q}$.

**第 1 步 — 辨识对称性。** 若 $L$ 不显含时间（$\partial L/\partial t = 0$），则 $L$ 在 $t \to t + \varepsilon$ 下不变，这诱导 $q(t) \to q(t + \varepsilon) \approx q(t) + \varepsilon \dot{q}(t)$。故生成元为 $K = \dot{q}$。

**Step 2 — Compute the Noether charge.** A time translation $t \to t + \varepsilon$ also moves the *independent* variable (not just the coordinates), so the conserved charge carries an extra $-L$ term relative to the coordinate-transformation formula of Section C: $Q = (\partial L/\partial \dot{q})\,\dot{q} - L = p\dot{q} - L$.

**第 2 步 — 计算诺特荷。** 时间平移 $t \to t + \varepsilon$ 还移动了*自变量*（而不只是坐标），故守恒荷相对 C 节的坐标变换公式多出一个 $-L$ 项：$Q = (\partial L/\partial \dot{q})\,\dot{q} - L = p\dot{q} - L$。

**Step 3 — Show $Q = H$.** For $L = T - V$ with $T = \tfrac12 m\dot{q}^2$:

**第 3 步 — 证明 $Q = H$。** 对于 $L = T - V$，$T = \tfrac12 m\dot{q}^2$：

$$ Q = p\dot{q} - L = m\dot{q}^2 - (T - V) = 2T - (T - V) = T + V = H, $$

where $p\dot{q} = m\dot{q}^2 = 2T$ by Euler's theorem on the homogeneous quadratic $T$.

More generally, $Q = \sum_i (\partial L/\partial \dot{q}_i)\,\dot{q}_i - L = H$ by the Legendre transform. Therefore time-translation symmetry conserves $\boxed{\,H = \text{total energy}\,}$ $\blacksquare$

更一般地，$Q = \sum_i (\partial L/\partial \dot{q}_i)\,\dot{q}_i - L = H$（由勒让德变换）。因此时间平移对称性守恒 $\boxed{\,H = \text{总能量}\,}$ $\blacksquare$

### D.2 Spatial Translation $\to$ Linear Momentum Conservation · 空间平移 $\to$ 线动量守恒

**Step 1 — Identify the symmetry.** For a free particle (or a system whose potential depends only on relative positions), $L$ is invariant under the uniform translation $\mathbf{q} \to \mathbf{q} + \varepsilon \hat{\mathbf{n}}$ (translation by $\varepsilon$ in direction $\hat{\mathbf{n}}$). The generator is $K = \hat{\mathbf{n}}$.

**第 1 步 — 辨识对称性。** 对于自由粒子（或势能仅依赖相对位置的系统），$L$ 在匀速平移 $\mathbf{q} \to \mathbf{q} + \varepsilon \hat{\mathbf{n}}$ 下不变（沿方向 $\hat{\mathbf{n}}$ 平移 $\varepsilon$）。生成元为 $K = \hat{\mathbf{n}}$。

**Step 2 — Compute the Noether charge.** $Q = (\partial L/\partial \dot{\mathbf{q}}) \cdot \hat{\mathbf{n}}$. With $\mathbf{p} = \partial L/\partial \dot{\mathbf{q}} = m\dot{\mathbf{q}}$ (Cartesian), $Q = \mathbf{p} \cdot \hat{\mathbf{n}} = $ the component of momentum along $\hat{\mathbf{n}}$.

**第 2 步 — 计算诺特荷。** $Q = (\partial L/\partial \dot{\mathbf{q}}) \cdot \hat{\mathbf{n}}$。以 $\mathbf{p} = \partial L/\partial \dot{\mathbf{q}} = m\dot{\mathbf{q}}$（笛卡尔），$Q = \mathbf{p} \cdot \hat{\mathbf{n}} = $ 动量沿 $\hat{\mathbf{n}}$ 方向的分量。

**Step 3 — Conclude.** Since $\hat{\mathbf{n}}$ is arbitrary, the full momentum vector $\boxed{\,\mathbf{p}\text{ is conserved}\,}$ whenever $L$ is invariant under all spatial translations. $\blacksquare$

**第 3 步 — 得出结论。** 由于 $\hat{\mathbf{n}}$ 是任意的，只要 $L$ 在所有空间平移下不变，完整动量矢量 $\boxed{\,\mathbf{p}\text{ 守恒}\,}$。$\blacksquare$

### D.3 Rotation $\to$ Angular Momentum Conservation · 旋转 $\to$ 角动量守恒

**Step 1 — Identify the symmetry.** For a particle in a central potential, $L$ is invariant under rotations about any axis $\hat{\mathbf{n}}$. An infinitesimal rotation by $\varepsilon$ about $\hat{\mathbf{n}}$ produces $\delta\mathbf{r} = \varepsilon\,\hat{\mathbf{n}} \times \mathbf{r}$. So $K = \hat{\mathbf{n}} \times \mathbf{r}$.

**第 1 步 — 辨识对称性。** 对于有心势中的粒子，$L$ 在绕任意轴 $\hat{\mathbf{n}}$ 的转动下不变。绕 $\hat{\mathbf{n}}$ 转过无穷小角度 $\varepsilon$ 产生 $\delta\mathbf{r} = \varepsilon\,\hat{\mathbf{n}} \times \mathbf{r}$。故 $K = \hat{\mathbf{n}} \times \mathbf{r}$。

**Step 2 — Compute the Noether charge.** With $\mathbf{p} = \partial L/\partial \dot{\mathbf{q}} = m\dot{\mathbf{r}}$ (for Cartesian $L = T - V$):

**第 2 步 — 计算诺特荷。** 以 $\mathbf{p} = \partial L/\partial \dot{\mathbf{q}} = m\dot{\mathbf{r}}$（笛卡尔 $L = T - V$）：

$$ Q = \mathbf{p} \cdot K = \mathbf{p} \cdot (\hat{\mathbf{n}} \times \mathbf{r}) = \hat{\mathbf{n}} \cdot (\mathbf{r} \times \mathbf{p}) = \hat{\mathbf{n}} \cdot \mathbf{L}. $$

(Using the scalar triple product identity $\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c}) = \mathbf{b} \cdot (\mathbf{c} \times \mathbf{a}) = \mathbf{c} \cdot (\mathbf{a} \times \mathbf{b})$.)

（利用标量三重积恒等式 $\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c}) = \mathbf{b} \cdot (\mathbf{c} \times \mathbf{a}) = \mathbf{c} \cdot (\mathbf{a} \times \mathbf{b})$。）

**Step 3 — Conclude.** Since $\hat{\mathbf{n}}$ is arbitrary, conservation of $Q$ for all $\hat{\mathbf{n}}$ means the full $\boxed{\,\text{angular momentum vector }\mathbf{L} = \mathbf{r} \times \mathbf{p}\text{ is conserved}\,}$ whenever $L$ is rotationally invariant. $\blacksquare$

**第 3 步 — 得出结论。** 由于 $\hat{\mathbf{n}}$ 是任意的，对所有 $\hat{\mathbf{n}}$ 的 $Q$ 守恒意味着只要 $L$ 在旋转下不变，完整 $\boxed{\,\text{角动量矢量 }\mathbf{L} = \mathbf{r} \times \mathbf{p}\text{ 守恒}\,}$。$\blacksquare$

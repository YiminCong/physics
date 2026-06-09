---
title: "Module 1.5 — Central-Force Problem & Kepler"
parent: "Phase 1 — Classical Physics"
nav_order: 5
---

# Module 1.5 — Central-Force Problem & Kepler
**模块 1.5 — 有心力问题与开普勒定律**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.5-central-force-kepler-derivations.md)

---

## 1. Reduction to a One-Dimensional Problem · 化为一维问题

**Definition.** A **central force** depends only on the separation $r = |\mathbf{r}_1 - \mathbf{r}_2|$ and points along the line joining two bodies: $\mathbf{F} = F(r)\,\hat{r}$. Introducing the **reduced mass** $\mu = m_1 m_2/(m_1 + m_2)$, the two-body problem reduces to the one-body problem of a particle of mass $\mu$ in the potential $V(r)$. Since $\mathbf{F}$ is central, angular momentum $L = \mu r^2\dot{\phi}$ is conserved (Noether, Module 1.4), and motion is confined to a plane. Writing the total energy in polar coordinates and eliminating $\dot{\phi}$ via $L$ introduces the **effective potential**:

**定义。** **有心力**仅依赖于两体间距 $r = |\mathbf{r}_1 - \mathbf{r}_2|$，方向沿连线：$\mathbf{F} = F(r)\,\hat{r}$。引入**约化质量** $\mu = m_1 m_2/(m_1 + m_2)$，二体问题化为质量为 $\mu$ 的粒子在势 $V(r)$ 中的单体问题。由于 $\mathbf{F}$ 是有心力，角动量 $L = \mu r^2\dot{\phi}$ 守恒（诺特定理，模块 1.4），运动被限制在一个平面内。用极坐标写出总能量并通过 $L$ 消去 $\dot{\phi}$，引入**有效势**：

$$ V_\text{eff}(r) = V(r) + \frac{L^2}{2\mu r^2}. $$

The second term is the centrifugal barrier. Radial motion satisfies $\tfrac12 \mu\dot{r}^2 + V_\text{eff}(r) = E$, a one-dimensional energy equation. Turning points ($\dot{r} = 0$) occur where $E = V_\text{eff}(r)$.

第二项是离心势垒。径向运动满足 $\tfrac12 \mu\dot{r}^2 + V_\text{eff}(r) = E$，这是一个一维能量方程。转折点（$\dot{r} = 0$）出现在 $E = V_\text{eff}(r)$ 处。

**Demonstration.** For gravity $V(r) = -Gm_1 m_2/r$, the effective potential has a minimum (stable circular orbit) at $r_0 = L^2/(G\mu^2 m_\text{total})$. Integrating the orbit equation $d^2 u/d\phi^2 + u = -\mu/(L^2) \cdot F(1/u)$ (where $u = 1/r$) for the $1/r$ force gives a conic section: $r = p/(1 + \varepsilon\cos\phi)$, where $p = L^2/(G\mu^2 m_\text{total})$ is the semi-latus rectum and $\varepsilon$ is the eccentricity. Ellipses ($\varepsilon < 1$), parabolas ($\varepsilon = 1$), and hyperbolas ($\varepsilon > 1$) correspond to $E < 0$, $E = 0$, $E > 0$.

**演示。** 对于引力 $V(r) = -Gm_1 m_2/r$，有效势在 $r_0 = L^2/(G\mu^2 m_\text{total})$ 处有极小值（稳定圆轨道）。对 $1/r$ 力积分轨道方程 $d^2 u/d\phi^2 + u = -\mu/(L^2) \cdot F(1/u)$（其中 $u = 1/r$），得到圆锥曲线：$r = p/(1 + \varepsilon\cos\phi)$，其中 $p = L^2/(G\mu^2 m_\text{total})$ 为半通径，$\varepsilon$ 为离心率。椭圆（$\varepsilon < 1$）、抛物线（$\varepsilon = 1$）和双曲线（$\varepsilon > 1$）分别对应 $E < 0$、$E = 0$、$E > 0$。

**Application.** Kepler's three laws follow directly. (1) Orbits are ellipses with the Sun at one focus ($\varepsilon < 1$ solutions). (2) Equal areas in equal times — this is simply conservation of $L$: $dA/dt = L/(2\mu) = \text{const}$. (3) $T^2 \propto a^3$, where $a$ is the semi-major axis, follows from integrating the period using the ellipse geometry.

**应用。** 开普勒三定律直接得出。(1) 轨道为以太阳为焦点的椭圆（$\varepsilon < 1$ 解）。(2) 等面积定律——这就是 $L$ 守恒：$dA/dt = L/(2\mu) = \text{常数}$。(3) $T^2 \propto a^3$，其中 $a$ 为半长轴，由用椭圆几何积分周期得出。

## 2. Connection to the Quantum Hydrogen Atom · 与量子氢原子的联系

**Definition.** The quantum version of the central-force problem replaces the classical orbit with the Schrödinger equation in spherical symmetry. The $-k/r$ potential of the hydrogen atom ($k = e^2/4\pi\varepsilon_0$) is the quantum analogue of the gravitational $-Gm_1 m_2/r$, with $L$ replaced by the quantum number $\ell$ and the discrete energy levels $E_n = -13.6\,\text{eV}/n^2$.

**定义。** 有心力问题的量子版本用球对称中的薛定谔方程取代了经典轨道。氢原子的 $-k/r$ 势（$k = e^2/4\pi\varepsilon_0$）是引力 $-Gm_1 m_2/r$ 的量子对应，$L$ 被量子数 $\ell$ 取代，能级变为离散值 $E_n = -13.6\,\text{eV}/n^2$。

**Application.** The classical analysis here — reduction by angular-momentum conservation, effective potential, energy classification of orbits — maps directly onto the quantum treatment of the hydrogen atom (Module 3.4). Understanding Kepler's problem in classical terms builds the geometric and physical intuition needed for that quantum solution.

**应用。** 这里的经典分析——通过角动量守恒化简、有效势、轨道的能量分类——直接对应于氢原子的量子处理（模块 3.4）。从经典角度理解开普勒问题，能建立量子解所需的几何和物理直觉。

---

**Self-test (blank page)**

1. Write down the effective potential for a particle in the gravitational field $V(r) = -k/r$. Sketch $V_\text{eff}(r)$ and identify the radius of a circular orbit.
2. Derive Kepler's second law (equal areas in equal times) as a direct consequence of angular momentum conservation.
3. What determines whether a gravitational orbit is an ellipse, parabola, or hyperbola? Give the condition in terms of total energy $E$.
4. How does the reduced-mass trick allow you to treat a two-body problem as a one-body problem? What is the reduced mass of the Earth–Sun system?

**自测（空白页）**

1. 写出粒子在引力场 $V(r) = -k/r$ 中的有效势。画出 $V_\text{eff}(r)$ 的草图，指出圆轨道的半径。
2. 将开普勒第二定律（等面积定律）作为角动量守恒的直接推论推导出来。
3. 什么决定引力轨道是椭圆、抛物线还是双曲线？用总能量 $E$ 给出条件。
4. 约化质量的技巧如何将二体问题转化为单体问题？地球–太阳系统的约化质量是多少？

---

← Previous: [Module 1.4 — Hamiltonian Mechanics, Action & Noether's Theorem](./module-1.4-hamiltonian-mechanics-noether.md) · [Phase 1 index](./README.md) · Next: [Module 1.6 — Small Oscillations & Coupled Oscillators](./module-1.6-small-oscillations-coupled-oscillators.md) →

---
title: "Module 1.13 — Special Relativity — Kinematics"
parent: "Phase 1 — Classical Physics"
nav_order: 13
---

# Module 1.13 — Special Relativity — Kinematics ⭐
**模块 1.13 — 狭义相对论——运动学 ⭐**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.13-special-relativity-kinematics-derivations.md)

---

## 1. Einstein's Postulates and the Lorentz Transformation · 爱因斯坦假设与洛伦兹变换

**Definition.** Special relativity rests on two postulates: (1) the **principle of relativity** — the laws of physics are the same in all inertial frames; (2) the **constancy of $c$** — the speed of light in vacuum is the same ($c \approx 3 \times 10^8$ m/s) for all inertial observers, regardless of the motion of the source or detector. These replace the Galilean transformation with the **Lorentz transformation**. For a frame $S'$ moving at velocity $v$ along the $x$-axis relative to $S$:

**定义。** 狭义相对论建立在两个假设之上：(1) **相对性原理**——物理定律在所有惯性系中相同；(2) **光速不变原理**——真空中光速对所有惯性观察者均相同（$c \approx 3 \times 10^8$ m/s），与光源或探测器的运动无关。这些假设用**洛伦兹变换**取代了伽利略变换。对于相对 $S$ 以速度 $v$ 沿 $x$ 轴运动的参考系 $S'$：

$$ x' = \gamma(x - vt), \qquad t' = \gamma(t - vx/c^2), \qquad y' = y, \qquad z' = z, $$

where $\gamma = 1/\sqrt{1 - v^2/c^2} \geq 1$ is the **Lorentz factor**. The inverse replaces $v \to -v$. **Velocity addition**: for an object with velocity $u'$ in $S'$, its velocity in $S$ is $u = (u' + v)/(1 + u'v/c^2)$, ensuring no velocity can exceed $c$.

其中 $\gamma = 1/\sqrt{1 - v^2/c^2} \geq 1$ 是**洛伦兹因子**。逆变换将 $v$ 替换为 $-v$。**速度叠加**：对于在 $S'$ 中速度为 $u'$ 的物体，其在 $S$ 中的速度为 $u = (u' + v)/(1 + u'v/c^2)$，确保速度不能超过 $c$。

**Demonstration.** Two key consequences follow directly. **Time dilation**: a clock at rest in $S'$ ticks at rate $dt = \gamma\, d\tau$, where $\tau$ is the **proper time** (the time measured in the rest frame). A muon created at the top of the atmosphere ($v/c \approx 0.9998$) with proper lifetime $\tau_0 = 2.2\ \mathrm{\mu s}$ survives $\gamma\tau_0 \approx 35\ \mathrm{\mu s}$ in the lab frame, long enough to reach Earth's surface — a direct experimental confirmation. **Length contraction**: an object of proper length $L_0$ (rest frame) has measured length $L = L_0/\gamma$ along the direction of motion.

**演示。** 两个关键推论直接得出。**时间膨胀**：静止在 $S'$ 中的时钟以速率 $dt = \gamma\, d\tau$ 走动，其中 $\tau$ 是**固有时**（静止系中测量的时间）。在大气顶部产生的 $\mu$ 子（$v/c \approx 0.9998$），固有寿命 $\tau_0 = 2.2\ \mathrm{\mu s}$，在实验室系中存活 $\gamma\tau_0 \approx 35\ \mathrm{\mu s}$，足以到达地球表面——这是直接的实验证实。**长度收缩**：固有长度为 $L_0$（静止系）的物体在运动方向上的测量长度为 $L = L_0/\gamma$。

**Application.** The Lorentz transformation reveals that time and space are not absolute but mix between frames. The resolution of the twin paradox (the travelling twin is younger) illustrates that elapsed proper time, not coordinate time, is the physically invariant quantity. The mathematical framework sets up the four-dimensional spacetime geometry of Section 2.

**应用。** 洛伦兹变换揭示时间和空间不是绝对的，而是在参考系间混合。双生子佯谬的解答（旅行的孪生子更年轻）说明，经历的固有时（而非坐标时）是物理不变量。该数学框架建立了第 2 节的四维时空几何。

## 2. Minkowski Spacetime and the Invariant Interval · 闵可夫斯基时空与不变间隔

**Definition.** Events are points in **Minkowski spacetime** labelled by four coordinates $x^\mu = (ct, x, y, z)$. The **spacetime interval** between two events is:

**定义。** 事件是**闵可夫斯基时空**中由四个坐标 $x^\mu = (ct, x, y, z)$ 标记的点。两事件间的**时空间隔**为：

$$ s^2 = (c\,\Delta t)^2 - (\Delta x)^2 - (\Delta y)^2 - (\Delta z)^2 $$

(using the $+---$ signature convention). This quantity is **Lorentz-invariant**: all inertial observers assign the same value $s^2$. Depending on sign: $s^2 > 0$ (**timelike** — a causal connection exists), $s^2 = 0$ (**lightlike** / null — connected by a light ray), $s^2 < 0$ (**spacelike** — no causal connection). The **relativity of simultaneity** follows: two events with $\Delta t = 0$ in $S$ but $\Delta x \neq 0$ are not simultaneous in $S'$ ($\Delta t' = -\gamma v\Delta x/c^2 \neq 0$).

（采用 $+---$ 号差约定）。这个量是**洛伦兹不变**的：所有惯性观察者赋予相同的 $s^2$ 值。根据符号：$s^2 > 0$（**类时**——存在因果联系），$s^2 = 0$（**类光**/零——由光线相连），$s^2 < 0$（**类空**——无因果联系）。**同时性的相对性**随之而来：在 $S$ 中 $\Delta t = 0$ 但 $\Delta x \neq 0$ 的两个事件，在 $S'$ 中不同时（$\Delta t' = -\gamma v\Delta x/c^2 \neq 0$）。

**Demonstration.** The invariant interval for muon travel: in the lab frame, $\Delta t = 35\ \mathrm{\mu s}$, $\Delta x = v\cdot\Delta t$. In the muon's rest frame $\Delta x' = 0$, $\Delta t' = \tau_0 = 2.2\ \mathrm{\mu s}$. Check: $s^2 = c^2(35\ \mathrm{\mu s})^2 - (v\cdot 35\ \mathrm{\mu s})^2 = c^2(35\ \mathrm{\mu s})^2(1 - v^2/c^2) = c^2(35\ \mathrm{\mu s})^2/\gamma^2 = c^2(2.2\ \mathrm{\mu s})^2$. Consistent.

**演示。** $\mu$ 子运动的不变间隔：在实验室系中，$\Delta t = 35\ \mathrm{\mu s}$，$\Delta x = v\cdot\Delta t$。在 $\mu$ 子静止系中 $\Delta x' = 0$，$\Delta t' = \tau_0 = 2.2\ \mathrm{\mu s}$。验证：$s^2 = c^2(35\ \mathrm{\mu s})^2 - (v\cdot 35\ \mathrm{\mu s})^2 = c^2(35\ \mathrm{\mu s})^2(1 - v^2/c^2) = c^2(35\ \mathrm{\mu s})^2/\gamma^2 = c^2(2.2\ \mathrm{\mu s})^2$。自洽。

**Application.** Minkowski's geometric formulation makes special relativity a theory of four-dimensional pseudo-Riemannian geometry. It generalises to curved spacetime in general relativity (Phase 7). The four-vector formalism developed here (four-position $x^\mu$, four-velocity, four-momentum) is the language of all relativistic physics: particle kinematics (Module 1.14), covariant electromagnetism (Module 1.15), and quantum field theory (Phase 6).

**应用。** 闵可夫斯基的几何表述使狭义相对论成为四维伪黎曼几何的理论，推广到广义相对论（第 7 阶段）中的弯曲时空。这里发展的四矢量形式（四位置 $x^\mu$、四速度、四动量）是所有相对论物理的语言：粒子运动学（模块 1.14）、协变电磁学（模块 1.15）以及量子场论（第 6 阶段）。

---

**Self-test (blank page)**

1. Derive the time-dilation formula $\Delta t = \gamma\Delta\tau$ from the Lorentz transformation. A particle lives $10\ \mathrm{\mu s}$ in its rest frame while moving at $v = 0.6c$. How long does it live in the lab frame, and how far does it travel?
2. Two events occur at the same place in frame $S$, separated by $\Delta t = 4$ s. What is the spatial separation in a frame where the events are separated by $\Delta t' = 5$ s?
3. Classify the interval $s^2$ between events $A = (0, 0, 0, 0)$ and $B = (c\cdot 3\text{ s}, 5\text{ m}, 0, 0)$ as timelike, lightlike, or spacelike. Can $B$ causally affect $A$?
4. Explain the relativity of simultaneity with a concrete example using a moving train and lightning strikes. Why does this not lead to paradoxes?

**自测（空白页）**

1. 从洛伦兹变换推导时间膨胀公式 $\Delta t = \gamma\Delta\tau$。一个粒子在静止系中寿命为 $10\ \mathrm{\mu s}$，以 $v = 0.6c$ 运动。它在实验室系中存活多长时间？行进多远？
2. 两个事件在参考系 $S$ 中发生在同一地点，时间间隔 $\Delta t = 4$ s。在事件时间间隔为 $\Delta t' = 5$ s 的参考系中，两事件的空间间隔是多少？
3. 将事件 $A = (0, 0, 0, 0)$ 和 $B = (c\cdot 3\text{ s}, 5\text{ m}, 0, 0)$ 之间的间隔 $s^2$ 分类为类时、类光或类空。$B$ 能否因果影响 $A$？
4. 用移动火车和闪电的具体例子解释同时性的相对性。为什么这不会导致悖论？

---

← Previous: [Module 1.12 — Optics & Interference](./module-1.12-optics-interference.md) · [Phase 1 index](./README.md) · Next: [Module 1.14 — Relativistic Dynamics & E = mc²](./module-1.14-relativistic-dynamics-energy-momentum.md) →

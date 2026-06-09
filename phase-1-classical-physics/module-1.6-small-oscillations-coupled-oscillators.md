---
title: "Module 1.6 — Small Oscillations & Coupled Oscillators"
parent: "Phase 1 — Classical Physics"
nav_order: 6
---

# Module 1.6 — Small Oscillations & Coupled Oscillators ⭐
**模块 1.6 — 小振动与耦合振子 ⭐**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.6-small-oscillations-coupled-oscillators-derivations.md)

---

## 1. Simple, Damped, and Driven Harmonic Motion · 简谐、阻尼与受迫振动

**Definition.** A system displaced slightly from a stable equilibrium experiences a restoring force linear in the displacement. Writing $V(x) \approx V(0) + \tfrac12 V''(0)x^2$, Newton's second law gives $\ddot{x} + \omega_0^2 x = 0$ with $\omega_0 = \sqrt{V''/m}$ — the **simple harmonic oscillator** (SHO). Adding a damping force $-b\dot{x}$ and a periodic drive $F_0 \cos(\omega t)$ yields the **driven damped oscillator**:

**定义。** 系统从稳定平衡位置微小偏移时，受到与位移成线性关系的恢复力。将 $V(x) \approx V(0) + \tfrac12 V''(0)x^2$ 代入牛顿第二定律，得 $\ddot{x} + \omega_0^2 x = 0$，其中 $\omega_0 = \sqrt{V''/m}$——即**简谐振子**（SHO）。加入阻尼力 $-b\dot{x}$ 和周期驱动力 $F_0 \cos(\omega t)$，得到**受迫阻尼振子**：

$$ m\ddot{x} + b\dot{x} + kx = F_0 \cos(\omega t). $$

Define the damping ratio $\gamma = b/2m$ and quality factor $Q = \omega_0/2\gamma$. The steady-state amplitude is $A(\omega) = (F_0/m) / \sqrt{(\omega_0^2 - \omega^2)^2 + 4\gamma^2\omega^2}$, which peaks near $\omega \approx \omega_0$ — **resonance**. The width of the resonance peak is $\Delta\omega \approx 2\gamma = \omega_0/Q$; high $Q$ means sharp resonance and slow energy decay.

定义阻尼比 $\gamma = b/2m$ 和品质因数 $Q = \omega_0/2\gamma$。稳态振幅为 $A(\omega) = (F_0/m) / \sqrt{(\omega_0^2 - \omega^2)^2 + 4\gamma^2\omega^2}$，在 $\omega \approx \omega_0$ 附近达到峰值——**共振**。共振峰的宽度为 $\Delta\omega \approx 2\gamma = \omega_0/Q$；高 $Q$ 值意味着尖锐的共振和缓慢的能量衰减。

**Demonstration.** At exact resonance ($\omega = \omega_0$, underdamped), the amplitude grows as $A = F_0 t / (2m\gamma)$ if $\gamma \to 0$, revealing secular growth — the energy pumped in per cycle exactly equals the work done against damping at the peak. The phase of the response shifts by $\pi$ across the resonance: the oscillator lags the drive by $90^\circ$ exactly at $\omega_0$.

**演示。** 在精确共振（$\omega = \omega_0$，欠阻尼）时，若 $\gamma \to 0$，振幅按 $A = F_0 t / (2m\gamma)$ 增长，显示出长期增长——每个周期注入的能量恰好等于在峰值处克服阻尼做的功。响应的相位在共振处改变 $\pi$：振子在 $\omega_0$ 处恰好滞后驱动力 $90^\circ$。

**Application.** Resonance is universal: mechanical bridges (Tacoma Narrows), electrical LC circuits, nuclear magnetic resonance, and atomic spectral lines all exploit or must guard against it. The SHO is the universal local approximation to any potential near a minimum — hence "every physicist's best friend."

**应用。** 共振是普遍的：机械桥梁（塔科马海峡吊桥）、电路 LC 回路、核磁共振以及原子谱线都利用或必须防范共振。简谐振子是势能极小值附近任意势能的普遍局域近似——因此是"每位物理学家最好的朋友"。

## 2. Normal Modes of Coupled Oscillators · 耦合振子的简正模式

**Definition.** For a system of $n$ coupled oscillators with coordinates $x_i$, the equations of motion take matrix form $M\ddot{\mathbf{x}} = -K\mathbf{x}$, where $M$ is the mass matrix and $K$ is the stiffness matrix (both symmetric, $M$ positive definite). Seeking solutions of the form $\mathbf{x}(t) = \mathbf{A} e^{i\omega t}$ converts this to the **generalised eigenvalue problem**:

**定义。** 对于坐标为 $x_i$ 的 $n$ 个耦合振子系统，运动方程取矩阵形式 $M\ddot{\mathbf{x}} = -K\mathbf{x}$，其中 $M$ 为质量矩阵，$K$ 为刚度矩阵（均对称，$M$ 正定）。寻求形如 $\mathbf{x}(t) = \mathbf{A} e^{i\omega t}$ 的解，将问题转化为**广义特征值问题**：

$$ K\mathbf{A} = \omega^2 M\mathbf{A}. $$

The $n$ solutions $(\omega_r^2, \mathbf{A}_r)$ give $n$ **normal modes**: collective motions in which every part oscillates at the same frequency $\omega_r$. Any general motion is a superposition of normal modes.

$n$ 个解 $(\omega_r^2, \mathbf{A}_r)$ 给出 $n$ 个**简正模式**：每个部分都以相同频率 $\omega_r$ 振荡的集体运动。任意一般运动都是简正模式的叠加。

**Demonstration.** Two equal masses $m$ connected by springs $k$ to fixed walls and coupled by spring $\kappa$. The eigenvalue problem yields two normal modes: (1) symmetric (both masses move together), $\omega_1^2 = k/m$; (2) antisymmetric (masses move oppositely), $\omega_2^2 = (k + 2\kappa)/m$. The general solution is a superposition; beats appear when the initial conditions excite both modes.

**演示。** 两个相等质量 $m$ 通过弹簧 $k$ 连接到固定壁，并通过弹簧 $\kappa$ 相互耦合。特征值问题给出两个简正模式：(1) 对称模式（两质量同向运动），$\omega_1^2 = k/m$；(2) 反对称模式（质量反向运动），$\omega_2^2 = (k + 2\kappa)/m$。通解是两者的叠加；当初始条件激励两种模式时出现拍。

**Application.** A crystal lattice is a chain of coupled oscillators — taking the continuum limit gives phonon dispersion relations (Module 4.3). Quantising these collective modes yields **phonons**, the quanta of lattice vibration. The quantum harmonic oscillator (Module 3.2) is the single-mode version of this; second quantisation (Module 3.12) systematises the many-mode generalisation. The eigenvalue structure here is a direct application of linear algebra (Module 0.2).

**应用。** 晶格是一串耦合振子——取连续极限给出声子色散关系（模块 4.3）。将这些集体模式量子化产生**声子**，即晶格振动的量子。量子谐振子（模块 3.2）是这一思路的单模版本；二次量子化（模块 3.12）系统化地处理多模推广。这里的特征值结构是线性代数（模块 0.2）的直接应用。

---

**Self-test (blank page)**

1. A mass $m$ on a spring $k$ is driven at frequency $\omega$. Write the steady-state solution and find the frequency at which the amplitude is maximum (to leading order in $\gamma$).
2. Define the quality factor $Q$ and explain what it tells you physically about the sharpness of resonance and the rate of energy decay.
3. Two equal masses coupled by three identical springs (in the symmetric configuration) have normal mode frequencies $\omega_1$ and $\omega_2$. Derive them and sketch the normal-mode motions.
4. How does the normal-mode problem for $n$ coupled oscillators map onto an eigenvalue problem? What plays the role of the matrix to be diagonalised?

**自测（空白页）**

1. 弹簧上质量 $m$ 以频率 $\omega$ 受迫振动。写出稳态解，求振幅最大时的频率（对 $\gamma$ 取主阶）。
2. 定义品质因数 $Q$，解释它在物理上告诉你关于共振尖锐度和能量衰减速率的什么。
3. 由三根相同弹簧（对称构型）耦合的两个相等质量具有简正模式频率 $\omega_1$ 和 $\omega_2$。推导它们并画出简正模式运动的草图。
4. $n$ 个耦合振子的简正模式问题如何映射为特征值问题？什么充当需要被对角化的矩阵？

---

← Previous: [Module 1.5 — Central-Force Problem & Kepler](./module-1.5-central-force-kepler.md) · [Phase 1 index](./README.md) · Next: [Module 1.7 — Rigid-Body Dynamics & Non-Inertial Frames](./module-1.7-rigid-body-non-inertial-frames.md) →

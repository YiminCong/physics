---
title: "Phase 1 — Classical Physics"
nav_order: 2
has_children: true
---

# Phase 1 — Classical Physics
**第 1 阶段 — 经典物理**

Classical physics encompasses Newtonian and analytical mechanics, electromagnetism, the mechanics of waves, fluids and deformable bodies, nonlinear dynamics, and the relativistic completion of it all in special relativity — the indispensable foundation on which all of modern physics is built. Each module follows the **Definition → Demonstration → Application** format: a precise statement of the core idea, a worked or illustrative example that makes it concrete, and a signpost to where the idea recurs at deeper levels.

经典物理涵盖牛顿力学与分析力学、电磁学、波动力学、流体与可变形体力学、非线性动力学，以及狭义相对论对以上内容的相对论性完善——这是构建全部现代物理的不可或缺的基础。每个模块均遵循**定义 → 演示 → 应用**格式：对核心思想的精确陈述、使其具体化的详解或示例，以及该思想在更深层次重现之处的指引。

## Prerequisites
**前置知识**

A working knowledge of **Phase 0** is assumed throughout, especially:
- **Module 0.1** — Calculus & Taylor Series (variational calculus, Taylor-expanding potentials)
- **Module 0.3** — Differential Equations (equations of motion, boundary-value problems)
- **Module 0.6** — Vector Calculus & Tensors ($\nabla$, $\nabla\cdot$, $\nabla\times$; index notation for relativistic modules)

全程假定读者掌握**第 0 阶段**的相关知识，尤其是：
- **模块 0.1** — 微积分与泰勒级数（变分法、势的泰勒展开）
- **模块 0.3** — 微分方程（运动方程、边值问题）
- **模块 0.6** — 矢量微积分与张量（$\nabla$、$\nabla\cdot$、$\nabla\times$；相对论模块的指标记号）

Fourier methods (Module 0.5) are needed for optics and waves; linear algebra (Module 0.2) for normal modes and the inertia tensor.

傅里叶方法（模块 0.5）用于光学与波动；线性代数（模块 0.2）用于简正模式和惯量张量。

## Modules
**模块列表**

### Mechanics (1.1–1.7) · 力学（1.1–1.7）

| Module | Title | Notes |
|--------|-------|-------|
| [1.1](./module-1.1-newtonian-mechanics.md) | Newtonian Mechanics · 牛顿力学 | $F = ma$, inertial frames, equations of motion |
| [1.2](./module-1.2-conservation-laws.md) | Conservation Laws · 守恒定律 | Energy, momentum, angular momentum, collisions |
| [1.3](./module-1.3-lagrangian-mechanics.md) | Lagrangian Mechanics & the Variational Principle ⭐ · 拉格朗日力学与变分原理 ⭐ | Action $S = \int L\, dt$, Euler–Lagrange, generalised coordinates |
| [1.4](./module-1.4-hamiltonian-mechanics-noether.md) | Hamiltonian Mechanics, Action & Noether's Theorem ⭐ · 哈密顿力学、作用量与诺特定理 ⭐ | $H(q,p)$, Hamilton's equations, Poisson brackets, symmetry → conservation |
| [1.5](./module-1.5-central-force-kepler.md) | Central-Force Problem & Kepler · 有心力问题与开普勒定律 | Reduced mass, effective potential, Kepler's laws |
| [1.6](./module-1.6-small-oscillations-coupled-oscillators.md) | Small Oscillations & Coupled Oscillators ⭐ · 小振动与耦合振子 ⭐ | SHO, resonance, normal modes, eigenvalue problem |
| [1.7](./module-1.7-rigid-body-non-inertial-frames.md) | Rigid-Body Dynamics & Non-Inertial Frames · 刚体动力学与非惯性系 | Inertia tensor, Euler's equations, Coriolis force |

### Electromagnetism (1.8–1.12) · 电磁学（1.8–1.12）

| Module | Title | Notes |
|--------|-------|-------|
| [1.8](./module-1.8-electrostatics-boundary-value-problems.md) | Electrostatics & Boundary-Value Problems ⭐ · 静电学与边值问题 ⭐ | Gauss's law, Poisson/Laplace, separation of variables |
| [1.9](./module-1.9-magnetostatics.md) | Magnetostatics · 静磁学 | Biot–Savart, Ampère, vector potential $\mathbf{A}$ |
| [1.10](./module-1.10-electrodynamics-maxwell-equations.md) | Electrodynamics & Maxwell's Equations ⭐ · 电动力学与麦克斯韦方程组 ⭐ | Faraday, displacement current, all four Maxwell equations |
| [1.11](./module-1.11-em-waves-radiation.md) | Electromagnetic Waves & Radiation · 电磁波与辐射 | Wave equation, $c = 1/\sqrt{\mu_0\varepsilon_0}$, Poynting vector, Larmor formula |
| [1.12](./module-1.12-optics-interference.md) | Optics & Interference · 光学与干涉 | Geometric optics, Huygens, double-slit, diffraction as Fourier transform |

### Special Relativity (1.13–1.15) · 狭义相对论（1.13–1.15）

| Module | Title | Notes |
|--------|-------|-------|
| [1.13](./module-1.13-special-relativity-kinematics.md) | Special Relativity — Kinematics ⭐ · 狭义相对论——运动学 ⭐ | Einstein's postulates, Lorentz transformation, Minkowski spacetime, $s^2$ |
| [1.14](./module-1.14-relativistic-dynamics-energy-momentum.md) | Relativistic Dynamics & $E = mc^2$ ⭐ · 相对论动力学与 $E = mc^2$ ⭐ | Four-vectors, $p^\mu$, $E^2 = (pc)^2 + (mc^2)^2$, relativistic force |
| [1.15](./module-1.15-covariant-electromagnetism.md) | Covariant Electromagnetism · 协变电磁学 | Four-potential $A^\mu$, field tensor $F^{\mu\nu}$, covariant Maxwell equations |

### Continuum, Fluids & Nonlinear Dynamics (1.16–1.19) · 连续介质、流体与非线性动力学（1.16–1.19）

*These extend classical mechanics to continuous media and to nonlinear systems. They depend only on the mechanics block (1.1–1.7), so you may read them right after Module 1.7 if you prefer a strict mechanics-first path.*

*这些模块将经典力学推广至连续介质和非线性系统。它们仅依赖力学模块（1.1–1.7），因此若偏好严格以力学为先的学习路径，可在模块 1.7 之后直接阅读。*

| Module | Title | Notes |
|--------|-------|-------|
| [1.16](./module-1.16-mechanical-waves-acoustics.md) | Mechanical Waves & Acoustics · 机械波与声学 | Wave equation, d'Alembert, standing waves, sound, Doppler, group velocity |
| [1.17](./module-1.17-fluid-mechanics.md) | Fluid Mechanics · 流体力学 | Continuity, Euler, Bernoulli, Navier–Stokes, Reynolds number, turbulence |
| [1.18](./module-1.18-continuum-mechanics-elasticity.md) | Continuum Mechanics & Elasticity · 连续介质力学与弹性理论 | Stress/strain tensors, Hooke's law, elastic (P/S) waves, seismology |
| [1.19](./module-1.19-nonlinear-dynamics-chaos.md) | Nonlinear Dynamics & Chaos · 非线性动力学与混沌 | Phase space, fixed points, bifurcations, Lyapunov exponent, logistic map |

### Advanced Topics: Analytical Mechanics, Scattering & Advanced Electrodynamics (1.20–1.23) · 进阶专题：分析力学、散射与进阶电动力学（1.20–1.23）

*Graduate-level extensions that complete the classical canon — the analytical-mechanics machinery (canonical transformations, Hamilton–Jacobi, action–angle), classical scattering cross sections, and the advanced electrodynamics of radiation and guided waves (Goldstein / Jackson / Landau territory).*

*完成经典物理体系的研究生级扩展——分析力学机制（正则变换、哈密顿–雅可比、作用量–角变量）、经典散射截面，以及辐射与导波的进阶电动力学（Goldstein / Jackson / Landau 的内容）。*

| Module | Title | Notes |
|--------|-------|-------|
| [1.20](./module-1.20-canonical-transformations-hamilton-jacobi.md) | Canonical Transformations, Hamilton–Jacobi & Action–Angle ⭐ · 正则变换、哈密顿–雅可比与作用量–角变量 ⭐ | Generating functions, symplectic condition, HJ equation, action–angle, adiabatic invariants |
| [1.21](./module-1.21-classical-scattering.md) | Classical Scattering Theory · 经典散射理论 | Impact parameter, differential cross section, Rutherford formula |
| [1.22](./module-1.22-retarded-potentials-radiation-reaction.md) | Retarded Potentials, Multipole Radiation & Radiation Reaction · 推迟势、多极辐射与辐射阻尼 | Liénard–Wiechert potentials, dipole radiation, Abraham–Lorentz force |
| [1.23](./module-1.23-waveguides-cavities-transmission-lines.md) | Waveguides, Cavity Resonators & Transmission Lines · 波导、谐振腔与传输线 | Cutoff frequency, TE/TM modes, cavity Q, telegrapher's equations, $Z_0$ |

## Phase 1 Checkpoint (blank page)
**第 1 阶段检查点（空白页）**

Work through these without notes — they span the whole phase.

不借助笔记完成以下题目——它们涵盖整个阶段的内容。

1. A particle moves in a central potential $V(r) = -k/r$. Using the Lagrangian in polar coordinates, find the equations of motion and derive Kepler's orbit equation $r(\phi) = p/(1 + \varepsilon\cos\phi)$.
2. State Noether's theorem. Apply it to show that invariance of the Lagrangian under spatial translation implies conservation of total linear momentum.
3. Write down all four Maxwell equations. Take the curl of Faraday's law, substitute Ampère–Maxwell, and derive the wave equation for $\mathbf{E}$ in free space. Identify the speed of propagation.
4. Define the electromagnetic field tensor $F^{\mu\nu}$. Write Maxwell's inhomogeneous equations in covariant form and show that charge conservation $\partial_\mu J^\mu = 0$ is automatic.
5. An electron and positron (each mass $m = 0.511\,\text{MeV}/c^2$) annihilate at rest to produce two photons. Using four-momentum conservation, find the frequency of each photon.
6. A pendulum of length $\ell$ and mass $m$ is released from small angle $\theta_0$. Use the Hamiltonian formalism to show the phase-space orbit is an ellipse and identify the adiabatic invariant.
7. Two masses $m$ connected to fixed walls and each other by identical springs of constant $k$ form a symmetric coupled oscillator. Find the normal mode frequencies and sketch the corresponding motions.
8. Explain physically why a purely electric Coulomb field in the rest frame of a charge acquires a magnetic component in a frame where the charge moves. Which transformation law makes this precise?
9. Derive the wave speed $c = \sqrt{T/\mu}$ on a string, and separately state the Bernoulli and Navier–Stokes equations, identifying which term in Navier–Stokes is responsible for turbulence.
10. Define the Lyapunov exponent and the strain tensor. Explain how the long-wavelength limit of the elastic wave equation (1.18) connects to the acoustic phonons of Phase 4.

**自测（空白页）**

1. 一粒子在有心势 $V(r) = -k/r$ 中运动。用极坐标下的拉格朗日量，求运动方程并推导开普勒轨道方程 $r(\phi) = p/(1 + \varepsilon\cos\phi)$。
2. 陈述诺特定理。利用它证明：拉格朗日量在空间平移下的不变性意味着总线动量守恒。
3. 写出全部四个麦克斯韦方程。对法拉第定律取旋度，代入安培–麦克斯韦方程，推导自由空间中 $\mathbf{E}$ 的波动方程，并指出传播速度。
4. 定义电磁场张量 $F^{\mu\nu}$。用协变形式写出麦克斯韦非齐次方程，并证明电荷守恒 $\partial_\mu J^\mu = 0$ 是自动满足的。
5. 一个电子和一个正电子（各自质量 $m = 0.511\,\text{MeV}/c^2$）静止湮灭产生两个光子。利用四动量守恒，求每个光子的频率。
6. 长为 $\ell$、质量为 $m$ 的摆从小角度 $\theta_0$ 释放。用哈密顿形式证明相空间轨道为椭圆，并确定绝热不变量。
7. 两个质量为 $m$ 的质点通过弹簧常数为 $k$ 的弹簧分别连接到固定壁和彼此，构成对称耦合振子。求简正模式频率并勾画相应运动。
8. 物理上解释为什么静止电荷参考系中的纯库仑电场，在电荷运动的参考系中会出现磁场分量。哪个变换定律给出精确表述？
9. 推导弦上的波速 $c = \sqrt{T/\mu}$，并分别陈述伯努利方程和纳维–斯托克斯方程，指出纳维–斯托克斯方程中哪一项负责湍流。
10. 定义李雅普诺夫指数和应变张量。解释弹性波方程（1.18）的长波极限如何与第 4 阶段的声学声子相联系。

---

→ Continue to **[Phase 2 — Thermodynamics & Statistical Mechanics](../phase-2-thermodynamics-statistical-mechanics/)**.

→ 继续学习**[第 2 阶段 — 热力学与统计力学](../phase-2-thermodynamics-statistical-mechanics/)**。

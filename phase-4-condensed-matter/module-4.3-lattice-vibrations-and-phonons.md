# Module 4.3 — Lattice Vibrations & Phonons ⭐
**模块 4.3 — 晶格振动与声子 ⭐**

> **Phase 4 — [Condensed Matter / Solid State](./README.md)** · Format: Definition → Demonstration → Application
> **第 4 阶段 — 凝聚态 / 固体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-4.3-derivations.md)

---

## 1. Normal Modes of the Lattice · 晶格的简正模

**Definition.** Atoms oscillate about equilibrium; the coupled equations (exactly the coupled-oscillator problem of Module 1.6) have collective **normal modes** — lattice waves with dispersion $\omega(k)$.

**定义。** 原子在平衡位置附近振荡；耦合方程（恰好是模块 1.6 的耦合振子问题）具有集体**简正模**——具有色散关系 $\omega(k)$ 的晶格波。

**Demonstration.** The **monatomic 1D chain** gives $\omega(k) = 2\sqrt{K/M}\,\lvert\sin(ka/2)\rvert$. A **diatomic chain** splits into two branches: a low-frequency **acoustic** branch and a high-frequency **optical** branch.

**演示。** **单原子一维链**给出 $\omega(k) = 2\sqrt{K/M}\,\lvert\sin(ka/2)\rvert$。**双原子链**分裂为两支：低频的**声学**支和高频的**光学**支。

## 2. Phonons · 声子

**Definition.** Quantizing each vibrational mode (each is a harmonic oscillator, Module 3.2) gives quanta called **phonons** — bosons with energy $\hbar\omega$, occupied according to Bose–Einstein statistics (Module 2.5).

**定义。** 对每个振动模式进行量子化（每个模式都是一个谐振子，模块 3.2），得到称为**声子**的量子——它们是能量为 $\hbar\omega$ 的玻色子，按玻色–爱因斯坦统计分布（模块 2.5）。

**Application.** Phonons carry heat and scatter electrons (causing resistance). Most importantly, the **electron–phonon interaction** provides the *attractive* force that binds electrons into Cooper pairs in conventional superconductors. The **isotope effect** — $T_c \propto M^{-1/2}$ in ion mass — was the smoking gun that phonons drive superconductivity (Phase 5).

**应用。** 声子传递热量并散射电子（造成电阻）。最重要的是，**电子–声子相互作用**提供了将电子束缚成库珀对的*吸引力*（传统超导体中）。**同位素效应**——$T_c \propto M^{-1/2}$ 对离子质量——是声子驱动超导性的确凿证据（第 5 阶段）。

## Key results · 核心结果

- $\omega(k) = 2\sqrt{K/M}\,|\sin(ka/2)|$ — dispersion of the 1D chain · 一维链色散关系
- Acoustic vs optical branches; a basis of $p$ atoms gives $3p$ branches · 声学支与光学支
- Phonons = quantized normal modes (one harmonic oscillator per mode, 1.6 → 3.2) · 声子即量子化简正模
- Phonons carry heat and mediate the electron attraction behind BCS · 声子输运热并介导 BCS 吸引

---

**Self-test (blank page)**

1. Derive (or state) the dispersion relation $\omega(k) = 2\sqrt{K/M}\,\lvert\sin(ka/2)\rvert$ for the monatomic 1D chain. What is the group velocity at the zone boundary, and why?
2. A diatomic chain with masses $M_1$ and $M_2$ has two branches. What is the gap that opens between the acoustic and optical branches at the zone boundary, and which atoms move in each branch at $k = 0$?
3. What are phonons? State their statistics, their energy, and explain why the Debye model gives $C \propto T^3$ at low temperature while the Einstein model does not reproduce this correctly.
4. State the isotope effect $T_c \propto M^{-1/2}$ and explain what it implies about the role of phonons in conventional superconductivity.

**自测（空白页）**

1. 推导（或写出）单原子一维链的色散关系 $\omega(k) = 2\sqrt{K/M}\,\lvert\sin(ka/2)\rvert$。区边界处的群速度是多少？为什么？
2. 质量为 $M_1$ 和 $M_2$ 的双原子链有两支色散。区边界处声学支与光学支之间打开的能隙是多少？在 $k = 0$ 处各支中哪些原子运动？
3. 什么是声子？写出其统计类型和能量，并解释为何德拜模型在低温下给出 $C \propto T^3$ 而爱因斯坦模型不能正确重现这一结果。
4. 写出同位素效应 $T_c \propto M^{-1/2}$，并解释它对传统超导中声子所起作用的含义。

---

← Previous: [Module 4.2 — Crystal Structure & Reciprocal Space](./module-4.2-crystal-structure-and-reciprocal-space.md) · [Phase 4 index](./README.md) · Next: [Module 4.4 — Electrons in a Periodic Potential](./module-4.4-electrons-in-a-periodic-potential.md) →

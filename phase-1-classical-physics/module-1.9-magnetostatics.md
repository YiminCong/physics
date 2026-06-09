# Module 1.9 — Magnetostatics
**模块 1.9 — 静磁学**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.9-magnetostatics-derivations.md)

---

## 1. Biot–Savart Law, Ampère's Law, and the Vector Potential · 毕奥–萨伐尔定律、安培定律与矢量势

**Definition.** A steady current density $\mathbf{J}(\mathbf{r})$ produces a magnetic field $\mathbf{B}(\mathbf{r})$ given by the **Biot–Savart law**:

**定义。** 稳恒电流密度 $\mathbf{J}(\mathbf{r})$ 产生由**毕奥–萨伐尔定律**给出的磁场 $\mathbf{B}(\mathbf{r})$：

$$ \mathbf{B}(\mathbf{r}) = \frac{\mu_0}{4\pi} \int \frac{\mathbf{J}(\mathbf{r}') \times (\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^3}\, dV'. $$

The static Maxwell equations for $\mathbf{B}$ are:

$\mathbf{B}$ 的静磁麦克斯韦方程为：

$$ \nabla \cdot \mathbf{B} = 0 \quad (\text{no magnetic monopoles}), \qquad \nabla \times \mathbf{B} = \mu_0 \mathbf{J} \quad (\text{Ampère's law, static}). $$

Because $\nabla \cdot \mathbf{B} = 0$, one can always write $\mathbf{B} = \nabla \times \mathbf{A}$, where $\mathbf{A}$ is the **magnetic vector potential**. $\mathbf{A}$ is not unique — the gauge transformation $\mathbf{A} \to \mathbf{A} + \nabla\chi$ leaves $\mathbf{B}$ unchanged. In the **Coulomb gauge** $\nabla \cdot \mathbf{A} = 0$, Ampère's law reduces to $\nabla^2\mathbf{A} = -\mu_0 \mathbf{J}$, a vector Poisson equation solved by the same Green's function as electrostatics.

由于 $\nabla \cdot \mathbf{B} = 0$，总可以写成 $\mathbf{B} = \nabla \times \mathbf{A}$，其中 $\mathbf{A}$ 是**磁矢量势**。$\mathbf{A}$ 不是唯一的——规范变换 $\mathbf{A} \to \mathbf{A} + \nabla\chi$ 不改变 $\mathbf{B}$。在**库仑规范** $\nabla \cdot \mathbf{A} = 0$ 下，安培定律化为 $\nabla^2\mathbf{A} = -\mu_0 \mathbf{J}$，这是一个用与静电学相同的格林函数求解的矢量泊松方程。

**Demonstration.** For an infinite straight wire carrying current $I$ along the $z$-axis, Ampère's law applied to a circular loop of radius $r$ gives $\mathbf{B} = \frac{\mu_0 I}{2\pi r}\,\hat{\boldsymbol{\phi}}$. The same calculation in integral form demonstrates the power of symmetry: the field is tangential and constant on the loop, making the line integral trivial.

**演示。** 对于沿 $z$ 轴流过电流 $I$ 的无限长直导线，将安培定律应用于半径为 $r$ 的圆形回路，得 $\mathbf{B} = \frac{\mu_0 I}{2\pi r}\,\hat{\boldsymbol{\phi}}$。用积分形式进行同样的计算展示了对称性的力量：场在回路上是切向且恒定的，使线积分变得简单。

**Application.** The vector potential $\mathbf{A}$ is not merely a mathematical convenience — in quantum mechanics it enters the Hamiltonian directly as $(\mathbf{p} - q\mathbf{A})^2/2m$ (the minimal coupling prescription), and the Aharonov–Bohm effect shows that $\mathbf{A}$ has physical consequences even where $\mathbf{B} = 0$. This gauge freedom is the classical seed of gauge field theory (Phase 8). The magnetic dipole moment $\mathbf{m} = \tfrac12 \int \mathbf{r} \times \mathbf{J}\, dV$ appears in NMR, magnetism, and the interaction of particles with external fields.

**应用。** 矢量势 $\mathbf{A}$ 不仅仅是数学上的便利——在量子力学中它直接以 $(\mathbf{p} - q\mathbf{A})^2/2m$ 进入哈密顿量（最小耦合方案），阿哈罗诺夫–玻姆效应表明即使在 $\mathbf{B} = 0$ 处 $\mathbf{A}$ 也有物理后果。这种规范自由度是规范场论（第 8 阶段）的经典萌芽。磁偶极矩 $\mathbf{m} = \tfrac12 \int \mathbf{r} \times \mathbf{J}\, dV$ 出现在核磁共振、磁学以及粒子与外场的相互作用中。

## 2. Magnetic Dipoles and Magnetic Materials · 磁偶极子与磁性材料

**Definition.** A small current loop of area $a$ carrying current $I$ has a **magnetic dipole moment** $\mathbf{m} = I a\,\hat{\mathbf{n}}$. At large distances $r \gg$ loop size, the field is a magnetic dipole: $\mathbf{B}_\text{dip} = \frac{\mu_0}{4\pi r^3}(2m\cos\theta\,\hat{\mathbf{r}} + m\sin\theta\,\hat{\boldsymbol{\theta}})$. The energy of a dipole in an external field is $U = -\mathbf{m} \cdot \mathbf{B}$, and the torque is $\boldsymbol{\tau} = \mathbf{m} \times \mathbf{B}$. For a magnetic medium, the macroscopic fields $\mathbf{H}$ and $\mathbf{B}$ are related by $\mathbf{B} = \mu_0(\mathbf{H} + \mathbf{M})$, where $\mathbf{M}$ is the magnetisation density.

**定义。** 面积为 $a$、载流 $I$ 的小电流环具有**磁偶极矩** $\mathbf{m} = I a\,\hat{\mathbf{n}}$。在远处（$r \gg$ 环尺寸），场为磁偶极子：$\mathbf{B}_\text{dip} = \frac{\mu_0}{4\pi r^3}(2m\cos\theta\,\hat{\mathbf{r}} + m\sin\theta\,\hat{\boldsymbol{\theta}})$。偶极子在外场中的能量为 $U = -\mathbf{m} \cdot \mathbf{B}$，力矩为 $\boldsymbol{\tau} = \mathbf{m} \times \mathbf{B}$。对于磁性介质，宏观场 $\mathbf{H}$ 和 $\mathbf{B}$ 通过 $\mathbf{B} = \mu_0(\mathbf{H} + \mathbf{M})$ 相联系，其中 $\mathbf{M}$ 为磁化密度。

**Demonstration.** A proton in a magnetic field $B_0\,\hat{\mathbf{z}}$ has a magnetic moment $\mathbf{m} = \gamma_p \mathbf{L}$ (where $\gamma_p$ is the gyromagnetic ratio). In equilibrium it precesses about $\hat{\mathbf{z}}$ at the **Larmor frequency** $\omega_L = \gamma_p B_0$. Driving with a transverse oscillating field at $\omega_L$ produces magnetic resonance — the basis of NMR and MRI.

**演示。** 磁场 $B_0\,\hat{\mathbf{z}}$ 中的质子具有磁矩 $\mathbf{m} = \gamma_p \mathbf{L}$（其中 $\gamma_p$ 为旋磁比）。在平衡时它以**拉莫尔频率** $\omega_L = \gamma_p B_0$ 绕 $\hat{\mathbf{z}}$ 进动。以横向振荡场在 $\omega_L$ 处驱动产生磁共振——核磁共振和核磁共振成像的基础。

**Application.** Magnetostatics feeds directly into electrodynamics (Module 1.10): Faraday's law of induction is the time-varying generalisation of the static Biot–Savart/Ampère framework. The gauge structure of $\mathbf{A}$ prefigures the four-potential $A^\mu$ in covariant electromagnetism (Module 1.15) and QED (Phase 8).

**应用。** 静磁学直接进入电动力学（模块 1.10）：法拉第电磁感应定律是静态毕奥–萨伐尔/安培框架的时变推广。$\mathbf{A}$ 的规范结构预示了协变电磁学（模块 1.15）和量子电动力学（第 8 阶段）中的四矢量势 $A^\mu$。

---

**Self-test (blank page)**

1. Use Ampère's law to find $\mathbf{B}$ inside and outside a long solenoid of $n$ turns per unit length carrying current $I$.
2. Define the magnetic vector potential $\mathbf{A}$. Show that the gauge transformation $\mathbf{A} \to \mathbf{A} + \nabla\chi$ leaves $\mathbf{B}$ unchanged. What is the Coulomb gauge condition?
3. A circular loop of radius $R$ carries current $I$. Find the magnetic field on the axis at distance $z$ from the centre using the Biot–Savart law.
4. What is the Aharonov–Bohm effect, and why does it demonstrate that $\mathbf{A}$ (not just $\mathbf{B}$) is physically meaningful in quantum mechanics?

**自测（空白页）**

1. 用安培定律求每单位长度 $n$ 匝、载流 $I$ 的长螺线管内外的 $\mathbf{B}$。
2. 定义磁矢量势 $\mathbf{A}$。证明规范变换 $\mathbf{A} \to \mathbf{A} + \nabla\chi$ 不改变 $\mathbf{B}$。库仑规范条件是什么？
3. 半径为 $R$ 的圆形线圈载流 $I$。用毕奥–萨伐尔定律求轴线上距中心 $z$ 处的磁场。
4. 阿哈罗诺夫–玻姆效应是什么？它为什么证明了 $\mathbf{A}$（而不仅仅是 $\mathbf{B}$）在量子力学中具有物理意义？

---

← Previous: [Module 1.8 — Electrostatics & Boundary-Value Problems](./module-1.8-electrostatics-boundary-value-problems.md) · [Phase 1 index](./README.md) · Next: [Module 1.10 — Electrodynamics & Maxwell's Equations](./module-1.10-electrodynamics-maxwell-equations.md) →

# Module 1.14 — Relativistic Dynamics & E = mc² ⭐
**模块 1.14 — 相对论动力学与 E = mc² ⭐**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.14-relativistic-dynamics-energy-momentum-derivations.md)

---

## 1. Four-Vectors and Relativistic Momentum · 四矢量与相对论动量

**Definition.** A **four-vector** is a set of four quantities that transforms under a Lorentz boost exactly like $(ct, x, y, z)$. The **proper time** $\tau$ is the Lorentz-invariant time measured by a co-moving clock, related to coordinate time by $d\tau = dt/\gamma$. The **four-velocity** is $U^\mu = dx^\mu/d\tau = \gamma(c, \mathbf{v})$, with $U^\mu U_\mu = c^2$ (constant). The **four-momentum** is:

**定义。** **四矢量**是在洛伦兹变换下与 $(ct, x, y, z)$ 完全相同变换的四个量的集合。**固有时** $\tau$ 是由共动时钟测量的洛伦兹不变时间，与坐标时的关系为 $d\tau = dt/\gamma$。**四速度**为 $U^\mu = dx^\mu/d\tau = \gamma(c, \mathbf{v})$，满足 $U^\mu U_\mu = c^2$（常数）。**四动量**为：

$$ p^\mu = m U^\mu = (E/c, p_x, p_y, p_z), $$

where $m$ is the **rest mass** (Lorentz scalar), the spatial part is the relativistic momentum $\mathbf{p} = \gamma m\mathbf{v}$, and the time component gives the **relativistic energy** $E = \gamma mc^2$. The invariant magnitude is:

其中 $m$ 为**静止质量**（洛伦兹标量），空间部分为相对论动量 $\mathbf{p} = \gamma m\mathbf{v}$，时间分量给出**相对论能量** $E = \gamma mc^2$。不变模长为：

$$ p^\mu p_\mu = (E/c)^2 - |\mathbf{p}|^2 = (mc)^2, $$

or equivalently $E^2 = (pc)^2 + (mc^2)^2$. For a photon $m = 0$, so $E = pc = h\nu$ (with the quantum relation, Module 3.1).

或等价地 $E^2 = (pc)^2 + (mc^2)^2$。对于光子 $m = 0$，故 $E = pc = h\nu$（配合量子关系，模块 3.1）。

**Demonstration.** Low-velocity limit: $E = \gamma mc^2 = mc^2 + \tfrac12 mv^2 + O(v^4/c^2)$. The first term is the **rest energy** $E_0 = mc^2$, the second is the familiar kinetic energy. At $v = 0$ the energy is not zero but $mc^2$ — a prediction with no classical counterpart. For an ultra-relativistic particle ($v \to c$, $pc \gg mc^2$), $E \approx pc$: the particle behaves like a massless particle.

**演示。** 低速极限：$E = \gamma mc^2 = mc^2 + \tfrac12 mv^2 + O(v^4/c^2)$。第一项是**静止能量** $E_0 = mc^2$，第二项是熟悉的动能。在 $v = 0$ 时能量不为零，而是 $mc^2$——这是经典力学没有对应的预言。对于超相对论粒子（$v \to c$，$pc \gg mc^2$），$E \approx pc$：粒子表现得像无质量粒子。

**Application.** Mass–energy equivalence $E = mc^2$ quantifies the energy released in nuclear reactions and particle–antiparticle annihilation. In fission of ${}^{235}\text{U}$, roughly 0.1% of rest mass converts to energy — the basis of nuclear power. The four-momentum is the fundamental kinematic quantity in all of particle physics (Phase 8): invariant mass $m^2 = (\sum p_i)^2 / c^2$ identifies particles, and four-momentum conservation (replacing the separate non-relativistic conservation laws for mass, momentum, and energy) constrains every scattering and decay process.

**应用。** 质能等价 $E = mc^2$ 量化了核反应和粒子–反粒子湮灭中释放的能量。在 ${}^{235}\text{U}$ 裂变中，约 0.1% 的静止质量转化为能量——核能的基础。四动量是所有粒子物理（第 8 阶段）中基本的运动学量：不变质量 $m^2 = (\sum p_i)^2 / c^2$ 鉴别粒子，四动量守恒（取代非相对论的质量、动量、能量三个独立守恒定律）约束每个散射和衰变过程。

## 2. Relativistic Dynamics and Force · 相对论动力学与力

**Definition.** The relativistic equation of motion is $f^\mu = dp^\mu/d\tau$, where $f^\mu$ is the **four-force**. The spatial part gives $d\mathbf{p}/dt = \mathbf{F}$ (three-force), with $\mathbf{p} = \gamma m\mathbf{v}$; the time component gives $dE/dt = \mathbf{F} \cdot \mathbf{v}$ (power). For a particle in an electromagnetic field, the four-force is $f^\mu = q F^{\mu\nu} U_\nu$ (the Lorentz force in covariant form, linking to Module 1.15). Newton's three laws are recovered in the limit $v \ll c$: $\mathbf{F} = d\mathbf{p}/dt \approx m\mathbf{a}$.

**定义。** 相对论运动方程为 $f^\mu = dp^\mu/d\tau$，其中 $f^\mu$ 是**四力**。空间部分给出 $d\mathbf{p}/dt = \mathbf{F}$（三维力），$\mathbf{p} = \gamma m\mathbf{v}$；时间分量给出 $dE/dt = \mathbf{F} \cdot \mathbf{v}$（功率）。对于电磁场中的粒子，四力为 $f^\mu = q F^{\mu\nu} U_\nu$（协变形式的洛伦兹力，与模块 1.15 相联系）。在 $v \ll c$ 极限下恢复牛顿三定律：$\mathbf{F} = d\mathbf{p}/dt \approx m\mathbf{a}$。

**Demonstration.** A particle accelerated from rest through potential difference $V$ gains kinetic energy $K = qV = (\gamma - 1)mc^2$. For an electron ($mc^2 = 0.511$ MeV) accelerated through $V = 1$ MV, $\gamma = 1 + 1/0.511 \approx 2.96$, $v/c = \sqrt{1 - 1/\gamma^2} \approx 0.94c$. Non-relativistic treatment would give $v/c \approx 1.98$ — faster than light, which is impossible. Relativistic treatment is mandatory.

**演示。** 粒子从静止通过电位差 $V$ 加速，获得动能 $K = qV = (\gamma - 1)mc^2$。对于通过 $V = 1$ MV 加速的电子（$mc^2 = 0.511$ MeV），$\gamma = 1 + 1/0.511 \approx 2.96$，$v/c = \sqrt{1 - 1/\gamma^2} \approx 0.94c$。非相对论处理给出 $v/c \approx 1.98$——超过光速，这是不可能的。相对论处理是必须的。

**Application.** Relativistic kinematics underpins every calculation in high-energy physics. The threshold energy for particle production (e.g. $e^+ e^- \to \mu^+ \mu^-$ requires $E_\text{cm} \geq 2m_\mu c^2$), invariant mass reconstruction of short-lived particles, and the kinematics of particle decays all use $E^2 = (pc)^2 + (mc^2)^2$ and four-momentum conservation. The Lorentz-covariant formulation connects directly to quantum field theory (Phase 6) and the Standard Model (Phase 8).

**应用。** 相对论运动学支撑着高能物理中的每一个计算。粒子产生的阈能（例如 $e^+ e^- \to \mu^+ \mu^-$ 要求 $E_\text{cm} \geq 2m_\mu c^2$）、短寿命粒子的不变质量重建以及粒子衰变运动学，都使用 $E^2 = (pc)^2 + (mc^2)^2$ 和四动量守恒。洛伦兹协变形式直接连接到量子场论（第 6 阶段）和标准模型（第 8 阶段）。

---

**Self-test (blank page)**

1. Show that the four-momentum $p^\mu p_\mu = m^2 c^2$ is Lorentz-invariant, and derive $E^2 = (pc)^2 + (mc^2)^2$ from this relation.
2. A pion ($m = 135$ MeV/$c^2$) at rest decays to two photons. Using four-momentum conservation, find the energy and momentum of each photon in the pion rest frame.
3. An electron is accelerated from rest through 2 MV. Find its final $\gamma$, speed $v/c$, and kinetic energy. Compare the relativistic and non-relativistic results.
4. Explain why "$\mathbf{F} = m\mathbf{a}$" must be modified in special relativity. Write the correct relativistic equation of motion and recover Newton's law in the non-relativistic limit.

**自测（空白页）**

1. 证明四动量 $p^\mu p_\mu = m^2 c^2$ 是洛伦兹不变的，并由此推导 $E^2 = (pc)^2 + (mc^2)^2$。
2. 静止的 $\pi$ 介子（$m = 135$ MeV/$c^2$）衰变为两个光子。利用四动量守恒，求 $\pi$ 介子静止系中每个光子的能量和动量。
3. 电子从静止通过 2 MV 加速。求其末态 $\gamma$、速度 $v/c$ 和动能。比较相对论结果与非相对论结果。
4. 解释为什么"$\mathbf{F} = m\mathbf{a}$"在狭义相对论中必须修改。写出正确的相对论运动方程，并在非相对论极限下恢复牛顿定律。

---

← Previous: [Module 1.13 — Special Relativity — Kinematics](./module-1.13-special-relativity-kinematics.md) · [Phase 1 index](./README.md) · Next: [Module 1.15 — Covariant Electromagnetism](./module-1.15-covariant-electromagnetism.md) →

# Module 1.11 — Electromagnetic Waves & Radiation
**模块 1.11 — 电磁波与辐射**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.11-em-waves-radiation-derivations.md)

---

## 1. The Wave Equation and Plane Waves · 波动方程与平面波

**Definition.** In free space ($\rho = 0$, $J = 0$) Maxwell's equations yield the **wave equation** for each component of $\mathbf{E}$ and $\mathbf{B}$:

**定义。** 在自由空间（$\rho = 0$，$J = 0$）中，麦克斯韦方程组给出 $\mathbf{E}$ 和 $\mathbf{B}$ 各分量的**波动方程**：

$$ \nabla^2\mathbf{E} = \mu_0\epsilon_0\frac{\partial^2 \mathbf{E}}{\partial t^2}, \qquad \nabla^2\mathbf{B} = \mu_0\epsilon_0\frac{\partial^2 \mathbf{B}}{\partial t^2}. $$

The **speed of light** is $c = 1/\sqrt{\mu_0\epsilon_0} \approx 3 \times 10^8$ m/s. A **plane wave** propagating in direction $\hat{\mathbf{k}}$ takes the form $\mathbf{E} = \mathbf{E}_0\, e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)}$, $\mathbf{B} = \mathbf{B}_0\, e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)}$, with the dispersion relation $\omega = c|\mathbf{k}|$. From the Maxwell curl equations: (i) $\mathbf{k} \cdot \mathbf{E}_0 = 0$ and $\mathbf{k} \cdot \mathbf{B}_0 = 0$ ($\mathbf{E}$, $\mathbf{B}$ transverse to propagation), (ii) $\mathbf{B}_0 = (\hat{\mathbf{k}} \times \mathbf{E}_0)/c$ ($\mathbf{E}$ and $\mathbf{B}$ mutually perpendicular), (iii) $|\mathbf{E}_0| = c|\mathbf{B}_0|$. **Polarisation** refers to the direction of $\mathbf{E}$; for circular polarisation, $\mathbf{E}_0$ is a complex vector with equal-amplitude perpendicular components differing by $\pi/2$ in phase.

**光速**为 $c = 1/\sqrt{\mu_0\epsilon_0} \approx 3 \times 10^8$ m/s。沿 $\hat{\mathbf{k}}$ 方向传播的**平面波**取形式 $\mathbf{E} = \mathbf{E}_0\, e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)}$，$\mathbf{B} = \mathbf{B}_0\, e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)}$，色散关系为 $\omega = c|\mathbf{k}|$。由麦克斯韦旋度方程：(i) $\mathbf{k} \cdot \mathbf{E}_0 = 0$ 且 $\mathbf{k} \cdot \mathbf{B}_0 = 0$（$\mathbf{E}$、$\mathbf{B}$ 横向于传播方向），(ii) $\mathbf{B}_0 = (\hat{\mathbf{k}} \times \mathbf{E}_0)/c$（$\mathbf{E}$ 和 $\mathbf{B}$ 相互垂直），(iii) $|\mathbf{E}_0| = c|\mathbf{B}_0|$。**偏振**指 $\mathbf{E}$ 的方向；圆偏振时 $\mathbf{E}_0$ 是复向量，两垂直分量等幅且相位差 $\pi/2$。

**Demonstration.** A linearly polarised wave in vacuum: $\mathbf{E} = E_0 \cos(kz - \omega t)\,\hat{\mathbf{x}}$, $\mathbf{B} = (E_0/c) \cos(kz - \omega t)\,\hat{\mathbf{y}}$. The **Poynting vector** $\mathbf{S} = \frac{1}{\mu_0} \mathbf{E} \times \mathbf{B} = \frac{E_0^2}{\mu_0 c} \cos^2(kz - \omega t)\,\hat{\mathbf{z}}$ gives the energy flux ($\mathrm{W/m^2}$). Time-averaging gives $\langle S\rangle = E_0^2/(2\mu_0 c) = \tfrac12\epsilon_0 c\, E_0^2$ — the **intensity** of the wave.

**演示。** 真空中的线偏振波：$\mathbf{E} = E_0 \cos(kz - \omega t)\,\hat{\mathbf{x}}$，$\mathbf{B} = (E_0/c) \cos(kz - \omega t)\,\hat{\mathbf{y}}$。**坡印亭矢量** $\mathbf{S} = \frac{1}{\mu_0} \mathbf{E} \times \mathbf{B} = \frac{E_0^2}{\mu_0 c} \cos^2(kz - \omega t)\,\hat{\mathbf{z}}$ 给出能量通量（$\mathrm{W/m^2}$）。时间平均给出 $\langle S\rangle = E_0^2/(2\mu_0 c) = \tfrac12\epsilon_0 c\, E_0^2$——即波的**强度**。

**Application.** The electromagnetic spectrum from radio waves to gamma rays is all the same physics at different frequencies. The wave equation reappears in acoustics, quantum mechanics (the free-particle Schrödinger equation in the high-frequency limit), and field theory. The Poynting vector generalises to a stress-energy tensor in both relativity (Phase 7) and field theory (Phase 6).

**应用。** 从无线电波到伽马射线的整个电磁频谱，都是不同频率下的同一物理。波动方程在声学、量子力学（高频极限下的自由粒子薛定谔方程）和场论中重复出现。坡印亭矢量在相对论（第 7 阶段）和场论（第 6 阶段）中都推广为应力–能量张量。

## 2. Radiation from Accelerating Charges · 加速电荷的辐射

**Definition.** An accelerating point charge radiates electromagnetic energy. The total power radiated by a charge $q$ with acceleration $a$ is given by the **Larmor formula**:

**定义。** 加速的点电荷辐射电磁能量。电荷 $q$ 以加速度 $a$ 运动时辐射的总功率由**拉莫尔公式**给出：

$$ P = \frac{q^2 a^2}{6\pi\epsilon_0 c^3} \quad (\text{SI units}). $$

For a charge undergoing simple harmonic oscillation (a **Hertzian dipole**), $P \propto \omega^4 |p|^2$, where $p$ is the dipole moment amplitude. The far-field radiation pattern goes as $\sin^2\theta$ (maximum perpendicular to the oscillation axis, zero along it), with the electric field $E_\text{rad} \propto (a/rc^2)\sin\theta$ falling off as $1/r$.

对于做简谐振荡的电荷（**赫兹偶极子**），$P \propto \omega^4 |p|^2$，其中 $p$ 为偶极矩振幅。远场辐射方向图为 $\sin^2\theta$（垂直于振荡轴方向最大，沿轴方向为零），电场 $E_\text{rad} \propto (a/rc^2)\sin\theta$ 按 $1/r$ 衰减。

**Demonstration.** A dipole antenna of length $d$ oscillating at angular frequency $\omega$ has time-averaged radiated power $P \propto (d/\lambda)^2 c\,\epsilon_0 E_0^2$. The $\omega^4$ frequency dependence explains why the sky is blue: Rayleigh scattering of sunlight by atmospheric molecules scales as $\omega^4$, scattering blue (high-$\omega$) light far more efficiently than red.

**演示。** 长度为 $d$、以角频率 $\omega$ 振荡的偶极天线的时间平均辐射功率 $P \propto (d/\lambda)^2 c\,\epsilon_0 E_0^2$。$\omega^4$ 的频率依赖性解释了天空为什么是蓝色的：大气分子对阳光的瑞利散射正比于 $\omega^4$，散射蓝光（高 $\omega$）的效率远高于红光。

**Application.** Larmor radiation imposes a fundamental limit on classical atomic models — an orbiting electron would spiral inward in $\sim 10^{-11}$ s, the crisis that quantum mechanics (Module 3.1) resolves. Synchrotron radiation from relativistic charged particles (the relativistic generalisation, where $P = q^2 c\,\gamma^4 a_\perp^2/(6\pi\epsilon_0(m c^2)^2)$) powers modern X-ray light sources. Quantising the radiation field yields photons and QED (Phase 6, Phase 8).

**应用。** 拉莫尔辐射对经典原子模型施加了根本性限制——轨道电子将在约 $10^{-11}$ s 内螺旋向内坠落，这正是量子力学（模块 3.1）所解决的危机。相对论带电粒子的同步辐射（相对论推广，其中 $P = q^2 c\,\gamma^4 a_\perp^2/(6\pi\epsilon_0(m c^2)^2)$）为现代 X 射线光源提供动力。将辐射场量子化产生光子和量子电动力学（第 6、8 阶段）。

---

**Self-test (blank page)**

1. Starting from Maxwell's equations in free space, derive the wave equation for $\mathbf{E}$. Identify the speed of the wave.
2. For a plane EM wave, show that $\mathbf{E}$ and $\mathbf{B}$ are perpendicular to each other and to the direction of propagation. What is the ratio $|\mathbf{E}|/|\mathbf{B}|$?
3. Define the Poynting vector and explain its physical meaning. Compute the time-averaged intensity of a plane wave with peak electric field amplitude $E_0$.
4. State the Larmor formula. Use it to explain why classical Bohr orbits are unstable, and what physics is missing.

**自测（空白页）**

1. 从自由空间的麦克斯韦方程组出发，推导 $\mathbf{E}$ 的波动方程。指出波速。
2. 对于平面电磁波，证明 $\mathbf{E}$ 和 $\mathbf{B}$ 相互垂直，且均垂直于传播方向。$|\mathbf{E}|/|\mathbf{B}|$ 的比值是多少？
3. 定义坡印亭矢量并解释其物理意义。计算峰值电场振幅为 $E_0$ 的平面波的时间平均强度。
4. 陈述拉莫尔公式。用它解释为什么经典玻尔轨道是不稳定的，以及缺少了哪些物理。

---

← Previous: [Module 1.10 — Electrodynamics & Maxwell's Equations](./module-1.10-electrodynamics-maxwell-equations.md) · [Phase 1 index](./README.md) · Next: [Module 1.12 — Optics & Interference](./module-1.12-optics-interference.md) →

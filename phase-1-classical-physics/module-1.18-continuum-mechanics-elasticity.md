# Module 1.18 — Continuum Mechanics & Elasticity
**模块 1.18 — 连续介质力学与弹性理论**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.18-continuum-mechanics-elasticity-derivations.md)

---

## 1. Stress and Strain · 应力与应变

**Definition.** Continuum mechanics treats a deformable solid as a continuous field rather than discrete atoms. Internal forces are encoded in the **stress tensor** $\sigma_{ij}$ (the $i$-component of force per unit area on a surface with normal in the $j$-direction); deformation is encoded in the **strain tensor** $\varepsilon_{ij} = \tfrac12(\partial u_i/\partial x_j + \partial u_j/\partial x_i)$, built from the displacement field $\mathbf{u}(\mathbf{r})$. Both are rank-2 tensors (Module 0.6).

**定义。** 连续介质力学将可变形固体视为连续场而非离散原子。内力编码在**应力张量** $\sigma_{ij}$（法向为 $j$ 方向的面上 $i$ 方向的力每单位面积）中；形变编码在**应变张量** $\varepsilon_{ij} = \tfrac12(\partial u_i/\partial x_j + \partial u_j/\partial x_i)$ 中，由位移场 $\mathbf{u}(\mathbf{r})$ 构建。两者均为 2 阶张量（模块 0.6）。

**Demonstration.** For small deformations of an isotropic solid, stress is linear in strain — **Hooke's law** in tensor form $\sigma_{ij} = \lambda\,(\mathrm{tr}\,\varepsilon)\,\delta_{ij} + 2\mu\,\varepsilon_{ij}$, with the **Lamé coefficients** $\lambda$ and $\mu$ (shear modulus). In 1D this reduces to the familiar $\sigma = E\varepsilon$ with **Young's modulus** $E$; a hanging rod stretches by $\Delta L/L = \sigma/E$.

**演示。** 对于各向同性固体的小形变，应力与应变成线性关系——张量形式的**胡克定律** $\sigma_{ij} = \lambda\,(\mathrm{tr}\,\varepsilon)\,\delta_{ij} + 2\mu\,\varepsilon_{ij}$，其中 **拉梅系数** $\lambda$ 和 $\mu$（剪切模量）。在一维情形下化简为熟悉的 $\sigma = E\varepsilon$，其中 **杨氏模量** $E$；悬挂杆伸长 $\Delta L/L = \sigma/E$。

**Application.** This is the engineering foundation for beams, bridges, and materials science, and the static limit of the dynamic theory below. The same tensor bookkeeping (stress–energy) reappears as the *source* of gravity in general relativity (Module 7.4).

**应用。** 这是梁、桥梁和材料科学的工程基础，也是以下动力学理论的静态极限。同样的张量记账方式（应力–能量）在广义相对论（模块 7.4）中作为引力的*源*重新出现。

## 2. Elastic Waves & the Continuum Limit · 弹性波与连续极限

**Definition.** Newton's second law for a continuous medium, $\rho\,\partial^2 u_i/\partial t^2 = \partial\sigma_{ij}/\partial x_j$, combined with Hooke's law gives the **elastic wave equation**. An isotropic solid supports two wave types: **longitudinal (P) waves** (compression) and **transverse (S) waves** (shear), travelling at different speeds set by the elastic moduli and density.

**定义。** 连续介质的牛顿第二定律 $\rho\,\partial^2 u_i/\partial t^2 = \partial\sigma_{ij}/\partial x_j$ 与胡克定律结合，给出**弹性波方程**。各向同性固体支持两种波：**纵波（P 波）**（压缩）和**横波（S 波）**（剪切），以由弹性模量和密度决定的不同速度传播。

**Demonstration.** A crystal is *not* truly continuous; on the scale of the lattice spacing the continuum description breaks down and waves become the discrete normal modes of coupled atoms (Module 1.6). The long-wavelength acoustic phonons of a solid (Module 4.3) are exactly these elastic waves; the continuum theory is their $k \to 0$ limit.

**演示。** 晶体*并非*真正连续；在晶格间距尺度上，连续描述失效，波成为耦合原子的离散简正模式（模块 1.6）。固体的长波长声学声子（模块 4.3）正是这些弹性波；连续理论是其 $k \to 0$ 极限。

**Application.** Elastic waves are the basis of **seismology** — P and S waves from earthquakes probe the Earth's interior, and the S-wave shadow zone revealed the liquid outer core. The continuum-to-lattice connection is the bridge from this classical module to the phonons that drive heat capacity and superconductivity (Phases 4–5).

**应用。** 弹性波是**地震学**的基础——地震产生的 P 波和 S 波探测地球内部，S 波阴影区揭示了液态外核的存在。从连续到晶格的联系是从这一经典模块到驱动热容和超导性的声子（第 4–5 阶段）的桥梁。

## Key results · 核心结果

- Stress $\sigma_{ij}$ and strain $\varepsilon_{ij}$ tensors (both symmetric) · 应力与应变张量
- Isotropic Hooke's law; 1D $\sigma=E\varepsilon$ · 各向同性胡克定律
- Longitudinal (P) and transverse (S) elastic waves · 纵波与横波
- Acoustic phonons are the quantized elastic waves · 声学声子即量子化弹性波

---

**Self-test (blank page)**

1. Define the stress and strain tensors and explain why each is symmetric.
2. Write Hooke's law for an isotropic solid and reduce it to $\sigma = E\varepsilon$ in one dimension.
3. Name the two types of elastic wave in a solid and state physically why they travel at different speeds.
4. Explain how the acoustic phonon branch of a crystal relates to the classical elastic wave equation.

**自测（空白页）**

1. 定义应力张量和应变张量，并解释为什么两者都是对称的。
2. 写出各向同性固体的胡克定律，并在一维情形下将其化简为 $\sigma = E\varepsilon$。
3. 命名固体中两种弹性波的类型，并物理地解释为什么它们传播速度不同。
4. 解释晶体的声学声子支如何与经典弹性波方程相联系。

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** $\sigma_{ij}$ = force per area ($i$-component on the $j$-face); $\varepsilon_{ij}=\tfrac12(\partial_i u_j+\partial_j u_i)$. Stress is symmetric by torque (angular-momentum) balance; strain by construction (rigid rotations removed). · 二者对称的原因。
**2.** Isotropic $\sigma_{ij}=\lambda\delta_{ij}\varepsilon_{kk}+2\mu\varepsilon_{ij}$; uniaxial 1D reduces to $\sigma=E\varepsilon$ ($E$ = Young's modulus). · 一维 $\sigma=E\varepsilon$。
**3.** Longitudinal (compression, P) and transverse (shear, S) waves; P is faster because the compression modulus exceeds the shear modulus. · 纵波快于横波。
**4.** The acoustic phonon branch ($\omega=v_s k$ as $k\to0$) is the quantized long-wavelength elastic/sound wave — same linear dispersion. · 声学声子即长波弹性波的量子化。

</details>

---

← Previous: [Module 1.17 — Fluid Mechanics](./module-1.17-fluid-mechanics.md) · [Phase 1 index](./README.md) · Next: [Module 1.19 — Nonlinear Dynamics & Chaos](./module-1.19-nonlinear-dynamics-chaos.md) →

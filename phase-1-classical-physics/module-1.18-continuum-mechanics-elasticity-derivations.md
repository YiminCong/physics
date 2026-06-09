# Derivations — Module 1.18: Continuum Mechanics & Elasticity
# 推导 — 模块 1.18：连续介质力学与弹性理论

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.18](./module-1.18-continuum-mechanics-elasticity.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.18](./module-1.18-continuum-mechanics-elasticity.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Stress Tensor and Strain Tensor Definitions · 应力张量与应变张量定义

**Claim.** The internal mechanical state of a deformable solid is completely described by the symmetric stress tensor $\sigma_{ij}$ (force per unit area) and the symmetric strain tensor $\varepsilon_{ij} = \tfrac12(\partial u_i/\partial x_j + \partial u_j/\partial x_i)$ (symmetrized displacement gradient).

**命题。** 可变形固体的内部力学状态完全由对称应力张量 $\sigma_{ij}$（单位面积的力）和对称应变张量 $\varepsilon_{ij} = \tfrac12(\partial u_i/\partial x_j + \partial u_j/\partial x_i)$（对称化的位移梯度）描述。

**Step 1 — Define the stress tensor.** Consider a surface element inside the solid with outward normal $\mathbf{n} = n_j\hat{e}_j$. The traction (force per unit area) exerted on the positive side by the negative side is

**第 1 步 — 定义应力张量。** 考虑固体内部法向为 $\mathbf{n} = n_j\hat{e}_j$ 的面元。正侧对负侧施加的牵引力（单位面积的力）为

$$ t_i = \sigma_{ij} n_j \qquad \text{(Cauchy's formula).} $$

The 9 components $\sigma_{ij}$ form the **stress tensor**: $\sigma_{ij}$ is the $i$-th component of force per unit area on a surface whose outward normal points in the $j$-direction. Off-diagonal components represent shear stresses; diagonal components are normal (tensile/compressive) stresses.

9 个分量 $\sigma_{ij}$ 构成**应力张量**：$\sigma_{ij}$ 是法向指向 $j$ 方向的面上 $i$ 方向的力每单位面积。非对角分量代表剪切应力；对角分量为法向（拉伸/压缩）应力。

**Step 2 — Symmetry of $\sigma_{ij}$.** Consider the torque on a small cube of side $\varepsilon$. The torque from $\sigma_{12}$ (force in $x_1$-direction on $x_2$-faces) is $\sim \sigma_{12}\varepsilon^2 \cdot (\varepsilon/2)$, acting to rotate the cube. Summing all such contributions and requiring the angular momentum of the cube ($\sim \rho\varepsilon^3 \cdot \varepsilon^2/12 \cdot \alpha$) to remain finite as $\varepsilon \to 0$ gives $\sigma_{12} = \sigma_{21}$. In general: $\sigma_{ij} = \sigma_{ji}$ (6 independent components).

**第 2 步 — $\sigma_{ij}$ 的对称性。** 考虑边长为 $\varepsilon$ 的小立方体所受力矩。$\sigma_{12}$（$x_2$ 面上 $x_1$ 方向的力）产生的力矩 $\sim \sigma_{12}\varepsilon^2 \cdot (\varepsilon/2)$。要求 $\varepsilon \to 0$ 时角动量（$\sim \rho\varepsilon^3 \cdot \varepsilon^2/12 \cdot \alpha$）保持有限，得 $\sigma_{12} = \sigma_{21}$。一般地：$\sigma_{ij} = \sigma_{ji}$（6 个独立分量）。

**Step 3 — Define the displacement and strain.** Let $\mathbf{u}(\mathbf{r})$ be the displacement field (vector from original to current position). The deformation gradient $\partial u_i/\partial x_j$ in general contains both stretching and rotation. To isolate the stretching (which produces stress), symmetrize:

**第 3 步 — 定义位移与应变。** 设 $\mathbf{u}(\mathbf{r})$ 为位移场（从原始位置到当前位置的矢量）。变形梯度 $\partial u_i/\partial x_j$ 一般同时包含拉伸和旋转。为分离产生应力的拉伸部分，对称化：

$$ \varepsilon_{ij} = \tfrac12(\partial u_i/\partial x_j + \partial u_j/\partial x_i). $$

The antisymmetric part $\omega_{ij} = \tfrac12(\partial u_i/\partial x_j - \partial u_j/\partial x_i)$ describes rigid-body rotation (no stress). $\varepsilon_{ij} = \varepsilon_{ji}$ by construction (6 independent components).

反对称部分 $\omega_{ij} = \tfrac12(\partial u_i/\partial x_j - \partial u_j/\partial x_i)$ 描述刚体转动（不产生应力）。由构造知 $\varepsilon_{ij} = \varepsilon_{ji}$（6 个独立分量）。

**Step 4 — Physical meaning of strain components.** The diagonal element $\varepsilon_{11} = \partial u_1/\partial x_1$ is the fractional elongation in the $x_1$-direction. The trace $\mathrm{tr}\,\varepsilon = \varepsilon_{ii} = \nabla\cdot\mathbf{u}$ is the fractional volume change (dilation). The off-diagonal element $\varepsilon_{12} = \tfrac12(\partial u_1/\partial x_2 + \partial u_2/\partial x_1)$ measures the shear angle.

**第 4 步 — 应变分量的物理意义。** 对角元 $\varepsilon_{11} = \partial u_1/\partial x_1$ 是 $x_1$ 方向的相对伸长量。迹 $\mathrm{tr}\,\varepsilon = \varepsilon_{ii} = \nabla\cdot\mathbf{u}$ 是相对体积变化（膨胀）。非对角元 $\varepsilon_{12} = \tfrac12(\partial u_1/\partial x_2 + \partial u_2/\partial x_1)$ 度量剪切角。

---

## B. Hooke's Law for an Isotropic Solid: $\sigma_{ij} = \lambda(\mathrm{tr}\,\varepsilon)\delta_{ij} + 2\mu\varepsilon_{ij}$ · 各向同性固体的胡克定律

**Claim.** For small deformations of an isotropic, linear elastic solid, the most general stress-strain relationship consistent with isotropy (no preferred direction) and linearity is $\sigma_{ij} = \lambda(\mathrm{tr}\,\varepsilon)\delta_{ij} + 2\mu\varepsilon_{ij}$, with Lamé coefficients $\lambda$ and $\mu$.

**命题。** 对各向同性线弹性固体的小变形，与各向同性（无特殊方向）和线性一致的最一般应力-应变关系为 $\sigma_{ij} = \lambda(\mathrm{tr}\,\varepsilon)\delta_{ij} + 2\mu\varepsilon_{ij}$，其中 $\lambda$ 和 $\mu$ 为拉梅系数。

**Step 1 — Most general linear isotropic tensor relation.** By the quotient theorem of tensor algebra, a linear relation $\sigma_{ij} = C_{ijkl}\,\varepsilon_{kl}$ requires a rank-4 tensor $C_{ijkl}$. For an isotropic material, the most general rank-4 isotropic tensor with the symmetries $C_{ijkl} = C_{jikl} = C_{ijlk} = C_{klij}$ is

**第 1 步 — 最一般的线性各向同性张量关系。** 由张量代数的商定理，线性关系 $\sigma_{ij} = C_{ijkl}\,\varepsilon_{kl}$ 需要 4 阶张量 $C_{ijkl}$。对各向同性材料，具有对称性 $C_{ijkl} = C_{jikl} = C_{ijlk} = C_{klij}$ 的最一般 4 阶各向同性张量为

$$ C_{ijkl} = \lambda\,\delta_{ij}\delta_{kl} + \mu(\delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk}), $$

with two independent constants $\lambda$ and $\mu$ (the **Lamé coefficients**). This follows from the fact that in 3D, a rank-4 isotropic tensor decomposes into exactly two independent isotropic tensors: $\delta_{ij}\delta_{kl}$ and $(\delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk})/2$.

两个独立常数 $\lambda$ 和 $\mu$ 即**拉梅系数**。这来自于在三维中，4 阶各向同性张量恰好分解为两个独立各向同性张量：$\delta_{ij}\delta_{kl}$ 与 $(\delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk})/2$。

**Step 2 — Evaluate the contraction.** Computing $\sigma_{ij} = C_{ijkl}\,\varepsilon_{kl}$:

**第 2 步 — 计算缩并。** 计算 $\sigma_{ij} = C_{ijkl}\,\varepsilon_{kl}$：

$$ \begin{aligned}
\sigma_{ij} &= \lambda\,\delta_{ij}\delta_{kl}\,\varepsilon_{kl} + \mu(\delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk})\,\varepsilon_{kl} \\
&= \lambda\,\delta_{ij}\,\varepsilon_{kk} + \mu(\varepsilon_{ij} + \varepsilon_{ji}) \\
&= \lambda\,(\mathrm{tr}\,\varepsilon)\,\delta_{ij} + 2\mu\,\varepsilon_{ij}, \qquad [\text{using } \varepsilon_{ij} = \varepsilon_{ji}].
\end{aligned} $$

So $\boxed{\, \sigma_{ij} = \lambda(\mathrm{tr}\,\varepsilon)\delta_{ij} + 2\mu\varepsilon_{ij} \,}$. $\blacksquare$

故 $\boxed{\, \sigma_{ij} = \lambda(\mathrm{tr}\,\varepsilon)\delta_{ij} + 2\mu\varepsilon_{ij} \,}$。$\blacksquare$

**Step 3 — Reduction to 1D (Young's modulus).** In a uniaxial test, stress is applied only in the $x_1$-direction: $\sigma_{11} = \sigma \ne 0$, $\sigma_{ij} = 0$ for $(i,j) \ne (1,1)$. From $\sigma_{22} = \lambda(\varepsilon_{11} + \varepsilon_{22} + \varepsilon_{33}) + 2\mu\varepsilon_{22} = 0$ and similarly $\sigma_{33} = 0$, by symmetry $\varepsilon_{22} = \varepsilon_{33} \equiv \varepsilon_\perp$. Then:

**第 3 步 — 化简到一维（杨氏模量）。** 在单轴拉伸试验中，仅在 $x_1$ 方向施加应力：$\sigma_{11} = \sigma \ne 0$，其余 $\sigma_{ij} = 0$。由对称性 $\varepsilon_{22} = \varepsilon_{33} \equiv \varepsilon_\perp$，则由 $\sigma_{22} = 0$：

$$ 0 = \lambda(\varepsilon_{11} + 2\varepsilon_\perp) + 2\mu\varepsilon_\perp \implies \varepsilon_\perp = -\lambda\varepsilon_{11}/(2(\lambda + \mu)). $$

Substituting back into $\sigma_{11} = \lambda(\varepsilon_{11} + 2\varepsilon_\perp) + 2\mu\varepsilon_{11}$:

代回 $\sigma_{11}$：

$$ \begin{aligned}
\sigma &= \lambda(\varepsilon_{11} + 2\varepsilon_\perp) + 2\mu\varepsilon_{11} \\
&= \lambda(\varepsilon_{11} - 2\lambda\varepsilon_{11}/(2(\lambda+\mu))) + 2\mu\varepsilon_{11} \\
&= \lambda\varepsilon_{11}(1 - \lambda/(\lambda+\mu)) + 2\mu\varepsilon_{11} \\
&= \lambda\varepsilon_{11} \cdot \mu/(\lambda+\mu) + 2\mu\varepsilon_{11} \\
&= \mu\varepsilon_{11}(\lambda/(\lambda+\mu) + 2) \\
&= \mu\varepsilon_{11} \cdot (\lambda + 2\lambda + 2\mu)/(\lambda+\mu) \\
&= \mu\varepsilon_{11} \cdot (3\lambda + 2\mu)/(\lambda+\mu).
\end{aligned} $$

Hence $\sigma = E\varepsilon_{11}$ with Young's modulus

故 $\sigma = E\varepsilon_{11}$，杨氏模量为

$$ \boxed{\, E = \mu(3\lambda + 2\mu)/(\lambda + \mu) \,} \quad\checkmark $$

The Poisson ratio $\nu = -\varepsilon_\perp/\varepsilon_{11} = \lambda/(2(\lambda+\mu))$.

泊松比 $\nu = -\varepsilon_\perp/\varepsilon_{11} = \lambda/(2(\lambda+\mu))$。

---

## C. The Elastic Wave Equation · 弹性波方程推导

**Claim.** Combining Newton's second law for a continuum $\rho\ddot{u}_i = \partial_j\sigma_{ij}$ with the isotropic Hooke's law yields the elastic wave equation, which supports P-waves (longitudinal, speed $v_P$) and S-waves (transverse, speed $v_S$):

**命题。** 将连续介质牛顿第二定律 $\rho\ddot{u}_i = \partial_j\sigma_{ij}$ 与各向同性胡克定律结合，得到弹性波方程，支持 P 波（纵波，速度 $v_P$）和 S 波（横波，速度 $v_S$）：

$$ v_P = \sqrt{(\lambda + 2\mu)/\rho}, \qquad v_S = \sqrt{\mu/\rho}. $$

**Step 1 — Equation of motion.** For a body with no external body forces, Newton's second law per unit volume for the $i$-th component of displacement is

**第 1 步 — 运动方程。** 对无外体力的物体，位移 $i$ 分量的单位体积牛顿第二定律为

$$ \rho\,\partial^2 u_i/\partial t^2 = \partial\sigma_{ij}/\partial x_j \qquad \text{(sum over } j\text{).} $$

**Step 2 — Substitute Hooke's law.** Substitute $\sigma_{ij} = \lambda(\partial_k u_k)\delta_{ij} + \mu(\partial_j u_i + \partial_i u_j)$ [using $\varepsilon_{ij} = \tfrac12(\partial_j u_i + \partial_i u_j)$ and the Lamé form]:

**第 2 步 — 代入胡克定律。** 代入 $\sigma_{ij} = \lambda(\partial_k u_k)\delta_{ij} + \mu(\partial_j u_i + \partial_i u_j)$：

$$ \begin{aligned}
\partial\sigma_{ij}/\partial x_j &= \lambda\,\partial_i(\partial_k u_k) + \mu\,\partial_j(\partial_j u_i + \partial_i u_j) \\
&= \lambda\,\partial_i(\nabla\cdot\mathbf{u}) + \mu(\nabla^2 u_i + \partial_i(\nabla\cdot\mathbf{u})) \\
&= (\lambda + \mu)\,\partial_i(\nabla\cdot\mathbf{u}) + \mu\,\nabla^2 u_i.
\end{aligned} $$

So the equation of motion is:

故运动方程为：

$$ \rho\,\partial^2\mathbf{u}/\partial t^2 = (\lambda + \mu)\,\nabla(\nabla\cdot\mathbf{u}) + \mu\,\nabla^2\mathbf{u}. $$

Using the vector identity $\nabla^2\mathbf{u} = \nabla(\nabla\cdot\mathbf{u}) - \nabla\times(\nabla\times\mathbf{u})$:

利用矢量恒等式 $\nabla^2\mathbf{u} = \nabla(\nabla\cdot\mathbf{u}) - \nabla\times(\nabla\times\mathbf{u})$：

$$ \rho\,\partial^2\mathbf{u}/\partial t^2 = (\lambda + 2\mu)\,\nabla(\nabla\cdot\mathbf{u}) - \mu\,\nabla\times(\nabla\times\mathbf{u}). \qquad \blacksquare $$

**Step 3 — Separate into P-waves (longitudinal).** Apply $\nabla\cdot$ to the wave equation. Define the dilatation $\phi = \nabla\cdot\mathbf{u}$:

**第 3 步 — 分离出 P 波（纵波）。** 对波动方程取 $\nabla\cdot$。定义膨胀量 $\phi = \nabla\cdot\mathbf{u}$：

$$ \rho\,\partial^2\phi/\partial t^2 = (\lambda + 2\mu)\,\nabla^2\phi - \mu\,\nabla\cdot(\nabla\times(\nabla\times\mathbf{u})). $$

Since $\nabla\cdot(\nabla\times\mathbf{A}) = 0$ for any vector $\mathbf{A}$, the last term vanishes:

由于 $\nabla\cdot(\nabla\times\mathbf{A}) = 0$，最后一项消失：

$$ \rho\,\partial^2\phi/\partial t^2 = (\lambda + 2\mu)\,\nabla^2\phi. $$

This is a wave equation for $\phi$ with speed

这是 $\phi$ 的波动方程，波速为

$$ \boxed{\, v_P = \sqrt{(\lambda + 2\mu)/\rho} \,} \qquad \blacksquare $$

P-waves are **compressional (longitudinal)** — the displacement is parallel to the propagation direction.

P 波为**压缩（纵）波**——位移平行于传播方向。

**Step 4 — Separate into S-waves (transverse).** Apply $\nabla\times$ to the wave equation. Define the rotation vector $\boldsymbol{\psi} = \nabla\times\mathbf{u}$:

**第 4 步 — 分离出 S 波（横波）。** 对波动方程取 $\nabla\times$。定义旋转矢量 $\boldsymbol{\psi} = \nabla\times\mathbf{u}$：

$$ \rho\,\partial^2\boldsymbol{\psi}/\partial t^2 = (\lambda + 2\mu)\nabla\times[\nabla(\nabla\cdot\mathbf{u})] - \mu\,\nabla\times[\nabla\times(\nabla\times\mathbf{u})]. $$

Since $\nabla\times\nabla(f) = 0$ for any scalar $f$, the first term vanishes. Using $\nabla\times(\nabla\times\boldsymbol{\psi}) = \nabla(\nabla\cdot\boldsymbol{\psi}) - \nabla^2\boldsymbol{\psi}$ and $\nabla\cdot\boldsymbol{\psi} = \nabla\cdot(\nabla\times\mathbf{u}) = 0$:

由于 $\nabla\times\nabla(f) = 0$，第一项消失。利用 $\nabla\cdot(\nabla\times\mathbf{u}) = 0$：

$$ \rho\,\partial^2\boldsymbol{\psi}/\partial t^2 = -\mu(-\nabla^2\boldsymbol{\psi}) = \mu\,\nabla^2\boldsymbol{\psi}. $$

This is a vector wave equation for $\boldsymbol{\psi} = \nabla\times\mathbf{u}$ with speed

这是 $\boldsymbol{\psi} = \nabla\times\mathbf{u}$ 的矢量波动方程，波速为

$$ \boxed{\, v_S = \sqrt{\mu/\rho} \,} \qquad \blacksquare $$

S-waves are **shear (transverse)** — the displacement is perpendicular to the propagation direction. Since $\lambda + 2\mu > \mu$ always (as $\lambda \ge 0$ for stable materials), we have $v_P > v_S$: P-waves travel faster than S-waves. In a liquid $\mu = 0$ (no shear stiffness), so $v_S = 0$ — liquids do not support shear waves, only P-waves (sound). This is why the absence of S-waves in Earth's outer core proves it is liquid.

S 波为**剪切（横）波**——位移垂直于传播方向。由于 $\lambda + 2\mu > \mu$（稳定材料 $\lambda \ge 0$），故 $v_P > v_S$：P 波比 S 波传播更快。在液体中 $\mu = 0$（无剪切刚度），故 $v_S = 0$——液体不支持剪切波，只支持 P 波（声波）。这就是为什么地球外核中 S 波的消失证明外核是液态的。

---

## D. Relation to the Lame Coefficients and Physical Moduli · 拉梅系数与物理模量的关系

**Summary table.** The Lamé coefficients $\lambda$ and $\mu$ relate to the measurable moduli:

**汇总表。** 拉梅系数 $\lambda$ 和 $\mu$ 与可测量模量的关系：

$$ \begin{aligned}
\text{Young's modulus:} \quad & E = \mu(3\lambda + 2\mu)/(\lambda + \mu) \\
\text{Bulk modulus:} \quad & K = \lambda + 2\mu/3 \\
\text{Poisson ratio:} \quad & \nu = \lambda/(2(\lambda + \mu)) \\
\text{Shear modulus:} \quad & G = \mu
\end{aligned} $$

The wave speeds in terms of physical moduli:

用物理模量表达波速：

$$ \begin{aligned}
v_P &= \sqrt{(K + 4G/3)/\rho} = \sqrt{E(1-\nu)/((1+\nu)(1-2\nu)\rho)}, \\
v_S &= \sqrt{G/\rho} = \sqrt{E/(2(1+\nu)\rho)}.
\end{aligned} $$

**Typical values for steel:** $E \approx 200\ \mathrm{GPa}$, $\rho \approx 7800\ \mathrm{kg/m^3}$, $\nu \approx 0.3$, giving $v_P \approx 5900\ \mathrm{m/s}$ and $v_S \approx 3200\ \mathrm{m/s}$.

**钢的典型值：** $E \approx 200\ \mathrm{GPa}$，$\rho \approx 7800\ \mathrm{kg/m^3}$，$\nu \approx 0.3$，给出 $v_P \approx 5900\ \mathrm{m/s}$，$v_S \approx 3200\ \mathrm{m/s}$。$\blacksquare$

---

*The elastic wave equation is a direct consequence of Newton's second law applied to a continuous medium with Hooke's law. The decomposition into P and S waves via divergence and curl mirrors the Helmholtz decomposition of any vector field into longitudinal (curl-free) and transverse (divergence-free) parts.*

*弹性波方程是牛顿第二定律应用于满足胡克定律的连续介质的直接结果。通过散度和旋度将其分解为 P 波和 S 波，与任意矢量场的亥姆霍兹分解（纵向无旋部分和横向无散部分）相对应。*

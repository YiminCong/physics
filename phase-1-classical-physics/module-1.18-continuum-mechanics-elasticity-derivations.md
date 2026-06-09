# Derivations — Module 1.18: Continuum Mechanics & Elasticity
# 推导 — 模块 1.18：连续介质力学与弹性理论

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.18](./module-1.18-continuum-mechanics-elasticity.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.18](./module-1.18-continuum-mechanics-elasticity.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Stress Tensor and Strain Tensor Definitions · 应力张量与应变张量定义

**Claim.** The internal mechanical state of a deformable solid is completely described by the symmetric stress tensor σ_{ij} (force per unit area) and the symmetric strain tensor ε_{ij} = ½(∂u_i/∂x_j + ∂u_j/∂x_i) (symmetrized displacement gradient).

**命题。** 可变形固体的内部力学状态完全由对称应力张量 σ_{ij}（单位面积的力）和对称应变张量 ε_{ij} = ½(∂u_i/∂x_j + ∂u_j/∂x_i)（对称化的位移梯度）描述。

**Step 1 — Define the stress tensor.** Consider a surface element inside the solid with outward normal **n** = n_j ê_j. The traction (force per unit area) exerted on the positive side by the negative side is

**第 1 步 — 定义应力张量。** 考虑固体内部法向为 **n** = n_j ê_j 的面元。正侧对负侧施加的牵引力（单位面积的力）为

  t_i = σ_{ij} n_j   (Cauchy's formula).

The 9 components σ_{ij} form the **stress tensor**: σ_{ij} is the i-th component of force per unit area on a surface whose outward normal points in the j-direction. Off-diagonal components represent shear stresses; diagonal components are normal (tensile/compressive) stresses.

9 个分量 σ_{ij} 构成**应力张量**：σ_{ij} 是法向指向 j 方向的面上 i 方向的力每单位面积。非对角分量代表剪切应力；对角分量为法向（拉伸/压缩）应力。

**Step 2 — Symmetry of σ_{ij}.** Consider the torque on a small cube of side ε. The torque from σ_{12} (force in x₁-direction on x₂-faces) is ~ σ_{12} ε² · (ε/2), acting to rotate the cube. Summing all such contributions and requiring the angular momentum of the cube (~ ρε³ · ε²/12 · α) to remain finite as ε → 0 gives σ_{12} = σ_{21}. In general: **σ_{ij} = σ_{ji}** (6 independent components).

**第 2 步 — σ_{ij} 的对称性。** 考虑边长为 ε 的小立方体所受力矩。σ_{12}（x₂ 面上 x₁ 方向的力）产生的力矩 ~ σ_{12} ε² · (ε/2)。要求 ε → 0 时角动量（~ ρε³ · ε²/12 · α）保持有限，得 σ_{12} = σ_{21}。一般地：**σ_{ij} = σ_{ji}**（6 个独立分量）。

**Step 3 — Define the displacement and strain.** Let **u**(**r**) be the displacement field (vector from original to current position). The deformation gradient ∂u_i/∂x_j in general contains both stretching and rotation. To isolate the stretching (which produces stress), symmetrize:

**第 3 步 — 定义位移与应变。** 设 **u**(**r**) 为位移场（从原始位置到当前位置的矢量）。变形梯度 ∂u_i/∂x_j 一般同时包含拉伸和旋转。为分离产生应力的拉伸部分，对称化：

  ε_{ij} = ½(∂u_i/∂x_j + ∂u_j/∂x_i).

The antisymmetric part ω_{ij} = ½(∂u_i/∂x_j − ∂u_j/∂x_i) describes rigid-body rotation (no stress). **ε_{ij} = ε_{ji}** by construction (6 independent components).

反对称部分 ω_{ij} = ½(∂u_i/∂x_j − ∂u_j/∂x_i) 描述刚体转动（不产生应力）。由构造知 **ε_{ij} = ε_{ji}**（6 个独立分量）。

**Step 4 — Physical meaning of strain components.** The diagonal element ε_{11} = ∂u_1/∂x_1 is the fractional elongation in the x₁-direction. The trace tr ε = ε_{ii} = ∇·**u** is the fractional volume change (dilation). The off-diagonal element ε_{12} = ½(∂u_1/∂x_2 + ∂u_2/∂x_1) measures the shear angle.

**第 4 步 — 应变分量的物理意义。** 对角元 ε_{11} = ∂u_1/∂x_1 是 x₁ 方向的相对伸长量。迹 tr ε = ε_{ii} = ∇·**u** 是相对体积变化（膨胀）。非对角元 ε_{12} = ½(∂u_1/∂x_2 + ∂u_2/∂x_1) 度量剪切角。

---

## B. Hooke's Law for an Isotropic Solid: σ_{ij} = λ(tr ε)δ_{ij} + 2με_{ij} · 各向同性固体的胡克定律

**Claim.** For small deformations of an isotropic, linear elastic solid, the most general stress-strain relationship consistent with isotropy (no preferred direction) and linearity is σ_{ij} = λ(tr ε)δ_{ij} + 2με_{ij}, with Lamé coefficients λ and μ.

**命题。** 对各向同性线弹性固体的小变形，与各向同性（无特殊方向）和线性一致的最一般应力-应变关系为 σ_{ij} = λ(tr ε)δ_{ij} + 2με_{ij}，其中 λ 和 μ 为拉梅系数。

**Step 1 — Most general linear isotropic tensor relation.** By the quotient theorem of tensor algebra, a linear relation σ_{ij} = C_{ijkl} ε_{kl} requires a rank-4 tensor C_{ijkl}. For an isotropic material, the most general rank-4 isotropic tensor with the symmetries C_{ijkl} = C_{jikl} = C_{ijlk} = C_{klij} is

**第 1 步 — 最一般的线性各向同性张量关系。** 由张量代数的商定理，线性关系 σ_{ij} = C_{ijkl} ε_{kl} 需要 4 阶张量 C_{ijkl}。对各向同性材料，具有对称性 C_{ijkl} = C_{jikl} = C_{ijlk} = C_{klij} 的最一般 4 阶各向同性张量为

  C_{ijkl} = λ δ_{ij} δ_{kl} + μ(δ_{ik} δ_{jl} + δ_{il} δ_{jk}),

with two independent constants λ and μ (the **Lamé coefficients**). This follows from the fact that in 3D, a rank-4 isotropic tensor decomposes into exactly two independent isotropic tensors: δ_{ij}δ_{kl} and (δ_{ik}δ_{jl} + δ_{il}δ_{jk})/2.

两个独立常数 λ 和 μ 即**拉梅系数**。这来自于在三维中，4 阶各向同性张量恰好分解为两个独立各向同性张量：δ_{ij}δ_{kl} 与 (δ_{ik}δ_{jl} + δ_{il}δ_{jk})/2。

**Step 2 — Evaluate the contraction.** Computing σ_{ij} = C_{ijkl} ε_{kl}:

**第 2 步 — 计算缩并。** 计算 σ_{ij} = C_{ijkl} ε_{kl}：

  σ_{ij} = λ δ_{ij} δ_{kl} ε_{kl} + μ(δ_{ik} δ_{jl} + δ_{il} δ_{jk}) ε_{kl}
          = λ δ_{ij} ε_{kk} + μ(ε_{ij} + ε_{ji})
          = λ (tr ε) δ_{ij} + 2μ ε_{ij},   [using ε_{ij} = ε_{ji}].

So **σ_{ij} = λ(tr ε)δ_{ij} + 2με_{ij}**. ∎

故 **σ_{ij} = λ(tr ε)δ_{ij} + 2με_{ij}**。∎

**Step 3 — Reduction to 1D (Young's modulus).** In a uniaxial test, stress is applied only in the x₁-direction: σ_{11} = σ ≠ 0, σ_{ij} = 0 for (i,j) ≠ (1,1). From σ_{22} = λ(ε_{11} + ε_{22} + ε_{33}) + 2με_{22} = 0 and similarly σ_{33} = 0, by symmetry ε_{22} = ε_{33} ≡ ε_⊥. Then:

**第 3 步 — 化简到一维（杨氏模量）。** 在单轴拉伸试验中，仅在 x₁ 方向施加应力：σ_{11} = σ ≠ 0，其余 σ_{ij} = 0。由对称性 ε_{22} = ε_{33} ≡ ε_⊥，则由 σ_{22} = 0：

  0 = λ(ε_{11} + 2ε_⊥) + 2με_⊥  ⟹  ε_⊥ = −λε_{11}/(2(λ + μ)).

Substituting back into σ_{11} = λ(ε_{11} + 2ε_⊥) + 2με_{11}:

代回 σ_{11}：

  σ = λ(ε_{11} + 2ε_⊥) + 2με_{11}
    = λ(ε_{11} − 2λε_{11}/(2(λ+μ))) + 2με_{11}
    = λε_{11}(1 − λ/(λ+μ)) + 2με_{11}
    = λε_{11} · μ/(λ+μ) + 2με_{11}
    = με_{11}(λ/(λ+μ) + 2)
    = με_{11} · (λ + 2λ + 2μ)/(λ+μ)
    = με_{11} · (3λ + 2μ)/(λ+μ).

Hence σ = E ε_{11} with Young's modulus

故 σ = E ε_{11}，杨氏模量为

  **E = μ(3λ + 2μ)/(λ + μ)**. ✓

The Poisson ratio ν = −ε_⊥/ε_{11} = λ/(2(λ+μ)).

泊松比 ν = −ε_⊥/ε_{11} = λ/(2(λ+μ))。

---

## C. The Elastic Wave Equation · 弹性波方程推导

**Claim.** Combining Newton's second law for a continuum ρü_i = ∂_j σ_{ij} with the isotropic Hooke's law yields the elastic wave equation, which supports P-waves (longitudinal, speed v_P) and S-waves (transverse, speed v_S):

**命题。** 将连续介质牛顿第二定律 ρü_i = ∂_j σ_{ij} 与各向同性胡克定律结合，得到弹性波方程，支持 P 波（纵波，速度 v_P）和 S 波（横波，速度 v_S）：

  v_P = √((λ + 2μ)/ρ),   v_S = √(μ/ρ).

**Step 1 — Equation of motion.** For a body with no external body forces, Newton's second law per unit volume for the i-th component of displacement is

**第 1 步 — 运动方程。** 对无外体力的物体，位移 i 分量的单位体积牛顿第二定律为

  ρ ∂²u_i/∂t² = ∂σ_{ij}/∂x_j   (sum over j).

**Step 2 — Substitute Hooke's law.** Substitute σ_{ij} = λ(∂_k u_k)δ_{ij} + μ(∂_j u_i + ∂_i u_j) [using ε_{ij} = ½(∂_j u_i + ∂_i u_j) and the Lamé form]:

**第 2 步 — 代入胡克定律。** 代入 σ_{ij} = λ(∂_k u_k)δ_{ij} + μ(∂_j u_i + ∂_i u_j)：

  ∂σ_{ij}/∂x_j = λ ∂_i(∂_k u_k) + μ ∂_j(∂_j u_i + ∂_i u_j)
               = λ ∂_i(∇·**u**) + μ(∇²u_i + ∂_i(∇·**u**))
               = (λ + μ) ∂_i(∇·**u**) + μ ∇²u_i.

So the equation of motion is:

故运动方程为：

  ρ ∂²**u**/∂t² = (λ + μ) ∇(∇·**u**) + μ ∇²**u**.

Using the vector identity ∇²**u** = ∇(∇·**u**) − ∇×(∇×**u**):

利用矢量恒等式 ∇²**u** = ∇(∇·**u**) − ∇×(∇×**u**)：

  ρ ∂²**u**/∂t² = (λ + 2μ) ∇(∇·**u**) − μ ∇×(∇×**u**). ∎

**Step 3 — Separate into P-waves (longitudinal).** Apply ∇· to the wave equation. Define the dilatation φ = ∇·**u**:

**第 3 步 — 分离出 P 波（纵波）。** 对波动方程取 ∇·。定义膨胀量 φ = ∇·**u**：

  ρ ∂²φ/∂t² = (λ + 2μ) ∇²φ − μ ∇·(∇×(∇×**u**)).

Since ∇·(∇×**A**) = 0 for any vector **A**, the last term vanishes:

由于 ∇·(∇×**A**) = 0，最后一项消失：

  ρ ∂²φ/∂t² = (λ + 2μ) ∇²φ.

This is a wave equation for φ with speed

这是 φ 的波动方程，波速为

  **v_P = √((λ + 2μ)/ρ)**. ∎

P-waves are **compressional (longitudinal)** — the displacement is parallel to the propagation direction.

P 波为**压缩（纵）波**——位移平行于传播方向。

**Step 4 — Separate into S-waves (transverse).** Apply ∇× to the wave equation. Define the rotation vector **ψ** = ∇×**u**:

**第 4 步 — 分离出 S 波（横波）。** 对波动方程取 ∇×。定义旋转矢量 **ψ** = ∇×**u**：

  ρ ∂²**ψ**/∂t² = (λ + 2μ)∇×[∇(∇·**u**)] − μ ∇×[∇×(∇×**u**)].

Since ∇×∇(f) = 0 for any scalar f, the first term vanishes. Using ∇×(∇×**ψ**) = ∇(∇·**ψ**) − ∇²**ψ** and ∇·**ψ** = ∇·(∇×**u**) = 0:

由于 ∇×∇(f) = 0，第一项消失。利用 ∇·(∇×**u**) = 0：

  ρ ∂²**ψ**/∂t² = −μ(−∇²**ψ**) = μ ∇²**ψ**.

This is a vector wave equation for **ψ** = ∇×**u** with speed

这是 **ψ** = ∇×**u** 的矢量波动方程，波速为

  **v_S = √(μ/ρ)**. ∎

S-waves are **shear (transverse)** — the displacement is perpendicular to the propagation direction. Since λ + 2μ > μ always (as λ ≥ 0 for stable materials), we have **v_P > v_S**: P-waves travel faster than S-waves. In a liquid μ = 0 (no shear stiffness), so v_S = 0 — liquids do not support shear waves, only P-waves (sound). This is why the absence of S-waves in Earth's outer core proves it is liquid.

S 波为**剪切（横）波**——位移垂直于传播方向。由于 λ + 2μ > μ（稳定材料 λ ≥ 0），故 **v_P > v_S**：P 波比 S 波传播更快。在液体中 μ = 0（无剪切刚度），故 v_S = 0——液体不支持剪切波，只支持 P 波（声波）。这就是为什么地球外核中 S 波的消失证明外核是液态的。

---

## D. Relation to the Lame Coefficients and Physical Moduli · 拉梅系数与物理模量的关系

**Summary table.** The Lamé coefficients λ and μ relate to the measurable moduli:

**汇总表。** 拉梅系数 λ 和 μ 与可测量模量的关系：

  Young's modulus:   E = μ(3λ + 2μ)/(λ + μ)
  Bulk modulus:      K = λ + 2μ/3
  Poisson ratio:     ν = λ/(2(λ + μ))
  Shear modulus:     G = μ

The wave speeds in terms of physical moduli:

用物理模量表达波速：

  v_P = √((K + 4G/3)/ρ) = √(E(1−ν)/((1+ν)(1−2ν)ρ)),
  v_S = √(G/ρ) = √(E/(2(1+ν)ρ)).

**Typical values for steel:** E ≈ 200 GPa, ρ ≈ 7800 kg/m³, ν ≈ 0.3, giving v_P ≈ 5900 m/s and v_S ≈ 3200 m/s.

**钢的典型值：** E ≈ 200 GPa，ρ ≈ 7800 kg/m³，ν ≈ 0.3，给出 v_P ≈ 5900 m/s，v_S ≈ 3200 m/s。∎

---

*The elastic wave equation is a direct consequence of Newton's second law applied to a continuous medium with Hooke's law. The decomposition into P and S waves via divergence and curl mirrors the Helmholtz decomposition of any vector field into longitudinal (curl-free) and transverse (divergence-free) parts.*

*弹性波方程是牛顿第二定律应用于满足胡克定律的连续介质的直接结果。通过散度和旋度将其分解为 P 波和 S 波，与任意矢量场的亥姆霍兹分解（纵向无旋部分和横向无散部分）相对应。*

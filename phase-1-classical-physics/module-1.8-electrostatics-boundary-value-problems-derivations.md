# Derivations — Module 1.8: Electrostatics & Boundary-Value Problems
# 推导 — 模块 1.8：静电学与边值问题

> Companion to [Module 1.8](./module-1.8-electrostatics-boundary-value-problems.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.8](./module-1.8-electrostatics-boundary-value-problems.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Gauss's Law from Coulomb's Law via Solid Angle and the Divergence Theorem · 从库仑定律经立体角与散度定理推导高斯定律

**Claim.** For any charge distribution ρ(r), ∮_S E · dA = Q_enc / ε₀ and ∇ · E = ρ / ε₀.

**命题。** 对任意电荷分布 ρ(r)，∮_S E · dA = Q_enc / ε₀ 且 ∇ · E = ρ / ε₀。

**Step 1 — Coulomb field of a point charge.** A point charge q at the origin produces an electric field at position r:

**第 1 步 — 点电荷的库仑场。** 位于原点的点电荷 q 在位置 r 处产生电场：

  E(r) = q / (4πε₀) · r̂ / r²  =  q / (4πε₀) · r / r³.

This follows from Coulomb's force law F = qQ r̂/(4πε₀r²) by defining E = F/Q for a test charge Q → 0.

这由库仑力定律 F = qQ r̂/(4πε₀r²) 出发，对试验电荷 Q → 0 取极限定义 E = F/Q 而得。

**Step 2 — Flux through an arbitrary closed surface enclosing q.** Consider the flux integral ∮_S E · dA over any smooth closed surface S enclosing the charge. The area element dA = n̂ dA has outward normal n̂. The integrand is:

**第 2 步 — 包围 q 的任意闭合曲面上的通量。** 考虑包围电荷的任意光滑闭合曲面 S 上的通量积分 ∮_S E · dA。面积元 dA = n̂ dA，n̂ 为外法线方向。被积量为：

  E · dA = q / (4πε₀) · (r̂ · n̂) / r² dA.

The solid angle subtended at the charge by the area element dA is dΩ = (r̂ · n̂) dA / r² (the projection of dA perpendicular to the radial direction, divided by r²). When the surface element faces the charge (r̂ · n̂ > 0) the solid angle is positive; when it faces away (r̂ · n̂ < 0), it is negative. Every line from q pierces a closed surface an odd number of times (once for a convex surface, possibly more for a non-convex one, but algebraically the sum is +1 for a charge inside).

在电荷处，面积元 dA 所张的立体角为 dΩ = (r̂ · n̂) dA / r²（dA 垂直于径向方向的投影除以 r²）。当曲面元朝向电荷时（r̂ · n̂ > 0），立体角为正；背向时（r̂ · n̂ < 0）为负。从 q 出发的每条直线穿过闭合曲面奇数次，代数求和结果对于内部电荷为 +1。

**Step 3 — Integration over the full solid angle.** Because a closed surface subtends the full 4π steradians of solid angle at any interior point:

**第 3 步 — 对全立体角积分。** 因为闭合曲面在任意内部点所张的全部立体角为 4π 球面度：

  ∮_S E · dA = q / (4πε₀) ∮_S dΩ = q / (4πε₀) · 4π = q / ε₀.

If the charge is outside S, every ray from q enters and exits S in pairs, so the net solid-angle integral is zero: ∮_S E · dA = 0 for q outside.

若电荷在 S 外，则从 q 出发的每条射线成对地穿入穿出 S，净立体角积分为零：q 在外时 ∮_S E · dA = 0。

**Step 4 — Superposition to the general case.** For a continuous charge distribution ρ(r′), the total field is E = ∫ E_dq over all charge elements. The flux integral is linear, so:

**第 4 步 — 叠加到一般情形。** 对于连续电荷分布 ρ(r′)，总场为 E = ∫ E_dq 对所有电荷元的积分。通量积分是线性的，故：

  ∮_S E · dA = (1/ε₀) ∫_{V} ρ(r′) dV′ = Q_enc / ε₀.

This is **Gauss's law in integral form**.

这就是**积分形式的高斯定律**。

**Step 5 — Differential form via the Divergence Theorem.** The divergence theorem states ∮_S E · dA = ∫_V (∇ · E) dV. Since the surface S and enclosed volume V are arbitrary:

**第 5 步 — 经散度定理得微分形式。** 散度定理表明 ∮_S E · dA = ∫_V (∇ · E) dV。由于曲面 S 和所围体积 V 是任意的：

  ∫_V (∇ · E) dV = (1/ε₀) ∫_V ρ dV,

and since this holds for every volume V, the integrands must be equal pointwise:

由于这对每个体积 V 都成立，被积函数在每点处必须相等：

  **∇ · E = ρ / ε₀.**   ∎

---

## B. Poisson's Equation ∇²φ = −ρ/ε₀ and Laplace's Equation · 泊松方程 ∇²φ = −ρ/ε₀ 及拉普拉斯方程

**Claim.** In electrostatics the curl-free condition and Gauss's law together imply ∇²φ = −ρ/ε₀, which reduces to ∇²φ = 0 in charge-free regions.

**命题。** 在静电学中，无旋条件与高斯定律共同意味着 ∇²φ = −ρ/ε₀，在无电荷区域化为 ∇²φ = 0。

**Step 1 — Establish ∇ × E = 0.** For a static point charge q at the origin, E = q r̂/(4πε₀ r²). Computing the curl in spherical coordinates, or noting that E = −∇(q/(4πε₀ r)), we have ∇ × E = ∇ × (−∇φ) = 0 identically, since the curl of a gradient is always zero. By superposition this holds for any static charge distribution.

**第 1 步 — 建立 ∇ × E = 0。** 对于位于原点的静电点电荷 q，E = q r̂/(4πε₀ r²)。在球坐标中计算旋度，或注意到 E = −∇(q/(4πε₀ r))，我们有 ∇ × E = ∇ × (−∇φ) = 0，因为梯度的旋度恒为零。由叠加原理，这对任意静电荷分布均成立。

**Step 2 — Introduce the scalar potential.** Because ∇ × E = 0, by the Helmholtz theorem (or directly from vector calculus: a curl-free field on a simply-connected domain is a gradient), there exists a scalar field φ(r) such that:

**第 2 步 — 引入标量电势。** 因为 ∇ × E = 0，由亥姆霍兹定理（或直接由向量分析：单连通域上的无旋场是梯度场），存在标量场 φ(r)，使得：

  E = −∇φ.

The sign is chosen by convention so that the field points from high to low potential (analogous to a force pointing down a slope).

符号按惯例选取，使得场从高电势指向低电势（类比于力沿斜面向下）。

**Step 3 — Substitute into Gauss's law.** Insert E = −∇φ into ∇ · E = ρ/ε₀:

**第 3 步 — 代入高斯定律。** 将 E = −∇φ 代入 ∇ · E = ρ/ε₀：

  ∇ · (−∇φ) = ρ / ε₀
  −∇²φ = ρ / ε₀
  **∇²φ = −ρ / ε₀.**   (Poisson's equation / 泊松方程)

**Step 4 — Laplace's equation in charge-free regions.** Where ρ = 0:

**第 4 步 — 无电荷区域的拉普拉斯方程。** 在 ρ = 0 处：

  **∇²φ = 0.**   (Laplace's equation / 拉普拉斯方程)

Solutions are called **harmonic functions**; they satisfy the mean-value property (the value at any interior point equals the average over any surrounding sphere), which immediately implies the **maximum principle**: φ can have no local maxima or minima in a charge-free region.

解被称为**调和函数**；它们满足平均值性质（任意内部点处的值等于任意外围球面的平均值），这立即意味着**最大值原理**：φ 在无电荷区域内不能有局部极大或极小值。∎

---

## C. Separation of Variables — Grounded Conducting Sphere in a Uniform External Field · 分离变量法——均匀外场中的接地导体球

**Claim.** A grounded conducting sphere of radius R placed in a uniform field E₀ ẑ has the exterior potential φ_out(r, θ) = −E₀ r cos θ + E₀ R³ cos θ / r², and the induced surface charge density is σ = 3ε₀ E₀ cos θ.

**命题。** 半径为 R 的接地导体球置于均匀场 E₀ ẑ 中，外部电势为 φ_out(r, θ) = −E₀ r cos θ + E₀ R³ cos θ / r²，感应面电荷密度为 σ = 3ε₀ E₀ cos θ。

**Step 1 — Set up Laplace's equation in spherical coordinates.** In the exterior region r > R, with no free charge, φ satisfies ∇²φ = 0. In spherical coordinates with azimuthal symmetry (no φ-dependence):

**第 1 步 — 在球坐标中建立拉普拉斯方程。** 在无自由电荷的外部区域 r > R，φ 满足 ∇²φ = 0。在具有方位角对称性（无 φ 依赖）的球坐标中：

  (1/r²) d/dr (r² dφ/dr) + (1/(r² sin θ)) d/dθ (sin θ dφ/dθ) = 0.

**Step 2 — Separate variables.** Write φ(r, θ) = R(r) Θ(θ). Substituting and dividing by R(r)Θ(θ)/r²:

**第 2 步 — 分离变量。** 令 φ(r, θ) = R(r) Θ(θ)。代入并除以 R(r)Θ(θ)/r²：

  (1/R) d/dr (r² dR/dr) = −(1/(Θ sin θ)) d/dθ (sin θ dΘ/dθ) = ℓ(ℓ+1),

where ℓ(ℓ+1) is the separation constant (chosen in this form to give polynomial solutions in cos θ). The two separated ODEs are:

其中 ℓ(ℓ+1) 为分离常数（选此形式使 cos θ 的多项式解存在）。两个分离的常微分方程为：

  Radial:   d/dr (r² dR/dr) − ℓ(ℓ+1) R = 0   →   R(r) = A_ℓ r^ℓ + B_ℓ r^{−(ℓ+1)},
  Angular:  (1/sin θ) d/dθ (sin θ dΘ/dθ) + ℓ(ℓ+1) Θ = 0   →   Θ = P_ℓ(cos θ),

where P_ℓ are the **Legendre polynomials**. For ℓ = 0: P₀ = 1; ℓ = 1: P₁ = cos θ; ℓ = 2: P₂ = (3cos²θ − 1)/2, etc.

其中 P_ℓ 为**勒让德多项式**。ℓ = 0：P₀ = 1；ℓ = 1：P₁ = cos θ；ℓ = 2：P₂ = (3cos²θ − 1)/2，等等。

**Step 3 — Apply boundary condition at r → ∞.** Far from the sphere the field must reduce to the uniform external field E₀ ẑ, whose potential is φ → −E₀ r cos θ as r → ∞. Therefore the only term that grows as r → ∞ must match −E₀ r cos θ, which is the ℓ = 1, r^1 term. All terms with A_ℓ for ℓ ≠ 1 must vanish, and A₁ = −E₀. The general exterior solution is:

**第 3 步 — 应用 r → ∞ 处的边界条件。** 远离球体，场必须还原为均匀外场 E₀ ẑ，其电势为 φ → −E₀ r cos θ（r → ∞）。因此，随 r → ∞ 增长的唯一项必须匹配 −E₀ r cos θ，即 ℓ = 1，r^1 项。所有 ℓ ≠ 1 的 A_ℓ 项必须为零，且 A₁ = −E₀。一般外部解为：

  φ_out = −E₀ r cos θ + Σ_ℓ B_ℓ r^{−(ℓ+1)} P_ℓ(cos θ).

**Step 4 — Apply the grounded-sphere boundary condition φ(R, θ) = 0.** Setting r = R:

**第 4 步 — 应用接地球面边界条件 φ(R, θ) = 0。** 令 r = R：

  −E₀ R cos θ + Σ_ℓ B_ℓ R^{−(ℓ+1)} P_ℓ(cos θ) = 0.

By the orthogonality of Legendre polynomials, each coefficient must separately vanish. The only non-zero driving term is the ℓ = 1 term (−E₀ R cos θ = −E₀ R P₁), so only B₁ is non-zero:

由勒让德多项式的正交性，每个系数必须分别为零。唯一非零的驱动项是 ℓ = 1 项（−E₀ R cos θ = −E₀ R P₁），所以只有 B₁ 非零：

  B₁ R^{−2} = E₀ R   →   B₁ = E₀ R³.

All other B_ℓ = 0. Therefore:

所有其他 B_ℓ = 0。因此：

  **φ_out(r, θ) = −E₀ r cos θ + E₀ R³ cos θ / r².**

**Step 5 — Physical interpretation.** The first term is the applied potential; the second is a dipole potential with effective dipole moment p = 4πε₀ R³ E₀ ẑ, arising from the induced surface charge. This is exactly the form of an electric dipole field (see Section D).

**第 5 步 — 物理诠释。** 第一项是外加电势；第二项是有效偶极矩 p = 4πε₀ R³ E₀ ẑ 的偶极子电势，由感应面电荷产生。这正是电偶极子场的形式（见 D 节）。

**Step 6 — Surface charge density.** The radial component of E just outside a conductor equals σ/ε₀. Computing E_r = −∂φ/∂r at r = R:

**第 6 步 — 面电荷密度。** 导体外侧紧邻处 E 的径向分量等于 σ/ε₀。在 r = R 处计算 E_r = −∂φ/∂r：

  E_r|_{r=R} = E₀ cos θ + 2 E₀ R³ cos θ / R³ = 3 E₀ cos θ.

Hence **σ = ε₀ E_r|_{r=R} = 3ε₀ E₀ cos θ.** ∎

故 **σ = ε₀ E_r|_{r=R} = 3ε₀ E₀ cos θ。** ∎

**Step 7 — Uniqueness theorem (why this is the unique solution).** The uniqueness theorem for Laplace's equation states: given boundary conditions on φ (Dirichlet) or ∂φ/∂n (Neumann) on a closed surface, the solution inside is unique. Proof sketch: suppose φ₁ and φ₂ are two solutions; let u = φ₁ − φ₂, which satisfies ∇²u = 0 with u = 0 on the boundary (Dirichlet). Then ∫_V |∇u|² dV = ∮_S u (∂u/∂n) dA = 0 (by Green's first identity, with u = 0 on S). Since |∇u|² ≥ 0, we must have ∇u = 0 everywhere, so u = constant = 0. Hence φ₁ = φ₂.

**第 7 步 — 唯一性定理（为何此解是唯一的）。** 拉普拉斯方程的唯一性定理指出：给定闭合曲面上 φ 的边界条件（狄利克雷）或 ∂φ/∂n（诺依曼），内部解是唯一的。证明概要：设 φ₁ 和 φ₂ 是两个解；令 u = φ₁ − φ₂，满足 ∇²u = 0，边界上 u = 0（狄利克雷）。则 ∫_V |∇u|² dV = ∮_S u (∂u/∂n) dA = 0（由格林第一恒等式，S 上 u = 0）。由于 |∇u|² ≥ 0，必有 ∇u = 0 处处成立，故 u = 常数 = 0。因此 φ₁ = φ₂。

---

## D. Multipole Expansion — Monopole, Dipole, and Quadrupole Terms · 多极展开——单极、偶极与四极项

**Claim.** At large distances from a bounded charge distribution ρ(r′), the potential can be expanded in inverse powers of r, with the leading terms being the monopole (1/r), dipole (1/r²), and quadrupole (1/r³).

**命题。** 距有界电荷分布 ρ(r′) 较远处，电势可展开为 r 的负幂次，主要项依次为单极（1/r）、偶极（1/r²）和四极（1/r³）。

**Step 1 — Exact expression.** The potential at field point r due to a charge distribution ρ(r′) confined near the origin is:

**第 1 步 — 精确表达式。** 场点 r 处由集中在原点附近的电荷分布 ρ(r′) 产生的电势为：

  φ(r) = (1/4πε₀) ∫ ρ(r′) / |r − r′| dV′.

**Step 2 — Expand 1/|r − r′| for r′ ≪ r.** Using the generating function for Legendre polynomials:

**第 2 步 — 展开 r′ ≪ r 时的 1/|r − r′|。** 利用勒让德多项式的母函数：

  1/|r − r′| = (1/r) Σ_{ℓ=0}^{∞} (r′/r)^ℓ P_ℓ(cos α),

where α is the angle between r and r′. This is exact when r > r′ (all charges inside a sphere of radius r).

其中 α 是 r 与 r′ 之间的夹角。当 r > r′ 时（所有电荷在半径为 r 的球内），此式精确成立。

**Step 3 — Identify each term.** Substituting:

**第 3 步 — 识别每一项。** 代入得：

  φ(r) = (1/4πε₀) Σ_{ℓ=0}^{∞} (1/r^{ℓ+1}) ∫ r′^ℓ P_ℓ(cos α) ρ(r′) dV′.

  ℓ = 0 (monopole):   φ_mono = (1/4πε₀) (Q/r),   Q = ∫ ρ dV′.
  ℓ = 1 (dipole):     φ_dip  = (1/4πε₀) (p · r̂/r²),   p = ∫ r′ ρ(r′) dV′.
  ℓ = 2 (quadrupole): φ_quad = (1/4πε₀) (1/r³) Σ_{ij} Q_ij r̂_i r̂_j / 2,

where Q_ij = ∫ (3r′_i r′_j − r′² δ_ij) ρ(r′) dV′ is the quadrupole tensor.

其中 Q_ij = ∫ (3r′_i r′_j − r′² δ_ij) ρ(r′) dV′ 是四极矩张量。

**Step 4 — Physical content.** If Q ≠ 0, the monopole dominates at large r (like a point charge). If Q = 0 but p ≠ 0 (e.g., equal and opposite charges separated by a distance), the dipole term dominates. Neutral atoms have Q = 0 and often p = 0 (nonpolar), so their leading interaction at large distances is through the quadrupole or induced-dipole terms. The electric dipole field E_dip = (1/4πε₀r³)(3(p·r̂)r̂ − p) is the far-field leading term for any neutral current-free source with a nonzero dipole moment. ∎

**第 4 步 — 物理内涵。** 若 Q ≠ 0，单极项在大 r 处主导（如点电荷）。若 Q = 0 但 p ≠ 0（例如等量异号电荷分开一段距离），偶极项主导。中性原子有 Q = 0，且通常 p = 0（非极性），其在大距离处的主导相互作用通过四极矩或感应偶极矩项进行。电偶极子场 E_dip = (1/4πε₀r³)(3(p·r̂)r̂ − p) 是任何偶极矩非零的中性无流源的远场主导项。∎

---

*All four Maxwell equations, boundary-value methods, and the multipole hierarchy developed here feed directly into Modules 1.9–1.11, the hydrogen atom (Module 3.4), and multipole radiation theory.*

*此处发展的所有四个麦克斯韦方程、边值方法和多极层次，直接支撑模块 1.9–1.11、氢原子（模块 3.4）和多极辐射理论。*

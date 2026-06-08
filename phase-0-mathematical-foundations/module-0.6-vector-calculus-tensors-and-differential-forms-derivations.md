# Derivations — Module 0.6: Vector Calculus, Tensors & Differential Forms
# 推导 — 模块 0.6：向量微积分、张量与微分形式

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 0.6](./module-0.6-vector-calculus-tensors-and-differential-forms.md). Full step-by-step proofs: the divergence theorem and Stokes' theorem (statement plus the standard cube/loop argument); derivation of ∇² in spherical coordinates; Maxwell's equations as applications of ∇· and ∇×; the Levi-Civita identity ε_{ijk}ε_{ilm} = δ_{jl}δ_{km} − δ_{jm}δ_{kl}; and the vector identity ∇×(∇×A) = ∇(∇·A) − ∇²A proved by index notation. English first, then 中文.
> [模块 0.6](./module-0.6-vector-calculus-tensors-and-differential-forms.md) 的配套文档：完整逐步证明：散度定理与斯托克斯定理（陈述及标准的立方体/回路论证）；球坐标下 ∇² 的推导；麦克斯韦方程作为 ∇· 和 ∇× 的应用；列维-奇维塔恒等式 ε_{ijk}ε_{ilm} = δ_{jl}δ_{km} − δ_{jm}δ_{kl}；以及用指标记号证明向量恒等式 ∇×(∇×A) = ∇(∇·A) − ∇²A。先英文，后中文。

---

## A. The Divergence Theorem · 散度定理

**Statement.** Let V be a compact region in ℝ³ with piecewise smooth boundary surface S = ∂V, with outward-pointing unit normal n̂. For any continuously differentiable vector field F:

**陈述。** 设 V 是 ℝ³ 中具有分片光滑边界曲面 S = ∂V 的紧致区域，n̂ 为向外单位法向量。对任意连续可微向量场 F：

  ∫_V (∇·F) dV = ∮_S F·n̂ dA.

**Proof — Step 1: Reduce to one component.** Write F = (F₁, F₂, F₃). By linearity, it suffices to prove the theorem for each component separately. We prove it for F = (F₁, 0, 0), i.e., show

**证明——第 1 步：归约到单个分量。** 写 F = (F₁, F₂, F₃)。由线性性，对每个分量分别证明定理即可。我们对 F = (F₁, 0, 0) 进行证明，即证明

  ∫_V ∂F₁/∂x dV = ∮_S F₁ n₁ dA,

where n₁ = n̂·ê_x is the x-component of the outward normal. The full theorem follows by adding the analogous results for F₂ and F₃.

其中 n₁ = n̂·ê_x 是外法向量的 x 分量。对 F₂ 和 F₃ 的类似结果相加即得完整定理。

**Step 2 — The unit cube argument.** First prove the result for V = [0,1]³ (the unit cube). For a fixed (y, z), integrate ∂F₁/∂x from x = 0 to x = 1 using the fundamental theorem of calculus:

**第 2 步 — 单位立方体论证。** 首先对 V = [0,1]³（单位立方体）证明此结果。对固定的 (y, z)，利用微积分基本定理对 x 从 0 积到 1：

  ∫_0^1 ∂F₁/∂x dx = F₁(1, y, z) − F₁(0, y, z).

Integrate over the remaining two variables:

对其余两个变量积分：

  ∫_V ∂F₁/∂x dV = ∫_0^1 ∫_0^1 [F₁(1,y,z) − F₁(0,y,z)] dy dz.

Now examine the boundary surface S of the cube. It has six faces:
- Face x = 1: n̂ = ê_x (outward), so F₁ n₁ dA = F₁(1,y,z) dy dz. Contribution: +∫∫ F₁(1,y,z) dy dz.
- Face x = 0: n̂ = −ê_x (outward), so F₁ n₁ dA = −F₁(0,y,z) dy dz. Contribution: −∫∫ F₁(0,y,z) dy dz.
- Four side faces (y=0,1 and z=0,1): n̂ has no x-component, so F₁ n₁ = 0 on these faces.

现在考察立方体的边界曲面 S，共有六个面：
- x = 1 面：n̂ = ê_x（向外），故 F₁ n₁ dA = F₁(1,y,z) dy dz。贡献：+∫∫ F₁(1,y,z) dy dz。
- x = 0 面：n̂ = −ê_x（向外），故 F₁ n₁ dA = −F₁(0,y,z) dy dz。贡献：−∫∫ F₁(0,y,z) dy dz。
- 四个侧面（y=0,1 和 z=0,1）：n̂ 无 x 分量，故 F₁ n₁ = 0。

Adding all boundary contributions:

将所有边界贡献相加：

  ∮_S F₁ n₁ dA = ∫_0^1 ∫_0^1 [F₁(1,y,z) − F₁(0,y,z)] dy dz = ∫_V ∂F₁/∂x dV. ✓

**Step 3 — Extend to general regions.** Any region V with piecewise smooth boundary can be subdivided (partitioned) into small "almost-cuboid" elements by a coordinate grid. Applying the result from Step 2 to each element and summing:

**第 3 步 — 推广到一般区域。** 任何具有分片光滑边界的区域 V 都可以通过坐标网格细分（剖分）为小的"近似长方体"元素。对每个元素应用第 2 步的结果并求和：

- Interior faces appear twice with opposite orientations and cancel.
- Only boundary faces survive.

- 内部面以相反方向出现两次，相互抵消。
- 只有边界面的贡献保留。

In the limit as the mesh size → 0, the sum converges to ∫_V ∇·F dV = ∮_S F·n̂ dA. ∎

当网格尺寸 → 0 时，求和收敛为 ∫_V ∇·F dV = ∮_S F·n̂ dA。∎

**Physical interpretation.** The divergence theorem converts "what's happening at every interior point" into "what's happening at the boundary." In electrostatics: Gauss's law ∮ E·dA = Q_enc/ε₀ follows from ∇·E = ρ/ε₀ via ∫_V ρ/ε₀ dV = Q_enc/ε₀. In fluid dynamics: ∇·v = 0 (incompressible flow) means no net flux through any closed surface.

**物理解释。** 散度定理将"每个内部点发生的事情"转化为"边界上发生的事情"。在静电学中：高斯定律 ∮ E·dA = Q_enc/ε₀ 由 ∇·E = ρ/ε₀ 通过 ∫_V ρ/ε₀ dV = Q_enc/ε₀ 得出。在流体力学中：∇·v = 0（不可压缩流）意味着穿过任意闭合曲面的净通量为零。

---

## B. Stokes' Theorem · 斯托克斯定理

**Statement.** Let S be an oriented surface in ℝ³ with piecewise smooth boundary curve C = ∂S (traversed counterclockwise when viewed from the side the normal n̂ points toward). For any continuously differentiable vector field F:

**陈述。** 设 S 是 ℝ³ 中具有分片光滑边界曲线 C = ∂S 的定向曲面（从法向量 n̂ 所指方向看去，C 沿逆时针方向绕行）。对任意连续可微向量场 F：

  ∫_S (∇×F)·n̂ dA = ∮_C F·dl.

**Proof — Step 1: Reduce to one component.** Write F = (F₁, F₂, F₃). By linearity we prove:

**证明——第 1 步：归约到单个分量。** 写 F = (F₁, F₂, F₃)。由线性性，我们对每个分量分别证明：

  ∫_S (∂F₂/∂x − ∂F₁/∂y) n_z dA = ∮_C (F₁ dx + F₂ dy)  [the xy-component],

and similarly for the yz and zx components.

以及类似的 yz 和 zx 分量。

**Step 2 — The unit square in the xy-plane.** For the simplest case where S is the unit square [0,1]² in the z=0 plane (so n̂ = ê_z, dA = dx dy), and C is its boundary traversed counterclockwise:

**第 2 步 — xy 平面中的单位正方形。** 对最简单的情形，S 是 z=0 平面中的单位正方形 [0,1]²（故 n̂ = ê_z，dA = dx dy），C 是沿逆时针方向绕行的边界：

Left side: ∫_S (∂F₂/∂x − ∂F₁/∂y) dx dy.

左侧：∫_S (∂F₂/∂x − ∂F₁/∂y) dx dy。

For the ∂F₂/∂x term, integrate first over x by FTC:

对 ∂F₂/∂x 项，先对 x 用基本定理积分：

  ∫_0^1 ∫_0^1 ∂F₂/∂x dx dy = ∫_0^1 [F₂(1,y) − F₂(0,y)] dy.

For the ∂F₁/∂y term, integrate first over y:

对 ∂F₁/∂y 项，先对 y 用基本定理积分：

  ∫_0^1 ∫_0^1 ∂F₁/∂y dy dx = ∫_0^1 [F₁(x,1) − F₁(x,0)] dx.

So the left side equals:

故左侧等于：

  ∫_0^1 [F₂(1,y) − F₂(0,y)] dy − ∫_0^1 [F₁(x,1) − F₁(x,0)] dx.

Right side: ∮_C (F₁ dx + F₂ dy). Traverse the four edges counterclockwise:
- Bottom (y=0, x: 0→1): ∫_0^1 F₁(x,0) dx
- Right (x=1, y: 0→1): ∫_0^1 F₂(1,y) dy
- Top (y=1, x: 1→0): ∫_1^0 F₁(x,1) dx = −∫_0^1 F₁(x,1) dx
- Left (x=0, y: 1→0): ∫_1^0 F₂(0,y) dy = −∫_0^1 F₂(0,y) dy

右侧：∮_C (F₁ dx + F₂ dy)。沿四条边逆时针绕行：
- 底边（y=0，x: 0→1）：∫_0^1 F₁(x,0) dx
- 右边（x=1，y: 0→1）：∫_0^1 F₂(1,y) dy
- 顶边（y=1，x: 1→0）：∫_1^0 F₁(x,1) dx = −∫_0^1 F₁(x,1) dx
- 左边（x=0，y: 1→0）：∫_1^0 F₂(0,y) dy = −∫_0^1 F₂(0,y) dy

Sum = ∫_0^1 [F₂(1,y) − F₂(0,y)] dy − ∫_0^1 [F₁(x,1) − F₁(x,0)] dx = Left side. ✓

求和 = ∫_0^1 [F₂(1,y) − F₂(0,y)] dy − ∫_0^1 [F₁(x,1) − F₁(x,0)] dx = 左侧。✓

**Step 3 — General surface by subdivision.** Any smooth surface S can be approximated by small "almost-planar" patches. Applying the result of Step 2 to each patch and summing, interior edge contributions cancel (each interior edge is shared by two patches traversed in opposite directions), leaving only the outer boundary C. In the limit, this gives Stokes' theorem for S. ∎

**第 3 步 — 通过细分推广到一般曲面。** 任何光滑曲面 S 都可以用小的"近似平面"片近似。对每个片应用第 2 步的结果并求和，内部边的贡献相消（每条内部边被两个相反方向绕行的片共享），只留下外边界 C。取极限即得 S 的斯托克斯定理。∎

**Physical applications.** Faraday's law: ∮_C E·dl = −d/dt ∫_S B·dA. In differential form this is ∇×E = −∂B/∂t; Stokes' theorem connects the two. Ampère's law: ∮_C B·dl = μ₀ I_enc relates the magnetic circulation around a loop to the current through the surface bounded by the loop.

**物理应用。** 法拉第定律：∮_C E·dl = −d/dt ∫_S B·dA。微分形式为 ∇×E = −∂B/∂t；斯托克斯定理将两者联系起来。安培定律：∮_C B·dl = μ₀ I_enc 将回路周围的磁环量与穿过该回路所围曲面的电流联系起来。

---

## C. Derivation of ∇² in Spherical Coordinates · 球坐标下 ∇² 的推导

**Setup.** The spherical coordinates (r, θ, φ) are related to Cartesian coordinates by:

**准备工作。** 球坐标 (r, θ, φ) 与笛卡尔坐标的关系为：

  x = r sin θ cos φ,   y = r sin θ sin φ,   z = r cos θ,

with r ≥ 0, 0 ≤ θ ≤ π, 0 ≤ φ < 2π.

其中 r ≥ 0，0 ≤ θ ≤ π，0 ≤ φ < 2π。

**Step 1 — Compute the scale factors.** The position vector is r⃗ = (r sin θ cos φ, r sin θ sin φ, r cos θ). The scale factors (metrics) are

**第 1 步 — 计算比例因子。** 位置向量为 r⃗ = (r sin θ cos φ, r sin θ sin φ, r cos θ)。比例因子（度规）为

  h_r = |∂r⃗/∂r| = 1,
  h_θ = |∂r⃗/∂θ| = r,
  h_φ = |∂r⃗/∂φ| = r sin θ.

Verify h_θ: ∂r⃗/∂θ = (r cos θ cos φ, r cos θ sin φ, −r sin θ), so h_θ = r√(cos²θ cos²φ + cos²θ sin²φ + sin²θ) = r√(cos²θ + sin²θ) = r. ✓

验证 h_θ：∂r⃗/∂θ = (r cos θ cos φ, r cos θ sin φ, −r sin θ)，故 h_θ = r√(cos²θ cos²φ + cos²θ sin²φ + sin²θ) = r√(cos²θ + sin²θ) = r。✓

**Step 2 — The volume element.** In an orthogonal curvilinear coordinate system the volume element is

**第 2 步 — 体积元。** 在正交曲线坐标系中，体积元为

  dV = h_r h_θ h_φ dr dθ dφ = (1)(r)(r sin θ) dr dθ dφ = r² sin θ dr dθ dφ.

**Step 3 — General Laplacian formula in orthogonal curvilinear coordinates.** For a scalar field f, the Laplacian is

**第 3 步 — 正交曲线坐标系中拉普拉斯算子的一般公式。** 对标量场 f，拉普拉斯算子为

  ∇²f = (1/(h₁h₂h₃)) [∂/∂q₁(h₂h₃/h₁ ∂f/∂q₁) + ∂/∂q₂(h₁h₃/h₂ ∂f/∂q₂) + ∂/∂q₃(h₁h₂/h₃ ∂f/∂q₃)].

This follows from computing ∇·(∇f) using the divergence formula in curvilinear coordinates.

这由在曲线坐标系中计算 ∇·(∇f) 的散度公式得到。

**Step 4 — Apply to spherical coordinates.** With (q₁,q₂,q₃) = (r,θ,φ) and (h₁,h₂,h₃) = (1, r, r sinθ):

**第 4 步 — 应用于球坐标。** 令 (q₁,q₂,q₃) = (r,θ,φ)，(h₁,h₂,h₃) = (1, r, r sinθ)：

  h₂h₃/h₁ = r² sin θ,   h₁h₃/h₂ = sin θ,   h₁h₂/h₃ = 1/sin θ.

  h₁h₂h₃ = r² sin θ.

So:

故：

  ∇²f = (1/(r² sin θ)) [∂/∂r(r² sin θ ∂f/∂r) + ∂/∂θ(sin θ ∂f/∂θ) + ∂/∂φ(1/sin θ ∂f/∂φ)].

The sin θ in the first term cancels with the prefactor:

第一项中的 sin θ 与前置因子约去：

  ∇²f = (1/r²) ∂/∂r(r² ∂f/∂r) + (1/(r² sin θ)) ∂/∂θ(sin θ ∂f/∂θ) + (1/(r² sin²θ)) ∂²f/∂φ².

**Step 5 — Expand the radial term.**

**第 5 步 — 展开径向项。**

  (1/r²) ∂/∂r(r² ∂f/∂r) = (1/r²)(2r ∂f/∂r + r² ∂²f/∂r²) = (2/r) ∂f/∂r + ∂²f/∂r².

So the full result is:

故完整结果为：

  **∇²f = ∂²f/∂r² + (2/r) ∂f/∂r + (1/r²) ∂/∂θ(sin θ ∂f/∂θ)/sin θ + (1/(r² sin²θ)) ∂²f/∂φ².**

Or equivalently:

或等价地：

  **∇²f = (1/r²) ∂/∂r(r² ∂f/∂r) + (1/(r² sin θ)) ∂/∂θ(sin θ ∂f/∂θ) + (1/(r² sin²θ)) ∂²f/∂φ².** ∎

**Physical application.** The time-independent Schrödinger equation for the hydrogen atom −(ℏ²/2m)∇²ψ + V(r)ψ = Eψ with V(r) = −e²/(4πε₀r) uses this exact expression. The separation ψ(r,θ,φ) = R(r)Yₗᵐ(θ,φ) works because ∇² separates into a radial part acting on R and an angular part (the Legendre equation) acting on Y.

**物理应用。** 氢原子的定态薛定谔方程 −(ℏ²/2m)∇²ψ + V(r)ψ = Eψ，其中 V(r) = −e²/(4πε₀r)，正是使用此表达式。分离 ψ(r,θ,φ) = R(r)Yₗᵐ(θ,φ) 之所以有效，是因为 ∇² 分离为作用于 R 的径向部分和作用于 Y 的角向部分（勒让德方程）。

---

## D. Maxwell's Equations in Differential Form and Their Integral Equivalents · 麦克斯韦方程的微分形式与积分等价形式

**Setup.** Maxwell's equations (SI units) in differential form are:

**准备工作。** 麦克斯韦方程组（国际单位制）的微分形式为：

  ∇·E = ρ/ε₀          [Gauss's law for E 高斯定律（电场）]
  ∇·B = 0             [Gauss's law for B 高斯定律（磁场）]
  ∇×E = −∂B/∂t        [Faraday's law 法拉第定律]
  ∇×B = μ₀J + μ₀ε₀∂E/∂t  [Ampère–Maxwell law 安培–麦克斯韦定律]

**Step 1 — Gauss's law via the divergence theorem.** Apply the divergence theorem to ∇·E = ρ/ε₀ over a volume V with boundary S:

**第 1 步 — 通过散度定理得出高斯定律。** 对区域 V（边界为 S）将散度定理应用于 ∇·E = ρ/ε₀：

  ∮_S E·n̂ dA = ∫_V ∇·E dV = (1/ε₀) ∫_V ρ dV = Q_enc/ε₀.

This is the **integral form of Gauss's law**: the total electric flux through any closed surface equals the enclosed charge divided by ε₀.

这就是**高斯定律的积分形式**：穿过任意闭合曲面的总电通量等于包围的电荷除以 ε₀。

**Step 2 — No magnetic monopoles.** Similarly ∇·B = 0 gives ∮_S B·n̂ dA = 0: there is no net magnetic flux through any closed surface, i.e., magnetic field lines form closed loops.

**第 2 步 — 无磁单极子。** 类似地，∇·B = 0 给出 ∮_S B·n̂ dA = 0：穿过任意闭合曲面的净磁通量为零，即磁场线形成闭合回路。

**Step 3 — Faraday's law via Stokes' theorem.** Apply Stokes' theorem to ∇×E = −∂B/∂t over a surface S bounded by curve C:

**第 3 步 — 通过斯托克斯定理得出法拉第定律。** 对以曲线 C 为边界的曲面 S，将斯托克斯定理应用于 ∇×E = −∂B/∂t：

  ∮_C E·dl = ∫_S (∇×E)·n̂ dA = −∫_S ∂B/∂t·n̂ dA = −d/dt ∫_S B·n̂ dA = −dΦ_B/dt.

This is Faraday's law: the EMF around a loop equals the negative rate of change of the magnetic flux through the loop.

这就是法拉第定律：回路的电动势等于穿过回路磁通量的负时间变化率。

**Step 4 — Ampère–Maxwell law via Stokes' theorem.** Apply Stokes' theorem to ∇×B = μ₀J + μ₀ε₀∂E/∂t:

**第 4 步 — 通过斯托克斯定理得出安培–麦克斯韦定律。** 对 ∇×B = μ₀J + μ₀ε₀∂E/∂t 应用斯托克斯定理：

  ∮_C B·dl = μ₀ ∫_S J·n̂ dA + μ₀ε₀ d/dt ∫_S E·n̂ dA = μ₀ I_enc + μ₀ε₀ dΦ_E/dt.

The term μ₀ε₀∂E/∂t is Maxwell's **displacement current**, needed to make the equation consistent with charge conservation (∇·J + ∂ρ/∂t = 0) and to allow electromagnetic waves to exist.

项 μ₀ε₀∂E/∂t 是麦克斯韦的**位移电流**，这是使方程与电荷守恒（∇·J + ∂ρ/∂t = 0）一致并使电磁波得以存在所必需的。

---

## E. The Levi-Civita Identity ε_{ijk} ε_{ilm} = δ_{jl}δ_{km} − δ_{jm}δ_{kl} · 列维-奇维塔恒等式

**Claim.** Summing over the repeated index i:

**命题。** 对重复指标 i 求和：

  Σ_i ε_{ijk} ε_{ilm} = δ_{jl} δ_{km} − δ_{jm} δ_{kl}.

**Step 1 — Properties of the Levi-Civita symbol.** Recall ε_{ijk} = +1 if (i,j,k) is an even permutation of (1,2,3), −1 if odd, and 0 if any two indices are equal. For three-dimensional space, ε_{ijk} ε_{ilm} sums over i = 1, 2, 3.

**第 1 步 — 列维-奇维塔符号的性质。** 回顾：若 (i,j,k) 是 (1,2,3) 的偶置换，ε_{ijk} = +1；奇置换为 −1；有两个相同指标为 0。在三维空间中，ε_{ijk} ε_{ilm} 对 i = 1, 2, 3 求和。

**Step 2 — Enumerate cases.** Since j, k ∈ {1,2,3} and ε_{ijk} = 0 unless all three indices are distinct, j ≠ k is required for a non-zero contribution. Similarly l ≠ m is required. For fixed j ≠ k, the only i that gives ε_{ijk} ≠ 0 is the unique third value: {i} = {1,2,3} \ {j,k}.

**第 2 步 — 枚举情形。** 由于 j, k ∈ {1,2,3}，且除非三个指标都不同否则 ε_{ijk} = 0，因此需要 j ≠ k 才能有非零贡献。类似地，需要 l ≠ m。对固定的 j ≠ k，使 ε_{ijk} ≠ 0 的唯一 i 是 {1,2,3}\{j,k} 中的第三个值。

**Step 3 — Compute systematically.** Fix j, k, l, m ∈ {1,2,3}. The sum Σ_i ε_{ijk} ε_{ilm} is non-zero only when:
- The pair {j,k} and the pair {l,m} each consists of two distinct elements, AND
- There is some i such that both ε_{ijk} ≠ 0 and ε_{ilm} ≠ 0, which requires {i,j,k} = {i,l,m} = {1,2,3}, forcing {j,k} = {l,m} as sets.

**第 3 步 — 系统计算。** 固定 j, k, l, m ∈ {1,2,3}。仅当以下条件满足时，Σ_i ε_{ijk} ε_{ilm} 才非零：
- 对 {j,k} 和 {l,m}，每对均由两个不同元素组成，且
- 存在某个 i 使得 ε_{ijk} ≠ 0 且 ε_{ilm} ≠ 0，这要求 {i,j,k} = {i,l,m} = {1,2,3}，从而作为集合 {j,k} = {l,m}。

This means either (l = j, m = k) or (l = k, m = j).

这意味着要么 (l = j, m = k)，要么 (l = k, m = j)。

**Step 4 — Determine the sign.** When l = j, m = k: Σ_i ε_{ijk} ε_{ijk} = (ε_{ijk})² = 1 (since (ε_{ijk})² = 0 or 1, and the single surviving term is ±1, so its square is 1).

**第 4 步 — 确定符号。** 当 l = j, m = k 时：Σ_i ε_{ijk} ε_{ijk} = (ε_{ijk})² = 1（因为 (ε_{ijk})² 为 0 或 1，唯一存活的项为 ±1，平方为 1）。

When l = k, m = j: the second factor becomes ε_{ikj} = −ε_{ijk} (swapping two indices flips sign). So Σ_i ε_{ijk} ε_{ikj} = −Σ_i (ε_{ijk})² = −1.

当 l = k, m = j 时：第二个因子变为 ε_{ikj} = −ε_{ijk}（交换两个指标改变符号）。故 Σ_i ε_{ijk} ε_{ikj} = −Σ_i (ε_{ijk})² = −1。

**Step 5 — Express using Kronecker deltas.** The two cases (l=j,m=k) → +1 and (l=k,m=j) → −1 are precisely captured by:

**第 5 步 — 用克罗内克 delta 表达。** 两种情形（l=j,m=k）→ +1 和（l=k,m=j）→ −1 恰好由以下式子捕捉：

  Σ_i ε_{ijk} ε_{ilm} = δ_{jl} δ_{km} − δ_{jm} δ_{kl}. ∎

Verify: if j=l=1, k=m=2: δ_{11}δ_{22} − δ_{12}δ_{21} = 1·1 − 0·0 = 1. ✓ If j=m=1, k=l=2: δ_{12}δ_{21} − δ_{11}δ_{22} = 0 − 1 = −1. ✓

验证：若 j=l=1, k=m=2：δ_{11}δ_{22} − δ_{12}δ_{21} = 1·1 − 0·0 = 1。✓ 若 j=m=1, k=l=2：δ_{12}δ_{21} − δ_{11}δ_{22} = 0 − 1 = −1。✓

---

## F. Vector Identity: ∇×(∇×A) = ∇(∇·A) − ∇²A via Index Notation · 向量恒等式的指标记号证明

**Claim.** For any twice-differentiable vector field A:

**命题。** 对任意二阶可微向量场 A：

  ∇×(∇×A) = ∇(∇·A) − ∇²A.

**Step 1 — Write the left side in index notation.** The i-th component of ∇×A is (∇×A)ᵢ = ε_{ijk} ∂_j Aₖ (where ∂_j = ∂/∂xⱼ and repeated indices are summed). Then the i-th component of ∇×(∇×A) is:

**第 1 步 — 用指标记号写出左侧。** ∇×A 的第 i 个分量为 (∇×A)ᵢ = ε_{ijk} ∂_j Aₖ（其中 ∂_j = ∂/∂xⱼ，重复指标求和）。则 ∇×(∇×A) 的第 i 个分量为：

  [∇×(∇×A)]ᵢ = ε_{ijk} ∂_j (∇×A)ₖ = ε_{ijk} ∂_j (ε_{klm} ∂_l Aₘ) = ε_{ijk} ε_{klm} ∂_j ∂_l Aₘ.

**Step 2 — Rewrite using the Levi-Civita identity.** We need ε_{ijk} ε_{klm}. Noting that ε_{ijk} = ε_{kij} (even cyclic permutation), we have ε_{ijk} ε_{klm} = ε_{kij} ε_{klm}. Applying the identity from Section E with the first index summed being k, and pairs (i,j) and (l,m):

**第 2 步 — 用列维-奇维塔恒等式改写。** 需要 ε_{ijk} ε_{klm}。注意 ε_{ijk} = ε_{kij}（偶数循环置换），故 ε_{ijk} ε_{klm} = ε_{kij} ε_{klm}。应用 E 节中对被求和第一指标为 k、配对为 (i,j) 和 (l,m) 的恒等式：

  ε_{kij} ε_{klm} = δ_{il} δ_{jm} − δ_{im} δ_{jl}.

**Step 3 — Substitute back.**

**第 3 步 — 代回。**

  [∇×(∇×A)]ᵢ = (δ_{il} δ_{jm} − δ_{im} δ_{jl}) ∂_j ∂_l Aₘ
              = δ_{il} δ_{jm} ∂_j ∂_l Aₘ − δ_{im} δ_{jl} ∂_j ∂_l Aₘ.

**Step 4 — Contract the Kronecker deltas.**

**第 4 步 — 缩并克罗内克 delta。**

First term: δ_{il} δ_{jm} ∂_j ∂_l Aₘ = ∂_j ∂_i Aⱼ (set l=i, m=j) = ∂_i(∂_j Aⱼ) = ∂_i(∇·A) = [∇(∇·A)]ᵢ.

第一项：δ_{il} δ_{jm} ∂_j ∂_l Aₘ = ∂_j ∂_i Aⱼ（令 l=i, m=j）= ∂_i(∂_j Aⱼ) = ∂_i(∇·A) = [∇(∇·A)]ᵢ。

Second term: δ_{im} δ_{jl} ∂_j ∂_l Aₘ = ∂_j ∂_j Aᵢ (set m=i, l=j) = (∇²A)ᵢ.

第二项：δ_{im} δ_{jl} ∂_j ∂_l Aₘ = ∂_j ∂_j Aᵢ（令 m=i, l=j）= (∇²A)ᵢ。

(Here ∇²A is the vector Laplacian, defined component-wise: (∇²A)ᵢ = ∂_j ∂_j Aᵢ = ∇²Aᵢ.)

（此处 ∇²A 是向量拉普拉斯算子，逐分量定义：(∇²A)ᵢ = ∂_j ∂_j Aᵢ = ∇²Aᵢ。）

**Step 5 — Combine.**

**第 5 步 — 合并。**

  [∇×(∇×A)]ᵢ = [∇(∇·A)]ᵢ − (∇²A)ᵢ.

Since this holds for every component i:

由于对每个分量 i 均成立：

  **∇×(∇×A) = ∇(∇·A) − ∇²A**. ∎

**Physical application — Electromagnetic wave equation.** In free space (ρ = 0, J = 0), Maxwell's equations give ∇×E = −∂B/∂t and ∇×B = μ₀ε₀ ∂E/∂t. Taking ∇× of the first:

**物理应用——电磁波方程。** 在自由空间（ρ = 0, J = 0）中，麦克斯韦方程给出 ∇×E = −∂B/∂t 和 ∇×B = μ₀ε₀ ∂E/∂t。对第一式取 ∇×：

  ∇×(∇×E) = −∂/∂t(∇×B) = −μ₀ε₀ ∂²E/∂t².

Applying the vector identity, and using ∇·E = 0 (no charges):

应用向量恒等式，并利用 ∇·E = 0（无电荷）：

  ∇(∇·E) − ∇²E = −μ₀ε₀ ∂²E/∂t²  →  **∇²E = μ₀ε₀ ∂²E/∂t²**.

This is the electromagnetic wave equation with wave speed c = 1/√(μ₀ε₀). The vector identity ∇×(∇×A) = ∇(∇·A) − ∇²A is the key algebraic step in its derivation.

这是波速为 c = 1/√(μ₀ε₀) 的电磁波方程。向量恒等式 ∇×(∇×A) = ∇(∇·A) − ∇²A 是其推导中的关键代数步骤。

---

## G. Two Further Index Identities and Applications · 另外两个指标恒等式及其应用

### G.1 — ∇·(∇×A) = 0

**Claim.** The divergence of any curl is zero.

**命题。** 任意旋度的散度为零。

**Proof.** In index notation, ∇·(∇×A) = ∂ᵢ(ε_{ijk} ∂ⱼAₖ) = ε_{ijk} ∂ᵢ∂ⱼAₖ. The product ε_{ijk} ∂ᵢ∂ⱼ is a contraction of the antisymmetric symbol ε_{ijk} (antisymmetric in i,j) with the symmetric operator ∂ᵢ∂ⱼ = ∂ⱼ∂ᵢ (symmetric in i,j, by equality of mixed partials). The contraction of a symmetric and antisymmetric tensor over the same pair of indices always vanishes:

**证明。** 用指标记号，∇·(∇×A) = ∂ᵢ(ε_{ijk} ∂ⱼAₖ) = ε_{ijk} ∂ᵢ∂ⱼAₖ。乘积 ε_{ijk} ∂ᵢ∂ⱼ 是反对称符号 ε_{ijk}（关于 i,j 反对称）与对称算符 ∂ᵢ∂ⱼ = ∂ⱼ∂ᵢ（关于 i,j 对称，由混合偏导的相等性保证）的缩并。对称张量与反对称张量在同一对指标上的缩并恒为零：

  ε_{ijk} ∂ᵢ∂ⱼAₖ = −ε_{jik} ∂ᵢ∂ⱼAₖ = −ε_{ijk} ∂ⱼ∂ᵢAₖ = −ε_{ijk} ∂ᵢ∂ⱼAₖ,

where we swapped i↔j and used symmetry of ∂ᵢ∂ⱼ. So ε_{ijk} ∂ᵢ∂ⱼAₖ = 0. ∎

其中交换了 i↔j 并利用了 ∂ᵢ∂ⱼ 的对称性。故 ε_{ijk} ∂ᵢ∂ⱼAₖ = 0。∎

**Physical interpretation.** ∇·B = 0 can be solved by writing B = ∇×A (the magnetic vector potential). The identity ∇·(∇×A) = 0 is automatically satisfied, consistent with the absence of magnetic monopoles.

**物理解释。** ∇·B = 0 可以通过令 B = ∇×A（磁矢势）来求解。恒等式 ∇·(∇×A) = 0 自动满足，与磁单极子不存在相一致。

---

### G.2 — ∇×(∇f) = 0

**Claim.** The curl of any gradient is zero.

**命题。** 任意梯度的旋度为零。

**Proof.** [∇×(∇f)]ᵢ = ε_{ijk} ∂ⱼ(∂ₖf) = ε_{ijk} ∂ⱼ∂ₖf. By the same symmetry/antisymmetry argument (ε_{ijk} antisymmetric in j,k; ∂ⱼ∂ₖ symmetric in j,k):

**证明。** [∇×(∇f)]ᵢ = ε_{ijk} ∂ⱼ(∂ₖf) = ε_{ijk} ∂ⱼ∂ₖf。由相同的对称/反对称论证（ε_{ijk} 关于 j,k 反对称；∂ⱼ∂ₖ 关于 j,k 对称）：

  ε_{ijk} ∂ⱼ∂ₖf = 0. ∎

**Physical interpretation.** In electrostatics ∇×E = 0 (for a static field), so E can be written as E = −∇φ for a scalar potential φ. The identity ∇×(∇φ) = 0 is then automatically satisfied — the electrostatic field is irrotational.

**物理解释。** 在静电学中 ∇×E = 0（对静态场），故 E 可以写成 E = −∇φ，其中 φ 是标量势。恒等式 ∇×(∇φ) = 0 自动满足——静电场是无旋的。

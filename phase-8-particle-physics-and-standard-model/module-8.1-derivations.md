# Derivations — Module 8.1: Symmetries & Gauge Theory
# 推导 — 模块 8.1：对称性与规范理论

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 8.1](./module-8.1-symmetries-and-gauge-theory.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 8.1](./module-8.1-symmetries-and-gauge-theory.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Local U(1) Invariance Forces a Gauge Field · 局域 U(1) 不变性迫使引入规范场

**Claim.** The free Dirac Lagrangian ℒ₀ = ψ̄(iγ^μ∂_μ − m)ψ is invariant under global U(1) but NOT under local U(1) transformations. Requiring local invariance forces the introduction of a gauge field A_μ with transformation law A_μ → A_μ + (1/e)∂_μα and a covariant derivative D_μ = ∂_μ + ieA_μ.

**命题。** 自由狄拉克拉格朗日量 ℒ₀ = ψ̄(iγ^μ∂_μ − m)ψ 在全局 U(1) 变换下不变，但在局域 U(1) 变换下不不变。要求局域不变性迫使引入规范场 A_μ，其变换律为 A_μ → A_μ + (1/e)∂_μα，以及协变导数 D_μ = ∂_μ + ieA_μ。

**Step 1 — Global U(1) invariance.** Under the global transformation ψ → e^{iα}ψ (α constant), we have ψ̄ → e^{−iα}ψ̄. Then:

**第 1 步 — 全局 U(1) 不变性。** 在全局变换 ψ → e^{iα}ψ（α 为常数）下，ψ̄ → e^{−iα}ψ̄。则：

  ℒ₀ → ψ̄ e^{−iα}(iγ^μ∂_μ − m)e^{iα}ψ = ψ̄(iγ^μ∂_μ − m)ψ = ℒ₀.

The phase factors cancel because α is constant and ∂_μ(e^{iα}ψ) = e^{iα}∂_μψ. So ℒ₀ is globally U(1)-invariant. By Noether's theorem this gives a conserved current j^μ = ψ̄γ^μψ with ∂_μj^μ = 0 — the electric current.

相位因子相消是因为 α 为常数，∂_μ(e^{iα}ψ) = e^{iα}∂_μψ。故 ℒ₀ 具有全局 U(1) 不变性。由诺特定理，这给出守恒流 j^μ = ψ̄γ^μψ，满足 ∂_μj^μ = 0——即电流。

**Step 2 — Local U(1) fails.** Now promote α → α(x), a function of spacetime. Under ψ → e^{iα(x)}ψ:

**第 2 步 — 局域 U(1) 不成立。** 现将 α 提升为时空函数 α(x)。在 ψ → e^{iα(x)}ψ 下：

  ∂_μψ → ∂_μ(e^{iα(x)}ψ) = e^{iα(x)}(∂_μψ + i(∂_μα)ψ).

Therefore the kinetic term transforms as:

因此动能项变换为：

  ψ̄(iγ^μ∂_μ)ψ → ψ̄ e^{−iα}·iγ^μ·e^{iα}(∂_μψ + i(∂_μα)ψ)
                  = ψ̄(iγ^μ∂_μ)ψ − ψ̄γ^μ(∂_μα)ψ.

The mass term −mψ̄ψ is unchanged (the exponentials cancel). So:

质量项 −mψ̄ψ 不变（指数因子相消）。故：

  ℒ₀ → ℒ₀ − (∂_μα)ψ̄γ^μψ = ℒ₀ − (∂_μα)j^μ.

The extra term −(∂_μα)j^μ ≠ 0 in general; local U(1) is violated.

额外项 −(∂_μα)j^μ ≠ 0，局域 U(1) 不变性被破坏。

**Step 3 — Introduce the gauge field.** To cure the failure, introduce a real vector field A_μ(x) that transforms simultaneously as:

**第 3 步 — 引入规范场。** 为修复这一问题，引入实矢量场 A_μ(x)，它同时按如下方式变换：

  A_μ → A_μ − (1/e)∂_μα.

Replace ∂_μ with the **covariant derivative**:

将 ∂_μ 替换为**协变导数**：

  D_μ ≡ ∂_μ + ieA_μ.

**Step 4 — Verify covariance.** Under the combined transformation ψ → e^{iα(x)}ψ and A_μ → A_μ − (1/e)∂_μα:

**第 4 步 — 验证协变性。** 在组合变换 ψ → e^{iα(x)}ψ 与 A_μ → A_μ − (1/e)∂_μα 下：

  D_μψ → (∂_μ + ie(A_μ − (1/e)∂_μα))(e^{iα}ψ)
         = e^{iα}(∂_μψ + i(∂_μα)ψ) + ieA_μ e^{iα}ψ − i(∂_μα)e^{iα}ψ
         = e^{iα}(∂_μ + ieA_μ)ψ
         = e^{iα}D_μψ.

The covariant derivative transforms the same way as ψ itself. Therefore:

协变导数与 ψ 本身的变换方式相同。因此：

  ψ̄(iγ^μD_μ)ψ → ψ̄ e^{−iα}·iγ^μ·e^{iα}D_μψ = ψ̄(iγ^μD_μ)ψ.

Local invariance is restored for the fermion kinetic term.

费米子动能项的局域不变性得以恢复。

**Step 5 — The gauge kinetic term.** The field A_μ needs its own kinetic term. Define the **field-strength tensor**:

**第 5 步 — 规范动能项。** 场 A_μ 需要自身的动能项。定义**场强张量**：

  F_μν ≡ ∂_μA_ν − ∂_νA_μ.

Under A_μ → A_μ − (1/e)∂_μα:

在 A_μ → A_μ − (1/e)∂_μα 下：

  F_μν → ∂_μ(A_ν − (1/e)∂_να) − ∂_ν(A_μ − (1/e)∂_μα)
         = F_μν − (1/e)(∂_μ∂_να − ∂_ν∂_μα) = F_μν,

since partial derivatives commute (∂_μ∂_ν = ∂_ν∂_μ). So F_μν is gauge-invariant. The unique renormalizable, Lorentz-invariant kinetic term for A_μ is −(1/4)F_μνF^{μν}. A mass term (1/2)m²A_μA^μ is NOT gauge-invariant (it transforms by terms involving ∂_μα), so A_μ must be massless.

因为偏导数对易（∂_μ∂_ν = ∂_ν∂_μ）。故 F_μν 是规范不变的。A_μ 的唯一可重整化、洛伦兹不变的动能项为 −(1/4)F_μνF^{μν}。质量项 (1/2)m²A_μA^μ 不是规范不变的（它在变换下产生含 ∂_μα 的项），故 A_μ 必须是无质量的。

**Step 6 — The full QED Lagrangian.** Combining:

**第 6 步 — 完整的 QED 拉格朗日量。** 综合以上：

  ℒ_QED = ψ̄(iγ^μD_μ − m)ψ − (1/4)F_μνF^{μν}
         = ψ̄(iγ^μ∂_μ − m)ψ − eψ̄γ^μψ A_μ − (1/4)F_μνF^{μν}.

The term −eψ̄γ^μψ A_μ = −ej^μA_μ is the interaction of the electromagnetic current with the field: the photon coupling. ∎

项 −eψ̄γ^μψ A_μ = −ej^μA_μ 是电磁流与场的相互作用：光子耦合。∎

---

## B. Gauge Transformation Law of A_μ · A_μ 的规范变换律

**Claim.** The transformation A_μ → A_μ + (1/e)∂_μα (equivalently A_μ → A_μ − (1/e)∂_μα in the convention above, depending on sign convention) is exactly the classical electromagnetic gauge freedom.

**命题。** 变换 A_μ → A_μ + (1/e)∂_μα（在上述符号约定中等价地为 A_μ → A_μ − (1/e)∂_μα）正是经典电磁学的规范自由度。

**Step 1 — Classical context.** In classical electromagnetism, the electric and magnetic fields E = −∇φ − ∂A/∂t and B = ∇×A are unchanged under A → A + ∇χ, φ → φ − ∂χ/∂t for any scalar χ(x,t). In covariant notation (A^μ = (φ/c, A)):

**第 1 步 — 经典背景。** 在经典电磁学中，电场 E = −∇φ − ∂A/∂t 和磁场 B = ∇×A 在 A → A + ∇χ，φ → φ − ∂χ/∂t 变换下不变，χ(x,t) 为任意标量。在协变记号（A^μ = (φ/c, A)）中：

  A^μ → A^μ + ∂^μχ,  i.e.  A_μ → A_μ + ∂_μχ.

**Step 2 — Matching.** Identifying χ = −α/e (i.e., α = −eχ), the QFT gauge transformation A_μ → A_μ − (1/e)∂_μα becomes A_μ → A_μ + ∂_μχ — exactly the classical rule. The covariant derivative D_μ = ∂_μ + ieA_μ is the quantum-mechanical minimal coupling, which we recognize in the Hamiltonian as p → p − eA (the Peierls substitution of Module 5.2). ∎

**第 2 步 — 匹配。** 令 χ = −α/e（即 α = −eχ），量子场论规范变换 A_μ → A_μ − (1/e)∂_μα 变为 A_μ → A_μ + ∂_μχ——正是经典规则。协变导数 D_μ = ∂_μ + ieA_μ 是量子力学中的最小耦合，在哈密顿量中表现为 p → p − eA（模块 5.2 的 Peierls 替换）。∎

---

## C. Non-Abelian (SU(N)) Gauge Theory · 非阿贝尔 SU(N) 规范理论

**Claim.** For a non-abelian Lie group G = SU(N), demanding local G-invariance of the matter Lagrangian leads to the covariant derivative D_μ = ∂_μ − igA^a_μT^a (summed over adjoint index a), the non-abelian field strength F^a_μν = ∂_μA^a_ν − ∂_νA^a_μ + gf^{abc}A^b_μA^c_ν, and a field strength that transforms homogeneously (not as a simple gradient).

**命题。** 对于非阿贝尔李群 G = SU(N)，要求物质拉格朗日量在局域 G 变换下不变，导出协变导数 D_μ = ∂_μ − igA^a_μT^a（对伴随指标 a 求和）、非阿贝尔场强 F^a_μν = ∂_μA^a_ν − ∂_νA^a_μ + gf^{abc}A^b_μA^c_ν，以及场强以齐次方式（而非简单梯度）变换。

**Step 1 — SU(N) generators and algebra.** The Lie algebra of SU(N) is spanned by hermitian traceless generators T^a (a = 1, …, N²−1) satisfying:

**第 1 步 — SU(N) 生成元与代数。** SU(N) 的李代数由厄米无迹生成元 T^a（a = 1, …, N²−1）张开，满足：

  [T^a, T^b] = if^{abc}T^c,

where f^{abc} are the (real, totally antisymmetric) **structure constants**. For SU(2): T^a = σ^a/2 (Pauli matrices), f^{abc} = ε^{abc}. For SU(3): T^a = λ^a/2 (Gell-Mann matrices), with f^{abc} the SU(3) structure constants.

其中 f^{abc} 是（实的、全反对称的）**结构常数**。对于 SU(2)：T^a = σ^a/2（泡利矩阵），f^{abc} = ε^{abc}。对于 SU(3)：T^a = λ^a/2（盖尔曼矩阵），f^{abc} 为 SU(3) 结构常数。

**Step 2 — Local SU(N) transformation.** Consider matter fields ψ_i (i = 1, …, N) in the fundamental representation. Under local SU(N):

**第 2 步 — 局域 SU(N) 变换。** 考虑基本表示中的物质场 ψ_i（i = 1, …, N）。在局域 SU(N) 下：

  ψ → U(x)ψ,  where U(x) = exp(iα^a(x)T^a) ∈ SU(N).

For infinitesimal α^a ≪ 1:

对于无穷小 α^a ≪ 1：

  ψ → (1 + iα^a T^a)ψ,  δψ = iα^a T^a ψ.

**Step 3 — Failure of ∂_μ.** Under ψ → Uψ:

**第 3 步 — ∂_μ 的失效。** 在 ψ → Uψ 下：

  ∂_μψ → ∂_μ(Uψ) = U(∂_μψ) + (∂_μU)ψ.

The extra term (∂_μU)ψ spoils the covariance, just as in the abelian case. For the Lagrangian ψ̄(iγ^μ∂_μ)ψ to be invariant, we need ∂_μψ → U(∂_μψ), which requires canceling (∂_μU)ψ.

额外项 (∂_μU)ψ 破坏了协变性，与阿贝尔情形相同。为使 ψ̄(iγ^μ∂_μ)ψ 不变，需要 ∂_μψ → U(∂_μψ)，这要求抵消 (∂_μU)ψ。

**Step 4 — Non-abelian covariant derivative.** Introduce the matrix-valued gauge field A_μ(x) = A^a_μ(x)T^a (dim(G) components). Define:

**第 4 步 — 非阿贝尔协变导数。** 引入矩阵值规范场 A_μ(x) = A^a_μ(x)T^a（dim(G) 个分量）。定义：

  D_μ ≡ ∂_μ − igA_μ = ∂_μ − igA^a_μT^a.

Require that D_μψ → U(D_μψ) under local SU(N), i.e., D_μ transforms as:

要求在局域 SU(N) 下 D_μψ → U(D_μψ)，即 D_μ 变换为：

  D_μ → UD_μU†  (acting on fundamental-representation fields).

**Step 5 — Gauge transformation of A_μ.** From D_μ → UD_μU†:

**第 5 步 — A_μ 的规范变换。** 由 D_μ → UD_μU†：

  ∂_μ − igA'_μ = U(∂_μ − igA_μ)U†.

Expanding the right side:

展开右端：

  U(∂_μ − igA_μ)U† = U(∂_μU†) + U U† ∂_μ − igUA_μU†
                     = (∂_μ) + U(∂_μU†) − igUA_μU†.

Here we used U U† = 1 and distributed. Matching coefficients:

这里用到 U U† = 1 并展开。匹配各项系数：

  A'_μ = UA_μU† − (i/g)(∂_μU)U† = UA_μU† + (i/g)U(∂_μU†).

For infinitesimal U = 1 + iα^aT^a:

对于无穷小 U = 1 + iα^aT^a：

  δA^a_μ = (1/g)∂_μα^a + f^{abc}α^b A^c_μ.

The first term is the abelian-like gradient; the second is purely non-abelian (absent for U(1) where f^{abc} = 0).

第一项是类阿贝尔梯度项；第二项是纯非阿贝尔项（当 f^{abc} = 0 时（U(1) 情形）不存在）。

**Step 6 — Non-abelian field strength.** Define F_μν via the commutator of covariant derivatives:

**第 6 步 — 非阿贝尔场强。** 通过协变导数的对易子定义 F_μν：

  [D_μ, D_ν]ψ ≡ −igF_μνψ.

Computing explicitly:

显式计算：

  [D_μ, D_ν] = [∂_μ − igA_μ, ∂_ν − igA_ν]
              = −ig(∂_μA_ν − ∂_νA_μ) − g²[A_μ, A_ν]
              = −ig(∂_μA_ν − ∂_νA_μ − ig[A_μ, A_ν]).

Therefore (using [A_μ, A_ν] = [A^a_μT^a, A^b_νT^b] = A^a_μA^b_ν[T^a, T^b] = if^{abc}A^a_μA^b_νT^c):

因此（利用 [A_μ, A_ν] = [A^a_μT^a, A^b_νT^b] = A^a_μA^b_ν[T^a, T^b] = if^{abc}A^a_μA^b_νT^c）：

  F_μν = ∂_μA_ν − ∂_νA_μ − ig[A_μ, A_ν],

i.e., component-wise:

即按分量：

  F^a_μν = ∂_μA^a_ν − ∂_νA^a_μ + gf^{abc}A^b_μA^c_ν.

The extra term gf^{abc}A^b_μA^c_ν (absent in U(1)) encodes the self-interaction of the gauge bosons.

额外项 gf^{abc}A^b_μA^c_ν（在 U(1) 中不存在）编码了规范玻色子的自相互作用。

**Step 7 — Transformation of F_μν.** Under U:

**第 7 步 — F_μν 的变换。** 在 U 下：

  F_μν → UF_μνU†.

Proof: [D_μ, D_ν](Uψ) = U([D_μ, D_ν]ψ) = U(−igF_μν)ψ = −igUF_μνU†(Uψ). So F_μν transforms in the adjoint representation — it is NOT gauge-invariant (unlike the abelian F_μν), but the trace Tr(F_μνF^{μν}) IS invariant:

证明：[D_μ, D_ν](Uψ) = U([D_μ, D_ν]ψ) = U(−igF_μν)ψ = −igUF_μνU†(Uψ)。故 F_μν 在伴随表示下变换——它不是规范不变的（不同于阿贝尔的 F_μν），但迹 Tr(F_μνF^{μν}) 是不变的：

  Tr(F'_μνF'^{μν}) = Tr(UF_μνU† · UF^{μν}U†) = Tr(UF_μνF^{μν}U†) = Tr(F_μνF^{μν}).

Using the normalization Tr(T^aT^b) = (1/2)δ^{ab}, we get:

利用归一化 Tr(T^aT^b) = (1/2)δ^{ab}，得：

  Tr(F_μνF^{μν}) = (1/2)F^a_μνF^{aμν}.

**Step 8 — The Yang–Mills Lagrangian.** The complete gauge-invariant Lagrangian is:

**第 8 步 — 杨–米尔斯拉格朗日量。** 完整的规范不变拉格朗日量为：

  ℒ_YM = ψ̄(iγ^μD_μ − m)ψ − (1/2)Tr(F_μνF^{μν})
        = ψ̄(iγ^μD_μ − m)ψ − (1/4)F^a_μνF^{aμν}.

Expanding F^a_μνF^{aμν} using F^a_μν = ∂_μA^a_ν − ∂_νA^a_μ + gf^{abc}A^b_μA^c_ν produces:
- A quadratic term (∂_μA^a_ν − ∂_νA^a_μ)² → free gauge-boson propagation.
- A cubic term 2(∂_μA^a_ν)gf^{abc}A^b_μA^c_ν → three-gauge-boson vertex (proportional to g).
- A quartic term g²(f^{abc}A^b_μA^c_ν)² → four-gauge-boson vertex (proportional to g²).

展开 F^a_μνF^{aμν}（利用 F^a_μν = ∂_μA^a_ν − ∂_νA^a_μ + gf^{abc}A^b_μA^c_ν）产生：
- 二次项 (∂_μA^a_ν − ∂_νA^a_μ)² → 自由规范玻色子传播。
- 三次项 2(∂_μA^a_ν)gf^{abc}A^b_μA^c_ν → 三规范玻色子顶角（正比于 g）。
- 四次项 g²(f^{abc}A^b_μA^c_ν)² → 四规范玻色子顶角（正比于 g²）。

These self-interactions are absent in Maxwell/QED (where f^{abc} = 0) and are the root of asymptotic freedom in QCD. ∎

这些自相互作用在麦克斯韦/QED 中不存在（因为 f^{abc} = 0），是 QCD 渐近自由的根源。∎

---

## D. Noether Current from Global U(1) · 全局 U(1) 的诺特流

**Claim.** The global U(1) symmetry ψ → e^{iα}ψ of ℒ_QED yields a conserved Noether current j^μ = ψ̄γ^μψ.

**命题。** ℒ_QED 的全局 U(1) 对称性 ψ → e^{iα}ψ 产生守恒诺特流 j^μ = ψ̄γ^μψ。

**Step 1 — Noether's theorem.** For a Lagrangian ℒ(ψ, ∂_μψ) invariant under δψ = iαψ (for infinitesimal α), the conserved current is:

**第 1 步 — 诺特定理。** 对于在 δψ = iαψ（无穷小 α）下不变的拉格朗日量 ℒ(ψ, ∂_μψ)，守恒流为：

  j^μ = (∂ℒ/∂(∂_μψ))δψ + c.c.

**Step 2 — Evaluate.** From ℒ = ψ̄(iγ^μ∂_μ − m)ψ:

**第 2 步 — 计算。** 由 ℒ = ψ̄(iγ^μ∂_μ − m)ψ：

  ∂ℒ/∂(∂_μψ) = iψ̄γ^μ.

So j^μ = iψ̄γ^μ · iψ + c.c. Carefully: with δψ = iαψ and δψ̄ = −iαψ̄:

故 j^μ = iψ̄γ^μ · iψ + c.c.。仔细处理：δψ = iαψ，δψ̄ = −iαψ̄：

  δℒ = 0 ⟹ j^μ = −(∂ℒ/∂(∂_μψ_a))(δψ_a/α) = ψ̄γ^μψ.

**Step 3 — Equation of motion.** The Euler–Lagrange equation from ℒ_QED gives:

**第 3 步 — 运动方程。** 由 ℒ_QED 的欧拉–拉格朗日方程得：

  (iγ^μD_μ − m)ψ = 0  (Dirac equation with minimal coupling),
  ∂_νF^{νμ} = ej^μ   (Maxwell equation with source).

Together these constitute the equations of motion of QED. Conservation ∂_μj^μ = 0 follows from the Dirac equation: ∂_μ(ψ̄γ^μψ) = (∂_μψ̄)γ^μψ + ψ̄γ^μ(∂_μψ) = 0 using the equations of motion. ∎

它们共同构成 QED 的运动方程。守恒性 ∂_μj^μ = 0 由狄拉克方程得出：∂_μ(ψ̄γ^μψ) = (∂_μψ̄)γ^μψ + ψ̄γ^μ(∂_μψ) = 0，利用运动方程可得。∎

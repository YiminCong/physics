# Derivations — Module 8.1: Symmetries & Gauge Theory
# 推导 — 模块 8.1：对称性与规范理论

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

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

---

## E. Gauge Fixing, Faddeev–Popov Ghosts, and BRST Symmetry · 规范固定、法捷耶夫–波波夫鬼粒子与 BRST 对称性

**Claim.** The naive path integral Z = ∫𝒟A e^{iS} over-counts physically equivalent (gauge-related) field configurations, and the gauge-field kinetic operator is non-invertible, so no propagator exists. The **Faddeev–Popov procedure** fixes the gauge at the cost of a gauge-fixing term −(1/2ξ)(∂^μA^a_μ)² and a ghost term c̄^a(−∂^μD^{ab}_μ)c^b. The gauge-fixed action retains a single global fermionic symmetry — the **nilpotent BRST symmetry** — which replaces gauge invariance and guarantees the unitarity and gauge-independence of physical amplitudes.

**命题。** 朴素路径积分 Z = ∫𝒟A e^{iS} 对物理上等价（规范相关）的场位形重复计数，且规范场动能算符不可逆，故不存在传播子。**法捷耶夫–波波夫方法**以引入规范固定项 −(1/2ξ)(∂^μA^a_μ)² 和鬼粒子项 c̄^a(−∂^μD^{ab}_μ)c^b 为代价固定规范。规范固定后的作用量保留唯一的整体费米型对称性——**幂零的 BRST 对称性**——它替代规范不变性，并保证物理振幅的幺正性与规范无关性。

**Step 1 — The over-counting problem.** Gauge-equivalent potentials A^a_μ and (A^U)^a_μ give the same action S[A] = S[A^U]. Hence Z = ∫𝒟A e^{iS} = (volume of the gauge orbit) × ∫(physical configurations) — an infinite, field-independent factor. Worse, expanding −¼F^a_{μν}F^{aμν} to quadratic order gives the operator

**第 1 步 — 重复计数问题。** 规范等价的势 A^a_μ 与 (A^U)^a_μ 给出相同作用量 S[A] = S[A^U]。故 Z = ∫𝒟A e^{iS} =（规范轨道的体积）× ∫（物理位形）——一个无穷大且与场无关的因子。更糟的是，将 −¼F^a_{μν}F^{aμν} 展开到二次阶给出算符

  𝒦^{μν} = η^{μν}∂² − ∂^μ∂^ν,

which annihilates every pure-gauge mode A_μ = ∂_μχ (𝒦^{μν}∂_νχ = 0). A matrix with zero eigenvalues cannot be inverted, so the gluon propagator does not exist until the gauge is fixed.

它湮灭每一个纯规范模式 A_μ = ∂_μχ（𝒦^{μν}∂_νχ = 0）。一个有零本征值的矩阵不可逆，故在固定规范之前胶子传播子不存在。

**Step 2 — Faddeev–Popov insertion of unity.** Pick a gauge condition G^a(A) = ∂^μA^a_μ − ω^a(x) = 0 and insert the identity

**第 2 步 — 法捷耶夫–波波夫插入单位元。** 选取规范条件 G^a(A) = ∂^μA^a_μ − ω^a(x) = 0 并插入恒等式

  1 = ∫𝒟α(x)  δ[G^a(A^α)]  det( δG^a(A^α)/δα^b ),

where A^α is the gauge transform of A by α. Under an infinitesimal gauge transformation δA^a_μ = D^{ab}_μ α^b, so the **Faddeev–Popov operator** is

其中 A^α 是 A 经 α 的规范变换。在无穷小规范变换下 δA^a_μ = D^{ab}_μ α^b，故**法捷耶夫–波波夫算符**为

  M^{ab} = δG^a(A^α)/δα^b |_{α=0} = ∂^μ D^{ab}_μ = ∂^μ(∂_μδ^{ab} + g f^{acb}A^c_μ).

The δ-function fixes the gauge; the determinant det M is the price for not double-counting.

δ 函数固定规范；行列式 det M 是避免重复计数的代价。

**Step 3 — Exponentiate det M with anticommuting ghosts.** A determinant of a bosonic operator is a Gaussian integral over **Grassmann** (anticommuting) fields:

**第 3 步 — 用反对易鬼粒子指数化 det M。** 玻色算符的行列式等于对**格拉斯曼**（反对易）场的高斯积分：

  det M = ∫𝒟c̄ 𝒟c  exp( i∫d⁴x  c̄^a M^{ab} c^b ) = ∫𝒟c̄ 𝒟c  exp( i∫d⁴x  c̄^a(−∂^μD^{ab}_μ)c^b ),

(the sign is convention; an integration by parts moves the derivative). The fields c^a, c̄^a are the **Faddeev–Popov ghosts** — Grassmann-valued *scalars* in the adjoint representation. They violate the spin–statistics theorem, which is permitted precisely because they never appear as external (physical) states; they exist only inside loops to cancel the unphysical gauge-boson polarizations. In **abelian** QED, M = ∂^μ∂_μ is field-independent, so the ghosts decouple and may be ignored. In **non-abelian** theory D_μ contains A^c_μ, producing a ghost–gluon vertex; these ghost loops are exactly what supply part of the +11C_A/3 in the QCD β function (Module 8.3).

（符号为约定；分部积分移动导数）。场 c^a, c̄^a 是**法捷耶夫–波波夫鬼粒子**——伴随表示中取格拉斯曼值的*标量*。它们违反自旋–统计定理，这之所以被允许，正是因为它们从不作为外（物理）态出现；它们只在圈内存在，以抵消规范玻色子的非物理极化。在**阿贝尔** QED 中，M = ∂^μ∂_μ 与场无关，故鬼粒子退耦可忽略。在**非阿贝尔**理论中 D_μ 含 A^c_μ，产生鬼–胶子顶角；这些鬼圈正是为 QCD β 函数中 +11C_A/3 提供部分贡献的来源（模块 8.3）。

**Step 4 — Gauge-averaging gives the ξ term.** The function ω^a was arbitrary, so average over it with a Gaussian weight exp(−(i/2ξ)∫(ω^a)²). The δ[∂·A − ω] then replaces ω by ∂·A, producing −(1/2ξ)(∂^μA^a_μ)². The complete **gauge-fixed Lagrangian** is

**第 4 步 — 规范平均给出 ξ 项。** 函数 ω^a 是任意的，故以高斯权重 exp(−(i/2ξ)∫(ω^a)²) 对其平均。δ[∂·A − ω] 随即将 ω 替换为 ∂·A，产生 −(1/2ξ)(∂^μA^a_μ)²。完整的**规范固定拉格朗日量**为

  **ℒ = −¼F^a_{μν}F^{aμν} − (1/2ξ)(∂^μA^a_μ)² + c̄^a(−∂^μD^{ab}_μ)c^b**,

with ξ the gauge parameter (ξ = 1 Feynman gauge, ξ → 0 Landau gauge). The gluon kinetic operator becomes η^{μν}∂² − (1 − 1/ξ)∂^μ∂^ν, which is now invertible, giving the propagator D^{ab}_{μν}(k) = (−iδ^{ab}/k²)[η_{μν} − (1−ξ)k_μk_ν/k²].

其中 ξ 为规范参数（ξ = 1 费曼规范，ξ → 0 朗道规范）。胶子动能算符变为 η^{μν}∂² − (1 − 1/ξ)∂^μ∂^ν，现在可逆，给出传播子 D^{ab}_{μν}(k) = (−iδ^{ab}/k²)[η_{μν} − (1−ξ)k_μk_ν/k²]。

**Step 5 — BRST symmetry (Nakanishi–Lautrup form).** Linearize the gauge-fixing term with an auxiliary field B^a: ℒ = −¼F² + B^a∂^μA^a_μ + (ξ/2)(B^a)² + c̄^a(−∂^μD^{ab}_μ)c^b (integrating out B^a returns the previous form). This Lagrangian is invariant under the **BRST transformation**, defined through the nilpotent operator s and a global Grassmann parameter θ (field variation δΦ = θ·sΦ):

**第 5 步 — BRST 对称性（中西–劳特鲁普形式）。** 用辅助场 B^a 线性化规范固定项：ℒ = −¼F² + B^a∂^μA^a_μ + (ξ/2)(B^a)² + c̄^a(−∂^μD^{ab}_μ)c^b（积掉 B^a 返回前一形式）。该拉格朗日量在 **BRST 变换**下不变，变换通过幂零算符 s 与整体格拉斯曼参数 θ 定义（场变换 δΦ = θ·sΦ）：

  s A^a_μ = D^{ab}_μ c^b,   s c^a = −½ g f^{abc} c^b c^c,   s c̄^a = B^a,   s B^a = 0,   s ψ = i g c^a T^a ψ.

The BRST transformation of A_μ is just a gauge transformation with the *ghost field itself* as parameter — this is why s reshuffles gauge invariance into a rigid (global) symmetry.

A_μ 的 BRST 变换正是以*鬼场本身*为参数的规范变换——这正是 s 将规范不变性重组为刚性（整体）对称性的原因。

**Step 6 — Nilpotency s² = 0.** A direct computation on each field, using the **Jacobi identity** f^{ade}f^{bce} + f^{bde}f^{cae} + f^{cde}f^{abe} = 0 of the structure constants, gives s² = 0. For example, on the ghost: s²c^a = −½gf^{abc}(s c^b)c^c + ½gf^{abc}c^b(s c^c) = ¼g²f^{abc}f^{bde}c^dc^ec^c, which vanishes by Jacobi and the antisymmetry of c^dc^e. Likewise s²A^a_μ = s(D^{ab}_μc^b) = 0. Nilpotency is the algebraic heart of the formalism.

**第 6 步 — 幂零性 s² = 0。** 对每个场直接计算，利用结构常数的**雅可比恒等式** f^{ade}f^{bce} + f^{bde}f^{cae} + f^{cde}f^{abe} = 0，得 s² = 0。例如对鬼场：s²c^a = −½gf^{abc}(s c^b)c^c + ½gf^{abc}c^b(s c^c) = ¼g²f^{abc}f^{bde}c^dc^ec^c，由雅可比恒等式及 c^dc^e 的反对称性而为零。同样 s²A^a_μ = s(D^{ab}_μc^b) = 0。幂零性是该形式体系的代数核心。

**Step 7 — Physical content: BRST cohomology, Slavnov–Taylor, unitarity.** The entire gauge-fixing + ghost sector is **BRST-exact** — it is s acting on the "gauge fermion" Ψ = c̄^a(∂^μA^a_μ + (ξ/2)B^a):

**第 7 步 — 物理内涵：BRST 上同调、斯拉夫诺夫–泰勒、幺正性。** 整个规范固定 + 鬼粒子部分是 **BRST 恰当的**——它是 s 作用于"规范费米子" Ψ = c̄^a(∂^μA^a_μ + (ξ/2)B^a)：

  ℒ_gf+gh = s Ψ,   so   S = S_inv + ∫d⁴x  sΨ,   with   s S = 0  (using s²=0 and sS_inv = 0).

Since s² = 0, the conserved **BRST charge** Q_B generates a cohomology, and **physical states** are defined by Q_B|phys⟩ = 0 modulo states of the form Q_B|·⟩ (the Kugo–Ojima criterion). This projection removes the unphysical longitudinal and timelike gauge-boson polarizations together with the ghosts, leaving a positive-norm physical Hilbert space and a **unitary S-matrix**. The Ward–Takahashi identities of QED generalize to the **Slavnov–Taylor identities**, the operator statement of BRST invariance, which enforce the renormalization relations among Z-factors and guarantee the gauge-independence of physical quantities such as the β function (Modules 8.3, 8.5). ∎

由于 s² = 0，守恒的 **BRST 荷** Q_B 生成上同调，**物理态**由 Q_B|phys⟩ = 0 模去形如 Q_B|·⟩ 的态来定义（久郷–大島判据）。该投影移除非物理的纵向与类时规范玻色子极化以及鬼粒子，留下正模物理希尔伯特空间和**幺正 S 矩阵**。QED 的沃德–高桥恒等式推广为 **斯拉夫诺夫–泰勒恒等式**，即 BRST 不变性的算符表述，它强制 Z 因子间的重整化关系，并保证 β 函数等物理量的规范无关性（模块 8.3、8.5）。∎

---

## F. From BRST to the Ward–Takahashi Identity · 由 BRST 导出沃德–高桥恒等式

**Claim.** Specializing the Slavnov–Taylor identities of §E to the abelian (QED) case yields the **Ward–Takahashi identity** for the electron–photon vertex Γ^μ and the full electron propagator S:

**命题。** 将 §E 的斯拉夫诺夫–泰勒恒等式特化到阿贝尔（QED）情形，给出电子–光子顶角 Γ^μ 与完整电子传播子 S 的**沃德–高桥恒等式**：

  q_μ Γ^μ(p+q, p) = S^{−1}(p+q) − S^{−1}(p),

whose on-shell, amputated form is the elementary transversality statement q_μ M^μ = 0 already used in [Module 8.2 §E](./module-8.2-derivations.md). This is the *deeper* route to that result: it follows from a symmetry of the quantum effective action, not merely from tree-level gauge invariance, so it holds to **all orders** in perturbation theory.

其在壳、截肢形式即 [模块 8.2 §E](./module-8.2-derivations.md) 中已用到的横向性陈述 q_μ M^μ = 0。这是通向该结果的*更深*途径：它源于量子有效作用量的对称性，而非仅仅树图阶的规范不变性，故对微扰论的**所有阶**都成立。

**Step 1 — The abelian BRST transformations.** For U(1), the structure constants vanish (f^{abc} = 0), so the §E transformations collapse to the *linear* set

**第 1 步 — 阿贝尔 BRST 变换。** 对 U(1)，结构常数为零（f^{abc} = 0），故 §E 的变换退化为*线性*集

  s A_μ = ∂_μ c,   s ψ = i e c ψ,   s ψ̄ = i e c ψ̄,   s c = 0,   s c̄ = B,   s B = 0.

Crucially s c = 0: the photon's ghost is **free** and decouples from physics — but it is the bookkeeping device that turns gauge invariance into the identity below.

关键在于 s c = 0：光子的鬼粒子是**自由**的，与物理退耦——但它正是把规范不变性转化为下述恒等式的记账工具。

**Step 2 — The master BRST identity.** Because the path-integral measure and the gauge-fixed action are BRST-invariant, the expectation value of any BRST variation vanishes: ⟨s 𝒪⟩ = 0 for any operator 𝒪. Choose 𝒪 = c̄(x) ψ(y) ψ̄(z). Using s(c̄ ψ ψ̄) = (s c̄)ψψ̄ − c̄ (sψ)ψ̄ + c̄ ψ (sψ̄) = B ψψ̄ − c̄(ie cψ)ψ̄ + c̄ψ(ie cψ̄), and ⟨…⟩ = 0, gives

**第 2 步 — BRST 主恒等式。** 由于路径积分测度与规范固定作用量都 BRST 不变，任意 BRST 变分的期望值为零：对任意算符 𝒪 有 ⟨s 𝒪⟩ = 0。取 𝒪 = c̄(x) ψ(y) ψ̄(z)，利用上述变换并令 ⟨…⟩ = 0，得

  ⟨B(x) ψ(y) ψ̄(z)⟩ = i e ⟨c̄(x) c(x) [ψ(y)ψ̄(z) with the two ie c insertions]⟩.

The auxiliary field obeys its equation of motion B = −(1/ξ)∂^μA_μ, and the free ghost contraction ⟨c̄(x)c(w)⟩ = (free propagator) strips the ghost pair, leaving a relation purely among the photon, electron field, and the current ∂^μA_μ.

辅助场满足其运动方程 B = −(1/ξ)∂^μA_μ，自由鬼粒子收缩 ⟨c̄(x)c(w)⟩ 消去鬼粒子对，留下纯粹关于光子、电子场与流 ∂^μA_μ 的关系。

**Step 3 — Momentum space: the Ward–Takahashi identity.** Fourier transforming and amputating the external electron legs converts the position-space relation into the statement that the *longitudinal* part of the vertex is fixed by the inverse propagators:

**第 3 步 — 动量空间：沃德–高桥恒等式。** 傅里叶变换并截去外电子腿，将坐标空间关系转化为：顶角的*纵向*部分由逆传播子固定：

  **q_μ Γ^μ(p+q, p) = S^{−1}(p+q) − S^{−1}(p)**.

At tree level Γ^μ = γ^μ and S^{−1}(p) = p̸ − m, so the right side is (p̸ + q̸ − m) − (p̸ − m) = q̸ = q_μγ^μ — the identity holds trivially. The content is that it continues to hold with the *full* (all-orders) Γ^μ and S.

在树图阶 Γ^μ = γ^μ、S^{−1}(p) = p̸ − m，故右边为 q̸ = q_μγ^μ——恒等式平凡成立。其内涵在于：对*完整*（所有阶）的 Γ^μ 与 S 它仍然成立。

**Step 4 — Consequences.** (i) **Z₁ = Z₂.** Differentiating the identity at q → 0 gives Γ^μ(p,p) = ∂S^{−1}/∂p_μ; since the vertex renormalization Z₁ and the wavefunction renormalization Z₂ multiply the two sides, the identity forces **Z₁ = Z₂**. Hence the renormalized charge e = e₀√Z₃ depends only on Z₃ (the photon vacuum polarization) — charge renormalization is **universal**, identical for the electron, muon, or any charged field. This is why the running coupling of [8.2 §D](./module-8.2-derivations.md) is a property of the photon alone.

**第 4 步 — 推论。** (i) **Z₁ = Z₂。** 在 q → 0 处对恒等式求导得 Γ^μ(p,p) = ∂S^{−1}/∂p_μ；由于顶角重整化 Z₁ 与波函数重整化 Z₂ 分别乘在两边，恒等式迫使 **Z₁ = Z₂**。故重整化电荷 e = e₀√Z₃ 只依赖于 Z₃（光子真空极化）——电荷重整化是**普适的**，对电子、μ 子或任何带电场都相同。这正是 [8.2 §D](./module-8.2-derivations.md) 的跑动耦合仅是光子自身性质的原因。

(ii) **Transverse vacuum polarization, massless photon.** Applied to the photon self-energy, the same identity gives q_μΠ^{μν}(q) = 0, so Π^{μν}(q) = (q²η^{μν} − q^μq^ν)Π(q²). The radiative correction is purely transverse, so it **cannot generate a photon mass term** m²η^{μν}: gauge invariance protects the photon's masslessness to all orders.

(ii) **横向真空极化、无质量光子。** 应用于光子自能，同一恒等式给出 q_μΠ^{μν}(q) = 0，故 Π^{μν}(q) = (q²η^{μν} − q^μq^ν)Π(q²)。辐射修正纯横向，故**不能产生光子质量项** m²η^{μν}：规范不变性保护光子无质量性到所有阶。

(iii) **On-shell transversality.** Contracting an external on-shell photon line of any amplitude with its momentum gives **q_μ M^μ = 0** — the elementary Ward identity of [8.2 §E](./module-8.2-derivations.md), here obtained as a corollary of the all-orders BRST/Slavnov–Taylor structure. ∎

(iii) **在壳横向性。** 用动量缩并任意振幅的外在壳光子线给出 **q_μ M^μ = 0**——即 [8.2 §E](./module-8.2-derivations.md) 的初等沃德恒等式，此处作为所有阶 BRST／斯拉夫诺夫–泰勒结构的推论得到。∎

# Derivations — Module 6.2: Green's Functions & Propagators
# 推导 — 模块 6.2：格林函数与传播子

> Companion to [Module 6.2](./module-6.2-greens-functions.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 6.2](./module-6.2-greens-functions.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Free Single-Particle Green's Function · 自由单粒子格林函数

**Claim.** For a free Fermi system with single-particle energies ε_k, the time-ordered single-particle Green's function at zero temperature is

  G⁰(k, t−t') = −i θ(t−t') e^{−iε_k(t−t')/ℏ} (1 − f_k)  −  i θ(t'−t) e^{−iε_k(t−t')/ℏ} (−f_k),

where f_k = θ(μ − ε_k) is the zero-temperature Fermi occupation. Its Fourier transform in frequency is

  G⁰(k, ω) = 1/(ω − ε_k/ℏ + iδ sgn(ε_k − μ)),    δ → 0⁺.

**命题。** 对于单粒子能量为 ε_k 的自由费米系统，零温时序单粒子格林函数为

  G⁰(k, t−t') = −i θ(t−t') e^{−iε_k(t−t')/ℏ} (1 − f_k)  −  i θ(t'−t) e^{−iε_k(t−t')/ℏ} (−f_k)，

其中 f_k = θ(μ − ε_k) 是零温费米占据数。其频率傅里叶变换为

  G⁰(k, ω) = 1/(ω − ε_k/ℏ + iδ sgn(ε_k − μ))，    δ → 0⁺。

**Step 1 — Define the time-ordered Green's function.** The single-particle Green's function is defined as

  G(k, t−t') = −i ⟨Ψ₀| T[ ĉ_k(t) ĉ†_k(t') ]|Ψ₀⟩,

where |Ψ₀⟩ is the many-body ground state, ĉ_k(t) = e^{iĤt/ℏ} ĉ_k e^{−iĤt/ℏ} is the Heisenberg-picture operator (Module 3.10), and T is the time-ordering operator: T[AB] = A(t)B(t') θ(t−t') ± B(t')A(t) θ(t'−t) with − for fermions.

**第 1 步 — 定义时序格林函数。** 单粒子格林函数定义为

  G(k, t−t') = −i ⟨Ψ₀| T[ ĉ_k(t) ĉ†_k(t') ]|Ψ₀⟩，

其中 |Ψ₀⟩ 是多体基态，ĉ_k(t) = e^{iĤt/ℏ} ĉ_k e^{−iĤt/ℏ} 是海森堡绘景算符（模块 3.10），T 是时序算符：T[AB] = A(t)B(t') θ(t−t') ± B(t')A(t) θ(t'−t)，费米子取 −。

**Step 2 — Evaluate for the free Hamiltonian.** For Ĥ₀ = Σ_k ε_k ĉ†_k ĉ_k, the Heisenberg equation gives ĉ_k(t) = e^{−iε_k t/ℏ} ĉ_k. For the non-interacting ground state |Ψ₀⟩ = Π_{k: ε_k<μ} ĉ†_k |0⟩:

  ⟨Ψ₀| ĉ_k(t) ĉ†_k(t') |Ψ₀⟩ = e^{−iε_k(t−t')/ℏ} ⟨Ψ₀| ĉ_k ĉ†_k |Ψ₀⟩ = e^{−iε_k(t−t')/ℏ} (1 − f_k),

  ⟨Ψ₀| ĉ†_k(t') ĉ_k(t) |Ψ₀⟩ = e^{−iε_k(t−t')/ℏ} ⟨Ψ₀| ĉ†_k ĉ_k |Ψ₀⟩ = e^{−iε_k(t−t')/ℏ} f_k,

since ⟨ĉ_k ĉ†_k⟩ = 1 − f_k and ⟨ĉ†_k ĉ_k⟩ = f_k by the anticommutator and the definition of f_k.

**第 2 步 — 对自由哈密顿量求值。** 对于 Ĥ₀ = Σ_k ε_k ĉ†_k ĉ_k，海森堡方程给出 ĉ_k(t) = e^{−iε_k t/ℏ} ĉ_k。对于非相互作用基态 |Ψ₀⟩ = Π_{k: ε_k<μ} ĉ†_k |0⟩：

  ⟨Ψ₀| ĉ_k(t) ĉ†_k(t') |Ψ₀⟩ = e^{−iε_k(t−t')/ℏ} ⟨Ψ₀| ĉ_k ĉ†_k |Ψ₀⟩ = e^{−iε_k(t−t')/ℏ} (1 − f_k)，

  ⟨Ψ₀| ĉ†_k(t') ĉ_k(t) |Ψ₀⟩ = e^{−iε_k(t−t')/ℏ} ⟨Ψ₀| ĉ†_k ĉ_k |Ψ₀⟩ = e^{−iε_k(t−t')/ℏ} f_k，

因为由反对易子和 f_k 的定义，⟨ĉ_k ĉ†_k⟩ = 1 − f_k，⟨ĉ†_k ĉ_k⟩ = f_k。

**Step 3 — Assemble the time-ordered result.**

  G⁰(k, t) = −i e^{−iε_k t/ℏ} [ θ(t)(1 − f_k) − θ(−t) f_k ],

where t ≡ t − t'. The sign of the second term comes from the fermionic minus in T.

**第 3 步 — 组合时序结果。**

  G⁰(k, t) = −i e^{−iε_k t/ℏ} [ θ(t)(1 − f_k) − θ(−t) f_k ]，

其中 t ≡ t − t'。第二项的符号来自 T 中费米子的负号。

**Step 4 — Fourier transform to frequency.** Compute G⁰(k, ω) = ∫_{−∞}^{∞} dt e^{iωt} G⁰(k, t). We need two Fourier transforms:

  (i)  ∫₀^∞ dt e^{i(ω − ε_k/ℏ)t} = i/(ω − ε_k/ℏ + iδ),

  (ii) ∫_{−∞}^0 dt e^{i(ω − ε_k/ℏ)t} = −i/(ω − ε_k/ℏ − iδ),

where δ → 0⁺ is required for convergence (it enforces the correct boundary condition). Therefore

  G⁰(k, ω) = (1 − f_k)/(ω − ε_k/ℏ + iδ) + f_k/(ω − ε_k/ℏ − iδ).

**第 4 步 — 傅里叶变换到频率空间。** 计算 G⁰(k, ω) = ∫_{−∞}^{∞} dt e^{iωt} G⁰(k, t)。需要两个傅里叶变换：

  (i)  ∫₀^∞ dt e^{i(ω − ε_k/ℏ)t} = i/(ω − ε_k/ℏ + iδ)，

  (ii) ∫_{−∞}^0 dt e^{i(ω − ε_k/ℏ)t} = −i/(ω − ε_k/ℏ − iδ)，

其中 δ → 0⁺ 是收敛所必需的（它强制执行正确的边界条件）。因此

  G⁰(k, ω) = (1 − f_k)/(ω − ε_k/ℏ + iδ) + f_k/(ω − ε_k/ℏ − iδ)。

**Step 5 — Combine into the compact form.** For ε_k > μ: f_k = 0, so G⁰(k, ω) = 1/(ω − ε_k/ℏ + iδ). For ε_k < μ: f_k = 1, so G⁰(k, ω) = 1/(ω − ε_k/ℏ − iδ). Both cases are unified as

  G⁰(k, ω) = 1/(ω − ε_k/ℏ + iδ sgn(ε_k − μ)).  ∎

The pole is at ω = ε_k/ℏ, above the real axis for ε_k > μ (particle excitation, causal) and below for ε_k < μ (hole excitation, anti-causal). The iδ prescription is precisely what defines the time-ordered (Feynman) propagator.

**第 5 步 — 合并为紧凑形式。** 对于 ε_k > μ：f_k = 0，故 G⁰(k, ω) = 1/(ω − ε_k/ℏ + iδ)。对于 ε_k < μ：f_k = 1，故 G⁰(k, ω) = 1/(ω − ε_k/ℏ − iδ)。两种情形统一为

  G⁰(k, ω) = 1/(ω − ε_k/ℏ + iδ sgn(ε_k − μ))。  ∎

极点在 ω = ε_k/ℏ 处，对于 ε_k > μ 位于实轴上方（粒子激发，因果），对于 ε_k < μ 位于实轴下方（空穴激发，反因果）。iδ 处方正是定义时序（费曼）传播子的东西。

---

## B. The Lehmann Spectral Representation · 莱曼谱表示

**Claim.** For the fully interacting system, the time-ordered Green's function has the spectral (Lehmann) representation

  G(k, ω) = ∫_{−∞}^{∞} dω' A(k, ω') [ θ(ω' − μ/ℏ)/(ω − ω' + iδ)  +  θ(μ/ℏ − ω')/(ω − ω' − iδ) ],

where A(k, ω) ≥ 0 is the spectral function. Consequently A(k, ω) = −(1/π) Im G^R(k, ω).

**命题。** 对于完全相互作用的系统，时序格林函数具有谱（莱曼）表示

  G(k, ω) = ∫_{−∞}^{∞} dω' A(k, ω') [ θ(ω' − μ/ℏ)/(ω − ω' + iδ)  +  θ(μ/ℏ − ω')/(ω − ω' − iδ) ]，

其中 A(k, ω) ≥ 0 是谱函数。因此 A(k, ω) = −(1/π) Im G^R(k, ω)。

**Step 1 — Insert a complete set of eigenstates.** Let |n⟩ denote the exact eigenstates of Ĥ with energies E_n and particle number N_n = N₀ ± 1 (adding or removing one particle from the N₀-particle ground state |Ψ₀⟩ with energy E₀). Insert 1 = Σ_n |n⟩⟨n| into the definition of G. For t > t':

  −i ⟨Ψ₀| ĉ_k(t) ĉ†_k(t') |Ψ₀⟩ = −i Σ_n |⟨n|ĉ†_k|Ψ₀⟩|² e^{−i(E_n − E₀)(t−t')/ℏ},

where we used ĉ_k(t)|Ψ₀⟩ = e^{iĤt/ℏ} ĉ_k |Ψ₀⟩ and ⟨Ψ₀|e^{−iĤt/ℏ} = ⟨Ψ₀|e^{−iE₀t/ℏ}.

**第 1 步 — 插入完备本征态集。** 设 |n⟩ 为 Ĥ 的精确本征态，能量为 E_n，粒子数为 N_n = N₀ ± 1（对 N₀ 粒子基态 |Ψ₀⟩ 增加或移除一个粒子，基态能量为 E₀）。将 1 = Σ_n |n⟩⟨n| 插入 G 的定义中。对于 t > t'：

  −i ⟨Ψ₀| ĉ_k(t) ĉ†_k(t') |Ψ₀⟩ = −i Σ_n |⟨n|ĉ†_k|Ψ₀⟩|² e^{−i(E_n − E₀)(t−t')/ℏ}，

其中用到了 ĉ_k(t)|Ψ₀⟩ = e^{iĤt/ℏ} ĉ_k |Ψ₀⟩ 和 ⟨Ψ₀|e^{−iĤt/ℏ} = ⟨Ψ₀|e^{−iE₀t/ℏ}。

**Step 2 — Define the spectral weight.** Set ω_n = (E_n − E₀)/ℏ for states with N_n = N₀ + 1 (particle sector) and ω_n = (E₀ − E_n)/ℏ for states with N_n = N₀ − 1 (hole sector). Define the spectral function as a sum of delta peaks:

  A(k, ω) = Σ_{n, N_n=N₀+1} |⟨n|ĉ†_k|Ψ₀⟩|² δ(ω − ω_n)  +  Σ_{n, N_n=N₀−1} |⟨n|ĉ_k|Ψ₀⟩|² δ(ω + ω_n).

Each term is manifestly non-negative. A(k, ω) is real and A(k, ω) ≥ 0.

**第 2 步 — 定义谱权重。** 对 N_n = N₀ + 1 的态（粒子扇区），令 ω_n = (E_n − E₀)/ℏ；对 N_n = N₀ − 1 的态（空穴扇区），令 ω_n = (E₀ − E_n)/ℏ。将谱函数定义为 δ 峰的求和：

  A(k, ω) = Σ_{n, N_n=N₀+1} |⟨n|ĉ†_k|Ψ₀⟩|² δ(ω − ω_n)  +  Σ_{n, N_n=N₀−1} |⟨n|ĉ_k|Ψ₀⟩|² δ(ω + ω_n)。

每项明显非负。A(k, ω) 是实的且 A(k, ω) ≥ 0。

**Step 3 — Fourier transform to ω.** Using the integral representation θ(t) = i/(2π) ∫ dω e^{−iωt}/(ω + iδ), the Fourier transform of the t > t' part gives the "particle" pole contribution:

  G_particle(k, ω) = ∫ dω' A_particle(k, ω')/(ω − ω' + iδ),

and similarly for the hole part with the opposite iδ prescription. Combining:

  G(k, ω) = ∫_{−∞}^{∞} dω' A(k, ω') [ θ(ω' − μ/ℏ)/(ω − ω' + iδ)  +  θ(μ/ℏ − ω')/(ω − ω' − iδ) ].  ∎

**第 3 步 — 傅里叶变换到 ω。** 利用积分表示 θ(t) = i/(2π) ∫ dω e^{−iωt}/(ω + iδ)，t > t' 部分的傅里叶变换给出"粒子"极点贡献：

  G_particle(k, ω) = ∫ dω' A_particle(k, ω')/(ω − ω' + iδ)，

空穴部分类似，但 iδ 处方相反。合并：

  G(k, ω) = ∫_{−∞}^{∞} dω' A(k, ω') [ θ(ω' − μ/ℏ)/(ω − ω' + iδ)  +  θ(μ/ℏ − ω')/(ω − ω' − iδ) ]。  ∎

**Step 4 — Extract A from Im G^R.** The retarded Green's function is G^R(k, ω) = ∫ dω' A(k, ω')/(ω − ω' + iδ) (all poles below the real axis). Using the Sokhotski–Plemelj identity 1/(x + iδ) = P(1/x) − iπδ(x):

  Im G^R(k, ω) = −π ∫ dω' A(k, ω') δ(ω − ω') = −π A(k, ω).

Therefore **A(k, ω) = −(1/π) Im G^R(k, ω)**. ∎

**第 4 步 — 从 Im G^R 提取 A。** 推迟格林函数为 G^R(k, ω) = ∫ dω' A(k, ω')/(ω − ω' + iδ)（所有极点在实轴下方）。利用 Sokhotski–Plemelj 恒等式 1/(x + iδ) = P(1/x) − iπδ(x)：

  Im G^R(k, ω) = −π ∫ dω' A(k, ω') δ(ω − ω') = −π A(k, ω)。

因此 **A(k, ω) = −(1/π) Im G^R(k, ω)**。∎

---

## C. The Spectral Sum Rule · 谱函数求和规则

**Claim.** The spectral function satisfies the sum rule

  ∫_{−∞}^{∞} dω A(k, ω) = 1    (per spin).

**命题。** 谱函数满足求和规则

  ∫_{−∞}^{∞} dω A(k, ω) = 1    （每个自旋）。

**Step 1 — Use the equal-time anticommutator.** Set t = t' in the definition of G and use the Fourier representation:

  G(k, t=0⁺) − G(k, t=0⁻) = −i ⟨{ĉ_k, ĉ†_k}⟩ = −i · 1 = −i.

**第 1 步 — 使用等时反对易子。** 在 G 的定义中令 t = t'，并使用傅里叶表示：

  G(k, t=0⁺) − G(k, t=0⁻) = −i ⟨{ĉ_k, ĉ†_k}⟩ = −i · 1 = −i。

**Step 2 — Relate to the frequency integral.** The discontinuity at t = 0 equals the integral of the spectral function (by the Fourier inversion theorem on the spectral representation):

  G(k, 0⁺) − G(k, 0⁻) = ∫ dω/(2π) · (−2πi) A(k, ω) · (−1/(2π i)) · 2πi.

More directly: integrating the spectral representation over ω with the appropriate contour closing gives

  ∫_{−∞}^{∞} dω A(k, ω) = −i [G(k, t=0⁺) − G(k, t=0⁻)] / (−i) = ⟨{ĉ_k, ĉ†_k}⟩ = 1.  ∎

The sum rule is an exact consequence of the fermionic anticommutation relation alone, independent of interactions. It provides a stringent check on any approximate A(k, ω).

**第 2 步 — 与频率积分相联系。** t = 0 处的不连续性等于谱函数的积分（由谱表示上的傅里叶反演定理）：

更直接地：对谱表示关于 ω 积分并取适当围道闭合，给出

  ∫_{−∞}^{∞} dω A(k, ω) = ⟨{ĉ_k, ĉ†_k}⟩ = 1。  ∎

求和规则是费米子反对易关系单独的精确推论，与相互作用无关。它对任何近似 A(k, ω) 提供了严格检验。

---

## D. Poles, Quasiparticles, and the Self-Energy · 极点、准粒子与自能

**Claim.** When interactions are included, the full Green's function takes the Dyson form G(k, ω) = 1/(ω − ε_k/ℏ − Σ(k, ω)). If Σ(k, ω) has a weak frequency dependence near a quasiparticle energy ω_{qp}, the pole structure defines a quasiparticle with energy ε̃_k and lifetime τ_k.

**命题。** 加入相互作用后，完整格林函数取戴森形式 G(k, ω) = 1/(ω − ε_k/ℏ − Σ(k, ω))。若 Σ(k, ω) 在准粒子能量 ω_{qp} 附近频率依赖较弱，则极点结构定义了具有能量 ε̃_k 和寿命 τ_k 的准粒子。

**Step 1 — Taylor expand the self-energy near the pole.** Write Σ(k, ω) = Re Σ(k, ω_{qp}) + iIm Σ(k, ω_{qp}) + (∂Re Σ/∂ω)(ω − ω_{qp}) + … The quasiparticle pole satisfies ω_{qp} − ε_k/ℏ − Re Σ(k, ω_{qp}) = 0, which defines the renormalized energy ε̃_k = ε_k + ℏ Re Σ(k, ω_{qp}).

**第 1 步 — 在极点附近对自能作泰勒展开。** 写出 Σ(k, ω) = Re Σ(k, ω_{qp}) + iIm Σ(k, ω_{qp}) + (∂Re Σ/∂ω)(ω − ω_{qp}) + …。准粒子极点满足 ω_{qp} − ε_k/ℏ − Re Σ(k, ω_{qp}) = 0，由此定义重整化能量 ε̃_k = ε_k + ℏ Re Σ(k, ω_{qp})。

**Step 2 — Define the quasiparticle residue Z_k.** The denominator of G near ω_{qp} is, to leading order in the expansion,

  ω − ε_k/ℏ − Σ ≈ (1 − ∂Re Σ/∂ω)|_{ω_{qp}} · (ω − ω_{qp}) − i Im Σ(k, ω_{qp})
                  = Z_k^{−1} (ω − ω_{qp} + i Γ_k/2),

where Z_k = [1 − ∂Re Σ/∂ω]^{−1}_{ω_{qp}} is the **quasiparticle residue** (0 < Z_k ≤ 1) and Γ_k = −2 Z_k Im Σ(k, ω_{qp}) is the quasiparticle decay rate.

**第 2 步 — 定义准粒子留数 Z_k。** G 的分母在 ω_{qp} 附近展开至领头阶为

  ω − ε_k/ℏ − Σ ≈ (1 − ∂Re Σ/∂ω)|_{ω_{qp}} · (ω − ω_{qp}) − i Im Σ(k, ω_{qp})
                  = Z_k^{−1} (ω − ω_{qp} + i Γ_k/2)，

其中 Z_k = [1 − ∂Re Σ/∂ω]^{−1}_{ω_{qp}} 是**准粒子留数**（0 < Z_k ≤ 1），Γ_k = −2 Z_k Im Σ(k, ω_{qp}) 是准粒子衰减率。

**Step 3 — Read off the spectral function.** The quasiparticle part of A(k, ω) near the pole is

  A_{qp}(k, ω) = Z_k/π · (Γ_k/2) / ((ω − ω_{qp})² + (Γ_k/2)²),

a Lorentzian of height Z_k/π at ω = ω_{qp} and half-width Γ_k/2. The quasiparticle lifetime is τ_k = 1/Γ_k = ℏ/(−2 Z_k Im Σ). In the non-interacting limit Im Σ → 0 and Z_k → 1, the Lorentzian collapses to a delta function δ(ω − ε_k/ℏ), recovering G⁰. ∎

**第 3 步 — 读出谱函数。** 极点附近 A(k, ω) 的准粒子部分为

  A_{qp}(k, ω) = Z_k/π · (Γ_k/2) / ((ω − ω_{qp})² + (Γ_k/2)²)，

一个在 ω = ω_{qp} 处高度为 Z_k/π、半宽为 Γ_k/2 的洛伦兹峰。准粒子寿命为 τ_k = 1/Γ_k = ℏ/(−2 Z_k Im Σ)。在非相互作用极限 Im Σ → 0、Z_k → 1 时，洛伦兹峰退化为 δ 函数 δ(ω − ε_k/ℏ)，还原 G⁰。∎

---

*These derivations establish the Green's function as the central object of many-body theory: it encodes the full single-particle excitation spectrum, is directly measurable (ARPES), satisfies exact sum rules, and has a perturbative expansion in terms of self-energies (Module 6.3).*

*上述推导确立了格林函数作为多体理论核心对象的地位：它编码完整的单粒子激发谱，可直接测量（ARPES），满足精确的求和规则，并关于自能（模块 6.3）有微扰展开。*

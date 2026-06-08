# Derivations — Module 3.4: Quantum Mechanics in 3D
# 推导 — 模块 3.4：三维量子力学

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.4](./module-3.4-quantum-mechanics-in-3d.md). Full step-by-step proofs of every non-trivial result quoted there. English first, then 中文.
> [模块 3.4](./module-3.4-quantum-mechanics-in-3d.md) 的配套文档：对该模块所引用每个非平凡结果的完整逐步证明。先英文，后中文。

---

## A. Separation of Variables in 3D Schrödinger Equation (Spherical Coordinates) · 三维薛定谔方程的球坐标分离变量

**Claim.** For a central potential V = V(r), the 3D time-independent Schrödinger equation (TISE) −(ℏ²/2m)∇²ψ + V(r)ψ = Eψ separates in spherical coordinates (r, θ, φ) into an angular equation and a radial equation, with the angular part solved by spherical harmonics Yₗᵐ(θ,φ).

**命题。** 对于中心势 V = V(r)，三维定态薛定谔方程 −(ℏ²/2m)∇²ψ + V(r)ψ = Eψ 在球坐标 (r, θ, φ) 中分离为角向方程与径向方程，角向部分由球谐函数 Yₗᵐ(θ,φ) 求解。

**Step 1 — Laplacian in spherical coordinates.** The Laplacian in spherical coordinates is:

**第 1 步 — 球坐标中的拉普拉斯算符。** 球坐标中的拉普拉斯算符为：

  ∇² = (1/r²) ∂/∂r (r² ∂/∂r) + (1/r² sinθ) ∂/∂θ (sinθ ∂/∂θ) + 1/(r² sin²θ) ∂²/∂φ².

The angular part is related to the orbital angular momentum operator L̂² by:

角向部分与轨道角动量算符 L̂² 的关系为：

  −ℏ² Λ² ≡ L̂²,   where Λ² = (1/sinθ) ∂/∂θ (sinθ ∂/∂θ) + 1/sin²θ ∂²/∂φ².

So: ∇² = (1/r²) ∂/∂r (r² ∂/∂r) − L̂²/(ℏ²r²).

因此：∇² = (1/r²) ∂/∂r (r² ∂/∂r) − L̂²/(ℏ²r²)。

**Step 2 — Write the TISE.** The TISE becomes:

**第 2 步 — 写出定态薛定谔方程。** 定态薛定谔方程变为：

  −(ℏ²/2m)[(1/r²) ∂/∂r (r² ∂ψ/∂r) − L̂²ψ/(ℏ²r²)] + V(r)ψ = Eψ.

Multiply through by −2m/ℏ²:

两边乘以 −2m/ℏ²：

  (1/r²) ∂/∂r (r² ∂ψ/∂r) − L̂²ψ/(ℏ²r²) + (2m/ℏ²)(E − V)ψ = 0.    … (TISE)

**Step 3 — Separate variables.** Try ψ(r,θ,φ) = R(r)·Y(θ,φ). Substitute:

**第 3 步 — 分离变量。** 尝试 ψ(r,θ,φ) = R(r)·Y(θ,φ)。代入：

  Y (1/r²) d/dr(r² R′) + R[−L̂²Y/(ℏ²r²)] + (2m/ℏ²)(E−V)RY = 0.

Divide by RY/r²:

除以 RY/r²：

  (1/R) d/dr(r² R′) + (2m/ℏ²)(E−V)r² = (1/Y) L̂²Y/ℏ².

The left side depends only on r; the right side only on angles. Both must equal a constant — call it ℓ(ℓ+1):

左边仅依赖于 r；右边仅依赖于角度。两边必须等于同一个常数——记为 ℓ(ℓ+1)：

  **Angular equation:** L̂²Y = ℏ²ℓ(ℓ+1) Y.    … (AE)

  **角向方程：** L̂²Y = ℏ²ℓ(ℓ+1) Y。    … (角)

  **Radial equation:** (1/r²) d/dr(r² dR/dr) + [2m/ℏ²(E−V) − ℓ(ℓ+1)/r²]R = 0.    … (RE)

  **径向方程：** (1/r²) d/dr(r² dR/dr) + [2m/ℏ²(E−V) − ℓ(ℓ+1)/r²]R = 0。    … (径)

**Step 4 — Further separation of the angular equation.** Set Y(θ,φ) = Θ(θ)Φ(φ). The φ-dependence in L̂² is just ∂²/∂φ², so L̂_z = −iℏ ∂/∂φ gives:

**第 4 步 — 角向方程的进一步分离。** 令 Y(θ,φ) = Θ(θ)Φ(φ)。L̂² 中的 φ 依赖仅为 ∂²/∂φ²，L̂_z = −iℏ ∂/∂φ 给出：

  d²Φ/dφ² = −m²Φ,   solution: Φ(φ) = e^{imφ}.

Single-valuedness Φ(φ + 2π) = Φ(φ) requires **m integer**. The remaining θ-equation (with L̂² including the −m²/sin²θ term from −Φ″/Φ) is the **associated Legendre equation**, whose normalizable solutions exist only for **ℓ = 0, 1, 2, …** and **−ℓ ≤ m ≤ ℓ**.

单值性条件 Φ(φ + 2π) = Φ(φ) 要求 **m 为整数**。剩余的 θ 方程（L̂² 包含来自 −Φ″/Φ 的 −m²/sin²θ 项）是**连带勒让德方程**，其可归一化的解仅在 **ℓ = 0, 1, 2, …** 且 **−ℓ ≤ m ≤ ℓ** 时存在。

The normalized solutions Yₗᵐ(θ,φ) = N · Pₗᵐ(cosθ) e^{imφ} are the **spherical harmonics**. They satisfy (AE) by construction. ∎

归一化解 Yₗᵐ(θ,φ) = N · Pₗᵐ(cosθ) e^{imφ} 是**球谐函数**。由构造它们满足（角）方程。∎

---

## B. Angular Momentum Algebra: L̂² and L̂_z Eigenvalues · 角动量代数：L̂² 与 L̂_z 的本征值

**Claim.** From the fundamental commutation relations [L̂_x, L̂_y] = iℏL̂_z (and cyclic permutations) and [L̂², L̂_i] = 0, the simultaneous eigenvalues of L̂² and L̂_z are ℏ²ℓ(ℓ+1) and mℏ respectively, with ℓ = 0, 1, 2, … and m = −ℓ, …, +ℓ.

**命题。** 由基本对易关系 [L̂_x, L̂_y] = iℏL̂_z（及其轮换），以及 [L̂², L̂_i] = 0，L̂² 与 L̂_z 的同时本征值分别为 ℏ²ℓ(ℓ+1) 和 mℏ，其中 ℓ = 0, 1, 2, …，m = −ℓ, …, +ℓ。

**Step 1 — Commutation relations.** In 3D, L̂ = r̂ × p̂, so L̂_x = ŷp̂_z − ẑp̂_y, etc. Using [x̂_i, p̂_j] = iℏδ_{ij}:

**第 1 步 — 对易关系。** 在三维中，L̂ = r̂ × p̂，故 L̂_x = ŷp̂_z − ẑp̂_y 等。利用 [x̂_i, p̂_j] = iℏδ_{ij}：

  [L̂_x, L̂_y] = [ŷp̂_z − ẑp̂_y, ẑp̂_x − x̂p̂_z]
               = ŷp̂_x[p̂_z, ẑ] + x̂p̂_y[ẑ, p̂_z]
               = ŷp̂_x(−iℏ) + x̂p̂_y(iℏ)
               = iℏ(x̂p̂_y − ŷp̂_x) = iℏL̂_z.

Similarly: [L̂_y, L̂_z] = iℏL̂_x, [L̂_z, L̂_x] = iℏL̂_y.

类似地：[L̂_y, L̂_z] = iℏL̂_x，[L̂_z, L̂_x] = iℏL̂_y。

From these: **[L̂², L̂_z] = 0** (and similarly [L̂², L̂_x] = [L̂², L̂_y] = 0), since:

由此：**[L̂², L̂_z] = 0**（同理 [L̂², L̂_x] = [L̂², L̂_y] = 0），因为：

  [L̂², L̂_z] = [L̂_x²+L̂_y²+L̂_z², L̂_z] = L̂_x[L̂_x,L̂_z]+[L̂_x,L̂_z]L̂_x + L̂_y[L̂_y,L̂_z]+[L̂_y,L̂_z]L̂_y
             = L̂_x(−iℏL̂_y)+(−iℏL̂_y)L̂_x + L̂_y(iℏL̂_x)+(iℏL̂_x)L̂_y = 0.

Therefore L̂² and L̂_z have simultaneous eigenstates |ℓ,m⟩.

因此 L̂² 和 L̂_z 有同时本征态 |ℓ,m⟩。

**Step 2 — Define ladder operators.** Let L̂_± = L̂_x ± iL̂_y. Key commutators:

**第 2 步 — 定义升降算符。** 令 L̂_± = L̂_x ± iL̂_y。关键对易子：

  [L̂_z, L̂_±] = [L̂_z, L̂_x] ± i[L̂_z, L̂_y] = iℏL̂_y ± i(−iℏL̂_x) = ±ℏL̂_±.

  [L̂², L̂_±] = 0.

**Step 3 — Ladder action on eigenstates.** Let L̂²|ℓ,m⟩ = λ|ℓ,m⟩ and L̂_z|ℓ,m⟩ = mℏ|ℓ,m⟩. From [L̂_z, L̂_+] = ℏL̂_+:

**第 3 步 — 升降算符对本征态的作用。** 设 L̂²|ℓ,m⟩ = λ|ℓ,m⟩，L̂_z|ℓ,m⟩ = mℏ|ℓ,m⟩。由 [L̂_z, L̂_+] = ℏL̂_+：

  L̂_z(L̂_+|ℓ,m⟩) = (L̂_+L̂_z + ℏL̂_+)|ℓ,m⟩ = (mℏ + ℏ)(L̂_+|ℓ,m⟩) = (m+1)ℏ (L̂_+|ℓ,m⟩).

So L̂_+|ℓ,m⟩ is an eigenstate of L̂_z with eigenvalue (m+1)ℏ. Similarly L̂_−|ℓ,m⟩ has eigenvalue (m−1)ℏ. Also [L̂², L̂_±] = 0 confirms that L̂_±|ℓ,m⟩ still has L̂² eigenvalue λ.

故 L̂_+|ℓ,m⟩ 是 L̂_z 的本征态，本征值为 (m+1)ℏ。类似地 L̂_−|ℓ,m⟩ 的本征值为 (m−1)ℏ。还有 [L̂², L̂_±] = 0 确认 L̂_±|ℓ,m⟩ 仍有 L̂² 本征值 λ。

**Step 4 — Bound on m.** The operator L̂² − L̂_z² = L̂_x² + L̂_y² is a sum of squares of Hermitian operators:

**第 4 步 — m 的上下界。** 算符 L̂² − L̂_z² = L̂_x² + L̂_y² 是厄米算符的平方和：

  ⟨ℓ,m|L̂²−L̂_z²|ℓ,m⟩ = ⟨ℓ,m|L̂_x²+L̂_y²|ℓ,m⟩ ≥ 0.

  ⟹  λ − m²ℏ² ≥ 0  ⟹  |m| ≤ √(λ)/ℏ.

So m is bounded. Let m_max be the maximum value. Since L̂_+|ℓ,m_max⟩ must be zero (no higher m exists):

故 m 有界。设 m_max 为最大值。由于 L̂_+|ℓ,m_max⟩ 必须为零（不存在更高的 m）：

  L̂_−L̂_+|ℓ,m_max⟩ = 0.

Expand L̂_−L̂_+ = L̂² − L̂_z² − ℏL̂_z (using L̂_±L̂_∓ = L̂² − L̂_z² ∓ ℏL̂_z):

展开 L̂_−L̂_+ = L̂² − L̂_z² − ℏL̂_z（利用 L̂_±L̂_∓ = L̂² − L̂_z² ∓ ℏL̂_z）：

  (L̂² − L̂_z² − ℏL̂_z)|ℓ,m_max⟩ = (λ − m_max²ℏ² − m_max ℏ²)|ℓ,m_max⟩ = 0.

  λ = m_max(m_max + 1)ℏ².

Set m_max = ℓ: **λ = ℏ²ℓ(ℓ+1)**. Similarly, with L̂_−|ℓ,m_min⟩ = 0: λ = m_min(m_min − 1)ℏ², giving m_min = −ℓ. The ladder from m_min to m_max takes integer steps, so **ℓ must be a non-negative integer or half-integer** (orbital: integer; spin: half-integer). For orbital angular momentum, single-valuedness of Yₗᵐ fixes **ℓ = 0, 1, 2, …** and **m = −ℓ, −ℓ+1, …, ℓ**. ∎

令 m_max = ℓ：**λ = ℏ²ℓ(ℓ+1)**。类似地，由 L̂_−|ℓ,m_min⟩ = 0 得 λ = m_min(m_min − 1)ℏ²，给出 m_min = −ℓ。从 m_min 到 m_max 的阶梯以整数步进，故 **ℓ 必须是非负整数或半整数**（轨道：整数；自旋：半整数）。对于轨道角动量，Yₗᵐ 的单值性限制 **ℓ = 0, 1, 2, …** 且 **m = −ℓ, −ℓ+1, …, ℓ**。∎

---

## C. Hydrogen Atom Radial Solution and Eₙ = −13.6 eV / n² · 氢原子径向解与 Eₙ = −13.6 eV / n²

**Claim.** For the hydrogen atom V(r) = −k_e e²/r, the radial Schrödinger equation (RE from Section A) with E < 0 has normalizable solutions only for energies Eₙ = −m k_e² e⁴/(2ℏ²n²) = −13.6 eV/n², n = 1, 2, 3, …, with n ≥ ℓ+1.

**命题。** 对于氢原子 V(r) = −k_e e²/r，径向薛定谔方程（第 A 节的径向方程）在 E < 0 时有可归一化解仅当 Eₙ = −m k_e² e⁴/(2ℏ²n²) = −13.6 eV/n²，n = 1, 2, 3, …，n ≥ ℓ+1。

**Step 1 — Radial equation for hydrogen.** Substitute V = −k_e e²/r into (RE) and let u(r) = r R(r) to remove the first-derivative term:

**第 1 步 — 氢原子的径向方程。** 将 V = −k_e e²/r 代入（径向方程），令 u(r) = r R(r) 以消去一阶导数项：

  d²u/dr² + [2m/ℏ²(E + k_e e²/r) − ℓ(ℓ+1)/r²]u = 0.

**Step 2 — Asymptotic analysis.** For E < 0, let κ = √(−2mE)/ℏ > 0. As r → ∞ the equation approaches d²u/dr² ≈ κ²u, giving u ~ e^{±κr}. Normalizability requires u ~ e^{−κr}.

**第 2 步 — 渐近分析。** 对于 E < 0，令 κ = √(−2mE)/ℏ > 0。当 r → ∞ 时方程趋近于 d²u/dr² ≈ κ²u，给出 u ~ e^{±κr}。可归一化要求 u ~ e^{−κr}。

As r → 0 with ℓ ≥ 1: the ℓ(ℓ+1)/r² term dominates, giving u ~ r^{ℓ+1} or r^{−ℓ}. Normalizability requires u ~ r^{ℓ+1}.

当 r → 0 且 ℓ ≥ 1 时：ℓ(ℓ+1)/r² 项主导，给出 u ~ r^{ℓ+1} 或 r^{−ℓ}。可归一化要求 u ~ r^{ℓ+1}。

**Step 3 — Power series / Laguerre polynomial solution.** Factor out the asymptotic behavior: u(r) = r^{ℓ+1} e^{−κr} v(r). Substituting into the equation gives a differential equation for v(r) that, in terms of the variable ρ = 2κr, becomes the **associated Laguerre equation**:

**第 3 步 — 幂级数/拉盖尔多项式解。** 提取渐近行为：u(r) = r^{ℓ+1} e^{−κr} v(r)。代入方程，用变量 ρ = 2κr，得到关于 v(r) 的**连带拉盖尔方程**：

  ρ v″ + (2ℓ+2−ρ) v′ + [n−(ℓ+1)] v = 0,

where n is defined by n = k_e e² m/(ℏ²κ) (this is the parameter). The series solution for v terminates (giving a polynomial) if and only if n − (ℓ+1) = n_r is a non-negative integer (n_r = 0, 1, 2, … is the radial quantum number). When the series does not terminate, v grows like e^ρ, making u non-normalizable.

其中 n 由 n = k_e e² m/(ℏ²κ) 定义（这是参数）。v 的级数解终止（给出多项式）当且仅当 n − (ℓ+1) = n_r 为非负整数（n_r = 0, 1, 2, … 是径向量子数）。当级数不终止时，v 的增长如 e^ρ，使 u 不可归一化。

**Step 4 — Energy quantization.** From n = k_e e²m/(ℏ²κ) and κ = √(−2mE)/ℏ:

**第 4 步 — 能量量子化。** 由 n = k_e e²m/(ℏ²κ) 和 κ = √(−2mE)/ℏ：

  κ = mk_e e²/(nℏ²),

  E = −ℏ²κ²/(2m) = −ℏ²/(2m) · m²k_e²e⁴/(n²ℏ⁴) = **−mk_e²e⁴/(2n²ℏ²)**.

Numerically: **Eₙ = −13.6 eV / n²**, n = 1, 2, 3, … The constraint n ≥ ℓ+1 means: for n = 1, only ℓ = 0; for n = 2, ℓ = 0 or 1; etc. This gives the degeneracy g(n) = Σ_{ℓ=0}^{n-1}(2ℓ+1) = n². ∎

数值上：**Eₙ = −13.6 eV / n²**，n = 1, 2, 3, …。约束 n ≥ ℓ+1 意味着：n = 1 时只有 ℓ = 0；n = 2 时 ℓ = 0 或 1；等等。这给出简并度 g(n) = Σ_{ℓ=0}^{n-1}(2ℓ+1) = n²。∎

---

## D. Spin-½: Pauli Matrices and S_z Eigenvalues · 自旋-½：泡利矩阵与 S_z 本征值

**Claim.** For a spin-½ particle, the spin operators Ŝ_i = (ℏ/2)σ_i satisfy the angular-momentum algebra [Ŝ_x, Ŝ_y] = iℏŜ_z (etc.), and S_z has eigenvalues ±ℏ/2 with eigenstates |↑⟩ and |↓⟩.

**命题。** 对自旋-½ 粒子，自旋算符 Ŝ_i = (ℏ/2)σ_i 满足角动量代数 [Ŝ_x, Ŝ_y] = iℏŜ_z（等），S_z 的本征值为 ±ℏ/2，本征态为 |↑⟩ 和 |↓⟩。

**Step 1 — General spin-½ state space.** By the angular-momentum algebra of Section B (which applies equally to half-integer spin), for s = ½ we have S² eigenvalue ℏ²·½·(½+1) = 3ℏ²/4, and m_s = ±½. The state space is 2-dimensional; choose basis {|↑⟩, |↓⟩} = {|s=½,m=+½⟩, |s=½,m=−½⟩}.

**第 1 步 — 一般自旋-½ 态空间。** 由第 B 节的角动量代数（同样适用于半整数自旋），对 s = ½ 有 S² 本征值 ℏ²·½·(½+1) = 3ℏ²/4，m_s = ±½。态空间是二维的；选取基 {|↑⟩, |↓⟩} = {|s=½,m=+½⟩, |s=½,m=−½⟩}。

**Step 2 — Matrix representations.** In this basis, the matrix elements of S_z are diagonal (since these are eigenstates):

**第 2 步 — 矩阵表示。** 在此基中，S_z 的矩阵元是对角的（因为这些是本征态）：

  S_z = ℏ/2 · (|↑⟩⟨↑| − |↓⟩⟨↓|) = (ℏ/2) [[1, 0], [0, −1]].

For S_±, from Section B: Ŝ_+|↓⟩ = ℏ|↑⟩, Ŝ_+|↑⟩ = 0; Ŝ_−|↑⟩ = ℏ|↓⟩, Ŝ_−|↓⟩ = 0. (Norm factor: √(s(s+1)−m(m±1)) = √(3/4−(−1/2)(1/2)) = 1 for ℓ=½ states.) Therefore:

对于 S_±，由第 B 节：Ŝ_+|↓⟩ = ℏ|↑⟩，Ŝ_+|↑⟩ = 0；Ŝ_−|↑⟩ = ℏ|↓⟩，Ŝ_−|↓⟩ = 0。因此：

  S_x = (S_+ + S_−)/2 = (ℏ/2)[[0,1],[1,0]],
  S_y = (S_+ − S_−)/(2i) = (ℏ/2)[[0,−i],[i,0]].

**Step 3 — Pauli matrices.** Define σ_i by Ŝ_i = (ℏ/2)σ_i:

**第 3 步 — 泡利矩阵。** 由 Ŝ_i = (ℏ/2)σ_i 定义 σ_i：

  σ_x = [[0,1],[1,0]],  σ_y = [[0,−i],[i,0]],  σ_z = [[1,0],[0,−1]].

**Step 4 — Verify the algebra.** [Ŝ_x, Ŝ_y] = (ℏ²/4)[σ_x, σ_y]:

**第 4 步 — 验证代数关系。** [Ŝ_x, Ŝ_y] = (ℏ²/4)[σ_x, σ_y]：

  [σ_x, σ_y] = σ_xσ_y − σ_yσ_x
              = [[0,1],[1,0]][[0,−i],[i,0]] − [[0,−i],[i,0]][[0,1],[1,0]]
              = [[i,0],[0,−i]] − [[−i,0],[0,i]]
              = [[2i,0],[0,−2i]] = 2i σ_z.

Therefore [Ŝ_x, Ŝ_y] = (ℏ²/4)·2iσ_z = iℏ·(ℏ/2)σ_z = **iℏŜ_z**. ✓

因此 [Ŝ_x, Ŝ_y] = (ℏ²/4)·2iσ_z = iℏ·(ℏ/2)σ_z = **iℏŜ_z**。✓

**Step 5 — S_z eigenvalues.** S_z = (ℏ/2)σ_z has eigenvalues (ℏ/2)·(±1) = **±ℏ/2**, with eigenvectors [1,0]ᵀ = |↑⟩ (eigenvalue +ℏ/2, "spin up") and [0,1]ᵀ = |↓⟩ (eigenvalue −ℏ/2, "spin down"). ∎

**第 5 步 — S_z 本征值。** S_z = (ℏ/2)σ_z 的本征值为 (ℏ/2)·(±1) = **±ℏ/2**，本征向量分别为 [1,0]ᵀ = |↑⟩（本征值 +ℏ/2，"自旋向上"）和 [0,1]ᵀ = |↓⟩（本征值 −ℏ/2，"自旋向下"）。∎

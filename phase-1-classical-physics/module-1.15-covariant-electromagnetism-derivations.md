# Derivations — Module 1.15: Covariant Electromagnetism
# 推导 — 模块 1.15：协变电磁学

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.15](./module-1.15-covariant-electromagnetism.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.15](./module-1.15-covariant-electromagnetism.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Building the Field Tensor F_{μν} = ∂_μ A_ν − ∂_ν A_μ · 构造场张量

**Claim.** The antisymmetric rank-2 tensor F_{μν} = ∂_μ A_ν − ∂_ν A_μ, formed from the four-potential A^μ = (φ/c, **A**), encodes the electric field E and magnetic field B in its components, and is automatically gauge-invariant.

**命题。** 由四矢量势 A^μ = (φ/c, **A**) 构造的反对称 2 阶张量 F_{μν} = ∂_μ A_ν − ∂_ν A_μ，在其分量中编码了电场 E 和磁场 B，并自动具有规范不变性。

**Step 1 — Conventions and index lowering.** Use the metric signature η_{μν} = diag(+1, −1, −1, −1) and the coordinate four-vector x^μ = (ct, x, y, z). The covariant derivative operator is ∂_μ = ∂/∂x^μ = (∂_t/c, ∂_x, ∂_y, ∂_z). The four-potential with lowered index is A_μ = η_{μν} A^ν = (φ/c, −A_x, −A_y, −A_z).

**第 1 步 — 约定与指标降低。** 采用度规号差 η_{μν} = diag(+1, −1, −1, −1)，坐标四矢量 x^μ = (ct, x, y, z)。协变导数算符为 ∂_μ = ∂/∂x^μ = (∂_t/c, ∂_x, ∂_y, ∂_z)。降低指标后的四矢量势为 A_μ = η_{μν} A^ν = (φ/c, −A_x, −A_y, −A_z)。

**Step 2 — Compute F_{0i} components.** For μ = 0, ν = i (spatial):

**第 2 步 — 计算 F_{0i} 分量。** 取 μ = 0，ν = i（空间）：

  F_{0i} = ∂_0 A_i − ∂_i A_0
          = (1/c)(∂A_i/∂t) − ∂_i (φ/c)     [but A_i = −A^i, so ∂_0 A_i = −(1/c)∂A^i/∂t]
          = −(1/c)(∂A^i/∂t) − (1/c) ∂φ/∂x^i.

Recall **E** = −∇φ − ∂**A**/∂t, so E^i = −∂φ/∂x^i − ∂A^i/∂t. Therefore:

回忆 **E** = −∇φ − ∂**A**/∂t，故 E^i = −∂φ/∂x^i − ∂A^i/∂t。因此：

  F_{0i} = (1/c)(−∂A^i/∂t − ∂φ/∂x^i) = E^i/c.

So **F_{0i} = E_i/c** (with E_i = E^i for Cartesian coordinates).

故 **F_{0i} = E_i/c**（在笛卡尔坐标中 E_i = E^i）。

**Step 3 — Compute F_{ij} components.** For μ = i, ν = j (both spatial):

**第 3 步 — 计算 F_{ij} 分量。** 取 μ = i，ν = j（均为空间）：

  F_{ij} = ∂_i A_j − ∂_j A_i = −∂_i A^j + ∂_j A^i = ∂_j A^i − ∂_i A^j.

The magnetic field is **B** = ∇ × **A**, i.e. B^k = ε^{ijk} ∂_i A^j (with ε^{ijk} the Levi-Civita symbol). Explicitly:

磁场为 **B** = ∇ × **A**，即 B^k = ε^{ijk} ∂_i A^j（ε^{ijk} 为列维-奇维塔符号）。明确地：

  F_{12} = ∂_2 A^1 − ∂_1 A^2 = −(∂_1 A^2 − ∂_2 A^1) = −B^3 = −B_z,
  F_{13} = ∂_3 A^1 − ∂_1 A^3 = −(∂_1 A^3 − ∂_3 A^1) = +B^2 = +B_y,
  F_{23} = ∂_3 A^2 − ∂_2 A^3 = −(∂_2 A^3 − ∂_3 A^2) = −B^1 = −B_x.

In general **F_{ij} = −ε_{ijk} B^k**. The explicit matrix of F_{μν} is:

一般地 **F_{ij} = −ε_{ijk} B^k**。F_{μν} 的显式矩阵为：

        ⎡  0      E_x/c   E_y/c   E_z/c ⎤
  F_{μν} = ⎢ −E_x/c   0     −B_z    B_y  ⎥
        ⎢ −E_y/c  B_z      0     −B_x  ⎥
        ⎣ −E_z/c  −B_y    B_x     0   ⎦

**Step 4 — Gauge invariance.** Under A_μ → A_μ + ∂_μ χ for any scalar field χ:

**第 4 步 — 规范不变性。** 在任意标量场 χ 的规范变换 A_μ → A_μ + ∂_μ χ 下：

  F_{μν} → ∂_μ(A_ν + ∂_ν χ) − ∂_ν(A_μ + ∂_μ χ)
          = F_{μν} + ∂_μ ∂_ν χ − ∂_ν ∂_μ χ
          = F_{μν} + 0   (partial derivatives commute).

Hence **F_{μν} is gauge-invariant** — the physically measurable fields E and B do not depend on the choice of gauge. ∎

故 **F_{μν} 是规范不变的**——可物理测量的场 E 和 B 不依赖于规范的选取。∎

---

## B. Transformation of E and B Under a Lorentz Boost · 洛伦兹变换下 E 和 B 的变换

**Claim.** Under a Lorentz boost with velocity v along the x-axis, the fields transform as: E_x′ = E_x, E_y′ = γ(E_y − vB_z), E_z′ = γ(E_z + vB_y), B_x′ = B_x, B_y′ = γ(B_y + vE_z/c²), B_z′ = γ(B_z − vE_y/c²).

**命题。** 在沿 x 轴以速度 v 的洛伦兹变换下，场的变换为：E_x′ = E_x，E_y′ = γ(E_y − vB_z)，E_z′ = γ(E_z + vB_y)，B_x′ = B_x，B_y′ = γ(B_y + vE_z/c²)，B_z′ = γ(B_z − vE_y/c²)。

**Step 1 — The Lorentz boost matrix.** A boost with velocity v along x (with β = v/c and γ = 1/√(1 − β²)) is

**第 1 步 — 洛伦兹变换矩阵。** 沿 x 轴以速度 v 的变换（β = v/c，γ = 1/√(1 − β²)）为

  Λ^μ_ν = ⎡ γ    −γβ   0  0 ⎤
           ⎢ −γβ   γ    0  0 ⎥
           ⎢  0    0    1  0 ⎥
           ⎣  0    0    0  1 ⎦

**Step 2 — Tensor transformation law.** A rank-2 covariant tensor transforms as

**第 2 步 — 张量变换法则。** 2 阶协变张量的变换法则为

  F′_{μν} = Λ^α_μ Λ^β_ν F_{αβ}.

We compute each independent component of F′_{μν}.

我们逐一计算 F′_{μν} 的各独立分量。

**Step 3 — Transform all six field components.**

**第 3 步 — 变换全部六个场分量。**

We work throughout with the **contravariant** tensor F^{μν}, whose components are fixed by Section A: since F_{0i} = E_i/c, raising both indices gives F^{0i} = η^{00}η^{ii}F_{0i} = −E_i/c, while F^{ij} = F_{ij} = −ε_{ijk}B^k, i.e. F^{12} = −B_z, F^{13} = +B_y, F^{23} = −B_x. The transformed fields are read off the **same way** on both sides: F′^{0i} = −E_i′/c, F′^{12} = −B_z′, F′^{13} = +B_y′, F′^{23} = −B_x′. Taking the primed frame S′ to move at velocity +v along x, the boost is Λ^0_0 = γ, Λ^0_1 = Λ^1_0 = −γβ, Λ^1_1 = γ, Λ^2_2 = Λ^3_3 = 1, and a rank-2 contravariant tensor transforms as F′^{μν} = Λ^μ_α Λ^ν_β F^{αβ}.

全程使用**逆变**张量 F^{μν}，其分量由 A 节固定：因 F_{0i} = E_i/c，升两个指标得 F^{0i} = −E_i/c，而 F^{ij} = F_{ij} = −ε_{ijk}B^k，即 F^{12} = −B_z、F^{13} = +B_y、F^{23} = −B_x。两边以**相同方式**读出变换后的场：F′^{0i} = −E_i′/c、F′^{12} = −B_z′、F′^{13} = +B_y′、F′^{23} = −B_x′。取主系 S′ 沿 x 以速度 +v 运动，变换矩阵为 Λ^0_0 = γ、Λ^0_1 = Λ^1_0 = −γβ、Λ^1_1 = γ、Λ^2_2 = Λ^3_3 = 1，2 阶逆变张量按 F′^{μν} = Λ^μ_α Λ^ν_β F^{αβ} 变换。

**Parallel components — E_x and B_x unchanged.** Only the indices 0,1 mix:

**平行分量——E_x 与 B_x 不变。** 只有指标 0,1 混合：

  F′^{01} = Λ^0_0 Λ^1_1 F^{01} + Λ^0_1 Λ^1_0 F^{10} = γ²F^{01} + γ²β²F^{10} = γ²(1 − β²)F^{01} = F^{01}  ⟹  **E_x′ = E_x**,
  F′^{23} = Λ^2_2 Λ^3_3 F^{23} = F^{23}  ⟹  **B_x′ = B_x**.  ✓

**E_y′ (from F′^{02}).** Since Λ^2_2 = 1, only α ∈ {0,1} contributes:

**E_y′（由 F′^{02}）。** 因 Λ^2_2 = 1，只有 α ∈ {0,1} 贡献：

  F′^{02} = Λ^0_0 F^{02} + Λ^0_1 F^{12} = γ(−E_y/c) + (−γβ)(−B_z) = −γE_y/c + γβB_z.

Reading F′^{02} = −E_y′/c gives −E_y′/c = −γE_y/c + γβB_z, hence **E_y′ = γ(E_y − vB_z)**. ✓

由 F′^{02} = −E_y′/c 得 **E_y′ = γ(E_y − vB_z)**。✓

**E_z′ (from F′^{03}).**

**E_z′（由 F′^{03}）。**

  F′^{03} = Λ^0_0 F^{03} + Λ^0_1 F^{13} = γ(−E_z/c) + (−γβ)(+B_y) = −γE_z/c − γβB_y.

With F′^{03} = −E_z′/c: **E_z′ = γ(E_z + vB_y)**. ✓

由 F′^{03} = −E_z′/c：**E_z′ = γ(E_z + vB_y)**。✓

**B_z′ (from F′^{12}).** Now the first index 1 mixes with 0:

**B_z′（由 F′^{12}）。** 此时第一个指标 1 与 0 混合：

  F′^{12} = Λ^1_0 F^{02} + Λ^1_1 F^{12} = (−γβ)(−E_y/c) + γ(−B_z) = γβE_y/c − γB_z.

Reading F′^{12} = −B_z′ and using β/c = v/c²: **B_z′ = γ(B_z − vE_y/c²)**. ✓

由 F′^{12} = −B_z′ 并用 β/c = v/c²：**B_z′ = γ(B_z − vE_y/c²)**。✓

**B_y′ (from F′^{13}).**

**B_y′（由 F′^{13}）。**

  F′^{13} = Λ^1_0 F^{03} + Λ^1_1 F^{13} = (−γβ)(−E_z/c) + γ(+B_y) = γβE_z/c + γB_y.

Reading F′^{13} = +B_y′: **B_y′ = γ(B_y + vE_z/c²)**. ✓

由 F′^{13} = +B_y′：**B_y′ = γ(B_y + vE_z/c²)**。✓

All six components reproduce the Claim with no convention ambiguity — the only requirement is to use F^{0i} = −E_i/c (Section A) consistently for both F and F′.

六个分量全部重现命题，且无约定歧义——唯一要求是在 F 与 F′ 两侧一致地使用 F^{0i} = −E_i/c（A 节）。

**Summary (adopting the convention that the primed frame moves at +v along x in S):**

**汇总（S′ 以 +v 沿 x 相对 S 运动；与本节命题及标准 Griffiths/Jackson 结果一致）：**

  E_x′ = E_x                        (parallel, unchanged)
  E_y′ = γ(E_y − vB_z)
  E_z′ = γ(E_z + vB_y)
  B_x′ = B_x                        (parallel, unchanged)
  B_y′ = γ(B_y + vE_z/c²)
  B_z′ = γ(B_z − vE_y/c²)

**Physical interpretation.** A purely electric Coulomb field in S (B = 0 there) appears in S′ as having both electric and magnetic components — **magnetism is the relativistic manifestation of electricity** when charges are observed in relative motion.

**物理诠释。** 在 S 系中纯粹的库仑电场（B = 0），在 S′ 系中同时具有电场和磁场分量——**磁性是电荷相对运动时电性的相对论表现**。∎

---

## C. The Inhomogeneous Maxwell Equations from ∂_μ F^{μν} = μ₀ J^ν · 由协变方程还原麦克斯韦方程

**Claim.** The single covariant equation ∂_μ F^{μν} = μ₀ J^ν, for ν = 0 and ν = 1, 2, 3 respectively, reproduces Gauss's law and the Ampère–Maxwell law.

**命题。** 单一协变方程 ∂_μ F^{μν} = μ₀ J^ν 对 ν = 0 和 ν = 1, 2, 3 分别重现高斯定律和安培–麦克斯韦定律。

**Step 1 — Identify the four-current.** The four-current is J^ν = (cρ, J_x, J_y, J_z), where ρ is the charge density and **J** is the three-current density.

**第 1 步 — 识别四电流。** 四电流为 J^ν = (cρ, J_x, J_y, J_z)，其中 ρ 为电荷密度，**J** 为三维电流密度。

**Step 2 — Setup: the explicit contravariant components.** From Section A the lowered tensor has F_{0i} = E_i/c and F_{ij} = −ε_{ijk}B^k. Raising both indices with η = diag(+,−,−,−) gives F^{0i} = η^{00}η^{ii}F_{0i} = −E_i/c (so F^{i0} = +E_i/c) and F^{ij} = F_{ij} = −ε_{ijk}B^k. The four-current is J^μ = (cρ, J_x, J_y, J_z), and ∂_μ = ∂/∂x^μ = ((1/c)∂_t, ∂_x, ∂_y, ∂_z). The key sign — the one that makes Gauss's law come out with the correct +ρ/ε₀ — is **F^{i0} = +E_i/c**, which follows directly from §A and must be used consistently.

**第 2 步 — 准备：显式逆变分量。** 由 A 节，降标张量有 F_{0i} = E_i/c 与 F_{ij} = −ε_{ijk}B^k。用 η = diag(+,−,−,−) 升两个指标得 F^{0i} = −E_i/c（故 F^{i0} = +E_i/c）与 F^{ij} = F_{ij} = −ε_{ijk}B^k。四电流为 J^μ = (cρ, J_x, J_y, J_z)，∂_μ = ((1/c)∂_t, ∂_x, ∂_y, ∂_z)。使高斯定律给出正确 +ρ/ε₀ 的关键符号是 **F^{i0} = +E_i/c**，它直接来自 §A，必须一致使用。

Take F^{μν} with the components:

取 F^{μν} 的分量：

  F^{μν} = ⎡  0    −E_x/c  −E_y/c  −E_z/c ⎤
            ⎢ E_x/c    0     −B_z     B_y  ⎥
            ⎢ E_y/c   B_z      0     −B_x  ⎥
            ⎣ E_z/c  −B_y    B_x      0   ⎦

and J^μ = (cρ, J_x, J_y, J_z), with ∂_μ = (1/c ∂_t, ∂_x, ∂_y, ∂_z).

For ν = 0:

  ∂_μ F^{μ0} = (1/c)∂_t(0) + ∂_x(E_x/c) + ∂_y(E_y/c) + ∂_z(E_z/c)
             = (1/c)∇·**E** = μ₀(cρ).

Therefore **∇·E = μ₀c²ρ = ρ/ε₀**. ✓ (Here F^{10} = +E_x/c with this sign convention — rows are μ = 0,1,2,3 and columns are ν = 0,1,2,3.)

因此 **∇·E = ρ/ε₀**。✓

For ν = 1:

  ∂_μ F^{μ1} = (1/c)∂_t(−E_x/c) + ∂_x(0) + ∂_y(B_z) + ∂_z(−B_y)
             = −(1/c²)∂E_x/∂t + (∂B_z/∂y − ∂B_y/∂z)
             = −(1/c²)∂E_x/∂t + (∇×**B**)_x = μ₀ J_x.

So **(∇×B)_x = μ₀ J_x + μ₀ε₀ ∂E_x/∂t** — the x-component of the **Ampère–Maxwell law** ∇×**B** = μ₀**J** + μ₀ε₀ ∂**E**/∂t. ✓

故 **(∇×B)_x = μ₀ J_x + μ₀ε₀ ∂E_x/∂t**——安培–麦克斯韦定律的 x 分量。✓

Similarly for ν = 2 and ν = 3, one recovers the y and z components. The two homogeneous Maxwell equations (∇·**B** = 0 and Faraday's law) follow automatically from the definition F^{μν} = ∂^μ A^ν − ∂^ν A^μ, as shown by the Bianchi identity ∂_[λ F_{μν}] = 0. ∎

类似地，ν = 2 和 ν = 3 给出 y 和 z 分量。两个齐次麦克斯韦方程（∇·**B** = 0 和法拉第定律）由定义 F^{μν} = ∂^μ A^ν − ∂^ν A^μ 自动给出，通过比安基恒等式 ∂_{[λ} F_{μν]} = 0 可见。∎

---

## D. The Two Lorentz Invariants F_{μν} F^{μν} and F_{μν} F̃^{μν} · 两个洛伦兹不变量

**Claim.** The only independent algebraic Lorentz scalars built from F^{μν} are:
(i) F_{μν} F^{μν} = 2(B² − E²/c²),
(ii) F_{μν} F̃^{μν} = −4E·B/c  (where F̃^{μν} = ½ ε^{μνρσ} F_{ρσ} is the dual tensor).

**命题。** 由 F^{μν} 构造的仅有的独立代数洛伦兹标量为：(i) F_{μν} F^{μν} = 2(B² − E²/c²)；(ii) F_{μν} F̃^{μν} = −4**E**·**B**/c（其中 F̃^{μν} = ½ ε^{μνρσ} F_{ρσ} 为对偶张量）。

**Step 1 — Compute F_{μν} F^{μν}.** The contraction sums over all μ, ν. Using the antisymmetry F_{μν} = −F_{νμ} and F^{μν} = −F^{νμ}, there are two contributions for each pair (μ,ν) with μ < ν:

**第 1 步 — 计算 F_{μν} F^{μν}。** 缩并对所有 μ, ν 求和。利用反对称性 F_{μν} = −F_{νμ}，每对 μ < ν 贡献两次：

  F_{μν} F^{μν} = 2(F_{01}F^{01} + F_{02}F^{02} + F_{03}F^{03} + F_{12}F^{12} + F_{13}F^{13} + F_{23}F^{23}).

From Section A the lowered components are F_{0i} = E_i/c and F_{ij} = −ε_{ijk}B^k. Raise indices with η = diag(+,−,−,−): a time–space index pair flips sign, F^{0i} = η^{00}η^{ii}F_{0i} = (+1)(−1)(E_i/c) = −E_i/c, while a space–space pair is unchanged, F^{ij} = η^{ii}η^{jj}F_{ij} = (−1)(−1)F_{ij} = F_{ij}. Hence each time–space product is F_{0i}F^{0i} = (E_i/c)(−E_i/c) = −E_i²/c², and each space–space product is F_{ij}F^{ij} = (F_{ij})² ≥ 0 with Σ_{i<j}(F_{ij})² = B² (since F_{12}=−B_z, F_{13}=+B_y, F_{23}=−B_x). Therefore:

由 A 节，降标分量为 F_{0i} = E_i/c 与 F_{ij} = −ε_{ijk}B^k。用 η = diag(+,−,−,−) 升指标：时间–空间对变号 F^{0i} = −E_i/c，空间–空间对不变 F^{ij} = F_{ij}。故每个时间–空间乘积为 F_{0i}F^{0i} = −E_i²/c²，每个空间–空间乘积为 F_{ij}F^{ij} = (F_{ij})²，且 Σ_{i<j}(F_{ij})² = B²。因此：

  F_{μν} F^{μν} = 2[−E_x²/c² − E_y²/c² − E_z²/c² + B_z² + B_y² + B_x²]
               = 2[B² − E²/c²].

So **F_{μν} F^{μν} = 2(B² − E²/c²)**. ✓

故 **F_{μν} F^{μν} = 2(B² − E²/c²)**。✓

**Step 2 — The dual tensor F̃^{μν}.** The dual is defined as F̃^{μν} = ½ ε^{μνρσ} F_{ρσ}, where ε^{0123} = +1 (or −1 depending on convention; we use ε^{0123} = +1 with the (+,−,−,−) metric giving ε^{0123}/√{−g} = +1). The non-zero components are found from the cyclic properties of ε^{μνρσ}:

**第 2 步 — 对偶张量 F̃^{μν}。** 对偶张量定义为 F̃^{μν} = ½ ε^{μνρσ} F_{ρσ}，其中 ε^{0123} = +1。非零分量由 ε^{μνρσ} 的循环性质给出：

  F̃^{01} = ½(ε^{0123}F_{23} + ε^{0132}F_{32}) = ½(F_{23} − F_{32}) = F_{23} = −B_x,  and cyclically F̃^{0i} = −B_i;
  F̃^{12} = ½(ε^{1203}F_{03} + ε^{1230}F_{30}) = F_{03} = E_z/c,  and cyclically F̃^{13} = −E_y/c, F̃^{23} = E_x/c.

In matrix form:

写成矩阵形式：

  F̃^{μν} = ⎡  0    −B_x   −B_y   −B_z ⎤
             ⎢  B_x    0    E_z/c −E_y/c⎥
             ⎢  B_y −E_z/c   0    E_x/c⎥
             ⎣  B_z  E_y/c −E_x/c   0  ⎦

In other words, F̃^{μν} is obtained from F^{μν} by the replacements **E/c → B** and **B → −E/c** (an electromagnetic duality rotation by π/2).

即 F̃^{μν} 由 F^{μν} 经替换 **E/c → B** 和 **B → −E/c** 得到（电磁对偶旋转 π/2）。

**Step 3 — Compute F_{μν} F̃^{μν}.** Summing each unordered pair twice, with the lowered components F_{0i} = E_i/c, F_{12} = −B_z, F_{13} = +B_y, F_{23} = −B_x (Section A) and F̃^{μν} from Step 2:

**第 3 步 — 计算 F_{μν} F̃^{μν}。** 每个无序对计两次，用降标分量 F_{0i} = E_i/c、F_{12} = −B_z、F_{13} = +B_y、F_{23} = −B_x（A 节）以及第 2 步的 F̃^{μν}：

  Time–space: Σ_i F_{0i} F̃^{0i} = Σ_i (E_i/c)(−B_i) = −(**E**·**B**)/c,
  Space–space: F_{12}F̃^{12} + F_{13}F̃^{13} + F_{23}F̃^{23} = (−B_z)(E_z/c) + (B_y)(−E_y/c) + (−B_x)(E_x/c) = −(**E**·**B**)/c.

Therefore:

因此：

  **F_{μν} F̃^{μν} = 2[ −(**E**·**B**)/c − (**E**·**B**)/c ] = −4(**E**·**B**)/c**  (SI, metric +−−−, ε^{0123} = +1).

The overall sign is fixed by the orientation convention ε^{0123} = +1; the magnitude 4|**E**·**B**|/c is convention-independent. This pseudoscalar, promoted to the non-abelian form G^a_{μν}G̃^{aμν}, is exactly the QCD **θ-term** behind the strong-CP problem (Module 8.3, [6.9 §D](../phase-6-quantum-field-theory/module-6.9-anomalies-and-nonperturbative-qft-derivations.md)).

总符号由定向约定 ε^{0123} = +1 固定；量值 4|**E**·**B**|/c 与约定无关。此赝标量推广为非阿贝尔形式 G^a_{μν}G̃^{aμν} 时，正是强 CP 问题背后的 QCD **θ 项**（模块 8.3、[6.9 §D](../phase-6-quantum-field-theory/module-6.9-anomalies-and-nonperturbative-qft-derivations.md)）。

**Step 4 — Physical significance of the two invariants.**

**第 4 步 — 两个不变量的物理意义。**

- **Invariant I = B² − E²/c²:** If I > 0, there exists a frame where E = 0 (purely magnetic). If I < 0, there exists a frame where B = 0 (purely electric). If I = 0 and **E**·**B** = 0, the field is null (e.g. a plane electromagnetic wave has B² = E²/c² and **E**·**B** = 0).

- **不变量 I = B² − E²/c²：** 若 I > 0，存在使 E = 0 的参考系（纯磁场）；若 I < 0，存在使 B = 0 的参考系（纯电场）；若 I = 0 且 **E**·**B** = 0，场为零曲率（例如平面电磁波满足 B² = E²/c² 且 **E**·**B** = 0）。

- **Invariant II ∝ E·B:** If this is zero in one frame, it is zero in all frames — no boost can produce **E**·**B** ≠ 0 from **E**·**B** = 0. This appears in the Lagrangian of the θ-vacuum in QCD (the strong CP problem, Phase 8).

- **不变量 II ∝ E·B：** 若在某参考系中为零，则在所有参考系中均为零——变换不能从 **E**·**B** = 0 产生 **E**·**B** ≠ 0。此量出现在 QCD θ 真空的拉格朗日量中（强 CP 问题，第 8 阶段）。∎

---

## E. Maxwell's Equations from the Action Principle · 由作用量原理导出麦克斯韦方程

**Claim.** The inhomogeneous Maxwell equations ∂_μ F^{μν} = μ₀ J^ν follow from extremizing the manifestly Lorentz-invariant action

**命题。** 非齐次麦克斯韦方程 ∂_μ F^{μν} = μ₀ J^ν 来自对显式洛伦兹不变作用量取极值

  S[A] = ∫ d⁴x  ℒ,   ℒ = −(1/4μ₀) F_{μν} F^{μν} − J^μ A_μ,

with respect to the four-potential A_μ. The homogeneous pair (Gauss's law for magnetism and Faraday's law) is **not** an equation of motion at all — it is the Bianchi identity, an algebraic consequence of F = dA. This is the cleanest statement of electromagnetism: one scalar functional, one field A_μ, and both pairs of Maxwell's equations drop out.

对四矢量势 A_μ 取极值。齐次对（磁场高斯定律与法拉第定律）**根本不是**运动方程——它是比安基恒等式，是 F = dA 的代数推论。这是电磁学最简洁的表述：一个标量泛函、一个场 A_μ，麦克斯韦方程的两对都随之而出。

**Step 1 — The field-strength term is the unique gauge-invariant kinetic term.** Under a gauge transformation A_μ → A_μ + ∂_μχ, the tensor F_{μν} = ∂_μA_ν − ∂_νA_μ is invariant (Section A), so any function of F_{μν} is gauge-invariant. Lorentz invariance, gauge invariance, parity, and at most two derivatives single out F_{μν}F^{μν} as the kinetic term (the dual invariant F_{μν}F̃^{μν} of Section D is a total derivative and does not affect the equations of motion). The constant −1/4μ₀ fixes the normalization so that ℒ reproduces the energy density ½(ε₀E² + B²/μ₀) below.

**第 1 步 — 场强项是唯一的规范不变动能项。** 在规范变换 A_μ → A_μ + ∂_μχ 下，张量 F_{μν} = ∂_μA_ν − ∂_νA_μ 不变（A 节），故 F_{μν} 的任何函数都规范不变。洛伦兹不变性、规范不变性、宇称以及至多两个导数共同选出 F_{μν}F^{μν} 作为动能项（D 节的对偶不变量 F_{μν}F̃^{μν} 是全导数，不影响运动方程）。常数 −1/4μ₀ 固定归一化，使 ℒ 重现下文的能量密度 ½(ε₀E² + B²/μ₀)。

**Step 2 — Euler–Lagrange equation for A_μ.** The Euler–Lagrange equation for the field A_β is

**第 2 步 — A_μ 的欧拉–拉格朗日方程。** 场 A_β 的欧拉–拉格朗日方程为

  ∂_α [ ∂ℒ/∂(∂_α A_β) ] − ∂ℒ/∂A_β = 0.

We need the derivative of the kinetic term with respect to ∂_αA_β. Write F_{μν}F^{μν} and use ∂F_{μν}/∂(∂_αA_β) = δ^α_μ δ^β_ν − δ^α_ν δ^β_μ:

我们需要动能项对 ∂_αA_β 的导数。利用 ∂F_{μν}/∂(∂_αA_β) = δ^α_μ δ^β_ν − δ^α_ν δ^β_μ：

  ∂(F_{μν}F^{μν})/∂(∂_αA_β) = 2 F^{μν} (δ^α_μ δ^β_ν − δ^α_ν δ^β_μ) = 2(F^{αβ} − F^{βα}) = 4F^{αβ},

so

故

  ∂ℒ/∂(∂_α A_β) = −(1/4μ₀)(4F^{αβ}) = −(1/μ₀) F^{αβ},   ∂ℒ/∂A_β = −J^β.

**Step 3 — Assemble the equation of motion.** Substituting into Euler–Lagrange:

**第 3 步 — 组装运动方程。** 代入欧拉–拉格朗日方程：

  ∂_α [ −(1/μ₀) F^{αβ} ] − ( −J^β ) = 0  ⟹  −(1/μ₀) ∂_α F^{αβ} + J^β = 0  ⟹  **∂_α F^{αβ} = μ₀ J^β**.

This is exactly the covariant inhomogeneous Maxwell equation of Section C — Gauss's law (β = 0) and the Ampère–Maxwell law (β = i). The current conservation ∂_β J^β = 0 follows immediately from the antisymmetry of F^{αβ}: ∂_β∂_α F^{αβ} = 0 because ∂_β∂_α is symmetric while F^{αβ} is antisymmetric.

这正是 C 节的协变非齐次麦克斯韦方程——高斯定律（β = 0）与安培–麦克斯韦定律（β = i）。电流守恒 ∂_β J^β = 0 立即由 F^{αβ} 的反对称性得出：∂_β∂_α F^{αβ} = 0，因为 ∂_β∂_α 对称而 F^{αβ} 反对称。

**Step 4 — The homogeneous pair is the Bianchi identity.** Because F_{μν} = ∂_μA_ν − ∂_νA_μ is exact (F = dA), it satisfies identically

**第 4 步 — 齐次对即比安基恒等式。** 由于 F_{μν} = ∂_μA_ν − ∂_νA_μ 是恰当的（F = dA），它恒满足

  ∂_λ F_{μν} + ∂_μ F_{νλ} + ∂_ν F_{λμ} = 0   ⟺   ∂_λ F̃^{λν} = 0,

where F̃^{μν} = ½ε^{μναβ}F_{αβ} is the dual. Each term cancels in pairs upon substituting F = ∂A and using ∂_λ∂_μ = ∂_μ∂_λ. The ν = 0 component is ∇·B = 0; the ν = i components are Faraday's law ∂B/∂t + ∇×E = 0. No dynamics, no source — purely the statement "F is a curl."

其中 F̃^{μν} = ½ε^{μναβ}F_{αβ} 是对偶张量。代入 F = ∂A 并用 ∂_λ∂_μ = ∂_μ∂_λ，各项成对相消。ν = 0 分量即 ∇·B = 0；ν = i 分量即法拉第定律 ∂B/∂t + ∇×E = 0。没有动力学、没有源——纯粹是"F 是一个旋度"这一陈述。

**Step 5 — The stress-energy tensor (Noether → Belinfante).** The canonical stress-energy tensor from translation invariance, T^{μν}_can = (∂ℒ/∂(∂_μA_λ))∂^νA_λ − η^{μν}ℒ = −(1/μ₀)F^{μλ}∂^νA_λ − η^{μν}ℒ, is neither symmetric nor gauge-invariant. Adding the improvement term (1/μ₀)∂_λ(F^{λμ}A^ν) — a total derivative that, using ∂_λF^{λμ} = μ₀J^μ = 0 in source-free regions, changes neither the conserved energy–momentum nor the local conservation law — symmetrizes it to the gauge-invariant **Belinfante tensor**

**第 5 步 — 能动张量（诺特 → 贝林方特）。** 由平移不变性得到的正则能动张量 T^{μν}_can = (∂ℒ/∂(∂_μA_λ))∂^νA_λ − η^{μν}ℒ = −(1/μ₀)F^{μλ}∂^νA_λ − η^{μν}ℒ 既不对称也不规范不变。加入改进项 (1/μ₀)∂_λ(F^{λμ}A^ν)——一个全导数，在无源区利用 ∂_λF^{λμ} = μ₀J^μ = 0，它既不改变守恒的能量–动量，也不改变局域守恒律——将其对称化为规范不变的**贝林方特张量**

  **T^{μν} = (1/μ₀) [ −F^{μα} F^ν{}_α + ¼ η^{μν} F_{αβ}F^{αβ} ]**   (metric +−−−).

(In the opposite signature −+++ this is written T^{μν} = (1/μ₀)[F^{μα}F^ν{}_α − ¼η^{μν}F²]; the two overall signs flip together with η, so T^{00} is positive in both. The explicit component check is carried out in Section F.)

（在相反符号 −+++ 下写作 T^{μν} = (1/μ₀)[F^{μα}F^ν{}_α − ¼η^{μν}F²]；两处总符号随 η 一起翻转，故 T^{00} 在两种约定下均为正。显式分量验证见 F 节。）

This tensor is symmetric (T^{μν} = T^{νμ}), gauge-invariant (built only from F), traceless (η_{μν}T^{μν} = 0, reflecting the masslessness/conformal invariance of the photon), and conserved: ∂_μT^{μν} = −F^{νλ}J_λ in the presence of a source J (the Lorentz four-force density), and ∂_μT^{μν} = 0 in vacuum — precisely Poynting's theorem (energy conservation) and electromagnetic momentum conservation. The whole mechanical force law thus follows from the field action alone. ∎

该张量对称（T^{μν} = T^{νμ}）、规范不变（仅由 F 构造）、无迹（η_{μν}T^{μν} = 0，反映光子的无质量／共形不变性），且守恒：有源 J 时 ∂_μT^{μν} = −F^{νλ}J_λ（洛伦兹四维力密度），真空中 ∂_μT^{μν} = 0——正是坡印廷定理（能量守恒）与电磁动量守恒。于是整个力学的力定律仅由场作用量便得出。∎

---

## F. Component-by-Component Verification of the Stress-Energy Tensor · 能动张量的逐分量验证

**Claim.** Evaluating the Belinfante tensor T^{μν} = (1/μ₀)[−F^{μα}F^ν{}_α + ¼η^{μν}F_{αβ}F^{αβ}] on the explicit field components of Section A reproduces, component by component, the electromagnetic energy density, the Poynting (momentum-flux) vector, and the Maxwell stress tensor of elementary electromagnetism.

**命题。** 将贝林方特张量 T^{μν} = (1/μ₀)[−F^{μα}F^ν{}_α + ¼η^{μν}F_{αβ}F^{αβ}] 在 A 节的显式场分量上求值，逐分量重现基础电磁学的电磁能量密度、坡印廷（动量通量）矢量与麦克斯韦应力张量。

**Setup — components with one index raised.** From Section A, F_{0i} = E_i/c and F_{ij} = −ε_{ijk}B^k. Raising one index with η = diag(+,−,−,−):

**准备——升一个指标的分量。** 由 A 节，F_{0i} = E_i/c，F_{ij} = −ε_{ijk}B^k。用 η = diag(+,−,−,−) 升一个指标：

  F^{0i} = −E_i/c,  F^i{}_0 = E_i/c,  F^i{}_j = ε_{ijk}B^k,   and  F_{αβ}F^{αβ} = 2(B² − E²/c²) (Section D).

**Step 1 — Energy density T^{00}.** With η^{00} = +1:

**第 1 步 — 能量密度 T^{00}。** 取 η^{00} = +1：

  T^{00} = (1/μ₀)[ −F^{0α}F^0{}_α + ¼ F_{αβ}F^{αβ} ].

The first term: F^{0α}F^0{}_α = F^{0i}F^0{}_i = Σ_i(−E_i/c)(E_i/c) = −E²/c² (using F^0{}_i = η^{00}F_{0i} = E_i/c). Hence

第一项：F^{0α}F^0{}_α = Σ_i(−E_i/c)(E_i/c) = −E²/c²。故

  T^{00} = (1/μ₀)[ E²/c² + ¼·2(B² − E²/c²) ] = (1/μ₀)[ E²/c² + ½B² − ½E²/c² ] = (1/μ₀)[ ½E²/c² + ½B² ].

Using ε₀ = 1/(μ₀c²):

利用 ε₀ = 1/(μ₀c²)：

  **T^{00} = ½(ε₀E² + B²/μ₀) = u**  — the electromagnetic energy density. ✓

**Step 2 — Energy flux / momentum density T^{0i}.** Since η^{0i} = 0:

**第 2 步 — 能流／动量密度 T^{0i}。** 因 η^{0i} = 0：

  T^{0i} = −(1/μ₀)F^{0α}F^i{}_α = −(1/μ₀)F^{0j}F^i{}_j = −(1/μ₀)Σ_j(−E_j/c)(ε_{ijk}B^k) = (1/μ₀c)ε_{ijk}E_jB^k.

Therefore

因此

  **T^{0i} = (1/μ₀c)(**E** × **B**)_i = S_i/c**,   where **S** = (1/μ₀)**E** × **B** is the Poynting vector. ✓

T^{0i} is simultaneously the energy flux (×1/c) and the electromagnetic momentum density g_i = S_i/c² (×c) — the field carries momentum, as the relativistic symmetry T^{0i} = T^{i0} demands.

T^{0i} 同时是能流（×1/c）与电磁动量密度 g_i = S_i/c²（×c）——场携带动量，正如相对论对称性 T^{0i} = T^{i0} 所要求。

**Step 3 — Stress (momentum flux) T^{ij} = the Maxwell stress tensor.** With η^{ij} = −δ_{ij}:

**第 3 步 — 应力（动量通量）T^{ij} = 麦克斯韦应力张量。** 取 η^{ij} = −δ_{ij}：

  T^{ij} = (1/μ₀)[ −F^{iα}F^j{}_α − ¼δ_{ij}F_{αβ}F^{αβ} ].

The contraction splits into time and space parts: −F^{iα}F^j{}_α = −[F^{i0}F^j{}_0 + F^{ik}F^j{}_k] = −[(E_i/c)(E_j/c) + (−ε_{ikm}B^m)(ε_{jkn}B^n)]. Using Σ_k ε_{ikm}ε_{jkn} = δ_{ij}δ_{mn} − δ_{in}δ_{mj}, the magnetic piece is −(−(δ_{ij}B² − B_iB_j)) = δ_{ij}B² − B_iB_j, so

缩并分为时间与空间两部分；利用 Σ_k ε_{ikm}ε_{jkn} = δ_{ij}δ_{mn} − δ_{in}δ_{mj} 处理磁场部分，得

  −F^{iα}F^j{}_α = −E_iE_j/c² + δ_{ij}B² − B_iB_j.

The trace term is −¼δ_{ij}·2(B² − E²/c²) = −½δ_{ij}B² + ½δ_{ij}E²/c². Adding:

迹项为 −½δ_{ij}B² + ½δ_{ij}E²/c²。相加：

  T^{ij} = (1/μ₀)[ −E_iE_j/c² − B_iB_j + ½δ_{ij}(E²/c² + B²) ]
         = −[ ε₀(E_iE_j − ½δ_{ij}E²) + (1/μ₀)(B_iB_j − ½δ_{ij}B²) ] = −σ_{ij},

which is **minus the Maxwell stress tensor** σ_{ij} of electrostatics/magnetostatics. The sign is correct: T^{ij} is the flux of i-momentum in the j-direction, and −σ_{ij} is the rate at which field momentum flows, so ∂_μT^{μi} = 0 reproduces the momentum-conservation law **f** + ∂**g**/∂t = ∇·σ of Maxwell stress. ✓ ∎

即**麦克斯韦应力张量 σ_{ij} 的相反数**。符号正确：T^{ij} 是 i 方向动量沿 j 方向的通量，−σ_{ij} 是场动量的流动率，故 ∂_μT^{μi} = 0 重现麦克斯韦应力的动量守恒律 **f** + ∂**g**/∂t = ∇·σ。✓ ∎

---

*All results follow from the covariant structure of F^{μν} = ∂^μ A^ν − ∂^ν A^μ and the Lorentz transformation law for rank-2 tensors.*

---

*All results follow from the covariant structure of F^{μν} = ∂^μ A^ν − ∂^ν A^μ and the Lorentz transformation law for rank-2 tensors.*

*所有结果均来自 F^{μν} = ∂^μ A^ν − ∂^ν A^μ 的协变结构以及 2 阶张量的洛伦兹变换法则。*

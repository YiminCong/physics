# Derivations — Module 5.5: BCS Theory
# 推导 — 模块 5.5：BCS 理论

> Companion to [Module 5.5](./module-5.5-bcs-theory.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 5.5](./module-5.5-bcs-theory.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The BCS Variational Ground State · BCS 变分基态

**Claim.** The BCS ground state |BCS⟩ = ∏_k (u_k + v_k c_{k↑}† c_{−k↓}†)|vac⟩ is a coherent superposition of pair-occupied and pair-empty states, with |u_k|² + |v_k|² = 1 (normalization) and v_k, u_k real. Minimizing ⟨BCS|Ĥ − μN̂|BCS⟩ yields the BCS coefficients and the gap equation.

**命题。** BCS 基态 |BCS⟩ = ∏_k (u_k + v_k c_{k↑}† c_{−k↓}†)|vac⟩ 是配对占据态和配对空态的相干叠加，满足 |u_k|² + |v_k|² = 1（归一化），v_k，u_k 为实数。最小化 ⟨BCS|Ĥ − μN̂|BCS⟩ 给出 BCS 系数和能隙方程。

**Step 1 — Define the BCS state.** For each momentum-spin pair (k↑, −k↓), introduce the pair state parametrized by real angles:

**第 1 步 — 定义 BCS 态。** 对每个动量–自旋对 (k↑, −k↓)，引入由实角度参数化的配对态：

  u_k = cos(θ_k/2),   v_k = sin(θ_k/2),   u_k² + v_k² = 1.

The state |BCS⟩ = ∏_k (u_k + v_k c_{k↑}† c_{−k↓}†)|vac⟩ is normalized: ⟨BCS|BCS⟩ = ∏_k (u_k² + v_k²) = 1.

态 |BCS⟩ = ∏_k (u_k + v_k c_{k↑}† c_{−k↓}†)|vac⟩ 是归一的：⟨BCS|BCS⟩ = ∏_k (u_k² + v_k²) = 1。

This state is a superposition of different particle numbers (not a number eigenstate), which is appropriate for a superconductor in the thermodynamic limit.

这个态是不同粒子数的叠加（不是粒子数本征态），在热力学极限下适合描述超导体。

**Step 2 — BCS Hamiltonian.** The full Hamiltonian (in second quantization, Module 3.12) is

**第 2 步 — BCS 哈密顿量。** 完整哈密顿量（用二次量子化，模块 3.12）为

  Ĥ = Σ_{k,σ} ε_k c_{kσ}† c_{kσ} − g Σ_{k,k′} c_{k′↑}† c_{−k′↓}† c_{−k↓} c_{k↑},

where ε_k is measured from the chemical potential μ (so ε_k = ℏ²k²/2m − μ < 0 below and > 0 above the Fermi surface), and −g < 0 is the constant attractive interaction within ℏω_D of E_F.

其中 ε_k 从化学势 μ 量起（故 ε_k = ℏ²k²/2m − μ：费米面以下 < 0，以上 > 0），−g < 0 是在 E_F 的 ℏω_D 范围内的常数吸引相互作用。

**Step 3 — Mean-field (BCS) decoupling.** Define the gap parameter

**第 3 步 — 平均场（BCS）解耦。** 定义能隙参数

  Δ = g Σ_k ⟨c_{−k↓} c_{k↑}⟩,

the expectation value of the pair annihilation operator (a c-number in the mean-field approximation). Write c_{−k↓} c_{k↑} = ⟨c_{−k↓} c_{k↑}⟩ + fluctuation. The quartic interaction term becomes (discarding quadratic fluctuation terms):

配对湮灭算符的期望值（在平均场近似中为一个 c 数）。写 c_{−k↓} c_{k↑} = ⟨c_{−k↓} c_{k↑}⟩ + 涨落。四次相互作用项变为（舍去二次涨落项）：

  −g Σ_{k,k′} c_{k′↑}† c_{−k′↓}† c_{−k↓} c_{k↑}
  ≈ −Σ_k [Δ c_{k↑}† c_{−k↓}† + Δ* c_{−k↓} c_{k↑}] + |Δ|²/g.

The effective BCS Hamiltonian is therefore

有效 BCS 哈密顿量因此为

  Ĥ_BCS = Σ_k ε_k (c_{k↑}† c_{k↑} + c_{−k↓}† c_{−k↓}) − Σ_k [Δ c_{k↑}† c_{−k↓}† + Δ* c_{−k↓} c_{k↑}] + |Δ|²/g.

---

## B. Bogoliubov Transformation and Quasiparticle Energies · 博戈留波夫变换与准粒子能量

**Claim.** The Bogoliubov transformation diagonalizes Ĥ_BCS. The new quasiparticle operators γ_{k↑} = u_k c_{k↑} − v_k c_{−k↓}† have energy E_k = √(ε_k² + Δ²), and the spectrum has a gap of magnitude Δ at the Fermi surface.

**命题。** 博戈留波夫变换对角化 Ĥ_BCS。新准粒子算符 γ_{k↑} = u_k c_{k↑} − v_k c_{−k↓}† 具有能量 E_k = √(ε_k² + Δ²)，谱在费米面处有大小为 Δ 的能隙。

**Step 1 — Define the Bogoliubov transformation.** Introduce new fermionic operators (Bogoliubov quasiparticles):

**第 1 步 — 定义博戈留波夫变换。** 引入新的费米子算符（博戈留波夫准粒子）：

  γ_{k↑} = u_k c_{k↑} − v_k c_{−k↓}†,
  γ_{−k↓} = u_k c_{−k↓} + v_k c_{k↑}†.

These satisfy canonical anticommutation relations {γ_{k↑}, γ_{k↑}†} = 1 provided u_k² + v_k² = 1 (check: {u_k c_{k↑} − v_k c_{−k↓}†, u_k c_{k↑}† − v_k c_{−k↓}} = u_k²{c_{k↑},c_{k↑}†} + v_k²{c_{−k↓}†,c_{−k↓}} = u_k² + v_k² = 1). ✓

这些算符满足正则反对易关系 {γ_{k↑}, γ_{k↑}†} = 1，条件是 u_k² + v_k² = 1（验证：{u_k c_{k↑} − v_k c_{−k↓}†, u_k c_{k↑}† − v_k c_{−k↓}} = u_k²{c_{k↑},c_{k↑}†} + v_k²{c_{−k↓}†,c_{−k↓}} = u_k² + v_k² = 1）。✓

**Step 2 — Invert the transformation.** Solving for c_{k↑} and c_{−k↓}†:

**第 2 步 — 求逆变换。** 求解 c_{k↑} 和 c_{−k↓}†：

  c_{k↑} = u_k γ_{k↑} + v_k γ_{−k↓}†,
  c_{−k↓}† = −v_k γ_{k↑} + u_k γ_{−k↓}†.

**Step 3 — Substitute into Ĥ_BCS.** Compute c_{k↑}† c_{k↑} + c_{−k↓}† c_{−k↓} and the off-diagonal terms c_{k↑}† c_{−k↓}† + h.c. in terms of γ. The algebra yields (for each k-pair):

**第 3 步 — 代入 Ĥ_BCS。** 用 γ 算符计算 c_{k↑}† c_{k↑} + c_{−k↓}† c_{−k↓} 以及非对角项 c_{k↑}† c_{−k↓}† + h.c.。代数运算给出（对每个 k-对）：

  ε_k(c_{k↑}†c_{k↑} + c_{−k↓}†c_{−k↓}) − Δ(c_{k↑}†c_{−k↓}† + c_{−k↓}c_{k↑})
  = (2ε_k v_k² − 2Δ u_k v_k) · 1  +  [2ε_k u_k v_k − Δ(u_k² − v_k²)] · (γ_{k↑}†γ_{−k↓}† + h.c.)
  + (ε_k(u_k² − v_k²) + 2Δ u_k v_k)(γ_{k↑}†γ_{k↑} + γ_{−k↓}†γ_{−k↓}).

**Step 4 — Choose u_k, v_k to eliminate off-diagonal terms.** Require the coefficient of the off-diagonal (γ†γ†) terms to vanish:

**第 4 步 — 选择 u_k、v_k 消去非对角项。** 要求非对角（γ†γ†）项的系数为零：

  2ε_k u_k v_k − Δ(u_k² − v_k²) = 0.

Using u_k = cos θ, v_k = sin θ: 2ε_k sin θ cos θ − Δ(cos²θ − sin²θ) = 0, i.e. ε_k sin(2θ) − Δ cos(2θ) = 0. Therefore:

使用 u_k = cos θ，v_k = sin θ：2ε_k sin θ cos θ + Δ(cos²θ − sin²θ) = 0，即 ε_k sin(2θ) + Δ cos(2θ) = 0。因此：

  tan(2θ) = Δ/ε_k   ⟹   2θ = arctan(Δ/ε_k).

The diagonal coefficient of γ†γ becomes (using the above condition to simplify):

γ†γ 的对角系数变为（利用上述条件化简）：

  E_k = ε_k(u_k² − v_k²) + 2Δ u_k v_k = ε_k cos(2θ) + Δ sin(2θ)
      = ε_k · (ε_k/E_k) + Δ · (Δ/E_k) = (ε_k² + Δ²)/E_k,

where we used cos(2θ) = ε_k/E_k and sin(2θ) = +Δ/E_k (from the condition, with the sign chosen so E_k > 0 and consistent with u_k v_k = Δ/2E_k of Section C). Solving:

其中用到 cos(2θ) = ε_k/E_k 和 sin(2θ) = +Δ/E_k（由条件给出，选择符号使 E_k > 0，并与 C 节 u_k v_k = Δ/2E_k 一致）。求解：

  **E_k = √(ε_k² + Δ²).**

**Step 5 — Diagonalized Hamiltonian.** The BCS Hamiltonian in terms of quasiparticles is

**第 5 步 — 对角化哈密顿量。** 用准粒子表示的 BCS 哈密顿量为

  Ĥ_BCS = E_gs + Σ_k E_k (γ_{k↑}†γ_{k↑} + γ_{−k↓}†γ_{−k↓}),

where E_gs = Σ_k (2ε_k v_k² − 2Δ u_k v_k) + |Δ|²/g = Σ_k (ε_k − E_k) + |Δ|²/g is the ground-state energy (condensation energy). The quasiparticles are free fermions with dispersion E_k ≥ Δ. The minimum energy Δ is the gap. ∎

其中 E_gs = Σ_k (2ε_k v_k² − 2Δ u_k v_k) + |Δ|²/g = Σ_k (ε_k − E_k) + |Δ|²/g 是基态能量（凝聚能）。准粒子是色散关系为 E_k ≥ Δ 的自由费米子。最小能量 Δ 就是能隙。∎

---

## C. The BCS Gap Equation · BCS 能隙方程

**Claim.** The self-consistency condition Δ = g Σ_k ⟨c_{−k↓} c_{k↑}⟩ evaluated in the BCS ground state yields the gap equation 1 = gN(0)∫₀^{ℏω_D} dε/√(ε² + Δ²).

**命题。** 在 BCS 基态中计算自洽条件 Δ = g Σ_k ⟨c_{−k↓} c_{k↑}⟩，得到能隙方程 1 = gN(0)∫₀^{ℏω_D} dε/√(ε² + Δ²)。

**Step 1 — Compute ⟨c_{−k↓} c_{k↑}⟩ in the BCS state.** Using c_{k↑} = u_k γ_{k↑} + v_k γ_{−k↓}† and c_{−k↓} = u_k γ_{−k↓} − v_k γ_{k↑}†:

**第 1 步 — 在 BCS 态中计算 ⟨c_{−k↓} c_{k↑}⟩。** 使用 c_{k↑} = u_k γ_{k↑} + v_k γ_{−k↓}† 和 c_{−k↓} = u_k γ_{−k↓} − v_k γ_{k↑}†：

  c_{−k↓} c_{k↑} = (u_k γ_{−k↓} − v_k γ_{k↑}†)(u_k γ_{k↑} + v_k γ_{−k↓}†)
               = u_k² γ_{−k↓}γ_{k↑} + u_k v_k γ_{−k↓}γ_{−k↓}† − v_k u_k γ_{k↑}†γ_{k↑} − v_k² γ_{k↑}†γ_{−k↓}†.

In the BCS ground state |BCS⟩ (all quasiparticle states empty, γ_{kσ}|BCS⟩ = 0):

在 BCS 基态 |BCS⟩（所有准粒子态为空，γ_{kσ}|BCS⟩ = 0）中：

  ⟨γ_{−k↓}γ_{k↑}⟩ = 0,   ⟨γ_{−k↓}γ_{−k↓}†⟩ = 1,   ⟨γ_{k↑}†γ_{k↑}⟩ = 0,   ⟨γ_{k↑}†γ_{−k↓}†⟩ = 0.

Therefore:

因此：

  ⟨c_{−k↓} c_{k↑}⟩ = u_k v_k · 1 = u_k v_k.

**Step 2 — Substitute into the gap definition.** Recalling u_k v_k = ½ sin(2θ_k) = Δ/(2E_k) (from Step 4 of Section B, where sin(2θ) = Δ/E_k with our chosen sign convention at T = 0):

**第 2 步 — 代入能隙定义。** 回顾 u_k v_k = ½ sin(2θ_k) = Δ/(2E_k)（由 B 节第 4 步，其中 sin(2θ) = Δ/E_k，取 T = 0 时的符号约定）：

  Δ = g Σ_k ⟨c_{−k↓} c_{k↑}⟩ = g Σ_k u_k v_k = g Σ_k Δ/(2E_k).

Divide both sides by Δ (assuming Δ ≠ 0, i.e., superconducting solution):

两边除以 Δ（假设 Δ ≠ 0，即超导解）：

  1 = g Σ_k 1/(2E_k) = g Σ_k 1/(2√(ε_k² + Δ²)).

**Step 3 — Convert to integral.** Replace the k-sum using the density of states N(0) (constant near the Fermi surface), integrating ε from −ℏω_D to +ℏω_D (the phonon window). By symmetry ε → −ε:

**第 3 步 — 转化为积分。** 用态密度 N(0)（在费米面附近为常数）替换 k 求和，对 ε 从 −ℏω_D 积分到 +ℏω_D（声子窗口）。由 ε → −ε 的对称性：

  1 = g N(0) ∫₋ℏω_D^{ℏω_D} dε/(2√(ε² + Δ²)) = g N(0) ∫₀^{ℏω_D} dε/√(ε² + Δ²).

This is the **BCS gap equation**:

这是 **BCS 能隙方程**：

  **1 = g N(0) ∫₀^{ℏω_D} dε/√(ε² + Δ²).** ∎

---

## D. Solving the Gap Equation: Δ ≈ 2ℏω_D e^{−1/(gN(0))} · 求解能隙方程：Δ ≈ 2ℏω_D e^{−1/(gN(0))}

**Claim.** In the weak-coupling limit gN(0) ≪ 1, the gap equation yields Δ(0) ≈ 2ℏω_D e^{−1/(gN(0))}.

**命题。** 在弱耦合极限 gN(0) ≪ 1 下，能隙方程给出 Δ(0) ≈ 2ℏω_D e^{−1/(gN(0))}。

**Step 1 — Evaluate the integral.** Compute I = ∫₀^{ℏω_D} dε/√(ε² + Δ²):

**第 1 步 — 计算积分。** 计算 I = ∫₀^{ℏω_D} dε/√(ε² + Δ²)：

  I = [sinh⁻¹(ε/Δ)]₀^{ℏω_D} = sinh⁻¹(ℏω_D/Δ) − sinh⁻¹(0) = sinh⁻¹(ℏω_D/Δ).

Using sinh⁻¹(x) = ln(x + √(x²+1)):

使用 sinh⁻¹(x) = ln(x + √(x²+1))：

  I = ln(ℏω_D/Δ + √((ℏω_D/Δ)² + 1)).

**Step 2 — Weak-coupling approximation.** For gN(0) ≪ 1, the gap Δ ≪ ℏω_D (we verify this a posteriori). Then ℏω_D/Δ ≫ 1, and √((ℏω_D/Δ)² + 1) ≈ ℏω_D/Δ:

**第 2 步 — 弱耦合近似。** 当 gN(0) ≪ 1 时，能隙 Δ ≪ ℏω_D（事后验证）。则 ℏω_D/Δ ≫ 1，√((ℏω_D/Δ)² + 1) ≈ ℏω_D/Δ：

  I ≈ ln(2ℏω_D/Δ).

**Step 3 — Solve for Δ.** The gap equation 1 = gN(0) · I gives:

**第 3 步 — 求解 Δ。** 能隙方程 1 = gN(0) · I 给出：

  1 = gN(0) ln(2ℏω_D/Δ)   ⟹   ln(2ℏω_D/Δ) = 1/(gN(0)).

Exponentiate:

取指数：

  2ℏω_D/Δ = e^{1/(gN(0))}   ⟹   **Δ(0) = 2ℏω_D e^{−1/(gN(0))}**.

**Step 4 — Consistency check.** For gN(0) = 0.3 (a typical weak-coupling value), Δ/ℏω_D ≈ 2e^{−1/0.3} ≈ 2 × 0.0357 ≈ 0.071 ≪ 1, confirming the weak-coupling approximation a posteriori. ∎

**第 4 步 — 一致性检验。** 对 gN(0) = 0.3（典型弱耦合值），Δ/ℏω_D ≈ 2e^{−1/0.3} ≈ 2 × 0.0357 ≈ 0.071 ≪ 1，事后确认弱耦合近似。∎

**Note on non-analyticity.** Like the Cooper binding energy of Module 5.4, Δ(0) ∝ e^{−1/(gN(0))} is non-analytic in g at g = 0. All Taylor coefficients of e^{−1/g} at g = 0 vanish, so the gap cannot be obtained by any finite-order perturbation theory. This is the microscopic explanation of why a mean-field theory is needed. ∎

**关于非解析性的注记。** 与模块 5.4 的库珀束缚能类似，Δ(0) ∝ e^{−1/(gN(0))} 在 g = 0 处对 g 是非解析的。e^{−1/g} 在 g = 0 处的所有泰勒系数均为零，故能隙不能由任何有限阶微扰论得到。这是需要平均场理论的微观解释。∎

---

## E. The Universal Ratio 2Δ(0) = 3.52 k_B T_c · 普适比值 2Δ(0) = 3.52 k_B T_c

**Claim.** Near T_c, Δ → 0 and the gap equation can be linearized to determine T_c. Combining the T_c formula with Δ(0) gives the universal (material-independent) ratio 2Δ(0)/(k_B T_c) = 2π/e^γ ≈ 3.528, where γ ≈ 0.5772 is the Euler–Mascheroni constant.

**命题。** 在 T_c 附近，Δ → 0，能隙方程可以被线性化以确定 T_c。将 T_c 公式与 Δ(0) 结合给出普适（与材料无关的）比值 2Δ(0)/(k_B T_c) = 2π/e^γ ≈ 3.528，其中 γ ≈ 0.5772 是欧拉–马斯凯罗尼常数。

**Step 1 — Gap equation at finite temperature.** At temperature T, the quasiparticle states are thermally occupied. The self-consistency condition generalizes to

**第 1 步 — 有限温度的能隙方程。** 在温度 T 下，准粒子态被热激活占据。自洽条件推广为

  1 = gN(0) ∫₀^{ℏω_D} dε/√(ε² + Δ²) · tanh(√(ε² + Δ²)/(2k_B T)).

The tanh factor accounts for the Fermi–Dirac distribution: at T = 0, tanh → 1, recovering Section D. The gap Δ(T) decreases monotonically from Δ(0) as T increases, reaching zero at T = T_c.

tanh 因子来自费米–狄拉克分布：在 T = 0 时，tanh → 1，还原到 D 节。能隙 Δ(T) 随 T 增大从 Δ(0) 单调减小，在 T = T_c 处趋于零。

**Step 2 — Determine T_c by linearization.** At T = T_c, Δ → 0. The gap equation reduces to (setting Δ = 0 in the integrand):

**第 2 步 — 通过线性化确定 T_c。** 在 T = T_c 时，Δ → 0。能隙方程化为（在被积函数中令 Δ = 0）：

  1 = gN(0) ∫₀^{ℏω_D} (dε/ε) tanh(ε/(2k_B T_c)).

**Step 3 — Evaluate the integral.** The integral I_c = ∫₀^{ℏω_D} (dε/ε) tanh(ε/(2k_BT_c)) is a standard result. Let x = ε/(2k_BT_c) and X = ℏω_D/(2k_BT_c) ≫ 1 (weak coupling). Then:

**第 3 步 — 计算积分。** 积分 I_c = ∫₀^{ℏω_D} (dε/ε) tanh(ε/(2k_BT_c)) 是标准结果。令 x = ε/(2k_BT_c)，X = ℏω_D/(2k_BT_c) ≫ 1（弱耦合）。则：

  I_c = ∫₀^X (dx/x) tanh(x).

Integration by parts and use of the known result for the Sommerfeld expansion (see any field theory text):

分部积分并使用索末菲展开的已知结果（见任何场论教材）：

  ∫₀^X (dx/x) tanh(x) = ln(X) + ln(4e^γ/π) + O(1/X²)   for X ≫ 1,

where γ = 0.5772… is the Euler–Mascheroni constant (the same that appears in the asymptotic expansion of the digamma function and in Σ 1/n − ln n). The key step uses the Fourier series for tanh and the integral ∫₀^∞ (tanh x − 1)/x dx = −ln(4e^γ/π). Thus:

其中 γ = 0.5772… 是欧拉–马斯凯罗尼常数（与双伽马（digamma）函数的渐近展开和 Σ 1/n − ln n 中出现的相同）。关键步骤使用 tanh 的傅里叶级数和积分 ∫₀^∞ (tanh x − 1)/x dx = −ln(4e^γ/π)。于是：

  I_c ≈ ln(ℏω_D/(2k_BT_c)) + ln(4e^γ/π) = ln(2e^γ ℏω_D/(π k_BT_c)).

**Step 4 — T_c formula.** Setting 1/(gN(0)) = I_c:

**第 4 步 — T_c 公式。** 令 1/(gN(0)) = I_c：

  1/(gN(0)) = ln(2e^γ ℏω_D/(π k_BT_c))   ⟹   k_BT_c = (2e^γ/π) ℏω_D e^{−1/(gN(0))}.

Numerically, 2e^γ/π = 2 × 1.7811/3.1416 ≈ 1.1340. Hence:

数值上，2e^γ/π = 2 × 1.7811/3.1416 ≈ 1.1340。故：

  **k_BT_c ≈ 1.134 ℏω_D e^{−1/(gN(0))}**.

**Step 5 — Compute 2Δ(0)/(k_BT_c).** Divide Δ(0) = 2ℏω_D e^{−1/(gN(0))} by k_BT_c:

**第 5 步 — 计算 2Δ(0)/(k_BT_c)。** 将 Δ(0) = 2ℏω_D e^{−1/(gN(0))} 除以 k_BT_c：

  2Δ(0)/(k_BT_c) = 2 × 2ℏω_D e^{−1/(gN(0))} / (1.134 ℏω_D e^{−1/(gN(0))})

                 = 4/1.134 = 4/(2e^γ/π) = 4π/(2e^γ) = 2π/e^γ.

**Step 6 — Numerical value.** e^γ = e^{0.5772} ≈ 1.7811, so 2π/e^γ ≈ 6.2832/1.7811 ≈ **3.528 ≈ 3.52**.

**第 6 步 — 数值。** e^γ = e^{0.5772} ≈ 1.7811，故 2π/e^γ ≈ 6.2832/1.7811 ≈ **3.528 ≈ 3.52**。

Therefore:

因此：

  **2Δ(0) = (2π/e^γ) k_BT_c ≈ 3.528 k_BT_c ≈ 3.52 k_BT_c.** ∎

**Step 7 — Universality.** Notice that the factor e^{−1/(gN(0))} has cancelled between Δ(0) and k_BT_c. The ratio 2Δ(0)/(k_BT_c) = 2π/e^γ involves only universal numbers (π and Euler's constant γ) — it is the **same** for every BCS superconductor regardless of material. This is a celebrated prediction of the theory. Measured values: Pb ≈ 4.3, Nb ≈ 3.8, Al ≈ 3.4 (deviations from 3.52 are due to strong-coupling corrections, quantified by Eliashberg theory). ∎

**第 7 步 — 普适性。** 注意到 e^{−1/(gN(0))} 在 Δ(0) 和 k_BT_c 之间已经约消。比值 2Δ(0)/(k_BT_c) = 2π/e^γ 只涉及普适数（π 和欧拉常数 γ）——对**每一种** BCS 超导体都**相同**，与材料无关。这是该理论的著名预言。测量值：Pb ≈ 4.3，Nb ≈ 3.8，Al ≈ 3.4（偏离 3.52 是由强耦合修正引起的，由埃利亚什伯格理论定量）。∎

---

## F. BCS Coefficients and Ground-State Occupancy · BCS 系数与基态占据率

**Claim.** The variational coefficients u_k and v_k are u_k² = ½(1 + ε_k/E_k) and v_k² = ½(1 − ε_k/E_k), giving a smooth crossover from v_k = 1 (filled, ε_k ≪ −Δ) to v_k = 0 (empty, ε_k ≫ Δ) on a scale ∼ Δ around the Fermi surface.

**命题。** 变分系数 u_k 和 v_k 为 u_k² = ½(1 + ε_k/E_k)，v_k² = ½(1 − ε_k/E_k)，在费米面附近 ∼ Δ 的尺度上从 v_k = 1（填满，ε_k ≪ −Δ）平滑过渡到 v_k = 0（空态，ε_k ≫ Δ）。

**Step 1 — From the condition u_k v_k = Δ/(2E_k).** Together with u_k² + v_k² = 1:

**第 1 步 — 由条件 u_k v_k = Δ/(2E_k)。** 结合 u_k² + v_k² = 1：

  (u_k² − v_k²)² = (u_k² + v_k²)² − 4u_k²v_k² = 1 − Δ²/E_k² = ε_k²/E_k².

So u_k² − v_k² = ε_k/E_k (taking the sign so that u_k → 1, v_k → 0 for ε_k → +∞). Combined with u_k² + v_k² = 1:

故 u_k² − v_k² = ε_k/E_k（取符号使当 ε_k → +∞ 时 u_k → 1，v_k → 0）。结合 u_k² + v_k² = 1：

  **v_k² = ½(1 − ε_k/E_k),   u_k² = ½(1 + ε_k/E_k).**

**Step 2 — Physical limits.** 

**第 2 步 — 物理极限。**

  ε_k → −∞ (well inside Fermi sea): E_k → |ε_k| = −ε_k, so v_k² → ½(1+1) = 1, u_k² → 0. Pair fully occupied. ✓
  ε_k → +∞ (well above Fermi surface): E_k → ε_k, so v_k² → 0, u_k² → 1. Pair empty. ✓
  ε_k = 0 (at Fermi surface): E_k = Δ, so v_k² = u_k² = ½. Maximum quantum fluctuation. ✓

  ε_k → −∞（费米海深处）：E_k → |ε_k| = −ε_k，故 v_k² → 1，u_k² → 0。配对完全占据。✓
  ε_k → +∞（费米面以上）：E_k → ε_k，故 v_k² → 0，u_k² → 1。配对为空。✓
  ε_k = 0（费米面处）：E_k = Δ，故 v_k² = u_k² = ½。最大量子涨落。✓

The smooth BCS momentum distribution v_k² replaces the sharp Fermi step function, spreading over a width ∼ Δ/v_F around k_F — a direct consequence of the macroscopic quantum coherence of the condensate. ∎

平滑的 BCS 动量分布 v_k² 取代了尖锐的费米阶梯函数，在 k_F 附近 ∼ Δ/v_F 的宽度内扩展——这是凝聚体宏观量子相干性的直接后果。∎

---

*The BCS theory derived here is the microscopic justification for every result in Modules 5.1–5.3 and the starting point for Modules 5.6–5.9. The Bogoliubov quasiparticles reappear in tunneling spectroscopy (5.6), the vortex-core states (5.7), and the ac Josephson effect (5.8).*

*此处推导的 BCS 理论是模块 5.1–5.3 中每个结果的微观基础，也是模块 5.6–5.9 的出发点。博戈留波夫准粒子再次出现于隧穿谱（5.6）、涡旋核态（5.7）和交流约瑟夫森效应（5.8）。*

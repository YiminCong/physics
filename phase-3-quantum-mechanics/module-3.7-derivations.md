# Derivations — Module 3.7: Variational & WKB Methods
# 推导 — 模块 3.7：变分法与 WKB 方法

> Companion to [Module 3.7](./module-3.7-variational-and-wkb-methods.md). Full step-by-step proofs of the variational theorem, the WKB wavefunction, the tunneling factor, and the Bohr–Sommerfeld quantization condition. English first, then 中文.
> [模块 3.7](./module-3.7-variational-and-wkb-methods.md) 的配套文档：变分定理、WKB 波函数、隧穿因子与玻尔–索末菲量子化条件的完整逐步证明。先英文，后中文。

---

## A. The Variational Theorem · 变分定理

**Claim.** For any normalized trial state |ψ_trial⟩, the expectation value of the Hamiltonian satisfies ⟨ψ_trial|Ĥ|ψ_trial⟩ ≥ E₀, where E₀ is the true ground-state energy.

**命题。** 对于任意归一化试探态 |ψ_trial⟩，哈密顿量的期望值满足 ⟨ψ_trial|Ĥ|ψ_trial⟩ ≥ E₀，其中 E₀ 为真实基态能量。

**Step 1 — Expand in the energy eigenbasis.** Assume Ĥ has a complete orthonormal set of eigenstates {|n⟩} with Ĥ|n⟩ = Eₙ|n⟩ and E₀ ≤ E₁ ≤ E₂ ≤ …. (By the spectral theorem for self-adjoint operators on L², such a basis exists whenever Ĥ has a purely discrete spectrum; in the general case with continuous spectrum the sum becomes an integral and the argument is unchanged in substance.) Expand the trial state as:

**第 1 步 — 在能量本征基中展开。** 假设 Ĥ 有完备正交归一本征态集 {|n⟩}，满足 Ĥ|n⟩ = Eₙ|n⟩，E₀ ≤ E₁ ≤ E₂ ≤ …。（由 L² 上自伴算符的谱定理，当 Ĥ 具有纯离散谱时此类基存在；一般连续谱情形下求和变为积分，论证实质不变。）将试探态展开为：

  |ψ_trial⟩ = Σₙ cₙ |n⟩,    cₙ = ⟨n|ψ_trial⟩.

**Step 2 — Normalization constraint.** The normalization condition ⟨ψ_trial|ψ_trial⟩ = 1 gives, using orthonormality ⟨m|n⟩ = δₘₙ:

**第 2 步 — 归一化约束。** 归一化条件 ⟨ψ_trial|ψ_trial⟩ = 1，利用正交归一性 ⟨m|n⟩ = δₘₙ，得：

  ⟨ψ_trial|ψ_trial⟩ = Σₙ |cₙ|² = 1.

**Step 3 — Compute the expectation value.** Insert the expansion and act with Ĥ:

**第 3 步 — 计算期望值。** 代入展开式，用 Ĥ 作用：

  ⟨ψ_trial|Ĥ|ψ_trial⟩ = (Σₘ cₘ* ⟨m|) Ĥ (Σₙ cₙ |n⟩)
                        = Σₘ Σₙ cₘ* cₙ ⟨m|Ĥ|n⟩
                        = Σₘ Σₙ cₘ* cₙ Eₙ ⟨m|n⟩
                        = Σₙ |cₙ|² Eₙ.

**Step 4 — Apply the ground-state lower bound.** Since Eₙ ≥ E₀ for all n, we may replace each Eₙ in the sum by E₀ (making the sum smaller or equal):

**第 4 步 — 应用基态下界。** 由于对所有 n 均有 Eₙ ≥ E₀，可在求和中将每个 Eₙ 替换为 E₀（使求和值减小或不变）：

  Σₙ |cₙ|² Eₙ ≥ Σₙ |cₙ|² E₀ = E₀ Σₙ |cₙ|² = E₀ · 1 = E₀.

**Step 5 — Conclude.** Combining Steps 3 and 4:

**第 5 步 — 结论。** 综合第 3、4 步：

  ⟨ψ_trial|Ĥ|ψ_trial⟩ = Σₙ |cₙ|² Eₙ ≥ E₀.

Equality holds if and only if cₙ = 0 for all n with Eₙ > E₀, i.e. if and only if the trial state lies entirely within the ground-state eigenspace. Therefore minimizing ⟨Ĥ⟩ over any family of trial states yields an upper bound on E₀ that approaches the true value as the family becomes more flexible. ∎

等号成立当且仅当对所有 Eₙ > E₀ 的 n 均有 cₙ = 0，即试探态完全落在基态本征空间内。因此，在任意一族试探态上最小化 ⟨Ĥ⟩ 给出 E₀ 的上界，随着该族函数越来越灵活，上界趋近真实值。∎

---

## B. The WKB Wavefunction · WKB 波函数

**Claim.** In the semiclassical limit ℏ → 0 with the de Broglie wavelength varying slowly compared to its own length scale, the Schrödinger equation −(ℏ²/2m)ψ″ + V(x)ψ = Eψ admits the approximate solution ψ(x) ≈ C/√(p(x)) · exp[(i/ℏ)∫ˣ p(x′) dx′], where p(x) = √(2m(E − V(x))) is the local classical momentum.

**命题。** 在半经典极限 ℏ → 0 下，当德布罗意波长的变化相对自身长度可以忽略时，薛定谔方程 −(ℏ²/2m)ψ″ + V(x)ψ = Eψ 有近似解 ψ(x) ≈ C/√(p(x)) · exp[(i/ℏ)∫ˣ p(x′) dx′]，其中 p(x) = √(2m(E − V(x))) 为局域经典动量。

**Step 1 — WKB ansatz.** Write the wavefunction as ψ(x) = exp[iS(x)/ℏ], where S(x) is a complex-valued function (the "eikonal"). This is motivated by the plane-wave solution in the uniform case V = const, where S = px − Et (classical action). Substituting into the Schrödinger equation:

**第 1 步 — WKB 拟设。** 将波函数写为 ψ(x) = exp[iS(x)/ℏ]，其中 S(x) 是复值函数（"程函"）。这受均匀情形 V = const 下平面波解 S = px − Et（经典作用量）的启发。代入薛定谔方程：

  −(ℏ²/2m) · (iS″/ℏ − (S′)²/ℏ²) ψ = (E − V) ψ.

Dividing both sides by ψ (which is nowhere zero in the classically allowed region):

两边除以 ψ（在经典允许区域不为零）：

  (S′)²/(2m) − iℏS″/(2m) = E − V = p²/(2m).

**Step 2 — Expand in powers of ℏ.** Write S = S₀ + (ℏ/i)S₁ + (ℏ/i)²S₂ + … and collect terms order by order.

**第 2 步 — 按 ℏ 幂次展开。** 令 S = S₀ + (ℏ/i)S₁ + (ℏ/i)²S₂ + …，逐阶收集各项。

Order ℏ⁰: (S₀′)² = p², so S₀′ = ±p(x), giving S₀ = ±∫ˣ p(x′) dx′.

ℏ⁰ 阶：(S₀′)² = p²，故 S₀′ = ±p(x)，得 S₀ = ±∫ˣ p(x′) dx′。

Order ℏ¹ (taking the + sign): 2S₀′ S₁′ = S₀″, so S₁′ = S₀″/(2S₀′) = p′/(2p). Integrating: S₁ = (1/2)ln(p) + const.

ℏ¹ 阶（取正号）：2S₀′ S₁′ = S₀″，故 S₁′ = S₀″/(2S₀′) = p′/(2p)。积分得：S₁ = (1/2)ln(p) + const。

**Step 3 — Reconstruct the wavefunction.** Inserting back into ψ = exp[iS/ℏ] = exp[iS₀/ℏ] · exp[−S₁ + O(ℏ)]:

**第 3 步 — 重构波函数。** 代回 ψ = exp[iS/ℏ] = exp[iS₀/ℏ] · exp[−S₁ + O(ℏ)]：

  ψ(x) ≈ exp[−(1/2)ln p] · exp[(i/ℏ)∫ˣ p dx′]
         = (1/√p(x)) · exp[(i/ℏ)∫ˣ p(x′) dx′].

Including both sign choices and absorbing the normalization constants A, B:

包含两种符号选择，将归一化常数记为 A、B：

  ψ(x) ≈ A/√p(x) · exp[(i/ℏ)∫ˣ p dx′] + B/√p(x) · exp[−(i/ℏ)∫ˣ p dx′].

**Step 4 — Validity condition.** The expansion is valid when higher-order terms are small, i.e. |ℏ dλ/dx| ≪ 1, where λ = h/p is the de Broglie wavelength. Equivalently:

**第 4 步 — 有效条件。** 展开有效的条件是高阶项很小，即 |ℏ dλ/dx| ≪ 1，其中 λ = h/p 为德布罗意波长。等价地：

  |dp/dx| ≪ p²/ℏ,   i.e.   |d(ℏ/p)/dx| ≪ 1.

This fails near classical turning points where p → 0. There the WKB approximation breaks down and connection formulae (involving Airy functions) must be used to match solutions across the turning point. ∎

这在经典转折点附近 p → 0 处失效。在转折点处 WKB 近似失效，必须使用联结公式（涉及艾里函数）将两侧的解匹配起来。∎

---

## C. The WKB Tunneling Factor · WKB 隧穿因子

**Claim.** For a classically forbidden region x₁ ≤ x ≤ x₂ where E < V(x) (so the local momentum is imaginary, p(x) = i|p(x)| with |p(x)| = √(2m(V(x) − E))), the WKB transmission amplitude is exponentially suppressed, giving a tunneling probability:

**命题。** 对于经典禁区 x₁ ≤ x ≤ x₂，其中 E < V(x)（局域动量为虚数，p(x) = i|p(x)|，|p(x)| = √(2m(V(x) − E))），WKB 透射振幅呈指数衰减，隧穿概率为：

  T ≈ exp[−(2/ℏ)∫_{x₁}^{x₂} |p(x)| dx].

**Step 1 — WKB in the forbidden region.** When E < V(x), define κ(x) = √(2m(V(x) − E))/ℏ > 0. The local "momentum" becomes purely imaginary: p = iℏκ. The WKB ansatz gives:

**第 1 步 — 禁区中的 WKB。** 当 E < V(x) 时，定义 κ(x) = √(2m(V(x) − E))/ℏ > 0。局域"动量"变为纯虚数：p = iℏκ。WKB 拟设给出：

  ψ(x) ≈ C/√(κ(x)) · exp[−∫_{x₁}^{x} κ(x′) dx′] + D/√(κ(x)) · exp[+∫_{x₁}^{x} κ(x′) dx′].

The growing exponential (D term) must be set to zero for a bound tunneling problem (or matched via connection formulae to an outgoing wave on the right); the decaying exponential is the tunneling solution.

增长指数项（D 项）在束缚隧穿问题中必须为零（或通过联结公式与右侧出射波匹配）；衰减指数项即隧穿解。

**Step 2 — Amplitude ratio across the barrier.** The amplitude of the transmitted wave at x₂ relative to the incident wave at x₁ is:

**第 2 步 — 势垒两侧振幅比。** 在 x₂ 处透射波振幅与 x₁ 处入射波振幅之比为：

  ψ(x₂)/ψ(x₁) = exp[−∫_{x₁}^{x₂} κ(x) dx] = exp[−(1/ℏ)∫_{x₁}^{x₂} √(2m(V−E)) dx].

**Step 3 — Transmission probability.** The transmission coefficient T is the ratio of transmitted to incident probability current j = (ℏ/m)Im(ψ* dψ/dx). Since the probability current is proportional to |ψ|² times the velocity in the WKB approximation, T ≈ |ψ(x₂)/ψ(x₁)|², giving:

**第 3 步 — 透射概率。** 透射系数 T 是透射概率流与入射概率流之比 j = (ℏ/m)Im(ψ* dψ/dx)。在 WKB 近似中概率流正比于 |ψ|² 乘以速度，故 T ≈ |ψ(x₂)/ψ(x₁)|²，得：

  T ≈ exp[−(2/ℏ)∫_{x₁}^{x₂} |p(x)| dx],

where |p(x)| = √(2m(V(x) − E)) = ℏκ(x). ∎

其中 |p(x)| = √(2m(V(x) − E)) = ℏκ(x)。∎

**Physical interpretation.** The exponent is the "WKB integral" or "tunneling integral." For alpha decay, the barrier is the Coulomb potential; this integral gives the Gamow factor explaining the enormous range of decay rates (factor of 10²⁰) by modest variation in alpha-particle energy.

**物理诠释。** 指数中的量为"WKB 积分"或"隧穿积分"。对于 α 衰变，势垒为库仑势；此积分给出伽莫夫因子，解释了衰变率极大范围的变化（相差 10²⁰ 倍）如何由 α 粒子能量的适度变化产生。

---

## D. Bohr–Sommerfeld Quantization · 玻尔–索末菲量子化

**Claim.** For a classically allowed region between two turning points x₁ and x₂, the WKB quantization condition is ∮ p dx = (n + ½)h, where the integral is over one complete classical oscillation and n = 0, 1, 2, …

**命题。** 对于两个转折点 x₁ 和 x₂ 之间的经典允许区域，WKB 量子化条件为 ∮ p dx = (n + ½)h，其中积分取一个完整经典振荡，n = 0, 1, 2, …

**Step 1 — WKB solution in the classically allowed region.** Between the turning points, p(x) = √(2m(E − V(x))) > 0. The general WKB solution is:

**第 1 步 — 经典允许区域中的 WKB 解。** 在转折点之间，p(x) = √(2m(E − V(x))) > 0。一般 WKB 解为：

  ψ(x) = A/√p · exp[(i/ℏ)∫_{x₁}^{x} p dx′] + B/√p · exp[−(i/ℏ)∫_{x₁}^{x} p dx′].

**Step 2 — Connection formulae at turning points.** Near a left turning point x₁ (where V(x₁) = E and p → 0 from the right), the exact solution is an Airy function. Matching the WKB forms across x₁ gives the connection:

**第 2 步 — 转折点处的联结公式。** 在左转折点 x₁（其中 V(x₁) = E，p 从右侧趋向 0）附近，精确解为艾里函数。在 x₁ 两侧匹配 WKB 形式给出联结公式：

  Decaying side: C/√κ exp[−∫κ dx]  ↔  Oscillating side: (2C/√p) cos[(1/ℏ)∫_{x₁}^{x} p dx′ − π/4].

The phase shift of −π/4 arises from the asymptotic behavior of the Airy function Ai(z) ~ (1/2)z^{−1/4} exp(−(2/3)z^{3/2}) for z → +∞ and Ai(z) ~ z^{−1/4} sin((2/3)|z|^{3/2} + π/4) for z → −∞.

−π/4 的相移来自艾里函数 Ai(z) 的渐近行为：当 z → +∞ 时 Ai(z) ~ (1/2)z^{−1/4} exp(−(2/3)z^{3/2})；当 z → −∞ 时 Ai(z) ~ z^{−1/4} sin((2/3)|z|^{3/2} + π/4)。

Similarly, at the right turning point x₂, matching gives a phase shift of −π/4 from that end.

类似地，在右转折点 x₂ 处，匹配给出来自该端 −π/4 的相移。

**Step 3 — Impose single-valuedness.** The WKB wavefunction in the interior must match at both ends simultaneously. Working from the left connection formula:

**第 3 步 — 施加单值性条件。** 内部的 WKB 波函数必须同时与两端匹配。从左端联结公式出发：

  ψ ∝ cos[(1/ℏ)∫_{x₁}^{x} p dx′ − π/4].

Working from the right connection formula, the solution from the right must be:

从右端联结公式出发，从右侧得到的解必须为：

  ψ ∝ cos[(1/ℏ)∫_{x}^{x₂} p dx′ − π/4].

Using cos θ = cos(−θ), write the right-derived solution as:

利用 cos θ = cos(−θ)，将右侧推导的解写为：

  ψ ∝ cos[−(1/ℏ)∫_{x}^{x₂} p dx′ + π/4]
       = cos[(1/ℏ)∫_{x₁}^{x} p dx′ − (1/ℏ)∫_{x₁}^{x₂} p dx′ + π/4].

**Step 4 — Matching condition.** For the two expressions to represent the same function (up to an overall sign), their arguments must differ by a multiple of π:

**第 4 步 — 匹配条件。** 为使两个表达式表示同一函数（相差整体符号），其自变量必须相差 π 的整数倍：

  [(1/ℏ)∫_{x₁}^{x} p dx′ − π/4] − [(1/ℏ)∫_{x₁}^{x} p dx′ − (1/ℏ)Φ + π/4] = nπ,

where Φ = ∫_{x₁}^{x₂} p dx. Simplifying:

其中 Φ = ∫_{x₁}^{x₂} p dx。化简：

  (1/ℏ)Φ − π/2 = nπ,   n = 0, 1, 2, …

  (1/ℏ)∫_{x₁}^{x₂} p dx = (n + ½)π.

**Step 5 — Bohr–Sommerfeld condition.** Multiplying both sides by 2ℏ and noting that one full oscillation = 2 × (x₁ to x₂):

**第 5 步 — 玻尔–索末菲条件。** 两边乘以 2ℏ，注意一次完整振荡 = 2 × （x₁ 到 x₂）：

  ∮ p dx = 2∫_{x₁}^{x₂} p dx = (2n + 1)πℏ = (n + ½)h,   n = 0, 1, 2, …

The ½ (the "Maslov correction" from the two π/4 phase shifts at the turning points) is essential: it gives the correct zero-point energy for the harmonic oscillator (n = 0 gives E₀ = ½ℏω, not zero). ∎

其中 ½（来自两个转折点处 π/4 相移的"马斯洛夫修正"）至关重要：它给出谐振子正确的零点能（n = 0 给出 E₀ = ½ℏω，而非零）。∎

**Check — Harmonic oscillator.** For V = ½mω²x², the turning points satisfy ½mω²x₁,₂² = E, so x₁,₂ = ∓√(2E/mω²). The integral is ∫_{x₁}^{x₂} p dx = (πE/ω) (the area of an ellipse in phase space). The Bohr–Sommerfeld condition gives 2(πE/ω) = (n + ½)h, so E = (n + ½)ℏω — exact agreement with the ladder-operator result.

**验证——谐振子。** 对 V = ½mω²x²，转折点满足 ½mω²x₁,₂² = E，故 x₁,₂ = ∓√(2E/mω²)。积分为 ∫_{x₁}^{x₂} p dx = πE/ω（相空间中椭圆的面积）。玻尔–索末菲条件给出 2(πE/ω) = (n + ½)h，故 E = (n + ½)ℏω——与梯形算符结果完全一致。

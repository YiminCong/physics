# Derivations — Module 3.2: Time-Independent Schrödinger Equation
# 推导 — 模块 3.2：定态薛定谔方程

> Companion to [Module 3.2](./module-3.2-time-independent-schrodinger-equation.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 3.2](./module-3.2-time-independent-schrodinger-equation.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Infinite Square Well · 无限深方势阱

**Claim.** For a particle confined to 0 ≤ x ≤ L by an infinite potential, the energy eigenvalues are Eₙ = n²π²ℏ²/(2mL²) with normalized eigenfunctions ψₙ(x) = √(2/L) sin(nπx/L), n = 1, 2, 3, …

**命题。** 对于被无限深势垒约束在 0 ≤ x ≤ L 内的粒子，能量本征值为 Eₙ = n²π²ℏ²/(2mL²)，归一化本征函数为 ψₙ(x) = √(2/L) sin(nπx/L)，n = 1, 2, 3, …

**Step 1 — Set up the equation.** Inside the well V(x) = 0, so the time-independent Schrödinger equation (TISE) Ĥψ = Eψ reads −(ℏ²/2m) ψ″(x) = E ψ(x). Define k² = 2mE/ℏ² (with E > 0, so k is real). The equation becomes ψ″ = −k² ψ — the second-order constant-coefficient ODE of Module 0.3.

**第 1 步 — 建立方程。** 阱内 V(x) = 0，故定态薛定谔方程 Ĥψ = Eψ 为 −(ℏ²/2m) ψ″(x) = E ψ(x)。定义 k² = 2mE/ℏ²（E > 0，故 k 为实数）。方程化为 ψ″ = −k² ψ——即模块 0.3 的二阶常系数常微分方程。

**Step 2 — General solution.** The general solution is ψ(x) = A sin(kx) + B cos(kx), with A, B constants fixed by boundary conditions.

**第 2 步 — 通解。** 通解为 ψ(x) = A sin(kx) + B cos(kx)，常数 A、B 由边界条件确定。

**Step 3 — Boundary conditions.** The wavefunction must be continuous and vanish where the potential is infinite, so ψ(0) = ψ(L) = 0. From ψ(0) = 0: A sin(0) + B cos(0) = B = 0, hence B = 0 and ψ(x) = A sin(kx). From ψ(L) = 0: A sin(kL) = 0. Since A ≠ 0 (else ψ ≡ 0), we need sin(kL) = 0, i.e. kL = nπ for integer n.

**第 3 步 — 边界条件。** 波函数必须连续，且在势能无穷大处为零，故 ψ(0) = ψ(L) = 0。由 ψ(0) = 0：A sin(0) + B cos(0) = B = 0，故 B = 0，ψ(x) = A sin(kx)。由 ψ(L) = 0：A sin(kL) = 0。因 A ≠ 0（否则 ψ ≡ 0），需 sin(kL) = 0，即 kL = nπ，n 为整数。

**Step 4 — Quantization.** Thus kₙ = nπ/L. We take n = 1, 2, 3, … (n = 0 gives ψ ≡ 0; negative n only flips the sign of ψ and adds nothing new). Substituting back into k² = 2mE/ℏ²:

**第 4 步 — 量子化。** 于是 kₙ = nπ/L。取 n = 1, 2, 3, …（n = 0 给出 ψ ≡ 0；负 n 只改变 ψ 的符号，无新解）。代回 k² = 2mE/ℏ²：

  Eₙ = ℏ²kₙ²/(2m) = **n²π²ℏ²/(2mL²)**.

**Step 5 — Normalization.** Require ∫₀ᴸ |ψ|² dx = 1: A² ∫₀ᴸ sin²(nπx/L) dx = A² · (L/2) = 1, using ∫₀ᴸ sin²(nπx/L) dx = L/2. Hence A = √(2/L), giving ψₙ(x) = √(2/L) sin(nπx/L). ∎

**第 5 步 — 归一化。** 要求 ∫₀ᴸ |ψ|² dx = 1：A² ∫₀ᴸ sin²(nπx/L) dx = A² · (L/2) = 1，其中用到 ∫₀ᴸ sin²(nπx/L) dx = L/2。故 A = √(2/L)，得 ψₙ(x) = √(2/L) sin(nπx/L)。∎

---

## B. The Harmonic Oscillator Spectrum via Ladder Operators · 用升降算符求谐振子谱

**Claim.** For Ĥ = p̂²/2m + ½mω²x̂², the spectrum is Eₙ = (n + ½)ℏω, n = 0, 1, 2, …, with a zero-point energy ½ℏω. This is the single most reused derivation in the curriculum (phonons in 4.3, fields in 6.1, 6.5).

**命题。** 对于 Ĥ = p̂²/2m + ½mω²x̂²，能谱为 Eₙ = (n + ½)ℏω，n = 0, 1, 2, …，零点能为 ½ℏω。这是全课程复用最多的推导（4.3 的声子、6.1 与 6.5 的场）。

**Step 1 — Define the ladder operators.** Let

**第 1 步 — 定义升降算符。** 令

  â = √(mω/2ℏ) (x̂ + i p̂/mω),  â† = √(mω/2ℏ) (x̂ − i p̂/mω).

**Step 2 — Their commutator.** Using the canonical commutator [x̂, p̂] = iℏ (proved in Module 3.3),

**第 2 步 — 它们的对易子。** 利用正则对易关系 [x̂, p̂] = iℏ（在模块 3.3 中证明），

  [â, â†] = (mω/2ℏ) [x̂ + ip̂/mω, x̂ − ip̂/mω] = (mω/2ℏ) ( −i/mω [x̂, p̂] + i/mω [p̂, x̂] ) = (mω/2ℏ) · (2/mω)·(ℏ) = 1.

So **[â, â†] = 1**. (Here we used [x̂,x̂]=[p̂,p̂]=0 and [p̂,x̂] = −iℏ.)

故 **[â, â†] = 1**。（这里用到 [x̂,x̂]=[p̂,p̂]=0 与 [p̂,x̂] = −iℏ。）

**Step 3 — Rewrite the Hamiltonian.** Compute â†â = (mω/2ℏ)(x̂ − ip̂/mω)(x̂ + ip̂/mω) = (mω/2ℏ)(x̂² + p̂²/m²ω² + (i/mω)[x̂,p̂]) = (1/ℏω)(p̂²/2m + ½mω²x̂²) − ½. Therefore

**第 3 步 — 改写哈密顿量。** 计算 â†â = (mω/2ℏ)(x̂ − ip̂/mω)(x̂ + ip̂/mω) = (mω/2ℏ)(x̂² + p̂²/m²ω² + (i/mω)[x̂,p̂]) = (1/ℏω)(p̂²/2m + ½mω²x̂²) − ½。因此

  **Ĥ = ℏω(â†â + ½) = ℏω(N̂ + ½)**,  where N̂ ≡ â†â is the **number operator**.

  **Ĥ = ℏω(â†â + ½) = ℏω(N̂ + ½)**，其中 N̂ ≡ â†â 为**数算符**。

**Step 4 — Commutators with N̂.** From [â, â†] = 1: [N̂, â] = [â†â, â] = â†[â,â] + [â†,â]â = −â, and similarly [N̂, â†] = +â†.

**第 4 步 — 与 N̂ 的对易子。** 由 [â, â†] = 1：[N̂, â] = [â†â, â] = â†[â,â] + [â†,â]â = −â，同理 [N̂, â†] = +â†。

**Step 5 — Ladder action.** Let N̂|n⟩ = n|n⟩. Then N̂(â|n⟩) = (âN̂ − â)|n⟩ = (n−1)(â|n⟩): â lowers the eigenvalue by 1. Likewise â†|n⟩ is an eigenstate with eigenvalue (n+1). So â and â† step between levels — hence "ladder" operators.

**第 5 步 — 阶梯作用。** 设 N̂|n⟩ = n|n⟩。则 N̂(â|n⟩) = (âN̂ − â)|n⟩ = (n−1)(â|n⟩)：â 将本征值降低 1。同理 â†|n⟩ 是本征值为 (n+1) 的本征态。故 â、â† 在能级间逐级移动——即"阶梯"算符。

**Step 6 — Spectrum is bounded below.** The norm satisfies ‖â|n⟩‖² = ⟨n|â†â|n⟩ = ⟨n|N̂|n⟩ = n ⟨n|n⟩ ≥ 0, so **n ≥ 0**. Repeated application of â would produce states of ever-lower eigenvalue, eventually negative — a contradiction — unless the chain terminates at a **ground state** |0⟩ with

**第 6 步 — 谱有下界。** 范数满足 ‖â|n⟩‖² = ⟨n|â†â|n⟩ = ⟨n|N̂|n⟩ = n ⟨n|n⟩ ≥ 0，故 **n ≥ 0**。反复作用 â 会产生本征值不断降低、最终为负的态——矛盾——除非阶梯在**基态** |0⟩ 处终止，且

  â|0⟩ = 0.

Then N̂|0⟩ = â†â|0⟩ = 0, so the lowest eigenvalue is n = 0, and all eigenvalues are non-negative integers n = 0, 1, 2, …

于是 N̂|0⟩ = â†â|0⟩ = 0，故最小本征值为 n = 0，所有本征值为非负整数 n = 0, 1, 2, …

**Step 7 — The energies.** Since Ĥ = ℏω(N̂ + ½),

**第 7 步 — 能量。** 由 Ĥ = ℏω(N̂ + ½)，

  **Eₙ = (n + ½)ℏω**,  n = 0, 1, 2, …

The ground-state energy E₀ = ½ℏω ≠ 0 is the **zero-point energy**: a direct consequence of the uncertainty principle (x and p cannot both vanish). ∎

基态能 E₀ = ½ℏω ≠ 0 即**零点能**：这是不确定性原理的直接后果（x 与 p 不能同时为零）。∎

**Step 8 — Normalized ladder & ground-state wavefunction.** From the norms, â|n⟩ = √n |n−1⟩ and â†|n⟩ = √(n+1) |n+1⟩, so |n⟩ = (â†)ⁿ/√(n!) |0⟩. Writing â|0⟩ = 0 in position space with p̂ = −iℏ d/dx gives (x + (ℏ/mω) d/dx) ψ₀ = 0, a first-order ODE whose solution is the **Gaussian ground state** ψ₀(x) ∝ exp(−mωx²/2ℏ) (normalized using the Gaussian integral of Module 0.1).

**第 8 步 — 归一化阶梯与基态波函数。** 由范数得 â|n⟩ = √n |n−1⟩、â†|n⟩ = √(n+1) |n+1⟩，故 |n⟩ = (â†)ⁿ/√(n!) |0⟩。在坐标表象中（p̂ = −iℏ d/dx）将 â|0⟩ = 0 写出，得 (x + (ℏ/mω) d/dx) ψ₀ = 0，这是一阶常微分方程，其解为**高斯基态** ψ₀(x) ∝ exp(−mωx²/2ℏ)（用模块 0.1 的高斯积分归一化）。

---

*This is a sample derivation document. If the depth and bilingual format are right, the same treatment can be produced for every formula across the curriculum.*

*这是一份样板推导文档。若深度与双语格式合适，可为课程中的每一个公式生成相同处理。*

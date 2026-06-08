# Derivations — Module 6.4: Path Integrals & Field Theory
# 推导 — 模块 6.4：路径积分与场论

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 6.4](./module-6.4-path-integrals.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 6.4](./module-6.4-path-integrals.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Derivation of the Feynman Path Integral by Time-Slicing · 通过时间切片推导费曼路径积分

**Claim.** The quantum amplitude for a particle to propagate from xᵢ to x_f in time T is

  K(x_f, T; xᵢ, 0) = ⟨x_f| e^{−iĤT/ℏ} |xᵢ⟩ = ∫ D[x(t)] e^{iS[x]/ℏ},

where S[x] = ∫₀^T dt [½mẋ² − V(x)] is the classical action and D[x(t)] is the functional measure over all paths with x(0) = xᵢ, x(T) = x_f.

**命题。** 粒子在时间 T 内从 xᵢ 传播到 x_f 的量子幅度为

  K(x_f, T; xᵢ, 0) = ⟨x_f| e^{−iĤT/ℏ} |xᵢ⟩ = ∫ D[x(t)] e^{iS[x]/ℏ}，

其中 S[x] = ∫₀^T dt [½mẋ² − V(x)] 是经典作用量，D[x(t)] 是满足 x(0) = xᵢ、x(T) = x_f 的所有路径的泛函测度。

**Step 1 — Slice the time interval.** Divide [0, T] into N equal subintervals of length ε = T/N. Write the propagator as a product of short-time propagators using the composition (semigroup) property of the evolution operator:

  e^{−iĤT/ℏ} = (e^{−iĤε/ℏ})^N = e^{−iĤε/ℏ} · e^{−iĤε/ℏ} · … · e^{−iĤε/ℏ}  (N factors).

**第 1 步 — 切分时间区间。** 将 [0, T] 划分为 N 个等长子区间，每段长度 ε = T/N。利用演化算符的复合（半群）性质，将传播子写成短时传播子之积：

  e^{−iĤT/ℏ} = (e^{−iĤε/ℏ})^N = e^{−iĤε/ℏ} · e^{−iĤε/ℏ} · … · e^{−iĤε/ℏ}（N 个因子）。

**Step 2 — Insert N−1 complete sets of position eigenstates.** Between each pair of adjacent factors, insert 1 = ∫ dx_j |x_j⟩⟨x_j|:

  ⟨x_f| e^{−iĤT/ℏ} |xᵢ⟩ = ∫ dx₁ dx₂ … dx_{N−1} ∏_{j=0}^{N−1} ⟨x_{j+1}| e^{−iĤε/ℏ} |x_j⟩,

where x₀ ≡ xᵢ and x_N ≡ x_f.

**第 2 步 — 插入 N−1 个完备位置本征态集。** 在每对相邻因子之间，插入 1 = ∫ dx_j |x_j⟩⟨x_j|：

  ⟨x_f| e^{−iĤT/ℏ} |xᵢ⟩ = ∫ dx₁ dx₂ … dx_{N−1} ∏_{j=0}^{N−1} ⟨x_{j+1}| e^{−iĤε/ℏ} |x_j⟩，

其中 x₀ ≡ xᵢ，x_N ≡ x_f。

**Step 3 — Evaluate a single short-time matrix element.** For Ĥ = p̂²/2m + V(x̂) and small ε, use the Trotter product formula e^{−iĤε/ℏ} ≈ e^{−ip̂²ε/2mℏ} e^{−iV(x̂)ε/ℏ} + O(ε²). Insert a resolution of the identity in momentum space 1 = ∫ dp/(2πℏ) |p⟩⟨p|:

  ⟨x_{j+1}| e^{−iĤε/ℏ} |x_j⟩ ≈ ∫ dp/(2πℏ) ⟨x_{j+1}|p⟩ e^{−ip²ε/2mℏ} ⟨p|x_j⟩ e^{−iV(x_j)ε/ℏ}.

Using ⟨x|p⟩ = e^{ipx/ℏ}/√(2πℏ):

  = ∫ dp/(2πℏ) e^{ip(x_{j+1} − x_j)/ℏ} e^{−ip²ε/2mℏ} e^{−iV(x_j)ε/ℏ}.

**第 3 步 — 计算单个短时矩阵元。** 对于 Ĥ = p̂²/2m + V(x̂) 和小 ε，使用 Trotter 乘积公式 e^{−iĤε/ℏ} ≈ e^{−ip̂²ε/2mℏ} e^{−iV(x̂)ε/ℏ} + O(ε²)。在动量空间插入单位分解 1 = ∫ dp/(2πℏ) |p⟩⟨p|：

  ⟨x_{j+1}| e^{−iĤε/ℏ} |x_j⟩ ≈ ∫ dp/(2πℏ) ⟨x_{j+1}|p⟩ e^{−ip²ε/2mℏ} ⟨p|x_j⟩ e^{−iV(x_j)ε/ℏ}。

利用 ⟨x|p⟩ = e^{ipx/ℏ}/√(2πℏ)：

  = ∫ dp/(2πℏ) e^{ip(x_{j+1} − x_j)/ℏ} e^{−ip²ε/2mℏ} e^{−iV(x_j)ε/ℏ}。

**Step 4 — Perform the Gaussian momentum integral.** The integral over p is of the form ∫ dp e^{ipΔx/ℏ − ip²ε/2mℏ} where Δx = x_{j+1} − x_j. Complete the square: let p' = p − mΔx/ε, so that

  ipΔx/ℏ − ip²ε/2mℏ = im(Δx)²/2ℏε − ip'²ε/2mℏ.

The Gaussian integral ∫ dp' e^{−ip'²ε/2mℏ} = √(2πmℏ/iε) (choosing the branch with Im(√) > 0 for convergence). Therefore

  ⟨x_{j+1}| e^{−iĤε/ℏ} |x_j⟩ ≈ √(m/2πiℏε) exp(i ε/ℏ [m(Δx/ε)²/2 − V(x_j)]).

**第 4 步 — 执行高斯动量积分。** 对 p 的积分形如 ∫ dp e^{ipΔx/ℏ − ip²ε/2mℏ}，其中 Δx = x_{j+1} − x_j。配方：令 p' = p − mΔx/ε，则

  ipΔx/ℏ − ip²ε/2mℏ = im(Δx)²/2ℏε − ip'²ε/2mℏ。

高斯积分 ∫ dp' e^{−ip'²ε/2mℏ} = √(2πmℏ/iε)（选择 Im(√) > 0 的分支以保证收敛）。因此

  ⟨x_{j+1}| e^{−iĤε/ℏ} |x_j⟩ ≈ √(m/2πiℏε) exp(i ε/ℏ [m(Δx/ε)²/2 − V(x_j)])。

**Step 5 — Recognize the discrete action and take N → ∞.** The exponent is

  i/ℏ Σ_{j=0}^{N−1} ε [½m(Δx_j/ε)² − V(x_j)]  →  iS[x]/ℏ  as  ε → 0,

where S[x] = ∫₀^T dt [½mẋ² − V(x(t))] is the classical action. The product of prefactors (√(m/2πiℏε))^N defines the functional measure D[x(t)]:

  ∫ D[x(t)] e^{iS[x]/ℏ} ≡ lim_{N→∞} (m/2πiℏε)^{N/2} ∫ dx₁ … dx_{N−1} e^{i/ℏ Σ_j ε L(x_j, ẋ_j)}.

The full result is

  ⟨x_f| e^{−iĤT/ℏ} |xᵢ⟩ = ∫ D[x(t)] e^{iS[x]/ℏ}.  ∎

**第 5 步 — 识别离散作用量并取 N → ∞。** 指数为

  i/ℏ Σ_{j=0}^{N−1} ε [½m(Δx_j/ε)² − V(x_j)]  →  iS[x]/ℏ，当 ε → 0 时，

其中 S[x] = ∫₀^T dt [½mẋ² − V(x(t))] 是经典作用量。前因子之积 (√(m/2πiℏε))^N 定义了泛函测度 D[x(t)]：

  ∫ D[x(t)] e^{iS[x]/ℏ} ≡ lim_{N→∞} (m/2πiℏε)^{N/2} ∫ dx₁ … dx_{N−1} e^{i/ℏ Σ_j ε L(x_j, ẋ_j)}。

完整结果为

  ⟨x_f| e^{−iĤT/ℏ} |xᵢ⟩ = ∫ D[x(t)] e^{iS[x]/ℏ}。  ∎

---

## B. The Classical Limit and the Stationary-Phase Condition · 经典极限与驻相条件

**Claim.** In the limit ℏ → 0, the path integral is dominated by the path x_{cl}(t) that extremizes the action, i.e. the classical trajectory satisfying δS[x_{cl}] = 0 (Hamilton's principle, Module 1.3).

**命题。** 在 ℏ → 0 的极限下，路径积分由使作用量取极值的路径 x_{cl}(t) 主导，即满足 δS[x_{cl}] = 0 的经典轨迹（哈密顿原理，模块 1.3）。

**Step 1 — Expand S around the classical path.** Write x(t) = x_{cl}(t) + η(t), where η(0) = η(T) = 0 (fixed endpoints). Taylor expand:

  S[x_{cl} + η] = S[x_{cl}] + δS[x_{cl}](η) + ½ δ²S[x_{cl}](η,η) + O(η³).

The first-order term δS[x_{cl}](η) = ∫₀^T dt (∂L/∂x − d/dt ∂L/∂ẋ)|_{x_{cl}} η(t) vanishes by the classical equation of motion (Euler–Lagrange equation, Module 1.3). The leading correction is the second-order (Gaussian) fluctuation.

**第 1 步 — 在经典路径附近展开 S。** 写出 x(t) = x_{cl}(t) + η(t)，其中 η(0) = η(T) = 0（固定端点）。泰勒展开：

  S[x_{cl} + η] = S[x_{cl}] + δS[x_{cl}](η) + ½ δ²S[x_{cl}](η,η) + O(η³)。

一阶项 δS[x_{cl}](η) = ∫₀^T dt (∂L/∂x − d/dt ∂L/∂ẋ)|_{x_{cl}} η(t) 由经典运动方程（欧拉–拉格朗日方程，模块 1.3）消失。领头修正是二阶（高斯）涨落。

**Step 2 — Stationary phase for oscillatory integrals.** In the path integral ∫ D[x] e^{iS[x]/ℏ}, each path contributes a phase e^{iS/ℏ}. As ℏ → 0, the phase oscillates rapidly for paths far from x_{cl}. These rapid oscillations produce cancellation among nearby paths (destructive interference). Only paths near x_{cl}, where the phase is stationary (δS = 0), contribute coherently (constructive interference). This is the stationary-phase (or saddle-point) approximation — the quantum-mechanical version of classical mechanics.

**第 2 步 — 振荡积分的驻相。** 在路径积分 ∫ D[x] e^{iS[x]/ℏ} 中，每条路径贡献相位 e^{iS/ℏ}。当 ℏ → 0 时，远离 x_{cl} 的路径相位振荡剧烈。这些快速振荡导致邻近路径之间相消干涉。只有 x_{cl} 附近相位驻定（δS = 0）的路径相长干涉。这是驻相（或鞍点）近似——经典力学的量子力学版本。

**Step 3 — Leading result and quantum corrections.** At lowest order in ℏ:

  K(x_f, T; xᵢ, 0) ≈ C e^{iS[x_{cl}]/ℏ},

where C comes from the Gaussian integral over η (the fluctuation determinant). The quantum corrections are suppressed by powers of ℏ. The classical limit ℏ → 0 recovers Newton's second law and Hamilton's equations precisely because the stationary condition δS = 0 is Hamilton's principle. ∎

**第 3 步 — 领头结果与量子修正。** 在 ℏ 的最低阶：

  K(x_f, T; xᵢ, 0) ≈ C e^{iS[x_{cl}]/ℏ}，

其中 C 来自对 η 的高斯积分（涨落行列式）。量子修正被 ℏ 的幂次压制。经典极限 ℏ → 0 精确还原牛顿第二定律和哈密顿方程，正是因为驻定条件 δS = 0 就是哈密顿原理。∎

---

## C. The Imaginary-Time Path Integral and the Partition Function · 虚时路径积分与配分函数

**Claim.** Under the Wick rotation t → −iτ (imaginary time), the quantum partition function becomes a Euclidean functional integral:

  Z = Tr e^{−βĤ} = ∫_{periodic} D[φ] e^{−S_E[φ]/ℏ},

where S_E is the Euclidean action and the fields obey periodic (bosons) or antiperiodic (fermions) boundary conditions in τ ∈ [0, ℏβ].

**命题。** 在维克转动 t → −iτ（虚时间）下，量子配分函数变为欧几里得泛函积分：

  Z = Tr e^{−βĤ} = ∫_{periodic} D[φ] e^{−S_E[φ]/ℏ}，

其中 S_E 是欧几里得作用量，场在 τ ∈ [0, ℏβ] 中满足周期（玻色子）或反周期（费米子）边界条件。

**Step 1 — Relate the partition function to the propagator.** The partition function is Z = Tr e^{−βĤ} = ∫ dx ⟨x|e^{−βĤ}|x⟩. Comparing with the propagator K(x_f, T; xᵢ, 0) = ⟨x_f|e^{−iĤT/ℏ}|xᵢ⟩, we see that setting T = −iℏβ (i.e. t → −iτ with T → ℏβ) and integrating over x_f = xᵢ = x gives

  Z = ∫ dx K(x, −iℏβ; x, 0).

**第 1 步 — 将配分函数与传播子联系起来。** 配分函数为 Z = Tr e^{−βĤ} = ∫ dx ⟨x|e^{−βĤ}|x⟩。与传播子 K(x_f, T; xᵢ, 0) = ⟨x_f|e^{−iĤT/ℏ}|xᵢ⟩ 比较，令 T = −iℏβ（即 t → −iτ，T → ℏβ），并对 x_f = xᵢ = x 积分，得

  Z = ∫ dx K(x, −iℏβ; x, 0)。

**Step 2 — Wick rotate the time-slicing derivation.** In the time-slicing derivation (Section A), replace t_j → −iτ_j. The step size becomes ε → −iΔτ (with Δτ = ℏβ/N > 0). The Lagrangian changes:

  i S/ℏ = i/ℏ ∫ dt [½m(dx/dt)² − V] → i/ℏ ∫ (−idτ) [½m(dx/d(−iτ))² − V]
         = −1/ℏ ∫₀^{ℏβ} dτ [½m(dx/dτ)² + V(x)] = −S_E[x]/ℏ,

where S_E[x] = ∫₀^{ℏβ} dτ [½m(dx/dτ)² + V(x)] is the **Euclidean action**. The oscillatory weight e^{iS/ℏ} becomes the real Boltzmann weight e^{−S_E/ℏ}.

**第 2 步 — 对时间切片推导进行维克转动。** 在时间切片推导（第 A 节）中，替换 t_j → −iτ_j。步长变为 ε → −iΔτ（Δτ = ℏβ/N > 0）。拉格朗日量改变：

  i S/ℏ = i/ℏ ∫ dt [½m(dx/dt)² − V] → i/ℏ ∫ (−idτ) [½m(dx/d(−iτ))² − V]
         = −1/ℏ ∫₀^{ℏβ} dτ [½m(dx/dτ)² + V(x)] = −S_E[x]/ℏ，

其中 S_E[x] = ∫₀^{ℏβ} dτ [½m(dx/dτ)² + V(x)] 是**欧几里得作用量**。振荡权重 e^{iS/ℏ} 变为实的玻尔兹曼权重 e^{−S_E/ℏ}。

**Step 3 — Impose boundary conditions for bosons.** The trace ∫ dx ⟨x|…|x⟩ means x(ℏβ) = x(0): the path closes on itself. In a field theory, the bosonic field satisfies φ(x, τ+ℏβ) = φ(x, τ) — **periodic boundary conditions**. The Matsubara (imaginary-time) frequencies are ω_n = 2πn/(ℏβ) for bosons (n ∈ ℤ), which quantize the frequency spectrum due to the periodicity. Therefore:

  Z = ∫_{φ(τ+ℏβ) = φ(τ)} D[φ] e^{−S_E[φ]/ℏ}.  ∎

**第 3 步 — 对玻色子施加边界条件。** 迹 ∫ dx ⟨x|…|x⟩ 意味着 x(ℏβ) = x(0)：路径自身封闭。在场论中，玻色子场满足 φ(x, τ+ℏβ) = φ(x, τ)——**周期边界条件**。松原（虚时）频率对玻色子为 ω_n = 2πn/(ℏβ)（n ∈ ℤ），由周期性量子化频率谱。因此：

  Z = ∫_{φ(τ+ℏβ) = φ(τ)} D[φ] e^{−S_E[φ]/ℏ}。  ∎

**Step 4 — Antiperiodic boundary conditions for fermions.** Fermionic fields ψ(τ) are Grassmann-valued (anticommuting), and the trace involves an extra minus sign from the anticommutation: Tr e^{−βĤ} = ∫ dψ̄ dψ ⟨ψ|e^{−βĤ}|−ψ⟩ (the coherent-state path integral). The minus sign in |−ψ⟩ gives the **antiperiodic** boundary condition ψ(τ+ℏβ) = −ψ(τ), and fermionic Matsubara frequencies ω_n = (2n+1)π/(ℏβ) (n ∈ ℤ) — odd multiples of π/ℏβ. The partition function is

  Z = ∫_{ψ(τ+ℏβ) = −ψ(τ)} D[ψ̄, ψ] e^{−S_E[ψ̄,ψ]/ℏ}.

**第 4 步 — 费米子的反周期边界条件。** 费米子场 ψ(τ) 是 Grassmann 值的（反对易），迹涉及来自反对易的额外负号：Tr e^{−βĤ} = ∫ dψ̄ dψ ⟨ψ|e^{−βĤ}|−ψ⟩（相干态路径积分）。|−ψ⟩ 中的负号给出**反周期**边界条件 ψ(τ+ℏβ) = −ψ(τ)，以及费米子松原频率 ω_n = (2n+1)π/(ℏβ)（n ∈ ℤ）——π/ℏβ 的奇数倍。配分函数为

  Z = ∫_{ψ(τ+ℏβ) = −ψ(τ)} D[ψ̄, ψ] e^{−S_E[ψ̄,ψ]/ℏ}。

**Step 5 — Physical interpretation.** The Euclidean path integral Z = ∫ D[φ] e^{−S_E/ℏ} is formally identical to a classical statistical mechanics partition function Z_{cl} = ∫ D[φ] e^{−βF[φ]} in d+1 dimensions, with ℏβ playing the role of the inverse temperature times the (d+1)-th extent. This is the quantum-to-classical mapping: a d-dimensional quantum system at temperature T is equivalent to a (d+1)-dimensional classical system. In particular, T = 0 gives an infinite imaginary-time extent and a d+1-dimensional classical system. ∎

**第 5 步 — 物理诠释。** 欧几里得路径积分 Z = ∫ D[φ] e^{−S_E/ℏ} 在形式上与 d+1 维的经典统计力学配分函数 Z_{cl} = ∫ D[φ] e^{−βF[φ]} 完全相同，ℏβ 扮演逆温度乘以第 (d+1) 方向范围的角色。这是量子到经典的映射：温度为 T 的 d 维量子系统等价于 (d+1) 维经典系统。特别地，T = 0 给出无限虚时范围和 d+1 维经典系统。∎

---

*The time-slicing derivation shows that the path integral is not an ansatz but a theorem: it follows by repeated insertion of resolutions of identity, followed by a Gaussian momentum integral. The Wick rotation then reveals the deep formal identity between quantum statistical mechanics and classical statistical field theory.*

*时间切片推导表明，路径积分不是一个猜测，而是一个定理：它由反复插入单位分解、再进行高斯动量积分而得到。维克转动随即揭示了量子统计力学与经典统计场论之间深刻的形式等同性。*

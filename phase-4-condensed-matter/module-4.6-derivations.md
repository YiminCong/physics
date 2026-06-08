# Derivations — Module 4.6: Magnetism & Spin Waves
# 推导 — 模块 4.6：磁性与自旋波

> Companion to [Module 4.6](./module-4.6-magnetism-and-spin-waves.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 4.6](./module-4.6-magnetism-and-spin-waves.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Curie Law from the Paramagnet's Partition Function · 顺磁体配分函数推导居里定律

**Claim.** For N independent spin-½ magnetic moments in an applied field B, the susceptibility is χ = C/T with C = n μ₀ g² μ_B² / (4 k_B).

**命题。** 对于外加磁场 B 中的 N 个独立自旋-½ 磁矩，磁化率为 χ = C/T，其中 C = n μ₀ g² μ_B² / (4 k_B)。

**Step 1 — Single-spin energy levels.** A spin-½ moment in field B (along z) has two energy levels: E_± = ∓ (1/2) g μ_B B, corresponding to spin up (m_s = +½, lower energy for g > 0) and spin down (m_s = −½).

**第 1 步 — 单自旋能级。** 磁场 B（沿 z 方向）中的自旋-½ 磁矩有两个能级：E_± = ∓ (1/2) g μ_B B，对应自旋向上（m_s = +½，能量较低，g > 0）和自旋向下（m_s = −½）。

**Step 2 — Single-spin partition function.** Define x = g μ_B B / (2 k_B T). The single-spin partition function is

**第 2 步 — 单自旋配分函数。** 定义 x = g μ_B B / (2 k_B T)。单自旋配分函数为

  z = e^x + e^{−x} = 2 cosh(x).

**Step 3 — Average magnetic moment.** The average z-component of the magnetic moment is

**第 3 步 — 平均磁矩。** 磁矩 z 分量的平均值为

  ⟨μ_z⟩ = k_B T (∂ ln z / ∂B) = (1/2) g μ_B (e^x − e^{−x}) / (e^x + e^{−x}) = (1/2) g μ_B tanh(x).

**Step 4 — High-temperature (weak-field) limit.** For x = g μ_B B / (2 k_B T) ≪ 1 (the Curie regime: weak field or high T):

**第 4 步 — 高温（弱场）极限。** 当 x = g μ_B B / (2 k_B T) ≪ 1 时（居里区：弱场或高温）：

  tanh(x) ≈ x,  so  ⟨μ_z⟩ ≈ (g μ_B)² B / (4 k_B T).

**Step 5 — Magnetization and susceptibility.** With n moments per unit volume:

**第 5 步 — 磁化强度与磁化率。** 设单位体积有 n 个磁矩：

  M = n ⟨μ_z⟩ = n g² μ_B² B / (4 k_B T).

Since M = χ/μ₀ · B in SI (or χ = μ₀ M / B):

  **χ = μ₀ n g² μ_B² / (4 k_B T) = C/T.**

For general spin S the two-level formula generalizes to ⟨μ_z⟩ = g μ_B S B_S(x) where B_S is the Brillouin function, and the high-T expansion gives C = n μ₀ g² μ_B² S(S+1) / (3 k_B). ∎

由于 M = χ/μ₀ · B（SI 制）（或 χ = μ₀ M / B）：

  **χ = μ₀ n g² μ_B² / (4 k_B T) = C/T。**

对于一般自旋 S，两能级公式推广为 ⟨μ_z⟩ = g μ_B S B_S(x)，其中 B_S 是布里渊函数，高温展开给出 C = n μ₀ g² μ_B² S(S+1) / (3 k_B)。∎

---

## B. Mean-Field T_c and Spontaneous Magnetization · 平均场 T_c 与自发磁化强度

**Claim.** In mean-field theory of the Heisenberg ferromagnet: (i) T_c = z J S(S+1) / (3 k_B), (ii) for T < T_c the spontaneous magnetization near T_c grows as m ∝ (T_c − T)^{1/2}, and (iii) the susceptibility above T_c obeys χ = C/(T − T_c).

**命题。** 在海森堡铁磁体的平均场理论中：(i) T_c = z J S(S+1) / (3 k_B)，(ii) 对于 T < T_c，T_c 附近的自发磁化强度增长为 m ∝ (T_c − T)^{1/2}，(iii) T_c 以上磁化率满足 χ = C/(T − T_c)。

**Step 1 — Mean-field approximation.** Replace the exchange interaction on site i from its z neighbours by an effective field. The exact term J Σ_j S_i · S_j becomes S_i · (J Σ_j ⟨S_j⟩) = S_i · (z J ⟨S⟩). Writing M = n g μ_B ⟨S^z⟩ for the magnetization, the effective field on each spin is

**第 1 步 — 平均场近似。** 将格点 i 处来自 z 个邻居的交换相互作用替换为有效场。精确项 J Σ_j S_i · S_j 变为 S_i · (J Σ_j ⟨S_j⟩) = S_i · (z J ⟨S⟩)。将磁化强度写为 M = n g μ_B ⟨S^z⟩，每个自旋上的有效场为

  B_eff = B_applied + λ M,   λ = 2 z J / (n g² μ_B²)

where the factor of 2 absorbs the double-counting in the exchange sum.

其中因子 2 吸收了交换求和中的重复计数。

**Step 2 — Self-consistency equation.** The magnetization of a spin-S system in field B_eff at temperature T is

**第 2 步 — 自洽方程。** 自旋 S 系统在温度 T、磁场 B_eff 中的磁化强度为

  M = M_sat · B_S(g μ_B S B_eff / k_B T)

where M_sat = n g μ_B S is the saturation magnetization and B_S is the Brillouin function. Substituting B_eff = λ M gives the self-consistency equation for M.

其中 M_sat = n g μ_B S 是饱和磁化强度，B_S 是布里渊函数。代入 B_eff = λ M 得到 M 的自洽方程。

**Step 3 — Finding T_c.** For small M (near the transition), use the small-argument expansion B_S(y) ≈ (S+1)y/(3S). The self-consistency equation becomes

**第 3 步 — 求 T_c。** 对于小 M（相变附近），使用小宗量展开 B_S(y) ≈ (S+1)y/(3S)。自洽方程变为

  M ≈ M_sat · (S+1)/(3S) · g μ_B S λ M / (k_B T) = M · [n g² μ_B² S(S+1) λ / (3 k_B T)].

A non-trivial solution M ≠ 0 exists only when the bracket equals 1, defining

  **T_c = n g² μ_B² S(S+1) λ / (3 k_B) = z J S(S+1) / (3 k_B).**

非平凡解 M ≠ 0 仅在括号等于 1 时存在，定义了

  **T_c = n g² μ_B² S(S+1) λ / (3 k_B) = z J S(S+1) / (3 k_B)。**

**Step 4 — Spontaneous magnetization near T_c.** Expand B_S to the next order: B_S(y) ≈ (S+1)y/(3S) − b y³ + … where b > 0. Writing M = M_sat m (m the reduced magnetization) and expanding the self-consistency equation:

**第 4 步 — T_c 附近的自发磁化强度。** 将 B_S 展开到下一阶：B_S(y) ≈ (S+1)y/(3S) − b y³ + …，其中 b > 0。令 M = M_sat m（m 为约化磁化强度），展开自洽方程：

  m ≈ (T_c/T) m − (T_c/T)³ A m³

where A > 0. For T → T_c from below, T ≈ T_c, so the linear terms give (T_c/T − 1) m ≈ A m³, hence

其中 A > 0。当 T 从下方趋近 T_c 时，T ≈ T_c，线性项给出 (T_c/T − 1) m ≈ A m³，因此

  m² ≈ (T_c − T) / (A T_c),  so  **m ∝ (T_c − T)^{1/2}.** ∎

**Step 5 — Curie–Weiss law above T_c.** For T > T_c with B_applied ≠ 0, the small-M expansion gives M = C(B_applied + λ M)/T, hence M(T − Cλ) = CB_applied, giving

**第 5 步 — T_c 以上的居里–魏斯定律。** 对 T > T_c 且 B_applied ≠ 0，小 M 展开给出 M = C(B_applied + λ M)/T，故 M(T − Cλ) = CB_applied，得

  **χ = M/B_applied = C/(T − T_c)** with T_c = Cλ. ∎

---

## C. Magnon Dispersion from the Heisenberg Model (Holstein–Primakoff) · 海森堡模型的磁振子色散（Holstein–Primakoff）

**Claim.** For the ferromagnetic Heisenberg chain (and its 3D generalisation), linearised spin-wave theory gives ω(k) = (2JS/ℏ) Σ_δ (1 − cos k·δ), which reduces to ω ∝ k² at small k.

**命题。** 对于铁磁海森堡链（及其三维推广），线性化自旋波理论给出 ω(k) = (2JS/ℏ) Σ_δ (1 − cos k·δ)，在小 k 时化为 ω ∝ k²。

**Step 1 — Heisenberg Hamiltonian.** Take H = −J Σ_{⟨i,j⟩} S_i · S_j with J > 0. In the ground state all spins point along +z with eigenvalue S. Write S_i^z = S − a_i†a_i where a_i, a_i† are bosonic deviation operators (Holstein–Primakoff to lowest order in 1/S):

**第 1 步 — 海森堡哈密顿量。** 取 H = −J Σ_{⟨i,j⟩} S_i · S_j，J > 0。基态中所有自旋沿 +z 方向，本征值为 S。令 S_i^z = S − a_i†a_i，其中 a_i、a_i† 是玻色偏离算符（Holstein–Primakoff 展开到 1/S 的最低阶）：

  S_i^+ ≈ √(2S) a_i,   S_i^− ≈ √(2S) a_i†.

**Step 2 — Expand the Hamiltonian.** Writing S_i · S_j = S_i^z S_j^z + ½(S_i^+ S_j^− + S_i^− S_j^+) and expanding to quadratic order in a, a†:

**第 2 步 — 展开哈密顿量。** 写出 S_i · S_j = S_i^z S_j^z + ½(S_i^+ S_j^− + S_i^− S_j^+) 并展开到 a、a† 的二次阶：

  H ≈ const + J S Σ_{⟨i,j⟩} (a_i†a_i + a_j†a_j − a_i†a_j − a_i a_j†).

The constant is the ground-state energy −J z N S².

常数项为基态能量 −J z N S²。

**Step 3 — Fourier transform.** Define a_k = (1/√N) Σ_i e^{ik·r_i} a_i. The quadratic Hamiltonian diagonalises:

**第 3 步 — 傅里叶变换。** 定义 a_k = (1/√N) Σ_i e^{ik·r_i} a_i。二次哈密顿量对角化为：

  H = Σ_k ℏ ω_k (a_k†a_k + ½) + const

where the magnon frequency is

磁振子频率为

  ℏ ω_k = 2 J S Σ_δ (1 − cos k·δ).

Here the sum runs over nearest-neighbour vectors δ of the lattice.

此处求和遍及格子的近邻矢量 δ。

**Step 4 — Small-k limit.** For small k expand cos k·δ ≈ 1 − (k·δ)²/2 + …:

**第 4 步 — 小 k 极限。** 对小 k 展开 cos k·δ ≈ 1 − (k·δ)²/2 + …：

  ℏ ω_k ≈ J S Σ_δ (k·δ)² = J S k² Σ_δ δ_z² (for k along z, cubic symmetry)

so **ω(k) ∝ k²**, quadratic — characteristic of a ferromagnet and distinct from the linear ω ∝ k of phonons. ∎

故 **ω(k) ∝ k²**，二次关系——铁磁体的特征，与声子线性 ω ∝ k 不同。∎

---

## D. Bloch T^{3/2} Magnetization Law · 布洛赫 T^{3/2} 磁化定律

**Claim.** At low temperature T ≪ T_c, the reduction in magnetization due to thermally excited magnons is ΔM/M(0) ∝ T^{3/2}.

**命题。** 在低温 T ≪ T_c 时，热激发磁振子引起的磁化强度减少为 ΔM/M(0) ∝ T^{3/2}。

**Step 1 — Magnetization and magnon number.** Each magnon carries spin −ℏ relative to the ferromagnetic ground state. The reduction in magnetization per unit volume is

**第 1 步 — 磁化强度与磁振子数。** 每个磁振子相对于铁磁基态携带自旋 −ℏ。单位体积磁化强度的减少量为

  ΔM = (g μ_B / V) Σ_k ⟨a_k†a_k⟩ = (g μ_B) ∫ D(ω) n_BE(ω, T) dω

where n_BE(ω, T) = 1/(e^{ℏω/k_BT} − 1) is the Bose–Einstein distribution.

其中 n_BE(ω, T) = 1/(e^{ℏω/k_BT} − 1) 是玻色–爱因斯坦分布。

**Step 2 — Density of states.** For ω = D k² (D = 2JS/ℏ × const), the magnon density of states in 3D is

**第 2 步 — 态密度。** 对于 ω = D k²（D = 2JS/ℏ × 常数），三维磁振子的态密度为

  D(ω) = (1/(4π²)) (1/D)^{3/2} ω^{1/2}.

This ω^{1/2} dependence is the key step (compare to the phonon D(ω) ∝ ω² for 3D acoustic branches).

这个 ω^{1/2} 依赖关系是关键步骤（与三维声学支声子的 D(ω) ∝ ω² 对比）。

**Step 3 — The integral.** At low T, the upper limit of the integral can be taken to infinity (few magnons at T ≪ T_c):

**第 3 步 — 积分。** 在低温时，积分上限可取为无穷（T ≪ T_c 时磁振子极少）：

  ΔM ∝ ∫_0^∞ ω^{1/2} / (e^{ℏω/k_BT} − 1) dω.

Substitute u = ℏω/(k_B T):

代换 u = ℏω/(k_B T)：

  ΔM ∝ (k_B T / ℏ)^{3/2} ∫_0^∞ u^{1/2} / (e^u − 1) du = (k_B T / ℏ)^{3/2} · Γ(3/2) · ζ(3/2).

The integral ∫_0^∞ u^{1/2}/(e^u − 1) du = Γ(3/2) ζ(3/2) = (√π/2) ζ(3/2) is a pure number ≈ 2.315.

积分 ∫_0^∞ u^{1/2}/(e^u − 1) du = Γ(3/2) ζ(3/2) = (√π/2) ζ(3/2) 是纯数 ≈ 2.315。

**Step 4 — Result.** Therefore

**第 4 步 — 结果。** 因此

  **ΔM / M(0) = A T^{3/2}**,   A = (g μ_B / M(0)) · (k_B/ℏ)^{3/2} · Γ(3/2) ζ(3/2) / (4π² D^{3/2}).

The T^{3/2} power arises from combining the ω^{1/2} density of states with the k^2 dispersion in three dimensions; it is a direct signature of ferromagnetic spin waves and one of the clearest low-temperature experimental probes of magnon physics. ∎

T^{3/2} 幂次源于三维中 ω^{1/2} 态密度与 k² 色散的组合；它是铁磁自旋波的直接标志，也是磁振子物理最清晰的低温实验探针之一。∎

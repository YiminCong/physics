# Derivations — Module 9.2: Atomic & Molecular Physics
# 推导 — 模块 9.2：原子与分子物理

> Companion to [Module 9.2](./module-9.2-atomic-and-molecular-physics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 9.2](./module-9.2-atomic-and-molecular-physics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Fine-Structure Spin–Orbit Energy Shift · 精细结构自旋–轨道能量移动

**Claim.** For an electron in a central-field potential U(r) with orbital angular momentum L and spin S, the spin–orbit interaction is H_SO = A(L · S) with coupling constant A = (1/2m²c²) (1/r)(dU/dr). This lifts the (2L+1)(2S+1)-fold degeneracy of the LS term, shifting the J-level by:

  E_SO(J) = (A/2)[J(J+1) − L(L+1) − S(S+1)].

The spacing between adjacent J and J+1 levels is ΔE = AJ (Landé interval rule).

**命题。** 对于中心场势 U(r) 中具有轨道角动量 L 和自旋 S 的电子，自旋–轨道相互作用为 H_SO = A(L · S)，耦合常数 A = (1/2m²c²) (1/r)(dU/dr)。这消除 LS 谱项的 (2L+1)(2S+1) 重简并，将 J 能级移动：

  E_SO(J) = (A/2)[J(J+1) − L(L+1) − S(S+1)]。

相邻 J 与 J+1 能级之间的间距为 ΔE = AJ（朗德区间规则）。

**Step 1 — Physical origin.** In the electron's rest frame, the nucleus (charge Ze) orbits it, creating a magnetic field B = −(v × E)/c² at the electron's location, where E = −(dU/dr) r̂/e. Writing the electron's orbital velocity v = p/m and using L = r × p:

**第 1 步 — 物理起源。** 在电子静止参考系中，原子核（电荷 Ze）绕其旋转，在电子位置产生磁场 B = −(v × E)/c²，其中 E = −(dU/dr) r̂/e。写出电子的轨道速度 v = p/m，并利用 L = r × p：

  B = (1/mc²e r)(dU/dr) L.

The electron's magnetic moment is μ_s = −g_s (e/2m) S with g_s ≈ 2. The interaction energy is −μ_s · B.

电子的磁矩为 μ_s = −g_s (e/2m) S，g_s ≈ 2。相互作用能为 −μ_s · B。

**Step 2 — Thomas precession correction.** There is a relativistic kinematic correction (Thomas precession) that reduces the naive result by a factor of 2. After accounting for it, the effective spin–orbit Hamiltonian is:

**第 2 步 — 托马斯进动修正。** 存在一个相对论运动学修正（托马斯进动），将朴素结果减小 2 倍。计入后，有效自旋–轨道哈密顿量为：

  H_SO = (1/2m²c²) (1/r)(dU/dr) L · S = A(r) L · S,

where the factor of 1/2 comes from the Thomas correction. For a hydrogenic potential U(r) = −Ze²/(4πε₀ r), dU/dr = Ze²/(4πε₀ r²), giving A = Ze²/(8πε₀ m²c² r³) — an operator in r.

其中 1/2 因子来自托马斯修正。对于类氢势 U(r) = −Ze²/(4πε₀ r)，dU/dr = Ze²/(4πε₀ r²)，给出 A = Ze²/(8πε₀ m²c² r³)——r 的算符。

**Step 3 — Evaluate the expectation value.** Take the expectation value of A(r) in the state |n, l, m_l⟩:

**第 3 步 — 计算期望值。** 在态 |n, l, m_l⟩ 中对 A(r) 取期望值：

  ⟨A⟩ = Ze²/(8πε₀ m²c²) ⟨1/r³⟩,

where for hydrogenic states ⟨1/r³⟩ = Z³/(a₀³ n³ l(l+½)(l+1)) with the Bohr radius a₀. Absorbing all radial factors into a single constant A_nl, the spin–orbit Hamiltonian in a given (n, l) manifold becomes:

其中对类氢态 ⟨1/r³⟩ = Z³/(a₀³ n³ l(l+½)(l+1))，a₀ 为玻尔半径。将所有径向因子吸收到单一常数 A_nl 中，给定 (n, l) 流形中的自旋–轨道哈密顿量变为：

  H_SO = A_nl (L · S).

**Step 4 — Diagonalize using J = L + S.** J² = (L + S)² = L² + S² + 2L · S, hence:

**第 4 步 — 用 J = L + S 对角化。** J² = (L + S)² = L² + S² + 2L · S，因此：

  L · S = (J² − L² − S²)/2.

In the basis |J, m_J; L, S⟩ (the coupled basis), J², L², S² are all diagonal with eigenvalues J(J+1)ℏ², L(L+1)ℏ², S(S+1)ℏ². Therefore:

在基矢 |J, m_J; L, S⟩（耦合基）中，J²、L²、S² 均对角，本征值分别为 J(J+1)ℏ²、L(L+1)ℏ²、S(S+1)ℏ²。因此：

  ⟨L · S⟩ = (ℏ²/2)[J(J+1) − L(L+1) − S(S+1)].

**Step 5 — Final energy shift.**

**第 5 步 — 最终能量移动。**

  **E_SO(J) = (A_nl ℏ²/2)[J(J+1) − L(L+1) − S(S+1)]**.

The spacing between adjacent levels is:

相邻能级之间的间距为：

  E_SO(J+1) − E_SO(J) = (A_nl ℏ²/2)[(J+1)(J+2) − J(J+1)] = A_nl ℏ² (J+1),

proportional to J+1 — this is the **Landé interval rule**: the energy gap between the J and J+1 levels is proportional to the larger J value. ∎

正比于 J+1——这是**朗德区间规则**：J 与 J+1 能级之间的能隙正比于较大的 J 值。∎

---

## B. H₂⁺ Bonding and Antibonding from LCAO · 从 LCAO 推导 H₂⁺ 的成键与反键

**Claim.** For H₂⁺ with nuclear separation R, the LCAO secular determinant gives two eigenvalues:

  E± = (H_AA ± H_AB)/(1 ± S),

where H_AA = ⟨φ_A|H|φ_A⟩ is the Coulomb integral, H_AB = ⟨φ_A|H|φ_B⟩ is the resonance (exchange) integral, and S = ⟨φ_A|φ_B⟩ is the overlap integral. E_+ < E_AA (bonding) and E_- > E_AA (antibonding) for H_AB < 0.

**命题。** 对于核间距为 R 的 H₂⁺，LCAO 久期行列式给出两个本征值：

  E± = (H_AA ± H_AB)/(1 ± S)，

其中 H_AA = ⟨φ_A|H|φ_A⟩ 为库仑积分，H_AB = ⟨φ_A|H|φ_B⟩ 为共振（交换）积分，S = ⟨φ_A|φ_B⟩ 为重叠积分。当 H_AB < 0 时，E_+ < E_AA（成键），E_- > E_AA（反键）。

**Step 1 — Set up the variational problem.** Write the trial function as ψ = c_A φ_A + c_B φ_B, where φ_A = φ_{1s}(r_A) and φ_B = φ_{1s}(r_B) are the ground-state hydrogen 1s orbitals on nuclei A and B. The electronic Hamiltonian is:

**第 1 步 — 建立变分问题。** 将试探函数写为 ψ = c_A φ_A + c_B φ_B，其中 φ_A = φ_{1s}(r_A) 和 φ_B = φ_{1s}(r_B) 是核 A 和 B 上的基态氢 1s 轨道。电子哈密顿量为：

  H = −(ℏ²/2m)∇² − e²/(4πε₀ r_A) − e²/(4πε₀ r_B) + e²/(4πε₀ R).

The last term is the nuclear repulsion (a constant for fixed R).

最后一项为核排斥（固定 R 时为常数）。

**Step 2 — Apply the variational principle.** Minimizing ⟨ψ|H|ψ⟩/⟨ψ|ψ⟩ over c_A, c_B gives the secular equations:

**第 2 步 — 应用变分原理。** 对 c_A、c_B 最小化 ⟨ψ|H|ψ⟩/⟨ψ|ψ⟩ 给出久期方程：

  (H_AA − E) c_A + (H_AB − ES) c_B = 0,
  (H_AB − ES) c_A + (H_BB − E) c_B = 0,

using the definitions H_AA = ⟨φ_A|H|φ_A⟩, H_BB = ⟨φ_B|H|φ_B⟩ = H_AA (by symmetry), H_AB = ⟨φ_A|H|φ_B⟩ = ⟨φ_B|H|φ_A⟩, and S = ⟨φ_A|φ_B⟩.

利用定义 H_AA = ⟨φ_A|H|φ_A⟩，H_BB = ⟨φ_B|H|φ_B⟩ = H_AA（由对称性），H_AB = ⟨φ_A|H|φ_B⟩ = ⟨φ_B|H|φ_A⟩，S = ⟨φ_A|φ_B⟩。

**Step 3 — Solve the secular determinant.** A non-trivial solution exists when:

**第 3 步 — 求解久期行列式。** 当以下条件满足时存在非平凡解：

  |H_AA − E    H_AB − ES|
  |H_AB − ES   H_AA − E | = 0.

Expanding: (H_AA − E)² − (H_AB − ES)² = 0, so H_AA − E = ±(H_AB − ES). Solving for E:

展开：(H_AA − E)² − (H_AB − ES)² = 0，故 H_AA − E = ±(H_AB − ES)。解出 E：

  **E± = (H_AA ± H_AB)/(1 ± S)**.

**Step 4 — Physical interpretation.** The Coulomb integral H_AA = E_{1s} + ⟨φ_A|−e²/(4πε₀ r_B)|φ_A⟩ + e²/(4πε₀ R) includes the energy of electron in the field of both nuclei. The resonance integral H_AB = S·E_{1s} + ⟨φ_A|−e²/(4πε₀ r_A)|φ_B⟩ represents the off-diagonal quantum-mechanical mixing of the two atomic states. For R > 0, H_AB < 0 (the overlap region lowers the kinetic energy through delocalization).

**第 4 步 — 物理诠释。** 库仑积分 H_AA = E_{1s} + ⟨φ_A|−e²/(4πε₀ r_B)|φ_A⟩ + e²/(4πε₀ R) 包含电子在两个原子核场中的能量。共振积分 H_AB = S·E_{1s} + ⟨φ_A|−e²/(4πε₀ r_A)|φ_B⟩ 代表两个原子态的非对角量子力学混合。对于 R > 0，H_AB < 0（重叠区域通过离域降低动能）。

**Step 5 — Bonding is below the atomic limit.** Since H_AB < 0 and S > 0 at finite R, the bonding energy E_+ = (H_AA + H_AB)/(1 + S) < H_AA = E_{atomic} (numerator is smaller, denominator larger than 1 when H_AB < 0). Hence the bonding orbital is genuinely lower in energy than the separated-atom limit, producing a potential-energy well and a stable bond. The antibonding E_- = (H_AA − H_AB)/(1 − S) > H_AA, with an extra node between the nuclei and a repulsive potential energy curve. ∎

**第 5 步 — 成键低于原子极限。** 由于在有限 R 处 H_AB < 0 且 S > 0，成键能量 E_+ = (H_AA + H_AB)/(1 + S) < H_AA = E_{atomic}（当 H_AB < 0 时分子小于分母大于 1）。因此成键轨道能量确实低于分离原子极限，产生势能阱和稳定键。反键 E_- = (H_AA − H_AB)/(1 − S) > H_AA，在两核之间有额外节点和排斥势能曲线。∎

---

## C. Rigid-Rotor Rotational Spectrum ΔE = 2B(J+1) · 刚性转子转动谱 ΔE = 2B(J+1)

**Claim.** For a diatomic molecule with moment of inertia I = μR², the rotational energy levels are E_J = ℏ²J(J+1)/(2I) = BJ(J+1) where B = ℏ²/(2I). The electric-dipole selection rule ΔJ = ±1 gives absorption lines at energies ΔE_J = E_{J+1} − E_J = 2B(J+1), equally spaced by 2B.

**命题。** 对于转动惯量 I = μR² 的双原子分子，转动能级为 E_J = ℏ²J(J+1)/(2I) = BJ(J+1)，其中 B = ℏ²/(2I)。电偶极选择规则 ΔJ = ±1 给出能量为 ΔE_J = E_{J+1} − E_J = 2B(J+1) 的吸收谱线，间距均匀为 2B。

**Step 1 — Quantum rigid rotor.** The kinetic energy of a rigid body rotating about its center of mass with angular momentum L is T = L²/(2I). In quantum mechanics, replace L² → L̂² with eigenvalues ℏ²J(J+1):

**第 1 步 — 量子刚性转子。** 绕质心旋转、角动量为 L 的刚体动能为 T = L²/(2I)。在量子力学中，用 L̂² 替换 L²，本征值为 ℏ²J(J+1)：

  Ĥ_rot = L̂²/(2I),   E_J = ℏ²J(J+1)/(2I),   J = 0, 1, 2, …

Defining the **rotational constant** B = ℏ²/(2I):

定义**转动常数** B = ℏ²/(2I)：

  **E_J = B J(J+1)**.

The (2J+1)-fold degeneracy in m_J is preserved until the symmetry is broken (e.g., by an external field — Stark effect).

m_J 的 (2J+1) 重简并保留，直到对称性被破坏（例如由外加电场——斯塔克效应）。

**Step 2 — Selection rule.** The electric-dipole matrix element for a rigid rotor with permanent dipole moment d is ⟨J', m'|d·ε̂|J, m⟩, where ε̂ is the photon polarization. This involves spherical harmonics Y_J^m. From the Wigner–Eckart theorem (or explicit evaluation), the matrix element vanishes unless:

**第 2 步 — 选择规则。** 具有固有偶极矩 d 的刚性转子的电偶极矩阵元为 ⟨J', m'|d·ε̂|J, m⟩，其中 ε̂ 为光子极化方向。这涉及球谐函数 Y_J^m。由维格纳–埃卡特定理（或显式计算），矩阵元为零，除非：

  ΔJ = J' − J = ±1   and   Δm_J = 0, ±1.

Physical reason: a photon carries spin-1, so absorbing or emitting a photon changes J by exactly 1 for a dipole transition.

物理原因：光子携带自旋 1，因此吸收或发射光子对于偶极跃迁将 J 改变恰好 1。

**Step 3 — Absorption line positions.** For the J → J+1 absorption:

**第 3 步 — 吸收谱线位置。** 对于 J → J+1 吸收：

  ΔE_J = E_{J+1} − E_J = B(J+1)(J+2) − BJ(J+1) = B[(J+1)(J+2) − J(J+1)]
        = B(J+1)[(J+2) − J] = **2B(J+1)**.

Lines occur at ΔE = 2B, 4B, 6B, 8B, … (for J = 0, 1, 2, 3, …), equally spaced by 2B.

谱线出现在 ΔE = 2B, 4B, 6B, 8B, …（对应 J = 0, 1, 2, 3, …），间距均匀为 2B。

**Step 4 — Measure B and hence I and R.** From the measured spacing Δν = 2B/h, one obtains:

**第 4 步 — 测量 B 进而得到 I 和 R。** 由测量的间距 Δν = 2B/h，得到：

  I = h/(4π² Δν),   then   R = √(I/μ),   μ = m₁m₂/(m₁+m₂).

For example, for ¹H³⁵Cl: Δν ≈ 6.34 × 10¹¹ Hz, giving R ≈ 127 pm, in excellent agreement with X-ray crystallography. ∎

例如，对于 ¹H³⁵Cl：Δν ≈ 6.34 × 10¹¹ Hz，给出 R ≈ 127 pm，与 X 射线晶体学结果完全吻合。∎

---

*All derivations are complete through intermediate algebra with physical interpretation. The Landé interval rule, LCAO secular determinant, and rigid-rotor line spacing are all standard and appear across spectroscopy, molecular physics, and astrochemistry.*

*所有推导均通过中间代数完整呈现并附物理诠释。朗德区间规则、LCAO 久期行列式和刚性转子谱线间距均为标准结果，广泛出现在光谱学、分子物理和天体化学中。*

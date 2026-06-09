# Derivations — Module 9.2: Atomic & Molecular Physics
# 推导 — 模块 9.2：原子与分子物理

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 9.2](./module-9.2-atomic-and-molecular-physics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 9.2](./module-9.2-atomic-and-molecular-physics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Fine-Structure Spin–Orbit Energy Shift · 精细结构自旋–轨道能量移动

**Claim.** For an electron in a central-field potential $U(r)$ with orbital angular momentum $\mathbf L$ and spin $\mathbf S$, the spin–orbit interaction is $H_{SO} = A(\mathbf L \cdot \mathbf S)$ with coupling constant $A = (1/2m^2c^2)(1/r)(dU/dr)$. This lifts the $(2L+1)(2S+1)$-fold degeneracy of the LS term, shifting the $J$-level by:

$$ E_{SO}(J) = (A/2)[J(J+1) - L(L+1) - S(S+1)]. $$

The spacing between adjacent $J$ and $J+1$ levels is $\Delta E = A(J+1)$ (Landé interval rule).

**命题。** 对于中心场势 $U(r)$ 中具有轨道角动量 $\mathbf L$ 和自旋 $\mathbf S$ 的电子，自旋–轨道相互作用为 $H_{SO} = A(\mathbf L \cdot \mathbf S)$，耦合常数 $A = (1/2m^2c^2)(1/r)(dU/dr)$。这消除 LS 谱项的 $(2L+1)(2S+1)$ 重简并，将 $J$ 能级移动：

$$ E_{SO}(J) = (A/2)[J(J+1) - L(L+1) - S(S+1)]. $$

相邻 $J$ 与 $J+1$ 能级之间的间距为 $\Delta E = A(J+1)$（朗德区间规则）。

**Step 1 — Physical origin.** In the electron's rest frame, the nucleus (charge $Ze$) orbits it, creating a magnetic field $\mathbf B = -(\mathbf v \times \mathbf E)/c^2$ at the electron's location, where $\mathbf E = -(dU/dr)\,\hat{\mathbf r}/e$. Writing the electron's orbital velocity $\mathbf v = \mathbf p/m$ and using $\mathbf L = \mathbf r \times \mathbf p$:

**第 1 步 — 物理起源。** 在电子静止参考系中，原子核（电荷 $Ze$）绕其旋转，在电子位置产生磁场 $\mathbf B = -(\mathbf v \times \mathbf E)/c^2$，其中 $\mathbf E = -(dU/dr)\,\hat{\mathbf r}/e$。写出电子的轨道速度 $\mathbf v = \mathbf p/m$，并利用 $\mathbf L = \mathbf r \times \mathbf p$：

$$ \mathbf B = (1/mc^2 e r)(dU/dr)\,\mathbf L. $$

The electron's magnetic moment is $\boldsymbol\mu_s = -g_s (e/2m)\,\mathbf S$ with $g_s \approx 2$. The interaction energy is $-\boldsymbol\mu_s \cdot \mathbf B$.

电子的磁矩为 $\boldsymbol\mu_s = -g_s (e/2m)\,\mathbf S$，$g_s \approx 2$。相互作用能为 $-\boldsymbol\mu_s \cdot \mathbf B$。

**Step 2 — Thomas precession correction.** There is a relativistic kinematic correction (Thomas precession) that reduces the naive result by a factor of 2. After accounting for it, the effective spin–orbit Hamiltonian is:

**第 2 步 — 托马斯进动修正。** 存在一个相对论运动学修正（托马斯进动），将朴素结果减小 2 倍。计入后，有效自旋–轨道哈密顿量为：

$$ H_{SO} = (1/2m^2c^2)(1/r)(dU/dr)\,\mathbf L \cdot \mathbf S = A(r)\,\mathbf L \cdot \mathbf S, $$

where the factor of $1/2$ comes from the Thomas correction. For a hydrogenic potential $U(r) = -Ze^2/(4\pi\varepsilon_0 r)$, $dU/dr = Ze^2/(4\pi\varepsilon_0 r^2)$, giving $A = Ze^2/(8\pi\varepsilon_0 m^2c^2 r^3)$ — an operator in $r$.

其中 $1/2$ 因子来自托马斯修正。对于类氢势 $U(r) = -Ze^2/(4\pi\varepsilon_0 r)$，$dU/dr = Ze^2/(4\pi\varepsilon_0 r^2)$，给出 $A = Ze^2/(8\pi\varepsilon_0 m^2c^2 r^3)$——$r$ 的算符。

**Step 3 — Evaluate the expectation value.** Take the expectation value of $A(r)$ in the state $|n, l, m_l\rangle$:

**第 3 步 — 计算期望值。** 在态 $|n, l, m_l\rangle$ 中对 $A(r)$ 取期望值：

$$ \langle A\rangle = Ze^2/(8\pi\varepsilon_0 m^2c^2)\,\langle 1/r^3\rangle, $$

where for hydrogenic states $\langle 1/r^3\rangle = Z^3/(a_0^3 n^3 l(l+\tfrac12)(l+1))$ with the Bohr radius $a_0$. Absorbing all radial factors into a single constant $A_{nl}$, the spin–orbit Hamiltonian in a given $(n, l)$ manifold becomes:

其中对类氢态 $\langle 1/r^3\rangle = Z^3/(a_0^3 n^3 l(l+\tfrac12)(l+1))$，$a_0$ 为玻尔半径。将所有径向因子吸收到单一常数 $A_{nl}$ 中，给定 $(n, l)$ 流形中的自旋–轨道哈密顿量变为：

$$ H_{SO} = A_{nl}\,(\mathbf L \cdot \mathbf S). $$

**Step 4 — Diagonalize using $\mathbf J = \mathbf L + \mathbf S$.** $\mathbf J^2 = (\mathbf L + \mathbf S)^2 = \mathbf L^2 + \mathbf S^2 + 2\mathbf L \cdot \mathbf S$, hence:

**第 4 步 — 用 $\mathbf J = \mathbf L + \mathbf S$ 对角化。** $\mathbf J^2 = (\mathbf L + \mathbf S)^2 = \mathbf L^2 + \mathbf S^2 + 2\mathbf L \cdot \mathbf S$，因此：

$$ \mathbf L \cdot \mathbf S = (\mathbf J^2 - \mathbf L^2 - \mathbf S^2)/2. $$

In the basis $|J, m_J; L, S\rangle$ (the coupled basis), $\mathbf J^2, \mathbf L^2, \mathbf S^2$ are all diagonal with eigenvalues $J(J+1)\hbar^2, L(L+1)\hbar^2, S(S+1)\hbar^2$. Therefore:

在基矢 $|J, m_J; L, S\rangle$（耦合基）中，$\mathbf J^2$、$\mathbf L^2$、$\mathbf S^2$ 均对角，本征值分别为 $J(J+1)\hbar^2$、$L(L+1)\hbar^2$、$S(S+1)\hbar^2$。因此：

$$ \langle \mathbf L \cdot \mathbf S\rangle = (\hbar^2/2)[J(J+1) - L(L+1) - S(S+1)]. $$

**Step 5 — Final energy shift.**

**第 5 步 — 最终能量移动。**

$$ \boxed{\, E_{SO}(J) = (A_{nl}\hbar^2/2)[J(J+1) - L(L+1) - S(S+1)] \,} $$

The spacing between adjacent levels is:

相邻能级之间的间距为：

$$ E_{SO}(J+1) - E_{SO}(J) = (A_{nl}\hbar^2/2)[(J+1)(J+2) - J(J+1)] = A_{nl}\hbar^2\,(J+1), $$

proportional to $J+1$ — this is the **Landé interval rule**: the energy gap between the $J$ and $J+1$ levels is proportional to the larger $J$ value. $\blacksquare$

正比于 $J+1$——这是**朗德区间规则**：$J$ 与 $J+1$ 能级之间的能隙正比于较大的 $J$ 值。$\blacksquare$

---

## B. $\text{H}_2^+$ Bonding and Antibonding from LCAO · 从 LCAO 推导 $\text{H}_2^+$ 的成键与反键

**Claim.** For $\text{H}_2^+$ with nuclear separation $R$, the LCAO secular determinant gives two eigenvalues:

$$ E_\pm = (H_{AA} \pm H_{AB})/(1 \pm S), $$

where $H_{AA} = \langle\phi_A|H|\phi_A\rangle$ is the Coulomb integral, $H_{AB} = \langle\phi_A|H|\phi_B\rangle$ is the resonance (exchange) integral, and $S = \langle\phi_A|\phi_B\rangle$ is the overlap integral. $E_+ < E_{AA}$ (bonding) and $E_- > E_{AA}$ (antibonding) for $H_{AB} < 0$.

**命题。** 对于核间距为 $R$ 的 $\text{H}_2^+$，LCAO 久期行列式给出两个本征值：

$$ E_\pm = (H_{AA} \pm H_{AB})/(1 \pm S), $$

其中 $H_{AA} = \langle\phi_A|H|\phi_A\rangle$ 为库仑积分，$H_{AB} = \langle\phi_A|H|\phi_B\rangle$ 为共振（交换）积分，$S = \langle\phi_A|\phi_B\rangle$ 为重叠积分。当 $H_{AB} < 0$ 时，$E_+ < E_{AA}$（成键），$E_- > E_{AA}$（反键）。

**Step 1 — Set up the variational problem.** Write the trial function as $\psi = c_A \phi_A + c_B \phi_B$, where $\phi_A = \phi_{1s}(r_A)$ and $\phi_B = \phi_{1s}(r_B)$ are the ground-state hydrogen 1s orbitals on nuclei A and B. The electronic Hamiltonian is:

**第 1 步 — 建立变分问题。** 将试探函数写为 $\psi = c_A \phi_A + c_B \phi_B$，其中 $\phi_A = \phi_{1s}(r_A)$ 和 $\phi_B = \phi_{1s}(r_B)$ 是核 A 和 B 上的基态氢 1s 轨道。电子哈密顿量为：

$$ H = -(\hbar^2/2m)\nabla^2 - e^2/(4\pi\varepsilon_0 r_A) - e^2/(4\pi\varepsilon_0 r_B) + e^2/(4\pi\varepsilon_0 R). $$

The last term is the nuclear repulsion (a constant for fixed $R$).

最后一项为核排斥（固定 $R$ 时为常数）。

**Step 2 — Apply the variational principle.** Minimizing $\langle\psi|H|\psi\rangle/\langle\psi|\psi\rangle$ over $c_A, c_B$ gives the secular equations:

**第 2 步 — 应用变分原理。** 对 $c_A$、$c_B$ 最小化 $\langle\psi|H|\psi\rangle/\langle\psi|\psi\rangle$ 给出久期方程：

$$ \begin{aligned} (H_{AA} - E)\,c_A + (H_{AB} - ES)\,c_B &= 0, \\ (H_{AB} - ES)\,c_A + (H_{BB} - E)\,c_B &= 0, \end{aligned} $$

using the definitions $H_{AA} = \langle\phi_A|H|\phi_A\rangle$, $H_{BB} = \langle\phi_B|H|\phi_B\rangle = H_{AA}$ (by symmetry), $H_{AB} = \langle\phi_A|H|\phi_B\rangle = \langle\phi_B|H|\phi_A\rangle$, and $S = \langle\phi_A|\phi_B\rangle$.

利用定义 $H_{AA} = \langle\phi_A|H|\phi_A\rangle$，$H_{BB} = \langle\phi_B|H|\phi_B\rangle = H_{AA}$（由对称性），$H_{AB} = \langle\phi_A|H|\phi_B\rangle = \langle\phi_B|H|\phi_A\rangle$，$S = \langle\phi_A|\phi_B\rangle$。

**Step 3 — Solve the secular determinant.** A non-trivial solution exists when:

**第 3 步 — 求解久期行列式。** 当以下条件满足时存在非平凡解：

$$ \begin{vmatrix} H_{AA} - E & H_{AB} - ES \\ H_{AB} - ES & H_{AA} - E \end{vmatrix} = 0. $$

Expanding: $(H_{AA} - E)^2 - (H_{AB} - ES)^2 = 0$, so $H_{AA} - E = \pm(H_{AB} - ES)$. Solving for $E$:

展开：$(H_{AA} - E)^2 - (H_{AB} - ES)^2 = 0$，故 $H_{AA} - E = \pm(H_{AB} - ES)$。解出 $E$：

$$ \boxed{\, E_\pm = (H_{AA} \pm H_{AB})/(1 \pm S) \,} $$

**Step 4 — Physical interpretation.** The Coulomb integral $H_{AA} = E_{1s} + \langle\phi_A|-e^2/(4\pi\varepsilon_0 r_B)|\phi_A\rangle + e^2/(4\pi\varepsilon_0 R)$ includes the energy of electron in the field of both nuclei. The resonance integral $H_{AB} = S\cdot E_{1s} + \langle\phi_A|-e^2/(4\pi\varepsilon_0 r_A)|\phi_B\rangle$ represents the off-diagonal quantum-mechanical mixing of the two atomic states. For $R > 0$, $H_{AB} < 0$ (the overlap region lowers the kinetic energy through delocalization).

**第 4 步 — 物理诠释。** 库仑积分 $H_{AA} = E_{1s} + \langle\phi_A|-e^2/(4\pi\varepsilon_0 r_B)|\phi_A\rangle + e^2/(4\pi\varepsilon_0 R)$ 包含电子在两个原子核场中的能量。共振积分 $H_{AB} = S\cdot E_{1s} + \langle\phi_A|-e^2/(4\pi\varepsilon_0 r_A)|\phi_B\rangle$ 代表两个原子态的非对角量子力学混合。对于 $R > 0$，$H_{AB} < 0$（重叠区域通过离域降低动能）。

**Step 5 — Bonding is below the atomic limit.** Since $H_{AB} < 0$ and $S > 0$ at finite $R$, the bonding energy $E_+ = (H_{AA} + H_{AB})/(1 + S) < H_{AA} = E_{atomic}$ (numerator is smaller, denominator larger than 1 when $H_{AB} < 0$). Hence the bonding orbital is genuinely lower in energy than the separated-atom limit, producing a potential-energy well and a stable bond. The antibonding $E_- = (H_{AA} - H_{AB})/(1 - S) > H_{AA}$, with an extra node between the nuclei and a repulsive potential energy curve. $\blacksquare$

**第 5 步 — 成键低于原子极限。** 由于在有限 $R$ 处 $H_{AB} < 0$ 且 $S > 0$，成键能量 $E_+ = (H_{AA} + H_{AB})/(1 + S) < H_{AA} = E_{atomic}$（当 $H_{AB} < 0$ 时分子小于分母大于 1）。因此成键轨道能量确实低于分离原子极限，产生势能阱和稳定键。反键 $E_- = (H_{AA} - H_{AB})/(1 - S) > H_{AA}$，在两核之间有额外节点和排斥势能曲线。$\blacksquare$

---

## C. Rigid-Rotor Rotational Spectrum $\Delta E = 2B(J+1)$ · 刚性转子转动谱 $\Delta E = 2B(J+1)$

**Claim.** For a diatomic molecule with moment of inertia $I = \mu R^2$, the rotational energy levels are $E_J = \hbar^2 J(J+1)/(2I) = BJ(J+1)$ where $B = \hbar^2/(2I)$. The electric-dipole selection rule $\Delta J = \pm 1$ gives absorption lines at energies $\Delta E_J = E_{J+1} - E_J = 2B(J+1)$, equally spaced by $2B$.

**命题。** 对于转动惯量 $I = \mu R^2$ 的双原子分子，转动能级为 $E_J = \hbar^2 J(J+1)/(2I) = BJ(J+1)$，其中 $B = \hbar^2/(2I)$。电偶极选择规则 $\Delta J = \pm 1$ 给出能量为 $\Delta E_J = E_{J+1} - E_J = 2B(J+1)$ 的吸收谱线，间距均匀为 $2B$。

**Step 1 — Quantum rigid rotor.** The kinetic energy of a rigid body rotating about its center of mass with angular momentum $\mathbf L$ is $T = \mathbf L^2/(2I)$. In quantum mechanics, replace $\mathbf L^2 \to \hat{\mathbf L}^2$ with eigenvalues $\hbar^2 J(J+1)$:

**第 1 步 — 量子刚性转子。** 绕质心旋转、角动量为 $\mathbf L$ 的刚体动能为 $T = \mathbf L^2/(2I)$。在量子力学中，用 $\hat{\mathbf L}^2$ 替换 $\mathbf L^2$，本征值为 $\hbar^2 J(J+1)$：

$$ \hat H_{rot} = \hat{\mathbf L}^2/(2I), \quad E_J = \hbar^2 J(J+1)/(2I), \quad J = 0, 1, 2, \ldots $$

Defining the **rotational constant** $B = \hbar^2/(2I)$:

定义**转动常数** $B = \hbar^2/(2I)$：

$$ \boxed{\, E_J = B J(J+1) \,} $$

The $(2J+1)$-fold degeneracy in $m_J$ is preserved until the symmetry is broken (e.g., by an external field — Stark effect).

$m_J$ 的 $(2J+1)$ 重简并保留，直到对称性被破坏（例如由外加电场——斯塔克效应）。

**Step 2 — Selection rule.** The electric-dipole matrix element for a rigid rotor with permanent dipole moment $\mathbf d$ is $\langle J', m'|\mathbf d\cdot\hat{\boldsymbol\varepsilon}|J, m\rangle$, where $\hat{\boldsymbol\varepsilon}$ is the photon polarization. This involves spherical harmonics $Y_J^m$. From the Wigner–Eckart theorem (or explicit evaluation), the matrix element vanishes unless:

**第 2 步 — 选择规则。** 具有固有偶极矩 $\mathbf d$ 的刚性转子的电偶极矩阵元为 $\langle J', m'|\mathbf d\cdot\hat{\boldsymbol\varepsilon}|J, m\rangle$，其中 $\hat{\boldsymbol\varepsilon}$ 为光子极化方向。这涉及球谐函数 $Y_J^m$。由维格纳–埃卡特定理（或显式计算），矩阵元为零，除非：

$$ \Delta J = J' - J = \pm 1 \quad\text{and}\quad \Delta m_J = 0, \pm 1. $$

Physical reason: a photon carries spin-1, so absorbing or emitting a photon changes $J$ by exactly 1 for a dipole transition.

物理原因：光子携带自旋 1，因此吸收或发射光子对于偶极跃迁将 $J$ 改变恰好 1。

**Step 3 — Absorption line positions.** For the $J \to J+1$ absorption:

**第 3 步 — 吸收谱线位置。** 对于 $J \to J+1$ 吸收：

$$ \begin{aligned} \Delta E_J = E_{J+1} - E_J &= B(J+1)(J+2) - BJ(J+1) = B[(J+1)(J+2) - J(J+1)] \\ &= B(J+1)[(J+2) - J] = \boxed{\, 2B(J+1) \,}. \end{aligned} $$

Lines occur at $\Delta E = 2B, 4B, 6B, 8B, \ldots$ (for $J = 0, 1, 2, 3, \ldots$), equally spaced by $2B$.

谱线出现在 $\Delta E = 2B, 4B, 6B, 8B, \ldots$（对应 $J = 0, 1, 2, 3, \ldots$），间距均匀为 $2B$。

**Step 4 — Measure $B$ and hence $I$ and $R$.** From the measured spacing $\Delta\nu = 2B/h$, one obtains:

**第 4 步 — 测量 $B$ 进而得到 $I$ 和 $R$。** 由测量的间距 $\Delta\nu = 2B/h$，得到：

$$ I = h/(4\pi^2 \Delta\nu), \quad\text{then}\quad R = \sqrt{I/\mu}, \quad \mu = m_1 m_2/(m_1+m_2). $$

For example, for ${}^{1}\text{H}{}^{35}\text{Cl}$: $\Delta\nu \approx 6.34 \times 10^{11}$ Hz, giving $R \approx 127$ pm, in excellent agreement with X-ray crystallography. $\blacksquare$

例如，对于 ${}^{1}\text{H}{}^{35}\text{Cl}$：$\Delta\nu \approx 6.34 \times 10^{11}$ Hz，给出 $R \approx 127$ pm，与 X 射线晶体学结果完全吻合。$\blacksquare$

---

*All derivations are complete through intermediate algebra with physical interpretation. The Landé interval rule, LCAO secular determinant, and rigid-rotor line spacing are all standard and appear across spectroscopy, molecular physics, and astrochemistry.*

*所有推导均通过中间代数完整呈现并附物理诠释。朗德区间规则、LCAO 久期行列式和刚性转子谱线间距均为标准结果，广泛出现在光谱学、分子物理和天体化学中。*

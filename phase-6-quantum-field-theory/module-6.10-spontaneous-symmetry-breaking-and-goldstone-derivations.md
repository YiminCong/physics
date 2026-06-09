# Derivations — Module 6.10: Spontaneous Symmetry Breaking & Goldstone's Theorem
# 推导 — 模块 6.10：自发对称性破缺与戈德斯通定理

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 6.10](./module-6.10-spontaneous-symmetry-breaking-and-goldstone.md). Full step-by-step proofs. English first, then 中文.
> [模块 6.10](./module-6.10-spontaneous-symmetry-breaking-and-goldstone.md) 的配套文档：完整逐步证明。先英文，后中文。

---

## A. SSB in a Real Scalar Theory: Vacuum and the Massive Field · 实标量理论中的自发对称性破缺：真空与有质量场

**Claim.** For $\mathcal{L} = \tfrac12(\partial\varphi)^2 - V(\varphi)$ with $V(\varphi) = -\tfrac12\mu^2\varphi^2 + \tfrac14\lambda\varphi^4$ ($\mu^2 > 0$, $\lambda > 0$), the $\mathbb{Z}_2$-symmetric point $\varphi = 0$ is a maximum, the vacuum is $\langle\varphi\rangle = v = \pm\sqrt{\mu^2/\lambda}$, and the fluctuation about it has mass $m_\eta^2 = 2\mu^2 = 2\lambda v^2$.

**Step 1 — Stationary points.** A constant field minimizes the energy when it minimizes $V$ (the gradient term $\tfrac12(\partial\varphi)^2$ vanishes for constant $\varphi$). Compute $V'(\varphi) = -\mu^2\varphi + \lambda\varphi^3 = \varphi(\lambda\varphi^2 - \mu^2)$. Setting $V'(\varphi) = 0$ gives $\varphi = 0$ or $\varphi^2 = \mu^2/\lambda$, i.e. $\varphi = \pm v$ with $v \equiv \sqrt{\mu^2/\lambda}$.

**Step 2 — Classify by curvature.** Compute $V''(\varphi) = -\mu^2 + 3\lambda\varphi^2$. At the symmetric point $V''(0) = -\mu^2 < 0$, so $\varphi = 0$ is a **maximum**. At $\varphi = \pm v$, $V''(\pm v) = -\mu^2 + 3\lambda(\mu^2/\lambda) = -\mu^2 + 3\mu^2 = 2\mu^2 > 0$, so $\varphi = \pm v$ are **minima**. The vacuum is therefore $\langle\varphi\rangle = v = \sqrt{\mu^2/\lambda}$ (choosing the + branch). Because the two minima are exchanged by $\varphi \to -\varphi$, selecting one breaks $\mathbb{Z}_2$: $\mathcal{L}$ is symmetric, the vacuum is not.

**Step 3 — Expand and read off the mass.** Write $\varphi = v + \eta$ with $\eta$ the fluctuation. Then $V(v + \eta) = V(v) + V'(v)\eta + \tfrac12 V''(v)\eta^2 + \ldots$. Since $V'(v) = 0$ (minimum) and $V''(v) = 2\mu^2$, the quadratic term is $\tfrac12(2\mu^2)\eta^2 = \tfrac12 m_\eta^2 \eta^2$ with

$$ \boxed{\, m_\eta^2 = V''(v) = 2\mu^2 = 2\lambda v^2 \,} \qquad \blacksquare $$

The negative mass-squared of the symmetric phase has become a positive mass once expanded about the true vacuum. The $\mathbb{Z}_2$ broken here is discrete, so no massless mode arises.

**Claim.** 对 $\mathcal{L} = \tfrac12(\partial\varphi)^2 - V(\varphi)$，$V(\varphi) = -\tfrac12\mu^2\varphi^2 + \tfrac14\lambda\varphi^4$（$\mu^2 > 0$，$\lambda > 0$），$\mathbb{Z}_2$ 对称点 $\varphi = 0$ 是极大值，真空为 $\langle\varphi\rangle = v = \pm\sqrt{\mu^2/\lambda}$，围绕它的涨落质量为 $m_\eta^2 = 2\mu^2 = 2\lambda v^2$。

**第 1 步 — 稳定点。** 常数场极小化能量当且仅当它极小化 $V$（梯度项 $\tfrac12(\partial\varphi)^2$ 对常数 $\varphi$ 为零）。计算 $V'(\varphi) = -\mu^2\varphi + \lambda\varphi^3 = \varphi(\lambda\varphi^2 - \mu^2)$。令 $V'(\varphi) = 0$ 给出 $\varphi = 0$ 或 $\varphi^2 = \mu^2/\lambda$，即 $\varphi = \pm v$，$v \equiv \sqrt{\mu^2/\lambda}$。

**第 2 步 — 用曲率分类。** 计算 $V''(\varphi) = -\mu^2 + 3\lambda\varphi^2$。对称点处 $V''(0) = -\mu^2 < 0$，故 $\varphi = 0$ 是**极大值**。在 $\varphi = \pm v$ 处，$V''(\pm v) = -\mu^2 + 3\lambda(\mu^2/\lambda) = -\mu^2 + 3\mu^2 = 2\mu^2 > 0$，故 $\varphi = \pm v$ 是**极小值**。真空因而为 $\langle\varphi\rangle = v = \sqrt{\mu^2/\lambda}$（取 + 分支）。由于两个极小值被 $\varphi \to -\varphi$ 交换，选取其一即破缺 $\mathbb{Z}_2$：$\mathcal{L}$ 对称，真空不对称。

**第 3 步 — 展开并读出质量。** 写 $\varphi = v + \eta$，$\eta$ 为涨落。则 $V(v + \eta) = V(v) + V'(v)\eta + \tfrac12 V''(v)\eta^2 + \ldots$。因 $V'(v) = 0$（极小值）且 $V''(v) = 2\mu^2$，二次项为 $\tfrac12(2\mu^2)\eta^2 = \tfrac12 m_\eta^2 \eta^2$，其中

$$ \boxed{\, m_\eta^2 = V''(v) = 2\mu^2 = 2\lambda v^2 \,} \qquad \blacksquare $$

对称相的负质量平方一旦围绕真实真空展开就变成正质量。这里破缺的 $\mathbb{Z}_2$ 是离散的，故不出现无质量模。

---

## B. The Goldstone Boson from a Broken U(1) · 破缺 U(1) 给出的戈德斯通玻色子

**Claim.** For a complex scalar with $\mathcal{L} = |\partial\varphi|^2 - V$, $V = -\mu^2|\varphi|^2 + \lambda|\varphi|^4$ and global $U(1)$ $\varphi \to e^{i\alpha}\varphi$, the vacuum $\langle\varphi\rangle = v/\sqrt{2}$ with $v = \sqrt{\mu^2/\lambda}$ breaks $U(1)$; the radial mode $h$ is massive with $m_h^2 = 2\mu^2 = 2\lambda v^2$, and the angular mode is exactly massless — the Goldstone boson.

**Step 1 — The circle of minima.** Write $\varphi = \rho\, e^{i\theta}/\sqrt{2}$ so $|\varphi|^2 = \tfrac12\rho^2$. Then $V = -\tfrac12\mu^2\rho^2 + \tfrac14\lambda\rho^4$, which is exactly the Section-A potential in the radial variable $\rho$. Minimizing in $\rho$ gives $\rho = v = \sqrt{\mu^2/\lambda}$, independent of $\theta$. The minimum is therefore the entire circle $|\varphi| = v/\sqrt{2}$; $V$ is *flat* along $\theta$. The vacuum picks one point, say $\theta = 0$, $\langle\varphi\rangle = v/\sqrt{2}$, breaking the $U(1)$.

**Step 2 — Parametrize the fluctuations.** Expand about the chosen vacuum in radial and angular fluctuations, $\varphi = (v + h)\, e^{i\theta/v}/\sqrt{2}$ (the $1/v$ makes $\theta$ canonically normalized). To quadratic order this is equivalent to the linear parametrization $\varphi = (v + h + i\pi)/\sqrt{2}$, where $h$ is the radial (Higgs-like) field and $\pi$ the angular (Goldstone) field.

**Step 3 — The potential to quadratic order.** With this parametrization $|\varphi|^2 = \tfrac12[(v + h)^2 + \pi^2] = \tfrac12[v^2 + 2vh + h^2 + \pi^2]$. Insert into $V = -\tfrac12\mu^2(2|\varphi|^2) + \tfrac14\lambda(2|\varphi|^2)^2$ and use $\mu^2 = \lambda v^2$:

$$ V = -\tfrac12\mu^2(v^2 + 2vh + h^2 + \pi^2) + \tfrac14\lambda(v^2 + 2vh + h^2 + \pi^2)^2. $$

Expanding and collecting quadratic terms, the linear terms cancel ($v$ is the minimum), and one finds the quadratic potential

$$ V_2 = \tfrac12(2\lambda v^2)\, h^2 + 0\cdot\pi^2 = \tfrac12 m_h^2 h^2, \qquad m_h^2 = 2\lambda v^2 = 2\mu^2. $$

The $h$ field is massive; the $\pi$ field has **no** quadratic term, so $m_\pi^2 = 0$.

**Step 4 — Why $\pi$ is massless: the flat direction.** The masslessness is geometry, not algebra. Adding a constant phase $\alpha$ to $\varphi$ is exactly the $U(1)$ transformation; it moves the field along the bottom of the "Mexican-hat" valley, where $V$ is constant by Step 1. The angular fluctuation $\pi$ is precisely a local displacement along this flat valley, so the restoring force — the curvature of $V$ transverse to the valley floor along the angular direction — is zero. Hence $m_\pi^2 = \partial^2 V/\partial\pi^2|_{\rm vac} = 0$ identically. The radial direction $h$ climbs the walls (curvature $2\lambda v^2$); the angular direction $\pi$ is the flat valley floor (curvature 0). The massless $\pi$ is the **Goldstone boson** of the broken $U(1)$. $\blacksquare$

**Claim.** 对复标量 $\mathcal{L} = |\partial\varphi|^2 - V$，$V = -\mu^2|\varphi|^2 + \lambda|\varphi|^4$，整体 $U(1)$ $\varphi \to e^{i\alpha}\varphi$，真空 $\langle\varphi\rangle = v/\sqrt{2}$（$v = \sqrt{\mu^2/\lambda}$）破缺 $U(1)$；径向模 $h$ 有质量 $m_h^2 = 2\mu^2 = 2\lambda v^2$，角向模严格无质量——戈德斯通玻色子。

**第 1 步 — 极小值圆。** 写 $\varphi = \rho\, e^{i\theta}/\sqrt{2}$，则 $|\varphi|^2 = \tfrac12\rho^2$。于是 $V = -\tfrac12\mu^2\rho^2 + \tfrac14\lambda\rho^4$，正是 A 节的势在径向变量 $\rho$ 中的形式。对 $\rho$ 极小化给出 $\rho = v = \sqrt{\mu^2/\lambda}$，与 $\theta$ 无关。极小值因而是整个圆 $|\varphi| = v/\sqrt{2}$；$V$ 沿 $\theta$ *平坦*。真空选取一点，设 $\theta = 0$，$\langle\varphi\rangle = v/\sqrt{2}$，破缺 $U(1)$。

**第 2 步 — 参数化涨落。** 围绕选定真空以径向和角向涨落展开，$\varphi = (v + h)\, e^{i\theta/v}/\sqrt{2}$（$1/v$ 使 $\theta$ 正则归一化）。到二次阶，这等价于线性参数化 $\varphi = (v + h + i\pi)/\sqrt{2}$，其中 $h$ 是径向（类希格斯）场，$\pi$ 是角向（戈德斯通）场。

**第 3 步 — 势到二次阶。** 用此参数化 $|\varphi|^2 = \tfrac12[(v + h)^2 + \pi^2] = \tfrac12[v^2 + 2vh + h^2 + \pi^2]$。代入 $V = -\tfrac12\mu^2(2|\varphi|^2) + \tfrac14\lambda(2|\varphi|^2)^2$ 并用 $\mu^2 = \lambda v^2$：

$$ V = -\tfrac12\mu^2(v^2 + 2vh + h^2 + \pi^2) + \tfrac14\lambda(v^2 + 2vh + h^2 + \pi^2)^2. $$

展开并收集二次项，线性项相消（$v$ 为极小值），得到二次势

$$ V_2 = \tfrac12(2\lambda v^2)\, h^2 + 0\cdot\pi^2 = \tfrac12 m_h^2 h^2, \qquad m_h^2 = 2\lambda v^2 = 2\mu^2. $$

$h$ 场有质量；$\pi$ 场**没有**二次项，故 $m_\pi^2 = 0$。

**第 4 步 — $\pi$ 为何无质量：平坦方向。** 无质量性源于几何而非代数。给 $\varphi$ 加上常数相位 $\alpha$ 正是 $U(1)$ 变换；它使场沿"墨西哥帽"山谷底部移动，那里由第 1 步 $V$ 为常数。角向涨落 $\pi$ 恰是沿此平坦山谷的局部位移，故回复力——$V$ 沿角向横越谷底的曲率——为零。因此 $m_\pi^2 = \partial^2 V/\partial\pi^2|_{\text{真空}} = 0$ 恒成立。径向方向 $h$ 攀爬壁（曲率 $2\lambda v^2$）；角向方向 $\pi$ 是平坦谷底（曲率 0）。无质量的 $\pi$ 就是破缺 $U(1)$ 的**戈德斯通玻色子**。$\blacksquare$

---

## C. Goldstone's Theorem in General & the Counting $\dim(G) - \dim(H)$ · 一般的戈德斯通定理与计数 $\dim(G) - \dim(H)$

**Claim.** For every spontaneously broken continuous global symmetry generator (one with $Q|0\rangle \ne 0$) of a Lorentz-invariant theory, there exists a massless particle. The number of such Goldstone bosons equals $\dim(G) - \dim(H)$, where $G$ is the symmetry group and $H$ the unbroken subgroup that leaves the vacuum invariant.

**Step 1 — Broken charge and the order parameter.** A continuous symmetry has a conserved Noether current $J^\mu$ with $\partial_\mu J^\mu = 0$ and charge $Q = \int d^3x\, J^0$. The symmetry is *spontaneously broken* when $Q$ does not annihilate the vacuum: $Q|0\rangle \ne 0$. Equivalently there exists a field operator $\Phi$ whose variation has nonzero vacuum expectation, $\langle 0|[Q, \Phi]|0\rangle = c \ne 0$; this $c$ is the order parameter (e.g. $c \propto v$ in Sections A–B).

**Step 2 — Insert a complete set of states.** Write the order parameter using the current. Because $J^0$ creates excitations from the vacuum, insert a complete set of momentum eigenstates $|n\rangle$ between $J^0$ and $\Phi$ in $c = \langle 0|[\int d^3x\, J^0(x), \Phi(0)]|0\rangle$. Translation invariance $J^\mu(x) = e^{iP\cdot x}J^\mu(0)e^{-iP\cdot x}$ fixes the $x$-dependence; carrying out $\int d^3x$ sets the spatial momentum of the intermediate states to zero. The nonvanishing of $c$ then requires at least one intermediate state $|n\rangle$ with $\langle 0|J^0(0)|n\rangle \ne 0$ and $\langle n|\Phi(0)|0\rangle \ne 0$.

**Step 3 — The matrix element and current conservation.** By Lorentz covariance the matrix element of the broken current between the vacuum and the relevant one-particle state $|\pi(p)\rangle$ must take the form

$$ \langle 0|J^\mu(x)|\pi(p)\rangle = i f p^\mu e^{-ip\cdot x}, $$

with a nonzero decay constant $f$ (nonzero precisely because $c \ne 0$ in Step 2 — the state is created by the broken current). Now impose current conservation:

$$ 0 = \partial_\mu\langle 0|J^\mu(x)|\pi(p)\rangle = \partial_\mu(i f p^\mu e^{-ip\cdot x}) = f p_\mu p^\mu e^{-ip\cdot x} = f p^2 e^{-ip\cdot x}. $$

Since $f \ne 0$ and the exponential is nonzero, this forces

$$ p^2 = 0. $$

A relativistic one-particle state with $p^2 = 0$ has zero rest mass: $m^2 = p^2 = 0$. Hence $|\pi(p)\rangle$ is a **massless particle** — the Goldstone boson. $\blacksquare$ (Step 1)

**Step 4 — The counting $\dim(G) - \dim(H)$.** Each broken generator $T_a$ ($a = 1, \ldots, \dim G$) gives a current $J_a^\mu$ and a candidate order-parameter relation $\langle 0|[Q_a, \Phi]|0\rangle$. Split the generators: those of the unbroken subgroup $H$ annihilate the vacuum ($Q_a|0\rangle = 0$ for $T_a \in H$, giving $f = 0$ and no Goldstone), while the remaining $\dim(G) - \dim(H)$ *broken* generators each satisfy $Q_a|0\rangle \ne 0$ and, by Steps 1–3, each produce an independent massless boson. The broken generators span the coset $G/H$ — the tangent space to the vacuum manifold (the "flat valley" of Section B) — so the number of flat directions equals $\dim(G/H) = \dim(G) - \dim(H)$. Therefore

$$ \boxed{\, \text{\# Goldstone bosons} = \dim(G) - \dim(H) \,} \qquad \blacksquare $$

Examples: $U(1) \to \{1\}$ has $\dim G - \dim H = 1 - 0 = 1$ (one Goldstone, Section B); $O(N) \to O(N-1)$ has $\tfrac12 N(N-1) - \tfrac12(N-1)(N-2) = N - 1$ Goldstones; chiral $SU(2)_L \times SU(2)_R \to SU(2)_V$ has $3 + 3 - 3 = 3$ Goldstones (the three pions, Module 8.7). $\blacksquare$

**Claim.** 对洛伦兹不变理论中每个被自发破缺的连续整体对称性生成元（满足 $Q|0\rangle \ne 0$），存在一个无质量粒子。此类戈德斯通玻色子的数目等于 $\dim(G) - \dim(H)$，其中 $G$ 是对称群，$H$ 是使真空不变的未破缺子群。

**第 1 步 — 破缺荷与序参量。** 连续对称性有守恒诺特流 $J^\mu$，满足 $\partial_\mu J^\mu = 0$，荷 $Q = \int d^3x\, J^0$。当 $Q$ 不湮灭真空时对称性*自发破缺*：$Q|0\rangle \ne 0$。等价地，存在场算符 $\Phi$，其变分有非零真空期望，$\langle 0|[Q, \Phi]|0\rangle = c \ne 0$；此 $c$ 即序参量（如 A–B 节中 $c \propto v$）。

**第 2 步 — 插入完备态。** 用流表示序参量。由于 $J^0$ 从真空产生激发，在 $c = \langle 0|[\int d^3x\, J^0(x), \Phi(0)]|0\rangle$ 中于 $J^0$ 与 $\Phi$ 之间插入完备动量本征态 $|n\rangle$。平移不变性 $J^\mu(x) = e^{iP\cdot x}J^\mu(0)e^{-iP\cdot x}$ 固定 $x$ 依赖；执行 $\int d^3x$ 使中间态的空间动量为零。$c$ 不为零便要求至少一个中间态 $|n\rangle$ 满足 $\langle 0|J^0(0)|n\rangle \ne 0$ 且 $\langle n|\Phi(0)|0\rangle \ne 0$。

**第 3 步 — 矩阵元与流守恒。** 由洛伦兹协变性，被破缺流在真空与相关单粒子态 $|\pi(p)\rangle$ 之间的矩阵元必取形式

$$ \langle 0|J^\mu(x)|\pi(p)\rangle = i f p^\mu e^{-ip\cdot x}, $$

衰变常数 $f \ne 0$（非零恰因第 2 步中 $c \ne 0$——该态由被破缺流产生）。现施加流守恒：

$$ 0 = \partial_\mu\langle 0|J^\mu(x)|\pi(p)\rangle = \partial_\mu(i f p^\mu e^{-ip\cdot x}) = f p_\mu p^\mu e^{-ip\cdot x} = f p^2 e^{-ip\cdot x}. $$

由于 $f \ne 0$ 且指数因子非零，这强制

$$ p^2 = 0. $$

$p^2 = 0$ 的相对论性单粒子态静止质量为零：$m^2 = p^2 = 0$。故 $|\pi(p)\rangle$ 是**无质量粒子**——戈德斯通玻色子。$\blacksquare$（第 1 步）

**第 4 步 — 计数 $\dim(G) - \dim(H)$。** 每个破缺生成元 $T_a$（$a = 1, \ldots, \dim G$）给出流 $J_a^\mu$ 和候选序参量关系 $\langle 0|[Q_a, \Phi]|0\rangle$。将生成元分类：未破缺子群 $H$ 的生成元湮灭真空（$T_a \in H$ 时 $Q_a|0\rangle = 0$，给出 $f = 0$，无戈德斯通），而其余 $\dim(G) - \dim(H)$ 个*破缺*生成元各满足 $Q_a|0\rangle \ne 0$，由第 1–3 步各产生一个独立的无质量玻色子。破缺生成元张成陪集 $G/H$——真空流形（B 节"平坦山谷"）的切空间——故平坦方向数等于 $\dim(G/H) = \dim(G) - \dim(H)$。因此

$$ \boxed{\, \text{戈德斯通玻色子数} = \dim(G) - \dim(H) \,} \qquad \blacksquare $$

例子：$U(1) \to \{1\}$ 有 $\dim G - \dim H = 1 - 0 = 1$（一个戈德斯通，B 节）；$O(N) \to O(N-1)$ 有 $\tfrac12 N(N-1) - \tfrac12(N-1)(N-2) = N - 1$ 个戈德斯通；手征 $SU(2)_L \times SU(2)_R \to SU(2)_V$ 有 $3 + 3 - 3 = 3$ 个戈德斯通（三个 $\pi$ 介子，模块 8.7）。$\blacksquare$

---

## D. The Mermin–Wagner Theorem: No Breaking in Low Dimensions · Mermin–Wagner 定理：低维无破缺

**Claim.** A continuous symmetry cannot be spontaneously broken in $d \le 2$ spatial dimensions at finite temperature (or $d \le 1$ in the quantum/zero-temperature case): the would-be Goldstone fluctuations are infrared-divergent and destroy long-range order.

**Step 1 — The Goldstone is the soft mode.** Suppose, for contradiction, the symmetry breaks and a Goldstone field $\pi$ exists. By Section B–C it is massless, so at low energy its effective action is purely the gradient term, $S = \tfrac12\rho_s \int d^dx\, (\nabla\pi)^2$, where $\rho_s$ is the stiffness (spin stiffness / superfluid density). The propagator of a massless field is $\langle\pi(k)\pi(-k)\rangle = 1/(\rho_s k^2)$.

**Step 2 — IR power counting of the fluctuation.** The mean-square fluctuation of the order-parameter phase at a point is the propagator integrated over all momenta (with an IR cutoff $L^{-1}$ from finite system size and a UV cutoff $\Lambda$):

$$ \langle\pi^2\rangle = \int \frac{d^dk}{(2\pi)^d} \cdot \frac{1}{\rho_s k^2} \propto \int_{1/L}^{\Lambda} dk \cdot \frac{k^{d-1}}{k^2} = \int_{1/L} dk \cdot k^{d-3}. $$

Count the IR behavior as the lower limit $1/L \to 0$:
 • $d = 3$: $\int dk\, k^0$ converges at small $k$ $\to \langle\pi^2\rangle$ finite $\to$ order survives.
 • $d = 2$: $\int dk\, k^{-1} = \ln(L\Lambda) \to$ **logarithmically divergent** as $L \to \infty$.
 • $d = 1$: $\int dk\, k^{-2} \propto L \to$ **linearly divergent** as $L \to \infty$.

**Step 3 — Divergence destroys order.** The order parameter is $\langle e^{i\pi}\rangle \sim e^{-\tfrac12\langle\pi^2\rangle}$ (Gaussian fluctuations). In $d \le 2$ the divergent $\langle\pi^2\rangle \to \infty$ drives $e^{-\tfrac12\langle\pi^2\rangle} \to 0$: the average order parameter vanishes in the thermodynamic limit. The infrared-divergent Goldstone fluctuations wash out the long-range order, so no symmetry breaking can occur. This is the **Mermin–Wagner (–Hohenberg–Coleman) theorem**. (Discrete symmetries are exempt — they have no Goldstone soft mode — which is why the 2D Ising model orders but the 2D Heisenberg model does not. The marginal $d = 2$ case admits the Berezinskii–Kosterlitz–Thouless transition with quasi-long-range order instead of true order.) $\blacksquare$

**Claim.** 连续对称性在 $d \le 2$ 空间维有限温度下（或量子/零温情形下 $d \le 1$）不能自发破缺：本应的戈德斯通涨落红外发散，破坏长程序。

**第 1 步 — 戈德斯通是软模。** 反证：设对称性破缺且存在戈德斯通场 $\pi$。由 B–C 节它无质量，故低能下其有效作用量纯为梯度项，$S = \tfrac12\rho_s \int d^dx\, (\nabla\pi)^2$，$\rho_s$ 为劲度（自旋劲度/超流密度）。无质量场的传播子为 $\langle\pi(k)\pi(-k)\rangle = 1/(\rho_s k^2)$。

**第 2 步 — 涨落的红外幂计数。** 序参量相位在一点的均方涨落是传播子对全动量的积分（红外截断 $L^{-1}$ 来自有限系统尺寸，紫外截断 $\Lambda$）：

$$ \langle\pi^2\rangle = \int \frac{d^dk}{(2\pi)^d} \cdot \frac{1}{\rho_s k^2} \propto \int_{1/L}^{\Lambda} dk \cdot \frac{k^{d-1}}{k^2} = \int_{1/L} dk \cdot k^{d-3}. $$

考察下限 $1/L \to 0$ 时的红外行为：
 • $d = 3$：$\int dk\, k^0$ 在小 $k$ 收敛 $\to \langle\pi^2\rangle$ 有限 $\to$ 序保留。
 • $d = 2$：$\int dk\, k^{-1} = \ln(L\Lambda) \to$ 随 $L \to \infty$ **对数发散**。
 • $d = 1$：$\int dk\, k^{-2} \propto L \to$ 随 $L \to \infty$ **线性发散**。

**第 3 步 — 发散破坏序。** 序参量为 $\langle e^{i\pi}\rangle \sim e^{-\tfrac12\langle\pi^2\rangle}$（高斯涨落）。在 $d \le 2$ 中发散的 $\langle\pi^2\rangle \to \infty$ 使 $e^{-\tfrac12\langle\pi^2\rangle} \to 0$：热力学极限下平均序参量消失。红外发散的戈德斯通涨落抹去长程序，故不能发生对称性破缺。这就是 **Mermin–Wagner（–Hohenberg–Coleman）定理**。（离散对称性除外——它们无戈德斯通软模——这正是二维伊辛模型有序而二维海森堡模型无序的原因。边缘的 $d = 2$ 情形允许 Berezinskii–Kosterlitz–Thouless 相变，呈准长程序而非真长程序。）$\blacksquare$

---

## E. Contrast with Gauge Theories: the Goldstone Is Eaten · 与规范理论的对比：戈德斯通被吞噬

**Claim.** When the spontaneously broken symmetry is *gauged* (local) rather than global, no physical massless Goldstone boson appears: the Goldstone degree of freedom becomes the longitudinal polarization of a gauge boson, which thereby acquires a mass. This is the Higgs mechanism.

**Step 1 — Gauge the $U(1)$.** Promote the global $U(1)$ of Section B to a local symmetry $\varphi \to e^{i\alpha(x)}\varphi$ by introducing a gauge field $A_\mu$ with covariant derivative $D_\mu\varphi = (\partial_\mu - ieA_\mu)\varphi$ and $A_\mu \to A_\mu + (1/e)\partial_\mu\alpha$. The Lagrangian is $\mathcal{L} = -\tfrac14 F_{\mu\nu}F^{\mu\nu} + |D_\mu\varphi|^2 - V(\varphi)$ with the same Mexican-hat $V$. The vacuum is still $\langle\varphi\rangle = v/\sqrt{2}$.

**Step 2 — Counting the degrees of freedom.** Before breaking: a massless gauge field $A_\mu$ has 2 physical polarizations, and the complex scalar $\varphi$ has 2 real components ($h$ and the would-be Goldstone $\pi$) — total 4. The $\pi$ is the flat-direction mode of Section B.

**Step 3 — The Goldstone is eaten.** Expand the kinetic term $|D_\mu\varphi|^2$ about the vacuum. The cross term contains, from $D_\mu\varphi \supset (\partial_\mu - ieA_\mu)(v/\sqrt{2})$, a piece $\propto e v A_\mu \partial^\mu\pi$ — a kinetic mixing between $A_\mu$ and the Goldstone $\pi$. Use the local gauge freedom to choose the **unitary gauge**: pick $\alpha(x)$ to rotate away the phase of $\varphi$, i.e. set $\pi \to 0$ everywhere. The Goldstone field is gauged away; it does not appear as an independent physical state. The remaining $|D_\mu\varphi|^2$ expanded with $\varphi = (v + h)/\sqrt{2}$ gives a mass term for the gauge field,

$$ |D_\mu\varphi|^2 \supset \tfrac12 e^2 v^2\, A_\mu A^\mu \implies m_A^2 = e^2 v^2. $$

The gauge boson is now **massive**.

**Step 4 — The bookkeeping balances.** After breaking: a massive vector has 3 physical polarizations (2 transverse + 1 longitudinal), and the real scalar $h$ remains (1) — total 4, matching Step 2. The one degree of freedom that was the massless Goldstone $\pi$ has become the *longitudinal* polarization of the now-massive gauge boson: the gauge field "ate" the Goldstone. Hence in the gauged (Higgs) case there is **no physical massless Goldstone particle**, in sharp contrast to the global case (Sections B–C) where the Goldstone is a genuine massless physical state. The full non-abelian treatment, giving masses to the W and Z, is Module 8.4. $\blacksquare$

**Claim.** 当被自发破缺的对称性是*规范*（局域）而非整体的时，不出现物理的无质量戈德斯通玻色子：戈德斯通自由度成为规范玻色子的纵向极化，规范玻色子因而获得质量。这就是希格斯机制。

**第 1 步 — 规范化 $U(1)$。** 将 B 节的整体 $U(1)$ 提升为局域对称性 $\varphi \to e^{i\alpha(x)}\varphi$，引入规范场 $A_\mu$，协变导数 $D_\mu\varphi = (\partial_\mu - ieA_\mu)\varphi$，$A_\mu \to A_\mu + (1/e)\partial_\mu\alpha$。拉格朗日量为 $\mathcal{L} = -\tfrac14 F_{\mu\nu}F^{\mu\nu} + |D_\mu\varphi|^2 - V(\varphi)$，$V$ 仍为墨西哥帽形。真空仍为 $\langle\varphi\rangle = v/\sqrt{2}$。

**第 2 步 — 自由度计数。** 破缺前：无质量规范场 $A_\mu$ 有 2 个物理极化，复标量 $\varphi$ 有 2 个实分量（$h$ 与本应的戈德斯通 $\pi$）——共 4 个。$\pi$ 是 B 节的平坦方向模。

**第 3 步 — 戈德斯通被吞噬。** 围绕真空展开动能项 $|D_\mu\varphi|^2$。交叉项含有来自 $D_\mu\varphi \supset (\partial_\mu - ieA_\mu)(v/\sqrt{2})$ 的一项 $\propto e v A_\mu \partial^\mu\pi$——$A_\mu$ 与戈德斯通 $\pi$ 之间的动能混合。用局域规范自由选取**幺正规范**：取 $\alpha(x)$ 旋转掉 $\varphi$ 的相位，即处处令 $\pi \to 0$。戈德斯通场被规范掉，不作为独立物理态出现。剩余的 $|D_\mu\varphi|^2$ 以 $\varphi = (v + h)/\sqrt{2}$ 展开给出规范场的质量项，

$$ |D_\mu\varphi|^2 \supset \tfrac12 e^2 v^2\, A_\mu A^\mu \implies m_A^2 = e^2 v^2. $$

规范玻色子现在**有质量**。

**第 4 步 — 计数平衡。** 破缺后：有质量矢量有 3 个物理极化（2 横向 + 1 纵向），实标量 $h$ 保留（1）——共 4 个，与第 2 步相符。曾是无质量戈德斯通 $\pi$ 的那个自由度已成为如今有质量规范玻色子的*纵向*极化：规范场"吃掉"了戈德斯通。故在规范（希格斯）情形中**不存在物理的无质量戈德斯通粒子**，与整体情形（B–C 节）戈德斯通为真正无质量物理态形成鲜明对比。给 W 与 Z 赋予质量的完整非阿贝尔处理见模块 8.4。$\blacksquare$

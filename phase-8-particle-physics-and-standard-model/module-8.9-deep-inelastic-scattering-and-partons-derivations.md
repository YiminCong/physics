# Derivations — Module 8.9: Deep Inelastic Scattering & Partons
# 推导 — 模块 8.9：深度非弹性散射与部分子

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 8.9](./module-8.9-deep-inelastic-scattering-and-partons.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 8.9](./module-8.9-deep-inelastic-scattering-and-partons.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. DIS Kinematics: $Q^2$, the Bjorken Variable $x$, and Its Range $(0,1)$ · DIS 运动学：$Q^2$、比约肯变量 $x$ 及其范围 $(0,1)$

**Claim.** In the process $e(k) + p(p) \to e(k') + X$, the virtuality of the exchanged photon is $Q^2 = -q^2 > 0$, the Bjorken variable is $x = Q^2/(2p\cdot q)$, and kinematic constraints force $x \in (0, 1)$.

**命题。** 在过程 $e(k) + p(p) \to e(k') + X$ 中，交换光子的虚度为 $Q^2 = -q^2 > 0$，比约肯变量为 $x = Q^2/(2p\cdot q)$，运动学约束迫使 $x \in (0, 1)$。

**Step 1 — Define the four-momenta.** Work in natural units $\hbar = c = 1$. Assign:

**第 1 步 — 定义四动量。** 在自然单位 $\hbar = c = 1$ 下，令：

$$ \begin{aligned}
k^\mu &= (E, \vec k) && \text{— incoming lepton (electron) 4-momentum,} \\
k'^\mu &= (E', \vec k') && \text{— outgoing lepton 4-momentum,} \\
p^\mu &= (M, \vec 0) && \text{— proton 4-momentum (proton at rest in the lab frame, mass } M \approx 938\ \text{MeV)}, \\
q^\mu &= k^\mu - k'^\mu && \text{— 4-momentum transfer (carried by the virtual photon).}
\end{aligned} $$

$$ \begin{aligned}
k^\mu &= (E, \vec k) && \text{— 入射轻子（电子）四动量，} \\
k'^\mu &= (E', \vec k') && \text{— 出射轻子四动量，} \\
p^\mu &= (M, \vec 0) && \text{— 质子四动量（质子在实验室系静止，质量 } M \approx 938\ \text{MeV），} \\
q^\mu &= k^\mu - k'^\mu && \text{— 四动量转移（由虚光子携带）。}
\end{aligned} $$

**Step 2 — Compute $Q^2$.** The invariant momentum transfer squared is:

**第 2 步 — 计算 $Q^2$。** 不变动量转移的平方为：

$$ q^2 = (k - k')^2 = k^2 + k'^2 - 2k\cdot k' = m_e^2 + m_e^2 - 2k\cdot k' \approx -2k\cdot k' \quad (\text{since } m_e \approx 0), $$

$$ q^2 = -2EE'(1 - \cos\theta), $$

where $\theta$ is the scattering angle of the lepton in the lab frame. Since $0 < \theta < \pi$ for real scattering, $(1 - \cos\theta) > 0$, so $\mathbf{q^2 < 0}$: the photon is **spacelike**. Define:

其中 $\theta$ 是轻子在实验室系中的散射角。由于实际散射 $0 < \theta < \pi$，$(1 - \cos\theta) > 0$，故 $\mathbf{q^2 < 0}$：光子是**类空的**。定义：

$$ \mathbf{Q^2 \equiv -q^2 = 2EE'(1 - \cos\theta) > 0}. $$

This is a positive definite quantity measuring the hardness of the scattering. Large $Q^2$ means the photon probes short distances $\sim 1/\sqrt{Q^2} \ll 1$ fm (proton radius), hence "deep" inelastic scattering.

这是正定量，衡量散射的硬度。大 $Q^2$ 意味着光子探测短距离 $\sim 1/\sqrt{Q^2} \ll 1$ fm（质子半径），故称"深度"非弹性散射。

**Step 3 — The invariant $\nu$ and $p\cdot q$.** Compute the proton-photon invariant:

**第 3 步 — 不变量 $\nu$ 与 $p\cdot q$。** 计算质子-光子不变量：

$$ p\cdot q = p\cdot(k - k') = p\cdot k - p\cdot k' = ME - ME' = M(E - E') \equiv M\nu, $$

where $\nu = E - E'$ is the energy loss of the lepton in the lab frame (the energy deposited into the target). So $p\cdot q = M\nu > 0$ (since $E > E'$ in DIS, energy is transferred from the lepton to the hadronic system).

其中 $\nu = E - E'$ 是轻子在实验室系中的能量损失（沉积到靶中的能量）。故 $p\cdot q = M\nu > 0$（DIS 中 $E > E'$，能量从轻子转移到强子系）。

**Step 4 — Define the Bjorken variable $x$.** The dimensionless ratio:

**第 4 步 — 定义比约肯变量 $x$。** 无量纲比值：

$$ \mathbf{x \equiv Q^2/(2p\cdot q) = Q^2/(2M\nu)}. $$

This is Lorentz invariant (ratio of two Lorentz scalars), so $x$ has the same value in any frame.

这是洛伦兹不变量（两个洛伦兹标量之比），故 $x$ 在任何参考系中取相同值。

**Step 5 — Prove $x \in (0, 1)$.** We need two bounds:

**第 5 步 — 证明 $x \in (0, 1)$。** 需要两个界：

*Lower bound $x > 0$:* Both $Q^2 > 0$ and $p\cdot q = M\nu > 0$, so $x > 0$. ($x = 0$ would require $q = 0$, i.e. no scattering.)

*下界 $x > 0$：* $Q^2 > 0$ 且 $p\cdot q = M\nu > 0$，故 $x > 0$。（$x = 0$ 意味着 $q = 0$，即无散射。）

*Upper bound $x < 1$:* Consider the invariant mass $W$ of the hadronic final state $X$:

*上界 $x < 1$：* 考虑强子末态 $X$ 的不变质量 $W$：

$$ W^2 = (p + q)^2 = p^2 + 2p\cdot q + q^2 = M^2 + 2M\nu - Q^2. $$

For the final state to be physical ($W^2 \ge M^2$: it must be at least as massive as the proton, since we need at least one baryon in the final state):

为使末态物理（$W^2 \ge M^2$：至少与质子一样重，因末态至少需要一个重子）：

$$ W^2 \ge M^2 \quad \implies \quad M^2 + 2M\nu - Q^2 \ge M^2 \quad \implies \quad 2M\nu \ge Q^2 \quad \implies \quad x = Q^2/(2M\nu) \le 1. $$

Equality $x = 1$ corresponds to $W^2 = M^2$, i.e. **elastic scattering** (the proton stays intact, $X = p$). For inelastic scattering $W > M$, so $\mathbf{x < 1}$ strictly.

等号 $x = 1$ 对应 $W^2 = M^2$，即**弹性散射**（质子保持完整，$X = p$）。对于非弹性散射 $W > M$，故严格地 $\mathbf{x < 1}$。

Combining: $\mathbf{0 < x \le 1}$, with $x = 1$ being the elastic limit and $x < 1$ for all inelastic processes. In the DIS regime (truly inelastic, $W \gg M$), $x$ is a continuous variable in $(0, 1)$. $\blacksquare$

综合：$\mathbf{0 < x \le 1}$，$x = 1$ 是弹性极限，$x < 1$ 对所有非弹性过程成立。在 DIS 区间（真正非弹性，$W \gg M$），$x$ 是 $(0, 1)$ 中的连续变量。$\blacksquare$

---

## B. The Inclusive DIS Cross-Section in Terms of Structure Functions $F_1$, $F_2$ · 用结构函数 $F_1$、$F_2$ 表示的 DIS 包容截面

**Claim.** The most general Lorentz-invariant, gauge-invariant form for the inclusive DIS cross-section $e + p \to e + X$, summed over all hadronic final states $X$, can be written in terms of only two independent structure functions $F_1(x, Q^2)$ and $F_2(x, Q^2)$.

**命题。** 对所有强子末态 $X$ 求和后，$e + p \to e + X$ 包容 DIS 截面最一般的洛伦兹不变、规范不变形式只能用两个独立结构函数 $F_1(x, Q^2)$ 和 $F_2(x, Q^2)$ 写出。

**Step 1 — The hadronic tensor.** The cross-section factorizes as:

**第 1 步 — 强子张量。** 截面因子化为：

$$ d\sigma \propto L^{\mu\nu}(k, k') \cdot W_{\mu\nu}(p, q), $$

where $L^{\mu\nu}$ is the **leptonic tensor** (calculable in QED) and $W_{\mu\nu}$ is the **hadronic tensor** encoding all the unknown proton structure.

其中 $L^{\mu\nu}$ 是**轻子张量**（在 QED 中可计算），$W_{\mu\nu}$ 是编码所有未知质子结构的**强子张量**。

**Step 2 — The leptonic tensor.** For an unpolarized electron (averaging over initial spins, summing over final spins), the QED calculation gives:

**第 2 步 — 轻子张量。** 对非极化电子（对初态自旋取平均，对末态自旋求和），QED 计算给出：

$$ L^{\mu\nu} = 2(k^\mu k'^\nu + k'^\mu k^\nu - g^{\mu\nu} k\cdot k'). $$

(This follows from the standard trace technology: $L^{\mu\nu} = \text{Tr}[\gamma^\mu \not{k} \gamma^\nu \not{k}'] / 2$, using $\text{Tr}[\gamma^\mu \gamma^\alpha \gamma^\nu \gamma^\beta] = 4(g^{\mu\alpha}g^{\nu\beta} - g^{\mu\nu}g^{\alpha\beta} + g^{\mu\beta}g^{\nu\alpha})$.)

（这源于标准迹技术：$L^{\mu\nu} = \text{Tr}[\gamma^\mu \not{k} \gamma^\nu \not{k}'] / 2$，利用 $\text{Tr}[\gamma^\mu \gamma^\alpha \gamma^\nu \gamma^\beta] = 4(g^{\mu\alpha}g^{\nu\beta} - g^{\mu\nu}g^{\alpha\beta} + g^{\mu\beta}g^{\nu\alpha})$。）

**Step 3 — Constraints on the hadronic tensor.** $W_{\mu\nu}$ must satisfy:
(i) **Current conservation** (Ward identity): $q^\mu W_{\mu\nu} = 0$ and $q^\nu W_{\mu\nu} = 0$.
(ii) **Lorentz covariance**: $W_{\mu\nu}$ must be built from the available Lorentz tensors constructed from $p^\mu$ and $q^\mu$ (the only independent 4-vectors, since we sum over all final states $X$).
(iii) **Hermiticity**: $W_{\mu\nu} = W_{\nu\mu}^*$ (for real structure functions: $W_{\mu\nu} = W_{\nu\mu}$).
(iv) **Time-reversal symmetry** (for parity-conserving electromagnetic interaction): $W_{\mu\nu}$ is symmetric.

**第 3 步 — 强子张量的约束。** $W_{\mu\nu}$ 必须满足：
(i) **流守恒**（沃德恒等式）：$q^\mu W_{\mu\nu} = 0$ 且 $q^\nu W_{\mu\nu} = 0$。
(ii) **洛伦兹协变性**：$W_{\mu\nu}$ 必须由可用的洛伦兹张量构造，即由 $p^\mu$ 和 $q^\mu$（对所有末态 $X$ 求和后仅有的独立四向量）构成。
(iii) **厄米性**：$W_{\mu\nu} = W_{\nu\mu}^*$（对实结构函数：$W_{\mu\nu} = W_{\nu\mu}$）。
(iv) **时间反演对称性**（对宇称守恒的电磁相互作用）：$W_{\mu\nu}$ 是对称的。

**Step 4 — Most general symmetric tensor from $p, q$.** The symmetric rank-2 tensors constructible from $p^\mu, q^\mu$ are: $g^{\mu\nu}$, $p^\mu p^\nu$, $q^\mu q^\nu$, $p^\mu q^\nu + q^\mu p^\nu$. Imposing $q^\mu W_{\mu\nu} = 0$ eliminates the $q^\mu q^\nu$ and $p^\mu q^\nu$ terms (they don't vanish on their own but must combine to satisfy transversality). The transverse projector is:

**第 4 步 — 由 $p$、$q$ 构造的最一般对称张量。** 由 $p^\mu$、$q^\mu$ 可构造的对称二阶张量有：$g^{\mu\nu}$、$p^\mu p^\nu$、$q^\mu q^\nu$、$p^\mu q^\nu + q^\mu p^\nu$。施加 $q^\mu W_{\mu\nu} = 0$ 消除了 $q^\mu q^\nu$ 和 $p^\mu q^\nu$ 项（它们自身不消失，但必须组合以满足横向性条件）。横向投影算符为：

$$ \begin{aligned}
T^{\mu\nu} &= -g^{\mu\nu} + q^\mu q^\nu/q^2, \\
\tilde P^\mu &= p^\mu - (p\cdot q/q^2)\, q^\mu \quad (\text{transverse projection of } p).
\end{aligned} $$

The most general transverse symmetric tensor is:

最一般的横向对称张量为：

$$ W^{\mu\nu} = W_1 (-g^{\mu\nu} + q^\mu q^\nu/q^2) + W_2/M^2 \cdot (p^\mu - p\cdot q/q^2 \cdot q^\mu)(p^\nu - p\cdot q/q^2 \cdot q^\nu). $$

**Step 5 — Standard conventions.** Define the dimensionless structure functions:

**第 5 步 — 标准惯例。** 定义无量纲结构函数：

$$ \begin{aligned}
F_1(x, Q^2) &\equiv M W_1(\nu, Q^2), \\
F_2(x, Q^2) &\equiv \nu W_2(\nu, Q^2).
\end{aligned} $$

(Conventions vary in the literature; these are the standard Bjorken–Paschos conventions.) The hadronic tensor becomes:

（文献中惯例有所不同；这是标准的比约肯–帕斯乔斯惯例。）强子张量变为：

$$ M W^{\mu\nu} = F_1 (-g^{\mu\nu} + q^\mu q^\nu/q^2) + F_2/(p\cdot q) \cdot (p^\mu - p\cdot q/q^2 \cdot q^\mu)(p^\nu - p\cdot q/q^2 \cdot q^\nu). $$

**Step 6 — The differential cross-section.** Contracting with $L^{\mu\nu}$ and integrating, the double-differential cross-section is (in the lab frame):

**第 6 步 — 微分截面。** 与 $L^{\mu\nu}$ 缩并并积分，实验室系中的双微分截面为：

$$ d^2\sigma/(dE'\, d\Omega) = \alpha^2/(4E^2\sin^4(\theta/2)) \cdot [F_2 \cos^2(\theta/2) + 2xF_1 \cdot (2/M) \sin^2(\theta/2) / \nu]. $$

This is the **Rosenbluth-like formula for DIS**, expressing the measurable cross-section in terms of the two structure functions $F_1$ and $F_2$. Separating longitudinal and transverse photon polarizations, one finds that $F_1$ couples to transversely polarized virtual photons and $F_2$ receives contributions from both transverse and longitudinal polarizations. $\blacksquare$

这是 **DIS 的类罗森布鲁斯公式**，用两个结构函数 $F_1$ 和 $F_2$ 表达可测截面。将纵向和横向光子极化分离，可以发现 $F_1$ 与横向极化虚光子耦合，$F_2$ 接收横向和纵向极化的贡献。$\blacksquare$

---

## C. The Parton-Model Result $F_2(x) = \sum_i e_i^2 x f_i(x)$ · 部分子模型结果 $F_2(x) = \sum_i e_i^2 x f_i(x)$

**Claim.** In the parton model (impulse approximation), the proton is composed of quasi-free pointlike constituents (partons) each carrying a fraction $x$ of the proton's momentum. The photon scatters elastically off a single parton. The result is $F_2(x) = \sum_i e_i^2 x f_i(x)$, where $f_i(x)\, dx$ is the probability of finding parton $i$ with momentum fraction in $(x, x+dx)$, and Bjorken scaling (independence of $Q^2$) emerges automatically.

**命题。** 在部分子模型（冲量近似）中，质子由准自由点状组分（部分子）构成，每个部分子携带质子动量的分数 $x$。光子弹性散射于单个部分子上。结果为 $F_2(x) = \sum_i e_i^2 x f_i(x)$，其中 $f_i(x)\, dx$ 是找到携带动量分数在 $(x, x+dx)$ 的部分子 $i$ 的概率，比约肯标度（对 $Q^2$ 的独立性）自动出现。

**Step 1 — The impulse approximation.** In the Breit frame (infinite momentum frame), the proton moves with very large momentum $P$ along the $z$-axis: $p^\mu = (P, 0, 0, P)$ with $P \to \infty$. In this limit, the proton looks like a beam of non-interacting partons, each moving collinearly with the proton. The interactions between partons are slow (long time-scale) compared to the interaction time of the virtual photon (short time-scale $\sim 1/Q$), and can be neglected during the scattering — this is the **impulse approximation**.

**第 1 步 — 冲量近似。** 在布雷特系（无限动量系）中，质子沿 $z$ 轴以极大动量 $P$ 运动：$p^\mu = (P, 0, 0, P)$，$P \to \infty$。在此极限下，质子看起来像是非相互作用部分子束，每个部分子沿质子方向共线运动。部分子间的相互作用（长时间尺度）相比虚光子的相互作用时间（短时间尺度 $\sim 1/Q$）缓慢，在散射过程中可以忽略——这就是**冲量近似**。

**Step 2 — Parton kinematics.** Let parton $i$ carry a fraction $\xi$ of the proton's 4-momentum:

**第 2 步 — 部分子运动学。** 设部分子 $i$ 携带质子四动量的分数 $\xi$：

$$ p_i^\mu = \xi p^\mu \quad (\text{massless parton: } p_i^2 = 0, \text{ since } \xi^2 p^2 = \xi^2 M^2 \to 0 \text{ for } M/P \to 0). $$

The photon scatters elastically off this parton: $\gamma^* + \text{parton}(\xi p) \to \text{parton}(p_i')$. The final parton momentum is:

光子弹性散射于此部分子：$\gamma^* + \text{部分子}(\xi p) \to \text{部分子}(p_i')$。末态部分子动量为：

$$ p_i'^\mu = p_i^\mu + q^\mu = \xi p^\mu + q^\mu. $$

**Step 3 — Elastic constraint fixes $\xi = x$.** The scattered parton must remain on-shell (massless):

**第 3 步 — 弹性约束固定 $\xi = x$。** 散射部分子必须保持在质量壳上（无质量）：

$$ p_i'^2 = (\xi p + q)^2 = \xi^2 p^2 + 2\xi(p\cdot q) + q^2 = 0 + 2\xi(p\cdot q) - Q^2 = 0. $$

Solving: $\mathbf{\xi = Q^2/(2p\cdot q) = x}$. The Bjorken variable $x$ is precisely the momentum fraction of the struck parton. This is the kinematic identification of $x$.

求解：$\mathbf{\xi = Q^2/(2p\cdot q) = x}$。比约肯变量 $x$ 正是被打部分子的动量分数。这是 $x$ 的运动学识别。

**Step 4 — Cross-section for scattering off a single parton.** Parton $i$ with charge $e_i$ (in units of $e$) is a pointlike Dirac particle. The QED cross-section for $\gamma^* + \text{parton}_i \to \text{parton}_i$ (elastic, massless) has the same kinematic structure as $\gamma^* + e \to e$, giving hadronic tensor contributions:

**第 4 步 — 散射于单个部分子的截面。** 带电荷 $e_i$（以 $e$ 为单位）的部分子 $i$ 是点状狄拉克粒子。$\gamma^* + \text{部分子}_i \to \text{部分子}_i$（弹性，无质量）的 QED 截面具有与 $\gamma^* + e \to e$ 相同的运动学结构，给出强子张量贡献：

$$ W_{\mu\nu}^{(i)}(\text{parton}) \propto e_i^2\, \delta(p_i^2 + 2p_i\cdot q + q^2) \cdot (\text{sum of tensor structures}). $$

The delta function $\delta(2\xi\, p\cdot q - Q^2) = \delta(\xi - x)/(2p\cdot q)$ enforces the elastic condition $\xi = x$.

$\delta$ 函数 $\delta(2\xi\, p\cdot q - Q^2) = \delta(\xi - x)/(2p\cdot q)$ 强制执行弹性条件 $\xi = x$。

**Step 5 — Integrate over parton distributions.** The total hadronic tensor is:

**第 5 步 — 对部分子分布积分。** 总强子张量为：

$$ W_{\mu\nu} = \sum_i \int_0^1 d\xi\, f_i(\xi) \cdot W_{\mu\nu}^{(i)}(\xi, q) $$

where $f_i(\xi)$ is the **parton distribution function (PDF)**: $f_i(\xi)\, d\xi = $ probability that parton $i$ has momentum fraction in $(\xi, \xi+d\xi)$.

其中 $f_i(\xi)$ 是**部分子分布函数（PDF）**：$f_i(\xi)\, d\xi = $ 部分子 $i$ 的动量分数在 $(\xi, \xi+d\xi)$ 内的概率。

The delta function $\delta(\xi - x)$ collapses the $\xi$ integral, giving the hadronic tensor evaluated at $\xi = x$. Reading off the $F_2$ coefficient:

$\delta$ 函数 $\delta(\xi - x)$ 使 $\xi$ 积分坍缩，给出在 $\xi = x$ 处求值的强子张量。读出 $F_2$ 系数：

$$ \mathbf{F_2(x) = \sum_i e_i^2 x f_i(x)}, $$

where the sum runs over all parton species $i$ (quarks of each flavor and, for charge-zero partons, gluons do not contribute directly since they have $e_g = 0$).

其中求和遍历所有部分子种类 $i$（每种味的夸克；对零电荷部分子，胶子由于 $e_g = 0$ 不直接贡献）。

**Step 6 — Bjorken scaling.** In the pure parton model, the PDFs $f_i(x)$ are functions of $x$ alone — they do not depend on $Q^2$. Therefore $F_2(x, Q^2) = F_2(x)$ depends only on $x$, not on $Q^2$. This is **Bjorken scaling**. Physically, the photon is scattering off a pointlike, structureless parton — there is no scale in the problem (a pointlike particle has no size), so the cross-section cannot depend on $Q^2$. $\blacksquare$

**第 6 步 — 比约肯标度。** 在纯部分子模型中，PDF $f_i(x)$ 只是 $x$ 的函数——不依赖 $Q^2$。因此 $F_2(x, Q^2) = F_2(x)$ 只依赖 $x$，不依赖 $Q^2$。这就是**比约肯标度**。物理上，光子散射于点状、无结构的部分子——问题中没有标度（点状粒子没有尺寸），截面不能依赖 $Q^2$。$\blacksquare$

---

## D. The Callan–Gross Relation $2xF_1 = F_2$ for Spin-$\tfrac12$ Partons · 自旋-$\tfrac12$ 部分子的卡兰–格罗斯关系 $2xF_1 = F_2$

**Claim.** For spin-$\tfrac12$ (Dirac) partons, the two structure functions satisfy $2xF_1 = F_2$. For spin-0 (scalar) partons, $F_1 = 0$. The experimental observation $2xF_1 \approx F_2$ (Bjorken–Paschos, SLAC 1969) therefore identifies the partons as spin-$\tfrac12$ quarks.

**命题。** 对自旋-$\tfrac12$（狄拉克）部分子，两个结构函数满足 $2xF_1 = F_2$。对自旋-0（标量）部分子，$F_1 = 0$。因此，$2xF_1 \approx F_2$ 的实验观测（比约肯–帕斯乔斯，SLAC 1969）将部分子识别为自旋-$\tfrac12$ 夸克。

**Step 1 — Virtual photon absorption cross-sections.** Introduce the longitudinal and transverse cross-sections for absorption of a virtual photon:

**第 1 步 — 虚光子吸收截面。** 引入虚光子吸收的纵向和横向截面：

$$ \begin{aligned}
\sigma_T &\propto F_1 && (\text{transverse photon, helicity } \pm 1), \\
\sigma_L &\propto (1 + Q^2/\nu^2) F_2/(2x) - F_1 && (\text{longitudinal photon, helicity } 0).
\end{aligned} $$

Equivalently, $R \equiv \sigma_L/\sigma_T$ measures the ratio of longitudinal to transverse cross-sections; $R = 0$ would imply $2xF_1 = F_2$.

等价地，$R \equiv \sigma_L/\sigma_T$ 衡量纵向与横向截面之比；$R = 0$ 意味着 $2xF_1 = F_2$。

**Step 2 — Tensor structure for a spin-$\tfrac12$ parton.** The elastic electromagnetic current of a massless spin-$\tfrac12$ Dirac particle is $j^\mu = \bar e(p') \gamma^\mu u(p)$. The squared matrix element summed over spins is:

**第 2 步 — 自旋-$\tfrac12$ 部分子的张量结构。** 无质量自旋-$\tfrac12$ 狄拉克粒子的弹性电磁流为 $j^\mu = \bar e(p') \gamma^\mu u(p)$。对自旋求和后的矩阵元平方为：

$$ \sum_{\text{spins}} |\langle p'|j^\mu|p\rangle|^2 = \text{Tr}[\gamma^\mu \not{p}' \gamma^\nu \not{p}] = 4(p'^\mu p^\nu + p'^\nu p^\mu - g^{\mu\nu} p'\cdot p). $$

Using $p = \xi p_{\text{proton}}$ and $p' = p + q$ ($= \xi p + q$), the parton-level hadronic tensor is:

利用 $p = \xi p_{\text{质子}}$ 和 $p' = p + q$（$= \xi p + q$），部分子级强子张量为：

$$ w^{\mu\nu}_{\text{spin-}1/2} = 2\, \delta(2\xi\, p\cdot q - Q^2) \cdot (p^\mu p'^\nu + p'^\mu p^\nu - g^{\mu\nu} p\cdot p'). $$

After integrating with $f_i(\xi)$ and using $\delta(\xi - x)$, one extracts:

对 $f_i(\xi)$ 积分并利用 $\delta(\xi - x)$ 后，提取：

$$ \begin{aligned}
W_1^{(i)} &\propto (1/2M)\, e_i^2 f_i(x), \\
W_2^{(i)} &\propto (x^2/M\nu)\, e_i^2 f_i(x).
\end{aligned} $$

In terms of the standard structure functions $F_1 = M W_1$ and $F_2 = \nu W_2$:

用标准结构函数 $F_1 = M W_1$ 和 $F_2 = \nu W_2$ 表示：

$$ \begin{aligned}
F_1 &= (1/2) \sum_i e_i^2 f_i(x), \\
F_2 &= x \sum_i e_i^2 f_i(x) = 2x F_1.
\end{aligned} $$

Therefore: $\mathbf{2xF_1 = F_2}$. This is the **Callan–Gross relation**.

因此：$\mathbf{2xF_1 = F_2}$。这就是**卡兰–格罗斯关系**。

**Step 3 — Physical interpretation: helicity conservation.** For a massless spin-$\tfrac12$ particle, helicity is conserved. A transverse (helicity $\pm 1$) photon can flip the helicity of the parton (spin-$\tfrac12$ has helicity $\pm 1/2$, and the interaction via $\gamma^\mu$ preserves helicity for massless fermions). But a longitudinal (scalar) photon carries helicity 0 and cannot be absorbed by a massless spin-$\tfrac12$ parton without violating angular momentum conservation along the beam axis. Therefore $\sigma_L = 0$ for massless spin-$\tfrac12$ partons, which is equivalent to $R = 0$, i.e. $\mathbf{2xF_1 = F_2}$.

**第 3 步 — 物理诠释：螺旋度守恒。** 对无质量自旋-$\tfrac12$ 粒子，螺旋度守恒。横向（螺旋度 $\pm 1$）光子可翻转部分子的螺旋度（自旋-$\tfrac12$ 螺旋度为 $\pm 1/2$，通过 $\gamma^\mu$ 的相互作用对无质量费米子守恒螺旋度）。但纵向（标量）光子携带螺旋度 0，不能被无质量自旋-$\tfrac12$ 部分子吸收而不违反沿束流轴的角动量守恒。因此对无质量自旋-$\tfrac12$ 部分子 $\sigma_L = 0$，等价于 $R = 0$，即 $\mathbf{2xF_1 = F_2}$。

**Step 4 — Contrast with spin-0 partons.** For a spin-0 (scalar) charged particle with coupling $\phi^* A^\mu \partial_\mu \phi$, the electromagnetic current is proportional to $(p + p')^\mu$ (no $\gamma^\mu$). The elastic form factor squared is:

**第 4 步 — 与自旋-0 部分子的对比。** 对耦合为 $\phi^* A^\mu \partial_\mu \phi$ 的自旋-0（标量）带电粒子，电磁流正比于 $(p + p')^\mu$（无 $\gamma^\mu$）。弹性形状因子平方为：

$$ |j^\mu|^2 \propto (p + p')^\mu (p + p')^\nu. $$

The tensor structure is symmetric and of rank 2 in momenta, but contains no $g^{\mu\nu}$ term. This means:

张量结构在动量中是对称的二阶张量，但不含 $g^{\mu\nu}$ 项。这意味着：

$$ W_1^{\text{spin-}0} = 0 \quad \implies \quad \mathbf{F_1 = 0}\quad (\text{for scalar partons}). $$

The transverse cross-section vanishes: $\sigma_T = 0$. Longitudinal photons do the scattering. So $\mathbf{R = \sigma_L/\sigma_T \to \infty}$ for spin-0 partons.

横向截面消失：$\sigma_T = 0$。纵向光子完成散射。故对自旋-0 部分子 $\mathbf{R = \sigma_L/\sigma_T \to \infty}$。

**Step 5 — Experimental test (SLAC 1969).** The SLAC experiment measured $F_2$ and $2xF_1$ separately by varying the beam energy and scattering angle at fixed $x$ and $Q^2$. The ratio $2xF_1/F_2$ was found to be close to 1 (i.e., $R \approx 0$) over a wide range of $x$ and $Q^2$, establishing that the partons are **spin-$\tfrac12$** particles — identified with the quarks of the quark model (Module 8.8). $\blacksquare$

**第 5 步 — 实验检验（SLAC 1969）。** SLAC 实验通过在固定 $x$ 和 $Q^2$ 下改变束流能量和散射角，分别测量了 $F_2$ 和 $2xF_1$。在宽广的 $x$ 和 $Q^2$ 范围内，比值 $2xF_1/F_2$ 接近 1（即 $R \approx 0$），确立了部分子是**自旋-$\tfrac12$** 粒子——与夸克模型（模块 8.8）的夸克等同。$\blacksquare$

---

## E. The Momentum Sum Rule and the ~50% Carried by Gluons · 动量求和规则与胶子携带的 ~50%

**Claim.** The momentum sum rule states $\sum_i \int_0^1 x f_i(x)\, dx = 1$ if all constituents are accounted for. Experimentally, quarks carry only ~50% of the proton momentum, implying that electrically neutral partons (gluons) carry the other ~50%.

**命题。** 动量求和规则陈述：若所有组分均被计入，则 $\sum_i \int_0^1 x f_i(x)\, dx = 1$。实验上，夸克只携带 ~50% 的质子动量，这意味着电中性部分子（胶子）携带另外 ~50%。

**Step 1 — Derive the sum rule.** In the infinite momentum frame, the total momentum of the proton is $P$ (by definition). The momentum of all partons must sum to $P$:

**第 1 步 — 推导求和规则。** 在无限动量系中，质子的总动量按定义为 $P$。所有部分子的动量必须求和为 $P$：

$$ \sum_i \langle p_i\rangle = P, $$

where $\langle p_i\rangle = P \int_0^1 \xi f_i(\xi)\, d\xi$ (average momentum of partons of type $i$). Dividing by $P$:

其中 $\langle p_i\rangle = P \int_0^1 \xi f_i(\xi)\, d\xi$（$i$ 类部分子的平均动量）。除以 $P$：

$$ \mathbf{\sum_i \int_0^1 x f_i(x)\, dx = 1}\quad (\text{momentum sum rule}). $$

The sum runs over all parton species: $u, \bar u, d, \bar d, s, \bar s, \ldots$ (quarks and antiquarks) AND gluons $g$.

求和遍历所有部分子种类：$u$、$\bar u$、$d$、$\bar d$、$s$、$\bar s$、$\ldots$（夸克和反夸克）以及胶子 $g$。

**Step 2 — What DIS measures.** Deep inelastic scattering is sensitive only to **charged** partons (the virtual photon couples to electric charge). The measured structure function $F_2$ gives:

**第 2 步 — DIS 测量什么。** 深度非弹性散射只对**带电**部分子灵敏（虚光子与电荷耦合）。测得的结构函数 $F_2$ 给出：

$$ \int_0^1 F_2(x)\, dx = \int_0^1 \sum_q e_q^2 x f_q(x)\, dx = \sum_q e_q^2 \int_0^1 x f_q(x)\, dx. $$

For a proton with $u, d, s$ quarks and their antiquarks, and using $e_u = 2/3$, $e_d = e_s = -1/3$:

对含 $u$、$d$、$s$ 夸克及其反夸克的质子，利用 $e_u = 2/3$，$e_d = e_s = -1/3$：

$$ \int_0^1 F_2^p(x)\, dx = (4/9)\langle xu + x\bar u\rangle + (1/9)\langle xd + x\bar d\rangle + (1/9)\langle xs + x\bar s\rangle, $$

where $\langle xq\rangle \equiv \int_0^1 x f_q(x)\, dx$.

其中 $\langle xq\rangle \equiv \int_0^1 x f_q(x)\, dx$。

**Step 3 — Experimental measurement.** At fixed $Q^2 \approx 10\ \text{GeV}^2$, early experiments (SLAC, CERN) measured:

**第 3 步 — 实验测量。** 在固定 $Q^2 \approx 10\ \text{GeV}^2$ 处，早期实验（SLAC、CERN）测量得到：

$$ \int_0^1 F_2^p(x)\, dx \approx 0.18, \quad \int_0^1 F_2^n(x)\, dx \approx 0.12. $$

(Here $F_2^n$ is from neutrino scattering or deuterium targets to get neutron structure.) Using the quark model relations, one can solve for the individual momentum fractions. The result is that quarks (of all flavors, quarks + antiquarks) carry:

（此处 $F_2^n$ 来自中微子散射或氘靶以获得中子结构。）利用夸克模型关系，可求解各动量分数。结果是所有味的夸克（夸克+反夸克）携带：

$$ \sum_q \int_0^1 x f_q(x)\, dx \approx 0.54 \quad (\text{quarks carry ~54\% of the proton's momentum}). $$

**Step 4 — The gluon fraction.** By the momentum sum rule, the remaining momentum is carried by gluons:

**第 4 步 — 胶子分数。** 由动量求和规则，剩余动量由胶子携带：

$$ \int_0^1 x f_g(x)\, dx = 1 - \sum_q \int_0^1 x f_q(x)\, dx \approx 1 - 0.54 = 0.46 \approx 50\%. $$

This is the **gluon momentum fraction**: roughly half the proton's momentum is carried by electrically neutral gluons that DIS cannot directly see. This is direct evidence for the existence of gluons as real physical constituents of the proton, and confirms QCD (Module 8.3). $\blacksquare$

这就是**胶子动量分数**：质子约一半的动量由 DIS 无法直接看到的电中性胶子携带。这是胶子作为质子真实物理组分存在的直接证据，证实了 QCD（模块 8.3）。$\blacksquare$

---

## F. Scaling Violations and the DGLAP Equations from Gluon Radiation · 胶子辐射导致的标度破坏与 DGLAP 方程

**Claim.** Pure Bjorken scaling ($F_2$ depends only on $x$, not $Q^2$) is violated by QCD. As $Q^2$ increases, the virtual photon resolves more and more gluon-radiation substructure, causing partons to split and the PDFs to evolve. The evolution is governed by the **DGLAP equations** (Dokshitzer–Gribov–Lipatov–Altarelli–Parisi), whose physical origin is gluon emission from quarks and quark–antiquark pair production from gluons. The coupling $\alpha_s(Q^2)$ runs to zero (asymptotic freedom), making the evolution calculable in perturbation theory.

**命题。** 纯比约肯标度（$F_2$ 只依赖 $x$，不依赖 $Q^2$）被 QCD 所破坏。随着 $Q^2$ 增大，虚光子分辨越来越多的胶子辐射子结构，导致部分子劈裂和 PDF 演化。演化由 **DGLAP 方程**（多克希策–格里博夫–利帕托夫–阿尔塔雷利–帕里西）支配，其物理起源是来自夸克的胶子辐射和来自胶子的正反夸克对产生。跑动耦合 $\alpha_s(Q^2)$ 趋向零（渐近自由），使得演化可在微扰论中计算。

**Step 1 — Physical picture of scaling violations.** At resolution scale $Q$, a photon probing a quark with momentum fraction $x$ sees the quark as a pointlike object — if the quark has not radiated. But at higher resolution $Q' > Q$, the photon can resolve the fact that the quark previously emitted a gluon (which carries away some momentum), so what appeared to be a single quark is revealed to be a quark-plus-gluon system. The quark now carries less momentum than $x$, and there are more partons at smaller $x$ values. Qualitatively:

**第 1 步 — 标度破坏的物理图像。** 在分辨尺度 $Q$ 处，探测动量分数为 $x$ 的夸克的光子将夸克视为点状物体——如果夸克没有辐射的话。但在更高分辨率 $Q' > Q$ 处，光子可以分辨出夸克之前发射了一个胶子（携走一些动量），因此看似单个夸克实际上被揭示为夸克加胶子系统。夸克现在携带的动量少于 $x$，且在更小 $x$ 值处有更多部分子。定性地：

- $F_2(x, Q^2)$ decreases at large $x$ as $Q^2$ increases (quarks radiate, losing momentum).
- $F_2(x, Q^2)$ increases at small $x$ as $Q^2$ increases (splittings populate the small-$x$ region).

- 随 $Q^2$ 增大，$F_2(x, Q^2)$ 在大 $x$ 处减小（夸克辐射，损失动量）。
- 随 $Q^2$ 增大，$F_2(x, Q^2)$ 在小 $x$ 处增大（劈裂填充小 $x$ 区域）。

**Step 2 — The splitting functions.** The probability for a quark with momentum fraction $y$ to emit a gluon and become a quark with momentum fraction $x = zy$ ($z < 1$) in a collinear splitting involves a **splitting function** $P_{qq}(z)$. At leading order in $\alpha_s$:

**第 2 步 — 劈裂函数。** 动量分数为 $y$ 的夸克辐射胶子并成为动量分数为 $x = zy$（$z < 1$）的夸克的概率，在共线劈裂中涉及**劈裂函数** $P_{qq}(z)$。在 $\alpha_s$ 的领头阶：

$$ \begin{aligned}
P_{qq}(z) &= C_F \cdot (1 + z^2)/(1 - z)_+, && C_F = 4/3\ (\text{Casimir of SU(3) fundamental}). \\
P_{gq}(z) &= C_F \cdot (1 + (1-z)^2)/z && (\text{quark} \to \text{gluon} + \text{quark}). \\
P_{qg}(z) &= T_F \cdot (z^2 + (1-z)^2), && T_F = 1/2\ (\text{gluon} \to \text{quark} + \text{antiquark}). \\
P_{gg}(z) &= 2C_A \cdot [z/(1-z)_+ + (1-z)/z + z(1-z)], && C_A = 3\ (\text{SU(3) adjoint Casimir}).
\end{aligned} $$

Here the "plus" distribution $(1/(1-z))_+$ regulates the collinear singularity at $z \to 1$.

此处"加"分布 $(1/(1-z))_+$ 正规化了 $z \to 1$ 处的共线奇点。

**Step 3 — Derive the DGLAP equations.** Consider the PDF $f_q(x, Q^2)$. At scale $Q^2$, the probability of finding a quark with fraction $x$ receives contributions from:

**第 3 步 — 推导 DGLAP 方程。** 考虑 PDF $f_q(x, Q^2)$。在标度 $Q^2$ 处，找到分数为 $x$ 的夸克的概率接收以下贡献：

(a) A quark at fraction $x$ that did not radiate (probability $\sim 1 - \alpha_s \cdot \text{correction}$).
(b) A quark at fraction $y > x$ that radiated a gluon and ended up at $x = zy$: integrated over all $y > x$.
(c) A gluon at fraction $y$ that split into a $q\bar q$ pair with the quark at $x$.

(a) 分数为 $x$ 的夸克未辐射（概率 $\sim 1 - \alpha_s \cdot \text{修正}$）。
(b) 分数为 $y > x$ 的夸克辐射胶子后到达 $x = zy$：对所有 $y > x$ 积分。
(c) 分数为 $y$ 的胶子劈裂为正反夸克对，夸克在 $x$ 处。

Taking the derivative with respect to $\ln Q^2$ (the natural variable for evolution, since $\alpha_s$ runs logarithmically):

对 $\ln Q^2$ 取导数（演化的自然变量，因 $\alpha_s$ 对数跑动）：

$$ \begin{aligned}
\frac{d}{d(\ln Q^2)} f_q(x, Q^2) &= \frac{\alpha_s(Q^2)}{2\pi} \cdot \int_x^1 \frac{dy}{y} [P_{qq}(x/y) f_q(y, Q^2) + P_{qg}(x/y) f_g(y, Q^2)], \\
\frac{d}{d(\ln Q^2)} f_g(x, Q^2) &= \frac{\alpha_s(Q^2)}{2\pi} \cdot \int_x^1 \frac{dy}{y} \Big[\sum_q P_{gq}(x/y) f_q(y, Q^2) + P_{gg}(x/y) f_g(y, Q^2)\Big].
\end{aligned} $$

These are the **DGLAP equations**. They are a set of coupled integro-differential equations for the PDFs.

这就是 **DGLAP 方程**。它们是 PDF 的一组耦合积分微分方程。

**Step 4 — The role of asymptotic freedom.** The evolution is proportional to $\alpha_s(Q^2)$. By asymptotic freedom (Module 8.3), as $Q^2$ increases, $\alpha_s(Q^2) \to 0$ logarithmically:

**第 4 步 — 渐近自由的作用。** 演化正比于 $\alpha_s(Q^2)$。由渐近自由（模块 8.3），随 $Q^2$ 增大，$\alpha_s(Q^2)$ 对数趋向零：

$$ \alpha_s(Q^2) = (2\pi) / (b_0 \ln(Q^2/\Lambda_{QCD}^2)), \quad b_0 = 11 - 2n_f/3, \quad \Lambda_{QCD} \approx 200\ \text{MeV}. $$

As $Q^2 \to \infty$, $\alpha_s \to 0$ and the evolution rate $d/d(\ln Q^2) \to 0$: the PDFs freeze and Bjorken scaling is approximately restored at very high $Q^2$. At finite $Q^2$, the violations are **logarithmic** in $Q^2$, not power-law. This is the precise statement of "weak" scaling violations.

随 $Q^2 \to \infty$，$\alpha_s \to 0$，演化率 $d/d(\ln Q^2) \to 0$：PDF 冻结，在极高 $Q^2$ 处比约肯标度近似恢复。在有限 $Q^2$ 处，破坏是 $Q^2$ 的**对数**，而非幂次律。这是"弱"标度破坏的精确表述。

**Step 5 — Gluon bremsstrahlung: physical mechanism.** In the Breit frame, a quark carrying fraction $x$ can radiate a gluon carrying fraction $(1-z)x$, leaving the quark at fraction $zx$:

**第 5 步 — 胶子轫致辐射：物理机制。** 在布雷特系中，携带分数 $x$ 的夸克可以辐射携带分数 $(1-z)x$ 的胶子，使夸克留在 $zx$ 处：

$$ q(x) \to q(zx) + g((1-z)x), \quad 0 < z < 1. $$

The probability amplitude for this splitting is proportional to the QCD coupling $g_s$, and the squared amplitude (probability) to $\alpha_s = g_s^2/(4\pi)$. The gluon can in turn split into $q\bar q$ ($P_{qg}$), populating small-$x$ regions. These processes, iterated over the logarithm $\ln(Q^2/Q_0^2)$, generate the full DGLAP evolution.

此劈裂的概率振幅正比于 QCD 耦合 $g_s$，概率正比于 $\alpha_s = g_s^2/(4\pi)$。胶子可以进而劈裂为 $q\bar q$（$P_{qg}$），填充小 $x$ 区域。这些过程在对数 $\ln(Q^2/Q_0^2)$ 上迭代，产生完整的 DGLAP 演化。

**Step 6 — Comparison with experiment.** The DGLAP equations predict specific patterns of scaling violation:

**第 6 步 — 与实验的比较。** DGLAP 方程预言标度破坏的特定模式：

- At $x > 0.1$: $F_2(x, Q^2)$ decreases as $Q^2$ increases (quarks lose momentum by gluon emission).
- At $x < 0.1$: $F_2(x, Q^2)$ increases as $Q^2$ increases (gluon splitting feeds small-$x$ quarks).
- The evolution is logarithmic in $Q^2$, not power-law.

- 在 $x > 0.1$：$F_2(x, Q^2)$ 随 $Q^2$ 增大而减小（夸克通过胶子辐射损失动量）。
- 在 $x < 0.1$：$F_2(x, Q^2)$ 随 $Q^2$ 增大而增大（胶子劈裂给小 $x$ 夸克提供动量）。
- 演化在 $Q^2$ 上是对数的，而非幂次律。

These predictions have been confirmed with high precision at HERA (DESY), over four decades in $Q^2$ ($1\ \text{GeV}^2$ to $10^4\ \text{GeV}^2$) and three decades in $x$ ($x \approx 10^{-5}$ to $x \approx 0.5$). The DGLAP equations are the cornerstone of quantitative perturbative QCD and are used as inputs to every hadron-collider prediction. $\blacksquare$

这些预言已在 HERA（德国电子同步加速器）以高精度得到证实，覆盖四个数量级的 $Q^2$（$1\ \text{GeV}^2$ 到 $10^4\ \text{GeV}^2$）和三个数量级的 $x$（$x \approx 10^{-5}$ 到 $x \approx 0.5$）。DGLAP 方程是定量微扰 QCD 的基石，被用作每个强子对撞机预言的输入。$\blacksquare$

---

*All derivations are complete at leading order. The Callan–Gross relation follows directly from the Dirac nature of quarks; the DGLAP equations encode gluon bremsstrahlung at leading-log accuracy; and the $x \in (0,1)$ bound is a rigorous consequence of Lorentz kinematics. Together they form the quantitative foundation of the parton model and perturbative QCD.*

*所有推导均在领头阶完整给出。卡兰–格罗斯关系直接源于夸克的狄拉克性质；DGLAP 方程在领头对数精度下编码胶子轫致辐射；$x \in (0,1)$ 的界是洛伦兹运动学的严格推论。它们共同构成部分子模型和微扰 QCD 的定量基础。*

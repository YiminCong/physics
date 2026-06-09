---
title: "Derivations — Module 5.11: Topological Superconductivity & Majorana Modes"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 5.11: Topological Superconductivity & Majorana Modes
# 推导 — 模块 5.11：拓扑超导与马约拉纳模

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 5.11](./module-5.11-topological-superconductivity-and-majorana.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 5.11](./module-5.11-topological-superconductivity-and-majorana.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Kitaev Chain in Majorana Operators: Topological Phase and Unpaired End Modes · 马约拉纳算符中的基塔耶夫链：拓扑相与未配对端模

**Claim.** Rewriting the Kitaev chain Hamiltonian in Majorana operators reveals that, at the special point $t = \Delta > 0$ and $\mu = 0$, the Hamiltonian couples only inter-site Majorana pairs, leaving one Majorana mode at each end of the chain exactly at zero energy. For $|\mu| < 2t$ (topological phase), these end modes remain at zero energy even away from the special point, exponentially localized at the ends.

**命题。** 将基塔耶夫链哈密顿量用马约拉纳算符改写后，可以看出在特殊点 $t = \Delta > 0$、$\mu = 0$ 处，哈密顿量仅耦合格点间马约拉纳对，使链每端各有一个马约拉纳模精确处于零能。对于 $|\mu| < 2t$（拓扑相），这些端模即使在远离特殊点处也保持零能，在端部指数局域。

**Step 1 — Define Majorana operators.** For each site $j = 1, \ldots, N$, define two Hermitian Majorana operators:

**第 1 步 — 定义马约拉纳算符。** 对每个格点 $j = 1, \ldots, N$，定义两个厄米马约拉纳算符：

$$ \gamma_{j,A} = c_j + c_j^\dagger, \qquad \gamma_{j,B} = i(c_j^\dagger - c_j). $$

These satisfy $\gamma_{j,A}^\dagger = \gamma_{j,A}$, $\gamma_{j,B}^\dagger = \gamma_{j,B}$ (Hermitian), and the anticommutation relations $\{\gamma_{j,\alpha}, \gamma_{k,\beta}\} = 2\delta_{jk} \delta_{\alpha\beta}$. The inverse relations are:

这些算符满足 $\gamma_{j,A}^\dagger = \gamma_{j,A}$，$\gamma_{j,B}^\dagger = \gamma_{j,B}$（厄米），以及反对易关系 $\{\gamma_{j,\alpha}, \gamma_{k,\beta}\} = 2\delta_{jk} \delta_{\alpha\beta}$。逆关系为：

$$ c_j = (\gamma_{j,A} + i\gamma_{j,B})/2, \qquad c_j^\dagger = (\gamma_{j,A} - i\gamma_{j,B})/2. $$

**Step 2 — Rewrite each term.** Compute the three types of terms in $H = -\mu \sum_j c_j^\dagger c_j - t \sum_j(c_j^\dagger c_{j+1} + c_{j+1}^\dagger c_j) + \Delta \sum_j(c_j c_{j+1} + c_{j+1}^\dagger c_j^\dagger)$:

**第 2 步 — 改写每一项。** 计算 $H = -\mu \sum_j c_j^\dagger c_j - t \sum_j(c_j^\dagger c_{j+1} + c_{j+1}^\dagger c_j) + \Delta \sum_j(c_j c_{j+1} + c_{j+1}^\dagger c_j^\dagger)$ 中的三类项：

*On-site number operator:*

$$ c_j^\dagger c_j = (\gamma_{j,A} - i\gamma_{j,B})(\gamma_{j,A} + i\gamma_{j,B})/4 = (1 + i\gamma_{j,A}\gamma_{j,B})/2 = (1 - i\gamma_{j,B}\gamma_{j,A})/2. \text{ So:} $$

$$ -\mu c_j^\dagger c_j = -\mu/2 + (i\mu/2) \gamma_{j,B} \gamma_{j,A}. $$

*格点占据数算符：*

$$ c_j^\dagger c_j = (1 - i\gamma_{j,B}\gamma_{j,A})/2, \text{ 故 } -\mu c_j^\dagger c_j = -\mu/2 + (i\mu/2) \gamma_{j,B} \gamma_{j,A}. $$

*Hopping term:*

$$ c_j^\dagger c_{j+1} + \text{h.c.} = [(\gamma_{j,A} - i\gamma_{j,B})(\gamma_{j+1,A} + i\gamma_{j+1,B})]/4 + \text{h.c.} $$

Expanding and taking real part (the h.c. doubles the real terms and cancels the imaginary terms):

$$ c_j^\dagger c_{j+1} + \text{h.c.} = (i/2)(\gamma_{j,B}\gamma_{j+1,A} - \gamma_{j,A}\gamma_{j+1,B}). $$

*跳跃项：*
展开并取实部（厄米共轭使实部加倍，消去虚部）：

$$ c_j^\dagger c_{j+1} + \text{h.c.} = (i/2)(\gamma_{j,B}\gamma_{j+1,A} - \gamma_{j,A}\gamma_{j+1,B}). $$

*Pairing term:*

$$ \begin{aligned} c_j c_{j+1} &= (\gamma_{j,A} + i\gamma_{j,B})(\gamma_{j+1,A} + i\gamma_{j+1,B})/4 \\ &= (\gamma_{j,A}\gamma_{j+1,A} + i\gamma_{j,A}\gamma_{j+1,B} + i\gamma_{j,B}\gamma_{j+1,A} - \gamma_{j,B}\gamma_{j+1,B})/4. \end{aligned} $$

Adding the h.c. $c_{j+1}^\dagger c_j^\dagger = (\gamma_{j+1,A} - i\gamma_{j+1,B})(\gamma_{j,A} - i\gamma_{j,B})/4$ and using $\gamma_{j+1,\alpha}\gamma_{j,\beta} = -\gamma_{j,\beta}\gamma_{j+1,\alpha}$, the $\gamma\gamma$-symmetric (real) parts cancel and the imaginary parts double:

$$ c_j c_{j+1} + \text{h.c.} = (i/2)(\gamma_{j,A}\gamma_{j+1,B} + \gamma_{j,B}\gamma_{j+1,A}). $$

(Note: this has the same structure as the hopping term but with opposite relative sign between the two Majorana cross-products.)

*配对项：*
经仔细代数运算（利用 $\alpha\ne\beta$ 时 $\gamma_{\alpha}\gamma_{\beta} = -\gamma_{\beta}\gamma_{\alpha}$ 和 $\gamma^2 = 1$）：

$$ c_j c_{j+1} + \text{h.c.} = (i/2)(\gamma_{j,B}\gamma_{j+1,A} + \gamma_{j,A}\gamma_{j+1,B}). $$

（注意：这与跳跃项结构相同，但两个马约拉纳交叉乘积之间的相对符号相反。）

**Step 3 — Assemble the full Hamiltonian.** Collecting all terms (dropping constant $-\mu N/2$):

**第 3 步 — 组装完整哈密顿量。** 收集所有项（舍去常数 $-\mu N/2$）：

$$ \begin{aligned} H &= (i\mu/2) \sum_j \gamma_{j,B} \gamma_{j,A} \\ &\quad + (i/2) \sum_j [ -t(\gamma_{j,B}\gamma_{j+1,A} - \gamma_{j,A}\gamma_{j+1,B}) + \Delta(\gamma_{j,B}\gamma_{j+1,A} + \gamma_{j,A}\gamma_{j+1,B}) ] \\ &= (i\mu/2) \sum_j \gamma_{j,B} \gamma_{j,A} \\ &\quad + (i/2) \sum_j [ (\Delta-t) \gamma_{j,A}\gamma_{j+1,B} + (\Delta+t) \gamma_{j,B}\gamma_{j+1,A} ]. \end{aligned} $$

**Step 4 — Special point $t = \Delta$, $\mu = 0$.** Setting $\mu = 0$ eliminates the first sum. Setting $\Delta = t$ makes the coefficient of $\gamma_{j,A}\gamma_{j+1,B}$ vanish ($\Delta-t = 0$):

**第 4 步 — 特殊点 $t = \Delta$，$\mu = 0$。** 令 $\mu = 0$ 消去第一个求和。令 $\Delta = t$ 使 $\gamma_{j,A}\gamma_{j+1,B}$ 的系数消失（$\Delta-t = 0$）：

$$ H|_{t=\Delta,\, \mu=0} = it \sum_{j=1}^{N-1} \gamma_{j,B} \gamma_{j+1,A}. $$

The Hamiltonian couples only the **B** Majorana on site $j$ to the **A** Majorana on site $j+1$. The $2N$ Majorana operators split into:
- **$N-1$ coupled pairs** ($\gamma_{j,B}, \gamma_{j+1,A}$): these form ordinary fermions $d_j = (\gamma_{j,B} + i\gamma_{j+1,A})/2$ with energy $\varepsilon = \pm t$ (positive gap $2t$).
- **Two unpaired operators**: $\gamma_{1,A}$ (left end) and $\gamma_{N,B}$ (right end), which do not appear in $H$ at all.

哈密顿量仅耦合格点 $j$ 上的 **B** 马约拉纳与格点 $j+1$ 上的 **A** 马约拉纳。$2N$ 个马约拉纳算符分为：
- **$N-1$ 个耦合对**（$\gamma_{j,B}, \gamma_{j+1,A}$）：形成普通费米子 $d_j = (\gamma_{j,B} + i\gamma_{j+1,A})/2$，能量 $\varepsilon = \pm t$（正能隙 $2t$）。
- **两个未配对算符**：$\gamma_{1,A}$（左端）和 $\gamma_{N,B}$（右端），完全不出现在 $H$ 中。

Since $[H, \gamma_{1,A}] = [H, \gamma_{N,B}] = 0$ and $\gamma_{1,A}^2 = \gamma_{N,B}^2 = 1$, these are **zero-energy Majorana modes**. The non-local fermion $f = (\gamma_{1,A} + i\gamma_{N,B})/2$ has $[H, f] = [H, f^\dagger] = 0$ and $\{f, f^\dagger\} = 1$, so $|0\rangle$ and $f^\dagger|0\rangle$ are degenerate ground states with the same energy. $\blacksquare$

由于 $[H, \gamma_{1,A}] = [H, \gamma_{N,B}] = 0$ 且 $\gamma_{1,A}^2 = \gamma_{N,B}^2 = 1$，这些是**零能马约拉纳模**。非局域费米子 $f = (\gamma_{1,A} + i\gamma_{N,B})/2$ 满足 $[H, f] = [H, f^\dagger] = 0$ 和 $\{f, f^\dagger\} = 1$，因此 $|0\rangle$ 和 $f^\dagger|0\rangle$ 是能量相同的简并基态。$\blacksquare$

---

## B. Topological Phase $|\mu| < 2t$ and Ground-State Degeneracy · 拓扑相 $|\mu| < 2t$ 与基态简并

**Claim.** The topological criterion $|\mu| < 2t$ follows from the bulk band structure of the Kitaev chain. The two ground states $|0\rangle$ and $|1\rangle = f^\dagger|0\rangle$ are exactly degenerate in the thermodynamic limit ($N \to \infty$) and differ only in the parity of the non-local fermion $f$.

**命题。** 拓扑判据 $|\mu| < 2t$ 来自基塔耶夫链的体能带结构。在热力学极限（$N \to \infty$）中，两个基态 $|0\rangle$ 和 $|1\rangle = f^\dagger|0\rangle$ 精确简并，仅在非局域费米子 $f$ 的宇称上有所不同。

**Step 1 — Bulk Hamiltonian in k-space.** For a periodic infinite chain (ignoring boundaries), Fourier transform $c_j = (1/\sqrt{N}) \sum_k e^{ikj} c_k$. The Hamiltonian in Nambu basis $\Psi_k = (c_k, c_{-k}^\dagger)^\top$ becomes:

**第 1 步 — k 空间中的体哈密顿量。** 对周期性无限链（忽略边界），傅里叶变换 $c_j = (1/\sqrt{N}) \sum_k e^{ikj} c_k$。Nambu 基 $\Psi_k = (c_k, c_{-k}^\dagger)^\top$ 中的哈密顿量变为：

$$ H = (1/2) \sum_k \Psi_k^\dagger h(k) \Psi_k, $$

$$ h(k) = (-\mu - 2t \cos k) \tau_z + 2\Delta \sin k \cdot \tau_y, $$

where $\tau_{y,z}$ are Pauli matrices in particle–hole (Nambu) space. The quasiparticle dispersion is:

其中 $\tau_{y,z}$ 是粒子–空穴（Nambu）空间中的泡利矩阵。准粒子色散为：

$$ E(k) = \pm\sqrt{(\mu + 2t \cos k)^2 + 4\Delta^2 \sin^2 k}. $$

**Step 2 — Gap-closing condition.** The bulk gap closes at $E(k) = 0$, which requires both:

$$ \mu + 2t \cos k = 0 \quad \text{AND} \quad 2\Delta \sin k = 0. $$

The second condition gives $k = 0$ or $k = \pi$. Substituting:
- $k = 0$: gap closes when $\mu + 2t = 0$, i.e. $\boldsymbol{\mu = -2t}$.
- $k = \pi$: gap closes when $\mu - 2t = 0$, i.e. $\boldsymbol{\mu = +2t}$.

**第 2 步 — 能隙关闭条件。** 体能隙在 $E(k) = 0$ 处关闭，这要求同时满足：

$$ \mu + 2t \cos k = 0 \quad \text{且} \quad 2\Delta \sin k = 0. $$

第二个条件给出 $k = 0$ 或 $k = \pi$。代入：
- $k = 0$：当 $\mu + 2t = 0$ 即 $\boldsymbol{\mu = -2t}$ 时能隙关闭。
- $k = \pi$：当 $\mu - 2t = 0$ 即 $\boldsymbol{\mu = +2t}$ 时能隙关闭。

Thus the bulk gap is open for $|\mu| \ne 2t$, and the gap-closing transitions at $\mu = \pm 2t$ separate two phases.

因此体能隙在 $|\mu| \ne 2t$ 时开启，在 $\mu = \pm 2t$ 处的能隙关闭相变分隔了两个相。

**Step 3 — Topological invariant (Pfaffian / winding number).** The BdG Hamiltonian $h(k)$ at $k = 0$ and $k = \pi$ is a real antisymmetric matrix (since $\sin 0 = \sin \pi = 0$). Define the **Majorana number** (Kitaev's $\mathbb{Z}_2$ invariant):

**第 3 步 — 拓扑不变量（普法夫/绕数）。** 在 $k = 0$ 和 $k = \pi$ 处，BdG 哈密顿量 $h(k)$ 是实反对称矩阵（因为 $\sin 0 = \sin \pi = 0$）。定义**马约拉纳数**（基塔耶夫的 $\mathbb{Z}_2$ 不变量）：

$$ M = \text{sgn}( \text{Pf}[h(0)] ) \times \text{sgn}( \text{Pf}[h(\pi)] ), $$

where Pf denotes the Pfaffian. For the Kitaev chain:

$$ \begin{aligned} h(0) &= (-\mu - 2t) \tau_z, & \text{Pf}[h(0)] &= -(\mu + 2t). \\ h(\pi) &= (-\mu + 2t) \tau_z, & \text{Pf}[h(\pi)] &= -(\mu - 2t). \\ M &= \text{sgn}[(\mu + 2t)(\mu - 2t)] = \text{sgn}[\mu^2 - 4t^2]. \end{aligned} $$

其中 Pf 表示普法夫式。对于基塔耶夫链：

$$ \begin{aligned} h(0) &= (-\mu - 2t) \tau_z, & \text{Pf}[h(0)] &= -(\mu + 2t). \\ h(\pi) &= (-\mu + 2t) \tau_z, & \text{Pf}[h(\pi)] &= -(\mu - 2t). \\ M &= \text{sgn}[(\mu + 2t)(\mu - 2t)] = \text{sgn}[\mu^2 - 4t^2]. \end{aligned} $$

- **Topological phase** ($|\mu| < 2t$): $\mu^2 < 4t^2$, so $M = \text{sgn}(\text{negative}) = \boldsymbol{-1}$. Majorana end modes exist.
- **Trivial phase** ($|\mu| > 2t$): $\mu^2 > 4t^2$, so $M = \text{sgn}(\text{positive}) = \boldsymbol{+1}$. No end modes.

- **拓扑相**（$|\mu| < 2t$）：$\mu^2 < 4t^2$，故 $M = \text{sgn}(\text{负}) = \boldsymbol{-1}$。马约拉纳端模存在。
- **平庸相**（$|\mu| > 2t$）：$\mu^2 > 4t^2$，故 $M = \text{sgn}(\text{正}) = \boldsymbol{+1}$。无端模。

This is the $\mathbb{Z}_2$ topological invariant. The **bulk–boundary correspondence** guarantees that $M = -1$ implies the existence of a zero-energy boundary mode for any open chain in the topological phase, not just at the special point. $\blacksquare$

这就是 $\mathbb{Z}_2$ 拓扑不变量。**体–边对应**保证 $M = -1$ 意味着拓扑相中任意开放链存在零能边界模，而不仅仅是在特殊点处。$\blacksquare$

**Step 4 — Ground-state degeneracy from the non-local fermion.** In the topological phase, the two end modes $\gamma_L$ and $\gamma_R$ are spatially separated by the entire chain of length $N$. Define:

**第 4 步 — 非局域费米子的基态简并。** 在拓扑相中，两个端模 $\gamma_L$ 和 $\gamma_R$ 在空间上被整个长度为 $N$ 的链分开。定义：

$$ f = (\gamma_L + i\gamma_R)/2, \qquad f^\dagger = (\gamma_L - i\gamma_R)/2. $$

The ground-state subspace is spanned by $|0\rangle$ ($f|0\rangle = 0$) and $|1\rangle = f^\dagger|0\rangle$. These states have:
- The **same energy** (since $\gamma_L$ and $\gamma_R$ decouple from $H$ in the limit of a long chain).
- **Different fermion parity**: $P = (-1)^{N_f}$ where $N_f$ is the total fermion number. $|0\rangle$ and $|1\rangle$ differ by adding one fermion (the non-local $f^\dagger$), so they have opposite parity.

基态子空间由 $|0\rangle$（$f|0\rangle = 0$）和 $|1\rangle = f^\dagger|0\rangle$ 张成。这两个态具有：
- **相同能量**（在长链极限下 $\gamma_L$ 和 $\gamma_R$ 从 $H$ 中解耦）。
- **不同费米子宇称**：$P = (-1)^{N_f}$，其中 $N_f$ 是总费米子数。$|0\rangle$ 和 $|1\rangle$ 相差一个非局域费米子 $f^\dagger$，因此宇称相反。

Any local operator acting on one end of the chain cannot distinguish $|0\rangle$ from $|1\rangle$ because the non-local fermion's quantum number is split between the two ends. This **topological protection** of the degeneracy is the key property that makes Majorana modes useful for quantum memory. $\blacksquare$

作用在链一端的任何局域算符都无法区分 $|0\rangle$ 和 $|1\rangle$，因为非局域费米子的量子数分裂在两端之间。这种简并的**拓扑保护**是使马约拉纳模在量子存储中有用的关键性质。$\blacksquare$

---

## C. Non-Abelian Braiding Rule for Majorana Modes · 马约拉纳模的非阿贝尔编织规则

**Claim.** Adiabatically exchanging (braiding) two Majorana modes $\gamma_i$ and $\gamma_j$ in 2D (or in a T-junction network in 1D) implements the unitary transformation $U_{ij} = (1 + \gamma_i \gamma_j)/\sqrt{2} = \exp(\pi\gamma_i \gamma_j/4)$ on the degenerate ground-state subspace. Sequential braidings do not commute, making the representation non-Abelian.

**命题。** 在二维（或一维 T 结网络中）绝热地交换（编织）两个马约拉纳模 $\gamma_i$ 和 $\gamma_j$，在简并基态子空间上实现酉变换 $U_{ij} = (1 + \gamma_i \gamma_j)/\sqrt{2} = \exp(\pi\gamma_i \gamma_j/4)$。序贯编织不对易，使该表示成为非阿贝尔的。

**Step 1 — Setup: four Majorana modes.** Consider four Majorana modes $\gamma_1, \gamma_2, \gamma_3, \gamma_4$ forming two non-local fermions:

**第 1 步 — 设置：四个马约拉纳模。** 考虑四个马约拉纳模 $\gamma_1$、$\gamma_2$、$\gamma_3$、$\gamma_4$，形成两个非局域费米子：

$$ \begin{aligned} f_{12} &= (\gamma_1 + i\gamma_2)/2 \qquad (\text{parity } p_{12} = 2f_{12}^\dagger f_{12} - 1 = i\gamma_1\gamma_2) \\ f_{34} &= (\gamma_3 + i\gamma_4)/2 \qquad (\text{parity } p_{34} = i\gamma_3\gamma_4) \end{aligned} $$

The four-dimensional degenerate subspace is spanned by $|n_{12}, n_{34}\rangle$ where $n_{12}, n_{34} \in \{0,1\}$ are the occupancies of $f_{12}$ and $f_{34}$. Total parity conservation (imposed by fermion parity superselection) restricts physical states to the two-dimensional subspace $\{|00\rangle, |11\rangle\}$ (even total parity) or $\{|01\rangle, |10\rangle\}$ (odd total parity).

四维简并子空间由 $|n_{12}, n_{34}\rangle$ 张成，其中 $n_{12}, n_{34} \in \{0,1\}$ 是 $f_{12}$ 和 $f_{34}$ 的占据数。总宇称守恒（由费米子宇称超选择定则施加）将物理态限制在二维子空间 $\{|00\rangle, |11\rangle\}$（偶总宇称）或 $\{|01\rangle, |10\rangle\}$（奇总宇称）中。

**Step 2 — Berry phase from adiabatic exchange.** To exchange $\gamma_1$ and $\gamma_2$, we adiabatically move them in the plane along a path that winds $\gamma_2$ around $\gamma_1$ by angle $\pi$ (a half-braid). The key physical ingredient is that the Hamiltonian $H(t)$ must close and reopen the local gap near each Majorana as they move, but the global gap (and the degeneracy subspace) never closes. The resulting Berry phase matrix, computed from the adiabatic connection $A = \langle\psi_n|d/dt|\psi_m\rangle\, dt$ integrated around the exchange path, gives:

**第 2 步 — 绝热交换的贝里相位。** 为了交换 $\gamma_1$ 和 $\gamma_2$，我们沿着将 $\gamma_2$ 绕 $\gamma_1$ 旋转 $\pi$ 角度（半编织）的路径绝热地移动它们。关键的物理成分是：哈密顿量 $H(t)$ 必须在每个马约拉纳移动时局域地关闭和重新开启能隙，但全局能隙（和简并子空间）从不关闭。由绝热联络 $A = \langle\psi_n|d/dt|\psi_m\rangle\, dt$ 沿交换路径积分得到贝里相位矩阵：

$$ U_{12} = \exp(\pi \gamma_1 \gamma_2 / 4) = (1 + \gamma_1\gamma_2)/\sqrt{2}. $$

This result follows from the Aharonov–Anandan holonomy for the non-Abelian Berry connection of the degenerate subspace.

这个结果来自简并子空间的非阿贝尔贝里联络的 Aharonov–Anandan 完整性。

**Step 3 — Explicit matrix representation.** In the $\{|00\rangle, |11\rangle\}$ subspace, compute $\gamma_1\gamma_2$ using $\gamma_1 = f_{12} + f_{12}^\dagger$ and $\gamma_2 = i(f_{12}^\dagger - f_{12})$:

**第 3 步 — 显式矩阵表示。** 在 $\{|00\rangle, |11\rangle\}$ 子空间中，利用 $\gamma_1 = f_{12} + f_{12}^\dagger$ 和 $\gamma_2 = i(f_{12}^\dagger - f_{12})$ 计算 $\gamma_1\gamma_2$：

$$ \begin{aligned} i\gamma_1\gamma_2 &= i(f_{12} + f_{12}^\dagger) \cdot i(f_{12}^\dagger - f_{12}) = -(f_{12} + f_{12}^\dagger)(f_{12}^\dagger - f_{12}) \\ &= -(f_{12}f_{12}^\dagger - f_{12}f_{12} + f_{12}^\dagger f_{12}^\dagger - f_{12}^\dagger f_{12}) \\ &= -(f_{12}f_{12}^\dagger - f_{12}^\dagger f_{12}) = -(1 - 2f_{12}^\dagger f_{12}) = 2n_{12} - 1. \end{aligned} $$

So $i\gamma_1\gamma_2$ acts as $+1$ on $|1,n_{34}\rangle$ and $-1$ on $|0,n_{34}\rangle$, i.e. $i\gamma_1\gamma_2 = \sigma_z$ in the $\{|00\rangle,|11\rangle\}$ basis. Therefore:

所以 $i\gamma_1\gamma_2$ 在 $|1,n_{34}\rangle$ 上作用为 $+1$，在 $|0,n_{34}\rangle$ 上为 $-1$，即在 $\{|00\rangle,|11\rangle\}$ 基中 $i\gamma_1\gamma_2 = \sigma_z$。因此：

$$ \begin{aligned} U_{12} &= (1 + \gamma_1\gamma_2)/\sqrt{2} = (1 - i\sigma_z)/\sqrt{2} = e^{-i\pi/4} \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/2} \end{pmatrix} \\ &= e^{-i\pi\sigma_z/4} \qquad \text{(a rotation by } \pi/2 \text{ around the z-axis).} \end{aligned} $$

Similarly, for braiding $\gamma_2$ and $\gamma_3$ (which mixes the two non-local fermions $f_{12}$ and $f_{34}$):

类似地，编织 $\gamma_2$ 和 $\gamma_3$（混合两个非局域费米子 $f_{12}$ 和 $f_{34}$）：

$$ U_{23} = (1 + \gamma_2\gamma_3)/\sqrt{2} = e^{-i\pi\sigma_x/4} \qquad \text{(a rotation by } \pi/2 \text{ around the x-axis).} $$

**Step 4 — Non-commutativity.** The key property:

**第 4 步 — 非对易性。** 关键性质：

$$ U_{12} U_{23} = e^{-i\pi\sigma_z/4} e^{-i\pi\sigma_x/4} \ne e^{-i\pi\sigma_x/4} e^{-i\pi\sigma_z/4} = U_{23} U_{12}, $$

because $\sigma_z$ and $\sigma_x$ do not commute: $[\sigma_z, \sigma_x] = 2i\sigma_y \ne 0$. The braiding operations generate the group of single-qubit rotations by multiples of $\pi/2$. Together with inter-qubit braidings and a few additional operations, these provide a **universal gate set** for topological quantum computation, where the quantum information is stored in the non-local fermion parities and gates are implemented by braiding trajectories. $\blacksquare$

因为 $\sigma_z$ 和 $\sigma_x$ 不对易：$[\sigma_z, \sigma_x] = 2i\sigma_y \ne 0$。编织操作生成 $\pi/2$ 倍数单量子比特旋转群。与量子比特间编织及少量附加操作一起，这些提供了拓扑量子计算的**通用门集**，其中量子信息存储在非局域费米子宇称中，量子门通过编织轨迹实现。$\blacksquare$

**Physical implementation note.** In a 1D wire system, Majoranas cannot be directly exchanged (they would have to pass through each other). Instead, a T-junction geometry is used: a horizontal wire joined by a vertical stub. Moving a Majorana from the stub to the horizontal wire and then to the other side effectively performs the exchange without the two modes meeting. This 2D-equivalent topological exchange is what Majorana-based qubit proposals (e.g. Microsoft's topological qubit roadmap) aim to implement.

**物理实现注记。** 在一维线系统中，马约拉纳模不能直接交换（它们必须相互穿过）。取而代之，使用 T 结几何：一条水平线与一个垂直短线相连。将马约拉纳从短线移到水平线再到另一侧，有效地执行了交换而两个模不相遇。这种等效二维的拓扑交换正是马约拉纳量子比特方案（例如微软拓扑量子比特路线图）旨在实现的。

---

*Summary: (A) In Majorana operator language the Kitaev chain Hamiltonian at $t = \Delta$, $\mu = 0$ pairs only inter-site Majorana modes, leaving $\gamma_{1,A}$ and $\gamma_{N,B}$ unpaired and at exactly zero energy. (B) The topological phase $|\mu| < 2t$ is identified by the $\mathbb{Z}_2$ Pfaffian invariant $M = -1$, following from the gap-closing transitions at $\mu = \pm 2t$; the resulting degenerate ground states $|0\rangle$ and $f^\dagger|0\rangle$ differ only in parity of the non-local fermion $f = (\gamma_L + i\gamma_R)/2$. (C) Adiabatic exchange of two Majorana modes implements $U_{ij} = \exp(\pi\gamma_i \gamma_j/4)$ on the ground-state subspace; since these generators satisfy non-commuting algebra, sequential braidings realize non-Abelian statistics and provide the building blocks of fault-tolerant topological quantum gates.*

*总结：(A) 在马约拉纳算符语言中，基塔耶夫链哈密顿量在 $t = \Delta$、$\mu = 0$ 处仅配对格点间马约拉纳模，使 $\gamma_{1,A}$ 和 $\gamma_{N,B}$ 未配对且精确处于零能。(B) 拓扑相 $|\mu| < 2t$ 由 $\mathbb{Z}_2$ 普法夫不变量 $M = -1$ 标识，来源于 $\mu = \pm 2t$ 处的能隙关闭相变；由此产生的简并基态 $|0\rangle$ 和 $f^\dagger|0\rangle$ 仅在非局域费米子 $f = (\gamma_L + i\gamma_R)/2$ 的宇称上不同。(C) 两个马约拉纳模的绝热交换在基态子空间上实现 $U_{ij} = \exp(\pi\gamma_i \gamma_j/4)$；由于这些生成元满足不对易代数，序贯编织实现非阿贝尔统计，提供容错拓扑量子门的构建块。*

---
title: "Derivations — Module 4.12: The Hubbard Model & Mott Insulators"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 4.12: The Hubbard Model & Mott Insulators
# 推导 — 模块 4.12：哈伯德模型与莫特绝缘体

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 4.12](./module-4.12-hubbard-model-and-mott-insulators.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 4.12](./module-4.12-hubbard-model-and-mott-insulators.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Hubbard Hamiltonian and Its Two Solvable Limits · 哈伯德哈密顿量及其两个可解极限

**Claim.** The Hubbard Hamiltonian $H = -t \sum_{\langle ij\rangle,\sigma} (c^\dagger_{i\sigma} c_{j\sigma} + \text{h.c.}) + U \sum_i n_{i\uparrow} n_{i\downarrow}$ reduces, at $U = 0$, to a tight-binding band with dispersion $\varepsilon_k = -2t \sum_a \cos(k_a a)$ and bandwidth $W = 2zt$; and at $t = 0$, to a sum of independent sites with single-site energies $0$ (empty or singly occupied) or $U$ (doubly occupied).

**命题。** 哈伯德哈密顿量 $H = -t \sum_{\langle ij\rangle,\sigma} (c^\dagger_{i\sigma} c_{j\sigma} + \text{h.c.}) + U \sum_i n_{i\uparrow} n_{i\downarrow}$ 在 $U = 0$ 时化为色散为 $\varepsilon_k = -2t \sum_a \cos(k_a a)$、带宽为 $W = 2zt$ 的紧束缚能带；在 $t = 0$ 时化为独立格点之和，单格点能量为 $0$（空或单占据）或 $U$（双占据）。

**Step 1 — Set up the model.** The operators obey fermionic anticommutation $\{c_{i\sigma}, c^\dagger_{j\sigma'}\} = \delta_{ij} \delta_{\sigma\sigma'}$, with $n_{i\sigma} = c^\dagger_{i\sigma} c_{i\sigma}$. The hopping term moves an electron of spin $\sigma$ from site $j$ to site $i$ with amplitude $-t$ over nearest-neighbour bonds; the interaction term adds $U$ for every doubly-occupied site. We treat the two terms in their respective dominant limits.

**第 1 步 — 建立模型。** 算符满足费米子反对易关系 $\{c_{i\sigma}, c^\dagger_{j\sigma'}\} = \delta_{ij} \delta_{\sigma\sigma'}$，且 $n_{i\sigma} = c^\dagger_{i\sigma} c_{i\sigma}$。跃迁项以幅度 $-t$ 将自旋为 $\sigma$ 的电子从格点 $j$ 沿最近邻键移到格点 $i$；相互作用项对每个双占据格点加上 $U$。我们在各自的主导极限下处理这两项。

**Step 2 — The $U = 0$ limit (tight-binding band).** With $U = 0$ only the hopping term survives, and each spin $\sigma$ is independent. Fourier transform $c_{i\sigma} = (1/\sqrt N) \sum_k e^{ik\cdot r_i} c_{k\sigma}$. On a hypercubic lattice with lattice constant $a$, each site has neighbours at $\pm a \hat x_a$ along the $d$ axes $a = 1,\ldots,d$. The hopping term becomes

$$ H_{U=0} = -t \sum_{k\sigma} \Big[ \sum_a (e^{ik_a a} + e^{-ik_a a}) \Big] c^\dagger_{k\sigma} c_{k\sigma} = \sum_{k\sigma} \varepsilon_k c^\dagger_{k\sigma} c_{k\sigma}, \qquad \varepsilon_k = -2t \sum_a \cos(k_a a). $$

The cosine ranges over $[-1, +1]$, so $\varepsilon_k$ runs from $-2td$ (at $k = 0$) to $+2td$ (at the zone corner). The full bandwidth is therefore

$$ W = \varepsilon_\text{max} - \varepsilon_\text{min} = 4td = 2zt, $$

using the hypercubic coordination number $z = 2d$. At $U = 0$ the half-filled system fills this band to its middle and is a metal.

**第 2 步 — $U = 0$ 极限（紧束缚能带）。** 当 $U = 0$ 时仅跃迁项存留，且每个自旋 $\sigma$ 独立。傅里叶变换 $c_{i\sigma} = (1/\sqrt N) \sum_k e^{ik\cdot r_i} c_{k\sigma}$。在晶格常数为 $a$ 的超立方格子上，每个格点沿 $d$ 个轴 $a = 1,\ldots,d$ 在 $\pm a \hat x_a$ 处有邻居。跃迁项变为

$$ H_{U=0} = -t \sum_{k\sigma} \Big[ \sum_a (e^{ik_a a} + e^{-ik_a a}) \Big] c^\dagger_{k\sigma} c_{k\sigma} = \sum_{k\sigma} \varepsilon_k c^\dagger_{k\sigma} c_{k\sigma}, \qquad \varepsilon_k = -2t \sum_a \cos(k_a a). $$

余弦取值于 $[-1, +1]$，故 $\varepsilon_k$ 从 $-2td$（在 $k = 0$）变到 $+2td$（在布里渊区角）。因此总带宽为

$$ W = \varepsilon_\text{max} - \varepsilon_\text{min} = 4td = 2zt, $$

其中用了超立方配位数 $z = 2d$。在 $U = 0$ 时半填充系统将此能带填至中部，为金属。

**Step 3 — The $t = 0$ limit (atomic limit).** With $t = 0$ the lattice decouples into independent sites, $H_{t=0} = U \sum_i n_{i\uparrow} n_{i\downarrow}$, and we diagonalise a single site. Its Hilbert space has four states with energies

$$ |0\rangle \text{ (empty):}\ E = 0, \qquad |\uparrow\rangle, |\downarrow\rangle \text{ (singly occupied):}\ E = 0, \qquad |\uparrow\downarrow\rangle \text{ (doubly occupied):}\ E = U, $$

since $n_{\uparrow} n_{\downarrow} = 1$ only on the doubly-occupied state. The spectrum of the whole lattice is built from these, so every site contributes **$0$ or $U$**. At half-filling the lowest-energy configuration places one electron per site (total energy $0$) with a $2^N$ spin degeneracy — and any conduction requires creating a doubly-occupied site at cost $U$. $\blacksquare$

**第 3 步 — $t = 0$ 极限（原子极限）。** 当 $t = 0$ 时格子解耦为独立格点，$H_{t=0} = U \sum_i n_{i\uparrow} n_{i\downarrow}$，我们对单个格点对角化。其希尔伯特空间有四个态，能量为

$$ |0\rangle \text{（空）：}\ E = 0, \qquad |\uparrow\rangle, |\downarrow\rangle \text{（单占据）：}\ E = 0, \qquad |\uparrow\downarrow\rangle \text{（双占据）：}\ E = U, $$

因为只有双占据态满足 $n_{\uparrow} n_{\downarrow} = 1$。整个格子的谱由这些构成，故每个格点贡献 **$0$ 或 $U$**。半填充下最低能组态为每格点一个电子（总能量 $0$），具有 $2^N$ 自旋简并——任何导电都需要以代价 $U$ 产生一个双占据格点。$\blacksquare$

---

## B. The Mott Gap at Half-Filling · 半填充下的莫特能隙

**Claim.** At half-filling, for $U \gg W$ the atomic level splits into a lower and an upper Hubbard band, each of width $\approx W$, centred at $\approx 0$ and $\approx U$ respectively; the charge (Mott) gap is $\Delta_\text{Mott} \approx U - W$, closing at the transition $U_c \sim W$.

**命题。** 在半填充下，当 $U \gg W$ 时原子能级劈裂为下、上哈伯德带，各宽 $\approx W$，分别以 $\approx 0$ 和 $\approx U$ 为中心；电荷（莫特）能隙为 $\Delta_\text{Mott} \approx U - W$，在相变 $U_c \sim W$ 处闭合。

**Step 1 — Charge excitations of the atomic limit.** Start at half-filling in the atomic limit (one electron per site). The relevant charge excitations are: (i) **removing** an electron from a singly-occupied site, leaving a hole — this costs energy $0$ relative to the chemical potential $\mu = U/2$ chosen symmetrically; (ii) **adding** an electron to a singly-occupied site, creating a double occupancy — this costs $U$. Measured from the chemical potential $\mu = U/2$, the removal (hole) states sit at energy $-U/2$ and the addition (double-occupancy) states at $+U/2$. The bare atomic gap between adding and removing a charge is exactly $U$.

**第 1 步 — 原子极限的电荷激发。** 从原子极限的半填充出发（每格点一个电子）。相关电荷激发为：(i) 从单占据格点**移走**一个电子，留下空穴——相对于对称选取的化学势 $\mu = U/2$，此过程能量代价为 $0$；(ii) 向单占据格点**加入**一个电子，产生双占据——代价为 $U$。从化学势 $\mu = U/2$ 量起，移走（空穴）态位于能量 $-U/2$，加入（双占据）态位于 $+U/2$。加入与移走一个电荷之间的裸原子能隙恰为 $U$。

**Step 2 — Broadening by hopping.** Turning on $t$ lets these charge excitations propagate. A hole in the sea of singly-occupied sites, or an added doubly-occupied site, can hop from site to site, acquiring dispersion just as in the tight-binding problem of Derivation A. Each set of charge excitations therefore broadens into a band of width $\approx W = 2zt$:

- the **lower Hubbard band (LHB)** of removal states, centred at $\approx -U/2$ (i.e. $\approx 0$ measured from the bottom), spanning $\approx W$;
- the **upper Hubbard band (UHB)** of addition states, centred at $\approx +U/2$ (i.e. $\approx U$), spanning $\approx W$.

**第 2 步 — 跃迁导致的展宽。** 开启 $t$ 使这些电荷激发能够传播。单占据格点海洋中的一个空穴，或一个新增的双占据格点，可以从格点跳到格点，如推导 A 的紧束缚问题那样获得色散。因此每组电荷激发展宽为宽度 $\approx W = 2zt$ 的能带：

- 移走态构成的**下哈伯德带（LHB）**，中心约在 $-U/2$（即从带底量起约为 $0$），跨度 $\approx W$；
- 加入态构成的**上哈伯德带（UHB）**，中心约在 $+U/2$（即约为 $U$），跨度 $\approx W$。

**Step 3 — The gap.** The gap to create a separated electron–hole pair (the charge gap) is the energy of the bottom of the UHB minus the top of the LHB. The band centres are split by $U$; subtracting half the width of each band ($W/2$ from the top of the LHB and $W/2$ from the bottom of the UHB) gives

$$ \Delta_\text{Mott} \approx U - (W/2 + W/2) = U - W. $$

**第 3 步 — 能隙。** 产生分离的电子–空穴对的能隙（电荷能隙）为 UHB 底部能量减去 LHB 顶部能量。两带中心相差 $U$；减去各带半宽（LHB 顶部的 $W/2$ 和 UHB 底部的 $W/2$）给出

$$ \Delta_\text{Mott} \approx U - (W/2 + W/2) = U - W. $$

**Step 4 — The transition.** The gap is positive (the system is a **Mott insulator**) for $U > W$ and vanishes when

$$ U_c \sim W, $$

below which the lower and upper Hubbard bands overlap and merge into a single half-filled metallic band. This simple band-edge estimate captures the essential physics; the precise critical ratio $U_c/W$ and the first-order, hysteretic character of the transition at intermediate coupling require **DMFT**. $\blacksquare$

**第 4 步 — 相变。** 当 $U > W$ 时能隙为正（系统为**莫特绝缘体**），并在

$$ U_c \sim W $$

时消失，其下下、上哈伯德带交叠并合并为单一半填充金属带。这一简单的带边估计抓住了本质物理；精确的临界比 $U_c/W$ 以及中等耦合下相变的一级、滞回特征则需要 **DMFT**。$\blacksquare$

---

## C. Superexchange: $J = 4t^2/U$ (the key result) · 超交换：$J = 4t^2/U$（关键结果）

**Claim.** In the half-filled Hubbard model with $U \gg t$, degenerate second-order perturbation theory in the hopping $t$ gives an effective spin Hamiltonian for each bond. The result is the antiferromagnetic Heisenberg model $H_\text{eff} = J \sum_{\langle ij\rangle} \boldsymbol{S}_i \cdot \boldsymbol{S}_j$ with $J = 4t^2/U > 0$.

**命题。** 在 $U \gg t$ 的半填充哈伯德模型中，对跃迁 $t$ 的简并二阶微扰论给出每条键的有效自旋哈密顿量。结果为反铁磁海森堡模型 $H_\text{eff} = J \sum_{\langle ij\rangle} \boldsymbol{S}_i \cdot \boldsymbol{S}_j$，其中 $J = 4t^2/U > 0$。

**Step 1 — The unperturbed problem on one bond.** Consider two neighbouring sites $i, j$ with one electron each (half-filling). Split $H = H_0 + V$, with $H_0 = U \sum n_\uparrow n_\downarrow$ the atomic (interaction) part and $V = -t \sum_\sigma (c^\dagger_{i\sigma} c_{j\sigma} + c^\dagger_{j\sigma} c_{i\sigma})$ the hopping. The ground manifold of $H_0$ has both sites singly occupied (no double occupancy), energy $E_0 = 0$, and is **four-fold degenerate** in spin: $\{|\uparrow\uparrow\rangle, |\uparrow\downarrow\rangle, |\downarrow\uparrow\rangle, |\downarrow\downarrow\rangle\}$. The hopping $V$ is the perturbation; we treat it to second order within this degenerate ground manifold.

**第 1 步 — 单键上的无微扰问题。** 考虑两个相邻格点 $i$、$j$，各有一个电子（半填充）。分解 $H = H_0 + V$，其中 $H_0 = U \sum n_\uparrow n_\downarrow$ 为原子（相互作用）部分，$V = -t \sum_\sigma (c^\dagger_{i\sigma} c_{j\sigma} + c^\dagger_{j\sigma} c_{i\sigma})$ 为跃迁。$H_0$ 的基态流形为两格点均单占据（无双占据），能量 $E_0 = 0$，在自旋上**四重简并**：$\{|\uparrow\uparrow\rangle, |\uparrow\downarrow\rangle, |\downarrow\uparrow\rangle, |\downarrow\downarrow\rangle\}$。跃迁 $V$ 为微扰；我们在此简并基态流形内将其处理到二阶。

**Step 2 — First order vanishes.** Acting once with $V$ on any ground state moves one electron onto its neighbour, producing a state with one empty and one doubly-occupied site. Such states lie outside the ground manifold (they have energy $U$), so $\langle\text{ground}|V|\text{ground}\rangle = 0$: the first-order correction vanishes and we must go to second order.

**第 2 步 — 一阶为零。** $V$ 作用于任一基态一次，会将一个电子移到其邻居上，产生一个一空一双占据的态。此类态位于基态流形之外（能量为 $U$），故 $\langle\text{基态}|V|\text{基态}\rangle = 0$：一阶修正为零，必须进至二阶。

**Step 3 — Second-order effective Hamiltonian.** Degenerate second-order perturbation theory gives an effective Hamiltonian within the ground manifold

$$ (H_\text{eff})_{ab} = \sum_m \frac{\langle a|V|m\rangle\langle m|V|b\rangle}{E_0 - E_m}, $$

where $|m\rangle$ runs over the excited (doubly-occupied) intermediate states with $E_m = U$ and $E_0 = 0$, so the energy denominator is $E_0 - E_m = -U$.

**第 3 步 — 二阶有效哈密顿量。** 简并二阶微扰论给出基态流形内的有效哈密顿量

$$ (H_\text{eff})_{ab} = \sum_m \frac{\langle a|V|m\rangle\langle m|V|b\rangle}{E_0 - E_m}, $$

其中 $|m\rangle$ 遍历激发（双占据）中间态，$E_m = U$ 且 $E_0 = 0$，故能量分母为 $E_0 - E_m = -U$。

**Step 4 — Parallel spins: no virtual hopping.** Take the fully aligned state $|\uparrow\uparrow\rangle$. Hopping would require moving an $\uparrow$ electron onto a site already holding an $\uparrow$ electron, i.e. two $\uparrow$ electrons on one site — forbidden by the Pauli principle (Module 3.5). Hence $V|\uparrow\uparrow\rangle$ has no component in the doubly-occupied manifold, and the second-order shift is

$$ \Delta E(\text{parallel}) = 0. $$

The same holds for $|\downarrow\downarrow\rangle$. Parallel neighbouring spins gain nothing.

**第 4 步 — 平行自旋：无虚跃迁。** 取完全对齐态 $|\uparrow\uparrow\rangle$。跃迁需要将一个 $\uparrow$ 电子移到已持有 $\uparrow$ 电子的格点上，即一个格点上两个 $\uparrow$ 电子——被泡利原理禁止（模块 3.5）。因此 $V|\uparrow\uparrow\rangle$ 在双占据流形中无分量，二阶移动为

$$ \Delta E(\text{平行}) = 0. $$

$|\downarrow\downarrow\rangle$ 同理。平行相邻自旋无所获。

**Step 5 — Antiparallel spins: two virtual channels.** Take the antiparallel state $|\uparrow\downarrow\rangle$ ($\uparrow$ on site $i$, $\downarrow$ on site $j$). The perturbation $V$ can move either electron onto its neighbour, producing two distinct doubly-occupied intermediate states $|m\rangle$ (both at energy $U$): the $\uparrow$ hops from $i$ to $j$ giving $|0, \uparrow\downarrow\rangle_j$, or the $\downarrow$ hops from $j$ to $i$ giving $|\uparrow\downarrow, 0\rangle_i$. Each path has matrix element $\pm t$ and an energy denominator $-U$, contributing

$$ \Delta E \text{ per channel} = \frac{|\langle m|V|\uparrow\downarrow\rangle|^2}{E_0 - E_m} = \frac{t^2}{-U} = -t^2/U. $$

There are two such channels (the $\uparrow$ hopping right, the $\downarrow$ hopping left), so the diagonal second-order shift of $|\uparrow\downarrow\rangle$ is

$$ \Delta E_\text{diag} = 2 \times (-t^2/U) = -2t^2/U. $$

**第 5 步 — 反平行自旋：两个虚跃迁通道。** 取反平行态 $|\uparrow\downarrow\rangle$（$\uparrow$ 在格点 $i$，$\downarrow$ 在格点 $j$）。微扰 $V$ 可将任一电子移到其邻居上，产生两个不同的双占据中间态 $|m\rangle$（均处能量 $U$）：$\uparrow$ 从 $i$ 跳到 $j$ 给出 $|0, \uparrow\downarrow\rangle_j$，或 $\downarrow$ 从 $j$ 跳到 $i$ 给出 $|\uparrow\downarrow, 0\rangle_i$。每条路径的矩阵元为 $\pm t$，能量分母为 $-U$，贡献

$$ \Delta E \text{ 每通道} = \frac{|\langle m|V|\uparrow\downarrow\rangle|^2}{E_0 - E_m} = \frac{t^2}{-U} = -t^2/U. $$

共有两条这样的通道（$\uparrow$ 右跳、$\downarrow$ 左跳），故 $|\uparrow\downarrow\rangle$ 的对角二阶移动为

$$ \Delta E_\text{diag} = 2 \times (-t^2/U) = -2t^2/U. $$

**Step 6 — Off-diagonal (spin-flip) term.** The two intermediate states also connect $|\uparrow\downarrow\rangle$ to $|\downarrow\uparrow\rangle$: an $\uparrow$ electron hops from $i$ to $j$, then the $\downarrow$ already at $j$ hops back to $i$, exchanging the two spins. This generates an off-diagonal matrix element of the same magnitude,

$$ (H_\text{eff})_{\uparrow\downarrow,\downarrow\uparrow} = -2t^2/U. $$

The $2\times 2$ block in the $\{|\uparrow\downarrow\rangle, |\downarrow\uparrow\rangle\}$ subspace is therefore

$$ H_\text{eff} = -\frac{2t^2}{U} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}. $$

Its eigenstates are the **singlet** $(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)/\sqrt 2$ with eigenvalue $-4t^2/U$, and a **triplet member** $(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle)/\sqrt 2$ with eigenvalue $0$. Together with $|\uparrow\uparrow\rangle$ and $|\downarrow\downarrow\rangle$ (also eigenvalue $0$), the triplet ($S = 1$) is three-fold degenerate at energy $0$ and the singlet ($S = 0$) sits below it at energy $-4t^2/U$. The singlet is favoured — antiferromagnetic correlation.

**第 6 步 — 非对角（自旋翻转）项。** 这两个中间态还将 $|\uparrow\downarrow\rangle$ 连到 $|\downarrow\uparrow\rangle$：一个 $\uparrow$ 电子从 $i$ 跳到 $j$，然后已在 $j$ 的 $\downarrow$ 跳回 $i$，交换两个自旋。这产生一个同样大小的非对角矩阵元，

$$ (H_\text{eff})_{\uparrow\downarrow,\downarrow\uparrow} = -2t^2/U. $$

因此 $\{|\uparrow\downarrow\rangle, |\downarrow\uparrow\rangle\}$ 子空间中的 $2\times 2$ 块为

$$ H_\text{eff} = -\frac{2t^2}{U} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}. $$

其本征态为**单态** $(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)/\sqrt 2$，本征值 $-4t^2/U$，以及一个**三重态成员** $(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle)/\sqrt 2$，本征值 $0$。连同 $|\uparrow\uparrow\rangle$ 与 $|\downarrow\downarrow\rangle$（本征值也为 $0$），三重态（$S = 1$）在能量 $0$ 处三重简并，单态（$S = 0$）位于其下，能量 $-4t^2/U$。单态受偏好——反铁磁关联。

**Step 7 — Recast as a Heisenberg coupling.** We now write the spectrum $\{\text{singlet at } -4t^2/U,\ \text{triplet at } 0\}$ in terms of the spin operators $\boldsymbol{S}_i \cdot \boldsymbol{S}_j$. Using $\boldsymbol{S}_i \cdot \boldsymbol{S}_j = \tfrac12[(\boldsymbol{S}_i + \boldsymbol{S}_j)^2 - \boldsymbol{S}_i^2 - \boldsymbol{S}_j^2] = \tfrac12[S_\text{tot}(S_\text{tot}+1) - \tfrac34 - \tfrac34]$, with $S_i = S_j = \tfrac12$:

$$ \text{singlet } (S_\text{tot} = 0):\ \boldsymbol{S}_i \cdot \boldsymbol{S}_j = \tfrac12[0 - 3/2] = -3/4, \qquad \text{triplet } (S_\text{tot} = 1):\ \boldsymbol{S}_i \cdot \boldsymbol{S}_j = \tfrac12[2 - 3/2] = +1/4. $$

Posit $H_\text{eff} = J\, \boldsymbol{S}_i \cdot \boldsymbol{S}_j + c$ (constant $c$). Matching the two energies:

$$ J(-3/4) + c = -4t^2/U \ \text{(singlet)}, \qquad J(+1/4) + c = 0 \ \text{(triplet)}. $$

Subtracting the second from the first eliminates $c$:

$$ J(-3/4 - 1/4) = -4t^2/U \implies -J = -4t^2/U \implies J = 4t^2/U. $$

**第 7 步 — 重写为海森堡耦合。** 现在用自旋算符 $\boldsymbol{S}_i \cdot \boldsymbol{S}_j$ 表达谱 $\{\text{单态在 } -4t^2/U,\ \text{三重态在 } 0\}$。利用 $\boldsymbol{S}_i \cdot \boldsymbol{S}_j = \tfrac12[(\boldsymbol{S}_i + \boldsymbol{S}_j)^2 - \boldsymbol{S}_i^2 - \boldsymbol{S}_j^2] = \tfrac12[S_\text{tot}(S_\text{tot}+1) - \tfrac34 - \tfrac34]$，且 $S_i = S_j = \tfrac12$：

$$ \text{单态（}S_\text{tot} = 0\text{）：}\boldsymbol{S}_i \cdot \boldsymbol{S}_j = \tfrac12[0 - 3/2] = -3/4, \qquad \text{三重态（}S_\text{tot} = 1\text{）：}\boldsymbol{S}_i \cdot \boldsymbol{S}_j = \tfrac12[2 - 3/2] = +1/4. $$

设 $H_\text{eff} = J\, \boldsymbol{S}_i \cdot \boldsymbol{S}_j + c$（常数 $c$）。匹配两个能量：

$$ J(-3/4) + c = -4t^2/U \ \text{（单态）}, \qquad J(+1/4) + c = 0 \ \text{（三重态）}. $$

第一式减第二式消去 $c$：

$$ J(-3/4 - 1/4) = -4t^2/U \implies -J = -4t^2/U \implies J = 4t^2/U. $$

**Step 8 — The lattice Hamiltonian.** Each bond $\langle ij\rangle$ contributes the same term, so summing over all nearest-neighbour bonds gives the effective low-energy Hamiltonian of the half-filled Mott insulator:

$$ H_\text{eff} = J \sum_{\langle ij\rangle} \boldsymbol{S}_i \cdot \boldsymbol{S}_j, \qquad J = 4t^2/U > 0. $$

Since $J > 0$, the energy is lowered by antiparallel neighbours: the large-$U$ half-filled Hubbard model is an **antiferromagnet**. This both confirms the AFM sign anticipated in Module 2 of the companion and gives the microscopic origin of the Heisenberg exchange $J$ introduced phenomenologically in Module 4.6. $\blacksquare$

**第 8 步 — 格子哈密顿量。** 每条键 $\langle ij\rangle$ 贡献相同的项，故对所有最近邻键求和给出半填充莫特绝缘体的有效低能哈密顿量：

$$ H_\text{eff} = J \sum_{\langle ij\rangle} \boldsymbol{S}_i \cdot \boldsymbol{S}_j, \qquad J = 4t^2/U > 0. $$

由于 $J > 0$，能量在相邻自旋反平行时降低：大 $U$ 半填充哈伯德模型为**反铁磁体**。这既证实了配套文档第 2 节预期的 AFM 符号，又给出了模块 4.6 中唯象引入的海森堡交换 $J$ 的微观起源。$\blacksquare$

---

## D. From Hubbard to the t–J Model · 从哈伯德到 t–J 模型

**Claim.** Away from half-filling, the canonical transformation that eliminates double occupancy to order $t^2/U$ turns the large-$U$ Hubbard model into the t–J model: constrained hopping in the no-double-occupancy subspace plus the $J = 4t^2/U$ exchange.

**命题。** 偏离半填充时，消去双占据至 $t^2/U$ 阶的正则变换将大 $U$ 哈伯德模型变为 t–J 模型：无双占据子空间中的受限跃迁加上 $J = 4t^2/U$ 交换。

**Step 1 — The low-energy subspace.** For $U \gg t$ the spectrum splits into sectors labelled by the number $N_d$ of doubly-occupied sites, separated by energy gaps $\approx U$. The low-energy physics lives in the **$N_d = 0$ subspace** (no double occupancy). Let $P$ be the projector onto this subspace. At exactly half-filling $N_d = 0$ means one electron per site and there is no room to move — only the spin (superexchange) dynamics of Derivation C survive. Away from half-filling there are empty sites (holes), and holes *can* move within the $N_d = 0$ subspace.

**第 1 步 — 低能子空间。** 当 $U \gg t$ 时，谱按双占据格点数 $N_d$ 分裂为不同扇区，彼此相隔能隙 $\approx U$。低能物理存在于 **$N_d = 0$ 子空间**（无双占据）。设 $P$ 为到此子空间的投影算符。在恰好半填充时 $N_d = 0$ 意味着每格点一个电子，无移动空间——仅推导 C 的自旋（超交换）动力学存留。偏离半填充时存在空位（空穴），空穴*可以*在 $N_d = 0$ 子空间内移动。

**Step 2 — Canonical (Schrieffer–Wolff) transformation.** Write $H = H_0 + V$ with $H_0 = U \sum n_\uparrow n_\downarrow$ and $V$ the hopping. A unitary transformation $\tilde H = e^{iS} H e^{-iS}$, with $S$ chosen of order $t/U$ to cancel the terms of $V$ that change $N_d$, removes the coupling to the high-energy (doubly-occupied) sector to leading order. The transformed Hamiltonian, projected onto $N_d = 0$, has two surviving pieces:

- the part of $V$ that does **not** change $N_d$, i.e. hopping of holes through singly-occupied sites — the **constrained hopping** $P(-t \sum c^\dagger c)P$;
- the second-order term $V (E_0 - H_0)^{-1} V$ generated by the transformation, which on neighbouring spins is exactly the superexchange of Derivation C — the **$J\, \boldsymbol{S}\cdot\boldsymbol{S}$** term.

**第 2 步 — 正则（Schrieffer–Wolff）变换。** 写 $H = H_0 + V$，其中 $H_0 = U \sum n_\uparrow n_\downarrow$，$V$ 为跃迁。选取量级为 $t/U$ 的 $S$，作幺正变换 $\tilde H = e^{iS} H e^{-iS}$ 以抵消 $V$ 中改变 $N_d$ 的项，从而在领头阶移除与高能（双占据）扇区的耦合。变换后的哈密顿量投影到 $N_d = 0$ 后，留下两部分：

- $V$ 中**不**改变 $N_d$ 的部分，即空穴通过单占据格点的跃迁——**受限跃迁** $P(-t \sum c^\dagger c)P$；
- 变换生成的二阶项 $V (E_0 - H_0)^{-1} V$，作用在相邻自旋上恰为推导 C 的超交换——**$J\, \boldsymbol{S}\cdot\boldsymbol{S}$** 项。

**Step 3 — The t–J Hamiltonian.** Collecting both pieces gives

$$ H_{tJ} = -t \sum_{\langle ij\rangle,\sigma} P (c^\dagger_{i\sigma} c_{j\sigma} + \text{h.c.}) P + J \sum_{\langle ij\rangle} (\boldsymbol{S}_i \cdot \boldsymbol{S}_j - \tfrac14 n_i n_j), \qquad J = 4t^2/U, $$

where the $-\tfrac14 n_i n_j$ term (a density–density correction also produced at order $t^2/U$) is conventionally grouped with the exchange and vanishes at half-filling where $n_i = 1$. At half-filling the projector kills the hopping term and $H_{tJ} \to J \sum \boldsymbol{S}_i \cdot \boldsymbol{S}_j$, recovering Derivation C. With a finite density of holes the constrained hopping is active, and the model describes holes propagating through (and frustrating) an antiferromagnetic spin background.

**第 3 步 — t–J 哈密顿量。** 合并两部分给出

$$ H_{tJ} = -t \sum_{\langle ij\rangle,\sigma} P (c^\dagger_{i\sigma} c_{j\sigma} + \text{h.c.}) P + J \sum_{\langle ij\rangle} (\boldsymbol{S}_i \cdot \boldsymbol{S}_j - \tfrac14 n_i n_j), \qquad J = 4t^2/U, $$

其中 $-\tfrac14 n_i n_j$ 项（同样在 $t^2/U$ 阶产生的密度–密度修正）按惯例与交换项归为一组，并在 $n_i = 1$ 的半填充处消失。半填充时投影算符消去跃迁项，$H_{tJ} \to J \sum \boldsymbol{S}_i \cdot \boldsymbol{S}_j$，回到推导 C。当存在有限空穴密度时受限跃迁起作用，模型描述空穴在反铁磁自旋背景中传播（并使其受挫）。

**Step 4 — Physical consequences.** This is the standard starting point for **doped Mott insulators** and the high-$T_c$ cuprates (Module 5.9): the undoped $\text{CuO}_2$ planes are antiferromagnetic Mott insulators (the $J$ term), and doping injects holes whose motion (the constrained-$t$ term) competes with antiferromagnetism and is widely believed to underlie cuprate superconductivity. Two caveats. First, in many real oxides the lowest charge excitation moves charge from oxygen-$p$ to metal-$d$ orbitals: the relevant gap is then a **charge-transfer gap** $\Delta_\text{CT}$ smaller than the bare Mott $U$, and the material is a "charge-transfer insulator" — still Mott-like but requiring a multi-orbital (e.g. three-band) description. Second, at **intermediate $U \sim W$** neither the band limit nor the atomic/t–J limit applies; quantitative results there require **DMFT and numerical methods** (QMC, DMRG, cluster DMFT). $\blacksquare$

**第 4 步 — 物理结果。** 这是**掺杂莫特绝缘体**与高温铜氧化物超导体（模块 5.9）的标准出发点：未掺杂的 $\text{CuO}_2$ 平面是反铁磁莫特绝缘体（$J$ 项），掺杂注入空穴，其运动（受限 $t$ 项）与反铁磁性竞争，普遍认为这是铜氧化物超导的根源。两点提醒。其一，许多真实氧化物中最低电荷激发是把电荷从氧 $p$ 轨道移到金属 $d$ 轨道：此时相关能隙为比裸莫特 $U$ 更小的**电荷转移能隙** $\Delta_\text{CT}$，材料为"电荷转移绝缘体"——仍属莫特类，但需要多轨道（如三带）描述。其二，在**中等 $U \sim W$** 时能带极限与原子/t–J 极限均不适用；那里的定量结果需要 **DMFT 与数值方法**（QMC、DMRG、团簇 DMFT）。$\blacksquare$

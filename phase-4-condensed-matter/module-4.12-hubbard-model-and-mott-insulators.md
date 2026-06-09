# Module 4.12 — The Hubbard Model & Mott Insulators
**模块 4.12 — 哈伯德模型与莫特绝缘体**

> **Phase 4 — [Condensed Matter / Solid State](./README.md)** · Format: Definition → Demonstration → Application
> **第 4 阶段 — 凝聚态 / 固体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-4.12-hubbard-model-and-mott-insulators-derivations.md)

---

## 1. The Hubbard Model · 哈伯德模型

**Definition.** The **Hubbard model** is the minimal lattice model of interacting electrons, capturing the competition between the kinetic tendency to delocalize and the Coulomb tendency to localize. On a lattice with sites $i$ it reads

$$ H = -t \sum_{\langle ij\rangle,\sigma} (c^\dagger_{i\sigma} c_{j\sigma} + \text{h.c.}) + U \sum_i n_{i\uparrow} n_{i\downarrow} $$

where $c^\dagger_{i\sigma}$ creates an electron of spin $\sigma$ on site $i$, $n_{i\sigma} = c^\dagger_{i\sigma} c_{i\sigma}$, and $\langle ij\rangle$ runs over nearest-neighbor bonds. The **hopping** term (amplitude $t$) is the tight-binding kinetic energy; it broadens atomic levels into a band of width $W \approx 2zt$, where $z$ is the coordination number. The **on-site Coulomb** term (energy $U > 0$) penalizes double occupancy of a single site: two electrons of opposite spin on the same orbital cost an extra energy $U$. (Cf. Module 4.4 for tight-binding bands and Bloch states; the Coulomb–Pauli origin of such interactions is set up in Modules 3.5 and 4.6.)

**定义。** **哈伯德模型**是相互作用电子的最简格点模型，刻画了动能的离域倾向与库仑相互作用的局域倾向之间的竞争。在以 $i$ 标记格点的格子上它写为

$$ H = -t \sum_{\langle ij\rangle,\sigma} (c^\dagger_{i\sigma} c_{j\sigma} + \text{h.c.}) + U \sum_i n_{i\uparrow} n_{i\downarrow} $$

其中 $c^\dagger_{i\sigma}$ 在格点 $i$ 上产生一个自旋为 $\sigma$ 的电子，$n_{i\sigma} = c^\dagger_{i\sigma} c_{i\sigma}$，$\langle ij\rangle$ 遍历最近邻键。**跃迁**项（幅度 $t$）是紧束缚动能；它将原子能级展宽为宽度 $W \approx 2zt$ 的能带，其中 $z$ 为配位数。**在位库仑**项（能量 $U > 0$）惩罚单个格点上的双占据：同一轨道上两个自旋相反的电子需要额外的能量 $U$。（紧束缚能带与布洛赫态见模块 4.4；此类相互作用的库仑–泡利起源见模块 3.5 和 4.6。）

**Demonstration — two solvable limits.** The model has two exactly solvable limits that bracket its physics (see Derivations A).

- **$U = 0$ (free / band limit):** only hopping survives. Fourier transforming gives a tight-binding band; on a hypercubic lattice with spacing $a$,

  $$ \varepsilon_k = -2t \sum_a \cos(k_a a) $$

  (the sum over Cartesian directions $a$). Electrons are itinerant and the system is metallic at generic filling.

- **$t = 0$ (atomic limit):** sites decouple. Each site has four states — $|0\rangle$, $|\uparrow\rangle$, $|\downarrow\rangle$, $|\uparrow\downarrow\rangle$ — with energies $0, 0, 0, U$. Singly occupied sites are degenerate (a free local spin); double occupancy costs $U$.

The full model interpolates between a delocalized band (small $U/t$) and an array of localized moments (large $U/t$). The dimensionless ratio $U/W$ controls everything.

**演示——两个可解极限。** 模型有两个精确可解的极限，框定了其物理（见推导 A）。

- **$U = 0$（自由 / 能带极限）：** 只剩跃迁项。傅里叶变换给出紧束缚能带；在格距为 $a$ 的超立方格子上，

  $$ \varepsilon_k = -2t \sum_a \cos(k_a a) $$

  （对笛卡尔方向 $a$ 求和）。电子是巡游的，一般填充下系统为金属。

- **$t = 0$（原子极限）：** 各格点解耦。每个格点有四个态——$|0\rangle$、$|\uparrow\rangle$、$|\downarrow\rangle$、$|\uparrow\downarrow\rangle$——能量为 $0, 0, 0, U$。单占据格点简并（一个自由的局域自旋）；双占据需要能量 $U$。

完整模型在离域能带（小 $U/t$）与局域磁矩阵列（大 $U/t$）之间插值。无量纲比 $U/W$ 决定一切。

**Application.** Despite its deceptive simplicity, the Hubbard model is believed to contain itinerant magnetism, the Mott metal–insulator transition, and — when doped — d-wave superconductivity. It is exactly solvable only in special cases (1D via Bethe ansatz, cf. Module 6.7; $U = 0$ or $t = 0$ trivially); in general dimensions it requires numerics or dynamical mean-field theory (DMFT). It is the standard "drosophila" of strongly correlated electron physics.

**应用。** 尽管表面上简单，哈伯德模型被认为蕴含巡游磁性、莫特金属–绝缘体相变，以及在掺杂后的 d 波超导。它仅在特殊情形精确可解（一维通过贝特拟设，见模块 6.7；$U = 0$ 或 $t = 0$ 平凡可解）；在一般维度需要数值或动力学平均场理论（DMFT）。它是强关联电子物理的标准"果蝇"模型。

---

## 2. The Mott Metal–Insulator Transition · 莫特金属–绝缘体相变

**Definition.** Consider the Hubbard model at **half-filling** — exactly one electron per site on average. Conventional band theory (Module 4.4) predicts a *metal*: a half-filled band conducts. But when the interaction dominates, $U \gg W$, the electrons localize one-per-site to avoid the energy cost $U$ of double occupancy, and the system becomes an insulator. This interaction-driven insulator is a **Mott insulator**, fundamentally distinct from a band (filled-band) insulator.

**定义。** 考虑半填充下的哈伯德模型——平均每格点恰好一个电子。常规能带理论（模块 4.4）预言为*金属*：半满能带导电。但当相互作用占主导，$U \gg W$ 时，电子局域为每格点一个以避免双占据的能量代价 $U$，系统成为绝缘体。这种由相互作用驱动的绝缘体即**莫特绝缘体**，与能带（满带）绝缘体本质不同。

**Demonstration — the Mott gap.** Track the energy to create a mobile charge excitation (see Derivations B). Starting from the half-filled, singly-occupied configuration:

- removing an electron leaves a hole that propagates in the **lower Hubbard band** (centered near energy $0$, bandwidth $\approx W$);
- adding an electron forces a double occupancy that propagates in the **upper Hubbard band** (centered near energy $U$, bandwidth $\approx W$).

The two bands are split by $U$ and broadened by $W$. The charge gap between them is

$$ \Delta_{\text{Mott}} \approx U - W. $$

For $U > W$ the gap is positive: an insulator. For $U < W$ the bands overlap and the system is a metal. The transition occurs near $U \sim W$. Crucially, the gap is opened by *interactions*, not by the lattice periodicity — there is no doubling of the unit cell, and the band would be metallic at $U = 0$.

**演示——莫特能隙。** 追踪产生一个可移动电荷激发所需的能量（见推导 B）。从半填充、单占据组态出发：

- 移除一个电子留下一个空穴，在**下哈伯德带**中传播（中心约在能量 $0$，带宽 $\approx W$）；
- 添加一个电子迫使产生一个双占据，在**上哈伯德带**中传播（中心约在能量 $U$，带宽 $\approx W$）。

两条带被 $U$ 劈裂、被 $W$ 展宽。它们之间的电荷能隙为

$$ \Delta_{\text{Mott}} \approx U - W. $$

当 $U > W$ 时能隙为正：绝缘体。当 $U < W$ 时两带交叠，系统为金属。相变发生在 $U \sim W$ 附近。关键在于，能隙是由*相互作用*打开的，而非晶格周期性——单胞没有加倍，且在 $U = 0$ 时能带本应是金属性的。

**Application — Mott vs band insulator.** A band insulator (e.g. an intrinsic semiconductor, Module 4.7) has an even number of electrons filling complete bands; its gap is a single-particle (band-structure) gap. A Mott insulator has an *odd* number of electrons per cell — band theory wrongly predicts a metal — and its gap is a many-body correlation gap. Transition-metal oxides (NiO, $\text{V}_2\text{O}_3$, cuprate parents) are canonical Mott insulators. When the upper Hubbard band lies above filled ligand (oxygen p) states, the relevant gap may instead be a **charge-transfer gap** (Zaanen–Sawatzky–Allen classification); the cuprates are charge-transfer insulators of Mott type.

**应用——莫特绝缘体与能带绝缘体。** 能带绝缘体（如本征半导体，模块 4.7）有偶数个电子填满完整能带；其能隙是单粒子（能带结构）能隙。莫特绝缘体每个单胞有*奇数*个电子——能带理论错误地预言金属——其能隙是多体关联能隙。过渡金属氧化物（NiO、$\text{V}_2\text{O}_3$、铜氧化物母体）是典范的莫特绝缘体。当上哈伯德带高于填满的配体（氧 p）态时，相关能隙可能转为**电荷转移能隙**（Zaanen–Sawatzky–Allen 分类）；铜氧化物是莫特型的电荷转移绝缘体。

---

## 3. Superexchange, the t–J Model & Consequences · 超交换、t–J 模型与物理后果

**Definition — superexchange.** Deep in the Mott phase (half-filling, $U \gg t$) the charge is frozen — one electron per site — but the **spins** remain free degrees of freedom. They are not, however, decoupled: virtual hopping to a neighbor and back lowers the energy of *antiparallel* neighboring spins while leaving *parallel* spins untouched (Pauli blocking forbids two same-spin electrons sharing a site). This second-order kinetic process is the **superexchange** mechanism, and it generates an effective spin Hamiltonian.

**定义——超交换。** 深入莫特相（半填充，$U \gg t$）时电荷被冻结——每格点一个电子——但**自旋**仍是自由度。然而它们并非解耦：向邻居的虚跃迁再跃回会降低*反平行*近邻自旋的能量，而对*平行*自旋无影响（泡利阻塞禁止两个同自旋电子共享一个格点）。这一二阶动力学过程即**超交换**机制，它产生一个有效自旋哈密顿量。

**Demonstration — the Heisenberg result $J = 4t^2/U$.** Do degenerate second-order perturbation theory in $t$ on a single bond (see Derivations C). For a parallel-spin pair, hopping is Pauli-forbidden $\Rightarrow$ no energy shift. For an antiparallel pair, an electron can virtually hop onto its neighbor (creating a doubly-occupied intermediate state of energy $U$) and hop back, giving a second-order shift of $-2\cdot(2t^2/U)$ per bond. Rewriting this spin-dependent shift in terms of $\mathbf{S}_i\cdot\mathbf{S}_j$ yields the **antiferromagnetic Heisenberg model**

$$ H_{\text{eff}} = J \sum_{\langle ij\rangle} \mathbf{S}_i \cdot \mathbf{S}_j, \qquad J = \frac{4t^2}{U} > 0. $$

The singlet (antiparallel-favoring) state is lowered relative to the triplet by exactly $J$, with $J = 4t^2/U$. The sign is *antiferromagnetic*: Mott insulators generically order antiferromagnetically (Néel order, Module 4.6).

**演示——海森堡结果 $J = 4t^2/U$。** 在单条键上对 $t$ 做简并二阶微扰论（见推导 C）。对平行自旋对，跃迁被泡利禁止 $\Rightarrow$ 无能量移动。对反平行对，一个电子可虚跃迁到邻居上（产生能量为 $U$ 的双占据中间态）再跃回，每条键给出二阶移动 $-2\cdot(2t^2/U)$。将此自旋相关的移动用 $\mathbf{S}_i\cdot\mathbf{S}_j$ 改写，得到**反铁磁海森堡模型**

$$ H_{\text{eff}} = J \sum_{\langle ij\rangle} \mathbf{S}_i \cdot \mathbf{S}_j, \qquad J = \frac{4t^2}{U} > 0. $$

单态（偏好反平行）相对三重态恰好降低 $J$，其中 $J = 4t^2/U$。符号为*反铁磁*：莫特绝缘体通常呈反铁磁序（奈尔序，模块 4.6）。

**Application — the t–J model and high-$T_c$.** Away from half-filling, the large-$U$ Hubbard model projects onto the **t–J model**: hopping is restricted to the subspace with *no* double occupancy (a constrained kinetic term $t$), supplemented by the superexchange $J\,\mathbf{S}_i\cdot\mathbf{S}_j$ between neighboring spins,

$$ H_{t\text{–}J} = -t \sum_{\langle ij\rangle,\sigma} P\,(c^\dagger_{i\sigma} c_{j\sigma} + \text{h.c.})\,P + J \sum_{\langle ij\rangle} \left(\mathbf{S}_i \cdot \mathbf{S}_j - \frac{n_i n_j}{4}\right), $$

with $P$ the Gutzwiller projector onto no-double-occupancy. **Doping a Mott insulator** — adding holes to the antiferromagnetic parent — is the route to the high-$T_c$ cuprate superconductors (Module 5.9): the t–J model is the leading candidate effective theory for them. At intermediate $U/W$ neither solvable limit applies, and quantitative results require DMFT and large-scale numerics. The Hubbard/t–J models thus connect tight-binding bands (Module 4.4), the Heisenberg magnet (Module 4.6), exactly solvable models (Module 6.7), and high-temperature superconductivity (Module 5.9).

**应用——t–J 模型与高温超导。** 偏离半填充时，大 $U$ 哈伯德模型投影到 **t–J 模型**：跃迁被限制在*无*双占据的子空间内（受约束的动能项 $t$），并补充近邻自旋间的超交换 $J\,\mathbf{S}_i\cdot\mathbf{S}_j$，

$$ H_{t\text{–}J} = -t \sum_{\langle ij\rangle,\sigma} P\,(c^\dagger_{i\sigma} c_{j\sigma} + \text{h.c.})\,P + J \sum_{\langle ij\rangle} \left(\mathbf{S}_i \cdot \mathbf{S}_j - \frac{n_i n_j}{4}\right), $$

其中 $P$ 是投影到无双占据的 Gutzwiller 投影算符。**掺杂莫特绝缘体**——向反铁磁母体中加入空穴——是通往高温铜氧化物超导体的途径（模块 5.9）：t–J 模型是它们最主要的候选有效理论。在中等 $U/W$ 下两个可解极限都不适用，定量结果需要 DMFT 与大规模数值。因此哈伯德 / t–J 模型连接了紧束缚能带（模块 4.4）、海森堡磁体（模块 4.6）、精确可解模型（模块 6.7）与高温超导（模块 5.9）。

---

**Self-test (blank page)**

1. Write down the Hubbard Hamiltonian and identify each term physically. What sets the bandwidth $W$, and what is the role of $U$?
2. Solve the two limits $U = 0$ and $t = 0$. What are the single-site energies in the atomic limit, and why is the band metallic at $U = 0$ and half-filling?
3. Explain why a half-filled Hubbard model becomes an insulator at large $U$. Estimate the Mott gap and contrast a Mott insulator with a band insulator.
4. Derive (at least sketch) why superexchange gives an *antiferromagnetic* Heisenberg coupling $J = 4t^2/U$, and explain the role of the Pauli principle.

**自测（空白页）**

1. 写出哈伯德哈密顿量并从物理上说明每一项。带宽 $W$ 由什么决定，$U$ 的作用是什么？
2. 求解 $U = 0$ 与 $t = 0$ 两个极限。原子极限下单格点能量是多少，为何在 $U = 0$ 半填充时能带是金属性的？
3. 解释为何半填充哈伯德模型在大 $U$ 下变为绝缘体。估计莫特能隙并对比莫特绝缘体与能带绝缘体。
4. 推导（至少勾勒）为何超交换给出*反铁磁*海森堡耦合 $J = 4t^2/U$，并说明泡利原理的作用。

---

← Previous: [Module 4.11 — Linear Response & Transport](./module-4.11-linear-response-and-transport.md) · [Phase 4 index](./README.md)

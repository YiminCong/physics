# Module 4.9 — Topological Matter & Berry Phase
**模块 4.9 — 拓扑物质与贝里相位**

> **Phase 4 — [Condensed Matter / Solid State](./README.md)** · Format: Definition → Demonstration → Application
> **第 4 阶段 — 凝聚态 / 固体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-4.9-derivations.md)

---

## 1. The Berry Phase · 贝里相位

**Definition.** Consider a quantum state $|\psi(t)\rangle$ that evolves under a Hamiltonian $H(\mathbf{R}(t))$ as the parameter $\mathbf{R}$ is slowly (adiabatically) varied around a closed loop in parameter space. By the **adiabatic theorem**, the system stays in the instantaneous eigenstate $|u(\mathbf{R})\rangle$ of $H(\mathbf{R})$, acquiring a dynamical phase $-(i/\hbar)\int E\,dt$ and an additional **geometric (Berry) phase**:

**定义。** 考虑在参数 $\mathbf{R}$ 缓慢（绝热地）沿参数空间中的闭合回路变化时，量子态 $|\psi(t)\rangle$ 在哈密顿量 $H(\mathbf{R}(t))$ 下演化。由**绝热定理**，系统保持在 $H(\mathbf{R})$ 的瞬时本征态 $|u(\mathbf{R})\rangle$ 中，获得动力学相位 $-(i/\hbar)\int E\,dt$ 和额外的**几何（贝里）相位**：

$$ \gamma = \oint \mathbf{A}(\mathbf{R}) \cdot d\mathbf{R}, \qquad \text{where } \mathbf{A}(\mathbf{R}) = i\langle u(\mathbf{R})|\nabla_{\mathbf{R}}|u(\mathbf{R})\rangle $$

is the **Berry connection** (a vector in parameter space). The Berry phase $\gamma$ is real (since $\langle u|\nabla u\rangle$ is pure imaginary by the normalisation condition $\langle u|u\rangle = 1$), gauge-covariant under $U(1)$ rephasing of $|u\rangle$, and — unlike the dynamical phase — depends only on the geometry of the path.

是**贝里联络**（参数空间中的矢量）。贝里相位 $\gamma$ 是实数（因为由归一化条件 $\langle u|u\rangle = 1$，$\langle u|\nabla u\rangle$ 是纯虚数），在 $|u\rangle$ 的 $U(1)$ 重新定相下协变，且与动力学相位不同——仅依赖于路径的几何形状。

**Demonstration.** In a crystalline solid, the Bloch Hamiltonian $H(\mathbf{k})$ acts on periodic parts $|u_n(\mathbf{k})\rangle$ of Bloch states. The **Berry curvature** (the field-strength of the Berry connection in $\mathbf{k}$-space) is

**演示。** 在晶态固体中，布洛赫哈密顿量 $H(\mathbf{k})$ 作用于布洛赫态的周期部分 $|u_n(\mathbf{k})\rangle$。**贝里曲率**（$\mathbf{k}$ 空间中贝里联络的场强）为

$$ \Omega_n(\mathbf{k}) = \nabla_{\mathbf{k}} \times \mathbf{A}_n(\mathbf{k}) = i\left(\langle \partial_{k_x} u_n| \partial_{k_y} u_n\rangle - \langle \partial_{k_y} u_n| \partial_{k_x} u_n\rangle\right) \quad \text{(in 2D)} $$

The integral of the Berry curvature over the Brillouin zone (BZ) for a filled band n is quantized — it is the **Chern number** (a topological integer):

贝里曲率在填充能带 $n$ 的布里渊区（BZ）上的积分是量子化的——它是**陈数**（拓扑整数）：

$$ C_n = \frac{1}{2\pi} \int_{\text{BZ}} \Omega_n(\mathbf{k})\, d^2k \in \mathbb{Z}. $$

The quantization of $C_n$ is the deep mathematical fact underlying the IQHE (Module 4.8): $\sigma_{xy} = (e^2/h) \sum_n C_n$.

$C_n$ 的量子化是 IQHE（模块 4.8）背后深刻的数学事实：$\sigma_{xy} = (e^2/h) \sum_n C_n$。

**Application.** The Berry phase also explains the **anomalous Hall effect** (a Hall effect in ferromagnets with zero applied B), **Bloch oscillations**, and **adiabatic pumping**. In 1D, the Zak phase $\gamma = \oint A\,dk$ over the full BZ can take values $0$ or $\pi$ and classifies 1D band insulators — directly realised in the SSH model below. The Berry phase is not merely abstract: it has been measured via interference experiments in molecular systems (Aharonov–Bohm), condensed-matter (Josephson junctions), and cold-atom platforms.

**应用。** 贝里相位还解释了**反常霍尔效应**（铁磁体中无外加 B 的霍尔效应）、**布洛赫振荡**和**绝热泵浦**。在一维中，整个 BZ 上的扎克相位 $\gamma = \oint A\,dk$ 可取值 $0$ 或 $\pi$，对一维能带绝缘体分类——在下面的 SSH 模型中直接实现。贝里相位不仅是抽象的：它已通过分子系统（阿哈罗诺夫–玻姆）、凝聚态（约瑟夫森结）和冷原子平台中的干涉实验得到测量。

---

## 2. Topological Insulators · 拓扑绝缘体

**Definition.** A **topological insulator** (TI) is a material that is insulating in the bulk (a non-zero gap) but hosts **topologically protected conducting states** on its surfaces or edges. The surface/edge states cannot be removed by any adiabatic deformation of the Hamiltonian that does not close the bulk gap — they are topologically robust against disorder and perturbations that preserve the relevant symmetry.

**定义。** **拓扑绝缘体**（TI）是一种体内绝缘（带隙非零）但其表面或边缘承载**拓扑保护导电态**的材料。边缘/表面态无法通过任何不关闭体带隙的哈密顿量绝热形变来消除——它们对保持相关对称性的无序和扰动具有拓扑鲁棒性。

**Demonstration: the SSH model.** The **Su–Schrieffer–Heeger (SSH) model** is the simplest 1D topological insulator. It describes a chain of sites with alternating hopping amplitudes $t_1$ (intracell) and $t_2$ (intercell):

**演示：SSH 模型。** **Su–Schrieffer–Heeger（SSH）模型**是最简单的一维拓扑绝缘体。它描述了具有交替跳跃振幅 $t_1$（胞内）和 $t_2$（胞间）的格点链：

$$ H(k) = (t_1 + t_2 \cos k)\,\sigma_x + t_2 \sin k\,\sigma_y $$

where $\sigma_{x,y}$ are Pauli matrices acting on the two sublattice sites per unit cell. The bulk bands are $E_\pm(k) = \pm\sqrt{t_1^2 + t_2^2 + 2 t_1 t_2 \cos k}$, with a gap when $t_1 \neq t_2$.

其中 $\sigma_{x,y}$ 是作用于每个单元中两个子格位点的泡利矩阵。体带为 $E_\pm(k) = \pm\sqrt{t_1^2 + t_2^2 + 2 t_1 t_2 \cos k}$，当 $t_1 \neq t_2$ 时有带隙。

The **winding number** (a $\mathbb{Z}$ topological invariant) of the SSH model is

SSH 模型的**缠绕数**（一个 $\mathbb{Z}$ 拓扑不变量）为

$$ w = \frac{1}{2\pi} \oint dk\; \frac{d}{dk}\left[\arg(t_1 + t_2 e^{ik})\right] = \begin{cases} 0 & \text{if } |t_1| > |t_2| \text{ (trivial)}, \\ 1 & \text{if } |t_2| > |t_1| \text{ (topological)}. \end{cases} $$

In the topological phase ($w = 1$), a finite chain hosts exactly two **zero-energy edge modes**, one at each end, that are exponentially localized at the boundary. These are protected as long as chiral symmetry (the symmetry $\sigma_z H(k) \sigma_z = -H(k)$) is preserved.

在拓扑相（$w = 1$）中，有限链恰好承载两个**零能边缘模式**，每端一个，在边界处指数局域。只要手征对称性（$\sigma_z H(k) \sigma_z = -H(k)$）保持，它们就受到保护。

**Application.** In 2D, time-reversal symmetry (for electrons, with $T^2 = -1$) allows a $\mathbb{Z}_2$ topological invariant $\nu \in \{0, 1\}$. The **quantum spin Hall (QSH) insulator** ($\nu = 1$) has a bulk gap but counter-propagating helical edge states — spin-up electrons moving right and spin-down electrons moving left (or vice versa). Back-scattering is forbidden by time-reversal symmetry: a time-reversed partner state always propagates in the opposite direction with opposite spin, and overlapping them would require a spin flip that time-reversal-symmetric disorder cannot provide. HgTe/CdTe quantum wells (König et al., 2007) were the first experimental realization.

**应用。** 在二维中，时间反演对称性（对于电子，$T^2 = -1$）允许一个 $\mathbb{Z}_2$ 拓扑不变量 $\nu \in \{0, 1\}$。**量子自旋霍尔（QSH）绝缘体**（$\nu = 1$）具有体带隙但有反向传播的螺旋边缘态——自旋向上的电子向右运动，自旋向下的电子向左运动（反之亦然）。时间反演对称性禁止背向散射：时间反演伴侣态总是沿相反方向传播且自旋相反，将它们叠加需要自旋翻转，而保持时间反演对称性的无序无法提供这一翻转。HgTe/CdTe 量子阱（König 等，2007 年）是首个实验实现。

In 3D the $\mathbb{Z}_2$ classification gives four invariants $(\nu_0; \nu_1\nu_2\nu_3)$: when $\nu_0 = 1$ the material is a **strong topological insulator** with an odd number of Dirac cones on each surface. $\text{Bi}_2\text{Se}_3$ and $\text{Bi}_2\text{Te}_3$ are canonical strong 3D TIs with a single Dirac cone on the surface, first observed by ARPES. The bulk–boundary correspondence — a topological invariant in the bulk implies protected boundary states — is the unifying principle of the entire field of topological matter, connecting the QHE (Module 4.8), TIs, Weyl semimetals, and topological superconductors.

在三维中，$\mathbb{Z}_2$ 分类给出四个不变量（$\nu_0$；$\nu_1\nu_2\nu_3$）：当 $\nu_0 = 1$ 时，材料是**强拓扑绝缘体**，每个表面上有奇数个狄拉克锥。$\text{Bi}_2\text{Se}_3$ 和 $\text{Bi}_2\text{Te}_3$ 是典型的强三维拓扑绝缘体，每个表面上有单个狄拉克锥，首先由 ARPES 观测到。**体–边界对应**——体内的拓扑不变量意味着受保护的边界态——是整个拓扑物质领域的统一原理，将量子霍尔效应（模块 4.8）、拓扑绝缘体、外尔半金属和拓扑超导体联系起来。

---

**Self-test (blank page)**

1. Define the Berry connection $\mathbf{A}(\mathbf{k})$ and Berry curvature $\Omega(\mathbf{k})$. What is the relationship between the Berry phase around a closed loop in $\mathbf{k}$-space and the Berry curvature?
2. State why the Chern number is an integer, and connect it to the IQHE Hall conductivity.
3. Write down the SSH Hamiltonian $H(k)$ and find the winding number in the two phases $|t_1| > |t_2|$ and $|t_2| > |t_1|$. What happens at the boundary between the two phases?
4. What is bulk–boundary correspondence? Illustrate with the SSH model.
5. Describe the helical edge states of a 2D $\mathbb{Z}_2$ topological insulator and explain why time-reversal symmetry forbids back-scattering.

**自测（空白页）**

1. 定义贝里联络 $\mathbf{A}(\mathbf{k})$ 和贝里曲率 $\Omega(\mathbf{k})$。$\mathbf{k}$ 空间中闭合回路上的贝里相位与贝里曲率有何关系？
2. 陈述陈数为何是整数，并将其与 IQHE 霍尔电导率联系起来。
3. 写出 SSH 哈密顿量 $H(k)$，求两相 $|t_1| > |t_2|$ 和 $|t_2| > |t_1|$ 中的缠绕数。两相边界处发生了什么？
4. 什么是体–边界对应？用 SSH 模型说明。
5. 描述二维 $\mathbb{Z}_2$ 拓扑绝缘体的螺旋边缘态，并解释为何时间反演对称性禁止背向散射。

---

← Previous: [Module 4.8 — Quantum Hall Effect](./module-4.8-quantum-hall-effect.md) · [Phase 4 index](./README.md) · Next: [Module 4.10 — Landau Fermi-Liquid Theory](./module-4.10-landau-fermi-liquid-theory.md) →

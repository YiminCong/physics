# Module 5.10 — Bogoliubov–de Gennes & Andreev Reflection
**模块 5.10 — Bogoliubov–de Gennes 方程与安德烈耶夫反射**

> **Phase 5 — [Superconductivity](./README.md)** · Format: Definition → Demonstration → Application
> **第 5 阶段 — 超导 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-5.10-bogoliubov-de-gennes-and-andreev-reflection-derivations.md)

---

## 1. The Bogoliubov–de Gennes Equations · Bogoliubov–de Gennes 方程

**Definition.** The **Bogoliubov–de Gennes (BdG) equations** are the real-space, mean-field equations of motion for a superconductor that may be **inhomogeneous** — where $\Delta$, the order parameter, and the single-particle Hamiltonian both vary with position. They generalize BCS from a uniform bulk to heterostructures, vortex cores, interfaces, and topological systems.

Working in **Nambu (particle–hole) space**, one doubles the degrees of freedom by grouping the electron field $\psi_\uparrow(\mathbf{r})$ together with the time-reversed hole field $\psi_\downarrow^\dagger(\mathbf{r})$ into a two-component spinor. The Nambu Hamiltonian (BdG Hamiltonian) takes the form

$$ H_\text{BdG} = \begin{pmatrix} H_0(\mathbf{r}) & \Delta(\mathbf{r}) \\ \Delta^*(\mathbf{r}) & -H_0^*(\mathbf{r}) \end{pmatrix}, $$

where $H_0(\mathbf{r}) = -\hbar^2\nabla^2/2m + U(\mathbf{r}) - \mu$ is the single-particle kinetic + potential energy measured from the chemical potential $\mu$, and $\Delta(\mathbf{r})$ is the **pair potential** (gap). The eigenvalue problem $H_\text{BdG}\,(u(\mathbf{r}), v(\mathbf{r}))^\mathsf{T} = E\,(u(\mathbf{r}), v(\mathbf{r}))^\mathsf{T}$ yields **quasiparticle amplitudes** $u(\mathbf{r})$ (particle-like) and $v(\mathbf{r})$ (hole-like) at energy $E$, with the **self-consistency condition** $\Delta(\mathbf{r}) = g \sum_n u_n(\mathbf{r}) v_n^*(\mathbf{r}) \tanh(E_n/2k_B T)$, where the sum runs over all positive-energy quasiparticle states and $g$ is the pairing strength.

**定义。** **Bogoliubov–de Gennes（BdG）方程**是适用于**非均匀**超导体的实空间平均场运动方程——其中序参量 $\Delta$ 和单粒子哈密顿量均随位置变化。它将 BCS 从均匀体相推广到异质结、涡旋核心、界面和拓扑体系。

在 **Nambu（粒子-空穴）空间**中，将电子场 $\psi_\uparrow(\mathbf{r})$ 与时间反演空穴场 $\psi_\downarrow^\dagger(\mathbf{r})$ 组合成二分量旋量，使自由度加倍。Nambu 哈密顿量（BdG 哈密顿量）的形式为

$$ H_\text{BdG} = \begin{pmatrix} H_0(\mathbf{r}) & \Delta(\mathbf{r}) \\ \Delta^*(\mathbf{r}) & -H_0^*(\mathbf{r}) \end{pmatrix}, $$

其中 $H_0(\mathbf{r}) = -\hbar^2\nabla^2/2m + U(\mathbf{r}) - \mu$ 是相对于化学势 $\mu$ 的单粒子动能加势能，$\Delta(\mathbf{r})$ 是**对势**（能隙）。本征值问题 $H_\text{BdG}\,(u(\mathbf{r}), v(\mathbf{r}))^\mathsf{T} = E\,(u(\mathbf{r}), v(\mathbf{r}))^\mathsf{T}$ 给出能量 $E$ 处的**准粒子振幅** $u(\mathbf{r})$（粒子型）和 $v(\mathbf{r})$（空穴型），以及**自洽条件** $\Delta(\mathbf{r}) = g \sum_n u_n(\mathbf{r}) v_n^*(\mathbf{r}) \tanh(E_n/2k_B T)$，求和遍历所有正能准粒子态，$g$ 为配对强度。

**Demonstration.** At uniform $\Delta$ and $U = 0$, the BdG equations reduce to the standard BCS Bogoliubov transformation: the plane-wave solutions give the familiar BCS quasiparticle spectrum $E_k = \sqrt{\xi_k^2 + \Delta^2}$ with $\xi_k = \hbar^2 k^2/2m - \mu$, and the coherence factors $u_k, v_k$ of BCS theory (Module 5.5). For a vortex, $\Delta(\mathbf{r})$ winds by $2\pi$ around the core and vanishes at $r = 0$; the BdG equations then predict **sub-gap bound states** inside the vortex core (Caroli–de Gennes–Matricon states), confirming the core is locally normal. This is the power of BdG: it gives the spatially resolved quasiparticle structure wherever $\Delta(\mathbf{r})$ is non-uniform.

**演示。** 在均匀 $\Delta$、$U = 0$ 的情况下，BdG 方程退化为标准 BCS Bogoliubov 变换：平面波解给出熟悉的 BCS 准粒子谱 $E_k = \sqrt{\xi_k^2 + \Delta^2}$，其中 $\xi_k = \hbar^2 k^2/2m - \mu$，以及 BCS 理论（模块 5.5）的相干因子 $u_k$、$v_k$。对于涡旋，$\Delta(\mathbf{r})$ 绕核心旋转 $2\pi$ 并在 $r = 0$ 处消失；BdG 方程预言涡旋核心内存在**亚能隙束缚态**（Caroli–de Gennes–Matricon 态），证实核心局域呈正常态。这正是 BdG 的优势：它在 $\Delta(\mathbf{r})$ 非均匀的任何地方都能给出空间分辨的准粒子结构。

**Application.** The BdG framework is the starting point for calculating **proximity effects**, Andreev bound states, Josephson currents through junctions, vortex-core spectroscopy (scanning tunneling microscopy), and — crucially for Module 5.11 — the emergence of Majorana zero modes at the ends of topological superconducting wires.

**应用。** BdG 框架是计算**近邻效应**、安德烈耶夫束缚态、通过结的约瑟夫森电流、涡旋核心谱（扫描隧道显微镜）的出发点，以及——对模块 5.11 至关重要的——拓扑超导线两端马约拉纳零模的涌现。

---

## 2. Andreev Reflection & the Proximity Effect · 安德烈耶夫反射与近邻效应

**Definition.** At a clean **normal-metal / superconductor (N–S) interface**, an electron incident from the normal side with energy $E < \Delta$ (below the gap) **cannot** propagate as a quasiparticle into the superconductor, because there are no available quasiparticle states. Instead it undergoes **Andreev reflection**: it is reflected back as a **hole** that retraces the electron's exact path (retro-reflection), while a Cooper pair is transmitted into the condensate, transferring charge **$2e$** to the superconductor. The reflected hole has the opposite charge and (in the retro-reflection limit) the opposite velocity to the incoming electron, so the hole literally reverses along the electron trajectory.

**Andreev bound states** form when an electron and hole bounce repeatedly between two N–S interfaces (or between two superconducting interfaces, as in an SNS junction), with each Andreev reflection converting one into the other. The quantization condition for bound states gives discrete sub-gap levels at energies $\pm E_A = \pm\Delta \cos(\phi/2)$ for a perfect SNS junction of zero length, where $\phi$ is the phase difference — this is the microscopic origin of the **Josephson current**.

The **proximity effect** is the spatial version: a superconductor induces finite pair correlations $\langle\psi_\uparrow\psi_\downarrow\rangle \neq 0$ into an adjacent normal metal over a length scale $\xi_N = \hbar v_F / 2\pi k_B T$ (clean limit) or $\xi_N = \sqrt{\hbar D/2\pi k_B T}$ (dirty limit, $D$ = diffusion constant). Beyond $\xi_N$ the induced correlations decay exponentially.

**定义。** 在洁净的**正常金属/超导体（N–S）界面**，从正常侧入射的能量 $E < \Delta$（低于能隙）的电子**无法**作为准粒子传播进超导体，因为没有可用的准粒子态。取而代之的是**安德烈耶夫反射**：电子被反射为一个**空穴**，该空穴沿电子的原路返回（逆向反射），同时一个库珀对被传输进凝聚体，向超导体转移电荷 **$2e$**。反射空穴的电荷相反，且（在逆向反射极限下）速度与入射电子相反，因此空穴确实沿电子轨迹反向传播。

**安德烈耶夫束缚态**在电子和空穴在两个 N–S 界面（或两个超导界面，如 SNS 结）之间反复弹跳时形成，每次安德烈耶夫反射将一种粒子转变为另一种。对于零长度的完美 SNS 结，束缚态的量子化条件给出离散的亚能隙能级 $\pm E_A = \pm\Delta \cos(\phi/2)$，其中 $\phi$ 是相位差——这是**约瑟夫森电流**的微观起源。

**近邻效应**是空间版本：超导体在相邻正常金属中诱导出有限的对关联 $\langle\psi_\uparrow\psi_\downarrow\rangle \neq 0$，其长度尺度为 $\xi_N = \hbar v_F / 2\pi k_B T$（洁净极限）或 $\xi_N = \sqrt{\hbar D/2\pi k_B T}$（脏极限，$D$ 为扩散常数）。超出 $\xi_N$ 后，诱导的关联指数衰减。

**Demonstration.** The hallmark of Andreev reflection is a **doubled sub-gap conductance**: at a transparent N–S interface each incident electron is Andreev-reflected as a hole, so two electron charges are transferred per scattering event, doubling the normal-state conductance for $|E| < \Delta$. This doubled conductance (and its suppression by a barrier) is the BTK (Blonder–Tinkham–Klapwijk) result, verified in countless point-contact experiments. In STM measurements on proximity-coupled metals, an induced gap appears in the local density of states, decaying with distance from the S layer over $\xi_N$.

**演示。** 安德烈耶夫反射的标志是**亚能隙电导加倍**：在透明 N–S 界面，每个入射电子被安德烈耶夫反射为一个空穴，每次散射事件转移两个电子电荷，使 $|E| < \Delta$ 时的正常态电导加倍。这种加倍电导（及其被势垒抑制的效应）即 BTK（Blonder–Tinkham–Klapwijk）结果，已在无数点接触实验中得到验证。在对超导体近邻耦合金属的 STM 测量中，局域态密度中出现诱导能隙，随距 S 层距离增加按 $\xi_N$ 指数衰减。

**Application.** Andreev reflection underpins **Andreev interferometry** (phase-sensitive probes of pairing), the operation of **superconducting proximity qubits**, and the formation of **topological Andreev bound states** (Module 5.11). The proximity effect is exploited in **superconducting spintronics** (inducing triplet pairing via magnetic interfaces) and in engineering the effective p-wave pairing needed for Majorana modes.

**应用。** 安德烈耶夫反射支撑了**安德烈耶夫干涉测量**（配对的相敏探测）、**超导近邻量子比特**的工作原理，以及**拓扑安德烈耶夫束缚态**的形成（模块 5.11）。近邻效应被应用于**超导自旋电子学**（通过磁性界面诱导三重态配对）以及工程化马约拉纳模所需的有效 p 波配对。

---

**Self-test (blank page)**

1. Write down the BdG Hamiltonian in Nambu space and identify each block. What is the self-consistency condition on $\Delta(\mathbf{r})$?
2. Explain why an electron with $E < \Delta$ incident on a clean N–S interface cannot enter the superconductor as a quasiparticle, and describe what happens instead (Andreev reflection).
3. What is retro-reflection, and how does it differ from ordinary specular reflection?
4. Derive the energy of an Andreev bound state in a short SNS junction and connect it to the Josephson current.
5. State the proximity-effect decay length $\xi_N$ in the clean limit and explain its temperature dependence.

**自测（空白页）**

1. 写出 Nambu 空间中的 BdG 哈密顿量并指出每个分块。$\Delta(\mathbf{r})$ 的自洽条件是什么？
2. 解释为何能量 $E < \Delta$ 的电子入射到洁净 N–S 界面时无法作为准粒子进入超导体，并描述替代过程（安德烈耶夫反射）。
3. 什么是逆向反射？它与普通镜面反射有何不同？
4. 推导短 SNS 结中安德烈耶夫束缚态的能量，并将其与约瑟夫森电流联系起来。
5. 陈述洁净极限下近邻效应衰减长度 $\xi_N$，并解释其温度依赖性。

---

← Previous: [Module 5.9 — Unconventional & High-Tᶜ Superconductors](./module-5.9-unconventional-and-high-tc-superconductors.md) · [Phase 5 index](./README.md) · Next: [Module 5.11 — Topological Superconductivity & Majorana Modes](./module-5.11-topological-superconductivity-and-majorana.md) →

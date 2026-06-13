# Module 6.1 — Second Quantization & the Many-Body Problem ⭐
**模块 6.1 — 二次量子化与多体问题 ⭐**

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 6 阶段 — 量子场论与多体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-6.1-second-quantization-derivations.md)

---

## 1. Creation, Annihilation, and Field Operators · 产生、湮灭与场算符

**Definition.** Second quantization (introduced in Module 3.12) re-expresses quantum mechanics in occupation-number (Fock) space, where the fundamental objects are creation and annihilation operators rather than many-particle wave functions. For bosons, $[a_k, a^\dagger_{k'}] = \delta_{kk'}$; for fermions, $\{c_k, c^\dagger_{k'}\} = \delta_{kk'}$ with $\{c_k, c_{k'}\} = 0$ (Pauli exclusion built in algebraically). A state with $n_1$ particles in mode 1, $n_2$ in mode 2, … is written $|n_1, n_2, \ldots\rangle$ — the Fock state. The full Fock space $\mathcal{F} = \bigoplus_{N=0}^\infty \mathcal{H}_N$ accommodates any particle number.

**定义。** 二次量子化（模块 3.12 中引入）将量子力学重新表述于粒子数（Fock）空间中，其基本对象是产生和湮灭算符，而非多粒子波函数。对于玻色子，$[a_k, a^\dagger_{k'}] = \delta_{kk'}$；对于费米子，$\{c_k, c^\dagger_{k'}\} = \delta_{kk'}$ 且 $\{c_k, c_{k'}\} = 0$（泡利不相容原理以代数方式内嵌）。模式 1 中有 $n_1$ 个粒子、模式 2 中有 $n_2$ 个粒子……的态写作 $|n_1, n_2, \ldots\rangle$——即 Fock 态。完整的 Fock 空间 $\mathcal{F} = \bigoplus_{N=0}^\infty \mathcal{H}_N$ 可容纳任意粒子数。

**Field operators** assemble the mode operators into a position-space object: $\psi(x) = \sum_k \varphi_k(x)\, c_k$, where $\varphi_k(x)$ are single-particle orbitals. $\psi^\dagger(x)$ creates a particle at $x$; $\psi(x)$ destroys one. Their (anti)commutators inherit from the mode operators: $\{\psi(x), \psi^\dagger(x')\} = \delta(x - x')$ for fermions.

**场算符**将模式算符组合成位置空间的对象：$\psi(x) = \sum_k \varphi_k(x)\, c_k$，其中 $\varphi_k(x)$ 为单粒子轨道。$\psi^\dagger(x)$ 在 $x$ 处产生一个粒子；$\psi(x)$ 湮灭一个。它们的（反）对易子继承自模式算符：对费米子，$\{\psi(x), \psi^\dagger(x')\} = \delta(x - x')$。

**Demonstration.** A generic one-body Hamiltonian $H_1 = \sum_{ij} t_{ij}\, c^\dagger_i c_j$, or in field form $H_1 = \int dx\, \psi^\dagger(x) \left[-\hbar^2\nabla^2/2m + V(x)\right] \psi(x)$. A two-body interaction (e.g., Coulomb) becomes $H_2 = \tfrac12 \int dx\, dx'\, \psi^\dagger(x)\, \psi^\dagger(x')\, U(x-x')\, \psi(x')\, \psi(x)$. No symmetrization is needed by hand: operator ordering plus (anti)commutation relations enforce it automatically. For $N \sim 10^{23}$ particles, writing an antisymmetrized $N$-particle wave function is computationally hopeless; the Fock-space formalism converts the problem to algebra on a manageable operator algebra.

**演示。** 一般单体哈密顿量 $H_1 = \sum_{ij} t_{ij}\, c^\dagger_i c_j$，或以场的形式写作 $H_1 = \int dx\, \psi^\dagger(x) \left[-\hbar^2\nabla^2/2m + V(x)\right] \psi(x)$。两体相互作用（如库仑）变为 $H_2 = \tfrac12 \int dx\, dx'\, \psi^\dagger(x)\, \psi^\dagger(x')\, U(x-x')\, \psi(x')\, \psi(x)$。无需手动对称化：算符排序加（反）对易关系自动强制执行。对于 $N \sim 10^{23}$ 个粒子，写出反对称化的 $N$ 粒子波函数在计算上毫无希望；Fock 空间形式主义将问题转化为可处理的算符代数。

**Application.** Every subsequent module in Phase 6 is written in this language. The BCS Hamiltonian (Module 5.5) $H_\text{BCS} = \sum_k \xi_k (c^\dagger_{k\uparrow}c_{k\uparrow} + c^\dagger_{-k\downarrow}c_{-k\downarrow}) - \sum_{kk'} V_{kk'}\, c^\dagger_{k\uparrow}c^\dagger_{-k\downarrow}c_{-k'\downarrow}c_{k'\uparrow}$ is second-quantized from the start: the pairing correlator $\langle c_{-k\downarrow}c_{k\uparrow}\rangle \neq 0$ signals the condensate. The formalism is also the starting point for Green's functions (Module 6.2) and Feynman diagrams (Module 6.3).

**应用。** 第 6 阶段后续每个模块都用这种语言书写。BCS 哈密顿量（模块 5.5）$H_\text{BCS} = \sum_k \xi_k (c^\dagger_{k\uparrow}c_{k\uparrow} + c^\dagger_{-k\downarrow}c_{-k\downarrow}) - \sum_{kk'} V_{kk'}\, c^\dagger_{k\uparrow}c^\dagger_{-k\downarrow}c_{-k'\downarrow}c_{k'\uparrow}$ 从一开始就是二次量子化的：配对关联子 $\langle c_{-k\downarrow}c_{k\uparrow}\rangle \neq 0$ 标志着凝聚体的出现。该形式主义也是格林函数（模块 6.2）和费曼图（模块 6.3）的出发点。

---

## 2. Why Fock Space is the Only Sane Bookkeeping · 为何 Fock 空间是唯一合理的记账方式

**Definition.** At fixed $N$, an $N$-boson or $N$-fermion wave function lives in the symmetrized or antisymmetrized tensor product of $N$ single-particle Hilbert spaces. For $N = 10^{23}$ this object has an astronomical number of degrees of freedom and cannot be written down. Fock space instead labels states by occupation numbers $\{n_k\}$, which are integers (bosons) or 0/1 (fermions). The entire physics is encoded in how operators act on these labels.

**定义。** 在固定 $N$ 的情况下，$N$ 个玻色子或 $N$ 个费米子的波函数存在于 $N$ 个单粒子希尔伯特空间的对称化或反对称化张量积中。对于 $N = 10^{23}$，该对象具有天文数字量级的自由度，无法写下。Fock 空间转而用占据数 $\{n_k\}$ 标记态，这些数对玻色子为整数，对费米子为 0/1。全部物理编码在算符如何作用于这些标记之中。

**Demonstration.** The number operator $\hat{N} = \sum_k c^\dagger_k c_k$ commutes with any number-conserving Hamiltonian, so energy eigenstates carry a good quantum number $N$. When particle number is not conserved — open systems, superconductors, relativistic QFT — Fock space allows superpositions of different $N$, essential for describing the BCS ground state $|\text{BCS}\rangle = \prod_k (u_k + v_k c^\dagger_{k\uparrow}c^\dagger_{-k\downarrow})|0\rangle$ which is a superposition of states with $0, 2, 4, \ldots$ Cooper pairs.

**演示。** 粒子数算符 $\hat{N} = \sum_k c^\dagger_k c_k$ 与任何粒子数守恒哈密顿量对易，因此能量本征态携带好量子数 $N$。当粒子数不守恒时——开放系统、超导体、相对论 QFT——Fock 空间允许不同 $N$ 的叠加，这对于描述 BCS 基态 $|\text{BCS}\rangle = \prod_k (u_k + v_k c^\dagger_{k\uparrow}c^\dagger_{-k\downarrow})|0\rangle$ 至关重要，该态是含有 $0$、$2$、$4$、$\ldots$ 个库珀对的态的叠加。

**Application.** Fock space is the universal arena: non-relativistic condensed matter (Phases 4–5), relativistic QFT (Module 6.5 and Phase 8), and finite-temperature field theory (Module 6.4). Coleman "Introduction to Many-Body Physics" and Fetter & Walecka "Quantum Theory of Many-Particle Systems" both open with this formalism for exactly this reason.

**应用。** Fock 空间是普遍的舞台：非相对论凝聚态（第 4–5 阶段）、相对论 QFT（模块 6.5 和第 8 阶段）以及有限温度场论（模块 6.4）。Coleman 的 "Introduction to Many-Body Physics" 和 Fetter & Walecka 的 "Quantum Theory of Many-Particle Systems" 都以这一形式主义开篇，原因正在于此。

## Key results · 核心结果

- Field operator $\hat\psi(x) = \sum_k a_k\,\phi_k(x)$ creates/destroys particles at a point · 场算符
- $[a_k, a^\dagger_{k'}] = \delta_{kk'}$ (bosons) / $\{c_k, c^\dagger_{k'}\} = \delta_{kk'}$ (fermions) · 玻色／费米(反)对易关系
- Fock space handles variable particle number naturally · Fock 空间处理可变粒子数
- One- and two-body operators rewrite cleanly in $a^\dagger, a$ — the language of many-body physics · 多体算符的统一语言

---

## Self-test (blank page) · 自测（空白页）

1. Write the anticommutation relations for fermionic field operators $\psi(x)$ and $\psi^\dagger(x')$. Derive them from the mode-operator anticommutators $\{c_k, c^\dagger_{k'}\} = \delta_{kk'}$.
2. Express the kinetic-energy operator $T = \sum_i p^2_i/2m$ in second-quantized form using field operators in momentum space. What does the occupation-number state $|n_{k_1}, n_{k_2}, \ldots\rangle$ represent physically?
3. Why does the BCS ground state require Fock space (rather than fixed-$N$ Hilbert space) for its natural description?

**自测（空白页）**

1. 写出费米子场算符 $\psi(x)$ 和 $\psi^\dagger(x')$ 的反对易关系。从模式算符反对易子 $\{c_k, c^\dagger_{k'}\} = \delta_{kk'}$ 推导它们。
2. 用动量空间中的场算符将动能算符 $T = \sum_i p^2_i/2m$ 表达为二次量子化形式。粒子数态 $|n_{k_1}, n_{k_2}, \ldots\rangle$ 在物理上代表什么？
3. 为什么 BCS 基态的自然描述需要 Fock 空间（而非固定 $N$ 的希尔伯特空间）？

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** With $\psi(x)=\sum_k c_k\varphi_k(x)$, $\{\psi(x),\psi^\dagger(x')\}=\sum_{kk'}\varphi_k(x)\varphi^*_{k'}(x')\{c_k,c^\dagger_{k'}\}=\sum_k\varphi_k(x)\varphi^*_k(x')=\delta(x-x')$ by completeness. · 由模式反对易子与完备性得 $\{\psi(x),\psi^\dagger(x')\}=\delta(x-x')$。

**2.** $T=\sum_k\dfrac{\hbar^2k^2}{2m}c^\dagger_k c_k$. The state $|n_{k_1},n_{k_2},\dots\rangle$ specifies how many particles occupy each mode — the occupation-number (Fock) representation. · $T=\sum_k\tfrac{\hbar^2k^2}{2m}c^\dagger_kc_k$;占据数态记录各模式粒子数。

**3.** The BCS ground state $|\text{BCS}\rangle=\prod_k(u_k+v_k c^\dagger_{k\uparrow}c^\dagger_{-k\downarrow})|0\rangle$ is a superposition of different particle numbers — not an eigenstate of $\hat N$ — so it lives naturally only in Fock space, not a fixed-$N$ Hilbert space. · BCS 基态是不同粒子数的叠加,需 Fock 空间。

</details>

---

← [Phase 6 index](./README.md) · Next: [Module 6.2 — Green's Functions & Propagators](./module-6.2-greens-functions.md) →

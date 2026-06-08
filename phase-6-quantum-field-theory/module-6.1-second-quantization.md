# Module 6.1 — Second Quantization & the Many-Body Problem ⭐
**模块 6.1 — 二次量子化与多体问题 ⭐**

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 6 阶段 — 量子场论与多体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-6.1-second-quantization-derivations.md)

---

## 1. Creation, Annihilation, and Field Operators · 产生、湮灭与场算符

**Definition.** Second quantization (introduced in Module 3.12) re-expresses quantum mechanics in occupation-number (Fock) space, where the fundamental objects are creation and annihilation operators rather than many-particle wave functions. For bosons, [a_k, a†_k'] = δ_{kk'}; for fermions, {c_k, c†_k'} = δ_{kk'} with {c_k, c_k'} = 0 (Pauli exclusion built in algebraically). A state with n_1 particles in mode 1, n_2 in mode 2, … is written |n_1, n_2, …⟩ — the Fock state. The full Fock space F = ⊕_{N=0}^∞ H_N accommodates any particle number.

**定义。** 二次量子化（模块 3.12 中引入）将量子力学重新表述于粒子数（Fock）空间中，其基本对象是产生和湮灭算符，而非多粒子波函数。对于玻色子，[a_k, a†_k'] = δ_{kk'}；对于费米子，{c_k, c†_k'} = δ_{kk'} 且 {c_k, c_k'} = 0（泡利不相容原理以代数方式内嵌）。模式 1 中有 n_1 个粒子、模式 2 中有 n_2 个粒子……的态写作 |n_1, n_2, …⟩——即 Fock 态。完整的 Fock 空间 F = ⊕_{N=0}^∞ H_N 可容纳任意粒子数。

**Field operators** assemble the mode operators into a position-space object: ψ(x) = Σ_k φ_k(x) c_k, where φ_k(x) are single-particle orbitals. ψ†(x) creates a particle at x; ψ(x) destroys one. Their (anti)commutators inherit from the mode operators: {ψ(x), ψ†(x')} = δ(x − x') for fermions.

**场算符**将模式算符组合成位置空间的对象：ψ(x) = Σ_k φ_k(x) c_k，其中 φ_k(x) 为单粒子轨道。ψ†(x) 在 x 处产生一个粒子；ψ(x) 湮灭一个。它们的（反）对易子继承自模式算符：对费米子，{ψ(x), ψ†(x')} = δ(x − x')。

**Demonstration.** A generic one-body Hamiltonian H₁ = Σ_{ij} t_{ij} c†_i c_j, or in field form H₁ = ∫ dx ψ†(x) [−ℏ²∇²/2m + V(x)] ψ(x). A two-body interaction (e.g., Coulomb) becomes H₂ = ½ ∫ dx dx' ψ†(x) ψ†(x') U(x−x') ψ(x') ψ(x). No symmetrization is needed by hand: operator ordering plus (anti)commutation relations enforce it automatically. For N ~ 10²³ particles, writing an antisymmetrized N-particle wave function is computationally hopeless; the Fock-space formalism converts the problem to algebra on a manageable operator algebra.

**演示。** 一般单体哈密顿量 H₁ = Σ_{ij} t_{ij} c†_i c_j，或以场的形式写作 H₁ = ∫ dx ψ†(x) [−ℏ²∇²/2m + V(x)] ψ(x)。两体相互作用（如库仑）变为 H₂ = ½ ∫ dx dx' ψ†(x) ψ†(x') U(x−x') ψ(x') ψ(x)。无需手动对称化：算符排序加（反）对易关系自动强制执行。对于 N ~ 10²³ 个粒子，写出反对称化的 N 粒子波函数在计算上毫无希望；Fock 空间形式主义将问题转化为可处理的算符代数。

**Application.** Every subsequent module in Phase 6 is written in this language. The BCS Hamiltonian (Module 5.5) H_BCS = Σ_k ξ_k (c†_{k↑}c_{k↑} + c†_{−k↓}c_{−k↓}) − Σ_{kk'} V_{kk'} c†_{k↑}c†_{−k↓}c_{−k'↓}c_{k'↑} is second-quantized from the start: the pairing correlator ⟨c_{−k↓}c_{k↑}⟩ ≠ 0 signals the condensate. The formalism is also the starting point for Green's functions (Module 6.2) and Feynman diagrams (Module 6.3).

**应用。** 第 6 阶段后续每个模块都用这种语言书写。BCS 哈密顿量（模块 5.5）H_BCS = Σ_k ξ_k (c†_{k↑}c_{k↑} + c†_{−k↓}c_{−k↓}) − Σ_{kk'} V_{kk'} c†_{k↑}c†_{−k↓}c_{−k'↓}c_{k'↑} 从一开始就是二次量子化的：配对关联子 ⟨c_{−k↓}c_{k↑}⟩ ≠ 0 标志着凝聚体的出现。该形式主义也是格林函数（模块 6.2）和费曼图（模块 6.3）的出发点。

---

## 2. Why Fock Space is the Only Sane Bookkeeping · 为何 Fock 空间是唯一合理的记账方式

**Definition.** At fixed N, an N-boson or N-fermion wave function lives in the symmetrized or antisymmetrized tensor product of N single-particle Hilbert spaces. For N = 10²³ this object has an astronomical number of degrees of freedom and cannot be written down. Fock space instead labels states by occupation numbers {n_k}, which are integers (bosons) or 0/1 (fermions). The entire physics is encoded in how operators act on these labels.

**定义。** 在固定 N 的情况下，N 个玻色子或 N 个费米子的波函数存在于 N 个单粒子希尔伯特空间的对称化或反对称化张量积中。对于 N = 10²³，该对象具有天文数字量级的自由度，无法写下。Fock 空间转而用占据数 {n_k} 标记态，这些数对玻色子为整数，对费米子为 0/1。全部物理编码在算符如何作用于这些标记之中。

**Demonstration.** The number operator N̂ = Σ_k c†_k c_k commutes with any number-conserving Hamiltonian, so energy eigenstates carry a good quantum number N. When particle number is not conserved — open systems, superconductors, relativistic QFT — Fock space allows superpositions of different N, essential for describing the BCS ground state |BCS⟩ = Π_k (u_k + v_k c†_{k↑}c†_{−k↓})|0⟩ which is a superposition of states with 0, 2, 4, … Cooper pairs.

**演示。** 粒子数算符 N̂ = Σ_k c†_k c_k 与任何粒子数守恒哈密顿量对易，因此能量本征态携带好量子数 N。当粒子数不守恒时——开放系统、超导体、相对论 QFT——Fock 空间允许不同 N 的叠加，这对于描述 BCS 基态 |BCS⟩ = Π_k (u_k + v_k c†_{k↑}c†_{−k↓})|0⟩ 至关重要，该态是含有 0、2、4、…… 个库珀对的态的叠加。

**Application.** Fock space is the universal arena: non-relativistic condensed matter (Phases 4–5), relativistic QFT (Module 6.5 and Phase 8), and finite-temperature field theory (Module 6.4). Coleman "Introduction to Many-Body Physics" and Fetter & Walecka "Quantum Theory of Many-Particle Systems" both open with this formalism for exactly this reason.

**应用。** Fock 空间是普遍的舞台：非相对论凝聚态（第 4–5 阶段）、相对论 QFT（模块 6.5 和第 8 阶段）以及有限温度场论（模块 6.4）。Coleman 的 "Introduction to Many-Body Physics" 和 Fetter & Walecka 的 "Quantum Theory of Many-Particle Systems" 都以这一形式主义开篇，原因正在于此。

---

## Self-test (blank page) · 自测（空白页）

1. Write the anticommutation relations for fermionic field operators ψ(x) and ψ†(x'). Derive them from the mode-operator anticommutators {c_k, c†_{k'}} = δ_{kk'}.
2. Express the kinetic-energy operator T = Σ_i p²_i/2m in second-quantized form using field operators in momentum space. What does the occupation-number state |n_{k₁}, n_{k₂}, …⟩ represent physically?
3. Why does the BCS ground state require Fock space (rather than fixed-N Hilbert space) for its natural description?

**自测（空白页）**

1. 写出费米子场算符 ψ(x) 和 ψ†(x') 的反对易关系。从模式算符反对易子 {c_k, c†_{k'}} = δ_{kk'} 推导它们。
2. 用动量空间中的场算符将动能算符 T = Σ_i p²_i/2m 表达为二次量子化形式。粒子数态 |n_{k₁}, n_{k₂}, …⟩ 在物理上代表什么？
3. 为什么 BCS 基态的自然描述需要 Fock 空间（而非固定 N 的希尔伯特空间）？

---

← [Phase 6 index](./README.md) · Next: [Module 6.2 — Green's Functions & Propagators](./module-6.2-greens-functions.md) →

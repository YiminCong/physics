# Module 3.12 — Symmetry, Identical Particles & Second Quantization ⭐⭐
**模块 3.12 — 对称性、全同粒子与二次量子化 ⭐⭐**

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 3 阶段 — 量子力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-3.12-derivations.md)

---

## 1. Discrete Symmetries · 离散对称性

**Definition.** Beyond continuous symmetries (Module 1.4), discrete ones matter: **parity** (spatial inversion) and **time reversal** classify states and constrain dynamics.

**定义。** 除连续对称性（模块 1.4）之外，离散对称性同样重要：**宇称**（空间反演）和**时间反演**对态进行分类并约束动力学。

## 2. Second Quantization — the key tool for what's ahead · 二次量子化——前方最重要的工具

**Definition.** Instead of tracking labeled particles, track **occupation numbers** of single-particle states. Introduce **creation/annihilation operators**: bosons $a_k^\dagger$, $a_k$ with $[a_k, a_{k'}^\dagger] = \delta_{kk'}$; fermions $c_k^\dagger$, $c_k$ with the **anticommutator** $\{c_k, c_{k'}^\dagger\} = \delta_{kk'}$. The number operator is $\hat{n}_k = c_k^\dagger c_k$.

**定义。** 不追踪有标记的粒子，而是追踪单粒子态的**占据数**。引入**产生/湮灭算符**：玻色子 $a_k^\dagger$、$a_k$ 满足 $[a_k, a_{k'}^\dagger] = \delta_{kk'}$；费米子 $c_k^\dagger$、$c_k$ 满足**反对易子** $\{c_k, c_{k'}^\dagger\} = \delta_{kk'}$。粒子数算符为 $\hat{n}_k = c_k^\dagger c_k$。

**Demonstration.** A many-fermion state is built by acting creation operators on the vacuum: $|\Psi\rangle = c_1^\dagger c_2^\dagger \ldots |0\rangle$. The anticommutation $\{c_1^\dagger, c_2^\dagger\} = 0$ automatically enforces antisymmetry and the Pauli principle — $(c^\dagger)^2 = 0$ means you can't create two fermions in the same state. This is just the harmonic-oscillator ladder algebra (3.2) promoted to "one oscillator per mode."

**演示。** 多费米子态通过对真空作用产生算符来构建：$|\Psi\rangle = c_1^\dagger c_2^\dagger \ldots |0\rangle$。反对易关系 $\{c_1^\dagger, c_2^\dagger\} = 0$ 自动强制满足反对称性和泡利不相容原理——$(c^\dagger)^2 = 0$ 意味着不能在同一态中产生两个费米子。这正是谐振子梯形代数（3.2）推广为"每个模式一个振子"的结果。

**Application.** **This is the single most important tool to carry into superconductivity.** The BCS Hamiltonian (Phase 5) is written entirely in terms of $c_k^\dagger$ and $c_k$; Cooper pairing is the operator $c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger$; and the whole machinery of condensed-matter field theory (Phase 6) is second quantization. If only one module of Phase 3 must be airtight, make it this one (alongside 3.2 and 3.5, which it builds on).

**应用。** **这是进入超导性最重要的单一工具。** BCS 哈密顿量（第 5 阶段）完全用 $c_k^\dagger$ 和 $c_k$ 书写；库珀配对即算符 $c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger$；凝聚态场论的全部机制（第 6 阶段）都是二次量子化。若第 3 阶段只能有一个模块做到炉火纯青，就是这个（以及它所依赖的 3.2 和 3.5）。

## Key results · 核心结果

- $[a_k, a_{k'}^\dagger] = \delta_{kk'}$ (bosons) vs $\{c_k, c_{k'}^\dagger\} = \delta_{kk'}$ (fermions) — commutation vs anticommutation · 对易／反对易关系
- $\hat{n}_k = c_k^\dagger c_k$ — number operator · 粒子数算符
- $(c_k^\dagger)^2 = 0$ — Pauli exclusion, automatic antisymmetry · 泡利不相容，自动反对称
- $|\Psi\rangle = c_1^\dagger c_2^\dagger \cdots |0\rangle$ — many-body states from the vacuum · 由真空构建多体态
- $c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger$ — the Cooper-pair operator carried into Phase 5 · 进入第 5 阶段的库珀对算符

---

**Self-test (blank page)**

1. State the commutation relation $[a_k, a_{k'}^\dagger] = \delta_{kk'}$ for bosonic operators and the anticommutation relation $\{c_k, c_{k'}^\dagger\} = \delta_{kk'}$ for fermionic operators. Show that the fermionic relation $(c_k^\dagger)^2 = 0$ follows directly from $\{c_k^\dagger, c_k^\dagger\} = 0$, and explain why this enforces the Pauli exclusion principle.
2. Explain what "occupation-number representation" means: how does the second-quantized description of a many-particle state differ from the first-quantized (labeled-particle) description, and what advantage does it offer for systems with variable particle number?
3. Write down the many-fermion state $|\Psi\rangle = c_1^\dagger c_2^\dagger \ldots c_n^\dagger |0\rangle$ and describe the role of the vacuum $|0\rangle$. How does swapping the order of two creation operators demonstrate that the state is automatically antisymmetric?
4. Express the BCS pairing operator in second-quantization notation and identify the single-particle states being paired. Why is the Cooper-pair operator $c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger$ written with opposite momenta and opposite spins?

**自测（空白页）**

1. 写出玻色子算符的对易关系 $[a_k, a_{k'}^\dagger] = \delta_{kk'}$ 和费米子算符的反对易关系 $\{c_k, c_{k'}^\dagger\} = \delta_{kk'}$。由 $\{c_k^\dagger, c_k^\dagger\} = 0$ 直接推导出 $(c_k^\dagger)^2 = 0$，并解释为什么这一关系强制满足泡利不相容原理。
2. 解释"占据数表象"的含义：二次量子化对多粒子态的描述与一次量子化（带标记粒子）的描述有何不同？对于粒子数可变的系统，它的优势是什么？
3. 写出多费米子态 $|\Psi\rangle = c_1^\dagger c_2^\dagger \ldots c_n^\dagger |0\rangle$，描述真空态 $|0\rangle$ 的作用。交换两个产生算符的顺序如何说明该态自动满足反对称性？
4. 用二次量子化符号写出 BCS 配对算符，并指出被配对的单粒子态。为什么库珀对算符 $c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger$ 要写成动量相反、自旋相反的形式？

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** Bosons: $[a_k,a^\dagger_{k'}]=\delta_{kk'}$; fermions: $\{c_k,c^\dagger_{k'}\}=\delta_{kk'}$. Setting $k=k'$ in $\{c_k^\dagger,c_k^\dagger\}=2(c_k^\dagger)^2=0$ gives $(c_k^\dagger)^2=0$: you cannot create two fermions in the same mode — the Pauli principle. · 费米子反对易关系取 $k=k'$ 即得 $(c_k^\dagger)^2=0$,无法在同一模式产生两个费米子,即泡利不相容。

**2.** Occupation-number representation labels a state by *how many* particles occupy each mode, $|n_1,n_2,\dots\rangle$, not by which labelled particle sits where. (Anti)symmetry is built into the operator algebra, and creation/annihilation operators change $N$, so variable particle number is natural. · 占据数表象按各模式的粒子数标记态,(反)对称性内建于算符代数,且能自然处理可变粒子数。

**3.** $|\Psi\rangle=c_1^\dagger\cdots c_n^\dagger|0\rangle$ with $|0\rangle$ the no-particle vacuum ($c_k|0\rangle=0$). Swapping two creation operators costs a sign by $\{c_i^\dagger,c_j^\dagger\}=0$, so the state is automatically antisymmetric. · 真空满足 $c_k|0\rangle=0$;交换两个产生算符因反对易关系变号,故态自动反对称。

**4.** $c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger$ creates a Cooper pair from the states $(\mathbf{k}\uparrow)$ and $(-\mathbf{k}\downarrow)$. Opposite momenta ⟹ zero total momentum (a condensate at rest); opposite spins ⟹ a spin-singlet, the attractive $s$-wave channel. · 相反动量给出零总动量,相反自旋给出自旋单态($s$ 波吸引道)。

</details>

---

← Previous: [Module 3.11 — Angular Momentum, Advanced](./module-3.11-angular-momentum-advanced.md) · [Phase 3 index](./README.md) · Next: [Module 3.13 — Entanglement, EPR & Bell's Theorem](./module-3.13-entanglement-epr-and-bell.md) →

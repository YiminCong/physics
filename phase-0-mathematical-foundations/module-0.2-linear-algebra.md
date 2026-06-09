# Module 0.2 — Linear Algebra ⭐
**模块 0.2 — 线性代数 ⭐**

> **Phase 0 — [Mathematical Foundations](./README.md)** · Format: Definition → Demonstration → Application
> **第 0 阶段 — 数学基础** · 格式：定义 → 演示 → 应用
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-0.2-linear-algebra-derivations.md)

Linear algebra is not background material for quantum mechanics — it *is* quantum mechanics. Every state, every measurement, every time evolution is a statement in the language of vectors and operators.

线性代数不是量子力学的背景材料——它*就是*量子力学。每一个态、每一次测量、每一次时间演化，都是用向量与算符语言写成的陈述。

---

## 1. Vectors, Inner Products & Bases · 向量、内积与基

**Definition.** A **vector space** is a set of objects (vectors) that can be added and scaled while staying in the set. An **inner product** $\langle u|v\rangle$ assigns a scalar to each pair of vectors, satisfying linearity, conjugate symmetry ($\langle u|v\rangle = \langle v|u\rangle^*$), and positive-definiteness ($\langle v|v\rangle \ge 0$). The **norm** is $\|v\| = \sqrt{\langle v|v\rangle}$. A set of vectors $\{e_i\}$ is **orthonormal** if $\langle e_i|e_j\rangle = \delta_{ij}$ and **complete** (a basis) if every vector can be written $v = \sum_i \langle e_i|v\rangle\, e_i$. The coefficients $\langle e_i|v\rangle$ are the **components** in that basis.

**定义。** **向量空间**是一组对象（向量）的集合，其元素可以相加和数乘且结果仍在集合内。**内积** $\langle u|v\rangle$ 为每对向量指定一个标量，满足线性性、共轭对称性（$\langle u|v\rangle = \langle v|u\rangle^*$）以及正定性（$\langle v|v\rangle \ge 0$）。**范数**为 $\|v\| = \sqrt{\langle v|v\rangle}$。若向量组 $\{e_i\}$ 满足 $\langle e_i|e_j\rangle = \delta_{ij}$，则称其为**正交归一**的；若每个向量都可写成 $v = \sum_i \langle e_i|v\rangle\, e_i$，则称其为**完备**的（即基）。系数 $\langle e_i|v\rangle$ 为该基下的**分量**。

**Demonstration.** In $\mathbb{R}^2$, the standard basis $\{(1,0), (0,1)\}$ is orthonormal under the dot product. Rotating to a new orthonormal basis changes the components but not the underlying vector — a lesson that carries into QM, where the basis of energy eigenstates and the basis of position eigenstates represent the same state in different ways.

**演示。** 在 $\mathbb{R}^2$ 中，标准基 $\{(1,0), (0,1)\}$ 在点积意义下是正交归一的。旋转到一个新的正交归一基会改变分量，但不改变底层向量本身——这一道理延伸到量子力学中：能量本征态基与位置本征态基以不同方式表示同一个态。

**Application.** The Hilbert space of quantum states is an (often infinite-dimensional) inner product space. The inner product $\langle\psi|\varphi\rangle$ gives transition amplitudes; completeness of the energy-eigenstate basis means any state can be written as a superposition — the foundation of all wave mechanics (Module 3.3).

**应用。** 量子态的希尔伯特空间是一个（通常为无穷维的）内积空间。内积 $\langle\psi|\varphi\rangle$ 给出跃迁振幅；能量本征态基的完备性意味着任何态都可以写成叠加——这是所有波动力学的基础（模块 3.3）。

---

## 2. Operators & Eigenvalues ⭐ · 算符与本征值 ⭐

**Definition.** A **linear operator** A maps vectors to vectors linearly. In a finite-dimensional space with a chosen basis, operators are represented as **matrices**. The **eigenvalue equation** is

**定义。** **线性算符** A 将向量线性地映射到向量。在有限维空间中选定基后，算符由**矩阵**表示。**本征值方程**为

$$ A v = \lambda v $$

where $v \ne 0$ is an **eigenvector** and $\lambda$ is the corresponding **eigenvalue**. Two special classes dominate physics:

其中 $v \ne 0$ 为**本征向量**，$\lambda$ 为对应的**本征值**。两类特殊算符在物理中占主导地位：

- **Hermitian operators** ($A = A^\dagger$, where $A^\dagger_{ij} = A_{ji}^*$): eigenvalues are **real**, eigenvectors for distinct eigenvalues are **orthogonal**, and the eigenvectors form a complete basis — the **spectral theorem**.
- **Unitary operators** ($U^\dagger U = I$): preserve norms ($\|Uv\| = \|v\|$) and have eigenvalues of modulus 1.

- **厄米算符**（$A = A^\dagger$，其中 $A^\dagger_{ij} = A_{ji}^*$）：本征值为**实数**，不同本征值对应的本征向量**正交**，本征向量构成完备基——即**谱定理**。
- **幺正算符**（$U^\dagger U = I$）：保持范数不变（$\|Uv\| = \|v\|$），本征值的模为 1。

The three **Pauli matrices** are the foundational Hermitian, traceless, unitary-up-to-phase operators of spin-$\tfrac12$:

三个**泡利矩阵**是自旋-$\tfrac12$ 系统的基本厄米、无迹、相位意义下幺正的算符：

$$ \sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} $$

They satisfy $\sigma_i \sigma_j = \delta_{ij} I + i \varepsilon_{ijk} \sigma_k$ and are the building blocks of all two-level quantum systems.

它们满足 $\sigma_i \sigma_j = \delta_{ij} I + i \varepsilon_{ijk} \sigma_k$，是所有两能级量子系统的构建模块。

**Demonstration.** Diagonalize $\sigma_x$. The characteristic equation $\det(\sigma_x - \lambda I) = 0$:

**演示。** 对 $\sigma_x$ 进行对角化。特征方程 $\det(\sigma_x - \lambda I) = 0$：

$$ \det\begin{pmatrix} -\lambda & 1 \\ 1 & -\lambda \end{pmatrix} = \lambda^2 - 1 = 0 \implies \lambda = \pm 1. $$

For $\lambda = +1$: $(\sigma_x - I)v = 0$ gives $v_1 = v_2$, so the eigenvector is $(1/\sqrt{2})(1, 1)^\top$.
For $\lambda = -1$: $v_1 = -v_2$, giving $(1/\sqrt{2})(1, -1)^\top$.
These two orthonormal eigenvectors are the **$|{+}x\rangle, |{-}x\rangle$ basis** — the spin eigenstates along $x$.

对 $\lambda = +1$：$(\sigma_x - I)v = 0$ 给出 $v_1 = v_2$，故本征向量为 $(1/\sqrt{2})(1, 1)^\top$。
对 $\lambda = -1$：$v_1 = -v_2$，给出 $(1/\sqrt{2})(1, -1)^\top$。
这两个正交归一本征向量就是 **$|{+}x\rangle, |{-}x\rangle$ 基**——沿 $x$ 方向的自旋本征态。

**Application.** Quantum mechanics is, at its core, linear algebra in Hilbert space: physical **observables are Hermitian operators** whose real eigenvalues are the only allowed measurement outcomes, and **time evolution is unitary** (Module 3.10), preserving probability. The spectral theorem guarantees any observable can be diagonalized and its eigenstates used as a basis — this is why energy eigenstates and momentum eigenstates are so central to Module 3.3. Separately, finding the **normal modes** of coupled oscillators (Module 1.6) is exactly the eigenvalue problem for the mass-weighted stiffness matrix.

**应用。** 量子力学的核心是希尔伯特空间中的线性代数：物理**可观测量是厄米算符**，其实数本征值是唯一允许的测量结果；**时间演化是幺正的**（模块 3.10），从而保持概率守恒。谱定理保证任何可观测量都可以被对角化，其本征态可用作基——这正是能量本征态和动量本征态在模块 3.3 中如此核心的原因。此外，寻找耦合振子的**简正模式**（模块 1.6）恰好就是质量加权刚度矩阵的本征值问题。

---

## Module 0.2 Self-Test (blank page)

1. Define an inner product and orthonormality; expand a vector in an orthonormal basis.
2. State the spectral theorem for Hermitian operators and its two key consequences.
3. Write down the three Pauli matrices and compute $\sigma_x \sigma_y$.
4. Find the eigenvalues and normalized eigenvectors of $\sigma_z$.
5. Explain why observables in QM must be Hermitian and why time evolution must be unitary.

**自测（空白页）**

1. 定义内积与正交归一性；在正交归一基下展开一个向量。
2. 陈述厄米算符的谱定理及其两个关键推论。
3. 写出三个泡利矩阵，并计算 $\sigma_x \sigma_y$。
4. 求 $\sigma_z$ 的本征值和归一化本征向量。
5. 解释为何量子力学中的可观测量必须是厄米的，时间演化必须是幺正的。

---

← Previous: [Module 0.1 — Calculus & Taylor Series](./module-0.1-calculus-and-taylor-series.md) · [Phase 0 index](./README.md) · Next: [Module 0.3 — Differential Equations](./module-0.3-differential-equations.md) →

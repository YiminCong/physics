# Module 6.7 — Exactly Solvable Models & Long-Range Order
**模块 6.7 — 精确可解模型与长程序**

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 6 阶段 — 量子场论与多体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-6.7-exactly-solvable-models-and-long-range-order-derivations.md)

*A set of exact, rigorous results in many-body physics — several due to C. N. Yang — that anchor the approximate methods of the rest of this phase.*

*多体物理中一组精确、严格的结果——其中多项归功于杨振宁——为本阶段其余近似方法提供了锚点。*

---

## 1. Exactly Solvable Models: Yang–Baxter & Lee–Yang · 精确可解模型：杨–巴克斯特方程与李–杨定理

**Definition.** Most many-body problems are only solvable approximately (Modules 6.3–6.4), but a special class is **exactly solvable** (integrable). The key consistency condition is the **Yang–Baxter equation** (Yang 1967, Baxter 1972): it guarantees that multi-particle scattering factorizes into two-body events, the engine behind the **Bethe ansatz**, quantum spin chains, and 2D statistical-mechanics models. Separately, the **Lee–Yang theorem** (1952) gives a rigorous theory of phase transitions: a transition occurs exactly where the **zeros of the partition function** (in the complex fugacity plane) pinch the real axis in the thermodynamic limit.

**定义。** 大多数多体问题只能近似求解（模块 6.3–6.4），但有一类特殊问题是**精确可解**（可积）的。关键的相容性条件是**杨–巴克斯特方程**（Yang 1967，Baxter 1972）：它保证多粒子散射分解为两体事件，这是**贝特拟设**、量子自旋链和二维统计力学模型背后的引擎。另外，**李–杨定理**（1952）给出了相变的严格理论：相变恰好发生在**配分函数的零点**（在复逸度平面中）在热力学极限下夹紧实轴之处。

**Demonstration.** The 1D Heisenberg spin chain and the 2D Ising model are solved exactly by these methods, giving benchmark results — exact energies, correlations, and critical exponents — against which perturbation theory (Module 6.3) and the renormalization group (Module 6.6) are checked.

**演示。** 一维海森堡自旋链和二维伊辛模型用这些方法精确求解，给出基准结果——精确能量、关联函数和临界指数——用以检验微扰论（模块 6.3）和重整化群（模块 6.6）。

## 2. Off-Diagonal Long-Range Order · 非对角长程序

**Definition.** **Yang (1962)** gave a unified, rigorous definition of superfluid and superconducting order: **off-diagonal long-range order (ODLRO)** — the reduced density matrix retains a non-vanishing element between far-separated points. The related **Byers–Yang theorem** shows that magnetic flux through a superconducting ring is quantized in units of $h/2e$, with the factor of 2 a direct signature of electron *pairing* (Module 5.3).

**定义。** **杨振宁（1962）**给出了超流和超导序的统一、严格定义：**非对角长程序（ODLRO）**——约化密度矩阵在远距离分离的点之间保留非零元素。相关的 **Byers–Yang 定理**表明，穿过超导环的磁通量以 $h/2e$ 为单位量子化，其中因子 2 是电子*配对*的直接标志（模块 5.3）。

**Application.** ODLRO is the precise statement behind the Ginzburg–Landau order parameter (Module 5.3) and Bose–Einstein condensation (Module 2.6): it says exactly what "macroscopic quantum coherence" means. These exact results — integrability and ODLRO — are the rigorous backbone of modern condensed-matter and cold-atom physics, and the testing ground for the approximate field-theory machinery of this phase.

**应用。** 非对角长程序是金兹堡–朗道序参量（模块 5.3）和玻色–爱因斯坦凝聚（模块 2.6）背后的精确表述：它准确说明了"宏观量子相干"的含义。这些精确结果——可积性和非对角长程序——是现代凝聚态和冷原子物理的严格骨架，也是本阶段近似场论机器的检验场。

## Key results · 核心结果

- Yang–Baxter equation ⟹ integrability (factorized scattering) · 杨–巴克斯特方程与可积性
- Bethe ansatz, transfer-matrix methods rely on it · 贝特拟设
- Lee–Yang zeros: phase transitions from partition-function zeros · 李–杨零点
- ODLRO; Byers–Yang $h/2e$ flux period reveals pairing · 非对角长程序与 $h/2e$

---

**Self-test (blank page)**

1. What does the Yang–Baxter equation guarantee, and which solution methods rely on it?
2. State the Lee–Yang picture of a phase transition in terms of partition-function zeros.
3. Define off-diagonal long-range order and explain how the Byers–Yang $h/2e$ flux quantum reveals electron pairing.

**自测（空白页）**

1. 杨–巴克斯特方程保证了什么？哪些求解方法依赖于它？
2. 用配分函数零点的语言陈述相变的李–杨图像。
3. 定义非对角长程序，并解释 Byers–Yang $h/2e$ 磁通量子如何揭示电子配对。

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** Yang–Baxter guarantees that multi-particle scattering factorizes consistently into two-body events (order-independent) → integrability; the Bethe ansatz and quantum inverse-scattering/transfer-matrix methods rely on it. · 散射可因子化,贝特拟设依赖它。
**2.** Lee–Yang: the partition function's zeros in the complex fugacity (or field) plane pinch the real axis in the thermodynamic limit; a phase transition occurs exactly where they touch (non-analyticity of $F$). · 配分函数零点触及实轴处发生相变。
**3.** ODLRO: the reduced density matrix stays finite at large separation — the hallmark of condensation. The Byers–Yang period $h/2e$ (not $h/e$) shows the carriers are charge-$2e$ pairs. · 非对角长程序;$h/2e$ 揭示电子配对。

</details>

---

← Previous: [Module 6.6 — Renormalization & the Renormalization Group](./module-6.6-renormalization.md) · [Phase 6 index](./README.md) · Next: [Module 6.8 — Scattering, the S-Matrix & LSZ Reduction](./module-6.8-scattering-s-matrix-and-lsz.md) →

# Phase 0 — Mathematical Foundations · 数学基础

<table>
<tr><th>English</th><th>中文</th></tr>
<tr>
<td>

This phase assembles the toolkit that every later phase draws on. All six modules follow the **Definition → Demonstration → Application** format — each section builds the idea, shows it working, and points forward to the physics that depends on it.

</td>
<td>

本阶段汇集了后续每个阶段都会用到的工具箱。全部六个模块均遵循**定义 → 演示 → 应用**格式——每一节先建立概念，再展示其运作，最后指向依赖它的物理内容。

</td>
</tr>
</table>

## Modules · 模块

| # | Title · 标题 | Notes · 说明 |
|---|-------|-------|
| 0.1 | [Calculus & Taylor Series · 微积分与泰勒级数](./module-0.1-calculus-and-taylor-series.md) | Derivatives, integrals, FTC; Taylor series as the universal approximation tool · 导数、积分、微积分基本定理；泰勒级数作为通用近似工具 |
| 0.2 | [Linear Algebra · 线性代数](./module-0.2-linear-algebra.md) ⭐ | Vector spaces, inner products, eigenvalues; the Pauli matrices; QM is this · 向量空间、内积、本征值；泡利矩阵；量子力学即线性代数 |
| 0.3 | [Differential Equations · 微分方程](./module-0.3-differential-equations.md) | First- and second-order ODEs, series solutions, PDEs and separation of variables · 一阶与二阶常微分方程、级数解、偏微分方程与分离变量法 |
| 0.4 | [Complex Analysis · 复分析](./module-0.4-complex-analysis.md) ⭐ | Euler's formula, analytic functions, contour integration; phase drives superconductivity · 欧拉公式、解析函数、围道积分；相位驱动超导 |
| 0.5 | [Fourier Analysis & Probability · 傅里叶分析与概率](./module-0.5-fourier-analysis-and-probability.md) ⭐ | Fourier transform, Dirac delta, convolution; mean, variance, Gaussian, CLT · 傅里叶变换、狄拉克 δ 函数、卷积；均值、方差、高斯分布、中心极限定理 |
| 0.6 | [Vector Calculus, Tensors & Differential Forms · 向量微积分、张量与微分形式](./module-0.6-vector-calculus-tensors-and-differential-forms.md) | ∇, ∇·, ∇×, integral theorems; index notation, the metric tensor; Maxwell in a line · ∇, ∇·, ∇×，积分定理；指标记号、度规张量；一行写尽麦克斯韦方程 |

## Why these matter downstream · 为何这些内容对后续至关重要

<table>
<tr><th>English</th><th>中文</th></tr>
<tr>
<td>

- **0.1** — the self-referential property eˣ = d/dx(eˣ) seeds every constant-coefficient ODE solution and, via iθ substitution, Euler's formula in 0.4.
- **0.2** — quantum mechanics is linear algebra in Hilbert space; Hermitian operators give measurement outcomes, unitary operators give time evolution (Phase 3).
- **0.3** — the second-order linear ODE is the time-independent Schrödinger equation in disguise; special functions (Hermite, Legendre, Laguerre) are the wavefunctions of the oscillator, angular momentum, and hydrogen (Phase 3).
- **0.4** — complex amplitudes underlie all of QM; the phase φ of the order parameter ψ = |ψ|e^{iφ} drives supercurrents and the Josephson effect (Phase 5).
- **0.5** — position and momentum are Fourier conjugates, making the uncertainty principle a theorem; the reciprocal lattice is the FT of the crystal (Phase 4).
- **0.6** — vector calculus is the native language of electromagnetism (Phase 1); the metric tensor g_{μν} is the central object of general relativity (Phase 7).

</td>
<td>

- **0.1** — eˣ = d/dx(eˣ) 的自指性质播下了所有常系数常微分方程解的种子，并经由代入 iθ 给出 0.4 中的欧拉公式。
- **0.2** — 量子力学是希尔伯特空间中的线性代数；厄米算符给出测量结果，幺正算符给出时间演化（第 3 阶段）。
- **0.3** — 二阶线性常微分方程是伪装的定态薛定谔方程；特殊函数（厄米、勒让德、拉盖尔）是谐振子、角动量和氢原子的波函数（第 3 阶段）。
- **0.4** — 复数幅度是全部量子力学的基础；序参量 ψ = |ψ|e^{iφ} 的相位 φ 驱动超导电流和约瑟夫森效应（第 5 阶段）。
- **0.5** — 位置与动量是傅里叶共轭，使不确定性原理成为一个定理；倒易格子是晶体的傅里叶变换（第 4 阶段）。
- **0.6** — 向量微积分是电磁学的母语（第 1 阶段）；度规张量 g_{μν} 是广义相对论的核心对象（第 7 阶段）。

</td>
</tr>
</table>

## Phase 0 Checkpoint (blank page) · 第 0 阶段检查点（空白页）

<table>
<tr><th>English</th><th>中文</th></tr>
<tr>
<td>

Work through these without notes. If any answer is unclear, revisit the corresponding module before moving on.

1. (0.1) Expand sin x and cos x as Taylor series; use them to derive Euler's formula e^{iθ} = cos θ + i sin θ.
2. (0.2) State the spectral theorem for Hermitian operators. Find the eigenvalues and eigenvectors of σ_y.
3. (0.3) Solve y″ + 2γy′ + ω₀²y = 0; identify the three damping regimes. How does separation of variables apply to the Schrödinger equation?
4. (0.4) Evaluate ∮ dz / (z² + 1) around a contour enclosing z = i using residues.
5. (0.5) Why is the Fourier transform of a Gaussian another Gaussian, and how does this become the Heisenberg uncertainty principle?
6. (0.6) Write Maxwell's four equations in differential form, naming the operator (∇·, ∇×) in each, and state the integral theorem that converts each to its integral form.

</td>
<td>

不看笔记独立完成以下各题。如有答案不清晰，先回顾对应模块再继续。

1. (0.1) 将 sin x 和 cos x 展开为泰勒级数；用它们推导欧拉公式 e^{iθ} = cos θ + i sin θ。
2. (0.2) 叙述厄米算符的谱定理。求 σ_y 的本征值与本征向量。
3. (0.3) 求解 y″ + 2γy′ + ω₀²y = 0；识别三种阻尼状态。分离变量法如何应用于薛定谔方程？
4. (0.4) 用留数定理计算 ∮ dz / (z² + 1) 沿包围 z = i 的围道的积分。
5. (0.5) 为何高斯函数的傅里叶变换仍是高斯函数？这如何成为海森堡不确定性原理？
6. (0.6) 写出麦克斯韦四个方程的微分形式，各指明所用算符（∇·, ∇×），并说明将各方程化为积分形式所用的积分定理。

</td>
</tr>
</table>

---

→ Continue to **[Phase 1 — Classical Physics](../phase-1-classical-physics/)**. · 继续前往**第 1 阶段——经典物理学**。

# Module 0.4 — Complex Analysis ⭐
**模块 0.4 — 复分析 ⭐**

> **Phase 0 — [Mathematical Foundations](./README.md)** · Format: Definition → Demonstration → Application
> **第 0 阶段 — 数学基础** · 格式：定义 → 演示 → 应用
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-0.4-complex-analysis-derivations.md)

Complex numbers aren't a mathematical curiosity in physics — quantum amplitudes are
intrinsically complex, and the *phase* of a complex number is what carries interference,
currents, and (in Phase 5) superconductivity itself.

物理学中的复数并非数学上的猎奇——量子幅度本质上是复数，而复数的*相位*正是携带干涉、电流以及（在第 5 阶段中）超导性本身的关键。

---

## 1. Complex Numbers · 复数

**Definition.** A complex number is z = a + bi, where i² = −1; a is the real part, b the imaginary part. The **complex conjugate** is z* = a − bi, and the **modulus** is |z| = √(a² + b²), with |z|² = z z*.

**定义。** 复数为 z = a + bi，其中 i² = −1；a 为实部，b 为虚部。**复共轭**为 z* = a − bi，**模**为 |z| = √(a² + b²)，且 |z|² = z z*。

**Demonstration.** (1 + i)(2 − i) = 2 − i + 2i − i² = 2 + i + 1 = **3 + i**. And |3 + 4i| = √(9 + 16) = **5**.

**演示。** (1 + i)(2 − i) = 2 − i + 2i − i² = 2 + i + 1 = **3 + i**。且 |3 + 4i| = √(9 + 16) = **5**。

**Application.** Quantum probability **amplitudes** are complex numbers; the physically observable probability is |amplitude|² = (amplitude)(amplitude)*. Complex conjugation is built into the QM inner product.

**应用。** 量子概率**幅度**是复数；物理上可观测的概率为 |amplitude|² = (amplitude)(amplitude)*。复共轭内嵌于量子力学的内积之中。

---

## 2. Euler's Formula ⭐ · 欧拉公式 ⭐

**Definition.** The bridge between exponentials and trigonometry:

**定义。** 指数函数与三角函数之间的桥梁：

  **e^{iθ} = cos θ + i sin θ.**

This gives the **polar form** z = r e^{iθ}, where r = |z| and θ is the phase angle. A famous special case: e^{iπ} + 1 = 0.

这给出了**极坐标形式** z = r e^{iθ}，其中 r = |z|，θ 为相位角。一个著名的特例：e^{iπ} + 1 = 0。

**Demonstration.** From the Taylor series (Module 0.1): substitute iθ into eˣ = Σ xⁿ/n!. The real terms reassemble into cos θ and the imaginary terms into i sin θ. Multiplication then **adds phases**: (r₁e^{iθ₁})(r₂e^{iθ₂}) = r₁r₂ e^{i(θ₁+θ₂)}.

**演示。** 根据泰勒级数（模块 0.1）：将 iθ 代入 eˣ = Σ xⁿ/n!。实数项重新组合为 cos θ，虚数项重新组合为 i sin θ。乘法则**叠加相位**：(r₁e^{iθ₁})(r₂e^{iθ₂}) = r₁r₂ e^{i(θ₁+θ₂)}。

**Application.** Plane-wave wavefunctions are written e^{i(kx − ωt)} — the phase encodes momentum and energy (Phase 3). In superconductivity the **order parameter** is ψ = |ψ| e^{iφ}; the *rigidity of that phase φ* across the material is precisely what drives dissipationless supercurrents and the Josephson effect (Phase 5). Phase is not optional bookkeeping — it's physics.

**应用。** 平面波波函数写作 e^{i(kx − ωt)}——相位编码了动量和能量（第 3 阶段）。在超导体中，**序参量**为 ψ = |ψ| e^{iφ}；材料中*该相位 φ 的刚性*正是驱动无耗散超电流和约瑟夫森效应的根本原因（第 5 阶段）。相位不是可有可无的记账工具——它就是物理。

---

## 3. Functions of a Complex Variable & Analyticity · 复变函数与解析性

**Definition.** A function f(z) is **analytic** (holomorphic) in a region if it is complex-differentiable there. Writing f = u(x,y) + i v(x,y), analyticity requires the **Cauchy–Riemann equations**: ∂u/∂x = ∂v/∂y and ∂u/∂y = −∂v/∂x. Analytic functions are extraordinarily well-behaved (infinitely differentiable, determined by their values on a boundary).

**定义。** 若函数 f(z) 在某区域内处处复可微，则称其在该区域**解析**（全纯）。令 f = u(x,y) + i v(x,y)，解析性要求满足**柯西–黎曼方程**：∂u/∂x = ∂v/∂y 且 ∂u/∂y = −∂v/∂x。解析函数性质极好（无穷次可微，由其在边界上的值唯一确定）。

**Demonstration.** Check f(z) = z² = (x² − y²) + i(2xy). Here u = x²−y², v = 2xy. Then ∂u/∂x = 2x = ∂v/∂y, and ∂u/∂y = −2y = −∂v/∂x. Cauchy–Riemann satisfied → z² is analytic.

**演示。** 验证 f(z) = z² = (x² − y²) + i(2xy)。其中 u = x²−y²，v = 2xy。则 ∂u/∂x = 2x = ∂v/∂y，且 ∂u/∂y = −2y = −∂v/∂x。柯西–黎曼方程满足 → z² 是解析的。

**Application.** Analyticity underlies **response functions** and **dispersion relations** in many-body physics: the fact that a system can't respond before it's perturbed (causality) forces the response function to be analytic in the upper half-plane, which links its real and imaginary parts (Phase 6).

**应用。** 解析性是多体物理中**响应函数**和**色散关系**的基础：系统不能在受到扰动之前做出响应（因果律），这迫使响应函数在上半平面解析，从而将其实部与虚部联系起来（第 6 阶段）。

---

## 4. Contour Integration & the Residue Theorem · 围道积分与留数定理

**Definition.** Integrals along paths ("contours") in the complex plane. The **residue theorem** states that a closed-contour integral equals 2πi times the sum of **residues** (coefficients of the 1/(z−z₀) term) at the poles enclosed:

**定义。** 沿复平面中路径（"围道"）的积分。**留数定理**指出，沿闭合围道的积分等于 2πi 乘以所有被围极点的**留数**（1/(z−z₀) 项的系数）之和：

  ∮_C f(z) dz = 2πi Σ Res(f, zₖ).

**Demonstration.** ∮ dz/z around a loop enclosing the origin: the residue of 1/z at z = 0 is 1, so the integral is **2πi**. This trick converts many hard *real* integrals into simple residue sums.

**演示。** ∮ dz/z 沿围绕原点的回路积分：1/z 在 z = 0 处的留数为 1，故积分为 **2πi**。这一技巧将许多困难的*实数*积分转化为简单的留数求和。

**Application.** Contour integration is the standard tool for evaluating integrals in quantum field theory and many-body physics, and it's how **Green's functions** and the **Kramers–Kronig relations** are handled (Phase 6). You won't need it heavily until the advanced phase, but recognizing it now pays off.

**应用。** 围道积分是量子场论和多体物理中计算积分的标准工具，**格林函数**和**克喇末–克朗尼希关系**也借助它来处理（第 6 阶段）。直到高级阶段才会大量用到它，但现在认识它会有所回报。

---

## Module 0.4 Self-Test (blank page)

1. Multiply two complex numbers and compute a modulus.
2. State Euler's formula and derive it from Taylor series; show that multiplication adds phases.
3. Write a plane wave in complex form and explain what its phase encodes.
4. Verify the Cauchy–Riemann equations for f(z) = z².
5. Evaluate ∮ dz/z around the origin using residues.

If solid, advance to **Module 0.5 — Fourier Analysis & Probability**.

**自测（空白页）**

1. 将两个复数相乘并计算模。
2. 陈述欧拉公式并从泰勒级数推导它；证明乘法叠加相位。
3. 用复数形式写出一个平面波，并解释其相位编码了什么。
4. 验证 f(z) = z² 满足柯西–黎曼方程。
5. 用留数定理计算 ∮ dz/z 绕原点的积分。

---

← Previous: [Module 0.3 — Differential Equations](./module-0.3-differential-equations.md) · [Phase 0 index](./README.md) · Next: [Module 0.5 — Fourier Analysis & Probability](./module-0.5-fourier-analysis-and-probability.md) →

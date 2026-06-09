---
title: "Module 0.6 — Vector Calculus, Tensors & Differential Forms"
parent: "Phase 0 — Mathematical Foundations"
nav_order: 6
---

# Module 0.6 — Vector Calculus, Tensors & Differential Forms
**模块 0.6 — 向量微积分、张量与微分形式**

> **Phase 0 — [Mathematical Foundations](./README.md)** · Format: Definition → Demonstration → Application
> **第 0 阶段 — 数学基础** · 格式：定义 → 演示 → 应用
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-0.6-vector-calculus-tensors-and-differential-forms-derivations.md)

Vector calculus is the native language of fields — electric, magnetic, gravitational. Tensors extend that language to curved spacetime, and differential forms give it a coordinate-free elegance that pays off in general relativity and advanced electrodynamics.

向量微积分是场——电场、磁场、引力场——的母语。张量将这种语言推广到弯曲时空，而微分形式则赋予它无坐标的优雅，这在广义相对论和高级电动力学中大有裨益。

---

## 1. Grad, Div, Curl & the Integral Theorems · 梯度、散度、旋度与积分定理

**Definition.** The **gradient** $\nabla f$ of a scalar field is a vector pointing in the direction of steepest increase, with magnitude equal to that rate of increase. The **divergence** $\nabla\cdot F$ of a vector field measures the net outward flux per unit volume — how much the field "spreads out" from a point. The **curl** $\nabla\times F$ measures the rotation or circulation per unit area around a point. The **Laplacian** $\nabla^2 f = \nabla\cdot(\nabla f)$ combines both, giving the rate at which $f$ differs from its local average.

**定义。** 标量场的**梯度** $\nabla f$ 是一个指向最陡增方向的向量，其大小等于该方向上的变化率。向量场的**散度** $\nabla\cdot F$ 衡量单位体积的净向外通量——即场从某点"向外扩散"的程度。**旋度** $\nabla\times F$ 衡量某点周围单位面积的旋转或环量。**拉普拉斯算子** $\nabla^2 f = \nabla\cdot(\nabla f)$ 将两者结合，给出 $f$ 与其局部平均值之差的变化率。

Two integral theorems convert between volume/surface integrals and boundary integrals:
- **Divergence theorem (Gauss):** $\int_V (\nabla\cdot F)\, dV = \oint_S F\cdot dA$ — total divergence inside equals flux through the boundary.
- **Stokes' theorem:** $\int_S (\nabla\times F)\cdot dA = \oint_C F\cdot dl$ — total curl through a surface equals circulation around its boundary.

两个积分定理在体积/曲面积分与边界积分之间转化：
- **散度定理（高斯定理）：** $\int_V (\nabla\cdot F)\, dV = \oint_S F\cdot dA$——内部总散度等于穿过边界的通量。
- **斯托克斯定理：** $\int_S (\nabla\times F)\cdot dA = \oint_C F\cdot dl$——穿过曲面的总旋度等于沿其边界的环量。

**Demonstration.** Maxwell's equations illustrate every operator at once. In differential form: $\nabla\cdot E = \rho/\varepsilon_0$ (divergence of $E$ equals charge density), $\nabla\cdot B = 0$ (no magnetic monopoles), $\nabla\times E = -\partial B/\partial t$ (curl of $E$ driven by changing $B$), $\nabla\times B = \mu_0 J + \mu_0 \varepsilon_0\, \partial E/\partial t$ (curl of $B$ driven by current and changing $E$). In spherical coordinates, $\nabla^2 = \frac{1}{r^2}\frac{\partial}{\partial r}\!\left(r^2 \frac{\partial}{\partial r}\right) + \frac{1}{r^2 \sin\theta}\frac{\partial}{\partial\theta}\!\left(\sin\theta\, \frac{\partial}{\partial\theta}\right) + \frac{1}{r^2 \sin^2\theta}\frac{\partial^2}{\partial\varphi^2}$, the form needed for the hydrogen atom's Schrödinger equation.

**演示。** 麦克斯韦方程组同时展示了所有算符。微分形式：$\nabla\cdot E = \rho/\varepsilon_0$（$E$ 的散度等于电荷密度），$\nabla\cdot B = 0$（无磁单极子），$\nabla\times E = -\partial B/\partial t$（$E$ 的旋度由变化的 $B$ 驱动），$\nabla\times B = \mu_0 J + \mu_0 \varepsilon_0\, \partial E/\partial t$（$B$ 的旋度由电流和变化的 $E$ 驱动）。在球坐标下，$\nabla^2 = \frac{1}{r^2}\frac{\partial}{\partial r}\!\left(r^2 \frac{\partial}{\partial r}\right) + \frac{1}{r^2 \sin\theta}\frac{\partial}{\partial\theta}\!\left(\sin\theta\, \frac{\partial}{\partial\theta}\right) + \frac{1}{r^2 \sin^2\theta}\frac{\partial^2}{\partial\varphi^2}$，这是氢原子薛定谔方程所需的形式。

**Application.** Gauss's law in integral form — $\oint E\cdot dA = Q_{\text{enc}}/\varepsilon_0$ — follows from the divergence theorem applied to $\nabla\cdot E = \rho/\varepsilon_0$, and it is the standard route to the Coulomb field of a point charge (Module 1.8). Stokes' theorem relates Faraday's law in integral and differential form (Module 1.10). The Laplacian $\nabla^2\varphi = 0$ is Laplace's equation for the electrostatic potential in charge-free regions (Module 1.8).

**应用。** 积分形式的高斯定律——$\oint E\cdot dA = Q_{\text{enc}}/\varepsilon_0$——源于将散度定理应用于 $\nabla\cdot E = \rho/\varepsilon_0$，是推导点电荷库仑场的标准路径（模块 1.8）。斯托克斯定理将法拉第定律的积分形式与微分形式联系起来（模块 1.10）。拉普拉斯算子方程 $\nabla^2\varphi = 0$ 是无电荷区域静电势满足的拉普拉斯方程（模块 1.8）。

---

## 2. Tensors & Index Notation · 张量与指标记号

**Definition.** A **scalar** is a rank-0 tensor (one component), a **vector** is rank-1 (one index), and a general **tensor** $T^{\mu\nu}$ is rank-2 (two indices, transforming as a product of two vectors under coordinate changes). **Einstein summation convention**: a repeated index — one upper, one lower — is summed over all values, e.g. $A^\mu B_\mu = \sum_\mu A^\mu B_\mu$.

**定义。** **标量**是 0 阶张量（一个分量），**向量**是 1 阶张量（一个指标），而一般的**张量** $T^{\mu\nu}$ 是 2 阶张量（两个指标，在坐标变换下按两个向量之积的方式变换）。**爱因斯坦求和约定**：一对重复指标——一个上标、一个下标——对所有值求和，例如 $A^\mu B_\mu = \sum_\mu A^\mu B_\mu$。

The **metric tensor** $g_{\mu\nu}$ encodes the geometry of the space: the invariant interval (distance) between two nearby events is $ds^2 = g_{\mu\nu}\, dx^\mu dx^\nu$. In flat spacetime with signature $(-,+,+,+)$, $g_{\mu\nu} = \operatorname{diag}(-1, 1, 1, 1)$ (the Minkowski metric $\eta_{\mu\nu}$). The metric **raises and lowers indices**: $V_\mu = g_{\mu\nu} V^\nu$, so it converts between contravariant (upper) and covariant (lower) components.

**度规张量** $g_{\mu\nu}$ 编码了空间的几何：两个相邻事件之间的不变间隔（距离）为 $ds^2 = g_{\mu\nu}\, dx^\mu dx^\nu$。在号差为 $(-,+,+,+)$ 的平坦时空中，$g_{\mu\nu} = \operatorname{diag}(-1, 1, 1, 1)$（闵可夫斯基度规 $\eta_{\mu\nu}$）。度规**升降指标**：$V_\mu = g_{\mu\nu} V^\nu$，从而在逆变（上标）和协变（下标）分量之间相互转换。

**Differential forms** give an index-free, coordinate-independent framework: a $p$-form is an antisymmetric rank-$p$ covariant tensor. The exterior derivative $d$ maps $p$-forms to $(p+1)$-forms and satisfies $d^2 = 0$ — a generalization of $\nabla\times(\nabla f) = 0$ and $\nabla\cdot(\nabla\times F) = 0$. Maxwell's equations in this language compress to $dF = 0$ and $d\star F = J$, where $F$ is the 2-form Faraday tensor and $\star$ is the Hodge dual.

**微分形式**提供了一个无指标、坐标无关的框架：$p$-形式是反对称的 $p$ 阶协变张量。外微分算子 $d$ 将 $p$-形式映射为 $(p+1)$-形式，并满足 $d^2 = 0$——这是 $\nabla\times(\nabla f) = 0$ 和 $\nabla\cdot(\nabla\times F) = 0$ 的推广。用这种语言，麦克斯韦方程组简化为 $dF = 0$ 和 $d\star F = J$，其中 $F$ 是 2-形式法拉第张量，$\star$ 是霍奇对偶算子。

**Demonstration.** In special relativity, the four-momentum is $p^\mu = (E/c, p_x, p_y, p_z)$. Its Lorentz-invariant magnitude is $p^\mu p_\mu = g_{\mu\nu} p^\mu p^\nu = -E^2/c^2 + |\mathbf{p}|^2 = -(mc)^2$, recovering $E^2 = (pc)^2 + (mc^2)^2$ — an entirely index-based derivation.

**演示。** 在狭义相对论中，四动量为 $p^\mu = (E/c, p_x, p_y, p_z)$。其洛伦兹不变量为 $p^\mu p_\mu = g_{\mu\nu} p^\mu p^\nu = -E^2/c^2 + |\mathbf{p}|^2 = -(mc)^2$，从而还原出 $E^2 = (pc)^2 + (mc^2)^2$——这是一个完全基于指标的推导。

**Application.** Vector calculus ($\nabla$, $\nabla\cdot$, $\nabla\times$) is the language of all classical electromagnetism in Modules 1.8–1.11. Tensor index notation and the metric $g_{\mu\nu}$ are indispensable for covariant electrodynamics (Module 1.15) and are the entire technical foundation of general relativity (Phase 7), where $g_{\mu\nu}$ becomes dynamical — the field itself. Differential forms give the most compact statement of Maxwell's equations and appear in the geometric formulation of gauge theories (Phase 6).

**应用。** 向量微积分（$\nabla$、$\nabla\cdot$、$\nabla\times$）是模块 1.8–1.11 中所有经典电磁学的语言。张量指标记号和度规 $g_{\mu\nu}$ 对协变电动力学（模块 1.15）不可或缺，也是广义相对论（第 7 阶段）的全部技术基础——在那里 $g_{\mu\nu}$ 变为动力学量，即场本身。微分形式给出麦克斯韦方程组最紧凑的表述，并出现在规范理论的几何表述中（第 6 阶段）。

---

## Module 0.6 Self-Test (blank page)

1. State the physical meaning of $\nabla\cdot F$ and $\nabla\times F$; give one Maxwell equation illustrating each.
2. State the divergence theorem and Stokes' theorem; explain which Maxwell equation each converts between integral and differential form.
3. Write the Laplacian in spherical coordinates and identify where it appears in the hydrogen-atom Schrödinger equation.
4. Define the Einstein summation convention; write the invariant interval $ds^2$ using $g_{\mu\nu}$.
5. Show that $p^\mu p_\mu = -(mc)^2$ for a relativistic particle and interpret the result.
6. State what a differential form is and what $d^2 = 0$ generalizes.

**自测（空白页）**

1. 陈述 $\nabla\cdot F$ 和 $\nabla\times F$ 的物理含义；各给出一个麦克斯韦方程进行说明。
2. 陈述散度定理和斯托克斯定理；解释各自将哪个麦克斯韦方程在积分形式与微分形式之间转化。
3. 写出球坐标下的拉普拉斯算子，并说明它在氢原子薛定谔方程中出现的位置。
4. 定义爱因斯坦求和约定；用 $g_{\mu\nu}$ 写出不变间隔 $ds^2$。
5. 证明相对论粒子满足 $p^\mu p_\mu = -(mc)^2$，并解释其含义。
6. 陈述微分形式是什么，以及 $d^2 = 0$ 推广了什么。

---

← Previous: [Module 0.5 — Fourier Analysis & Probability](./module-0.5-fourier-analysis-and-probability.md) · [Phase 0 index](./README.md) · Next: [Module 0.7 — Group Theory & Lie Algebras](./module-0.7-group-theory-and-lie-algebras.md) →

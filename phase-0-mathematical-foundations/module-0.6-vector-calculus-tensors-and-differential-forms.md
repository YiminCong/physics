# Module 0.6 — Vector Calculus, Tensors & Differential Forms · 向量微积分、张量与微分形式

> **Phase 0 — [Mathematical Foundations](./README.md)** · Format: Definition → Demonstration → Application
> **第 0 阶段 — 数学基础** · 格式：定义 → 演示 → 应用

<table>
<tr><th>English</th><th>中文</th></tr>
<tr>
<td>

Vector calculus is the native language of fields — electric, magnetic, gravitational. Tensors extend that language to curved spacetime, and differential forms give it a coordinate-free elegance that pays off in general relativity and advanced electrodynamics.

</td>
<td>

向量微积分是场（电场、磁场、引力场）的母语。张量将这种语言延伸至弯曲时空，而微分形式则赋予它无坐标的优雅，这在广义相对论与高级电动力学中大有裨益。

</td>
</tr>
</table>

---

## 1. Grad, Div, Curl & the Integral Theorems · 梯度、散度、旋度与积分定理

<table>
<tr><th>English</th><th>中文</th></tr>
<tr>
<td>

**Definition.** The **gradient** ∇f of a scalar field is a vector pointing in the direction of steepest increase, with magnitude equal to that rate of increase. The **divergence** ∇·F of a vector field measures the net outward flux per unit volume — how much the field "spreads out" from a point. The **curl** ∇×F measures the rotation or circulation per unit area around a point. The **Laplacian** ∇²f = ∇·(∇f) combines both, giving the rate at which f differs from its local average.

Two integral theorems convert between volume/surface integrals and boundary integrals:
- **Divergence theorem (Gauss):** ∫_V (∇·F) dV = ∮_S F·dA — total divergence inside equals flux through the boundary.
- **Stokes' theorem:** ∫_S (∇×F)·dA = ∮_C F·dl — total curl through a surface equals circulation around its boundary.

</td>
<td>

**定义。** 标量场的**梯度** ∇f 是一个指向最陡上升方向的向量，其大小等于该方向的变化率。向量场的**散度** ∇·F 度量单位体积内的净向外通量——即场从某点"散开"的程度。**旋度** ∇×F 度量场绕某点单位面积的旋转或环量。**拉普拉斯算符** ∇²f = ∇·(∇f) 综合了两者，给出 f 偏离其局部平均值的速率。

两个积分定理在体积／面积积分与边界积分之间转换：
- **散度定理（高斯定理）：** ∫_V (∇·F) dV = ∮_S F·dA——内部总散度等于通过边界的通量。
- **斯托克斯定理：** ∫_S (∇×F)·dA = ∮_C F·dl——穿过曲面的总旋度等于沿其边界的环量。

</td>
</tr>
<tr>
<td>

**Demonstration.** Maxwell's equations illustrate every operator at once. In differential form: ∇·E = ρ/ε₀ (divergence of E equals charge density), ∇·B = 0 (no magnetic monopoles), ∇×E = −∂B/∂t (curl of E driven by changing B), ∇×B = μ₀J + μ₀ε₀ ∂E/∂t (curl of B driven by current and changing E). In spherical coordinates, ∇² = (1/r²) ∂/∂r(r² ∂/∂r) + (1/r² sin θ) ∂/∂θ(sin θ ∂/∂θ) + (1/r² sin²θ) ∂²/∂φ², the form needed for the hydrogen atom's Schrödinger equation.

</td>
<td>

**演示。** 麦克斯韦方程组同时体现了所有算符。微分形式：∇·E = ρ/ε₀（E 的散度等于电荷密度），∇·B = 0（无磁单极子），∇×E = −∂B/∂t（E 的旋度由变化的 B 驱动），∇×B = μ₀J + μ₀ε₀ ∂E/∂t（B 的旋度由电流与变化的 E 驱动）。在球坐标中，∇² = (1/r²) ∂/∂r(r² ∂/∂r) + (1/r² sin θ) ∂/∂θ(sin θ ∂/∂θ) + (1/r² sin²θ) ∂²/∂φ²，这是氢原子薛定谔方程所需的形式。

</td>
</tr>
<tr>
<td>

**Application.** Gauss's law in integral form — ∮ E·dA = Q_enc/ε₀ — follows from the divergence theorem applied to ∇·E = ρ/ε₀, and it is the standard route to the Coulomb field of a point charge (Module 1.8). Stokes' theorem relates Faraday's law in integral and differential form (Module 1.10). The Laplacian ∇²φ = 0 is Laplace's equation for the electrostatic potential in charge-free regions (Module 1.8).

</td>
<td>

**应用。** 积分形式的高斯定律——∮ E·dA = Q_enc/ε₀——由散度定理作用于 ∇·E = ρ/ε₀ 得出，是推导点电荷库仑场的标准途径（模块 1.8）。斯托克斯定理联系了法拉第定律的积分形式与微分形式（模块 1.10）。拉普拉斯方程 ∇²φ = 0 是无电荷区域静电势满足的方程（模块 1.8）。

</td>
</tr>
</table>

---

## 2. Tensors & Index Notation · 张量与指标记号

<table>
<tr><th>English</th><th>中文</th></tr>
<tr>
<td>

**Definition.** A **scalar** is a rank-0 tensor (one component), a **vector** is rank-1 (one index), and a general **tensor** T^{μν} is rank-2 (two indices, transforming as a product of two vectors under coordinate changes). **Einstein summation convention**: a repeated index — one upper, one lower — is summed over all values, e.g. A^μ B_μ = Σ_μ A^μ B_μ.

The **metric tensor** g_{μν} encodes the geometry of the space: the invariant interval (distance) between two nearby events is ds² = g_{μν} dx^μ dx^ν. In flat spacetime with signature (−,+,+,+), g_{μν} = diag(−1, 1, 1, 1) (the Minkowski metric η_{μν}). The metric **raises and lowers indices**: V_μ = g_{μν} V^ν, so it converts between contravariant (upper) and covariant (lower) components.

**Differential forms** give an index-free, coordinate-independent framework: a p-form is an antisymmetric rank-p covariant tensor. The exterior derivative d maps p-forms to (p+1)-forms and satisfies d² = 0 — a generalization of ∇×(∇f) = 0 and ∇·(∇×F) = 0. Maxwell's equations in this language compress to dF = 0 and d★F = J, where F is the 2-form Faraday tensor and ★ is the Hodge dual.

</td>
<td>

**定义。** **标量**是 0 阶张量（一个分量），**向量**是 1 阶张量（一个指标），一般**张量** T^{μν} 是 2 阶张量（两个指标，在坐标变换下按两个向量之积变换）。**爱因斯坦求和约定**：重复出现一次上标一次下标的指标对所有值求和，如 A^μ B_μ = Σ_μ A^μ B_μ。

**度规张量** g_{μν} 编码了空间的几何：两个相邻事件之间的不变间隔（距离）为 ds² = g_{μν} dx^μ dx^ν。在符号为 (−,+,+,+) 的平直时空中，g_{μν} = diag(−1, 1, 1, 1)（闵可夫斯基度规 η_{μν}）。度规**升降指标**：V_μ = g_{μν} V^ν，从而在逆变（上标）与协变（下标）分量之间相互转换。

**微分形式**提供了一种无指标、坐标无关的框架：p-形式是反对称的 p 阶协变张量。外微分算符 d 将 p-形式映射为 (p+1)-形式，且满足 d² = 0——这是 ∇×(∇f) = 0 与 ∇·(∇×F) = 0 的推广。麦克斯韦方程组在这种语言中压缩为 dF = 0 和 d★F = J，其中 F 是 2-形式法拉第张量，★ 是霍奇对偶。

</td>
</tr>
<tr>
<td>

**Demonstration.** In special relativity, the four-momentum is p^μ = (E/c, pₓ, p_y, p_z). Its Lorentz-invariant magnitude is p^μ p_μ = g_{μν} p^μ p^ν = −E²/c² + |p|² = −(mc)², recovering E² = (pc)² + (mc²)² — an entirely index-based derivation.

</td>
<td>

**演示。** 在狭义相对论中，四动量为 p^μ = (E/c, pₓ, p_y, p_z)。其洛伦兹不变的大小为 p^μ p_μ = g_{μν} p^μ p^ν = −E²/c² + |p|² = −(mc)²，从而还原出 E² = (pc)² + (mc²)²——这是一个完全基于指标的推导。

</td>
</tr>
<tr>
<td>

**Application.** Vector calculus (∇, ∇·, ∇×) is the language of all classical electromagnetism in Modules 1.8–1.11. Tensor index notation and the metric g_{μν} are indispensable for covariant electrodynamics (Module 1.15) and are the entire technical foundation of general relativity (Phase 7), where g_{μν} becomes dynamical — the field itself. Differential forms give the most compact statement of Maxwell's equations and appear in the geometric formulation of gauge theories (Phase 6).

</td>
<td>

**应用。** 向量微积分（∇, ∇·, ∇×）是模块 1.8–1.11 中全部经典电磁学的语言。张量指标记号与度规 g_{μν} 对协变电动力学（模块 1.15）不可或缺，并且是广义相对论（第 7 阶段）的全部技术基础——在那里，g_{μν} 成为动力学量，即场本身。微分形式给出麦克斯韦方程组最紧凑的表述，并出现在规范理论的几何形式中（第 6 阶段）。

</td>
</tr>
</table>

---

## Module 0.6 Self-Test (blank page) · 模块 0.6 自测（空白页）

<table>
<tr><th>English</th><th>中文</th></tr>
<tr>
<td>

1. State the physical meaning of ∇·F and ∇×F; give one Maxwell equation illustrating each.
2. State the divergence theorem and Stokes' theorem; explain which Maxwell equation each converts between integral and differential form.
3. Write the Laplacian in spherical coordinates and identify where it appears in the hydrogen-atom Schrödinger equation.
4. Define the Einstein summation convention; write the invariant interval ds² using g_{μν}.
5. Show that p^μ p_μ = −(mc)² for a relativistic particle and interpret the result.
6. State what a differential form is and what d² = 0 generalizes.

</td>
<td>

1. 叙述 ∇·F 和 ∇×F 的物理意义；各举一条麦克斯韦方程加以说明。
2. 叙述散度定理和斯托克斯定理；解释各自将哪条麦克斯韦方程的积分形式与微分形式相互转换。
3. 写出球坐标中的拉普拉斯算符，并指出它在氢原子薛定谔方程中出现的位置。
4. 定义爱因斯坦求和约定；用 g_{μν} 写出不变间隔 ds²。
5. 证明相对论性粒子满足 p^μ p_μ = −(mc)²，并解释其物理意义。
6. 叙述微分形式的定义，以及 d² = 0 所推广的是什么。

</td>
</tr>
</table>

---

← Previous: [Module 0.5 — Fourier Analysis & Probability](./module-0.5-fourier-analysis-and-probability.md) · [Phase 0 index](./README.md)

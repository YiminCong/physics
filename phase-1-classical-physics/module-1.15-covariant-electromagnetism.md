# Module 1.15 — Covariant Electromagnetism
**模块 1.15 — 协变电磁学**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.15-covariant-electromagnetism-derivations.md)

---

## 1. The Four-Potential and the Field Tensor · 四矢量势与场张量

**Definition.** The scalar potential $\varphi$ and vector potential $\mathbf{A}$ (Module 1.10) combine into the **four-potential**:

**定义。** 标量势 $\varphi$ 和矢量势 $\mathbf{A}$（模块 1.10）合并为**四矢量势**：

$$ A^\mu = (\varphi/c,\, A_x,\, A_y,\, A_z). $$

The **gauge transformation** $A^\mu \to A^\mu + \partial^\mu \chi$ (where $\partial^\mu = (\partial_t/c,\, -\nabla)$) leaves all physical fields unchanged — the covariant statement of gauge invariance. From $A^\mu$ one constructs the **electromagnetic field tensor** (an antisymmetric rank-2 tensor):

**规范变换** $A^\mu \to A^\mu + \partial^\mu \chi$（其中 $\partial^\mu = (\partial_t/c,\, -\nabla)$）不改变任何物理场——这是规范不变性的协变表述。由 $A^\mu$ 构造**电磁场张量**（反对称 2 阶张量）：

$$ F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu. $$

Its components are: $F^{0i} = E_i/c$ and $F^{ij} = -\varepsilon_{ijk} B_k$. Explicitly, the six independent components of $F^{\mu\nu}$ encode all three components of $\mathbf{E}$ and all three of $\mathbf{B}$ — the electric and magnetic fields are not separate objects but two faces of a single relativistic entity.

其分量为：$F^{0i} = E_i/c$，$F^{ij} = -\varepsilon_{ijk} B_k$。具体地，$F^{\mu\nu}$ 的六个独立分量编码了 $\mathbf{E}$ 的全部三个分量和 $\mathbf{B}$ 的全部三个分量——电场和磁场不是独立的对象，而是单一相对论实体的两个侧面。

**Demonstration.** Under a Lorentz boost with velocity $v$ along the $x$-axis, the field tensor transforms as $F^{\mu\nu} \to \Lambda^\mu{}_\alpha \Lambda^\nu{}_\beta F^{\alpha\beta}$. Reading off the components: $E_x' = E_x$ (parallel component unchanged), $E_y' = \gamma(E_y - vB_z)$, $E_z' = \gamma(E_z + vB_y)$, $B_x' = B_x$, $B_y' = \gamma(B_y + vE_z/c^2)$, $B_z' = \gamma(B_z - vE_y/c^2)$. A purely electric field in one frame (e.g. the Coulomb field of a charge at rest) acquires a magnetic component in a frame where the charge is moving — magnetism is a relativistic effect of electricity.

**演示。** 在沿 $x$ 轴以速度 $v$ 的洛伦兹变换下，场张量变换为 $F^{\mu\nu} \to \Lambda^\mu{}_\alpha \Lambda^\nu{}_\beta F^{\alpha\beta}$。读出各分量：$E_x' = E_x$（平行分量不变），$E_y' = \gamma(E_y - vB_z)$，$E_z' = \gamma(E_z + vB_y)$，$B_x' = B_x$，$B_y' = \gamma(B_y + vE_z/c^2)$，$B_z' = \gamma(B_z - vE_y/c^2)$。在某参考系中纯粹的电场（例如静止电荷的库仑场），在电荷运动的参考系中获得磁场分量——磁性是电性的相对论效应。

**Application.** Two Lorentz scalars are built from $F^{\mu\nu}$: $F^{\mu\nu} F_{\mu\nu} = 2(B^2 - E^2/c^2)$ and $\varepsilon_{\mu\nu\rho\sigma} F^{\mu\nu} F^{\rho\sigma} \propto \mathbf{E} \cdot \mathbf{B}$. These are invariant under all Lorentz transformations and appear in the electromagnetic Lagrangian density $\mathcal{L}_\text{EM} = -(1/4\mu_0) F^{\mu\nu} F_{\mu\nu}$, which quantised gives QED (Phase 8).

**应用。** 由 $F^{\mu\nu}$ 构造两个洛伦兹标量：$F^{\mu\nu} F_{\mu\nu} = 2(B^2 - E^2/c^2)$ 和 $\varepsilon_{\mu\nu\rho\sigma} F^{\mu\nu} F^{\rho\sigma} \propto \mathbf{E} \cdot \mathbf{B}$。它们在所有洛伦兹变换下不变，出现在电磁拉格朗日密度 $\mathcal{L}_\text{EM} = -(1/4\mu_0) F^{\mu\nu} F_{\mu\nu}$ 中，量子化后给出量子电动力学（第 8 阶段）。

## 2. Maxwell's Equations in Covariant Form · 协变形式的麦克斯韦方程组

**Definition.** The full set of Maxwell's equations compresses into two covariant equations. The **inhomogeneous equations** (Gauss electric + Ampère–Maxwell) become:

**定义。** 完整的麦克斯韦方程组压缩为两个协变方程。**非齐次方程**（高斯电场方程 + 安培–麦克斯韦方程）变为：

$$ \partial_\mu F^{\mu\nu} = \mu_0 J^\nu, $$

where $J^\nu = (c\rho,\, \mathbf{J})$ is the **four-current** and $\partial_\mu = (\partial_t/c,\, \nabla)$. The **homogeneous equations** (Gauss magnetic + Faraday), which follow automatically from $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$, are:

其中 $J^\nu = (c\rho,\, \mathbf{J})$ 是**四电流**，$\partial_\mu = (\partial_t/c,\, \nabla)$。**齐次方程**（高斯磁场方程 + 法拉第方程）由 $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$ 自动得出：

$$ \partial_\mu \tilde{F}^{\mu\nu} = 0, \qquad \text{where } \tilde{F}^{\mu\nu} = \tfrac12 \varepsilon^{\mu\nu\rho\sigma} F_{\rho\sigma} \text{ is the dual tensor.} $$

Charge conservation $\partial_\mu J^\mu = 0$ follows from the antisymmetry of $F^{\mu\nu}$: $\partial_\nu \partial_\mu F^{\mu\nu} = 0$ automatically. In the Lorenz gauge $\partial_\mu A^\mu = 0$, the inhomogeneous Maxwell equation becomes $\Box^2 A^\nu = \mu_0 J^\nu$.

电荷守恒 $\partial_\mu J^\mu = 0$ 由 $F^{\mu\nu}$ 的反对称性自动得出：$\partial_\nu \partial_\mu F^{\mu\nu} = 0$。在洛伦兹规范 $\partial_\mu A^\mu = 0$ 下，非齐次麦克斯韦方程变为 $\Box^2 A^\nu = \mu_0 J^\nu$。

**Demonstration.** In a region with $J^\nu = 0$, the equation $\partial_\mu F^{\mu\nu} = 0$ with Lorenz gauge gives $\Box^2 A^\nu = 0$ — the wave equation for each component of the four-potential. The solution $A^\nu \propto \varepsilon^\nu e^{ik_\mu x^\mu}$ with $k^\mu k_\mu = 0$ (null four-vector) represents a photon with polarisation four-vector $\varepsilon^\mu$. The condition $k \cdot \varepsilon = 0$ (from the Lorenz gauge) removes one polarisation degree of freedom; a further gauge freedom removes a second, leaving the two physical transverse polarisations of Module 1.11.

**演示。** 在 $J^\nu = 0$ 的区域，方程 $\partial_\mu F^{\mu\nu} = 0$ 配合洛伦兹规范给出 $\Box^2 A^\nu = 0$——四矢量势各分量的波动方程。解 $A^\nu \propto \varepsilon^\nu e^{ik_\mu x^\mu}$（其中 $k^\mu k_\mu = 0$，零四矢量）代表具有偏振四矢量 $\varepsilon^\mu$ 的光子。条件 $k \cdot \varepsilon = 0$（来自洛伦兹规范）去掉一个偏振自由度；进一步的规范自由度再去掉一个，保留模块 1.11 的两个物理横向偏振。

**Application.** Covariant electromagnetism is the prototype of a **relativistic gauge field theory**. The pattern — an antisymmetric field tensor $F^{\mu\nu}$ derived from a gauge potential $A^\mu$, with field equations $\partial_\mu F^{\mu\nu} = J^\nu$ — is the template for: QED (replace $U(1)$ gauge group, add quantum fields, Phase 8.2); the Yang–Mills theories of the weak and strong force (replace $U(1)$ with $SU(2)$ and $SU(3)$, Phase 8.1); and canonical field quantisation (Module 6.5). The electromagnetic field tensor $F_{\mu\nu}$ and its action $-\tfrac14 F^{\mu\nu} F_{\mu\nu}$ are the starting point that the entire Standard Model generalises.

**应用。** 协变电磁学是**相对论规范场论**的原型。其模式——由规范势 $A^\mu$ 推导出反对称场张量 $F^{\mu\nu}$，场方程为 $\partial_\mu F^{\mu\nu} = J^\nu$——是以下理论的模板：量子电动力学（替换 $U(1)$ 规范群，加入量子场，第 8.2 阶段）；弱力和强力的杨–米尔斯理论（将 $U(1)$ 替换为 $SU(2)$ 和 $SU(3)$，第 8.1 阶段）；以及正则场量子化（模块 6.5）。电磁场张量 $F_{\mu\nu}$ 及其作用量 $-\tfrac14 F^{\mu\nu} F_{\mu\nu}$ 是整个标准模型推广的出发点。

## Key results · 核心结果

- Four-potential $A^\mu=(\varphi/c,\mathbf A)$; field tensor $F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu$ · 四势与场强张量
- $\mathbf E$ and $\mathbf B$ are components of $F^{\mu\nu}$ · $E,B$ 为 $F^{\mu\nu}$ 分量
- Covariant Maxwell $\partial_\mu F^{\mu\nu}=\mu_0 J^\nu$ · 协变麦克斯韦方程
- Invariants $F_{\mu\nu}F^{\mu\nu}\propto B^2-E^2/c^2$ and $F_{\mu\nu}\tilde F^{\mu\nu}\propto\mathbf E\cdot\mathbf B$ · 两个洛伦兹不变量

---

**Self-test (blank page)**

1. Write down the four-potential $A^\mu$ and the field tensor $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$. Show how $\mathbf{E}$ and $\mathbf{B}$ are encoded in the components of $F^{\mu\nu}$.
2. Apply the Lorentz transformation of $F^{\mu\nu}$ to find $\mathbf{E}'$ and $\mathbf{B}'$ for a charge $q$ at rest in frame $S$. Verify that in frame $S'$ (moving at velocity $v$ relative to $S$), the transformed $\mathbf{B}'$ matches the Biot–Savart result for a moving charge.
3. Write Maxwell's inhomogeneous equations in covariant form $\partial_\mu F^{\mu\nu} = \mu_0 J^\nu$ and expand the $\nu = 0$ and $\nu = 1$ components explicitly to recover the familiar 3D Maxwell equations.
4. What are the two independent Lorentz scalars constructed from $F^{\mu\nu}$? What are their physical meanings, and why must they be invariant?

**自测（空白页）**

1. 写出四矢量势 $A^\mu$ 和场张量 $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$。展示 $\mathbf{E}$ 和 $\mathbf{B}$ 如何编码在 $F^{\mu\nu}$ 的分量中。
2. 对静止在 $S$ 系中的电荷 $q$，应用 $F^{\mu\nu}$ 的洛伦兹变换求 $\mathbf{E}'$ 和 $\mathbf{B}'$。验证在 $S'$ 系（相对 $S$ 以速度 $v$ 运动）中，变换后的 $\mathbf{B}'$ 与运动电荷的毕奥–萨伐尔结果一致。
3. 写出协变形式的麦克斯韦非齐次方程 $\partial_\mu F^{\mu\nu} = \mu_0 J^\nu$，并展开 $\nu = 0$ 和 $\nu = 1$ 分量以恢复熟悉的三维麦克斯韦方程。
4. 由 $F^{\mu\nu}$ 构造的两个独立洛伦兹标量是什么？它们的物理意义是什么？为什么它们必须是不变的？

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** $A^\mu=(\varphi/c,\mathbf A)$; $F^{0i}=E_i/c$ (time–space components) and $F^{ij}=-\varepsilon_{ijk}B_k$ (space–space). · $E$ 在时空分量,$B$ 在空间分量。
**2.** Boosting the static-charge $F^{\mu\nu}$: $\mathbf E'_\parallel$ unchanged, $\mathbf E'_\perp$ enhanced by $\gamma$, and $\mathbf B'=-(\mathbf v/c^2)\times\mathbf E'$ — the Biot–Savart field of a moving charge. · 变换给运动电荷的 $\mathbf B'$。
**3.** $\partial_\mu F^{\mu\nu}=\mu_0 J^\nu$: $\nu=0\Rightarrow\nabla\cdot\mathbf E=\rho/\epsilon_0$; $\nu=i\Rightarrow\nabla\times\mathbf B-\tfrac1{c^2}\partial_t\mathbf E=\mu_0\mathbf J$. · 展开得高斯与安培定律。
**4.** $F_{\mu\nu}F^{\mu\nu}\propto B^2-E^2/c^2$ and $F_{\mu\nu}\tilde F^{\mu\nu}\propto\mathbf E\cdot\mathbf B$; both are frame-independent, so e.g. a pure light wave has both invariants zero in every frame. · 两不变量在所有参考系相同。

</details>

---

← Previous: [Module 1.14 — Relativistic Dynamics & E = mc²](./module-1.14-relativistic-dynamics-energy-momentum.md) · [Phase 1 index](./README.md) · Next: [Module 1.16 — Mechanical Waves & Acoustics](./module-1.16-mechanical-waves-acoustics.md) →

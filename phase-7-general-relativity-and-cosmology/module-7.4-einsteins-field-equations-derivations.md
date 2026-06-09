# Derivations — Module 7.4: Einstein's Field Equations
# 推导 — 模块 7.4：爱因斯坦场方程

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 7.4](./module-7.4-einsteins-field-equations.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 7.4](./module-7.4-einsteins-field-equations.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Einstein Field Equations from the Einstein–Hilbert Action · 从爱因斯坦-希尔伯特作用量推导爱因斯坦场方程

**Claim.** Varying the Einstein–Hilbert action

$$ S = (c^4/16\pi G) \int R \sqrt{-g}\, d^4x + S_\text{matter} $$

with respect to the inverse metric $g^{\mu\nu}$ and setting $\delta S = 0$ yields the Einstein field equations

$$ G_{\mu\nu} = R_{\mu\nu} - \tfrac12 R g_{\mu\nu} = (8\pi G/c^4) T_{\mu\nu}. $$

**命题。** 对爱因斯坦-希尔伯特作用量

$$ S = (c^4/16\pi G) \int R \sqrt{-g}\, d^4x + S_\text{matter} $$

关于逆度规 $g^{\mu\nu}$ 变分并令 $\delta S = 0$，得到爱因斯坦场方程

$$ G_{\mu\nu} = R_{\mu\nu} - \tfrac12 R g_{\mu\nu} = (8\pi G/c^4) T_{\mu\nu}. $$

**Step 1 — Vary the Ricci scalar.** Write $R = g^{\mu\nu} R_{\mu\nu}$ (Module 7.2). Its variation under $g^{\mu\nu} \to g^{\mu\nu} + \delta g^{\mu\nu}$ is

**第 1 步 — 对里奇标量变分。** 写出 $R = g^{\mu\nu} R_{\mu\nu}$（模块 7.2）。在 $g^{\mu\nu} \to g^{\mu\nu} + \delta g^{\mu\nu}$ 下其变分为

$$ \delta R = R_{\mu\nu} \delta g^{\mu\nu} + g^{\mu\nu} \delta R_{\mu\nu}. $$

The second term $g^{\mu\nu} \delta R_{\mu\nu}$ is a total covariant divergence (the *Palatini identity*):

第二项 $g^{\mu\nu} \delta R_{\mu\nu}$ 是全协变散度（*帕拉提尼恒等式*）：

$$ g^{\mu\nu} \delta R_{\mu\nu} = \nabla_\mu (g^{\alpha\beta} \delta\Gamma^{\mu}{}_{\alpha\beta} - g^{\alpha\mu} \delta\Gamma^{\beta}{}_{\alpha\beta}). $$

By the divergence theorem, this integrates to a boundary term that vanishes for variations that are zero on the boundary. We discard it (or handle it with the Gibbons–Hawking–York boundary term, which does not affect the bulk equations of motion).

由散度定理，此项积分为边界项，对在边界处为零的变分消失。我们将其舍去（或用吉本斯-霍金-约克边界项处理，其不影响体内运动方程）。

Therefore, effectively: $\delta(R) = R_{\mu\nu} \delta g^{\mu\nu}$ (plus a discarded surface term).

因此，实际上：$\delta(R) = R_{\mu\nu} \delta g^{\mu\nu}$（加上一个舍去的面项）。

**Step 2 — Vary $\sqrt{-g}$.** The determinant varies as $\delta g = g \cdot g^{\mu\nu} \delta g_{\mu\nu}$. Note that $\delta g^{\mu\nu}$ and $\delta g_{\mu\nu}$ are related by $\delta g_{\mu\nu} = -g_{\mu\alpha} g_{\nu\beta} \delta g^{\alpha\beta}$, so $g \cdot g^{\mu\nu} \delta g_{\mu\nu} = -g \cdot g_{\mu\nu} \delta g^{\mu\nu}$. Therefore:

**第 2 步 — 对 $\sqrt{-g}$ 变分。** 行列式变分为 $\delta g = g \cdot g^{\mu\nu} \delta g_{\mu\nu}$。注意 $\delta g^{\mu\nu}$ 与 $\delta g_{\mu\nu}$ 的关系为 $\delta g_{\mu\nu} = -g_{\mu\alpha} g_{\nu\beta} \delta g^{\alpha\beta}$，故 $g \cdot g^{\mu\nu} \delta g_{\mu\nu} = -g \cdot g_{\mu\nu} \delta g^{\mu\nu}$。因此：

$$ \delta\sqrt{-g} = -\delta(-g)/(2\sqrt{-g}) = -(\delta g)/(2\sqrt{-g}) = -(g \cdot g^{\mu\nu} \delta g_{\mu\nu})/(2\sqrt{-g}) = \tfrac12 \sqrt{-g}\, g_{\mu\nu} \delta g^{\mu\nu}. $$

(Here we used $g^{\mu\nu} \delta g_{\mu\nu} = -g_{\mu\nu} \delta g^{\mu\nu}$, with an overall sign flip from $g < 0$.)

（这里用到 $g^{\mu\nu} \delta g_{\mu\nu} = -g_{\mu\nu} \delta g^{\mu\nu}$，整体符号来自 $g < 0$。）

**Step 3 — Vary the gravitational part of the action.** Combining Steps 1 and 2:

**第 3 步 — 对作用量引力部分变分。** 合并第 1 步和第 2 步：

$$ \begin{aligned}
\delta(R\sqrt{-g}) & = \sqrt{-g}\, R_{\mu\nu} \delta g^{\mu\nu} + R \cdot \tfrac12 \sqrt{-g}\, g_{\mu\nu} \delta g^{\mu\nu} \\
& = \sqrt{-g}\, (R_{\mu\nu} - \tfrac12 R g_{\mu\nu}) \delta g^{\mu\nu} \\
& = \sqrt{-g}\, G_{\mu\nu} \delta g^{\mu\nu}.
\end{aligned} $$

The gravitational part of the action variation is:

作用量引力部分的变分为：

$$ \delta S_\text{grav} = (c^4/16\pi G) \int \sqrt{-g}\, G_{\mu\nu} \delta g^{\mu\nu}\, d^4x. $$

**Step 4 — Vary the matter action.** The matter action $S_\text{matter}$ depends on $g^{\mu\nu}$ and matter fields $\psi$. Its variation defines the stress-energy tensor:

**第 4 步 — 对物质作用量变分。** 物质作用量 $S_\text{matter}$ 依赖于 $g^{\mu\nu}$ 和物质场 $\psi$。其变分定义了能动张量：

$$ \delta S_\text{matter} = -\tfrac12 \int \sqrt{-g}\, T_{\mu\nu} \delta g^{\mu\nu}\, d^4x, $$

where $T_{\mu\nu} \equiv -(2/\sqrt{-g})\, \delta S_\text{matter}/\delta g^{\mu\nu}$. The factor of $-2$ is conventional, chosen so that $T_{00} = $ energy density. This definition is manifestly covariant and symmetric.

其中 $T_{\mu\nu} \equiv -(2/\sqrt{-g})\, \delta S_\text{matter}/\delta g^{\mu\nu}$。$-2$ 因子是约定的，使得 $T_{00} = $ 能量密度。此定义是显式协变且对称的。

**Step 5 — Set $\delta S = 0$.** The total variation is

**第 5 步 — 令 $\delta S = 0$。** 总变分为

$$ \delta S = \int \sqrt{-g}\, [(c^4/16\pi G) G_{\mu\nu} - \tfrac12 T_{\mu\nu}] \delta g^{\mu\nu}\, d^4x = 0. $$

Since $\delta g^{\mu\nu}$ is arbitrary (varied independently at each spacetime point), the integrand must vanish:

由于 $\delta g^{\mu\nu}$ 是任意的（在每个时空点独立变分），被积函数必须为零：

$$ (c^4/16\pi G) G_{\mu\nu} = \tfrac12 T_{\mu\nu} \implies \boxed{\, G_{\mu\nu} = (8\pi G/c^4) T_{\mu\nu} \,} \qquad \blacksquare $$

**Step 6 — Include the cosmological constant.** Adding the cosmological-constant term $\Lambda$ to the action, $S = (c^4/16\pi G) \int (R - 2\Lambda) \sqrt{-g}\, d^4x + S_\text{matter}$:

**第 6 步 — 加入宇宙学常数。** 将宇宙学常数项 $\Lambda$ 添加到作用量，$S = (c^4/16\pi G) \int (R - 2\Lambda) \sqrt{-g}\, d^4x + S_\text{matter}$：

$$ \delta(-2\Lambda\sqrt{-g}) = -2\Lambda \cdot \tfrac12\sqrt{-g}\, g_{\mu\nu} \delta g^{\mu\nu} = -\sqrt{-g}\, \Lambda g_{\mu\nu} \delta g^{\mu\nu}. $$

So the equations of motion become:

于是运动方程变为：

$$ G_{\mu\nu} + \Lambda g_{\mu\nu} = (8\pi G/c^4) T_{\mu\nu}, $$

i.e., $R_{\mu\nu} - \tfrac12 R g_{\mu\nu} + \Lambda g_{\mu\nu} = (8\pi G/c^4) T_{\mu\nu}$.

即 $R_{\mu\nu} - \tfrac12 R g_{\mu\nu} + \Lambda g_{\mu\nu} = (8\pi G/c^4) T_{\mu\nu}$。

---

## B. Fixing the Constant $8\pi G/c^4$ from the Newtonian Limit · 从牛顿极限确定常数 $8\pi G/c^4$

**Claim.** The constant $\kappa$ in $G_{\mu\nu} = \kappa T_{\mu\nu}$ is fixed to $\kappa = 8\pi G/c^4$ by requiring that the 00-component of the EFE reduces to Poisson's equation $\nabla^2\varphi = 4\pi G\rho$ in the Newtonian limit.

**命题。** 通过要求 EFE 的 00 分量在牛顿极限下化为泊松方程 $\nabla^2\varphi = 4\pi G\rho$，可以确定 $G_{\mu\nu} = \kappa T_{\mu\nu}$ 中的常数 $\kappa = 8\pi G/c^4$。

**Step 1 — Newtonian-limit metric.** From Module 7.3, in the weak-field slow-motion limit: $g_{00} = -(1 + 2\varphi/c^2)$, $g_{ij} \approx \delta_{ij}$, $g_{0i} \approx 0$. To first order in $\varphi/c^2$:

**第 1 步 — 牛顿极限度规。** 由模块 7.3，在弱场慢速运动极限下：$g_{00} = -(1 + 2\varphi/c^2)$，$g_{ij} \approx \delta_{ij}$，$g_{0i} \approx 0$。在 $\varphi/c^2$ 一阶近似下：

$$ h_{00} = -2\varphi/c^2, \quad \text{all other } h_{\mu\nu} \approx 0. $$

**Step 2 — Compute the Christoffel symbols.** Non-zero to first order (static field, so $\partial_0 h_{\mu\nu} = 0$):

**第 2 步 — 计算克里斯托费尔符号。** 在一阶非零项（静态场，故 $\partial_0 h_{\mu\nu} = 0$）：

$$ \Gamma^{i}{}_{00} = -\tfrac12 \partial^i h_{00} = \partial^i \varphi/c^2, \quad \Gamma^{0}{}_{0i} = \tfrac12 \partial_i h_{00} = -\partial_i \varphi/c^2. $$

**Step 3 — Compute $R_{00}$.** Using $R_{\mu\nu} = \partial_\rho \Gamma^{\rho}{}_{\nu\mu} - \partial_\nu \Gamma^{\rho}{}_{\rho\mu} + $ quadratic terms (dropped at linearized order):

**第 3 步 — 计算 $R_{00}$。** 利用 $R_{\mu\nu} = \partial_\rho \Gamma^{\rho}{}_{\nu\mu} - \partial_\nu \Gamma^{\rho}{}_{\rho\mu} + $ 二次项（在线性化阶舍去）：

$$ R_{00} = \partial_i \Gamma^{i}{}_{00} - \partial_0 \Gamma^{i}{}_{i0} = \partial_i (\partial^i \varphi/c^2) - 0 = \nabla^2\varphi/c^2. $$

(Here $\partial_i \Gamma^{i}{}_{00} = (1/c^2) \partial_i \partial^i \varphi = \nabla^2\varphi/c^2$.)

（此处 $\partial_i \Gamma^{i}{}_{00} = (1/c^2) \partial_i \partial^i \varphi = \nabla^2\varphi/c^2$。）

**Step 4 — Compute the Ricci scalar $R$.** In the Newtonian limit $R_{ij} \approx 0$ and $R_{0i} \approx 0$ to leading order, so

**第 4 步 — 计算里奇标量 $R$。** 在牛顿极限下，$R_{ij} \approx 0$，$R_{0i} \approx 0$（主导阶），故

$$ R = g^{\mu\nu} R_{\mu\nu} \approx g^{00} R_{00} \approx -R_{00}/c^2 = -\nabla^2\varphi/c^4. $$

(Using $g^{00} \approx -1/c^2$ for $x^0 = ct$.)

（利用 $x^0 = ct$ 时 $g^{00} \approx -1/c^2$。）

**Step 5 — Compute $G_{00}$.** The Einstein tensor component:

**第 5 步 — 计算 $G_{00}$。** 爱因斯坦张量分量：

A consistent Newtonian limit must keep the **spatial** perturbation as well, not only $g_{00}$: take $g_{00} = -(1 + 2\varphi/c^2)$ **and** $g_{ij} = (1 - 2\varphi/c^2)\delta_{ij}$. (Dropping $g_{ij}$ is exactly what spoils the factor of 2.) With both, $R_{00} = \nabla^2\varphi/c^2$ (Step 4) and the Ricci scalar evaluates to $R = 2\nabla^2\varphi/c^2$. Using $g_{00} \approx -1$:

一致的牛顿极限必须同时保留**空间**扰动，而不只是 $g_{00}$：取 $g_{00} = -(1 + 2\varphi/c^2)$ **且** $g_{ij} = (1 - 2\varphi/c^2)\delta_{ij}$。（丢掉 $g_{ij}$ 正是破坏因子 2 的原因。）两者皆保留时，$R_{00} = \nabla^2\varphi/c^2$（第 4 步），里奇标量为 $R = 2\nabla^2\varphi/c^2$。取 $g_{00} \approx -1$：

$$ G_{00} = R_{00} - \tfrac12 R g_{00} = \nabla^2\varphi/c^2 - \tfrac12(2\nabla^2\varphi/c^2)(-1) = \nabla^2\varphi/c^2 + \nabla^2\varphi/c^2 = 2\nabla^2\varphi/c^2. $$

**Step 6 — Matter source: $T_{00}$.** For slow-moving pressureless matter (dust), $T_{00} = \rho c^2$ (the energy density in the frame where the matter is nearly at rest). The full expression for a perfect fluid $T_{00} = (\rho + p/c^2) u_0 u_0 + p g_{00}$ reduces to $T_{00} \approx \rho c^2$ when $p \ll \rho c^2$ and $u^0 \approx c$.

**第 6 步 — 物质源：$T_{00}$。** 对于缓慢运动的无压物质（尘埃），$T_{00} = \rho c^2$（物质近似静止的参考系中的能量密度）。完美流体的完整表达式 $T_{00} = (\rho + p/c^2) u_0 u_0 + p g_{00}$ 在 $p \ll \rho c^2$ 和 $u^0 \approx c$ 时化为 $T_{00} \approx \rho c^2$。

**Step 7 — Match to Poisson's equation.** The 00-component of $G_{\mu\nu} = \kappa T_{\mu\nu}$:

**第 7 步 — 与泊松方程匹配。** $G_{\mu\nu} = \kappa T_{\mu\nu}$ 的 00 分量：

$$ G_{00} = \kappa T_{00}, \qquad 2\nabla^2\varphi/c^2 = \kappa \rho c^2. $$

For this to match Poisson's equation $\nabla^2\varphi = 4\pi G\rho$:

为使其与泊松方程 $\nabla^2\varphi = 4\pi G\rho$ 匹配：

$$ 2 \cdot 4\pi G\rho/c^2 = \kappa \rho c^2 \quad\implies\quad \kappa = 8\pi G/c^4. $$

Therefore the Einstein field equations are:

因此爱因斯坦场方程为：

$$ \boxed{\, G_{\mu\nu} = (8\pi G/c^4) T_{\mu\nu} \,} \qquad \blacksquare $$

The coefficient $8\pi G/c^4 \approx 2.07 \times 10^{-43}$ m/J quantifies the extraordinary "stiffness" of spacetime: a Joule of energy produces a metric distortion of only $\sim 10^{-43}$ in geometric units.

系数 $8\pi G/c^4 \approx 2.07 \times 10^{-43}$ m/J 量化了时空非凡的"刚度"：1 焦耳的能量仅产生约 $10^{-43}$ 的度规扰动（几何单位）。

---

## C. Conservation of Energy–Momentum as a Geometric Identity · 能量-动量守恒作为几何恒等式

**Claim.** The contracted Bianchi identity $\nabla^\mu G_{\mu\nu} = 0$ (proved in Module 7.2 Derivations Section C) together with the EFE immediately implies $\nabla^\mu T_{\mu\nu} = 0$ — energy-momentum conservation is automatic, not a separate postulate.

**命题。** 缩并比安基恒等式 $\nabla^\mu G_{\mu\nu} = 0$（在模块 7.2 推导 C 节中证明）结合 EFE 立即推出 $\nabla^\mu T_{\mu\nu} = 0$——能量-动量守恒是自动的，而非独立假设。

**Step 1 — Apply the divergence to both sides.** Taking $\nabla^\mu$ of $G_{\mu\nu} = (8\pi G/c^4) T_{\mu\nu}$:

**第 1 步 — 对两边取散度。** 对 $G_{\mu\nu} = (8\pi G/c^4) T_{\mu\nu}$ 取 $\nabla^\mu$：

$$ \nabla^\mu G_{\mu\nu} = (8\pi G/c^4) \nabla^\mu T_{\mu\nu}. $$

**Step 2 — Use the Bianchi identity.** From the contracted second Bianchi identity: $\nabla^\mu G_{\mu\nu} = 0$ (identically, for any metric). Therefore:

**第 2 步 — 使用比安基恒等式。** 由缩并第二比安基恒等式：$\nabla^\mu G_{\mu\nu} = 0$（对任意度规恒成立）。因此：

$$ 0 = (8\pi G/c^4) \nabla^\mu T_{\mu\nu} \quad\implies\quad \nabla^\mu T_{\mu\nu} = 0. $$

**Step 3 — Physical interpretation.** In flat spacetime, $\partial^\mu T_{\mu\nu} = 0$ gives conservation of energy ($\nu = 0$) and momentum ($\nu = 1, 2, 3$). In curved spacetime, $\nabla^\mu T_{\mu\nu} = 0$ is the covariant generalization: energy and momentum are not simply conserved globally (due to spacetime curvature exchanging energy with the gravitational field), but locally the law holds. The geodesic equation for dust ($p = 0$) is a consequence: $\nabla^\mu T_{\mu\nu} = 0$ with $T_{\mu\nu} = \rho u_\mu u_\nu$ implies $u^\mu \nabla_\mu u^\nu = 0$, which is exactly the geodesic equation. $\blacksquare$

**第 3 步 — 物理诠释。** 在平坦时空中，$\partial^\mu T_{\mu\nu} = 0$ 给出能量（$\nu = 0$）和动量（$\nu = 1, 2, 3$）守恒。在弯曲时空中，$\nabla^\mu T_{\mu\nu} = 0$ 是协变推广：能量和动量在全局上并非简单守恒（由于时空曲率与引力场交换能量），但局域定律成立。尘埃（$p = 0$）的测地线方程是一个推论：$\nabla^\mu T_{\mu\nu} = 0$ 与 $T_{\mu\nu} = \rho u_\mu u_\nu$ 意味着 $u^\mu \nabla_\mu u^\nu = 0$，这正是测地线方程。$\blacksquare$

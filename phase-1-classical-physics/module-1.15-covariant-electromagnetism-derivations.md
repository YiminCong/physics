# Derivations — Module 1.15: Covariant Electromagnetism
# 推导 — 模块 1.15：协变电磁学

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.15](./module-1.15-covariant-electromagnetism.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.15](./module-1.15-covariant-electromagnetism.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Building the Field Tensor $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ · 构造场张量

**Claim.** The antisymmetric rank-2 tensor $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$, formed from the four-potential $A^\mu = (\varphi/c, \mathbf{A})$, encodes the electric field $\mathbf{E}$ and magnetic field $\mathbf{B}$ in its components, and is automatically gauge-invariant.

**命题。** 由四矢量势 $A^\mu = (\varphi/c, \mathbf{A})$ 构造的反对称 2 阶张量 $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$，在其分量中编码了电场 $\mathbf{E}$ 和磁场 $\mathbf{B}$，并自动具有规范不变性。

**Step 1 — Conventions and index lowering.** Use the metric signature $\eta_{\mu\nu} = \mathrm{diag}(+1, -1, -1, -1)$ and the coordinate four-vector $x^\mu = (ct, x, y, z)$. The covariant derivative operator is $\partial_\mu = \partial/\partial x^\mu = (\partial_t/c, \partial_x, \partial_y, \partial_z)$. The four-potential with lowered index is $A_\mu = \eta_{\mu\nu} A^\nu = (\varphi/c, -A_x, -A_y, -A_z)$.

**第 1 步 — 约定与指标降低。** 采用度规号差 $\eta_{\mu\nu} = \mathrm{diag}(+1, -1, -1, -1)$，坐标四矢量 $x^\mu = (ct, x, y, z)$。协变导数算符为 $\partial_\mu = \partial/\partial x^\mu = (\partial_t/c, \partial_x, \partial_y, \partial_z)$。降低指标后的四矢量势为 $A_\mu = \eta_{\mu\nu} A^\nu = (\varphi/c, -A_x, -A_y, -A_z)$。

**Step 2 — Compute $F_{0i}$ components.** For $\mu = 0$, $\nu = i$ (spatial):

**第 2 步 — 计算 $F_{0i}$ 分量。** 取 $\mu = 0$，$\nu = i$（空间）：

$$ \begin{aligned}
F_{0i} &= \partial_0 A_i - \partial_i A_0 \\
&= (1/c)(\partial A_i/\partial t) - \partial_i (\varphi/c) \qquad [\text{but } A_i = -A^i, \text{ so } \partial_0 A_i = -(1/c)\partial A^i/\partial t] \\
&= -(1/c)(\partial A^i/\partial t) - (1/c)\,\partial\varphi/\partial x^i.
\end{aligned} $$

Recall $\mathbf{E} = -\nabla\varphi - \partial\mathbf{A}/\partial t$, so $E^i = -\partial\varphi/\partial x^i - \partial A^i/\partial t$. Therefore:

回忆 $\mathbf{E} = -\nabla\varphi - \partial\mathbf{A}/\partial t$，故 $E^i = -\partial\varphi/\partial x^i - \partial A^i/\partial t$。因此：

$$ F_{0i} = (1/c)(-\partial A^i/\partial t - \partial\varphi/\partial x^i) = E^i/c. $$

So $F_{0i} = E_i/c$ (with $E_i = E^i$ for Cartesian coordinates).

故 $F_{0i} = E_i/c$（在笛卡尔坐标中 $E_i = E^i$）。

**Step 3 — Compute $F_{ij}$ components.** For $\mu = i$, $\nu = j$ (both spatial):

**第 3 步 — 计算 $F_{ij}$ 分量。** 取 $\mu = i$，$\nu = j$（均为空间）：

$$ F_{ij} = \partial_i A_j - \partial_j A_i = -\partial_i A^j + \partial_j A^i = \partial_j A^i - \partial_i A^j. $$

The magnetic field is $\mathbf{B} = \nabla \times \mathbf{A}$, i.e. $B^k = \varepsilon^{ijk}\,\partial_i A^j$ (with $\varepsilon^{ijk}$ the Levi-Civita symbol). Explicitly:

磁场为 $\mathbf{B} = \nabla \times \mathbf{A}$，即 $B^k = \varepsilon^{ijk}\,\partial_i A^j$（$\varepsilon^{ijk}$ 为列维-奇维塔符号）。明确地：

$$ \begin{aligned}
F_{12} &= \partial_2 A^1 - \partial_1 A^2 = -(\partial_1 A^2 - \partial_2 A^1) = -B^3 = -B_z, \\
F_{13} &= \partial_3 A^1 - \partial_1 A^3 = -(\partial_1 A^3 - \partial_3 A^1) = +B^2 = +B_y, \\
F_{23} &= \partial_3 A^2 - \partial_2 A^3 = -(\partial_2 A^3 - \partial_3 A^2) = -B^1 = -B_x.
\end{aligned} $$

In general $F_{ij} = -\varepsilon_{ijk} B^k$. The explicit matrix of $F_{\mu\nu}$ is:

一般地 $F_{ij} = -\varepsilon_{ijk} B^k$。$F_{\mu\nu}$ 的显式矩阵为：

$$ F_{\mu\nu} = \begin{pmatrix}
0 & E_x/c & E_y/c & E_z/c \\
-E_x/c & 0 & -B_z & B_y \\
-E_y/c & B_z & 0 & -B_x \\
-E_z/c & -B_y & B_x & 0
\end{pmatrix} $$

**Step 4 — Gauge invariance.** Under $A_\mu \to A_\mu + \partial_\mu \chi$ for any scalar field $\chi$:

**第 4 步 — 规范不变性。** 在任意标量场 $\chi$ 的规范变换 $A_\mu \to A_\mu + \partial_\mu \chi$ 下：

$$ \begin{aligned}
F_{\mu\nu} &\to \partial_\mu(A_\nu + \partial_\nu \chi) - \partial_\nu(A_\mu + \partial_\mu \chi) \\
&= F_{\mu\nu} + \partial_\mu \partial_\nu \chi - \partial_\nu \partial_\mu \chi \\
&= F_{\mu\nu} + 0 \qquad (\text{partial derivatives commute}).
\end{aligned} $$

Hence $F_{\mu\nu}$ is gauge-invariant — the physically measurable fields $\mathbf{E}$ and $\mathbf{B}$ do not depend on the choice of gauge. $\blacksquare$

故 $F_{\mu\nu}$ 是规范不变的——可物理测量的场 $\mathbf{E}$ 和 $\mathbf{B}$ 不依赖于规范的选取。$\blacksquare$

---

## B. Transformation of $\mathbf{E}$ and $\mathbf{B}$ Under a Lorentz Boost · 洛伦兹变换下 $\mathbf{E}$ 和 $\mathbf{B}$ 的变换

**Claim.** Under a Lorentz boost with velocity $v$ along the $x$-axis, the fields transform as: $E_x' = E_x$, $E_y' = \gamma(E_y - vB_z)$, $E_z' = \gamma(E_z + vB_y)$, $B_x' = B_x$, $B_y' = \gamma(B_y + vE_z/c^2)$, $B_z' = \gamma(B_z - vE_y/c^2)$.

**命题。** 在沿 $x$ 轴以速度 $v$ 的洛伦兹变换下，场的变换为：$E_x' = E_x$，$E_y' = \gamma(E_y - vB_z)$，$E_z' = \gamma(E_z + vB_y)$，$B_x' = B_x$，$B_y' = \gamma(B_y + vE_z/c^2)$，$B_z' = \gamma(B_z - vE_y/c^2)$。

**Step 1 — The Lorentz boost matrix.** A boost with velocity $v$ along $x$ (with $\beta = v/c$ and $\gamma = 1/\sqrt{1 - \beta^2}$) is

**第 1 步 — 洛伦兹变换矩阵。** 沿 $x$ 轴以速度 $v$ 的变换（$\beta = v/c$，$\gamma = 1/\sqrt{1 - \beta^2}$）为

$$ \Lambda^\mu{}_\nu = \begin{pmatrix}
\gamma & -\gamma\beta & 0 & 0 \\
-\gamma\beta & \gamma & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix} $$

**Step 2 — Tensor transformation law.** A rank-2 covariant tensor transforms as

**第 2 步 — 张量变换法则。** 2 阶协变张量的变换法则为

$$ F'_{\mu\nu} = \Lambda^\alpha{}_\mu \Lambda^\beta{}_\nu F_{\alpha\beta}. $$

We compute each independent component of $F'_{\mu\nu}$.

我们逐一计算 $F'_{\mu\nu}$ 的各独立分量。

**Step 3 — Transform all six field components.**

**第 3 步 — 变换全部六个场分量。**

We work throughout with the **contravariant** tensor $F^{\mu\nu}$, whose components are fixed by Section A: since $F_{0i} = E_i/c$, raising both indices gives $F^{0i} = \eta^{00}\eta^{ii}F_{0i} = -E_i/c$, while $F^{ij} = F_{ij} = -\varepsilon_{ijk}B^k$, i.e. $F^{12} = -B_z$, $F^{13} = +B_y$, $F^{23} = -B_x$. The transformed fields are read off the **same way** on both sides: $F'^{0i} = -E_i'/c$, $F'^{12} = -B_z'$, $F'^{13} = +B_y'$, $F'^{23} = -B_x'$. Taking the primed frame $S'$ to move at velocity $+v$ along $x$, the boost is $\Lambda^0{}_0 = \gamma$, $\Lambda^0{}_1 = \Lambda^1{}_0 = -\gamma\beta$, $\Lambda^1{}_1 = \gamma$, $\Lambda^2{}_2 = \Lambda^3{}_3 = 1$, and a rank-2 contravariant tensor transforms as $F'^{\mu\nu} = \Lambda^\mu{}_\alpha \Lambda^\nu{}_\beta F^{\alpha\beta}$.

全程使用**逆变**张量 $F^{\mu\nu}$，其分量由 A 节固定：因 $F_{0i} = E_i/c$，升两个指标得 $F^{0i} = -E_i/c$，而 $F^{ij} = F_{ij} = -\varepsilon_{ijk}B^k$，即 $F^{12} = -B_z$、$F^{13} = +B_y$、$F^{23} = -B_x$。两边以**相同方式**读出变换后的场：$F'^{0i} = -E_i'/c$、$F'^{12} = -B_z'$、$F'^{13} = +B_y'$、$F'^{23} = -B_x'$。取主系 $S'$ 沿 $x$ 以速度 $+v$ 运动，变换矩阵为 $\Lambda^0{}_0 = \gamma$、$\Lambda^0{}_1 = \Lambda^1{}_0 = -\gamma\beta$、$\Lambda^1{}_1 = \gamma$、$\Lambda^2{}_2 = \Lambda^3{}_3 = 1$，2 阶逆变张量按 $F'^{\mu\nu} = \Lambda^\mu{}_\alpha \Lambda^\nu{}_\beta F^{\alpha\beta}$ 变换。

**Parallel components — $E_x$ and $B_x$ unchanged.** Only the indices $0,1$ mix:

**平行分量——$E_x$ 与 $B_x$ 不变。** 只有指标 $0,1$ 混合：

$$ \begin{aligned}
F'^{01} &= \Lambda^0{}_0 \Lambda^1{}_1 F^{01} + \Lambda^0{}_1 \Lambda^1{}_0 F^{10} = \gamma^2 F^{01} + \gamma^2\beta^2 F^{10} = \gamma^2(1 - \beta^2)F^{01} = F^{01} \implies E_x' = E_x, \\
F'^{23} &= \Lambda^2{}_2 \Lambda^3{}_3 F^{23} = F^{23} \implies B_x' = B_x. \quad\checkmark
\end{aligned} $$

**$E_y'$ (from $F'^{02}$).** Since $\Lambda^2{}_2 = 1$, only $\alpha \in \{0,1\}$ contributes:

**$E_y'$（由 $F'^{02}$）。** 因 $\Lambda^2{}_2 = 1$，只有 $\alpha \in \{0,1\}$ 贡献：

$$ F'^{02} = \Lambda^0{}_0 F^{02} + \Lambda^0{}_1 F^{12} = \gamma(-E_y/c) + (-\gamma\beta)(-B_z) = -\gamma E_y/c + \gamma\beta B_z. $$

Reading $F'^{02} = -E_y'/c$ gives $-E_y'/c = -\gamma E_y/c + \gamma\beta B_z$, hence $E_y' = \gamma(E_y - vB_z)$. $\checkmark$

由 $F'^{02} = -E_y'/c$ 得 $E_y' = \gamma(E_y - vB_z)$。$\checkmark$

**$E_z'$ (from $F'^{03}$).**

**$E_z'$（由 $F'^{03}$）。**

$$ F'^{03} = \Lambda^0{}_0 F^{03} + \Lambda^0{}_1 F^{13} = \gamma(-E_z/c) + (-\gamma\beta)(+B_y) = -\gamma E_z/c - \gamma\beta B_y. $$

With $F'^{03} = -E_z'/c$: $E_z' = \gamma(E_z + vB_y)$. $\checkmark$

由 $F'^{03} = -E_z'/c$：$E_z' = \gamma(E_z + vB_y)$。$\checkmark$

**$B_z'$ (from $F'^{12}$).** Now the first index $1$ mixes with $0$:

**$B_z'$（由 $F'^{12}$）。** 此时第一个指标 $1$ 与 $0$ 混合：

$$ F'^{12} = \Lambda^1{}_0 F^{02} + \Lambda^1{}_1 F^{12} = (-\gamma\beta)(-E_y/c) + \gamma(-B_z) = \gamma\beta E_y/c - \gamma B_z. $$

Reading $F'^{12} = -B_z'$ and using $\beta/c = v/c^2$: $B_z' = \gamma(B_z - vE_y/c^2)$. $\checkmark$

由 $F'^{12} = -B_z'$ 并用 $\beta/c = v/c^2$：$B_z' = \gamma(B_z - vE_y/c^2)$。$\checkmark$

**$B_y'$ (from $F'^{13}$).**

**$B_y'$（由 $F'^{13}$）。**

$$ F'^{13} = \Lambda^1{}_0 F^{03} + \Lambda^1{}_1 F^{13} = (-\gamma\beta)(-E_z/c) + \gamma(+B_y) = \gamma\beta E_z/c + \gamma B_y. $$

Reading $F'^{13} = +B_y'$: $B_y' = \gamma(B_y + vE_z/c^2)$. $\checkmark$

由 $F'^{13} = +B_y'$：$B_y' = \gamma(B_y + vE_z/c^2)$。$\checkmark$

All six components reproduce the Claim with no convention ambiguity — the only requirement is to use $F^{0i} = -E_i/c$ (Section A) consistently for both $F$ and $F'$.

六个分量全部重现命题，且无约定歧义——唯一要求是在 $F$ 与 $F'$ 两侧一致地使用 $F^{0i} = -E_i/c$（A 节）。

**Summary (adopting the convention that the primed frame moves at $+v$ along $x$ in $S$):**

**汇总（$S'$ 以 $+v$ 沿 $x$ 相对 $S$ 运动；与本节命题及标准 Griffiths/Jackson 结果一致）：**

$$ \begin{aligned}
E_x' &= E_x &&\text{(parallel, unchanged)} \\
E_y' &= \gamma(E_y - vB_z) \\
E_z' &= \gamma(E_z + vB_y) \\
B_x' &= B_x &&\text{(parallel, unchanged)} \\
B_y' &= \gamma(B_y + vE_z/c^2) \\
B_z' &= \gamma(B_z - vE_y/c^2)
\end{aligned} $$

**Physical interpretation.** A purely electric Coulomb field in $S$ ($\mathbf{B} = 0$ there) appears in $S'$ as having both electric and magnetic components — **magnetism is the relativistic manifestation of electricity** when charges are observed in relative motion.

**物理诠释。** 在 $S$ 系中纯粹的库仑电场（$\mathbf{B} = 0$），在 $S'$ 系中同时具有电场和磁场分量——**磁性是电荷相对运动时电性的相对论表现**。$\blacksquare$

---

## C. The Inhomogeneous Maxwell Equations from $\partial_\mu F^{\mu\nu} = \mu_0 J^\nu$ · 由协变方程还原麦克斯韦方程

**Claim.** The single covariant equation $\partial_\mu F^{\mu\nu} = \mu_0 J^\nu$, for $\nu = 0$ and $\nu = 1, 2, 3$ respectively, reproduces Gauss's law and the Ampère–Maxwell law.

**命题。** 单一协变方程 $\partial_\mu F^{\mu\nu} = \mu_0 J^\nu$ 对 $\nu = 0$ 和 $\nu = 1, 2, 3$ 分别重现高斯定律和安培–麦克斯韦定律。

**Step 1 — Identify the four-current.** The four-current is $J^\nu = (c\rho, J_x, J_y, J_z)$, where $\rho$ is the charge density and $\mathbf{J}$ is the three-current density.

**第 1 步 — 识别四电流。** 四电流为 $J^\nu = (c\rho, J_x, J_y, J_z)$，其中 $\rho$ 为电荷密度，$\mathbf{J}$ 为三维电流密度。

**Step 2 — Setup: the explicit contravariant components.** From Section A the lowered tensor has $F_{0i} = E_i/c$ and $F_{ij} = -\varepsilon_{ijk}B^k$. Raising both indices with $\eta = \mathrm{diag}(+,-,-,-)$ gives $F^{0i} = \eta^{00}\eta^{ii}F_{0i} = -E_i/c$ (so $F^{i0} = +E_i/c$) and $F^{ij} = F_{ij} = -\varepsilon_{ijk}B^k$. The four-current is $J^\mu = (c\rho, J_x, J_y, J_z)$, and $\partial_\mu = \partial/\partial x^\mu = ((1/c)\partial_t, \partial_x, \partial_y, \partial_z)$. The key sign — the one that makes Gauss's law come out with the correct $+\rho/\varepsilon_0$ — is $F^{i0} = +E_i/c$, which follows directly from §A and must be used consistently.

**第 2 步 — 准备：显式逆变分量。** 由 A 节，降标张量有 $F_{0i} = E_i/c$ 与 $F_{ij} = -\varepsilon_{ijk}B^k$。用 $\eta = \mathrm{diag}(+,-,-,-)$ 升两个指标得 $F^{0i} = -E_i/c$（故 $F^{i0} = +E_i/c$）与 $F^{ij} = F_{ij} = -\varepsilon_{ijk}B^k$。四电流为 $J^\mu = (c\rho, J_x, J_y, J_z)$，$\partial_\mu = ((1/c)\partial_t, \partial_x, \partial_y, \partial_z)$。使高斯定律给出正确 $+\rho/\varepsilon_0$ 的关键符号是 $F^{i0} = +E_i/c$，它直接来自 §A，必须一致使用。

Take $F^{\mu\nu}$ with the components:

取 $F^{\mu\nu}$ 的分量：

$$ F^{\mu\nu} = \begin{pmatrix}
0 & -E_x/c & -E_y/c & -E_z/c \\
E_x/c & 0 & -B_z & B_y \\
E_y/c & B_z & 0 & -B_x \\
E_z/c & -B_y & B_x & 0
\end{pmatrix} $$

and $J^\mu = (c\rho, J_x, J_y, J_z)$, with $\partial_\mu = ((1/c)\partial_t, \partial_x, \partial_y, \partial_z)$.

For $\nu = 0$:

$$ \begin{aligned}
\partial_\mu F^{\mu 0} &= (1/c)\partial_t(0) + \partial_x(E_x/c) + \partial_y(E_y/c) + \partial_z(E_z/c) \\
&= (1/c)\nabla\cdot\mathbf{E} = \mu_0(c\rho).
\end{aligned} $$

Therefore $\nabla\cdot\mathbf{E} = \mu_0 c^2\rho = \rho/\varepsilon_0$. $\checkmark$ (Here $F^{10} = +E_x/c$ with this sign convention — rows are $\mu = 0,1,2,3$ and columns are $\nu = 0,1,2,3$.)

因此 $\nabla\cdot\mathbf{E} = \rho/\varepsilon_0$。$\checkmark$

For $\nu = 1$:

$$ \begin{aligned}
\partial_\mu F^{\mu 1} &= (1/c)\partial_t(-E_x/c) + \partial_x(0) + \partial_y(B_z) + \partial_z(-B_y) \\
&= -(1/c^2)\partial E_x/\partial t + (\partial B_z/\partial y - \partial B_y/\partial z) \\
&= -(1/c^2)\partial E_x/\partial t + (\nabla\times\mathbf{B})_x = \mu_0 J_x.
\end{aligned} $$

So $(\nabla\times\mathbf{B})_x = \mu_0 J_x + \mu_0\varepsilon_0\,\partial E_x/\partial t$ — the $x$-component of the **Ampère–Maxwell law** $\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\,\partial\mathbf{E}/\partial t$. $\checkmark$

故 $(\nabla\times\mathbf{B})_x = \mu_0 J_x + \mu_0\varepsilon_0\,\partial E_x/\partial t$——安培–麦克斯韦定律的 $x$ 分量。$\checkmark$

Similarly for $\nu = 2$ and $\nu = 3$, one recovers the $y$ and $z$ components. The two homogeneous Maxwell equations ($\nabla\cdot\mathbf{B} = 0$ and Faraday's law) follow automatically from the definition $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$, as shown by the Bianchi identity $\partial_{[\lambda} F_{\mu\nu]} = 0$. $\blacksquare$

类似地，$\nu = 2$ 和 $\nu = 3$ 给出 $y$ 和 $z$ 分量。两个齐次麦克斯韦方程（$\nabla\cdot\mathbf{B} = 0$ 和法拉第定律）由定义 $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$ 自动给出，通过比安基恒等式 $\partial_{[\lambda} F_{\mu\nu]} = 0$ 可见。$\blacksquare$

---

## D. The Two Lorentz Invariants $F_{\mu\nu} F^{\mu\nu}$ and $F_{\mu\nu} \tilde{F}^{\mu\nu}$ · 两个洛伦兹不变量

**Claim.** The only independent algebraic Lorentz scalars built from $F^{\mu\nu}$ are:
(i) $F_{\mu\nu} F^{\mu\nu} = 2(B^2 - E^2/c^2)$,
(ii) $F_{\mu\nu} \tilde{F}^{\mu\nu} = -4\,\mathbf{E}\cdot\mathbf{B}/c$ (where $\tilde{F}^{\mu\nu} = \tfrac12 \varepsilon^{\mu\nu\rho\sigma} F_{\rho\sigma}$ is the dual tensor).

**命题。** 由 $F^{\mu\nu}$ 构造的仅有的独立代数洛伦兹标量为：(i) $F_{\mu\nu} F^{\mu\nu} = 2(B^2 - E^2/c^2)$；(ii) $F_{\mu\nu} \tilde{F}^{\mu\nu} = -4\,\mathbf{E}\cdot\mathbf{B}/c$（其中 $\tilde{F}^{\mu\nu} = \tfrac12 \varepsilon^{\mu\nu\rho\sigma} F_{\rho\sigma}$ 为对偶张量）。

**Step 1 — Compute $F_{\mu\nu} F^{\mu\nu}$.** The contraction sums over all $\mu, \nu$. Using the antisymmetry $F_{\mu\nu} = -F_{\nu\mu}$ and $F^{\mu\nu} = -F^{\nu\mu}$, there are two contributions for each pair $(\mu,\nu)$ with $\mu < \nu$:

**第 1 步 — 计算 $F_{\mu\nu} F^{\mu\nu}$。** 缩并对所有 $\mu, \nu$ 求和。利用反对称性 $F_{\mu\nu} = -F_{\nu\mu}$，每对 $\mu < \nu$ 贡献两次：

$$ F_{\mu\nu} F^{\mu\nu} = 2(F_{01}F^{01} + F_{02}F^{02} + F_{03}F^{03} + F_{12}F^{12} + F_{13}F^{13} + F_{23}F^{23}). $$

From Section A the lowered components are $F_{0i} = E_i/c$ and $F_{ij} = -\varepsilon_{ijk}B^k$. Raise indices with $\eta = \mathrm{diag}(+,-,-,-)$: a time–space index pair flips sign, $F^{0i} = \eta^{00}\eta^{ii}F_{0i} = (+1)(-1)(E_i/c) = -E_i/c$, while a space–space pair is unchanged, $F^{ij} = \eta^{ii}\eta^{jj}F_{ij} = (-1)(-1)F_{ij} = F_{ij}$. Hence each time–space product is $F_{0i}F^{0i} = (E_i/c)(-E_i/c) = -E_i^2/c^2$, and each space–space product is $F_{ij}F^{ij} = (F_{ij})^2 \ge 0$ with $\sum_{i<j}(F_{ij})^2 = B^2$ (since $F_{12}=-B_z$, $F_{13}=+B_y$, $F_{23}=-B_x$). Therefore:

由 A 节，降标分量为 $F_{0i} = E_i/c$ 与 $F_{ij} = -\varepsilon_{ijk}B^k$。用 $\eta = \mathrm{diag}(+,-,-,-)$ 升指标：时间–空间对变号 $F^{0i} = -E_i/c$，空间–空间对不变 $F^{ij} = F_{ij}$。故每个时间–空间乘积为 $F_{0i}F^{0i} = -E_i^2/c^2$，每个空间–空间乘积为 $F_{ij}F^{ij} = (F_{ij})^2$，且 $\sum_{i<j}(F_{ij})^2 = B^2$。因此：

$$ \begin{aligned}
F_{\mu\nu} F^{\mu\nu} &= 2[-E_x^2/c^2 - E_y^2/c^2 - E_z^2/c^2 + B_z^2 + B_y^2 + B_x^2] \\
&= 2[B^2 - E^2/c^2].
\end{aligned} $$

So $F_{\mu\nu} F^{\mu\nu} = 2(B^2 - E^2/c^2)$. $\checkmark$

故 $F_{\mu\nu} F^{\mu\nu} = 2(B^2 - E^2/c^2)$。$\checkmark$

**Step 2 — The dual tensor $\tilde{F}^{\mu\nu}$.** The dual is defined as $\tilde{F}^{\mu\nu} = \tfrac12 \varepsilon^{\mu\nu\rho\sigma} F_{\rho\sigma}$, where $\varepsilon^{0123} = +1$ (or $-1$ depending on convention; we use $\varepsilon^{0123} = +1$ with the $(+,-,-,-)$ metric giving $\varepsilon^{0123}/\sqrt{-g} = +1$). The non-zero components are found from the cyclic properties of $\varepsilon^{\mu\nu\rho\sigma}$:

**第 2 步 — 对偶张量 $\tilde{F}^{\mu\nu}$。** 对偶张量定义为 $\tilde{F}^{\mu\nu} = \tfrac12 \varepsilon^{\mu\nu\rho\sigma} F_{\rho\sigma}$，其中 $\varepsilon^{0123} = +1$。非零分量由 $\varepsilon^{\mu\nu\rho\sigma}$ 的循环性质给出：

$$ \begin{aligned}
\tilde{F}^{01} &= \tfrac12(\varepsilon^{0123}F_{23} + \varepsilon^{0132}F_{32}) = \tfrac12(F_{23} - F_{32}) = F_{23} = -B_x, &&\text{and cyclically } \tilde{F}^{0i} = -B_i; \\
\tilde{F}^{12} &= \tfrac12(\varepsilon^{1203}F_{03} + \varepsilon^{1230}F_{30}) = F_{03} = E_z/c, &&\text{and cyclically } \tilde{F}^{13} = -E_y/c,\; \tilde{F}^{23} = E_x/c.
\end{aligned} $$

In matrix form:

写成矩阵形式：

$$ \tilde{F}^{\mu\nu} = \begin{pmatrix}
0 & -B_x & -B_y & -B_z \\
B_x & 0 & E_z/c & -E_y/c \\
B_y & -E_z/c & 0 & E_x/c \\
B_z & E_y/c & -E_x/c & 0
\end{pmatrix} $$

In other words, $\tilde{F}^{\mu\nu}$ is obtained from $F^{\mu\nu}$ by the replacements $\mathbf{E}/c \to \mathbf{B}$ and $\mathbf{B} \to -\mathbf{E}/c$ (an electromagnetic duality rotation by $\pi/2$).

即 $\tilde{F}^{\mu\nu}$ 由 $F^{\mu\nu}$ 经替换 $\mathbf{E}/c \to \mathbf{B}$ 和 $\mathbf{B} \to -\mathbf{E}/c$ 得到（电磁对偶旋转 $\pi/2$）。

**Step 3 — Compute $F_{\mu\nu} \tilde{F}^{\mu\nu}$.** Summing each unordered pair twice, with the lowered components $F_{0i} = E_i/c$, $F_{12} = -B_z$, $F_{13} = +B_y$, $F_{23} = -B_x$ (Section A) and $\tilde{F}^{\mu\nu}$ from Step 2:

**第 3 步 — 计算 $F_{\mu\nu} \tilde{F}^{\mu\nu}$。** 每个无序对计两次，用降标分量 $F_{0i} = E_i/c$、$F_{12} = -B_z$、$F_{13} = +B_y$、$F_{23} = -B_x$（A 节）以及第 2 步的 $\tilde{F}^{\mu\nu}$：

$$ \begin{aligned}
\text{Time–space: } &\sum_i F_{0i} \tilde{F}^{0i} = \sum_i (E_i/c)(-B_i) = -(\mathbf{E}\cdot\mathbf{B})/c, \\
\text{Space–space: } &F_{12}\tilde{F}^{12} + F_{13}\tilde{F}^{13} + F_{23}\tilde{F}^{23} = (-B_z)(E_z/c) + (B_y)(-E_y/c) + (-B_x)(E_x/c) = -(\mathbf{E}\cdot\mathbf{B})/c.
\end{aligned} $$

Therefore:

因此：

$$ F_{\mu\nu} \tilde{F}^{\mu\nu} = 2\big[ -(\mathbf{E}\cdot\mathbf{B})/c - (\mathbf{E}\cdot\mathbf{B})/c \big] = -4(\mathbf{E}\cdot\mathbf{B})/c \qquad (\text{SI, metric } +{-}{-}{-},\; \varepsilon^{0123} = +1). $$

The overall sign is fixed by the orientation convention $\varepsilon^{0123} = +1$; the magnitude $4|\mathbf{E}\cdot\mathbf{B}|/c$ is convention-independent. This pseudoscalar, promoted to the non-abelian form $G^a_{\mu\nu}\tilde{G}^{a\mu\nu}$, is exactly the QCD **$\theta$-term** behind the strong-CP problem (Module 8.3, [6.9 §D](../phase-6-quantum-field-theory/module-6.9-anomalies-and-nonperturbative-qft-derivations.md)).

总符号由定向约定 $\varepsilon^{0123} = +1$ 固定；量值 $4|\mathbf{E}\cdot\mathbf{B}|/c$ 与约定无关。此赝标量推广为非阿贝尔形式 $G^a_{\mu\nu}\tilde{G}^{a\mu\nu}$ 时，正是强 CP 问题背后的 QCD **$\theta$ 项**（模块 8.3、[6.9 §D](../phase-6-quantum-field-theory/module-6.9-anomalies-and-nonperturbative-qft-derivations.md)）。

**Step 4 — Physical significance of the two invariants.**

**第 4 步 — 两个不变量的物理意义。**

- **Invariant $I = B^2 - E^2/c^2$:** If $I > 0$, there exists a frame where $\mathbf{E} = 0$ (purely magnetic). If $I < 0$, there exists a frame where $\mathbf{B} = 0$ (purely electric). If $I = 0$ and $\mathbf{E}\cdot\mathbf{B} = 0$, the field is null (e.g. a plane electromagnetic wave has $B^2 = E^2/c^2$ and $\mathbf{E}\cdot\mathbf{B} = 0$).

- **不变量 $I = B^2 - E^2/c^2$：** 若 $I > 0$，存在使 $\mathbf{E} = 0$ 的参考系（纯磁场）；若 $I < 0$，存在使 $\mathbf{B} = 0$ 的参考系（纯电场）；若 $I = 0$ 且 $\mathbf{E}\cdot\mathbf{B} = 0$，场为零曲率（例如平面电磁波满足 $B^2 = E^2/c^2$ 且 $\mathbf{E}\cdot\mathbf{B} = 0$）。

- **Invariant $II \propto \mathbf{E}\cdot\mathbf{B}$:** If this is zero in one frame, it is zero in all frames — no boost can produce $\mathbf{E}\cdot\mathbf{B} \ne 0$ from $\mathbf{E}\cdot\mathbf{B} = 0$. This appears in the Lagrangian of the $\theta$-vacuum in QCD (the strong CP problem, Phase 8).

- **不变量 $II \propto \mathbf{E}\cdot\mathbf{B}$：** 若在某参考系中为零，则在所有参考系中均为零——变换不能从 $\mathbf{E}\cdot\mathbf{B} = 0$ 产生 $\mathbf{E}\cdot\mathbf{B} \ne 0$。此量出现在 QCD $\theta$ 真空的拉格朗日量中（强 CP 问题，第 8 阶段）。$\blacksquare$

---

## E. Maxwell's Equations from the Action Principle · 由作用量原理导出麦克斯韦方程

**Claim.** The inhomogeneous Maxwell equations $\partial_\mu F^{\mu\nu} = \mu_0 J^\nu$ follow from extremizing the manifestly Lorentz-invariant action

**命题。** 非齐次麦克斯韦方程 $\partial_\mu F^{\mu\nu} = \mu_0 J^\nu$ 来自对显式洛伦兹不变作用量取极值

$$ S[A] = \int d^4x\; \mathcal{L}, \qquad \mathcal{L} = -\frac{1}{4\mu_0} F_{\mu\nu} F^{\mu\nu} - J^\mu A_\mu, $$

with respect to the four-potential $A_\mu$. The homogeneous pair (Gauss's law for magnetism and Faraday's law) is **not** an equation of motion at all — it is the Bianchi identity, an algebraic consequence of $F = dA$. This is the cleanest statement of electromagnetism: one scalar functional, one field $A_\mu$, and both pairs of Maxwell's equations drop out.

对四矢量势 $A_\mu$ 取极值。齐次对（磁场高斯定律与法拉第定律）**根本不是**运动方程——它是比安基恒等式，是 $F = dA$ 的代数推论。这是电磁学最简洁的表述：一个标量泛函、一个场 $A_\mu$，麦克斯韦方程的两对都随之而出。

**Step 1 — The field-strength term is the unique gauge-invariant kinetic term.** Under a gauge transformation $A_\mu \to A_\mu + \partial_\mu\chi$, the tensor $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ is invariant (Section A), so any function of $F_{\mu\nu}$ is gauge-invariant. Lorentz invariance, gauge invariance, parity, and at most two derivatives single out $F_{\mu\nu}F^{\mu\nu}$ as the kinetic term (the dual invariant $F_{\mu\nu}\tilde{F}^{\mu\nu}$ of Section D is a total derivative and does not affect the equations of motion). The constant $-1/4\mu_0$ fixes the normalization so that $\mathcal{L}$ reproduces the energy density $\tfrac12(\varepsilon_0 E^2 + B^2/\mu_0)$ below.

**第 1 步 — 场强项是唯一的规范不变动能项。** 在规范变换 $A_\mu \to A_\mu + \partial_\mu\chi$ 下，张量 $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ 不变（A 节），故 $F_{\mu\nu}$ 的任何函数都规范不变。洛伦兹不变性、规范不变性、宇称以及至多两个导数共同选出 $F_{\mu\nu}F^{\mu\nu}$ 作为动能项（D 节的对偶不变量 $F_{\mu\nu}\tilde{F}^{\mu\nu}$ 是全导数，不影响运动方程）。常数 $-1/4\mu_0$ 固定归一化，使 $\mathcal{L}$ 重现下文的能量密度 $\tfrac12(\varepsilon_0 E^2 + B^2/\mu_0)$。

**Step 2 — Euler–Lagrange equation for $A_\mu$.** The Euler–Lagrange equation for the field $A_\beta$ is

**第 2 步 — $A_\mu$ 的欧拉–拉格朗日方程。** 场 $A_\beta$ 的欧拉–拉格朗日方程为

$$ \partial_\alpha\left[ \frac{\partial\mathcal{L}}{\partial(\partial_\alpha A_\beta)} \right] - \frac{\partial\mathcal{L}}{\partial A_\beta} = 0. $$

We need the derivative of the kinetic term with respect to $\partial_\alpha A_\beta$. Write $F_{\mu\nu}F^{\mu\nu}$ and use $\partial F_{\mu\nu}/\partial(\partial_\alpha A_\beta) = \delta^\alpha_\mu \delta^\beta_\nu - \delta^\alpha_\nu \delta^\beta_\mu$:

我们需要动能项对 $\partial_\alpha A_\beta$ 的导数。利用 $\partial F_{\mu\nu}/\partial(\partial_\alpha A_\beta) = \delta^\alpha_\mu \delta^\beta_\nu - \delta^\alpha_\nu \delta^\beta_\mu$：

$$ \frac{\partial(F_{\mu\nu}F^{\mu\nu})}{\partial(\partial_\alpha A_\beta)} = 2 F^{\mu\nu} (\delta^\alpha_\mu \delta^\beta_\nu - \delta^\alpha_\nu \delta^\beta_\mu) = 2(F^{\alpha\beta} - F^{\beta\alpha}) = 4F^{\alpha\beta}, $$

so

故

$$ \frac{\partial\mathcal{L}}{\partial(\partial_\alpha A_\beta)} = -\frac{1}{4\mu_0}(4F^{\alpha\beta}) = -\frac{1}{\mu_0} F^{\alpha\beta}, \qquad \frac{\partial\mathcal{L}}{\partial A_\beta} = -J^\beta. $$

**Step 3 — Assemble the equation of motion.** Substituting into Euler–Lagrange:

**第 3 步 — 组装运动方程。** 代入欧拉–拉格朗日方程：

$$ \partial_\alpha\left[ -\frac{1}{\mu_0} F^{\alpha\beta} \right] - ( -J^\beta ) = 0 \implies -\frac{1}{\mu_0} \partial_\alpha F^{\alpha\beta} + J^\beta = 0 \implies \boxed{\, \partial_\alpha F^{\alpha\beta} = \mu_0 J^\beta \,}. $$

This is exactly the covariant inhomogeneous Maxwell equation of Section C — Gauss's law ($\beta = 0$) and the Ampère–Maxwell law ($\beta = i$). The current conservation $\partial_\beta J^\beta = 0$ follows immediately from the antisymmetry of $F^{\alpha\beta}$: $\partial_\beta\partial_\alpha F^{\alpha\beta} = 0$ because $\partial_\beta\partial_\alpha$ is symmetric while $F^{\alpha\beta}$ is antisymmetric.

这正是 C 节的协变非齐次麦克斯韦方程——高斯定律（$\beta = 0$）与安培–麦克斯韦定律（$\beta = i$）。电流守恒 $\partial_\beta J^\beta = 0$ 立即由 $F^{\alpha\beta}$ 的反对称性得出：$\partial_\beta\partial_\alpha F^{\alpha\beta} = 0$，因为 $\partial_\beta\partial_\alpha$ 对称而 $F^{\alpha\beta}$ 反对称。

**Step 4 — The homogeneous pair is the Bianchi identity.** Because $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ is exact ($F = dA$), it satisfies identically

**第 4 步 — 齐次对即比安基恒等式。** 由于 $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ 是恰当的（$F = dA$），它恒满足

$$ \partial_\lambda F_{\mu\nu} + \partial_\mu F_{\nu\lambda} + \partial_\nu F_{\lambda\mu} = 0 \iff \partial_\lambda \tilde{F}^{\lambda\nu} = 0, $$

where $\tilde{F}^{\mu\nu} = \tfrac12\varepsilon^{\mu\nu\alpha\beta}F_{\alpha\beta}$ is the dual. Each term cancels in pairs upon substituting $F = \partial A$ and using $\partial_\lambda\partial_\mu = \partial_\mu\partial_\lambda$. The $\nu = 0$ component is $\nabla\cdot\mathbf{B} = 0$; the $\nu = i$ components are Faraday's law $\partial\mathbf{B}/\partial t + \nabla\times\mathbf{E} = 0$. No dynamics, no source — purely the statement "$F$ is a curl."

其中 $\tilde{F}^{\mu\nu} = \tfrac12\varepsilon^{\mu\nu\alpha\beta}F_{\alpha\beta}$ 是对偶张量。代入 $F = \partial A$ 并用 $\partial_\lambda\partial_\mu = \partial_\mu\partial_\lambda$，各项成对相消。$\nu = 0$ 分量即 $\nabla\cdot\mathbf{B} = 0$；$\nu = i$ 分量即法拉第定律 $\partial\mathbf{B}/\partial t + \nabla\times\mathbf{E} = 0$。没有动力学、没有源——纯粹是"$F$ 是一个旋度"这一陈述。

**Step 5 — The stress-energy tensor (Noether $\to$ Belinfante).** The canonical stress-energy tensor from translation invariance, $T^{\mu\nu}_{\text{can}} = (\partial\mathcal{L}/\partial(\partial_\mu A_\lambda))\partial^\nu A_\lambda - \eta^{\mu\nu}\mathcal{L} = -(1/\mu_0)F^{\mu\lambda}\partial^\nu A_\lambda - \eta^{\mu\nu}\mathcal{L}$, is neither symmetric nor gauge-invariant. Adding the improvement term $(1/\mu_0)\partial_\lambda(F^{\lambda\mu}A^\nu)$ — a total derivative that, using $\partial_\lambda F^{\lambda\mu} = \mu_0 J^\mu = 0$ in source-free regions, changes neither the conserved energy–momentum nor the local conservation law — symmetrizes it to the gauge-invariant **Belinfante tensor**

**第 5 步 — 能动张量（诺特 $\to$ 贝林方特）。** 由平移不变性得到的正则能动张量 $T^{\mu\nu}_{\text{can}} = (\partial\mathcal{L}/\partial(\partial_\mu A_\lambda))\partial^\nu A_\lambda - \eta^{\mu\nu}\mathcal{L} = -(1/\mu_0)F^{\mu\lambda}\partial^\nu A_\lambda - \eta^{\mu\nu}\mathcal{L}$ 既不对称也不规范不变。加入改进项 $(1/\mu_0)\partial_\lambda(F^{\lambda\mu}A^\nu)$——一个全导数，在无源区利用 $\partial_\lambda F^{\lambda\mu} = \mu_0 J^\mu = 0$，它既不改变守恒的能量–动量，也不改变局域守恒律——将其对称化为规范不变的**贝林方特张量**

$$ \boxed{\, T^{\mu\nu} = \frac{1}{\mu_0}\left[ -F^{\mu\alpha} F^\nu{}_\alpha + \tfrac14 \eta^{\mu\nu} F_{\alpha\beta}F^{\alpha\beta} \right] \,} \qquad (\text{metric } +{-}{-}{-}). $$

(In the opposite signature $-{+}{+}{+}$ this is written $T^{\mu\nu} = (1/\mu_0)[F^{\mu\alpha}F^\nu{}_\alpha - \tfrac14\eta^{\mu\nu}F^2]$; the two overall signs flip together with $\eta$, so $T^{00}$ is positive in both. The explicit component check is carried out in Section F.)

（在相反符号 $-{+}{+}{+}$ 下写作 $T^{\mu\nu} = (1/\mu_0)[F^{\mu\alpha}F^\nu{}_\alpha - \tfrac14\eta^{\mu\nu}F^2]$；两处总符号随 $\eta$ 一起翻转，故 $T^{00}$ 在两种约定下均为正。显式分量验证见 F 节。）

This tensor is symmetric ($T^{\mu\nu} = T^{\nu\mu}$), gauge-invariant (built only from $F$), traceless ($\eta_{\mu\nu}T^{\mu\nu} = 0$, reflecting the masslessness/conformal invariance of the photon), and conserved: $\partial_\mu T^{\mu\nu} = -F^{\nu\lambda}J_\lambda$ in the presence of a source $J$ (the Lorentz four-force density), and $\partial_\mu T^{\mu\nu} = 0$ in vacuum — precisely Poynting's theorem (energy conservation) and electromagnetic momentum conservation. The whole mechanical force law thus follows from the field action alone. $\blacksquare$

该张量对称（$T^{\mu\nu} = T^{\nu\mu}$）、规范不变（仅由 $F$ 构造）、无迹（$\eta_{\mu\nu}T^{\mu\nu} = 0$，反映光子的无质量／共形不变性），且守恒：有源 $J$ 时 $\partial_\mu T^{\mu\nu} = -F^{\nu\lambda}J_\lambda$（洛伦兹四维力密度），真空中 $\partial_\mu T^{\mu\nu} = 0$——正是坡印廷定理（能量守恒）与电磁动量守恒。于是整个力学的力定律仅由场作用量便得出。$\blacksquare$

---

## F. Component-by-Component Verification of the Stress-Energy Tensor · 能动张量的逐分量验证

**Claim.** Evaluating the Belinfante tensor $T^{\mu\nu} = (1/\mu_0)[-F^{\mu\alpha}F^\nu{}_\alpha + \tfrac14\eta^{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}]$ on the explicit field components of Section A reproduces, component by component, the electromagnetic energy density, the Poynting (momentum-flux) vector, and the Maxwell stress tensor of elementary electromagnetism.

**命题。** 将贝林方特张量 $T^{\mu\nu} = (1/\mu_0)[-F^{\mu\alpha}F^\nu{}_\alpha + \tfrac14\eta^{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}]$ 在 A 节的显式场分量上求值，逐分量重现基础电磁学的电磁能量密度、坡印廷（动量通量）矢量与麦克斯韦应力张量。

**Setup — components with one index raised.** From Section A, $F_{0i} = E_i/c$ and $F_{ij} = -\varepsilon_{ijk}B^k$. Raising one index with $\eta = \mathrm{diag}(+,-,-,-)$:

**准备——升一个指标的分量。** 由 A 节，$F_{0i} = E_i/c$，$F_{ij} = -\varepsilon_{ijk}B^k$。用 $\eta = \mathrm{diag}(+,-,-,-)$ 升一个指标：

$$ F^{0i} = -E_i/c, \quad F^i{}_0 = E_i/c, \quad F^i{}_j = \varepsilon_{ijk}B^k, \qquad \text{and} \quad F_{\alpha\beta}F^{\alpha\beta} = 2(B^2 - E^2/c^2) \;\text{(Section D)}. $$

**Step 1 — Energy density $T^{00}$.** With $\eta^{00} = +1$:

**第 1 步 — 能量密度 $T^{00}$。** 取 $\eta^{00} = +1$：

$$ T^{00} = (1/\mu_0)\left[ -F^{0\alpha}F^0{}_\alpha + \tfrac14 F_{\alpha\beta}F^{\alpha\beta} \right]. $$

The first term: $F^{0\alpha}F^0{}_\alpha = F^{0i}F^0{}_i = \sum_i(-E_i/c)(E_i/c) = -E^2/c^2$ (using $F^0{}_i = \eta^{00}F_{0i} = E_i/c$). Hence

第一项：$F^{0\alpha}F^0{}_\alpha = \sum_i(-E_i/c)(E_i/c) = -E^2/c^2$。故

$$ T^{00} = (1/\mu_0)\left[ E^2/c^2 + \tfrac14\cdot 2(B^2 - E^2/c^2) \right] = (1/\mu_0)\left[ E^2/c^2 + \tfrac12 B^2 - \tfrac12 E^2/c^2 \right] = (1/\mu_0)\left[ \tfrac12 E^2/c^2 + \tfrac12 B^2 \right]. $$

Using $\varepsilon_0 = 1/(\mu_0 c^2)$:

利用 $\varepsilon_0 = 1/(\mu_0 c^2)$：

$$ \boxed{\, T^{00} = \tfrac12(\varepsilon_0 E^2 + B^2/\mu_0) = u \,} \quad\text{— the electromagnetic energy density.} \;\checkmark $$

**Step 2 — Energy flux / momentum density $T^{0i}$.** Since $\eta^{0i} = 0$:

**第 2 步 — 能流／动量密度 $T^{0i}$。** 因 $\eta^{0i} = 0$：

$$ T^{0i} = -(1/\mu_0)F^{0\alpha}F^i{}_\alpha = -(1/\mu_0)F^{0j}F^i{}_j = -(1/\mu_0)\sum_j(-E_j/c)(\varepsilon_{ijk}B^k) = (1/\mu_0 c)\varepsilon_{ijk}E_j B^k. $$

Therefore

因此

$$ \boxed{\, T^{0i} = (1/\mu_0 c)(\mathbf{E} \times \mathbf{B})_i = S_i/c \,}, \qquad \text{where } \mathbf{S} = (1/\mu_0)\mathbf{E} \times \mathbf{B} \text{ is the Poynting vector.} \;\checkmark $$

$T^{0i}$ is simultaneously the energy flux ($\times 1/c$) and the electromagnetic momentum density $g_i = S_i/c^2$ ($\times c$) — the field carries momentum, as the relativistic symmetry $T^{0i} = T^{i0}$ demands.

$T^{0i}$ 同时是能流（$\times 1/c$）与电磁动量密度 $g_i = S_i/c^2$（$\times c$）——场携带动量，正如相对论对称性 $T^{0i} = T^{i0}$ 所要求。

**Step 3 — Stress (momentum flux) $T^{ij} =$ the Maxwell stress tensor.** With $\eta^{ij} = -\delta_{ij}$:

**第 3 步 — 应力（动量通量）$T^{ij} =$ 麦克斯韦应力张量。** 取 $\eta^{ij} = -\delta_{ij}$：

$$ T^{ij} = (1/\mu_0)\left[ -F^{i\alpha}F^j{}_\alpha - \tfrac14\delta_{ij}F_{\alpha\beta}F^{\alpha\beta} \right]. $$

The contraction splits into time and space parts: $-F^{i\alpha}F^j{}_\alpha = -[F^{i0}F^j{}_0 + F^{ik}F^j{}_k] = -[(E_i/c)(E_j/c) + (-\varepsilon_{ikm}B^m)(\varepsilon_{jkn}B^n)]$. Using $\sum_k \varepsilon_{ikm}\varepsilon_{jkn} = \delta_{ij}\delta_{mn} - \delta_{in}\delta_{mj}$, the magnetic piece is $-(-(\delta_{ij}B^2 - B_iB_j)) = \delta_{ij}B^2 - B_iB_j$, so

缩并分为时间与空间两部分；利用 $\sum_k \varepsilon_{ikm}\varepsilon_{jkn} = \delta_{ij}\delta_{mn} - \delta_{in}\delta_{mj}$ 处理磁场部分，得

$$ -F^{i\alpha}F^j{}_\alpha = -E_iE_j/c^2 + \delta_{ij}B^2 - B_iB_j. $$

The trace term is $-\tfrac14\delta_{ij}\cdot 2(B^2 - E^2/c^2) = -\tfrac12\delta_{ij}B^2 + \tfrac12\delta_{ij}E^2/c^2$. Adding:

迹项为 $-\tfrac12\delta_{ij}B^2 + \tfrac12\delta_{ij}E^2/c^2$。相加：

$$ \begin{aligned}
T^{ij} &= (1/\mu_0)\left[ -E_iE_j/c^2 - B_iB_j + \tfrac12\delta_{ij}(E^2/c^2 + B^2) \right] \\
&= -\left[ \varepsilon_0(E_iE_j - \tfrac12\delta_{ij}E^2) + (1/\mu_0)(B_iB_j - \tfrac12\delta_{ij}B^2) \right] = -\sigma_{ij},
\end{aligned} $$

which is **minus the Maxwell stress tensor** $\sigma_{ij}$ of electrostatics/magnetostatics. The sign is correct: $T^{ij}$ is the flux of $i$-momentum in the $j$-direction, and $-\sigma_{ij}$ is the rate at which field momentum flows, so $\partial_\mu T^{\mu i} = 0$ reproduces the momentum-conservation law $\mathbf{f} + \partial\mathbf{g}/\partial t = \nabla\cdot\sigma$ of Maxwell stress. $\checkmark$ $\blacksquare$

即**麦克斯韦应力张量 $\sigma_{ij}$ 的相反数**。符号正确：$T^{ij}$ 是 $i$ 方向动量沿 $j$ 方向的通量，$-\sigma_{ij}$ 是场动量的流动率，故 $\partial_\mu T^{\mu i} = 0$ 重现麦克斯韦应力的动量守恒律 $\mathbf{f} + \partial\mathbf{g}/\partial t = \nabla\cdot\sigma$。$\checkmark$ $\blacksquare$

---

*All results follow from the covariant structure of $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$ and the Lorentz transformation law for rank-2 tensors.*

---

*All results follow from the covariant structure of $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$ and the Lorentz transformation law for rank-2 tensors.*

*所有结果均来自 $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$ 的协变结构以及 2 阶张量的洛伦兹变换法则。*

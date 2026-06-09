---
title: "Derivations — Module 1.22: Retarded Potentials, Multipole Radiation & Radiation Reaction"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 1.22: Retarded Potentials, Multipole Radiation & Radiation Reaction
# 推导 — 模块 1.22：推迟势、多极辐射与辐射阻尼

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.22](./module-1.22-retarded-potentials-radiation-reaction.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.22](./module-1.22-retarded-potentials-radiation-reaction.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Retarded Potentials from the Wave Equation · 从波动方程推导推迟势

**Claim.** In the Lorenz gauge $\partial_\mu A^\mu = 0$, the potentials satisfy $\Box\varphi = -\rho/\varepsilon_0$ and $\Box\mathbf{A} = -\mu_0\mathbf{J}$ (with $\Box = \nabla^2 - (1/c^2)\partial^2/\partial t^2$). The causal solutions are the retarded potentials $\varphi(\mathbf{r},t) = (1/4\pi\varepsilon_0)\int \rho(\mathbf{r}',t_r)/|\mathbf{r}-\mathbf{r}'|\,d^3r'$ and $\mathbf{A}(\mathbf{r},t) = (\mu_0/4\pi)\int \mathbf{J}(\mathbf{r}',t_r)/|\mathbf{r}-\mathbf{r}'|\,d^3r'$, with $t_r = t - |\mathbf{r}-\mathbf{r}'|/c$.

**命题。** 在洛伦兹规范 $\partial_\mu A^\mu = 0$ 下，势满足 $\Box\varphi = -\rho/\varepsilon_0$ 与 $\Box\mathbf{A} = -\mu_0\mathbf{J}$（$\Box = \nabla^2 - (1/c^2)\partial^2/\partial t^2$）。因果解为推迟势 $\varphi(\mathbf{r},t) = (1/4\pi\varepsilon_0)\int \rho(\mathbf{r}',t_r)/|\mathbf{r}-\mathbf{r}'|\,d^3r'$ 与 $\mathbf{A}(\mathbf{r},t) = (\mu_0/4\pi)\int \mathbf{J}(\mathbf{r}',t_r)/|\mathbf{r}-\mathbf{r}'|\,d^3r'$，其中 $t_r = t - |\mathbf{r}-\mathbf{r}'|/c$。

**Step 1 — Reduce Maxwell's equations to wave equations.** Write the fields via potentials $\mathbf{E} = -\boldsymbol{\nabla}\varphi - \partial\mathbf{A}/\partial t$, $\mathbf{B} = \boldsymbol{\nabla}\times\mathbf{A}$ (Module 1.10). Gauss's law $\boldsymbol{\nabla}\cdot\mathbf{E} = \rho/\varepsilon_0$ becomes $-\nabla^2\varphi - \partial(\boldsymbol{\nabla}\cdot\mathbf{A})/\partial t = \rho/\varepsilon_0$, and Ampère–Maxwell $\boldsymbol{\nabla}\times\mathbf{B} = \mu_0\mathbf{J} + (1/c^2)\partial\mathbf{E}/\partial t$ becomes $\boldsymbol{\nabla}(\boldsymbol{\nabla}\cdot\mathbf{A}) - \nabla^2\mathbf{A} = \mu_0\mathbf{J} - (1/c^2)\boldsymbol{\nabla}(\partial\varphi/\partial t) - (1/c^2)\partial^2\mathbf{A}/\partial t^2$.

**第 1 步 — 将麦克斯韦方程化为波动方程。** 用势写出场 $\mathbf{E} = -\boldsymbol{\nabla}\varphi - \partial\mathbf{A}/\partial t$，$\mathbf{B} = \boldsymbol{\nabla}\times\mathbf{A}$（模块 1.10）。高斯定律 $\boldsymbol{\nabla}\cdot\mathbf{E} = \rho/\varepsilon_0$ 化为 $-\nabla^2\varphi - \partial(\boldsymbol{\nabla}\cdot\mathbf{A})/\partial t = \rho/\varepsilon_0$，安培–麦克斯韦方程 $\boldsymbol{\nabla}\times\mathbf{B} = \mu_0\mathbf{J} + (1/c^2)\partial\mathbf{E}/\partial t$ 化为 $\boldsymbol{\nabla}(\boldsymbol{\nabla}\cdot\mathbf{A}) - \nabla^2\mathbf{A} = \mu_0\mathbf{J} - (1/c^2)\boldsymbol{\nabla}(\partial\varphi/\partial t) - (1/c^2)\partial^2\mathbf{A}/\partial t^2$。

**Step 2 — Impose the Lorenz gauge.** Choosing $\boldsymbol{\nabla}\cdot\mathbf{A} + (1/c^2)\partial\varphi/\partial t = 0$ (i.e. $\partial_\mu A^\mu = 0$) eliminates the cross terms. The two equations decouple into

**第 2 步 — 施加洛伦兹规范。** 选取 $\boldsymbol{\nabla}\cdot\mathbf{A} + (1/c^2)\partial\varphi/\partial t = 0$（即 $\partial_\mu A^\mu = 0$）消去交叉项。两个方程解耦为

$$ \nabla^2\varphi - \frac{1}{c^2}\frac{\partial^2\varphi}{\partial t^2} = -\frac{\rho}{\varepsilon_0}, \qquad \nabla^2\mathbf{A} - \frac{1}{c^2}\frac{\partial^2\mathbf{A}}{\partial t^2} = -\mu_0\mathbf{J}, $$

i.e. $\Box\varphi = -\rho/\varepsilon_0$ and $\Box\mathbf{A} = -\mu_0\mathbf{J}$ — four identical scalar wave equations with sources.

即 $\Box\varphi = -\rho/\varepsilon_0$ 与 $\Box\mathbf{A} = -\mu_0\mathbf{J}$——四个形式相同的带源标量波动方程。

**Step 3 — Green's function of the d'Alembertian.** The retarded Green's function solves $\Box G(\mathbf{r},t; \mathbf{r}',t') = -\delta^3(\mathbf{r}-\mathbf{r}')\delta(t-t')$ with purely outgoing (causal) boundary conditions. The standard result is

**第 3 步 — 达朗贝尔算子的格林函数。** 推迟格林函数满足 $\Box G(\mathbf{r},t; \mathbf{r}',t') = -\delta^3(\mathbf{r}-\mathbf{r}')\delta(t-t')$，具纯外向（因果）边界条件。标准结果为

$$ G(\mathbf{r},t; \mathbf{r}',t') = \frac{\delta(t' - [t - |\mathbf{r}-\mathbf{r}'|/c])}{4\pi|\mathbf{r}-\mathbf{r}'|} = \frac{\delta(t_r - t')}{4\pi|\mathbf{r}-\mathbf{r}'|}, $$

where $t_r = t - |\mathbf{r}-\mathbf{r}'|/c$ is the retarded time: the delta function fires only when $t'$ equals the moment a signal leaving $\mathbf{r}'$ at speed $c$ arrives at $\mathbf{r}$ at time $t$.

其中 $t_r = t - |\mathbf{r}-\mathbf{r}'|/c$ 为推迟时刻：仅当 $t'$ 等于从 $\mathbf{r}'$ 以速度 $c$ 出发的信号在 $t$ 时刻到达 $\mathbf{r}$ 的那一时刻时，$\delta$ 函数才作用。

**Step 4 — Convolve source with Green's function.** Since $\Box\varphi = -\rho/\varepsilon_0$, the particular solution is $\varphi = (1/\varepsilon_0)\int G\rho\,d^3r'\,dt'$. Insert $G$ and integrate over $t'$ using the delta function:

**第 4 步 — 源与格林函数的卷积。** 由 $\Box\varphi = -\rho/\varepsilon_0$，特解为 $\varphi = (1/\varepsilon_0)\int G\rho\,d^3r'\,dt'$。代入 $G$ 并用 $\delta$ 函数对 $t'$ 积分：

$$ \begin{aligned}
\varphi(\mathbf{r},t) &= \frac{1}{\varepsilon_0}\int d^3r' \int dt'\, \frac{\delta(t_r - t')}{4\pi|\mathbf{r}-\mathbf{r}'|}\,\rho(\mathbf{r}',t') \\
&= \frac{1}{4\pi\varepsilon_0}\int \frac{\rho(\mathbf{r}', t_r)}{|\mathbf{r}-\mathbf{r}'|}\,d^3r'.
\end{aligned} $$

The same convolution with $\Box\mathbf{A} = -\mu_0\mathbf{J}$ gives

对 $\Box\mathbf{A} = -\mu_0\mathbf{J}$ 作相同卷积给出

$$ \mathbf{A}(\mathbf{r},t) = \frac{\mu_0}{4\pi}\int \frac{\mathbf{J}(\mathbf{r}', t_r)}{|\mathbf{r}-\mathbf{r}'|}\,d^3r'. $$

**Step 5 — Causality fixes the retarded (not advanced) choice.** The wave operator also admits an advanced Green's function with $t_a = t + |\mathbf{r}-\mathbf{r}'|/c$, giving fields determined by the *future* of the source. Physical causality — effects follow causes — selects the retarded solution: the field at $(\mathbf{r},t)$ depends only on the source at the earlier time $t_r$. $\blacksquare$

**第 5 步 — 因果性选定推迟解（而非超前解）。** 波动算子也容许带 $t_a = t + |\mathbf{r}-\mathbf{r}'|/c$ 的超前格林函数，给出由源的*未来*决定的场。物理因果性——果随因——选择推迟解：$(\mathbf{r},t)$ 处的场只依赖于较早时刻 $t_r$ 的源。$\blacksquare$

---

## B. The Liénard–Wiechert Potentials and the $\kappa = 1 - \mathbf{n}\cdot\boldsymbol{\beta}$ Factor · 李纳–维谢尔势与 $\kappa = 1 - \mathbf{n}\cdot\boldsymbol{\beta}$ 因子

**Claim.** For a point charge $q$ moving on trajectory $\mathbf{w}(t)$, the retarded potentials evaluate to $\varphi = (1/4\pi\varepsilon_0)\, q/[\kappa R]_{\text{ret}}$ and $\mathbf{A} = (\mu_0/4\pi)\, qc\boldsymbol{\beta}/[\kappa R]_{\text{ret}} = (\boldsymbol{\beta}/c)\varphi$, where $R = |\mathbf{r} - \mathbf{w}(t_r)|$, $\mathbf{n} = (\mathbf{r} - \mathbf{w}(t_r))/R$, $\boldsymbol{\beta} = \mathbf{v}(t_r)/c$, and $\kappa = 1 - \mathbf{n}\cdot\boldsymbol{\beta}$.

**命题。** 对沿轨迹 $\mathbf{w}(t)$ 运动的点电荷 $q$，推迟势计算为 $\varphi = (1/4\pi\varepsilon_0)\, q/[\kappa R]_{\text{ret}}$ 与 $\mathbf{A} = (\mu_0/4\pi)\, qc\boldsymbol{\beta}/[\kappa R]_{\text{ret}} = (\boldsymbol{\beta}/c)\varphi$，其中 $R = |\mathbf{r} - \mathbf{w}(t_r)|$，$\mathbf{n} = (\mathbf{r} - \mathbf{w}(t_r))/R$，$\boldsymbol{\beta} = \mathbf{v}(t_r)/c$，$\kappa = 1 - \mathbf{n}\cdot\boldsymbol{\beta}$。

**Step 1 — Point-charge sources.** A point charge has $\rho(\mathbf{r}',t') = q\,\delta^3(\mathbf{r}' - \mathbf{w}(t'))$ and $\mathbf{J}(\mathbf{r}',t') = q\,\mathbf{v}(t')\,\delta^3(\mathbf{r}' - \mathbf{w}(t'))$, with $\mathbf{v} = \dot{\mathbf{w}}$. Substitute into the retarded potential, keeping the explicit time-delta form (before the $t'$ integration is collapsed):

**第 1 步 — 点电荷源。** 点电荷有 $\rho(\mathbf{r}',t') = q\,\delta^3(\mathbf{r}' - \mathbf{w}(t'))$ 与 $\mathbf{J}(\mathbf{r}',t') = q\,\mathbf{v}(t')\,\delta^3(\mathbf{r}' - \mathbf{w}(t'))$，$\mathbf{v} = \dot{\mathbf{w}}$。代入推迟势，保留显式时间 $\delta$ 形式（在折叠 $t'$ 积分之前）：

$$ \varphi(\mathbf{r},t) = \frac{1}{4\pi\varepsilon_0}\int d^3r' \int dt'\, \frac{\delta(t' - t + |\mathbf{r}-\mathbf{r}'|/c)}{|\mathbf{r}-\mathbf{r}'|}\, q\,\delta^3(\mathbf{r}' - \mathbf{w}(t')). $$

**Step 2 — Do the space integral.** The $\delta^3$ sets $\mathbf{r}' = \mathbf{w}(t')$, so $|\mathbf{r}-\mathbf{r}'| \to |\mathbf{r} - \mathbf{w}(t')| \equiv R(t')$:

**第 2 步 — 完成空间积分。** $\delta^3$ 令 $\mathbf{r}' = \mathbf{w}(t')$，故 $|\mathbf{r}-\mathbf{r}'| \to |\mathbf{r} - \mathbf{w}(t')| \equiv R(t')$：

$$ \varphi(\mathbf{r},t) = \frac{q}{4\pi\varepsilon_0}\int dt'\, \frac{\delta(t' - t + R(t')/c)}{R(t')}. $$

**Step 3 — Do the time integral with the Jacobian.** The remaining $\delta$ is a function of $t'$ through its argument $g(t') = t' - t + R(t')/c$. Using $\delta(g(t')) = \delta(t' - t_r)/|g'(t_r)|$, where $t_r$ is the root $g(t_r) = 0$ (the retarded time), we need $g'(t')$:

**第 3 步 — 用雅可比因子完成时间积分。** 剩余 $\delta$ 通过其宗量 $g(t') = t' - t + R(t')/c$ 依赖 $t'$。利用 $\delta(g(t')) = \delta(t' - t_r)/|g'(t_r)|$，其中 $t_r$ 为根 $g(t_r) = 0$（推迟时刻），需要 $g'(t')$：

$$ g'(t') = 1 + \frac{1}{c}\frac{dR}{dt'}. $$

Now $R = |\mathbf{r} - \mathbf{w}(t')|$, so $dR/dt' = -(\mathbf{r} - \mathbf{w})\cdot\dot{\mathbf{w}}/|\mathbf{r} - \mathbf{w}| = -\mathbf{n}\cdot\mathbf{v}$, where $\mathbf{n} = (\mathbf{r} - \mathbf{w})/R$. Hence

现 $R = |\mathbf{r} - \mathbf{w}(t')|$，故 $dR/dt' = -(\mathbf{r} - \mathbf{w})\cdot\dot{\mathbf{w}}/|\mathbf{r} - \mathbf{w}| = -\mathbf{n}\cdot\mathbf{v}$，$\mathbf{n} = (\mathbf{r} - \mathbf{w})/R$。于是

$$ g'(t') = 1 - \mathbf{n}\cdot\mathbf{v}/c = 1 - \mathbf{n}\cdot\boldsymbol{\beta} \equiv \kappa. $$

**Step 4 — Assemble the scalar potential.** The time integral picks up the factor $1/|g'(t_r)| = 1/\kappa$, evaluated at the retarded time:

**第 4 步 — 组装标量势。** 时间积分给出因子 $1/|g'(t_r)| = 1/\kappa$，在推迟时刻取值：

$$ \varphi(\mathbf{r},t) = \frac{q}{4\pi\varepsilon_0} \cdot \frac{1}{[R\kappa]_{\text{ret}}} = \boxed{\, \frac{1}{4\pi\varepsilon_0}\frac{q}{[\kappa R]_{\text{ret}}} \,}, $$

with $[\cdots]_{\text{ret}}$ meaning all quantities evaluated at $t_r$. The $\kappa = 1 - \mathbf{n}\cdot\boldsymbol{\beta}$ factor is purely kinematic: it is the Jacobian of the map $t' \mapsto g(t')$, encoding the **searchlight/Doppler compression** — while the charge moves a distance $v\,dt'$ toward the observer, the retarded "now" surface sweeps less retarded volume, so a charge approaching the field point ($\mathbf{n}\cdot\boldsymbol{\beta} \to 1$) packs its retarded contribution into a thin shell and the potential is enhanced by $1/\kappa$.

其中 $[\cdots]_{\text{ret}}$ 表示所有量在 $t_r$ 取值。$\kappa = 1 - \mathbf{n}\cdot\boldsymbol{\beta}$ 因子纯粹是运动学的：它是映射 $t' \mapsto g(t')$ 的雅可比因子，编码了**探照灯/多普勒压缩**——当电荷朝观察者移动 $v\,dt'$ 时，推迟"现在"面扫过的推迟体积更少，故趋近场点的电荷（$\mathbf{n}\cdot\boldsymbol{\beta} \to 1$）将其推迟贡献压入薄壳，势增强 $1/\kappa$ 倍。

**Step 5 — Vector potential.** The current differs from the charge density only by the factor $\mathbf{v}(t') = c\boldsymbol{\beta}(t')$, which the space integral evaluates at $\mathbf{r}' = \mathbf{w}(t')$. The identical time integral then gives

**第 5 步 — 矢量势。** 电流与电荷密度仅相差因子 $\mathbf{v}(t') = c\boldsymbol{\beta}(t')$，空间积分在 $\mathbf{r}' = \mathbf{w}(t')$ 处取值。相同的时间积分给出

$$ \mathbf{A}(\mathbf{r},t) = \frac{\mu_0}{4\pi}\frac{q\mathbf{v}}{[\kappa R]_{\text{ret}}} = \boxed{\, \frac{\mu_0}{4\pi}\frac{qc\boldsymbol{\beta}}{[\kappa R]_{\text{ret}}} = \frac{\boldsymbol{\beta}}{c}\varphi \,}, $$

using $\mu_0 c = 1/(\varepsilon_0 c)$ so that $(\mu_0/4\pi)\,qc = (1/4\pi\varepsilon_0)(q/c)$. Thus $\mathbf{A}$ and $\varphi$ carry the same $\kappa R$ denominator and $\mathbf{A} = (\mathbf{v}/c^2)\varphi = (\boldsymbol{\beta}/c)\varphi$. $\blacksquare$

利用 $\mu_0 c = 1/(\varepsilon_0 c)$，得 $(\mu_0/4\pi)\,qc = (1/4\pi\varepsilon_0)(q/c)$。故 $\mathbf{A}$ 与 $\varphi$ 含相同的 $\kappa R$ 分母，且 $\mathbf{A} = (\mathbf{v}/c^2)\varphi = (\boldsymbol{\beta}/c)\varphi$。$\blacksquare$

---

## C. Fields of a Point Charge: Velocity and Radiation (Acceleration) Fields · 点电荷的场：速度场与辐射（加速度）场

**Claim.** Differentiating the Liénard–Wiechert potentials gives $\mathbf{E} = \mathbf{E}_{\text{vel}} + \mathbf{E}_{\text{acc}}$, where the velocity field $\mathbf{E}_{\text{vel}} \propto (\mathbf{n} - \boldsymbol{\beta})/(\kappa^3 R^2)$ falls off as $1/R^2$, and the **radiation field** $\mathbf{E}_{\text{acc}} = (q/4\pi\varepsilon_0 c^2)\,[\mathbf{n} \times ((\mathbf{n} - \boldsymbol{\beta}) \times \mathbf{a})]/(\kappa^3 R)$ falls off as $1/R$, with $\mathbf{B} = (\mathbf{n} \times \mathbf{E})/c$. Only $\mathbf{E}_{\text{acc}}$ carries energy to infinity.

**命题。** 对李纳–维谢尔势求导给出 $\mathbf{E} = \mathbf{E}_{\text{vel}} + \mathbf{E}_{\text{acc}}$，其中速度场 $\mathbf{E}_{\text{vel}} \propto (\mathbf{n} - \boldsymbol{\beta})/(\kappa^3 R^2)$ 按 $1/R^2$ 衰减，**辐射场** $\mathbf{E}_{\text{acc}} = (q/4\pi\varepsilon_0 c^2)\,[\mathbf{n} \times ((\mathbf{n} - \boldsymbol{\beta}) \times \mathbf{a})]/(\kappa^3 R)$ 按 $1/R$ 衰减，$\mathbf{B} = (\mathbf{n} \times \mathbf{E})/c$。只有 $\mathbf{E}_{\text{acc}}$ 将能量带到无穷远。

**Step 1 — Fields from potentials.** The fields are $\mathbf{E} = -\boldsymbol{\nabla}\varphi - \partial\mathbf{A}/\partial t$ and $\mathbf{B} = \boldsymbol{\nabla}\times\mathbf{A}$. The subtlety is that $\varphi$ and $\mathbf{A}$ depend on $\mathbf{r}$ and $t$ both explicitly and *through* the retarded time $t_r(\mathbf{r},t)$, since $R$ appears inside $t_r = t - R(t_r)/c$. Differentiating the implicit relation gives the building blocks

**第 1 步 — 由势求场。** 场为 $\mathbf{E} = -\boldsymbol{\nabla}\varphi - \partial\mathbf{A}/\partial t$ 与 $\mathbf{B} = \boldsymbol{\nabla}\times\mathbf{A}$。微妙之处在于 $\varphi$ 与 $\mathbf{A}$ 既显式依赖 $\mathbf{r}$ 与 $t$，又*通过*推迟时刻 $t_r(\mathbf{r},t)$ 依赖，因为 $R$ 出现于 $t_r = t - R(t_r)/c$ 中。对隐式关系求导给出基本关系

$$ \frac{\partial t_r}{\partial t} = \frac{1}{\kappa}, \qquad \boldsymbol{\nabla} t_r = -\frac{\mathbf{n}}{c\kappa}, $$

which follow from differentiating $t_r = t - R(t_r)/c$ and using $dR/dt_r = -c\,\mathbf{n}\cdot\boldsymbol{\beta}$ (Section B, Step 3).

它们来自对 $t_r = t - R(t_r)/c$ 求导并使用 $dR/dt_r = -c\,\mathbf{n}\cdot\boldsymbol{\beta}$（B 节第 3 步）。

**Step 2 — Carry out the differentiation.** Applying $\boldsymbol{\nabla}$ and $\partial/\partial t$ to $\varphi = (q/4\pi\varepsilon_0)/(\kappa R)$ and $\mathbf{A} = (\boldsymbol{\beta}/c)\varphi$, and using the chain-rule factors from Step 1, the algebra (standard; e.g. Jackson, Griffiths) yields the exact field

**第 2 步 — 执行微分。** 将 $\boldsymbol{\nabla}$ 与 $\partial/\partial t$ 作用于 $\varphi = (q/4\pi\varepsilon_0)/(\kappa R)$ 与 $\mathbf{A} = (\boldsymbol{\beta}/c)\varphi$，并使用第 1 步的链式因子，代数运算（标准；如 Jackson、Griffiths）给出精确场

$$ \mathbf{E}(\mathbf{r},t) = \frac{q}{4\pi\varepsilon_0}\left\{ \frac{(\mathbf{n} - \boldsymbol{\beta})(1 - \beta^2)}{\kappa^3 R^2} + \frac{\mathbf{n} \times [(\mathbf{n} - \boldsymbol{\beta}) \times \mathbf{a}]}{c^2\kappa^3 R} \right\}_{\text{ret}}. $$

**Step 3 — Identify the two pieces.** The first term, $\mathbf{E}_{\text{vel}} \propto (\mathbf{n} - \boldsymbol{\beta})(1 - \beta^2)/(\kappa^3 R^2)$, is independent of acceleration and falls off as $1/R^2$; it is the boosted Coulomb (generalized "velocity") field, reducing to $q/(4\pi\varepsilon_0 R^2)$ when $\beta \to 0$. The second term,

**第 3 步 — 辨认两部分。** 第一项 $\mathbf{E}_{\text{vel}} \propto (\mathbf{n} - \boldsymbol{\beta})(1 - \beta^2)/(\kappa^3 R^2)$ 与加速度无关，按 $1/R^2$ 衰减；它是洛伦兹变换的库仑（广义"速度"）场，$\beta \to 0$ 时退化为 $q/(4\pi\varepsilon_0 R^2)$。第二项，

$$ \boxed{\, \mathbf{E}_{\text{acc}} = \frac{q}{4\pi\varepsilon_0 c^2}\frac{\mathbf{n} \times ((\mathbf{n} - \boldsymbol{\beta}) \times \mathbf{a})}{\kappa^3 R} \,}, $$

is linear in the acceleration $\mathbf{a}$ and falls off only as $1/R$. The magnetic field is exactly $\mathbf{B} = (\mathbf{n} \times \mathbf{E})/c$.

正比于加速度 $\mathbf{a}$，仅按 $1/R$ 衰减。磁场精确为 $\mathbf{B} = (\mathbf{n} \times \mathbf{E})/c$。

**Step 4 — Only the $1/R$ field radiates.** The Poynting flux is $\mathbf{S} = (1/\mu_0)\mathbf{E}\times\mathbf{B}$, with $|\mathbf{S}| \propto |\mathbf{E}|^2$. Through a sphere of radius $R$ the power is $\oint \mathbf{S}\cdot d\mathbf{A} \propto |\mathbf{E}|^2 R^2$. The velocity field gives $|\mathbf{E}_{\text{vel}}|^2 R^2 \propto R^2/R^4 = 1/R^2 \to 0$ as $R \to \infty$: no net energy escapes. The acceleration field gives $|\mathbf{E}_{\text{acc}}|^2 R^2 \propto R^2/R^2 = \text{const}$, a finite, $R$-independent flux. Hence **only the acceleration (radiation) field transports energy to infinity** — radiation requires acceleration. $\blacksquare$

**第 4 步 — 只有 $1/R$ 场辐射。** 坡印亭通量 $\mathbf{S} = (1/\mu_0)\mathbf{E}\times\mathbf{B}$，$|\mathbf{S}| \propto |\mathbf{E}|^2$。穿过半径 $R$ 球面的功率为 $\oint \mathbf{S}\cdot d\mathbf{A} \propto |\mathbf{E}|^2 R^2$。速度场给出 $|\mathbf{E}_{\text{vel}}|^2 R^2 \propto R^2/R^4 = 1/R^2 \to 0$（$R \to \infty$）：无净能量逸出。加速度场给出 $|\mathbf{E}_{\text{acc}}|^2 R^2 \propto R^2/R^2 = \text{常数}$，给出有限、与 $R$ 无关的通量。故**只有加速度（辐射）场将能量输运到无穷远**——辐射需要加速度。$\blacksquare$

---

## D. Electric-Dipole Radiation and Reduction to Larmor · 电偶极辐射及向拉莫尔公式的退化

**Claim.** For a localized oscillating source of dipole moment $\mathbf{p}(t)$, the radiated angular power is $dP/d\Omega = (\mu_0 \ddot{p}^2/16\pi^2 c)\sin^2\theta$ and the total power is $P = \mu_0 \ddot{p}^2/(6\pi c) = \ddot{p}^2/(6\pi\varepsilon_0 c^3)$. For a single charge ($\mathbf{p} = q\mathbf{d}$) this reduces to the Larmor formula $P = \mu_0 q^2 a^2/(6\pi c)$ of Module 1.11.

**命题。** 对偶极矩为 $\mathbf{p}(t)$ 的局域振荡源，辐射角功率为 $dP/d\Omega = (\mu_0 \ddot{p}^2/16\pi^2 c)\sin^2\theta$，总功率为 $P = \mu_0 \ddot{p}^2/(6\pi c) = \ddot{p}^2/(6\pi\varepsilon_0 c^3)$。对单个电荷（$\mathbf{p} = q\mathbf{d}$），它退化为模块 1.11 的拉莫尔公式 $P = \mu_0 q^2 a^2/(6\pi c)$。

**Step 1 — Radiation field of a dipole.** In the radiation (far) zone of a slowly moving source ($\beta \ll 1$), set $\boldsymbol{\beta} \to 0$ in the acceleration field of Section C and sum over the charges. With $\mathbf{p}(t) = \int \mathbf{r}'\rho(\mathbf{r}',t)\,d^3r'$ so that $\ddot{\mathbf{p}} = \int \mathbf{r}'\ddot{\rho}\,d^3r' = \sum q\mathbf{a}$ (the collective "$q\mathbf{a}$"), the non-relativistic radiation field is

**第 1 步 — 偶极的辐射场。** 在缓变源（$\beta \ll 1$）的辐射（远）区，将 C 节加速度场中 $\boldsymbol{\beta} \to 0$ 并对电荷求和。设 $\mathbf{p}(t) = \int \mathbf{r}'\rho(\mathbf{r}',t)\,d^3r'$，故 $\ddot{\mathbf{p}} = \int \mathbf{r}'\ddot{\rho}\,d^3r' = \sum q\mathbf{a}$（集体的"$q\mathbf{a}$"），非相对论辐射场为

$$ \mathbf{E}_{\text{rad}} = \frac{\mu_0}{4\pi r}[\mathbf{n} \times (\mathbf{n} \times \ddot{\mathbf{p}})]_{\text{ret}}, \qquad \mathbf{B}_{\text{rad}} = \frac{\mathbf{n} \times \mathbf{E}_{\text{rad}}}{c}, $$

evaluated at the retarded time $t_r = t - r/c$. The magnitude is $|\mathbf{E}_{\text{rad}}| = (\mu_0/4\pi r)\,\ddot{p}\sin\theta$, $\theta$ being the angle between $\mathbf{n}$ and $\ddot{\mathbf{p}}$.

在推迟时刻 $t_r = t - r/c$ 取值。其大小为 $|\mathbf{E}_{\text{rad}}| = (\mu_0/4\pi r)\,\ddot{p}\sin\theta$，$\theta$ 为 $\mathbf{n}$ 与 $\ddot{\mathbf{p}}$ 的夹角。

**Step 2 — Poynting flux.** The radiated power per unit area is $|\mathbf{S}| = |\mathbf{E}_{\text{rad}}|^2/(\mu_0 c)$ (since $|\mathbf{E}_{\text{rad}}\times\mathbf{B}_{\text{rad}}|/\mu_0 = |\mathbf{E}_{\text{rad}}|^2/(\mu_0 c)$ for the orthogonal radiation fields):

**第 2 步 — 坡印亭通量。** 单位面积辐射功率为 $|\mathbf{S}| = |\mathbf{E}_{\text{rad}}|^2/(\mu_0 c)$（因正交辐射场 $|\mathbf{E}_{\text{rad}}\times\mathbf{B}_{\text{rad}}|/\mu_0 = |\mathbf{E}_{\text{rad}}|^2/(\mu_0 c)$）：

$$ |\mathbf{S}| = \frac{1}{\mu_0 c}\left(\frac{\mu_0}{4\pi r}\right)^2 \ddot{p}^2\sin^2\theta = \frac{\mu_0}{16\pi^2 c}\frac{\ddot{p}^2\sin^2\theta}{r^2}. $$

**Step 3 — Angular power.** Multiply by $r^2$ to get power per solid angle $d\Omega$:

**第 3 步 — 角功率。** 乘以 $r^2$ 得单位立体角功率 $d\Omega$：

$$ \boxed{\, \frac{dP}{d\Omega} = r^2|\mathbf{S}| = \frac{\mu_0 \ddot{p}^2}{16\pi^2 c}\sin^2\theta \,}. $$

This is the dipole doughnut: zero along the dipole axis ($\theta = 0, \pi$), maximum broadside ($\theta = \pi/2$).

这是偶极甜甜圈：沿偶极轴（$\theta = 0, \pi$）为零，垂直方向（$\theta = \pi/2$）最大。

**Step 4 — Integrate over the sphere.** With $d\Omega = \sin\theta\,d\theta\,d\phi$:

**第 4 步 — 对球面积分。** 取 $d\Omega = \sin\theta\,d\theta\,d\phi$：

$$ P = \frac{\mu_0 \ddot{p}^2}{16\pi^2 c}\int_0^{2\pi} d\phi \int_0^\pi \sin^2\theta\cdot\sin\theta\,d\theta = \frac{\mu_0 \ddot{p}^2}{16\pi^2 c}\cdot 2\pi\cdot\frac{4}{3}, $$

using $\int_0^\pi \sin^3\theta\,d\theta = 4/3$ (Module 1.11, Section D). Therefore

利用 $\int_0^\pi \sin^3\theta\,d\theta = 4/3$（模块 1.11，D 节）。因此

$$ \boxed{\, P = \frac{\mu_0 \ddot{p}^2}{6\pi c} \,}, \qquad \text{equivalently} \qquad \boxed{\, P = \frac{\ddot{p}^2}{6\pi\varepsilon_0 c^3} \,} \quad (\text{using } 1/\varepsilon_0 = \mu_0 c^2). $$

**Step 5 — Reduction to Larmor.** A single point charge has dipole moment $\mathbf{p} = q\mathbf{d}$, where $\mathbf{d}(t)$ is its position; then $\dot{\mathbf{p}} = q\dot{\mathbf{d}} = q\mathbf{v}$ and $\ddot{\mathbf{p}} = q\dot{\mathbf{v}} = q\mathbf{a}$. Substituting $\ddot{p}^2 = q^2 a^2$:

**第 5 步 — 退化为拉莫尔公式。** 单个点电荷的偶极矩为 $\mathbf{p} = q\mathbf{d}$，$\mathbf{d}(t)$ 为其位置；则 $\dot{\mathbf{p}} = q\dot{\mathbf{d}} = q\mathbf{v}$，$\ddot{\mathbf{p}} = q\dot{\mathbf{v}} = q\mathbf{a}$。代入 $\ddot{p}^2 = q^2 a^2$：

$$ P = \frac{\mu_0 (qa)^2}{6\pi c} = \boxed{\, \frac{\mu_0 q^2 a^2}{6\pi c} \,}, $$

exactly the **Larmor formula** of Module 1.11. The dipole result is the natural extension to an arbitrary localized source; we do not re-derive Larmor here but recover it as the one-charge special case. $\blacksquare$

正是模块 1.11 的**拉莫尔公式**。偶极结果是向任意局域源的自然推广；此处不重新推导拉莫尔公式，而是将其作为单电荷特例重新得到。$\blacksquare$

---

## E. Radiation Reaction: the Abraham–Lorentz Force · 辐射阻尼：阿布拉罕–洛伦兹力

**Claim.** Energy conservation forces a self-force $\mathbf{F}_{\text{rad}} = (\mu_0 q^2/6\pi c)\dot{\mathbf{a}} = (q^2/6\pi\varepsilon_0 c^3)\dot{\mathbf{a}}$ on a radiating charge, with characteristic time $\tau = \mu_0 q^2/(6\pi mc) = q^2/(6\pi\varepsilon_0 mc^3)$. The resulting equation of motion exhibits runaway and pre-acceleration pathologies.

**命题。** 能量守恒迫使辐射电荷受自力 $\mathbf{F}_{\text{rad}} = (\mu_0 q^2/6\pi c)\dot{\mathbf{a}} = (q^2/6\pi\varepsilon_0 c^3)\dot{\mathbf{a}}$，特征时间 $\tau = \mu_0 q^2/(6\pi mc) = q^2/(6\pi\varepsilon_0 mc^3)$。由此得到的运动方程呈现失控与预加速病态。

**Step 1 — Energy-balance requirement.** The charge radiates Larmor power $P = \mu_0 q^2 a^2/(6\pi c)$ (Section D). By energy conservation this energy is drained from the particle's mechanical energy, so the self-force $\mathbf{F}_{\text{rad}}$ must do negative work at exactly this rate, on average over any interval where the motion is periodic (so the charge returns to its initial state):

**第 1 步 — 能量平衡要求。** 电荷辐射拉莫尔功率 $P = \mu_0 q^2 a^2/(6\pi c)$（D 节）。由能量守恒，该能量从粒子的机械能中抽取，故自力 $\mathbf{F}_{\text{rad}}$ 必以恰好此速率做负功，在运动为周期（电荷回到初态）的任意区间上平均：

$$ \int_{t_1}^{t_2} \mathbf{F}_{\text{rad}}\cdot\mathbf{v}\,dt = -\int_{t_1}^{t_2} \frac{\mu_0 q^2}{6\pi c} a^2\,dt. $$

**Step 2 — Rewrite $a^2$ via integration by parts.** Note $a^2 = \mathbf{a}\cdot\mathbf{a} = \dot{\mathbf{v}}\cdot\dot{\mathbf{v}}$ ($\dot{\mathbf{v}}$ is the jerk). Use the identity $\dot{\mathbf{v}}\cdot\dot{\mathbf{v}} = d(\dot{\mathbf{v}}\cdot\mathbf{v})/dt - \ddot{\mathbf{v}}\cdot\mathbf{v}$ (since $d(\dot{\mathbf{v}}\cdot\mathbf{v})/dt = \ddot{\mathbf{v}}\cdot\mathbf{v} + \dot{\mathbf{v}}\cdot\dot{\mathbf{v}}$). Integrate the right side:

**第 2 步 — 用分部积分改写 $a^2$。** 注意 $a^2 = \mathbf{a}\cdot\mathbf{a} = \dot{\mathbf{v}}\cdot\dot{\mathbf{v}}$。利用恒等式 $\dot{\mathbf{v}}\cdot\dot{\mathbf{v}} = d(\dot{\mathbf{v}}\cdot\mathbf{v})/dt - \ddot{\mathbf{v}}\cdot\mathbf{v}$（因 $d(\dot{\mathbf{v}}\cdot\mathbf{v})/dt = \ddot{\mathbf{v}}\cdot\mathbf{v} + \dot{\mathbf{v}}\cdot\dot{\mathbf{v}}$）。对右侧积分：

$$ \int_{t_1}^{t_2} a^2\,dt = \int_{t_1}^{t_2} \dot{\mathbf{v}}\cdot\dot{\mathbf{v}}\,dt = [\dot{\mathbf{v}}\cdot\mathbf{v}]_{t_1}^{t_2} - \int_{t_1}^{t_2} \ddot{\mathbf{v}}\cdot\mathbf{v}\,dt. $$

For periodic (or otherwise vanishing-boundary) motion, the boundary term $[\dot{\mathbf{v}}\cdot\mathbf{v}]_{t_1}^{t_2} = [\mathbf{a}\cdot\mathbf{v}]_{t_1}^{t_2}$ vanishes, leaving

对周期（或边界项为零）的运动，边界项 $[\dot{\mathbf{v}}\cdot\mathbf{v}]_{t_1}^{t_2} = [\mathbf{a}\cdot\mathbf{v}]_{t_1}^{t_2}$ 消失，剩

$$ \int_{t_1}^{t_2} a^2\,dt = -\int_{t_1}^{t_2} \ddot{\mathbf{v}}\cdot\mathbf{v}\,dt = -\int_{t_1}^{t_2} \dot{\mathbf{a}}\cdot\mathbf{v}\,dt. $$

**Step 3 — Read off the force.** Substitute into the energy balance of Step 1:

**第 3 步 — 读出力。** 代入第 1 步的能量平衡：

$$ \int_{t_1}^{t_2} \mathbf{F}_{\text{rad}}\cdot\mathbf{v}\,dt = -\frac{\mu_0 q^2}{6\pi c}\int_{t_1}^{t_2} a^2\,dt = +\frac{\mu_0 q^2}{6\pi c}\int_{t_1}^{t_2} \dot{\mathbf{a}}\cdot\mathbf{v}\,dt. $$

This must hold for arbitrary periodic motion, so the integrands match (up to terms integrating to zero):

此须对任意周期运动成立，故被积函数匹配（至多差积分为零的项）：

$$ \boxed{\, \mathbf{F}_{\text{rad}} = \frac{\mu_0 q^2}{6\pi c}\dot{\mathbf{a}} = \frac{q^2}{6\pi\varepsilon_0 c^3}\dot{\mathbf{a}} \,}, $$

the **Abraham–Lorentz force**, proportional to the jerk $\dot{\mathbf{a}}$ (using $1/\varepsilon_0 = \mu_0 c^2$ for the second form).

即**阿布拉罕–洛伦兹力**，正比于急动度 $\dot{\mathbf{a}}$（第二种形式用 $1/\varepsilon_0 = \mu_0 c^2$）。

**Step 4 — Characteristic time.** Write $\mathbf{F}_{\text{rad}} = m\tau\dot{\mathbf{a}}$. Matching coefficients defines

**第 4 步 — 特征时间。** 写 $\mathbf{F}_{\text{rad}} = m\tau\dot{\mathbf{a}}$。匹配系数定义

$$ \boxed{\, \tau = \frac{\mu_0 q^2}{6\pi mc} = \frac{q^2}{6\pi\varepsilon_0 mc^3} \,}. $$

For the electron, $\tau \approx 6.3 \times 10^{-24}\ \mathrm{s}$ — the time light takes to cross a classical electron radius. Newton's law with the self-force becomes $m\mathbf{a} = \mathbf{F}_{\text{ext}} + m\tau\dot{\mathbf{a}}$, i.e. $\mathbf{a} - \tau\dot{\mathbf{a}} = \mathbf{F}_{\text{ext}}/m$ (the Abraham–Lorentz equation).

对电子，$\tau \approx 6.3 \times 10^{-24}\ \mathrm{s}$——光穿过经典电子半径的时间。含自力的牛顿定律变为 $m\mathbf{a} = \mathbf{F}_{\text{ext}} + m\tau\dot{\mathbf{a}}$，即 $\mathbf{a} - \tau\dot{\mathbf{a}} = \mathbf{F}_{\text{ext}}/m$（阿布拉罕–洛伦兹方程）。

**Step 5 — Runaway and pre-acceleration pathologies.** With no external force ($\mathbf{F}_{\text{ext}} = 0$), the equation $\mathbf{a} - \tau\dot{\mathbf{a}} = 0$ has the solution $\mathbf{a}(t) = \mathbf{a}(0) e^{t/\tau}$: the acceleration grows without bound — an unphysical **runaway**. Demanding $\mathbf{a} \to 0$ as $t \to \infty$ instead forces the integral (acausal) solution

**第 5 步 — 失控与预加速病态。** 无外力（$\mathbf{F}_{\text{ext}} = 0$）时，方程 $\mathbf{a} - \tau\dot{\mathbf{a}} = 0$ 有解 $\mathbf{a}(t) = \mathbf{a}(0) e^{t/\tau}$：加速度无界增长——非物理的**失控**。改为要求 $t \to \infty$ 时 $\mathbf{a} \to 0$ 则迫使积分（非因果）解

$$ \mathbf{a}(t) = \frac{1}{m\tau}\int_t^\infty e^{-(t'-t)/\tau}\mathbf{F}_{\text{ext}}(t')\,dt', $$

in which $\mathbf{a}(t)$ depends on the **future** force $\mathbf{F}_{\text{ext}}(t' > t)$: the charge begins to accelerate a time $\sim \tau$ *before* the force is applied — **pre-acceleration**. Both pathologies signal that the rigid point charge is an over-idealization; they are removed only in QED, where $\mathbf{F}_{\text{rad}}$ is the classical limit of the electron self-energy and the divergences are absorbed by mass renormalization (Modules 8.2 / 6.x). $\blacksquare$

其中 $\mathbf{a}(t)$ 依赖于**未来**的力 $\mathbf{F}_{\text{ext}}(t' > t)$：电荷在力施加*之前*约 $\tau$ 时间便开始加速——**预加速**。两种病态都表明刚性点电荷是过度理想化；它们只在量子电动力学中消除，其中 $\mathbf{F}_{\text{rad}}$ 是电子自能的经典极限，发散通过质量重整化被吸收（模块 8.2 / 6.x）。$\blacksquare$

---

*The retarded potentials and Liénard–Wiechert fields are the complete classical solution of radiation from moving charges; the dipole formula organizes the leading multipole emission; and the Abraham–Lorentz force — together with its runaway/pre-acceleration pathologies — marks the precise point at which the classical theory of the electron must yield to quantum electrodynamics.*

*推迟势与李纳–维谢尔场是运动电荷辐射的完整经典解；偶极公式组织领头多极发射；阿布拉罕–洛伦兹力——连同其失控/预加速病态——标志着电子的经典理论必须让位于量子电动力学的确切节点。*

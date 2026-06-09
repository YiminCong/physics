---
title: "Derivations — Module 1.3: Lagrangian Mechanics"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 1.3: Lagrangian Mechanics
# 推导 — 模块 1.3：拉格朗日力学

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.3](./module-1.3-lagrangian-mechanics.md). Full step-by-step proofs of every result quoted there. English first, then 中文.
> [模块 1.3](./module-1.3-lagrangian-mechanics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Euler–Lagrange Equations from $\delta S = 0$ · 从 $\delta S = 0$ 推导欧拉–拉格朗日方程

**Claim.** For a system with generalised coordinates $q(t)$ and Lagrangian $L(q, \dot{q}, t)$, requiring the action $S = \int_{t_1}^{t_2} L\, dt$ to be stationary under all variations $\delta q$ that vanish at the endpoints ($\delta q(t_1) = \delta q(t_2) = 0$) yields the Euler–Lagrange equation:

$$ \frac{d}{dt}\Big(\frac{\partial L}{\partial \dot{q}}\Big) - \frac{\partial L}{\partial q} = 0. $$

(For brevity we treat a single degree of freedom; the multi-coordinate case follows by applying the argument independently to each $q_i$.)

**命题。** 对于广义坐标为 $q(t)$、拉格朗日量为 $L(q, \dot{q}, t)$ 的系统，要求作用量 $S = \int_{t_1}^{t_2} L\, dt$ 在所有端点处为零的变分 $\delta q$（$\delta q(t_1) = \delta q(t_2) = 0$）下取驻值，可得欧拉–拉格朗日方程：

$$ \frac{d}{dt}\Big(\frac{\partial L}{\partial \dot{q}}\Big) - \frac{\partial L}{\partial q} = 0. $$

（简洁起见，我们处理单自由度情形；多坐标情形通过对每个 $q_i$ 独立应用同一论证得到。）

**Step 1 — Perturb the path.** Let $q(t)$ be the physical trajectory and consider a one-parameter family of nearby paths:

**第 1 步 — 扰动路径。** 设 $q(t)$ 为物理轨迹，考虑一族邻近路径：

$$ q_\varepsilon(t) = q(t) + \varepsilon\,\eta(t), $$

where $\varepsilon$ is a small real parameter and $\eta(t)$ is an arbitrary smooth function satisfying the boundary conditions $\eta(t_1) = \eta(t_2) = 0$.

其中 $\varepsilon$ 是小实数参数，$\eta(t)$ 是满足边界条件 $\eta(t_1) = \eta(t_2) = 0$ 的任意光滑函数。

**Step 2 — Expand the action to first order in $\varepsilon$.** The action evaluated on $q_\varepsilon$ is:

**第 2 步 — 将作用量展开至 $\varepsilon$ 的一阶。** 在 $q_\varepsilon$ 上计算的作用量为：

$$ S(\varepsilon) = \int_{t_1}^{t_2} L(q + \varepsilon\eta,\, \dot{q} + \varepsilon\dot{\eta},\, t)\, dt. $$

Taylor-expanding the integrand to first order in $\varepsilon$:

将被积函数关于 $\varepsilon$ 一阶泰勒展开：

$$ L(q + \varepsilon\eta,\, \dot{q} + \varepsilon\dot{\eta},\, t) = L(q, \dot{q}, t) + \varepsilon\Big(\frac{\partial L}{\partial q}\,\eta + \frac{\partial L}{\partial \dot{q}}\,\dot{\eta}\Big) + O(\varepsilon^2). $$

**Step 3 — Stationarity condition.** Stationarity of $S$ requires $dS/d\varepsilon|_{\varepsilon=0} = 0$:

**第 3 步 — 驻值条件。** $S$ 取驻值要求 $dS/d\varepsilon|_{\varepsilon=0} = 0$：

$$ \delta S = \int_{t_1}^{t_2} \Big(\frac{\partial L}{\partial q}\,\eta + \frac{\partial L}{\partial \dot{q}}\,\dot{\eta}\Big)\, dt = 0. $$

**Step 4 — Integration by parts on the second term.** The second term involves $\dot{\eta}$. Integrate by parts, using $u = \partial L/\partial \dot{q}$ and $dv = \dot{\eta}\, dt$:

**第 4 步 — 对第二项分部积分。** 第二项含 $\dot{\eta}$。令 $u = \partial L/\partial \dot{q}$，$dv = \dot{\eta}\, dt$，分部积分：

$$ \int_{t_1}^{t_2} \frac{\partial L}{\partial \dot{q}}\,\dot{\eta}\, dt = \Big[\frac{\partial L}{\partial \dot{q}}\,\eta\Big]_{t_1}^{t_2} - \int_{t_1}^{t_2} \frac{d}{dt}\Big(\frac{\partial L}{\partial \dot{q}}\Big)\,\eta\, dt. $$

**Step 5 — Boundary terms vanish.** The boundary term $\big[(\partial L/\partial \dot{q})\,\eta\big]_{t_1}^{t_2} = 0$ because $\eta(t_1) = \eta(t_2) = 0$ by assumption.

**第 5 步 — 边界项消失。** 边界项 $\big[(\partial L/\partial \dot{q})\,\eta\big]_{t_1}^{t_2} = 0$，因为由假设 $\eta(t_1) = \eta(t_2) = 0$。

**Step 6 — Combine into a single integral.** Substituting back:

**第 6 步 — 合并为单一积分。** 代回得：

$$ \delta S = \int_{t_1}^{t_2} \Big(\frac{\partial L}{\partial q} - \frac{d}{dt}\Big(\frac{\partial L}{\partial \dot{q}}\Big)\Big)\,\eta\, dt = 0. $$

**Step 7 — Apply the fundamental lemma of the calculus of variations.** Since $\delta S = 0$ for every arbitrary smooth $\eta$, the integrand must vanish identically (if it were nonzero at some point, we could choose $\eta$ to have the same sign there, making the integral nonzero — a contradiction):

**第 7 步 — 应用变分法基本引理。** 由于对任意光滑 $\eta$ 均有 $\delta S = 0$，被积函数必须恒等于零（若在某点不为零，可选取 $\eta$ 在该点与之同号，使积分不为零——矛盾）：

$$ \frac{\partial L}{\partial q} - \frac{d}{dt}\Big(\frac{\partial L}{\partial \dot{q}}\Big) = 0, \quad\text{i.e.}\quad \boxed{\, \frac{d}{dt}\Big(\frac{\partial L}{\partial \dot{q}}\Big) - \frac{\partial L}{\partial q} = 0 \,} \qquad \blacksquare $$

---

## B. Equivalence to Newton's Second Law for $L = T - V$ · $L = T - V$ 时与牛顿第二定律的等价性

**Claim.** For a particle in Cartesian coordinates with $L = T - V = \tfrac12 m \dot{x}^2 - V(x)$, the Euler–Lagrange equation is equivalent to Newton's second law $m\ddot{x} = -dV/dx$.

**命题。** 对于笛卡尔坐标中的粒子，$L = T - V = \tfrac12 m \dot{x}^2 - V(x)$，欧拉–拉格朗日方程等价于牛顿第二定律 $m\ddot{x} = -dV/dx$。

**Step 1 — Compute the partial derivatives.** With $L = \tfrac12 m\dot{x}^2 - V(x)$:

**第 1 步 — 计算偏导数。** 对于 $L = \tfrac12 m\dot{x}^2 - V(x)$：

$$ \frac{\partial L}{\partial \dot{x}} = m\dot{x}, \qquad \frac{\partial L}{\partial x} = -\frac{dV}{dx}. $$

**Step 2 — Apply the Euler–Lagrange equation.** The E-L equation $\dfrac{d}{dt}\big(\dfrac{\partial L}{\partial \dot{x}}\big) - \dfrac{\partial L}{\partial x} = 0$ gives:

**第 2 步 — 应用欧拉–拉格朗日方程。** 欧拉–拉格朗日方程 $\dfrac{d}{dt}\big(\dfrac{\partial L}{\partial \dot{x}}\big) - \dfrac{\partial L}{\partial x} = 0$ 给出：

$$ \frac{d}{dt}(m\dot{x}) - \Big(-\frac{dV}{dx}\Big) = 0 \quad\implies\quad m\ddot{x} + \frac{dV}{dx} = 0 \quad\implies\quad \boxed{\, m\ddot{x} = -\frac{dV}{dx} = F \,} \qquad \blacksquare $$

This confirms that the Euler–Lagrange equations are precisely Newton's equations in disguise when $L = T - V$.

这证实了当 $L = T - V$ 时，欧拉–拉格朗日方程恰好是牛顿方程的另一种形式。

---

## C. The Simple Pendulum via Euler–Lagrange · 用欧拉–拉格朗日方程求解单摆

**Claim.** For a simple pendulum of length $\ell$ and mass $m$, the Euler–Lagrange equation with generalised coordinate $\theta$ gives the exact equation of motion $\ell\ddot{\theta} + g \sin\theta = 0$.

**命题。** 对于摆长为 $\ell$、质量为 $m$ 的单摆，以 $\theta$ 为广义坐标的欧拉–拉格朗日方程给出精确运动方程 $\ell\ddot{\theta} + g \sin\theta = 0$。

**Step 1 — Identify the kinetic and potential energies.** The bob moves on a circle of radius $\ell$. Its speed is $\ell\dot{\theta}$, so:

**第 1 步 — 确定动能和势能。** 摆球在半径为 $\ell$ 的圆上运动，速度为 $\ell\dot{\theta}$，故：

$$ T = \tfrac12 m(\ell\dot{\theta})^2 = \tfrac12 m\ell^2\dot{\theta}^2. $$

Taking the pivot as the reference level, the height of the bob below the pivot is $\ell \cos\theta$, so the height above the lowest point is $\ell(1 - \cos\theta)$:

以转轴为参考零点，摆球在最低点以上的高度为 $\ell(1 - \cos\theta)$：

$$ V = mg\ell(1 - \cos\theta). $$

**Step 2 — Write the Lagrangian.**

**第 2 步 — 写出拉格朗日量。**

$$ L = T - V = \tfrac12 m\ell^2\dot{\theta}^2 - mg\ell(1 - \cos\theta). $$

**Step 3 — Compute the required partial derivatives.**

**第 3 步 — 计算所需的偏导数。**

$$ \frac{\partial L}{\partial \dot{\theta}} = m\ell^2\dot{\theta}, \qquad \frac{d}{dt}\Big(\frac{\partial L}{\partial \dot{\theta}}\Big) = m\ell^2\ddot{\theta}, \qquad \frac{\partial L}{\partial \theta} = -mg\ell \sin\theta. $$

**Step 4 — Apply the Euler–Lagrange equation.** $\dfrac{d}{dt}\big(\dfrac{\partial L}{\partial \dot{\theta}}\big) - \dfrac{\partial L}{\partial \theta} = 0$ gives:

**第 4 步 — 应用欧拉–拉格朗日方程。** $\dfrac{d}{dt}\big(\dfrac{\partial L}{\partial \dot{\theta}}\big) - \dfrac{\partial L}{\partial \theta} = 0$ 给出：

$$ m\ell^2\ddot{\theta} - (-mg\ell \sin\theta) = 0 \quad\implies\quad m\ell^2\ddot{\theta} + mg\ell \sin\theta = 0. $$

Dividing by $m\ell$:

除以 $m\ell$：

$$ \boxed{\, \ell\ddot{\theta} + g \sin\theta = 0 \,} \qquad \blacksquare $$

**Step 5 — Small-angle approximation.** For small $\theta$, $\sin\theta \approx \theta$, giving $\ell\ddot{\theta} + g\theta = 0$, i.e. $\ddot{\theta} = -(g/\ell)\theta$. This is simple harmonic motion with angular frequency $\omega_0 = \sqrt{g/\ell}$ and period $T = 2\pi\sqrt{\ell/g}$, independent of mass and (for small amplitudes) of amplitude.

**第 5 步 — 小角近似。** 对于小 $\theta$，$\sin\theta \approx \theta$，得 $\ell\ddot{\theta} + g\theta = 0$，即 $\ddot{\theta} = -(g/\ell)\theta$。这是角频率 $\omega_0 = \sqrt{g/\ell}$、周期 $T = 2\pi\sqrt{\ell/g}$ 的简谐运动，与质量无关，（在小振幅下）与振幅无关。

---

## D. Cyclic Coordinates and Conserved Momenta · 循环坐标与守恒动量

**Claim.** If $\partial L/\partial q_i = 0$ (coordinate $q_i$ does not appear explicitly in $L$), then the conjugate momentum $p_i = \partial L/\partial \dot{q}_i$ is conserved: $dp_i/dt = 0$.

**命题。** 若 $\partial L/\partial q_i = 0$（坐标 $q_i$ 不显含于 $L$ 中），则共轭动量 $p_i = \partial L/\partial \dot{q}_i$ 守恒：$dp_i/dt = 0$。

**Proof.** The Euler–Lagrange equation for $q_i$ states:

**证明。** $q_i$ 的欧拉–拉格朗日方程为：

$$ \frac{d}{dt}\Big(\frac{\partial L}{\partial \dot{q}_i}\Big) = \frac{\partial L}{\partial q_i}. $$

If $\partial L/\partial q_i = 0$, this becomes $dp_i/dt = \dfrac{d}{dt}\big(\dfrac{\partial L}{\partial \dot{q}_i}\big) = 0$, so $p_i = \text{const}$. $\blacksquare$

若 $\partial L/\partial q_i = 0$，则变为 $dp_i/dt = \dfrac{d}{dt}\big(\dfrac{\partial L}{\partial \dot{q}_i}\big) = 0$，故 $p_i = $ 常数。$\blacksquare$

**Example.** For a particle in 2D polar coordinates $(r, \varphi)$ with central potential $V(r)$: $L = \tfrac12 m(\dot{r}^2 + r^2\dot{\varphi}^2) - V(r)$. Since $\partial L/\partial \varphi = 0$, the conjugate momentum $p_\varphi = \partial L/\partial \dot{\varphi} = mr^2\dot{\varphi}$ is conserved — this is the angular momentum $L = mr^2\dot{\varphi}$.

**例。** 对于极坐标 $(r, \varphi)$ 中处于有心势 $V(r)$ 的粒子：$L = \tfrac12 m(\dot{r}^2 + r^2\dot{\varphi}^2) - V(r)$。由于 $\partial L/\partial \varphi = 0$，共轭动量 $p_\varphi = \partial L/\partial \dot{\varphi} = mr^2\dot{\varphi}$ 守恒——这就是角动量 $L = mr^2\dot{\varphi}$。

# Derivations — Module 7.3: Geodesics & the Motion of Particles
# 推导 — 模块 7.3：测地线与粒子运动

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 7.3](./module-7.3-geodesics-and-motion-of-particles.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 7.3](./module-7.3-geodesics-and-motion-of-particles.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Geodesic Equation from the Variational Principle · 从变分原理推导测地线方程

**Claim.** Extremizing the proper-time functional $S = \int d\tau = \int \sqrt{-g_{\mu\nu} (dx^\mu/d\lambda)(dx^\nu/d\lambda)}\, d\lambda$ with respect to the worldline $x^\mu(\lambda)$ yields the geodesic equation

$$ d^2x^\mu/d\tau^2 + \Gamma^{\mu}{}_{\alpha\beta} (dx^\alpha/d\tau)(dx^\beta/d\tau) = 0. $$

**命题。** 对固有时泛函 $S = \int d\tau = \int \sqrt{-g_{\mu\nu} (dx^\mu/d\lambda)(dx^\nu/d\lambda)}\, d\lambda$ 关于世界线 $x^\mu(\lambda)$ 取极值，得到测地线方程

$$ d^2x^\mu/d\tau^2 + \Gamma^{\mu}{}_{\alpha\beta} (dx^\alpha/d\tau)(dx^\beta/d\tau) = 0. $$

**Step 1 — Choose a convenient Lagrangian.** Extremizing $\int d\tau$ is equivalent to extremizing the squared-length functional because the square root is monotone. It is technically simpler to work with the Lagrangian

**第 1 步 — 选择方便的拉格朗日量。** 极值化 $\int d\tau$ 等价于极值化平方长度泛函，因为平方根是单调函数。在技术上，使用拉格朗日量更简便：

$$ L = g_{\mu\nu} (dx^\mu/d\tau)(dx^\nu/d\tau) = g_{\mu\nu} \dot{x}^\mu \dot{x}^\nu, $$

where an overdot denotes $d/d\tau$ (proper-time derivative). For a massive particle this equals $-c^2$ along the worldline. Varying $\int L\, d\tau$ gives the same Euler–Lagrange equations as varying $\int \sqrt{-L}\, d\tau$, provided $\tau$ is affine (which it is for proper time). This is the standard trick used to avoid the square root.

其中点号表示 $d/d\tau$（固有时导数）。对于有质量粒子，沿世界线此值等于 $-c^2$。对 $\int L\, d\tau$ 变分与对 $\int \sqrt{-L}\, d\tau$ 变分给出相同的欧拉-拉格朗日方程，前提是 $\tau$ 是仿射参数（固有时正是如此）。这是避免平方根的标准技巧。

**Step 2 — Write the Euler–Lagrange equations.** The Euler–Lagrange equations for coordinates $x^\mu$ are

**第 2 步 — 写出欧拉-拉格朗日方程。** 坐标 $x^\mu$ 的欧拉-拉格朗日方程为

$$ \frac{d}{d\tau}\Big(\frac{\partial L}{\partial \dot{x}^\mu}\Big) - \frac{\partial L}{\partial x^\mu} = 0. $$

Compute each term. Since $L = g_{\alpha\beta} \dot{x}^\alpha \dot{x}^\beta$:

计算每一项。由于 $L = g_{\alpha\beta} \dot{x}^\alpha \dot{x}^\beta$：

$$ \frac{\partial L}{\partial \dot{x}^\mu} = 2 g_{\mu\beta} \dot{x}^\beta \quad \text{(using symmetry of } g_{\alpha\beta}\text{)} $$

$$ \frac{\partial L}{\partial \dot{x}^\mu} = 2 g_{\mu\beta} \dot{x}^\beta \quad \text{（利用 } g_{\alpha\beta} \text{ 的对称性）} $$

$$ \frac{\partial L}{\partial x^\mu} = (\partial_\mu g_{\alpha\beta}) \dot{x}^\alpha \dot{x}^\beta. $$

$$ \frac{\partial L}{\partial x^\mu} = (\partial_\mu g_{\alpha\beta}) \dot{x}^\alpha \dot{x}^\beta. $$

**Step 3 — Compute the total $\tau$-derivative.** Apply the chain rule to $d/d\tau (2 g_{\mu\beta} \dot{x}^\beta)$:

**第 3 步 — 计算全 $\tau$ 导数。** 对 $d/d\tau (2 g_{\mu\beta} \dot{x}^\beta)$ 应用链式法则：

$$ \frac{d}{d\tau}(2 g_{\mu\beta} \dot{x}^\beta) = 2 g_{\mu\beta} \ddot{x}^\beta + 2 (\partial_\alpha g_{\mu\beta}) \dot{x}^\alpha \dot{x}^\beta. $$

The Euler–Lagrange equation becomes:

欧拉-拉格朗日方程变为：

$$ 2 g_{\mu\beta} \ddot{x}^\beta + 2 (\partial_\alpha g_{\mu\beta}) \dot{x}^\alpha \dot{x}^\beta - (\partial_\mu g_{\alpha\beta}) \dot{x}^\alpha \dot{x}^\beta = 0. $$

**Step 4 — Symmetrize the middle term.** The term $(\partial_\alpha g_{\mu\beta}) \dot{x}^\alpha \dot{x}^\beta$ is contracted with $\dot{x}^\alpha \dot{x}^\beta$, which is symmetric in $\alpha,\beta$. Therefore:

**第 4 步 — 对称化中间项。** 项 $(\partial_\alpha g_{\mu\beta}) \dot{x}^\alpha \dot{x}^\beta$ 与关于 $\alpha,\beta$ 对称的 $\dot{x}^\alpha \dot{x}^\beta$ 缩并。因此：

$$ (\partial_\alpha g_{\mu\beta}) \dot{x}^\alpha \dot{x}^\beta = \tfrac12 (\partial_\alpha g_{\mu\beta} + \partial_\beta g_{\mu\alpha}) \dot{x}^\alpha \dot{x}^\beta. $$

Substitute back:

代回：

$$ 2 g_{\mu\beta} \ddot{x}^\beta + (\partial_\alpha g_{\mu\beta} + \partial_\beta g_{\mu\alpha} - \partial_\mu g_{\alpha\beta}) \dot{x}^\alpha \dot{x}^\beta = 0. $$

**Step 5 — Identify the Christoffel symbols.** Multiply through by $\tfrac12 g^{\nu\mu}$ (the inverse metric):

**第 5 步 — 识别克里斯托费尔符号。** 两边乘以 $\tfrac12 g^{\nu\mu}$（逆度规）：

$$ \ddot{x}^\nu + \tfrac12 g^{\nu\mu}(\partial_\alpha g_{\mu\beta} + \partial_\beta g_{\mu\alpha} - \partial_\mu g_{\alpha\beta}) \dot{x}^\alpha \dot{x}^\beta = 0. $$

The coefficient of $\dot{x}^\alpha \dot{x}^\beta$ is exactly the Christoffel symbol $\Gamma^{\nu}{}_{\alpha\beta}$ (from Module 7.2). Therefore:

$\dot{x}^\alpha \dot{x}^\beta$ 的系数正是克里斯托费尔符号 $\Gamma^{\nu}{}_{\alpha\beta}$（来自模块 7.2）。因此：

$$ \boxed{\, \ddot{x}^\mu + \Gamma^{\mu}{}_{\alpha\beta} \dot{x}^\alpha \dot{x}^\beta = 0 \,} $$

i.e., $d^2x^\mu/d\tau^2 + \Gamma^{\mu}{}_{\alpha\beta} (dx^\alpha/d\tau)(dx^\beta/d\tau) = 0$. $\blacksquare$

即 $d^2x^\mu/d\tau^2 + \Gamma^{\mu}{}_{\alpha\beta} (dx^\alpha/d\tau)(dx^\beta/d\tau) = 0$。$\blacksquare$

**Step 6 — Massless particles.** For photons, $ds^2 = 0$, so $\tau$ is not a suitable parameter. Replace $\tau$ by any affine parameter $\lambda$ (related to $\tau$ by a linear transformation where the proportionality constant is absorbed). The geodesic equation takes the same form with $\tau \to \lambda$, and the constraint $g_{\mu\nu} (dx^\mu/d\lambda)(dx^\nu/d\lambda) = 0$ is imposed separately.

**第 6 步 — 无质量粒子。** 对于光子，$ds^2 = 0$，故 $\tau$ 不是合适的参数。将 $\tau$ 换为任意仿射参数 $\lambda$（与 $\tau$ 的关系通过线性变换，比例常数被吸收）。测地线方程形式不变（$\tau \to \lambda$），约束条件 $g_{\mu\nu} (dx^\mu/d\lambda)(dx^\nu/d\lambda) = 0$ 单独施加。

---

## B. Newtonian Limit: Recovering $d^2x/dt^2 = -\nabla\varphi$ · 牛顿极限：恢复 $d^2x/dt^2 = -\nabla\varphi$

**Claim.** In the limit of slow motion ($|dx^i/d\tau| \ll c$) and a weak, static gravitational field ($g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$, $|h_{\mu\nu}| \ll 1$, $h_{\mu\nu,0} = 0$), the geodesic equation reduces to Newton's law $d^2x^i/dt^2 = -\partial_i \varphi$, where $\varphi$ is the Newtonian potential and $g_{00} = -(1 + 2\varphi/c^2)$.

**命题。** 在慢速运动（$|dx^i/d\tau| \ll c$）和弱静态引力场（$g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$，$|h_{\mu\nu}| \ll 1$，$h_{\mu\nu,0} = 0$）的极限下，测地线方程化为牛顿定律 $d^2x^i/dt^2 = -\partial_i \varphi$，其中 $\varphi$ 是牛顿引力势，$g_{00} = -(1 + 2\varphi/c^2)$。

**Step 1 — Slow-motion approximation.** In the slow-motion limit, the spatial velocity components satisfy $|dx^i/d\tau| \ll c = |dx^0/d\tau|$, so $dx^0/d\tau \approx c\, dt/d\tau$ dominates. The geodesic equation becomes (to leading order):

**第 1 步 — 慢速运动近似。** 在慢速运动极限下，空间速度分量满足 $|dx^i/d\tau| \ll c = |dx^0/d\tau|$，故 $dx^0/d\tau \approx c\, dt/d\tau$ 占主导。测地线方程（在主导阶）变为：

$$ d^2x^i/d\tau^2 + \Gamma^{i}{}_{00} (dx^0/d\tau)^2 = 0. $$

The terms involving $\Gamma^{i}{}_{0j} (dx^0/d\tau)(dx^j/d\tau)$ and $\Gamma^{i}{}_{jk} (dx^j/d\tau)(dx^k/d\tau)$ are of higher order in $v/c$ and are dropped.

涉及 $\Gamma^{i}{}_{0j} (dx^0/d\tau)(dx^j/d\tau)$ 和 $\Gamma^{i}{}_{jk} (dx^j/d\tau)(dx^k/d\tau)$ 的项在 $v/c$ 方面是高阶小量，予以舍去。

**Step 2 — Compute $\Gamma^{i}{}_{00}$ in the weak-field limit.** Using the Christoffel formula and a static perturbation (all time derivatives of $h_{\mu\nu}$ vanish):

**第 2 步 — 在弱场极限下计算 $\Gamma^{i}{}_{00}$。** 利用克里斯托费尔公式和静态微扰（$h_{\mu\nu}$ 的所有时间导数为零）：

$$ \Gamma^{i}{}_{00} = \tfrac12 g^{i\sigma}(\partial_0 g_{\sigma 0} + \partial_0 g_{\sigma 0} - \partial_\sigma g_{00}) = \tfrac12 g^{i\sigma}(2 \partial_0 g_{\sigma 0} - \partial_\sigma g_{00}). $$

For a static field $\partial_0 g_{\sigma 0} = 0$. The inverse metric to first order is $g^{ij} \approx \delta^{ij}$ (spatial flat), so:

对于静态场 $\partial_0 g_{\sigma 0} = 0$。逆度规在一阶近似下 $g^{ij} \approx \delta^{ij}$（空间平坦），故：

$$ \Gamma^{i}{}_{00} = -\tfrac12 g^{ij} \partial_j g_{00} \approx -\tfrac12 \delta^{ij} \partial_j h_{00} = -\tfrac12 \partial^i h_{00}. $$

**Step 3 — Identify $h_{00}$ with the Newtonian potential.** For the metric to reproduce Newton's law, we need $\Gamma^{i}{}_{00} = \partial^i \varphi / c^2$. Comparing:

**第 3 步 — 将 $h_{00}$ 与牛顿引力势对应。** 为使度规还原牛顿定律，需要 $\Gamma^{i}{}_{00} = \partial^i \varphi / c^2$。比较得：

$$ -\tfrac12 \partial^i h_{00} = \partial^i \varphi / c^2 \quad\implies\quad h_{00} = -2\varphi/c^2 \quad\implies\quad g_{00} = -1 - 2\varphi/c^2 = -(1 + 2\varphi/c^2). $$

(With $\varphi < 0$ near a mass, $g_{00} = -1 + |2\varphi|/c^2$ is slightly less negative than $-1$, i.e., $|g_{00}| < 1$.)

（在质量附近 $\varphi < 0$，$g_{00} = -1 + |2\varphi|/c^2$ 比 $-1$ 稍小，即 $|g_{00}| < 1$。）

**Step 4 — Convert to coordinate time.** In the slow-motion limit, proper time and coordinate time are related by $d\tau \approx dt$ (to lowest order). For the spatial geodesic equation:

**第 4 步 — 换算为坐标时。** 在慢速运动极限下，固有时与坐标时的关系为 $d\tau \approx dt$（最低阶）。对于空间方向的测地线方程：

$$ d^2x^i/dt^2 \approx d^2x^i/d\tau^2 = -\Gamma^{i}{}_{00} (dx^0/d\tau)^2 = -\Gamma^{i}{}_{00} c^2 = -(-\tfrac12 \partial^i h_{00}) c^2 = \tfrac12 c^2 \partial^i h_{00}. $$

Substituting $h_{00} = -2\varphi/c^2$:

代入 $h_{00} = -2\varphi/c^2$：

$$ d^2x^i/dt^2 = \tfrac12 c^2 \cdot \partial^i(-2\varphi/c^2) = -\partial^i \varphi = -\partial\varphi/\partial x^i. $$

In vector form: $\boxed{\, d^2x/dt^2 = -\nabla\varphi \,}$. $\blacksquare$

矢量形式：$\boxed{\, d^2x/dt^2 = -\nabla\varphi \,}$。$\blacksquare$

**Step 5 — Summary of approximations used.** Three conditions were needed: (a) slow motion $|v| \ll c$, so spatial velocity terms in the geodesic equation are negligible; (b) weak field $|h_{\mu\nu}| \ll 1$, so the metric is nearly flat and Christoffel symbols are linear in $h$; (c) static field $\partial_t g_{\mu\nu} = 0$, so time-derivative Christoffel components vanish. All three conditions hold for the Solar System (the strongest Solar-system potential is $\varphi_\odot/c^2 \sim 10^{-6}$ at the Sun's surface).

**第 5 步 — 所用近似总结。** 需要三个条件：(a) 慢速运动 $|v| \ll c$，使测地线方程中的空间速度项可忽略；(b) 弱场 $|h_{\mu\nu}| \ll 1$，使度规近似平坦且克里斯托费尔符号对 $h$ 是线性的；(c) 静态场 $\partial_t g_{\mu\nu} = 0$，使含时间导数的克里斯托费尔分量消失。这三个条件在太阳系中都成立（太阳表面最强的太阳系势 $\varphi_\odot/c^2 \sim 10^{-6}$）。

---

## C. Gravitational Time Dilation from the Geodesic and the Redshift · 从测地线推导引力时间膨胀与红移

**Claim.** For a static observer in a metric with $g_{00} = -(1 + 2\varphi/c^2)$, the ratio of proper time to coordinate time is $d\tau/dt = \sqrt{-g_{00}} \approx 1 + \varphi/c^2$. Two static observers at potentials $\varphi_1$ and $\varphi_2$ observe a frequency ratio $\nu_2/\nu_1 = \sqrt{-g_{00}(x_1)} / \sqrt{-g_{00}(x_2)} \approx 1 + (\varphi_1 - \varphi_2)/c^2$.

**命题。** 对于度规 $g_{00} = -(1 + 2\varphi/c^2)$ 中的静止观察者，固有时与坐标时之比为 $d\tau/dt = \sqrt{-g_{00}} \approx 1 + \varphi/c^2$。势能分别为 $\varphi_1$ 和 $\varphi_2$ 的两个静止观察者观测到的频率比为 $\nu_2/\nu_1 = \sqrt{-g_{00}(x_1)} / \sqrt{-g_{00}(x_2)} \approx 1 + (\varphi_1 - \varphi_2)/c^2$。

**Step 1 — Static observer.** For a static observer, $dx^i/d\tau = 0$. The line element gives

**第 1 步 — 静止观察者。** 对于静止观察者，$dx^i/d\tau = 0$。线元给出

$$ c^2 d\tau^2 = -ds^2 = -g_{00} (dx^0)^2 = -g_{00} c^2 dt^2 \implies d\tau = \sqrt{-g_{00}}\, dt. $$

In the weak-field limit: $d\tau \approx (1 + \varphi/c^2) dt$. Clocks at lower potential (more negative $\varphi$) tick slower. This was already derived in Module 7.1 Derivations Section C; here it follows as a special case of the geodesic formalism.

在弱场极限下：$d\tau \approx (1 + \varphi/c^2) dt$。势能更低（更负的 $\varphi$）处的时钟走得更慢。这已在模块 7.1 推导 C 节中推导；此处它作为测地线形式的特例得出。

**Step 2 — Coordinate-time interval between crests is conserved.** In a static metric ($\partial_t g_{\mu\nu} = 0$), the time-translation Killing vector $\partial/\partial t$ implies that the coordinate frequency of a photon is conserved along its null geodesic. Equivalently, the coordinate time interval $\Delta t$ between successive wavefronts is the same at emission and reception.

**第 2 步 — 波峰间的坐标时间间隔守恒。** 在静态度规（$\partial_t g_{\mu\nu} = 0$）中，时间平移基灵矢量 $\partial/\partial t$ 意味着光子沿其零测地线的坐标频率守恒。等价地，连续波前之间的坐标时间间隔 $\Delta t$ 在发射和接收处相同。

**Step 3 — Proper-time intervals and frequency ratio.** Since the proper-time interval between crests at position $x_A$ is $d\tau_A = \sqrt{-g_{00}(x_A)}\, \Delta t$ and frequency is $\nu_A = 1/d\tau_A$:

**第 3 步 — 固有时间隔与频率比。** 由于位置 $x_A$ 处波峰间的固有时间隔为 $d\tau_A = \sqrt{-g_{00}(x_A)}\, \Delta t$，频率为 $\nu_A = 1/d\tau_A$：

$$ \nu_2/\nu_1 = d\tau_1/d\tau_2 = \sqrt{-g_{00}(x_1)} / \sqrt{-g_{00}(x_2)}. $$

In the weak-field limit:

在弱场极限下：

$$ \nu_2/\nu_1 \approx (1 + \varphi_1/c^2)/(1 + \varphi_2/c^2) \approx 1 + (\varphi_1 - \varphi_2)/c^2. $$

The fractional redshift for upward emission ($\varphi_1 < \varphi_2$, $\Delta\varphi = \varphi_2 - \varphi_1 > 0$) is

向上发射（$\varphi_1 < \varphi_2$，$\Delta\varphi = \varphi_2 - \varphi_1 > 0$）的分数红移为

$$ z = (\nu_1 - \nu_2)/\nu_2 \approx \Delta\varphi/c^2, \qquad \blacksquare $$

in agreement with the equivalence-principle result of Module 7.1.

与模块 7.1 等效原理结果一致。$\blacksquare$

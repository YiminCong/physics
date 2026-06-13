# Module 7.3 — Geodesics & the Motion of Particles
**模块 7.3 — 测地线与粒子运动**

> **Phase 7 — [General Relativity & Cosmology](./README.md)** · Format: Definition → Demonstration → Application
> **第 7 阶段 — 广义相对论与宇宙学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-7.3-geodesics-and-motion-of-particles-derivations.md)

---

## 1. The Geodesic Equation · 测地线方程

**Definition.** In GR, freely falling particles (no non-gravitational forces) move along *geodesics* of the spacetime metric: curves that extremize the proper time (equivalently, parallel-transport their own tangent vector). Applying the variational principle (Module 1.3) to the action $S = -mc \int d\tau = -mc \int\sqrt{-g_{\mu\nu}\, dx^\mu dx^\nu}$ yields the *geodesic equation*:

**定义。** 在广义相对论中，自由下落的粒子（无非引力作用）沿时空度规的*测地线*运动：这些曲线使固有时取极值（等价地，平行移动自身的切矢量）。对作用量 $S = -mc \int d\tau = -mc \int\sqrt{-g_{\mu\nu}\, dx^\mu dx^\nu}$ 应用变分原理（模块 1.3），得到*测地线方程*：

$$ \frac{d^2 x^\mu}{d\tau^2} + \Gamma^{\mu}{}_{\nu\rho} \frac{dx^\nu}{d\tau}\frac{dx^\rho}{d\tau} = 0 $$

Here $\tau$ is proper time and $\Gamma^{\mu}{}_{\nu\rho}$ are the Christoffel symbols of the metric (Module 7.2). For massless particles (photons), $\tau$ is replaced by an affine parameter $\lambda$ and $ds^2 = 0$. The geodesic equation is the GR replacement for Newton's second law $F = ma$ under gravity.

其中 $\tau$ 为固有时，$\Gamma^{\mu}{}_{\nu\rho}$ 为度规的克里斯托费尔符号（模块 7.2）。对无质量粒子（光子），$\tau$ 换为仿射参数 $\lambda$，且 $ds^2 = 0$。测地线方程是广义相对论中替代引力下牛顿第二定律 $F = ma$ 的方程。

**Demonstration.** *Newtonian limit*: take $g_{\mu\nu} \approx \eta_{\mu\nu} + h_{\mu\nu}$ with $|h_{\mu\nu}| \ll 1$, slow motion $dx^i/d\tau \ll c$, and a static field $h_{00} = -2\varphi/c^2$ ($\varphi$ Newtonian potential). The time-time Christoffel symbol gives $\Gamma^{i}{}_{00} \approx -\tfrac12\partial^i h_{00} = \partial^i \varphi/c^2$. The geodesic spatial components reduce to

**演示。** *牛顿极限*：取 $g_{\mu\nu} \approx \eta_{\mu\nu} + h_{\mu\nu}$，其中 $|h_{\mu\nu}| \ll 1$，慢速运动 $dx^i/d\tau \ll c$，以及静态场 $h_{00} = -2\varphi/c^2$（$\varphi$ 为牛顿引力势）。时间-时间分量的克里斯托费尔符号给出 $\Gamma^{i}{}_{00} \approx -\tfrac12\partial^i h_{00} = \partial^i \varphi/c^2$。测地线方程的空间分量化为

$$ \frac{d^2 x^i}{dt^2} = -\partial^i \varphi $$

which is precisely Newton's law of gravity (Module 1.1). The geometry reproduces Newtonian gravity in the appropriate limit.

这正是牛顿引力定律（模块 1.1）。该几何在适当极限下还原了牛顿引力。

*Gravitational time dilation and redshift*: for a static metric with $g_{00} = -(1 + 2\varphi/c^2)$, proper time and coordinate time are related by $d\tau = \sqrt{-g_{00}}\, dt \approx (1 + \varphi/c^2)dt$. A clock at lower potential $\varphi_1 < \varphi_2$ runs slow: $d\tau_1/d\tau_2 \approx 1 + (\varphi_1 - \varphi_2)/c^2 < 1$. Light emitted at frequency $\nu_1$ near a massive body is received at frequency $\nu_2 = \nu_1(1 + \Delta\varphi/c^2)$ — *gravitational redshift*, $z \approx \Delta\varphi/c^2$.

*引力时间膨胀与红移*：对于静态度规 $g_{00} = -(1 + 2\varphi/c^2)$，固有时与坐标时的关系为 $d\tau = \sqrt{-g_{00}}\, dt \approx (1 + \varphi/c^2)dt$。处于较低势 $\varphi_1 < \varphi_2$ 的时钟走慢：$d\tau_1/d\tau_2 \approx 1 + (\varphi_1 - \varphi_2)/c^2 < 1$。在大质量天体附近以频率 $\nu_1$ 发出的光，被接收时频率为 $\nu_2 = \nu_1(1 + \Delta\varphi/c^2)$——*引力红移*，$z \approx \Delta\varphi/c^2$。

**Application.**

**应用。**

- *GPS corrections*: GPS satellites orbit at altitude $\approx 20\,200$ km where $\varphi$ is less negative. Gravitational time dilation causes satellite clocks to run fast by $\approx +45.9\ \mu\text{s/day}$; SR velocity time dilation (Module 1.14) causes them to run slow by $\approx -7.2\ \mu\text{s/day}$; net correction $\approx +38.7\ \mu\text{s/day}$. Without this, GPS positions would drift by $\approx 10$ km/day.
- *Perihelion precession of Mercury*: the Schwarzschild geodesic for a planet gives an orbit that is not a closed ellipse (Module 1.5) but precesses by $\Delta\varphi = 6\pi GM/(a(1-e^2)c^2)$ per orbit. For Mercury this is $\approx 43$ arcsec/century — the famous anomaly unexplained by Newtonian gravity, confirmed precisely by GR.

- *GPS 修正*：GPS 卫星在约 $20\,200$ km 高度轨道运行，该处 $\varphi$ 较地面更不负。引力时间膨胀使卫星时钟每天快约 $+45.9\ \mu\text{s}$；狭义相对论速度时间膨胀（模块 1.14）使其每天慢约 $-7.2\ \mu\text{s}$；净修正约 $+38.7\ \mu\text{s/}$天。若不作此修正，GPS 定位每天将漂移约 $10$ km。
- *水星近日点进动*：史瓦西时空中行星的测地线给出的轨道不是封闭椭圆（模块 1.5），而是每圈进动 $\Delta\varphi = 6\pi GM/(a(1-e^2)c^2)$。对水星而言约为 $43$ 弧秒/世纪——这是牛顿引力无法解释的著名异常，被广义相对论精确证实。

## Key results · 核心结果

- Geodesic equation $\dfrac{d^2x^\mu}{d\tau^2}+\Gamma^\mu{}_{\nu\rho}\dfrac{dx^\nu}{d\tau}\dfrac{dx^\rho}{d\tau}=0$ · 测地线方程
- Newtonian limit $\ddot x^i=-\partial^i\varphi$ · 牛顿极限
- $g_{00}\approx-(1+2\varphi/c^2)$ encodes the gravitational potential · 引力势编码于 $g_{00}$
- Gravitational redshift $z\approx\Delta\varphi/c^2$ · 引力红移

---

**Self-test (blank page)**

1. Derive the geodesic equation from the variational principle $\delta\int d\tau = 0$. At what step do the Christoffel symbols appear?
2. Show that in the Newtonian limit, the geodesic equation reduces to $d^2 x^i/dt^2 = -\nabla\varphi$. What approximations are required?
3. A photon climbs from the Sun's surface ($\varphi_\text{surface} \approx -1.91 \times 10^{11}$ J/kg) to infinity. Estimate its gravitational redshift $z$.

**自测（空白页）**

1. 从变分原理 $\delta\int d\tau = 0$ 推导测地线方程。克里斯托费尔符号在哪一步出现？
2. 证明在牛顿极限下，测地线方程化为 $d^2 x^i/dt^2 = -\nabla\varphi$。需要哪些近似？
3. 一个光子从太阳表面（$\varphi_\text{surface} \approx -1.91 \times 10^{11}$ J/kg）向无穷远爬升。估算其引力红移 $z$。

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** Extremize $\delta\int d\tau=0$; the Euler–Lagrange equations of the proper-time functional give the geodesic equation, and the Christoffel symbols appear when differentiating $g_{\mu\nu}(x)$ (the $\partial g$ terms assemble into $\Gamma$). · 变分给测地线;微分度规处出现 $\Gamma$。
**2.** Weak field $g_{00}\approx-(1+2\varphi/c^2)$, slow motion, static: the only surviving term is $\Gamma^i{}_{00}(dx^0/d\tau)^2\approx\partial^i\varphi$, giving $\ddot x^i=-\partial^i\varphi$. · 弱场慢速静态极限。
**3.** $z\approx\Delta\varphi/c^2=|\varphi_\text{surface}|/c^2=1.91\times10^{11}/(9\times10^{16})\approx2.1\times10^{-6}$. · 红移约 $2.1\times10^{-6}$。

</details>

---

← Previous: [Module 7.2 — Tensors, the Metric & Curvature](./module-7.2-tensors-metric-and-curvature.md) · [Phase 7 index](./README.md) · Next: [Module 7.4 — Einstein's Field Equations](./module-7.4-einsteins-field-equations.md) →

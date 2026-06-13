# Module 7.1 — The Equivalence Principle & Curved Spacetime ⭐
**模块 7.1 — 等效原理与弯曲时空 ⭐**

> **Phase 7 — [General Relativity & Cosmology](./README.md)** · Format: Definition → Demonstration → Application
> **第 7 阶段 — 广义相对论与宇宙学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-7.1-equivalence-principle-and-curved-spacetime-derivations.md)

---

## 1. The Equivalence Principle · 等效原理

**Definition.** The *weak equivalence principle* states that gravitational mass (the charge that sources and responds to gravity) and inertial mass (resistance to acceleration) are identical for all bodies. Einstein elevated this to the *strong equivalence principle*: no local experiment — mechanical or otherwise — can distinguish a freely falling frame from an inertial frame in empty space. Equivalently, a uniformly accelerating frame is locally indistinguishable from a uniform gravitational field. This is the founding observation of General Relativity.

**定义。** *弱等效原理*指出，引力质量（引力的源与响应者）与惯性质量（对加速度的阻抗）对一切物体完全相同。爱因斯坦将其提升为*强等效原理*：任何局域实验——无论力学还是其他——都无法区分自由下落参考系与空旷空间中的惯性参考系。等价地，匀加速参考系与匀强引力场在局域上无法区分。这是广义相对论的奠基性观察。

**Demonstration.** Consider an observer in a sealed elevator. If the elevator accelerates upward at $g$, a dropped ball falls to the floor at rate $g$ — identical to the behaviour inside a gravitational field of strength $g$. Conversely, a freely falling elevator is locally inertial: a released ball floats beside the observer, just as in deep space. The equivalence is exact to all orders locally; tidal effects (geodesic deviation) only become measurable at finite separations, encoding curvature.

**演示。** 设想一个观察者在密封电梯中。若电梯以加速度 $g$ 向上加速，投出的球以 $g$ 的加速度落向地板——与引力场强度为 $g$ 的行为完全相同。反之，自由下落的电梯是局域惯性的：释放的球漂浮在观察者身旁，如同在深空中一样。该等效性在局域上对所有阶都精确成立；潮汐效应（测地偏差）只在有限间隔处才可测量，它编码了曲率信息。

**Application.** The equivalence principle has two immediate physical consequences, derivable before writing a single field equation.

**应用。** 等效原理有两个直接的物理推论，在写下任何场方程之前即可推导。

- *Gravitational time dilation*: a clock deeper in a gravitational potential $\varphi$ runs slow by the factor $(1 + \varphi/c^2)$ relative to one at higher potential (derivable by treating a gravitational field as an equivalent acceleration). Clocks at Earth's surface lose $\approx 45\ \mu\text{s/day}$ relative to GPS satellites due to this effect (partially offset by the velocity/SR effect; see Module 7.3).
- *Light bending*: a horizontal light beam inside an accelerating elevator is deflected downward by the acceleration. By equivalence, gravity must also bend light — and by a factor of two more than Newtonian optics predicts, because spacetime curvature (not just time dilation) contributes equally. Confirmed by Eddington's 1919 solar-eclipse measurement.

- *引力时间膨胀*：处于引力势 $\varphi$ 较深处的时钟相对于较高势处的时钟走慢，慢慢因子为 $(1 + \varphi/c^2)$（可通过将引力场等效为加速度来推导）。由于此效应，地球表面的时钟相对于 GPS 卫星每天慢约 $45\ \mu\text{s}$（部分被速度/狭义相对论效应抵消；见模块 7.3）。
- *光线弯曲*：在加速电梯中，水平光束因加速度向下偏转。根据等效原理，引力同样必须使光线弯曲——且偏转量是牛顿光学预测的两倍，因为时空曲率（而非仅时间膨胀）贡献了同等效应。这一结论由爱丁顿 1919 年的日食观测所证实。

---

## 2. From Flat to Curved Spacetime · 从平坦时空到弯曲时空

**Definition.** Special Relativity (Module 1.13) is framed in *Minkowski spacetime*: a flat, globally inertial manifold with line element $ds^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2 = \eta_{\mu\nu}\, dx^\mu dx^\nu$, where $\eta_{\mu\nu} = \mathrm{diag}(-1, +1, +1, +1)$. Gravity cannot be accommodated in flat spacetime while respecting the equivalence principle. Einstein's great insight: gravity is not a force propagating through a fixed background but is instead the *curvature of spacetime itself*. The spacetime manifold has a dynamical metric $g_{\mu\nu}(x)$ that replaces $\eta_{\mu\nu}$; freely falling particles follow the straightest paths (*geodesics*) in this curved geometry.

**定义。** 狭义相对论（模块 1.13）建立在*闵可夫斯基时空*中：一个平坦的、整体惯性的流形，其线元为 $ds^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2 = \eta_{\mu\nu}\, dx^\mu dx^\nu$，其中 $\eta_{\mu\nu} = \mathrm{diag}(-1, +1, +1, +1)$。在平坦时空中容纳引力同时满足等效原理是不可能的。爱因斯坦的伟大洞见：引力不是在固定背景中传播的力，而是*时空自身的曲率*。时空流形拥有动态度规张量 $g_{\mu\nu}(x)$ 取代 $\eta_{\mu\nu}$；自由下落的粒子在弯曲几何中沿最直路径（*测地线*）运动。

**Demonstration.** On the surface of a sphere, initially parallel lines of longitude converge at the poles: parallel transport around a closed loop rotates a vector by an angle equal to the solid angle enclosed. This is an intrinsic curvature effect requiring no embedding in a higher dimension. In 4-D spacetime, the Riemann tensor $R^{\mu}{}_{\nu\rho\sigma}$ (Module 7.2) captures this rotation; where $R^{\mu}{}_{\nu\rho\sigma} = 0$ everywhere, spacetime is flat and SR is recovered globally.

**演示。** 在球面上，最初平行的经线在极点处汇聚：沿封闭回路的平行移动使矢量旋转一个等于所围立体角的角度。这是一种不依赖嵌入高维空间的内禀曲率效应。在四维时空中，黎曼曲率张量 $R^{\mu}{}_{\nu\rho\sigma}$（模块 7.2）捕捉这种旋转；当处处 $R^{\mu}{}_{\nu\rho\sigma} = 0$ 时，时空是平坦的，狭义相对论在全局得以恢复。

**Application.** The conceptual leap — gravity as geometry — unifies the universality of free fall (all bodies follow the same geodesics regardless of composition, because the trajectory depends only on the metric) with the field-theoretic description of gravity. It sets the stage for the full mathematical machinery (Module 7.2), geodesic motion (Module 7.3), and Einstein's field equations (Module 7.4). It also signals a break from the Newtonian picture of gravity as an instantaneous force (Module 1.5): information about curvature propagates at $c$.

**应用。** 这一概念飞跃——将引力视为几何——将自由落体的普遍性（所有物体无论成分如何都沿相同测地线运动，因为轨迹仅取决于度规）与引力的场论描述统一起来。它为完整的数学机制（模块 7.2）、测地线运动（模块 7.3）和爱因斯坦场方程（模块 7.4）奠定基础。它也标志着与牛顿引力（将引力视为瞬时力，见模块 1.5）的决裂：曲率信息以 $c$ 的速度传播。

## Key results · 核心结果

- Equivalence principle: free fall is locally indistinguishable from inertial motion · 等效原理
- $ds^2 = \eta_{\mu\nu}\,dx^\mu dx^\nu$, $\eta_{\mu\nu} = \text{diag}(-1,+1,+1,+1)$ — flat (mostly-plus, GR convention) · 平坦度规(GR 号差)
- Gravity is curvature of spacetime, not a force · 引力即时空弯曲
- Free particles follow geodesics · 自由粒子沿测地线运动

---

**Self-test (blank page)**

1. State the strong equivalence principle. How does it imply that freely falling frames are locally inertial, and what is the role of tidal forces in limiting this?
2. Derive the gravitational redshift formula $z \approx \Delta\varphi/c^2$ using only the equivalence principle and the Doppler effect — no field equations needed.
3. Why does GR predict twice the Newtonian deflection of light by the Sun? Which physical effect contributes the "extra" factor?

**自测（空白页）**

1. 陈述强等效原理。它如何表明自由下落参考系在局域上是惯性的？潮汐力在限制这一点上扮演什么角色？
2. 仅利用等效原理和多普勒效应推导引力红移公式 $z \approx \Delta\varphi/c^2$——无需场方程。
3. 为何广义相对论预言太阳对光线的偏折是牛顿值的两倍？哪个物理效应贡献了"额外"的那一半？

---

← [Phase 7 index](./README.md) · Next: [Module 7.2 — Tensors, the Metric & Curvature](./module-7.2-tensors-metric-and-curvature.md) →

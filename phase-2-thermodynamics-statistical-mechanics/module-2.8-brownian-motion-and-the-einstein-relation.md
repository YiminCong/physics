# Module 2.8 — Brownian Motion & the Einstein Relation
**模块 2.8 — 布朗运动与爱因斯坦关系**

> **Phase 2 — [Thermodynamics & Statistical Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 2 阶段 — 热力学与统计力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-2.8-derivations.md)

---

## 1. Brownian Motion · 布朗运动

**Definition.** **Brownian motion** is the incessant random jittering of a microscopic particle (a pollen grain, a colloid) suspended in a fluid, caused by unbalanced collisions with the fluid's molecules. **Einstein (1905)** modelled it as a random walk and showed the **mean-square displacement grows linearly in time**: $\langle x^2\rangle = 2Dt$ (in one dimension), where $D$ is the **diffusion coefficient**. The particle drifts nowhere on average, but spreads diffusively.

**定义。** **布朗运动**是悬浮在流体中的微观粒子（花粉粒、胶体粒子）由于与流体分子的非平衡碰撞而产生的持续随机抖动。**爱因斯坦（1905）**将其建模为随机游走，并证明**均方位移随时间线性增长**：$\langle x^2\rangle = 2Dt$（一维），其中 $D$ 为**扩散系数**。粒子平均而言不发生漂移，但以扩散方式扩展。

**Demonstration.** Einstein connected this microscopic randomness to a measurable macroscopic coefficient via the **Einstein relation** $D = \mu k_B T$, where $\mu$ is the particle's mobility (drift velocity per unit force). For a sphere of radius $r$ in a fluid of viscosity $\eta$, Stokes' law gives $\mu = 1/(6\pi\eta r)$, so $D = k_B T / (6\pi\eta r)$ (the Stokes–Einstein relation). Measuring $D$ and $\eta$ therefore yields **Avogadro's number** — exactly what **Perrin's experiments (1908)** did, giving the decisive proof that atoms are real.

**演示。** 爱因斯坦通过**爱因斯坦关系** $D = \mu k_B T$ 将这种微观随机性与可测量的宏观系数联系起来，其中 $\mu$ 为粒子的迁移率（单位力下的漂移速度）。对于粘度为 $\eta$ 的流体中半径为 $r$ 的球体，斯托克斯定律给出 $\mu = 1/(6\pi\eta r)$，故 $D = k_B T / (6\pi\eta r)$（斯托克斯–爱因斯坦关系）。因此测量 $D$ 和 $\eta$ 可得到**阿伏加德罗常数**——这正是**佩兰实验（1908）**所做的，为原子的真实存在提供了决定性证明。

## 2. Fluctuation–Dissipation · 涨落–耗散定理

**Definition.** The Einstein relation $D = \mu k_B T$ is the first instance of the **fluctuation–dissipation theorem**: the random fluctuations of a system (diffusion $D$) are tied to its dissipative response (mobility/friction $\mu$), both rooted in the same molecular collisions.

**定义。** 爱因斯坦关系 $D = \mu k_B T$ 是**涨落–耗散定理**的第一个实例：系统的随机涨落（扩散 $D$）与其耗散响应（迁移率/摩擦 $\mu$）相互联系，两者均源于相同的分子碰撞。

**Application.** Beyond confirming atomism, this launched the theory of **stochastic processes** — the Langevin equation, random walks, and noise. The same logic gives **Johnson–Nyquist thermal noise** in electrical circuits and underpins the transport coefficients of Module 2.7. It remains the workhorse for modelling everything from colloids and polymers to financial time series.

**应用。** 除证实原子论之外，这还开创了**随机过程**理论——郎之万方程、随机游走和噪声。同样的逻辑给出了电路中的**约翰逊–奈奎斯特热噪声**，并支撑着模块 2.7 的输运系数。它至今仍是建模一切事物的主要工具，从胶体和聚合物到金融时间序列皆然。

---

**Self-test (blank page)**

1. Write Einstein's result $\langle x^2\rangle = 2Dt$ and contrast diffusive spreading with ballistic motion.
2. State the Einstein relation $D = \mu k_B T$ and the Stokes–Einstein form; explain how it yields Avogadro's number.
3. What does the fluctuation–dissipation theorem connect, and why are the two sides linked?

**自测（空白页）**

1. 写出爱因斯坦结果 $\langle x^2\rangle = 2Dt$，并将扩散式扩展与弹道运动进行对比。
2. 陈述爱因斯坦关系 $D = \mu k_B T$ 和斯托克斯–爱因斯坦形式；解释它如何给出阿伏加德罗常数。
3. 涨落–耗散定理联系了什么，为什么两侧是相互关联的？

---

← Previous: [Module 2.7 — Kinetic Theory & Transport](./module-2.7-kinetic-theory-and-transport.md) · [Phase 2 index](./README.md)

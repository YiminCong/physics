---
title: "Module 7.7 — Tests of GR & Gravitational-Wave Astronomy"
parent: "Phase 7 — General Relativity & Cosmology"
nav_order: 7
---

# Module 7.7 — Tests of GR & Gravitational-Wave Astronomy
**模块 7.7 — 广义相对论的检验与引力波天文学**

> **Phase 7 — [General Relativity & Cosmology](./README.md)** · Format: Definition → Demonstration → Application
> **第 7 阶段 — 广义相对论与宇宙学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-7.7-tests-of-gr-and-gravitational-wave-astronomy-derivations.md)

---

## 1. The Classical Tests and Frame-Dragging · 经典检验与参考系拖曳

**Definition.** Einstein's general relativity makes four immediately testable predictions that differ from Newtonian gravity — the *classical tests* — plus a fifth effect, *frame-dragging*, that requires extreme precision.

**定义。** 爱因斯坦的广义相对论提出了四个与牛顿引力不同的即时可检验预言——*经典检验*——以及第五个需要极高精度的效应：*参考系拖曳*。

**Demonstration — (i) Perihelion Precession of Mercury.** The vacuum Schwarzschild geometry gives an orbit equation with a small correction beyond the Newtonian ellipse. The effective potential has an extra term $-GM\ell^2/c^2 r^3$ (where $\ell = r^2 d\varphi/d\tau$ is the specific angular momentum) that causes the ellipse to precess. The precession per orbit (see Derivations A) is:

**演示——（一）水星近日点进动。** 史瓦西真空几何给出的轨道方程在牛顿椭圆之外有一个小修正项。有效势中的额外项 $-GM\ell^2/c^2 r^3$（$\ell = r^2 d\varphi/d\tau$ 为比角动量）使椭圆进动。每圈进动量（见推导 A）为：

$$ \Delta\varphi = \frac{6\pi GM}{c^2 a (1 - e^2)} $$

For Mercury: $M = M_\odot = 1.989 \times 10^{30}$ kg, $a = 5.79 \times 10^{10}$ m, $e = 0.206$. This gives $\Delta\varphi \approx 43$ arcseconds per century — precisely the anomalous precession left over after all Newtonian perturbations (from other planets) are removed. This was the first quantitative confirmation of GR.

对水星：$M = M_\odot = 1.989 \times 10^{30}$ kg，$a = 5.79 \times 10^{10}$ m，$e = 0.206$，给出 $\Delta\varphi \approx 43$ 弧秒每世纪——正是扣除所有牛顿摄动（来自其他行星）后剩余的反常进动值。这是广义相对论的首个定量确认。

**Demonstration — (ii) Deflection of Light by the Sun.** A photon passing the Sun at impact parameter $b$ follows a geodesic of the Schwarzschild metric. The total deflection angle (see Derivations B) is:

**演示——（二）光线被太阳偏折。** 以碰撞参数 $b$ 经过太阳的光子沿史瓦西度规的测地线运动。总偏折角（见推导 B）为：

$$ \alpha = \frac{4GM_\odot}{c^2 b} $$

For a ray grazing the solar limb ($b = R_\odot = 6.96 \times 10^8$ m): $\alpha = 1.75''$ — exactly twice the Newtonian value. This was confirmed by Eddington's 1919 eclipse expedition and has since been verified to better than 0.1% precision by VLBI observations of radio sources passing near the Sun.

对掠日光线（$b = R_\odot = 6.96 \times 10^8$ m）：$\alpha = 1.75''$——恰好是牛顿值的两倍。1919 年爱丁顿日食探险队对此加以确认，此后甚长基线干涉测量（VLBI）对太阳附近射电源的观测以优于 0.1% 的精度进行了验证。

**Demonstration — (iii) Gravitational Redshift.** A photon climbing out of a gravitational potential well loses energy. For a clock at radius $r$ in Schwarzschild geometry, coordinate time ticks at a rate $d\tau/dt = \sqrt{1 - r_s/r}$ relative to a distant observer. The redshift between two radii $r_e$ (emitter) and $r_r$ (receiver $> r_e$) is:

**演示——（三）引力红移。** 从引力势阱中向外传播的光子损失能量。对于史瓦西几何中位于 $r$ 处的时钟，相对于遥远观测者，坐标时以 $d\tau/dt = \sqrt{1 - r_s/r}$ 的速率流逝。在发射半径 $r_e$ 和接收半径 $r_r > r_e$ 之间的红移为：

$$ z = \frac{\lambda_r - \lambda_e}{\lambda_e} = \sqrt{\frac{1 - r_s/r_e}{1 - r_s/r_r}} - 1 \approx \frac{GM(1/r_e - 1/r_r)}{c^2} $$

First tested by Pound and Rebka (1959) over a 22 m height difference using the Mössbauer effect; confirmed to better than 1%. GPS satellites must apply a $\sim 38\ \mu\text{s/day}$ GR correction or accumulated errors would reach $\sim 10$ km/day.

由庞德和雷布卡（1959 年）利用穆斯堡尔效应在 22 m 高度差上首次检验，精度优于 1%。GPS 卫星必须应用约 $38\ \mu\text{s/}$天的广义相对论修正，否则累积误差将达约 $10$ km/天。

**Demonstration — (iv) Shapiro Time Delay.** A radar pulse sent past the Sun to a planet (or spacecraft) takes longer to return than Euclidean geometry predicts. The extra delay (Shapiro 1964) is:

**演示——（四）夏皮罗时间延迟。** 掠过太阳发射至行星（或航天器）的雷达脉冲返回所需的时间比欧几里得几何预测的更长。额外延迟（夏皮罗，1964 年）为：

$$ \Delta t = \frac{4GM_\odot}{c^3} \ln\frac{4 r_e r_r}{b^2} $$

where $r_e, r_r$ are the distances of emitter and reflector from the Sun and $b$ is the closest approach. The Cassini mission (2003) measured this to 20 parts per million, the most precise test of the post-Newtonian parameter $\gamma$.

其中 $r_e$、$r_r$ 分别为发射端和反射端到太阳的距离，$b$ 为最近距离。卡西尼探测器（2003 年）以 20 ppm 的精度测量了此效应，是对后牛顿参数 $\gamma$ 最精确的检验。

**Demonstration — (v) Frame-Dragging (Lense–Thirring Effect).** A rotating mass drags inertial frames: the spacetime is described by the *Kerr metric* (Module 7.5), which carries an off-diagonal term $g_{t\varphi} \propto -2GJ/(c^2 r)$ (far-field, where $J$ is angular momentum). A gyroscope in polar orbit precesses at the rate:

**演示——（五）参考系拖曳（楞次–蒂林效应）。** 旋转质量拖曳惯性系：时空由*克尔度规*（模块 7.5）描述，其携带非对角项 $g_{t\varphi} \propto -2GJ/(c^2 r)$（远场，$J$ 为角动量）。极轨道上的陀螺仪以如下速率进动：

$$ \Omega_\text{LT} = \frac{GJ}{c^2 r^3} \quad \text{(in appropriate units, with factors of 2 depending on conventions)} $$

*Gravity Probe B* (2011) confirmed the geodetic precession (6606.1 mas/yr, due to curved spacetime, independent of rotation) and the Lense–Thirring precession ($-37.2$ mas/yr, due to Earth's rotation) to 0.3% and 19% respectively, using cryogenic gyroscopes in polar orbit at 642 km altitude.

*引力探测器 B*（2011 年）利用 642 km 高度极轨道上的低温陀螺仪，以 0.3% 和 19% 的精度分别确认了测地线进动（6606.1 mas/yr，源于弯曲时空，与自转无关）和楞次–蒂林进动（$-37.2$ mas/yr，源于地球自转）。

---

## 2. Gravitational Lensing and Gravitational-Wave Astronomy · 引力透镜与引力波天文学

**Definition.** When light from a distant source passes near a massive body, it is deflected, producing multiple images, arcs, or a complete ring — *gravitational lensing*. A completely separate observational window is opened by *gravitational waves* (GW): ripples in spacetime curvature propagating at c, generated by accelerating masses.

**定义。** 当来自遥远源的光经过大质量天体附近时，它被偏折，产生多个像、弧或完整的环——*引力透镜效应*。*引力波*（GW）则开辟了一个全新的观测窗口：由加速质量产生的、以光速传播的时空曲率涟漪。

**Demonstration — Gravitational Lensing.** The *thin-lens approximation* treats the deflecting mass as a point at angular diameter distance $D_L$ from the observer, with the source at $D_S$ and lens-to-source distance $D_{LS}$. The *lens equation* (see Derivations C) is:

**演示——引力透镜。** *薄透镜近似*将偏折质量视为位于角直径距离 $D_L$ 处的点，源位于 $D_S$ 处，透镜到源的距离为 $D_{LS}$。*透镜方程*（见推导 C）为：

$$ \beta = \theta - \frac{\theta_E^2}{\theta} $$

where $\beta$ is the true source position, $\theta$ is the image position, both measured as angles from the lens on the sky. The *Einstein ring radius* (angular) is:

其中 $\beta$ 为真实源位置，$\theta$ 为像位置，均从天空中透镜处量起。*爱因斯坦环半径*（角度）为：

$$ \theta_E = \sqrt{\frac{4GM\, D_{LS}}{c^2 D_L D_S}} $$

When source, lens, and observer are perfectly aligned ($\beta = 0$), the image is a complete ring of angular radius $\theta_E$. For a galaxy cluster acting as a lens, $\theta_E \sim 1'$. Gravitational lensing is now a primary tool for measuring dark matter distributions (weak lensing shear), discovering exoplanets (microlensing), and constraining the Hubble constant (time-delay lensing).

当源、透镜和观测者完美对齐（$\beta = 0$）时，像为角半径 $\theta_E$ 的完整圆环。对于作为透镜的星系团，$\theta_E \sim 1'$。引力透镜现已成为测量暗物质分布（弱透镜剪切）、发现系外行星（微透镜）和约束哈勃常数（时延透镜）的主要工具。

**Demonstration — LIGO/Virgo Interferometers.** A GW stretches space in one arm of a Michelson interferometer while compressing the perpendicular arm, causing a differential path-length change:

**演示——LIGO/Virgo 干涉仪。** 引力波拉伸迈克耳孙干涉仪的一臂空间，同时压缩垂直臂，导致差分光程变化：

$$ \Delta L = \frac{hL}{2} $$

where $h$ is the *strain* (dimensionless metric perturbation, $h \sim 10^{-21}$ for astrophysical sources) and $L$ is the arm length (4 km for LIGO). Fabry–Perot cavities increase the effective arm length to ~1600 km; power recycling boosts the light power to ~750 kW. The design sensitivity reaches $\Delta x \sim 10^{-18}$ m — below the classical uncertainty limit via squeezed light injection.

其中 $h$ 为*应变*（无量纲度规扰动，对天体物理源 $h \sim 10^{-21}$），$L$ 为臂长（LIGO 为 4 km）。法布里-珀罗腔将有效臂长增至约 1600 km；功率循环将光功率提升至约 750 kW。设计灵敏度达 $\Delta x \sim 10^{-18}$ m——通过压缩光注入突破了经典不确定性极限。

**Demonstration — Chirp of a Compact Binary Inspiral.** Two compact objects (neutron stars or black holes) in a circular orbit radiate GW energy (from the quadrupole formula, Module 7.5), causing the orbit to shrink. As the separation decreases, the orbital frequency increases, sweeping upward in frequency — a *chirp*. The instantaneous GW frequency is $f_\text{GW} = 2 f_\text{orbital}$. From the quadrupole power and orbital mechanics, the *chirp mass* $\mathcal{M}_c$ characterizes the inspiral rate:

**演示——致密双星并合的啁啾信号。** 圆形轨道上的两个致密天体（中子星或黑洞）辐射引力波能量（来自四极矩公式，模块 7.5），导致轨道收缩。随着间距减小，轨道频率升高，频率向上扫描——即*啁啾*。瞬时引力波频率为 $f_\text{GW} = 2 f_\text{orbital}$。由四极矩功率和轨道力学，*啁啾质量* $\mathcal{M}_c$ 表征了并合速率：

$$ \mathcal{M}_c = \frac{(m_1 m_2)^{3/5}}{(m_1 + m_2)^{1/5}} $$

The frequency evolution satisfies:

频率演化满足：

$$ \frac{df}{dt} = \frac{96\pi^{8/3}}{5} \left(\frac{G\mathcal{M}_c}{c^3}\right)^{5/3} f^{11/3} $$

Measuring the frequency chirp rate $df/dt$ and the frequency $f$ directly gives $\mathcal{M}_c$ from the observed signal alone — a *standard siren* calibration of distance independent of the cosmic distance ladder.

直接测量频率啁啾率 $df/dt$ 和频率 $f$，就可仅从观测信号中得到 $\mathcal{M}_c$——这是一种独立于宇宙距离阶梯的*标准汽笛*距离定标方法。

**Application — GW150914 and GW170817.**

**应用——GW150914 与 GW170817。**

*GW150914* (detected 14 September 2015, announced February 2016): the first direct detection of gravitational waves, from the merger of two stellar-mass black holes ($m_1 \approx 36\, M_\odot$, $m_2 \approx 29\, M_\odot$) at luminosity distance ~410 Mpc. The signal lasted ~0.2 s at LIGO frequencies (35–150 Hz), with peak strain $h \sim 10^{-21}$. The remnant is a black hole of $\sim 62\, M_\odot$ (with $\sim 3\, M_\odot c^2$ radiated as GWs). This confirmed the existence of stellar-mass black hole binaries and opened the era of GW astronomy.

*GW150914*（2015 年 9 月 14 日探测，2016 年 2 月公布）：首次直接探测到引力波，来自两个恒星质量黑洞（$m_1 \approx 36\, M_\odot$，$m_2 \approx 29\, M_\odot$）的并合，光度距离约 410 Mpc。信号在 LIGO 频率（35–150 Hz）处持续约 0.2 s，峰值应变 $h \sim 10^{-21}$。残余为约 $62\, M_\odot$ 的黑洞（约 $3\, M_\odot c^2$ 以引力波形式辐射）。这确认了恒星质量黑洞双星的存在，开启了引力波天文学时代。

*GW170817* (17 August 2017): the first binary neutron star merger detected in GWs, simultaneously observed across the electromagnetic spectrum (a *kilonova* in optical/infrared, a short gamma-ray burst GRB 170817A, and X-ray/radio afterglow) — the dawn of *multi-messenger astronomy*. Key results: the GW and gamma-ray signals arrived within 1.7 s of each other despite traveling ~40 Mpc, constraining the GW speed to $|v_\text{GW} - c|/c < 10^{-15}$; the kilonova ejecta showed r-process nucleosynthesis (confirming neutron star mergers as a site of heavy-element production); and the combined GW+EM distance and redshift gave $H_0 = 70^{+12}_{-8}$ km s$^{-1}$ Mpc$^{-1}$ (the first standard-siren Hubble measurement).

*GW170817*（2017 年 8 月 17 日）：首次在引力波中探测到双中子星并合，同时在全电磁波段观测到（光学/红外*千新星*、短伽马射线暴 GRB 170817A 以及 X 射线/射电余辉）——*多信使天文学*的黎明。主要结果：尽管经过约 40 Mpc 的传播，引力波和伽马射线信号仅相差 1.7 s 到达，将引力波速度约束在 $|v_\text{GW} - c|/c < 10^{-15}$；千新星抛射物显示出 r 过程核合成（证实中子星并合是重元素产生地）；引力波与电磁波联合给出的距离和红移测得 $H_0 = 70^{+12}_{-8}$ km s$^{-1}$ Mpc$^{-1}$（首次标准汽笛哈勃测量）。

---

**Self-test (blank page)**

1. Explain why the GR orbit equation contains an extra term $-GM\ell^2/c^2 r^3$ compared to the Newtonian case. Show how this leads to perihelion precession and state the result for Mercury.
2. The Newtonian deflection of light by the Sun gives $0.87''$; the GR result is $1.75''$. What extra physics (beyond a straight particle in a Newtonian potential) accounts for the factor of 2?
3. Define the chirp mass $\mathcal{M}_c$ and explain why it can be read off the GW frequency evolution alone. What additional information is needed to break the mass-ratio degeneracy?
4. Describe the multi-messenger significance of GW170817. What constraints did it place on GW propagation speed, on neutron star physics, and on the Hubble constant?

**自测（空白页）**

1. 解释为何广义相对论轨道方程比牛顿情形多出额外项 $-GM\ell^2/c^2 r^3$。说明这如何导致近日点进动，并给出水星的结果。
2. 牛顿光线偏折给出 $0.87''$；广义相对论结果为 $1.75''$。超出牛顿势中直线粒子的额外物理（因子 2）是什么？
3. 定义啁啾质量 $\mathcal{M}_c$，并解释为何仅凭引力波频率演化就能读出它。还需要什么额外信息才能解除质量比的简并？
4. 描述 GW170817 多信使观测的意义。它对引力波传播速度、中子星物理和哈勃常数分别给出了哪些约束？

---

← Previous: [Module 7.6 — Cosmology](./module-7.6-cosmology.md) · [Phase 7 index](./README.md) · Next: [Module 7.8 — Global Structure & Singularity Theorems](./module-7.8-global-structure-and-singularity-theorems.md) →

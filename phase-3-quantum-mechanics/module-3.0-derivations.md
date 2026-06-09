# Derivations — Module 3.0: Old Quantum Theory & the Photoelectric Effect
# 推导 — 模块 3.0：旧量子论与光电效应

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.0](./module-3.0-old-quantum-theory-and-photoelectric-effect.md). Full step-by-step proofs of every non-trivial result quoted there. English first, then 中文.
> [模块 3.0](./module-3.0-old-quantum-theory-and-photoelectric-effect.md) 的配套文档：对该模块所引用每个非平凡结果的完整逐步证明。先英文，后中文。

---

## A. Photoelectric Effect: $KE_{\max} = h\nu - W$ and the Stopping-Voltage Line · 光电效应：$KE_{\max} = h\nu - W$ 与截止电压直线

**Claim.** When light of frequency $\nu$ strikes a metal with work function $W$, the maximum kinetic energy of ejected electrons is $KE_{\max} = h\nu - W$, and the stopping voltage $V_{\text{stop}}$ satisfies $e V_{\text{stop}} = h\nu - W$ — a straight line in $\nu$ with slope $h/e$ and $y$-intercept $-W/e$.

**命题。** 当频率为 $\nu$ 的光照射逸出功为 $W$ 的金属时，被射出电子的最大动能为 $KE_{\max} = h\nu - W$，截止电压 $V_{\text{stop}}$ 满足 $e V_{\text{stop}} = h\nu - W$——这是关于 $\nu$ 的一条直线，斜率为 $h/e$，纵截距为 $-W/e$。

**Step 1 — Einstein's photon hypothesis.** Model light of frequency $\nu$ as a stream of photons, each carrying energy $E_{\text{photon}} = h\nu$. This is a postulate; its self-consistency is confirmed by what follows.

**第 1 步 — 爱因斯坦光子假说。** 将频率为 $\nu$ 的光建模为光子流，每个光子携带能量 $E_{\text{photon}} = h\nu$。这是一个假设；其自洽性由以下推导得到验证。

**Step 2 — Energy accounting for one absorption event.** When a single photon is absorbed by a conduction electron inside the metal, all of the photon's energy $h\nu$ is transferred to that one electron (photons are absorbed whole, not split). The electron must then overcome the binding energy $W$ (the minimum energy needed to escape the metal surface — the work function). After escaping, the electron has kinetic energy

**第 2 步 — 单次吸收事件的能量守恒。** 当一个光子被金属内的传导电子吸收时，光子的全部能量 $h\nu$ 转移给该电子（光子被整体吸收，不可分割）。电子随后必须克服结合能 $W$（逃离金属表面所需的最小能量——逸出功）。逃逸后，电子的动能为

$$ KE = h\nu - W - (\text{extra binding energy of that electron's initial position}). $$

$$ KE = h\nu - W - (\text{该电子初始位置的额外结合能}). $$

**Step 3 — Maximizing the kinetic energy.** Electrons at the top of the conduction band (i.e., those with the smallest additional binding energy, which is zero by definition of the work function) escape with the maximum kinetic energy:

**第 3 步 — 最大化动能。** 处于导带顶部的电子（即额外结合能最小为零的电子，这正是逸出功的定义）以最大动能逃逸：

$$ KE_{\max} = h\nu - W. $$

This is zero when $h\nu = W$ (the threshold frequency $\nu_0 = W/h$). For $h\nu < W$ no electron escapes at all, regardless of intensity — because one electron absorbs one photon and that single quantum of energy is insufficient. This explains why a dim ultraviolet source ejects electrons while a bright red source does not.

当 $h\nu = W$ 时此值为零（阈值频率 $\nu_0 = W/h$）。当 $h\nu < W$ 时无论光强多大都没有电子逸出——因为一个电子吸收一个光子，而那单个能量子不足以使其逃脱。这就解释了为何微弱紫外光能射出电子而强烈红光却不能。

**Step 4 — The stopping voltage.** Apply a retarding potential $V_{\text{stop}}$ (the collector is negative relative to the emitter). The electric field does negative work $-eV_{\text{stop}}$ on the electron as it travels from emitter to collector. The fastest electrons (those with $KE_{\max}$) are just stopped when all their kinetic energy has been converted to electrical potential energy:

**第 4 步 — 截止电压。** 施加反向截止电位 $V_{\text{stop}}$（收集极相对于发射极为负极）。电场对电子做负功 $-eV_{\text{stop}}$。当最快电子（具有 $KE_{\max}$ 的电子）的全部动能转化为电势能时，它们恰好被截止：

$$ KE_{\max} = e V_{\text{stop}}. $$

Substituting $KE_{\max}$:

代入 $KE_{\max}$：

$$ e V_{\text{stop}} = h\nu - W, $$

$$ V_{\text{stop}} = \frac{h}{e}\,\nu - \frac{W}{e}. $$

**Step 5 — Interpretation of the line.** This is a linear function of $\nu$: slope $h/e$ is universal (independent of the metal), and the $y$-intercept $-W/e$ depends on the material. Plotting $V_{\text{stop}}$ vs $\nu$ gives a straight line; the slope yields $h$ directly, confirming Planck's constant from a completely different experiment. The $x$-intercept $\nu_0 = W/h$ is the threshold. $\blacksquare$

**第 5 步 — 直线的解释。** 这是关于 $\nu$ 的线性函数：斜率 $h/e$ 是普适的（与金属无关），纵截距 $-W/e$ 取决于材料。绘出 $V_{\text{stop}}$ 对 $\nu$ 的图像为一条直线；斜率直接给出 $h$，从一个完全不同的实验中证实了普朗克常数。横截距 $\nu_0 = W/h$ 是阈值频率。$\blacksquare$

---

## B. Bohr Hydrogen Atom: Energies $E_n = -13.6\ \text{eV} / n^2$ · 玻尔氢原子：能量 $E_n = -13.6\ \text{eV} / n^2$

**Claim.** For the hydrogen atom, combining the Coulomb force law with Bohr's angular-momentum quantization postulate $L = n\hbar$ yields circular-orbit energies $E_n = -me^4/(2\hbar^2 n^2) = -13.6\ \text{eV} / n^2$.

**命题。** 对于氢原子，将库仑力定律与玻尔角动量量子化假设 $L = n\hbar$ 结合，得到圆形轨道能量 $E_n = -me^4/(2\hbar^2 n^2) = -13.6\ \text{eV} / n^2$。

**Step 1 — Setup and notation.** Consider an electron (mass $m$, charge $-e$) orbiting a proton (charge $+e$, assumed infinitely massive) in a circular orbit of radius $r$ with speed $v$. We use SI units: the Coulomb constant $k_e = 1/(4\pi\varepsilon_0)$. The Coulomb force provides the centripetal acceleration:

**第 1 步 — 建立符号与方程。** 考虑质量为 $m$、电荷为 $-e$ 的电子在半径为 $r$、速度为 $v$ 的圆轨道上绕质量无穷大的质子（电荷 $+e$）运动。使用SI单位制：库仑常数 $k_e = 1/(4\pi\varepsilon_0)$。库仑力提供向心加速度：

$$ \frac{k_e e^2}{r^2} = \frac{m v^2}{r}. \qquad (1) $$

**Step 2 — Apply Bohr's quantization postulate.** Bohr postulated that only orbits with angular momentum equal to an integer multiple of $\hbar$ are allowed:

**第 2 步 — 应用玻尔量子化假设。** 玻尔假设只有角动量等于 $\hbar$ 整数倍的轨道才被允许：

$$ L = m v r = n\hbar, \qquad n = 1, 2, 3, \ldots \qquad (2) $$

**Step 3 — Solve for $v$ and $r$ in terms of $n$.** From (2): $v = n\hbar/(mr)$. Substitute into (1):

**第 3 步 — 用 $n$ 表示 $v$ 和 $r$。** 由 (2)：$v = n\hbar/(mr)$。代入 (1)：

$$ \frac{k_e e^2}{r^2} = \frac{m v^2}{r} = \frac{m (n\hbar)^2}{m^2 r^2 \cdot r} = \frac{n^2\hbar^2}{mr^3}. $$

Multiply both sides by $r^3$:

两边乘以 $r^3$：

$$ k_e e^2 r = \frac{n^2\hbar^2}{m}. $$

$$ r = \frac{n^2\hbar^2}{m k_e e^2} = n^2 a_0, $$

where $a_0 = \hbar^2/(m k_e e^2) \approx 0.529\ \text{Å}$ is the **Bohr radius**. So $r_n = n^2 a_0$ — the radius grows as $n^2$.

其中 $a_0 = \hbar^2/(m k_e e^2) \approx 0.529\ \text{Å}$ 是**玻尔半径**。因此 $r_n = n^2 a_0$——半径随 $n^2$ 增大。

From $v = n\hbar/(mr)$:

由 $v = n\hbar/(mr)$：

$$ v_n = \frac{n\hbar}{m \cdot n^2 a_0} = \frac{\hbar}{mn a_0} = \frac{k_e e^2}{n\hbar}. $$

**Step 4 — Compute the total energy.** The total mechanical energy is kinetic plus potential:

**第 4 步 — 计算总能量。** 总机械能为动能加势能：

$$ E = \tfrac12 m v^2 - \frac{k_e e^2}{r}. $$

From (1): $k_e e^2/r = mv^2$, so the kinetic energy is $\tfrac12 m v^2 = \tfrac12 k_e e^2/r$, and:

由 (1)：$k_e e^2/r = mv^2$，故动能为 $\tfrac12 m v^2 = \tfrac12 k_e e^2/r$，从而：

$$ E = \frac{1}{2}\frac{k_e e^2}{r} - \frac{k_e e^2}{r} = -\frac{1}{2}\frac{k_e e^2}{r}. $$

This is the **virial theorem** for a $1/r$ potential: $E_{\text{total}} = -\tfrac12|V|$. Now substitute $r_n = n^2 a_0$:

这是 $1/r$ 势的**位力定理**：$E_{\text{total}} = -\tfrac12|V|$。代入 $r_n = n^2 a_0$：

$$ E_n = -\frac{1}{2}\frac{k_e e^2}{n^2 a_0} = -\frac{1}{2} k_e e^2 \cdot \frac{m k_e e^2}{n^2\hbar^2} = -\frac{m k_e^2 e^4}{2n^2\hbar^2}. $$

**Step 5 — Evaluate numerically.** The ground-state energy ($n = 1$) is the Rydberg energy:

**第 5 步 — 数值计算。** 基态能量（$n = 1$）为里德伯能量：

$$ E_1 = -\frac{m k_e^2 e^4}{2\hbar^2}. $$

Using $m = 9.109 \times 10^{-31}\ \text{kg}$, $k_e = 8.988 \times 10^{9}\ \text{N}\cdot\text{m}^2/\text{C}^2$, $e = 1.602 \times 10^{-19}\ \text{C}$, $\hbar = 1.055 \times 10^{-34}\ \text{J}\cdot\text{s}$:

$$ E_1 = -2.179 \times 10^{-18}\ \text{J} = -13.6\ \text{eV}. $$

Therefore:

因此：

$$ \boxed{\, E_n = -13.6\ \text{eV} / n^2 \,}, \qquad n = 1, 2, 3, \ldots $$

Spectral lines arise from transitions between levels: $h\nu = E_n - E_m$ ($m < n$), giving the Rydberg formula. $\blacksquare$

谱线来自能级跃迁：$h\nu = E_n - E_m$（$m < n$），给出里德伯公式。$\blacksquare$

---

## C. Compton Scattering: $\Delta\lambda = (h/mc)(1 - \cos\theta)$ · 康普顿散射：$\Delta\lambda = (h/mc)(1 - \cos\theta)$

**Claim.** When a photon scatters off a free electron initially at rest, the photon's wavelength shifts by $\Delta\lambda = \lambda' - \lambda = (h/mc)(1 - \cos\theta)$, where $\theta$ is the photon's scattering angle and $h/mc$ is the **Compton wavelength** $\lambda_C \approx 2.426\ \text{pm}$.

**命题。** 当光子从静止的自由电子上散射时，光子的波长偏移为 $\Delta\lambda = \lambda' - \lambda = (h/mc)(1 - \cos\theta)$，其中 $\theta$ 为光子散射角，$h/mc$ 为**康普顿波长** $\lambda_C \approx 2.426\ \text{pm}$。

**Step 1 — Assign four-momenta.** Use relativistic mechanics. Photon has energy $E = h\nu = hc/\lambda$ and momentum $p = h/\lambda$ (magnitude). Electron starts at rest: energy $mc^2$, momentum $0$. Let the photon scatter at angle $\theta$ and the electron recoil at angle $\varphi$. Define:

**第 1 步 — 指定四动量。** 使用相对论力学。光子能量 $E = h\nu = hc/\lambda$，动量大小 $p = h/\lambda$。电子初始静止：能量 $mc^2$，动量为零。设光子散射角为 $\theta$，电子反冲角为 $\varphi$。定义：

$$ \begin{aligned} &\text{Initial photon:} && \text{energy } hc/\lambda, && x\text{-momentum } h/\lambda, && y\text{-momentum } 0. \\ &\text{Initial electron:} && \text{energy } mc^2, && x\text{-momentum } 0, && y\text{-momentum } 0. \\ &\text{Final photon:} && \text{energy } hc/\lambda', && x\text{-momentum } (h/\lambda')\cos\theta, && y\text{-momentum } (h/\lambda')\sin\theta. \\ &\text{Final electron:} && \text{energy } E_e, && x\text{-momentum } p_e \cos\varphi, && y\text{-momentum } -p_e \sin\varphi. \end{aligned} $$

**Step 2 — Conservation laws.** Energy conservation:

**第 2 步 — 守恒定律。** 能量守恒：

$$ \frac{hc}{\lambda} + mc^2 = \frac{hc}{\lambda'} + E_e. \qquad (\text{i}) $$

$x$-momentum conservation:

$x$ 方向动量守恒：

$$ \frac{h}{\lambda} = \frac{h}{\lambda'}\cos\theta + p_e \cos\varphi. \qquad (\text{ii}) $$

$y$-momentum conservation:

$y$ 方向动量守恒：

$$ 0 = \frac{h}{\lambda'}\sin\theta - p_e \sin\varphi. \qquad (\text{iii}) $$

**Step 3 — Eliminate the electron variables.** Isolate the electron momentum components from (ii) and (iii):

**第 3 步 — 消去电子变量。** 从 (ii) 和 (iii) 中分离出电子动量分量：

$$ p_e \cos\varphi = \frac{h}{\lambda} - \frac{h}{\lambda'}\cos\theta, \qquad p_e \sin\varphi = \frac{h}{\lambda'}\sin\theta. $$

Square and add to eliminate $\varphi$:

平方相加以消去 $\varphi$：

$$ p_e^2 = \left(\frac{h}{\lambda}\right)^2 - 2\frac{h}{\lambda}\frac{h}{\lambda'}\cos\theta + \left(\frac{h}{\lambda'}\right)^2. \qquad (\text{iv}) $$

From energy conservation (i): $E_e = hc/\lambda - hc/\lambda' + mc^2$. Use the relativistic energy–momentum relation $E_e^2 = (p_e c)^2 + (mc^2)^2$:

由能量守恒 (i)：$E_e = hc/\lambda - hc/\lambda' + mc^2$。利用相对论能量–动量关系 $E_e^2 = (p_e c)^2 + (mc^2)^2$：

$$ \left(\frac{hc}{\lambda} - \frac{hc}{\lambda'} + mc^2\right)^2 = (p_e c)^2 + (mc^2)^2. $$

Expand the left side:

展开左边：

$$ \left(\frac{hc}{\lambda} - \frac{hc}{\lambda'}\right)^2 + 2mc^2\left(\frac{hc}{\lambda} - \frac{hc}{\lambda'}\right) + (mc^2)^2 = (p_e c)^2 + (mc^2)^2. $$

The $(mc^2)^2$ cancels:

$(mc^2)^2$ 消去：

$$ \left(\frac{hc}{\lambda} - \frac{hc}{\lambda'}\right)^2 + 2mc^2\left(\frac{hc}{\lambda} - \frac{hc}{\lambda'}\right) = (p_e c)^2. $$

Divide by $c^2$:

除以 $c^2$：

$$ \left(\frac{h}{\lambda} - \frac{h}{\lambda'}\right)^2 + 2mc\left(\frac{h}{\lambda} - \frac{h}{\lambda'}\right) = p_e^2. \qquad (\text{v}) $$

**Step 4 — Equate the two expressions for $p_e^2$.** From (iv) and (v):

**第 4 步 — 联立 $p_e^2$ 的两个表达式。** 由 (iv) 与 (v)：

$$ \left(\frac{h}{\lambda}\right)^2 - 2\frac{h}{\lambda}\frac{h}{\lambda'}\cos\theta + \left(\frac{h}{\lambda'}\right)^2 = \left(\frac{h}{\lambda} - \frac{h}{\lambda'}\right)^2 + 2mc\left(\frac{h}{\lambda} - \frac{h}{\lambda'}\right). $$

Expand the right side: $(h/\lambda)^2 - 2(h^2/\lambda\lambda') + (h/\lambda')^2 + 2mc(h/\lambda - h/\lambda')$. The $(h/\lambda)^2$ and $(h/\lambda')^2$ cancel from both sides:

展开右边：$(h/\lambda)^2 - 2(h^2/\lambda\lambda') + (h/\lambda')^2 + 2mc(h/\lambda - h/\lambda')$。两边的 $(h/\lambda)^2$ 和 $(h/\lambda')^2$ 消去：

$$ -2\frac{h^2}{\lambda\lambda'}\cos\theta = -2\frac{h^2}{\lambda\lambda'} + 2mc\left(\frac{h}{\lambda} - \frac{h}{\lambda'}\right). $$

Rearrange:

整理：

$$ 2\frac{h^2}{\lambda\lambda'} - 2\frac{h^2}{\lambda\lambda'}\cos\theta = 2mc\left(\frac{h}{\lambda} - \frac{h}{\lambda'}\right). $$

$$ \frac{h^2}{\lambda\lambda'}(1 - \cos\theta) = mc \cdot \frac{h(\lambda' - \lambda)}{\lambda\lambda'}. $$

Multiply both sides by $\lambda\lambda'/(mch)$:

两边乘以 $\lambda\lambda'/(mch)$：

$$ \frac{h(1 - \cos\theta)}{mc} = \lambda' - \lambda. $$

Therefore:

因此：

$$ \boxed{\, \Delta\lambda = \lambda' - \lambda = \frac{h}{mc}(1 - \cos\theta) \,} \qquad \blacksquare $$

**Step 5 — Properties.** The Compton wavelength $\lambda_C = h/mc \approx 2.426 \times 10^{-12}\ \text{m}$. The shift $\Delta\lambda$ depends only on the scattering angle $\theta$, not on the initial wavelength — a purely particle-collision result. Maximum shift $2\lambda_C$ occurs at $\theta = 180°$ (backscattering). No shift at $\theta = 0°$ (forward scattering, no collision).

**第 5 步 — 性质。** 康普顿波长 $\lambda_C = h/mc \approx 2.426 \times 10^{-12}\ \text{m}$。偏移 $\Delta\lambda$ 仅取决于散射角 $\theta$，与初始波长无关——这是纯粒子碰撞的结果。最大偏移 $2\lambda_C$ 在 $\theta = 180°$（反向散射）时发生。$\theta = 0°$（前向散射，无碰撞）时无偏移。$\blacksquare$

---

## D. de Broglie Relation: $\lambda = h/p$ · 德布罗意关系：$\lambda = h/p$

**Claim.** By symmetry with the photon, a matter particle of momentum $p$ has an associated wavelength $\lambda = h/p$.

**命题。** 根据与光子的对称性，动量为 $p$ 的物质粒子具有对应波长 $\lambda = h/p$。

**Step 1 — Photon relations as template.** For a photon: energy $E = h\nu = hc/\lambda$ and momentum $p = E/c = h\nu/c = h/\lambda$. Equivalently, in terms of angular frequency $\omega = 2\pi\nu$ and wave vector $k = 2\pi/\lambda$:

**第 1 步 — 以光子关系为模板。** 对于光子：能量 $E = h\nu = hc/\lambda$，动量 $p = E/c = h\nu/c = h/\lambda$。等价地，用角频率 $\omega = 2\pi\nu$ 和波矢 $k = 2\pi/\lambda$ 表示：

$$ E = \hbar\omega, \qquad p = \hbar k. $$

**Step 2 — de Broglie's hypothesis.** de Broglie (1924) proposed that these same relations hold for massive particles. The motivation: Einstein had shown (special relativity + photon) that energy and momentum mix under Lorentz boosts, so both relations $E = \hbar\omega$ and $p = \hbar k$ must hold together, or neither. If a particle has a definite momentum $p$, then it has a definite wave vector $k = p/\hbar$ and hence a wavelength:

**第 2 步 — 德布罗意假说。** 德布罗意（1924 年）提出这些相同的关系对有质量的粒子同样成立。动机：爱因斯坦已经表明（狭义相对论加光子）能量和动量在洛伦兹变换下混合，因此 $E = \hbar\omega$ 和 $p = \hbar k$ 这两个关系必须同时成立，或者都不成立。如果粒子有确定的动量 $p$，则它有确定的波矢 $k = p/\hbar$，从而有波长：

$$ \boxed{\, \lambda = \frac{2\pi}{k} = \frac{2\pi\hbar}{p} = \frac{h}{p} \,} $$

**Step 3 — Consistency with Bohr quantization.** If an electron's de Broglie wave must form a standing wave around a circular orbit of circumference $2\pi r$, then an integer number of wavelengths must fit:

**第 3 步 — 与玻尔量子化的一致性。** 如果电子的德布罗意波必须在周长为 $2\pi r$ 的圆形轨道上形成驻波，则必须有整数个波长容纳在其中：

$$ n \lambda = 2\pi r \implies n\frac{h}{p} = 2\pi r \implies pr = n\hbar \implies L = n\hbar. $$

This reproduces Bohr's quantization postulate — it is not an independent assumption but follows from wave fitting. This retroactively justifies Bohr's rule. $\blacksquare$

这重现了玻尔的量子化假设——它不是独立的假设，而是由波的配合条件推出的。这从回溯的角度为玻尔定则提供了合理性。$\blacksquare$

**Step 4 — Experimental confirmation.** Davisson–Germer (1927): an electron beam (accelerated through voltage $V$, giving $p = \sqrt{2meV}$) diffracts off a Ni crystal with lattice spacing $d$. The diffraction maxima obey Bragg's law $d \sin\theta = n\lambda$ with $\lambda = h/\sqrt{2meV}$ — confirmed to high precision.

**第 4 步 — 实验确认。** 戴维孙–革末实验（1927 年）：经电压 $V$ 加速的电子束（动量 $p = \sqrt{2meV}$）从晶格间距为 $d$ 的 Ni 晶体上衍射。衍射极大满足布拉格定律 $d \sin\theta = n\lambda$，其中 $\lambda = h/\sqrt{2meV}$——以高精度得到证实。$\blacksquare$

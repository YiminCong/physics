---
title: "Derivations — Module 8.2: Quantum Electrodynamics (QED)"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 8.2: Quantum Electrodynamics (QED)
# 推导 — 模块 8.2：量子电动力学

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 8.2](./module-8.2-quantum-electrodynamics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 8.2](./module-8.2-quantum-electrodynamics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The QED Lagrangian and Equations of Motion · QED 拉格朗日量与运动方程

**Claim.** The QED Lagrangian $\mathcal{L}_\text{QED} = \bar\psi(i\gamma^\mu D_\mu - m)\psi - (1/4)F_{\mu\nu}F^{\mu\nu}$ (with $D_\mu = \partial_\mu + ieA_\mu$) yields the Dirac equation with electromagnetic coupling and the Maxwell equations with a source.

**命题。** QED 拉格朗日量 $\mathcal{L}_\text{QED} = \bar\psi(i\gamma^\mu D_\mu - m)\psi - (1/4)F_{\mu\nu}F^{\mu\nu}$（$D_\mu = \partial_\mu + ieA_\mu$）给出带有电磁耦合的狄拉克方程和带有源的麦克斯韦方程。

**Step 1 — Expand the Lagrangian.** Writing out $D_\mu$:

**第 1 步 — 展开拉格朗日量。** 写出 $D_\mu$：

$$ \mathcal{L}_\text{QED} = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi - e\bar\psi\gamma^\mu\psi A_\mu - (1/4)F_{\mu\nu}F^{\mu\nu}. $$

The three terms are: (i) free Dirac field, (ii) fermion–photon interaction vertex $-e\bar\psi\gamma^\mu\psi A_\mu$, (iii) free photon kinetic term.

三项分别为：(i) 自由狄拉克场，(ii) 费米子–光子相互作用顶角 $-e\bar\psi\gamma^\mu\psi A_\mu$，(iii) 自由光子动能项。

**Step 2 — Euler–Lagrange for $\bar\psi$ (varies $\psi$).** The E–L equation is:

**第 2 步 — 对 $\bar\psi$ 的欧拉–拉格朗日方程（变分 $\psi$）。** E–L 方程为：

$$ \partial\mathcal{L}/\partial\bar\psi - \partial_\mu(\partial\mathcal{L}/\partial(\partial_\mu\bar\psi)) = 0. $$

Since $\mathcal{L}$ contains $\bar\psi$ but not $\partial_\mu\bar\psi$ (only $\partial_\mu\psi$ appears in the kinetic term):

由于 $\mathcal{L}$ 含 $\bar\psi$ 但不含 $\partial_\mu\bar\psi$（动能项中只含 $\partial_\mu\psi$）：

$$ \partial\mathcal{L}/\partial\bar\psi = (i\gamma^\mu\partial_\mu - m)\psi - e\gamma^\mu A_\mu\psi = (i\gamma^\mu D_\mu - m)\psi = 0. $$

This is the **gauged Dirac equation**: $(i\gamma^\mu D_\mu - m)\psi = 0$, i.e., $(i\gamma^\mu(\partial_\mu + ieA_\mu) - m)\psi = 0$.

这是**规范化狄拉克方程**：$(i\gamma^\mu D_\mu - m)\psi = 0$，即 $(i\gamma^\mu(\partial_\mu + ieA_\mu) - m)\psi = 0$。

**Step 3 — Euler–Lagrange for $A_\nu$.** Now vary $A_\nu$:

**第 3 步 — 对 $A_\nu$ 的欧拉–拉格朗日方程。** 现变分 $A_\nu$：

$$ \begin{aligned} \partial\mathcal{L}/\partial A_\nu &= -e\bar\psi\gamma^\nu\psi = -ej^\nu. \\ \partial\mathcal{L}/\partial(\partial_\mu A_\nu) &= -F^{\mu\nu} \quad \text{(since } F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu\text{).} \end{aligned} $$

The E–L equation $\partial\mathcal{L}/\partial A_\nu - \partial_\mu(\partial\mathcal{L}/\partial(\partial_\mu A_\nu)) = 0$ gives:

E–L 方程 $\partial\mathcal{L}/\partial A_\nu - \partial_\mu(\partial\mathcal{L}/\partial(\partial_\mu A_\nu)) = 0$ 给出：

$$ -ej^\nu + \partial_\mu F^{\mu\nu} = 0 \implies \partial_\mu F^{\mu\nu} = ej^\nu. $$

This is **Maxwell's equation** in covariant form with source $j^\nu = \bar\psi\gamma^\nu\psi$ (the electromagnetic current). The homogeneous equation $\partial_{[\mu}F_{\nu\rho]} = 0$ (Bianchi identity) follows automatically from $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$. $\blacksquare$

这是协变形式的**麦克斯韦方程**，源为 $j^\nu = \bar\psi\gamma^\nu\psi$（电磁流）。齐次方程 $\partial_{[\mu}F_{\nu\rho]} = 0$（Bianchi 恒等式）自动由 $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ 得出。$\blacksquare$

---

## B. Feynman Rules from the QED Lagrangian · 由 QED 拉格朗日量导出费曼规则

**Claim.** The QED interaction vertex is $-ie\gamma^\mu$, the photon propagator (in Feynman gauge) is $-ig_{\mu\nu}/q^2$, and the fermion propagator is $i(\gamma^\mu p_\mu + m)/(p^2 - m^2 + i\varepsilon)$.

**命题。** QED 相互作用顶角为 $-ie\gamma^\mu$，光子传播子（费曼规范）为 $-ig_{\mu\nu}/q^2$，费米子传播子为 $i(\gamma^\mu p_\mu + m)/(p^2 - m^2 + i\varepsilon)$。

**Step 1 — Path integral approach / perturbation theory.** The S-matrix element is computed as the perturbative expansion of $\langle 0|T[\ldots]|0\rangle$ with the interaction Lagrangian treated as a perturbation. The interaction term is:

**第 1 步 — 路径积分方法/微扰论。** S 矩阵元作为 $\langle 0|T[\ldots]|0\rangle$ 的微扰展开来计算，相互作用拉格朗日量作为微扰处理。相互作用项为：

$$ \mathcal{L}_\text{int} = -e\bar\psi\gamma^\mu\psi A_\mu = -ej^\mu A_\mu. $$

Each power of $\mathcal{L}_\text{int}$ in the Dyson series contributes one vertex. A single insertion gives:

狄森级数中 $\mathcal{L}_\text{int}$ 的每一幂次贡献一个顶角。单次插入给出：

$$ -ie \int d^4x\, \bar\psi(x)\gamma^\mu\psi(x)A_\mu(x). $$

In momentum space, each vertex contributes a factor $-ie\gamma^\mu$ (with momentum conservation enforced by a delta function at each vertex).

在动量空间，每个顶角贡献因子 $-ie\gamma^\mu$（通过每个顶角处的 $\delta$ 函数强制动量守恒）。

**Step 2 — Fermion propagator.** The free Dirac Lagrangian $\mathcal{L}_D = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$ gives the equation of motion $(i\gamma^\mu\partial_\mu - m)\psi = 0$. In momentum space ($\partial_\mu \to -ip_\mu$):

**第 2 步 — 费米子传播子。** 自由狄拉克拉格朗日量 $\mathcal{L}_D = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$ 给出运动方程 $(i\gamma^\mu\partial_\mu - m)\psi = 0$。在动量空间（$\partial_\mu \to -ip_\mu$）：

$$ (\gamma^\mu p_\mu - m)\psi(p) = 0. $$

The propagator $S_F(p)$ is the inverse of the kinetic operator $(\gamma^\mu p_\mu - m)$:

传播子 $S_F(p)$ 是动能算符 $(\gamma^\mu p_\mu - m)$ 的逆：

$$ S_F(p) = i/(\gamma^\mu p_\mu - m + i\varepsilon). $$

Multiply numerator and denominator by $(\gamma^\nu p_\nu + m)$:

分子分母同乘 $(\gamma^\nu p_\nu + m)$：

$$ \begin{aligned} (\gamma^\mu p_\mu - m)(\gamma^\nu p_\nu + m) &= \gamma^\mu\gamma^\nu p_\mu p_\nu - m^2 = (1/2)\{\gamma^\mu,\gamma^\nu\}p_\mu p_\nu - m^2 \\ &= g^{\mu\nu}p_\mu p_\nu - m^2 = p^2 - m^2. \end{aligned} $$

Therefore:

因此：

$$ S_F(p) = i(\gamma^\mu p_\mu + m)/(p^2 - m^2 + i\varepsilon). $$

The $i\varepsilon$ prescription (Feynman prescription) encodes the correct time-ordering and corresponds to particles propagating forward in time and antiparticles backward.

$i\varepsilon$ 处方（费曼处方）编码了正确的时间排序，对应于粒子向前传播、反粒子向后传播（在时间上）。

**Step 3 — Photon propagator.** The free photon action is $-(1/4)\int F_{\mu\nu}F^{\mu\nu}d^4x$. In momentum space with a gauge-fixing term $-(1/2\xi)(\partial_\mu A^\mu)^2$ (Lorenz gauge parameter $\xi$):

**第 3 步 — 光子传播子。** 自由光子作用量为 $-(1/4)\int F_{\mu\nu}F^{\mu\nu}d^4x$。在动量空间中，加入规范固定项 $-(1/2\xi)(\partial_\mu A^\mu)^2$（洛伦兹规范参数 $\xi$）：

$$ S_\text{photon} = \int d^4q/(2\pi)^4\, A^\mu(q)[-g_{\mu\nu} q^2 + q_\mu q_\nu(1 - 1/\xi)]A^\nu(-q). $$

The kinetic operator in brackets has the inverse (photon propagator):

括号中的动能算符的逆（光子传播子）为：

$$ D_F^{\mu\nu}(q) = -i[g^{\mu\nu} - (1-\xi)q^\mu q^\nu/q^2]/(q^2 + i\varepsilon). $$

In **Feynman gauge** $\xi = 1$, this simplifies to:

在**费曼规范** $\xi = 1$ 中，化简为：

$$ D_F^{\mu\nu}(q) = -ig^{\mu\nu}/(q^2 + i\varepsilon). $$

The longitudinal piece $\propto q^\mu q^\nu$ drops out in gauge-invariant physical amplitudes (Ward identities). $\blacksquare$

纵向部分 $\propto q^\mu q^\nu$ 在规范不变的物理振幅中消失（沃德恒等式）。$\blacksquare$

---

## C. Tree-Level $e^+e^- \to \mu^+\mu^-$ Amplitude and Cross-Section · 树图 $e^+e^- \to \mu^+\mu^-$ 振幅与散射截面

**Claim.** At tree level (leading order in $\alpha$), the differential cross-section for $e^+e^- \to \mu^+\mu^-$ in the center-of-mass frame at high energy ($\sqrt{s} \gg m_e, m_\mu$) is:

**命题。** 在树图（$\alpha$ 的领头阶），高能质心系（$\sqrt{s} \gg m_e, m_\mu$）中 $e^+e^- \to \mu^+\mu^-$ 的微分散射截面为：

$$ d\sigma/d\Omega = \alpha^2/(4s) \cdot (1 + \cos^2\theta), $$

integrating to $\sigma_\text{total} = 4\pi\alpha^2/(3s)$.

积分得 $\sigma_\text{total} = 4\pi\alpha^2/(3s)$。

**Step 1 — The Feynman diagram.** At tree level there is a single diagram: $e^-(p_1) + e^+(p_2)$ annihilate into a virtual photon (momentum $q = p_1 + p_2$), which creates $\mu^-(k_1) + \mu^+(k_2)$. Using the Feynman rules:

**第 1 步 — 费曼图。** 在树图阶，只有一个图：$e^-(p_1) + e^+(p_2)$ 湮灭为虚光子（动量 $q = p_1 + p_2$），产生 $\mu^-(k_1) + \mu^+(k_2)$。利用费曼规则：

$$ iM = [\bar v(p_2)(-ie\gamma^\mu)u(p_1)] \cdot [-ig_{\mu\nu}/q^2] \cdot [\bar u(k_1)(-ie\gamma^\nu)v(k_2)]. $$

So:

故：

$$ M = -e^2/q^2 \cdot [\bar v(p_2)\gamma^\mu u(p_1)] \cdot [\bar u(k_1)\gamma_\mu v(k_2)]. $$

At center of mass $s = q^2 = (p_1 + p_2)^2$, so $M = (e^2/s)J_e^\mu J_{\mu,\mu}$ where $J^\mu$ are the currents.

在质心系 $s = q^2 = (p_1 + p_2)^2$，故 $M = (e^2/s)J_e^\mu J_{\mu,\mu}$，$J^\mu$ 为流。

**Step 2 — Spin sum.** We average over initial spins and sum over final spins. Using the completeness relations:

**第 2 步 — 自旋求和。** 对初态自旋取平均，对末态自旋求和。利用完备性关系：

$$ \sum_\text{spins} u(p,s)\bar u(p,s) = \gamma^\mu p_\mu + m, \quad \sum_\text{spins} v(p,s)\bar v(p,s) = \gamma^\mu p_\mu - m. $$

The spin-summed/averaged $|M|^2$ is:

自旋求和/平均后的 $|M|^2$ 为：

$$ \langle|M|^2\rangle = (e^4/4s^2) \cdot \mathrm{Tr}[(\gamma^\mu\not{p}_1 + m_e)\gamma^\nu(\gamma^\rho\not{p}_2 - m_e)\gamma^\sigma] \cdot g_{\mu\rho}g_{\nu\sigma} \cdot \text{(Leptonic tensors)} $$

More precisely:

更精确地：

$$ \langle|M|^2\rangle = (e^4/4s^2) \cdot L^{\mu\nu}_e \cdot L_{\mu\nu,\mu} $$

where $L^{\mu\nu}_e = \mathrm{Tr}[(\not{p}_1 + m_e)\gamma^\mu(\not{p}_2 - m_e)\gamma^\nu]$ is the electron leptonic tensor, and $L_{\mu\nu,\mu} = \mathrm{Tr}[(\not{k}_1 + m_\mu)\gamma_\mu(\not{k}_2 - m_\mu)\gamma_\nu]$ is the muon leptonic tensor.

其中 $L^{\mu\nu}_e = \mathrm{Tr}[(\not{p}_1 + m_e)\gamma^\mu(\not{p}_2 - m_e)\gamma^\nu]$ 是电子轻子张量，$L_{\mu\nu,\mu} = \mathrm{Tr}[(\not{k}_1 + m_\mu)\gamma_\mu(\not{k}_2 - m_\mu)\gamma_\nu]$ 是 $\mu$ 子轻子张量。

**Step 3 — Trace technology.** In the ultra-relativistic limit $m_e, m_\mu \to 0$ (valid when $\sqrt{s} \gg \max(m_e, m_\mu)$):

**第 3 步 — 迹技术。** 在超相对论极限 $m_e, m_\mu \to 0$（当 $\sqrt{s} \gg \max(m_e, m_\mu)$ 时成立）：

$$ L^{\mu\nu}_e \to \mathrm{Tr}[\not{p}_1\gamma^\mu\not{p}_2\gamma^\nu] = 4(p_1^\mu p_2^\nu + p_1^\nu p_2^\mu - g^{\mu\nu}(p_1\cdot p_2)). $$

Using standard trace identities: $\mathrm{Tr}[\gamma^\alpha\gamma^\beta\gamma^\gamma\gamma^\delta] = 4(g^{\alpha\beta}g^{\gamma\delta} - g^{\alpha\gamma}g^{\beta\delta} + g^{\alpha\delta}g^{\beta\gamma})$.

利用标准迹恒等式：$\mathrm{Tr}[\gamma^\alpha\gamma^\beta\gamma^\gamma\gamma^\delta] = 4(g^{\alpha\beta}g^{\gamma\delta} - g^{\alpha\gamma}g^{\beta\delta} + g^{\alpha\delta}g^{\beta\gamma})$。

**Step 4 — Contract the tensors.** The contraction $L^{\mu\nu}_e \cdot L_{\mu\nu,\mu}$ (in massless limit):

**第 4 步 — 张量缩并。** 缩并 $L^{\mu\nu}_e \cdot L_{\mu\nu,\mu}$（无质量极限）：

$$ \begin{aligned} L^{\mu\nu}_e L_{\mu\nu,\mu} &= 4(p_1^\mu p_2^\nu + p_1^\nu p_2^\mu - g^{\mu\nu}p_1\cdot p_2)\cdot 4(k_{1\mu}k_{2\nu} + k_{1\nu}k_{2\mu} - g_{\mu\nu}k_1\cdot k_2) \\ &= 32[(p_1\cdot k_1)(p_2\cdot k_2) + (p_1\cdot k_2)(p_2\cdot k_1)]. \end{aligned} $$

This is the key kinematic identity (the "crossing" structure reflects $t$ and $u$ channel kinematics).

这是关键的运动学恒等式（"crossing"结构反映了 $t$ 道和 $u$ 道运动学）。

**Step 5 — Kinematics.** In the CM frame, with $\sqrt{s} = 2E$:

**第 5 步 — 运动学。** 在质心系中，$\sqrt{s} = 2E$：

$$ \begin{aligned} p_1 &= (E, 0, 0, E), \quad p_2 = (E, 0, 0, -E), \\ k_1 &= (E, E\sin\theta, 0, E\cos\theta), \quad k_2 = (E, -E\sin\theta, 0, -E\cos\theta). \end{aligned} $$

Computing the dot products:

计算内积：

$$ \begin{aligned} p_1\cdot k_1 &= E^2(1 - \cos\theta), \quad p_2\cdot k_2 = E^2(1 - \cos\theta), \\ p_1\cdot k_2 &= E^2(1 + \cos\theta), \quad p_2\cdot k_1 = E^2(1 + \cos\theta). \end{aligned} $$

Therefore:

因此：

$$ L^{\mu\nu}_e L_{\mu\nu,\mu} = 32[E^4(1-\cos\theta)^2 + E^4(1+\cos\theta)^2] = 32E^4\cdot 2(1 + \cos^2\theta) = 64E^4(1 + \cos^2\theta). $$

And $s = (2E)^2 = 4E^2$, so $E^4 = s^2/16$.

而 $s = (2E)^2 = 4E^2$，故 $E^4 = s^2/16$。

**Step 6 — Compute $|M|^2$.** Combining:

**第 6 步 — 计算 $|M|^2$。** 综合：

$$ \begin{aligned} \langle|M|^2\rangle &= (e^4/(4s^2)) \cdot 64E^4(1 + \cos^2\theta) = (e^4/(4s^2)) \cdot 64(s^2/16)(1 + \cos^2\theta) \\ &= e^4(1 + \cos^2\theta) = 16\pi^2\alpha^2(1 + \cos^2\theta). \end{aligned} $$

using $e^2 = 4\pi\alpha$.

利用 $e^2 = 4\pi\alpha$。

**Step 7 — Differential cross-section.** The general formula for $2\to2$ scattering in the CM frame (massless final states) is:

**第 7 步 — 微分散射截面。** 质心系中 $2\to2$ 散射（无质量末态）的一般公式为：

$$ d\sigma/d\Omega = \langle|M|^2\rangle/(64\pi^2 s). $$

Therefore:

因此：

$$ d\sigma/d\Omega = 16\pi^2\alpha^2(1 + \cos^2\theta)/(64\pi^2 s) = \boxed{\, \alpha^2(1 + \cos^2\theta)/(4s) \,}. $$

**Step 8 — Total cross-section.** Integrate over the full solid angle:

**第 8 步 — 总截面。** 对全立体角积分：

$$ \begin{aligned} \sigma &= \int d\Omega\, \alpha^2(1 + \cos^2\theta)/(4s) = (\alpha^2/4s)\int_0^{2\pi}d\varphi\int_{-1}^{+1}(1 + \cos^2\theta)\,d(\cos\theta) \\ &= (\alpha^2/4s)\cdot 2\pi\cdot[\cos\theta + \cos^3\theta/3]_{-1}^{+1} = (\alpha^2/4s)\cdot 2\pi\cdot(2 + 2/3) \\ &= (\alpha^2/4s)\cdot 2\pi\cdot 8/3 = \boxed{\, 4\pi\alpha^2/(3s) \,}. \end{aligned} $$

$$ \blacksquare $$

---

## D. One-Loop Running of $\alpha$ · $\alpha$ 的单圈跑动

**Claim.** The one-loop QED renormalization group equation is $d\alpha/d(\ln\mu) = \alpha^2/(3\pi)$ with solution $1/\alpha(\mu) = 1/\alpha(\mu_0) - (1/3\pi)\ln(\mu/\mu_0)$, giving $\alpha(m_Z) \approx 1/128$ from $\alpha(m_e) \approx 1/137$.

**命题。** 单圈 QED 重整化群方程为 $d\alpha/d(\ln\mu) = \alpha^2/(3\pi)$，解为 $1/\alpha(\mu) = 1/\alpha(\mu_0) - (1/3\pi)\ln(\mu/\mu_0)$，从 $\alpha(m_e) \approx 1/137$ 给出 $\alpha(m_Z) \approx 1/128$。

**Step 1 — Vacuum polarization.** The photon propagator receives a one-loop correction from a fermion loop (a virtual $e^+e^-$ pair). In dimensional regularization ($d = 4-2\varepsilon$), this loop gives a correction to the photon self-energy $\Pi(q^2)$:

**第 1 步 — 真空极化。** 光子传播子从费米子圈（虚 $e^+e^-$ 对）接收单圈修正。在维数正规化（$d = 4-2\varepsilon$）中，该圈给出对光子自能 $\Pi(q^2)$ 的修正：

$$ \Pi(q^2) = -(e^2/2\pi^2)\int_0^1 dx\, x(1-x)\ln[m^2-x(1-x)q^2]/m^2 + (\text{pole in } \varepsilon). $$

The pole $1/\varepsilon$ is absorbed into the renormalization of the electric charge. The physical, renormalized result after subtraction at $\mu$:

极点 $1/\varepsilon$ 被吸收到电荷的重整化中。在 $\mu$ 处减除后的物理重整化结果为：

$$ \Pi_R(q^2) = (\alpha/3\pi)[\ln(q^2/\mu^2) - (\text{terms regular at } q^2 = 0)]. $$

**Step 2 — Renormalization group equation.** The requirement that physical observables are $\mu$-independent (the running coupling absorbs the log) gives the **Callan–Symanzik equation**. The one-loop $\beta$ function for QED:

**第 2 步 — 重整化群方程。** 物理可观测量不依赖于 $\mu$（跑动耦合吸收对数）的要求给出 **Callan–Symanzik 方程**。QED 的单圈 $\beta$ 函数：

$$ \beta(e) = \mu\, de/d\mu = e^3/(12\pi^2) \implies \beta(\alpha) = d\alpha/d(\ln\mu) = \alpha^2/(3\pi). $$

The coefficient $+1/(3\pi)$ is positive ($\beta > 0$), meaning $\alpha$ **increases** with $\mu$: the photon cloud of virtual pairs screens the bare charge, and one needs more energy (shorter distance) to penetrate the screening.

系数 $+1/(3\pi)$ 为正（$\beta > 0$），意味着 $\alpha$ 随 $\mu$ **增大**：虚对组成的光子云屏蔽了裸电荷，需要更高能量（更短距离）来穿透屏蔽。

**Step 3 — Solve the RGE.** Separate variables:

**第 3 步 — 求解重整化群方程。** 分离变量：

$$ \begin{aligned} d\alpha/\alpha^2 &= d(\ln\mu)/(3\pi) \implies -1/\alpha\big|^{\alpha(\mu)}_{\alpha(\mu_0)} = \ln(\mu/\mu_0)/(3\pi). \\ 1/\alpha(\mu) &= 1/\alpha(\mu_0) - (1/3\pi)\ln(\mu/\mu_0). \end{aligned} $$

**Step 4 — Numerical check.** Set $\mu_0 = m_e \approx 0.511$ MeV, $\alpha(m_e) \approx 1/137.036$, $\mu = m_Z \approx 91.2$ GeV:

**第 4 步 — 数值验证。** 令 $\mu_0 = m_e \approx 0.511$ MeV，$\alpha(m_e) \approx 1/137.036$，$\mu = m_Z \approx 91.2$ GeV：

$$ \begin{aligned} \ln(m_Z/m_e) &= \ln(91.2 \times 10^3/0.511) = \ln(1.784 \times 10^5) \approx 12.09. \\ \Delta(1/\alpha) &= -(1/3\pi)\cdot 12.09 \approx -1.28. \\ 1/\alpha(m_Z) &\approx 137.036 - 1.28 \approx 135.7. \end{aligned} $$

(The observed value $1/\alpha(m_Z) \approx 127.9$ differs because all charged particles — not just the electron — contribute loops; the quarks and heavier leptons add additional contributions of order $\ln(m_Z/m_f)$ for each flavor $f$. Including all SM fermions gives the full $\Delta(1/\alpha) \approx 9$, consistent with the observation.) $\blacksquare$

（观测值 $1/\alpha(m_Z) \approx 127.9$ 不同是因为所有带电粒子——不仅是电子——都贡献了圈图；夸克和较重的轻子为每种 $f$ 额外贡献约 $\ln(m_Z/m_f)$ 的量级。包含所有 SM 费米子后给出完整的 $\Delta(1/\alpha) \approx 9$，与观测一致。）$\blacksquare$

---

## E. Ward Identity and Gauge Invariance of Amplitudes · 沃德恒等式与振幅的规范不变性

**Claim.** In QED, any S-matrix amplitude $M^\mu$ satisfies $q_\mu M^\mu = 0$ when $q$ is the momentum of an external photon (with polarization vector $\varepsilon^\mu$). This ensures that longitudinal photons ($\varepsilon^\mu \propto q^\mu$) do not contribute to physical amplitudes.

**命题。** 在 QED 中，对于任何 S 矩阵振幅 $M^\mu$，当 $q$ 是外光子（极化矢量为 $\varepsilon^\mu$）的动量时，满足 $q_\mu M^\mu = 0$。这确保了纵向光子（$\varepsilon^\mu \propto q^\mu$）不对物理振幅作贡献。

**Step 1 — Derivation from U(1) invariance.** The Ward identity $q_\mu M^\mu = 0$ is the momentum-space statement of current conservation $\partial_\mu j^\mu = 0$. It follows from the gauge invariance of the Lagrangian: replacing the photon polarization $\varepsilon^\mu(q) \to \varepsilon^\mu(q) + q^\mu\lambda$ (a gauge transformation) must leave S-matrix elements invariant, so $M^\mu q_\mu\lambda = 0$ for all $\lambda$, giving $q_\mu M^\mu = 0$.

**第 1 步 — 从 U(1) 不变性推导。** 沃德恒等式 $q_\mu M^\mu = 0$ 是流守恒 $\partial_\mu j^\mu = 0$ 在动量空间的表述。它来自拉格朗日量的规范不变性：将光子极化 $\varepsilon^\mu(q) \to \varepsilon^\mu(q) + q^\mu\lambda$（规范变换）必须使 S 矩阵元不变，故对所有 $\lambda$ 有 $M^\mu q_\mu\lambda = 0$，即 $q_\mu M^\mu = 0$。

**Step 2 — Consequence for the photon propagator.** The Ward identity implies that the photon propagator's longitudinal component $\propto q^\mu q^\nu/q^2$ does not contribute to physical matrix elements — justifying our use of the simplified Feynman-gauge propagator $-ig^{\mu\nu}/q^2$ in gauge-invariant calculations. $\blacksquare$

**第 2 步 — 对光子传播子的推论。** 沃德恒等式意味着光子传播子的纵向分量 $\propto q^\mu q^\nu/q^2$ 不对物理矩阵元作贡献——这证明了在规范不变计算中使用简化费曼规范传播子 $-ig^{\mu\nu}/q^2$ 的合理性。$\blacksquare$

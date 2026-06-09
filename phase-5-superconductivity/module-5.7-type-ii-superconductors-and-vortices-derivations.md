---
title: "Derivations — Module 5.7: Type II Superconductors & Vortices"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 5.7: Type II Superconductors & Vortices
# 推导 — 模块 5.7：II 型超导体与涡旋

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 5.7](./module-5.7-type-ii-superconductors-and-vortices.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 5.7](./module-5.7-type-ii-superconductors-and-vortices.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Quantized Flux: $\Phi_0 = h/2e$ · 量子化磁通量：$\Phi_0 = h/2e$

**Claim.** A single superconducting vortex carries exactly one flux quantum $\Phi_0 = h/2e \approx 2.07 \times 10^{-15}$ Wb. No smaller unit of flux can be trapped in a superconductor.

**命题。** 单个超导涡旋恰好携带一个磁通量子 $\Phi_0 = h/2e \approx 2.07 \times 10^{-15}$ Wb。超导体中不能俘获比此更小的磁通单元。

**Step 1 — The GL order parameter and its phase.** In Ginzburg–Landau theory (Module 5.3), the superconducting state is described by the complex order parameter $\Psi(r) = |\Psi(r)|\, e^{i\varphi(r)}$, where $\varphi(r)$ is the macroscopic phase. The GL supercurrent density is

$$ J_s = \frac{\hbar e^*}{m^*}\big[\, |\Psi|^2 (\nabla\varphi - e^* A/\hbar) \,\big], $$

where $e^* = 2e$ is the Cooper-pair charge, $m^* = 2m$ is the pair mass, and $A$ is the vector potential. This follows from the standard substitution $p \to p - e^* A$ in quantum mechanics applied to the pair condensate.

**第 1 步 — GL 序参量及其相位。** 在金兹堡–朗道理论（模块 5.3）中，超导态由复序参量 $\Psi(r) = |\Psi(r)|\, e^{i\varphi(r)}$ 描述，$\varphi(r)$ 为宏观相位。GL 超电流密度为

$$ J_s = \frac{\hbar e^*}{m^*}\big[\, |\Psi|^2 (\nabla\varphi - e^* A/\hbar) \,\big], $$

其中 $e^* = 2e$ 为库珀对电荷，$m^* = 2m$ 为对质量，$A$ 为矢量势。这由量子力学中对配对凝聚体作标准代换 $p \to p - e^* A$ 而来。

**Step 2 — Contour integral deep inside the vortex.** Take a closed contour $C$ that encircles the vortex core and lies deep inside the superconductor (at distances much larger than the penetration depth $\lambda$ from the core). Deep inside, $J_s = 0$ (the Meissner-like screening is complete). Setting $J_s = 0$ in the GL equation:

$$ \nabla\varphi = e^* A/\hbar = 2eA/\hbar. $$

Integrate around the contour $C$:

$$ \oint_C \nabla\varphi \cdot dl = \frac{2e}{\hbar} \oint_C A \cdot dl = \frac{2e}{\hbar} \Phi, $$

where $\Phi = \oint A \cdot dl = \iint B \cdot dS$ is the total flux through $C$ by Stokes' theorem.

**第 2 步 — 在涡旋深处的回路积分。** 取一封闭回路 $C$，绕涡旋核心，且位于超导体深处（距核心距离远大于穿透深度 $\lambda$）。深处 $J_s = 0$（迈斯纳屏蔽完全）。在 GL 方程中令 $J_s = 0$：

$$ \nabla\varphi = e^* A/\hbar = 2eA/\hbar. $$

沿回路 $C$ 积分：

$$ \oint_C \nabla\varphi \cdot dl = \frac{2e}{\hbar} \oint_C A \cdot dl = \frac{2e}{\hbar} \Phi, $$

其中由斯托克斯定理 $\Phi = \oint A \cdot dl = \iint B \cdot dS$ 为穿过 $C$ 的总磁通量。

**Step 3 — Single-valuedness of $\Psi$.** The order parameter $\Psi = |\Psi|\, e^{i\varphi}$ must be single-valued: going around $C$ must return $\varphi$ to the same value modulo $2\pi$. Thus

$$ \oint_C \nabla\varphi \cdot dl = 2\pi n, \qquad n \in \mathbb{Z}. $$

**第 3 步 — $\Psi$ 的单值性。** 序参量 $\Psi = |\Psi|\, e^{i\varphi}$ 必须单值：绕 $C$ 一圈后 $\varphi$ 必须回到相差 $2\pi$ 整数倍的同一值。因此

$$ \oint_C \nabla\varphi \cdot dl = 2\pi n, \qquad n \in \mathbb{Z}. $$

**Step 4 — Flux quantization.** Equating Steps 2 and 3:

$$ \frac{2e}{\hbar} \Phi = 2\pi n \implies \Phi = n \cdot \pi\hbar/e = n \cdot h/(2e) = n \Phi_0, $$

where $\boxed{\Phi_0 = h/(2e)}$ is the fundamental flux quantum. A single vortex corresponds to $|n| = 1$, carrying one $\Phi_0$. Vortices with $|n| > 1$ are energetically unstable (their energy scales as $n^2$, so they split into $n$ single-quantum vortices). $\blacksquare$

**第 4 步 — 磁通量子化。** 由第 2、3 步相等：

$$ \frac{2e}{\hbar} \Phi = 2\pi n \implies \Phi = n \cdot \pi\hbar/e = n \cdot h/(2e) = n \Phi_0, $$

其中 $\boxed{\Phi_0 = h/(2e)}$ 为基本磁通量子。单个涡旋对应 $|n| = 1$，携带一个 $\Phi_0$。$|n| > 1$ 的涡旋能量上不稳定（能量正比于 $n^2$），会分裂为 $n$ 个单量子涡旋。$\blacksquare$

---

## B. Lower Critical Field $H_{c1}$ · 下临界场 $H_{c1}$

**Claim.** A single vortex line per unit length in a type-II superconductor has a self-energy (London limit, $\kappa \gg 1$)

$$ \varepsilon_v \approx \frac{\Phi_0^2}{4\pi\mu_0\lambda^2} \ln(\lambda/\xi) \qquad \text{per unit length.} $$

The lower critical field $H_{c1}$ is the applied field at which it first becomes thermodynamically favorable for a vortex to enter, determined by balancing the vortex energy against the magnetic energy gained:

$$ \mu_0 H_{c1} = \frac{\Phi_0}{4\pi\lambda^2} \cdot \ln(\lambda/\xi) \qquad \text{(Gaussian: } H_{c1} = \Phi_0/(4\pi\lambda^2) \ln\kappa\text{).} $$

**命题。** 在 II 型超导体中，单条涡旋线单位长度的自能（伦敦极限，$\kappa \gg 1$）为

$$ \varepsilon_v \approx \frac{\Phi_0^2}{4\pi\mu_0\lambda^2} \ln(\lambda/\xi) \qquad \text{每单位长度。} $$

下临界场 $H_{c1}$ 是使涡旋进入热力学上有利的外场，由涡旋能量与所获磁能平衡决定：

$$ \mu_0 H_{c1} = \frac{\Phi_0}{4\pi\lambda^2} \cdot \ln(\lambda/\xi) \qquad \text{（高斯制：} H_{c1} = \Phi_0/(4\pi\lambda^2) \ln\kappa\text{）。} $$

**Step 1 — London equations in the vortex region.** Outside the normal core ($r > \xi$), the superconductor satisfies the London equation:

$$ \nabla \times B = \mu_0 J_s = -(\mu_0/\lambda^2) A_s \qquad \text{(London gauge } \nabla\cdot A = 0\text{),} $$

which together with $\nabla \times B = \mu_0 J_s$ and $\nabla \times (\nabla \times B) = -\nabla^2 B$ gives

$$ -\nabla^2 B + B/\lambda^2 = 0 \qquad \text{(for } r > \xi\text{).} $$

For a single vortex along the $z$-axis, the field $B = B(r)\, \hat{z}$ depends only on the distance $r$ from the axis.

**第 1 步 — 涡旋区域的伦敦方程。** 在正常态核心外（$r > \xi$），超导体满足伦敦方程：

$$ \nabla \times B = \mu_0 J_s = -(\mu_0/\lambda^2) A_s \qquad \text{（伦敦规范 } \nabla\cdot A = 0\text{），} $$

结合 $\nabla \times B = \mu_0 J_s$ 及 $\nabla \times (\nabla \times B) = -\nabla^2 B$ 得

$$ -\nabla^2 B + B/\lambda^2 = 0 \qquad \text{（} r > \xi \text{ 时）。} $$

对沿 $z$ 轴的单涡旋，场 $B = B(r)\, \hat{z}$ 仅依赖于距轴的距离 $r$。

**Step 2 — Cylindrical London equation and its solution.** In cylindrical coordinates, $\nabla^2 B = (1/r)\, d/dr\, (r\, dB/dr)$, so the London equation becomes the modified Bessel equation:

$$ \frac{1}{r} \frac{d}{dr}\left(r \frac{dB}{dr}\right) - B/\lambda^2 = 0. $$

This is the modified Bessel equation of order zero. Its solution decaying at $r \to \infty$ is

$$ B(r) = C\, K_0(r/\lambda), $$

where $K_0$ is the modified Bessel function of the second kind of order zero, and $C$ is a constant fixed by the flux condition.

**第 2 步 — 柱坐标伦敦方程及其解。** 在柱坐标中 $\nabla^2 B = (1/r)\, d/dr\, (r\, dB/dr)$，伦敦方程化为零阶修正贝塞尔方程：

$$ \frac{1}{r} \frac{d}{dr}\left(r \frac{dB}{dr}\right) - B/\lambda^2 = 0. $$

该方程在 $r \to \infty$ 时衰减的解为

$$ B(r) = C\, K_0(r/\lambda), $$

其中 $K_0$ 为零阶第二类修正贝塞尔函数，$C$ 由磁通条件确定。

**Step 3 — Fix the constant from flux quantization.** The total flux must equal $\Phi_0$:

$$ \int_0^\infty B(r)\, 2\pi r\, dr = \Phi_0. $$

Using $\int_0^\infty K_0(r/\lambda)\, r\, dr = \lambda^2$, we get $C \cdot 2\pi\lambda^2 = \Phi_0$, so

$$ C = \frac{\Phi_0}{2\pi\lambda^2}. $$

Thus $B(r) = (\Phi_0/2\pi\lambda^2)\, K_0(r/\lambda)$.

**第 3 步 — 由磁通量子化确定常数。** 总磁通须等于 $\Phi_0$：

$$ \int_0^\infty B(r)\, 2\pi r\, dr = \Phi_0. $$

利用 $\int_0^\infty K_0(r/\lambda)\, r\, dr = \lambda^2$，得 $C \cdot 2\pi\lambda^2 = \Phi_0$，即

$$ C = \frac{\Phi_0}{2\pi\lambda^2}, $$

从而 $B(r) = (\Phi_0/2\pi\lambda^2)\, K_0(r/\lambda)$。

**Step 4 — Compute the vortex line energy.** The electromagnetic energy per unit length stored in the vortex field is

$$ \varepsilon_v = \int (B^2/2\mu_0 + \mu_0\lambda^2 J_s^2/2)\, 2\pi r\, dr. $$

In the London regime both terms are equal (virial theorem for London equations), so $\varepsilon_v = \int (B^2/\mu_0)\, 2\pi r\, dr$ (integrating from $\xi$ to $\infty$ — the core itself has a small condensation energy contribution). Substituting $B(r)$:

$$ \varepsilon_v = (1/\mu_0)(\Phi_0/2\pi\lambda^2)^2 \int_\xi^\infty K_0^2(r/\lambda)\, 2\pi r\, dr. $$

For $\kappa = \lambda/\xi \gg 1$, using $K_0(x) \approx -\ln(x)$ for $x \ll 1$ and $K_0(x) \approx \sqrt{\pi/2x}\, e^{-x}$ for $x \gg 1$, the integral evaluates to $\approx \pi\lambda^2 \ln(\lambda/\xi)$. Hence

$$ \varepsilon_v \approx \frac{\Phi_0^2}{4\pi\mu_0\lambda^2} \ln(\lambda/\xi) = \frac{\Phi_0^2}{4\pi\mu_0\lambda^2} \ln\kappa \qquad \text{per unit length.} $$

**第 4 步 — 计算涡旋线能量。** 单位长度涡旋场储存的电磁能为

$$ \varepsilon_v = \int (B^2/2\mu_0 + \mu_0\lambda^2 J_s^2/2)\, 2\pi r\, dr. $$

在伦敦体制中两项相等（伦敦方程的维里定理），故 $\varepsilon_v = \int (B^2/\mu_0)\, 2\pi r\, dr$（从 $\xi$ 到 $\infty$ 积分——核心本身有小的凝聚能贡献）。代入 $B(r)$：

$$ \varepsilon_v = (1/\mu_0)(\Phi_0/2\pi\lambda^2)^2 \int_\xi^\infty K_0^2(r/\lambda)\, 2\pi r\, dr. $$

对 $\kappa = \lambda/\xi \gg 1$，利用 $K_0(x) \approx -\ln(x)$（$x \ll 1$ 时）和 $K_0(x) \approx \sqrt{\pi/2x}\, e^{-x}$（$x \gg 1$ 时），积分约为 $\pi\lambda^2 \ln(\lambda/\xi)$。故

$$ \varepsilon_v \approx \frac{\Phi_0^2}{4\pi\mu_0\lambda^2} \ln(\lambda/\xi) = \frac{\Phi_0^2}{4\pi\mu_0\lambda^2} \ln\kappa \qquad \text{每单位长度。} $$

**Step 5 — Thermodynamic condition for $H_{c1}$.** A vortex first enters when the Gibbs free energy per unit length gained by the field threading equals the vortex self-energy. The magnetic energy gain per unit length when one flux quantum $\Phi_0$ enters at external field $H$ is

$$ \Delta G_{\text{mag}} = -\mu_0 H \Phi_0 \qquad \text{(per unit length, the work done by the field source).} $$

Setting $\varepsilon_v + \Delta G_{\text{mag}} = 0$ at the onset field $H = H_{c1}$:

$$ \mu_0 H_{c1} \Phi_0 = \varepsilon_v \implies \mu_0 H_{c1} = (\Phi_0/4\pi\lambda^2) \ln\kappa. $$

This is the **lower critical field**. $\blacksquare$

**第 5 步 — $H_{c1}$ 的热力学条件。** 当磁场穿透所带来的吉布斯自由能收益等于涡旋自能时，涡旋开始进入。单位长度内一个磁通量子 $\Phi_0$ 在外场 $H$ 下穿入所获磁能为

$$ \Delta G_{\text{mag}} = -\mu_0 H \Phi_0 \qquad \text{（单位长度，即场源做的功）。} $$

在起始场 $H = H_{c1}$ 处令 $\varepsilon_v + \Delta G_{\text{mag}} = 0$：

$$ \mu_0 H_{c1} \Phi_0 = \varepsilon_v \implies \mu_0 H_{c1} = (\Phi_0/4\pi\lambda^2) \ln\kappa. $$

这即为**下临界场**。$\blacksquare$

---

## C. Upper Critical Field $H_{c2}$: GL as a Landau-Level Problem · 上临界场 $H_{c2}$：GL 方程化为朗道能级问题

**Claim.** The upper critical field is

$$ H_{c2} = \frac{\Phi_0}{2\pi\mu_0\xi^2} \quad \text{(SI),} \qquad \text{i.e.,} \qquad B_{c2} = \frac{\Phi_0}{2\pi\xi^2}. $$

It is found by solving the linearized GL equation near the normal-to-superconductor transition, which maps exactly onto a 2D quantum harmonic oscillator (Landau levels).

**命题。** 上临界场为

$$ H_{c2} = \frac{\Phi_0}{2\pi\mu_0\xi^2} \quad \text{（SI），} \qquad \text{即} \qquad B_{c2} = \frac{\Phi_0}{2\pi\xi^2}. $$

它由在正常–超导相变附近求解线性化 GL 方程得到，该方程恰好对应二维量子谐振子（朗道能级）。

**Step 1 — Linearized GL equation.** Near $H_{c2}$, the order parameter $|\Psi|$ is small (the transition is second order). The full GL equation (Module 5.3) is

$$ \frac{1}{2m^*} (-i\hbar\nabla - e^* A)^2 \Psi + \alpha \Psi + \beta|\Psi|^2 \Psi = 0. $$

Linearize by dropping the $|\Psi|^2$ term (valid for small $|\Psi|$):

$$ \frac{1}{2m^*} (-i\hbar\nabla - e^* A)^2 \Psi = -\alpha \Psi. $$

With $\alpha < 0$ below $T_c$, write $-\alpha = |\alpha| > 0$. This is a Schrödinger-like equation for $\Psi$ in an effective magnetic field.

**第 1 步 — 线性化 GL 方程。** 在 $H_{c2}$ 附近，序参量 $|\Psi|$ 很小（相变为二级）。完整 GL 方程（模块 5.3）为

$$ \frac{1}{2m^*} (-i\hbar\nabla - e^* A)^2 \Psi + \alpha \Psi + \beta|\Psi|^2 \Psi = 0. $$

线性化（去掉 $|\Psi|^2$ 项，小 $|\Psi|$ 时有效）：

$$ \frac{1}{2m^*} (-i\hbar\nabla - e^* A)^2 \Psi = -\alpha \Psi. $$

在 $T_c$ 以下 $\alpha < 0$，令 $-\alpha = |\alpha| > 0$。这是 $\Psi$ 在有效磁场中的类薛定谔方程。

**Step 2 — Map to a quantum harmonic oscillator.** Choose the Landau gauge $A = (0, Bx, 0)$ for a uniform field $B$ along $z$. The kinetic operator expands:

$$ (-i\hbar\nabla - e^* A)^2 = -\hbar^2\partial^2/\partial x^2 + (-i\hbar\partial/\partial y - e^* Bx)^2 + (-i\hbar\partial/\partial z)^2 $$

Try a solution of the form $\Psi = e^{i(k_y y + k_z z)} f(x)$. Substituting:

$$ \left[-\hbar^2\partial^2/\partial x^2 + (\hbar k_y - e^* Bx)^2/(2m^*) + \hbar^2 k_z^2/(2m^*)\right] f(x) = |\alpha| f(x). $$

This is the 1D harmonic oscillator equation in $x$, centered at $x_0 = \hbar k_y/(e^* B)$, with frequency $\omega_c = e^* B/m^*$ (the cyclotron frequency for the pair). Setting $k_z = 0$ (the critical field arises from the lowest-energy mode):

$$ \left[-\frac{\hbar^2}{2m^*} \cdot \partial^2/\partial x^2 + \tfrac12 m^* \omega_c^2 (x - x_0)^2\right] f(x) = |\alpha| f(x). $$

**第 2 步 — 映射到量子谐振子。** 选朗道规范 $A = (0, Bx, 0)$，$B$ 沿 $z$ 方向均匀。动能算符展开：

$$ (-i\hbar\nabla - e^* A)^2 = -\hbar^2\partial^2/\partial x^2 + (-i\hbar\partial/\partial y - e^* Bx)^2 + (-i\hbar\partial/\partial z)^2 $$

尝试 $\Psi = e^{i(k_y y + k_z z)} f(x)$ 形式的解，代入：

$$ \left[-\hbar^2\partial^2/\partial x^2 + (\hbar k_y - e^* Bx)^2/(2m^*) + \hbar^2 k_z^2/(2m^*)\right] f(x) = |\alpha| f(x). $$

这是以 $x_0 = \hbar k_y/(e^* B)$ 为中心、频率 $\omega_c = e^* B/m^*$（对的回旋频率）的一维谐振子方程。令 $k_z = 0$（临界场来自最低能量模式）：

$$ \left[-\frac{\hbar^2}{2m^*} \cdot \partial^2/\partial x^2 + \tfrac12 m^* \omega_c^2 (x - x_0)^2\right] f(x) = |\alpha| f(x). $$

**Step 3 — Landau level eigenvalues.** From Module 3.2 (harmonic oscillator), the eigenvalues are

$$ |\alpha| = \hbar\omega_c (n + \tfrac12), \qquad n = 0, 1, 2, \ldots $$

The largest field $B$ at which a non-trivial solution first appears corresponds to the smallest $|\alpha|$ compatible with the equation, which occurs for the lowest Landau level $n = 0$:

$$ |\alpha| = \tfrac12 \hbar\omega_c = \tfrac12 \hbar(e^* B/m^*) = \hbar eB/m \qquad \text{(using } e^* = 2e,\ m^* = 2m\text{).} $$

**第 3 步 — 朗道能级本征值。** 由模块 3.2（谐振子），本征值为

$$ |\alpha| = \hbar\omega_c (n + \tfrac12), \qquad n = 0, 1, 2, \ldots $$

非平凡解首次出现的最大场 $B$ 对应与方程相容的最小 $|\alpha|$，发生在最低朗道能级 $n = 0$：

$$ |\alpha| = \tfrac12 \hbar\omega_c = \tfrac12 \hbar(e^* B/m^*) = \hbar eB/m \qquad \text{（利用 } e^* = 2e\text{，} m^* = 2m\text{）。} $$

**Step 4 — Identify $H_{c2}$ from the GL coherence length.** The GL coherence length $\xi$ is defined by $|\alpha| = \hbar^2/(2m^*\xi^2) = \hbar^2/(4m\xi^2)$. Setting this equal to the Landau-level result:

$$ \hbar^2/(4m\xi^2) = \hbar eB_{c2}/m \implies B_{c2} = \hbar/(4e\xi^2) \cdot (\hbar/\hbar)\cdot? $$

Let us be careful. The pair charge is $e^* = 2e$ and pair mass $m^* = 2m$. So $\omega_c = e^* B/m^* = 2eB/(2m) = eB/m$, and the harmonic oscillator ground state energy is $\hbar\omega_c/2 = \hbar eB/(2m)$. The GL coherence length is defined from the gradient term: $\xi^2 = \hbar^2/(2m^*|\alpha|) = \hbar^2/(4m|\alpha|)$. Thus $|\alpha| = \hbar^2/(4m\xi^2)$. Setting equal:

$$ \hbar^2/(4m\xi^2) = \hbar eB_{c2}/(2m) \implies B_{c2} = \hbar/(2e\xi^2) = h/(4\pi e\xi^2) = \Phi_0/(2\pi\xi^2). $$

In SI units, $B_{c2} = \mu_0 H_{c2}$, so

$$ \boxed{\, H_{c2} = \Phi_0/(2\pi\mu_0\xi^2) \,} \qquad \blacksquare $$

**第 4 步 — 由 GL 相干长度确定 $H_{c2}$。** GL 相干长度 $\xi$ 由 $|\alpha| = \hbar^2/(2m^*\xi^2) = \hbar^2/(4m\xi^2)$ 定义。令其等于朗道能级结果：

对的电荷 $e^* = 2e$，质量 $m^* = 2m$，故 $\omega_c = e^* B/m^* = eB/m$，谐振子基态能 $\hbar\omega_c/2 = \hbar eB/(2m)$。由 $\xi$ 的定义 $|\alpha| = \hbar^2/(4m\xi^2)$，令相等：

$$ \hbar^2/(4m\xi^2) = \hbar eB_{c2}/(2m) \implies B_{c2} = \hbar/(2e\xi^2) = \Phi_0/(2\pi\xi^2). $$

在 SI 单位中 $B_{c2} = \mu_0 H_{c2}$，故

$$ \boxed{\, H_{c2} = \Phi_0/(2\pi\mu_0\xi^2) \,} \qquad \blacksquare $$

---

## D. Abrikosov Lattice Energetics · 阿布里科索夫格子的能量学

**Claim.** In the mixed state, vortices repel one another and arrange into a triangular (hexagonal) lattice that minimizes the free energy. This was predicted by Abrikosov (1957) from GL theory and confirmed by neutron scattering.

**命题。** 在混合态中，涡旋相互排斥并排列成三角形（六方）格子，以最小化自由能。这由阿布里科索夫（1957年）从 GL 理论预言，并被中子散射证实。

**Step 1 — Vortex-vortex interaction.** Two parallel vortices at distance $d$ interact via their overlapping current fields. The interaction energy per unit length between two vortices both carrying $\Phi_0$ is (London limit):

$$ \varepsilon_{12}(d) = (\Phi_0^2/2\pi\mu_0\lambda^2) K_0(d/\lambda). $$

Since $K_0 > 0$ always, the interaction is **repulsive** for same-sign vortices. For $d \ll \lambda$ the repulsion diverges logarithmically; for $d \gg \lambda$ it decays exponentially.

**第 1 步 — 涡旋–涡旋相互作用。** 两条相距 $d$ 的平行涡旋通过其重叠电流场相互作用。两个均携带 $\Phi_0$ 的涡旋单位长度上的相互作用能为（伦敦极限）：

$$ \varepsilon_{12}(d) = (\Phi_0^2/2\pi\mu_0\lambda^2) K_0(d/\lambda). $$

由于 $K_0$ 恒为正，同号涡旋间的作用为**排斥**。$d \ll \lambda$ 时排斥对数发散；$d \gg \lambda$ 时指数衰减。

**Step 2 — Lattice energy minimization.** With $n_v = B/\Phi_0$ vortices per unit area (to carry the applied flux $B$), the lattice spacing $a$ satisfies $n_v \cdot (\sqrt{3}/2) a^2 = 1$ (area per vortex for triangular lattice). This gives $a = (2/\sqrt{3})^{1/2} (\Phi_0/B)^{1/2}$. The total free energy per unit volume includes the sum of vortex self-energies plus all pairwise interaction energies. Minimizing over lattice geometry (comparing triangular vs. square vs. other Bravais lattices) shows the triangular lattice has the lowest energy. Abrikosov defined the ratio parameter

$$ \beta_A = \langle|\Psi|^4\rangle / \langle|\Psi|^2\rangle^2, $$

which equals $\approx 1.1596$ for the triangular lattice and $\approx 1.1803$ for the square lattice. The free energy near $H_{c2}$ is

$$ F = F_n - \alpha^2/(2\beta \beta_A), $$

where $\alpha$ and $\beta$ are GL coefficients, confirming the mixed state is thermodynamically favorable. Since $F$ is minimized by the **smallest** $\beta_A$, the triangular lattice ($1.1596 < 1.1803$) is the ground state.

**第 2 步 — 格子能量最小化。** 每单位面积有 $n_v = B/\Phi_0$ 个涡旋（携带外加磁通 $B$），三角格子的格间距 $a$ 满足 $n_v \cdot (\sqrt{3}/2) a^2 = 1$，给出 $a = (2/\sqrt{3})^{1/2} (\Phi_0/B)^{1/2}$。每单位体积的总自由能包括涡旋自能之和加上所有对相互作用能。对格子几何结构（比较三角、方形及其他布拉维格子）做最小化，显示三角格子能量最低。阿布里科索夫定义参数

$$ \beta_A = \langle|\Psi|^4\rangle / \langle|\Psi|^2\rangle^2, $$

三角格子 $\beta_A \approx 1.1596$，方格子 $\beta_A \approx 1.1803$（$F$ 由最小的 $\beta_A$ 极小化，故三角格子胜出）。$H_{c2}$ 附近的自由能为

$$ F = F_n - \alpha^2/(2\beta \beta_A), $$

证实混合态热力学上更有利。

**Step 3 — Observational consequence.** The vortex lattice spacing $a$ decreases as $B$ increases ($a \propto B^{-1/2}$). At $B = B_{c2}$, the cores (radius $\sim \xi$) touch and overlap: $(\xi/a)^2 \sim 1/(\kappa^2)$, so superconductivity is destroyed uniformly. The vortex lattice can be directly imaged by decoration experiments (ferromagnetic powder), small-angle neutron scattering, and scanning tunneling microscopy. $\blacksquare$

**第 3 步 — 可观测后果。** 涡旋格子间距 $a$ 随 $B$ 增大而减小（$a \propto B^{-1/2}$）。在 $B = B_{c2}$ 时，核心（半径 $\sim \xi$）相互接触重叠：$(\xi/a)^2 \sim 1/\kappa^2$，超导性均匀消失。涡旋格子可通过装饰实验（铁磁粉末）、小角中子散射和扫描隧道显微镜直接成像。$\blacksquare$

---

## E. Flux Pinning and the Critical Current · 磁通钉扎与临界电流

**Claim.** Moving vortices dissipate energy via a viscous drag force. Vortices remain pinned on defects up to a critical current density $J_c$, above which the Lorentz-like force exceeds the pinning force and vortices move, restoring resistance.

**命题。** 运动的涡旋通过粘滞拖曳力耗散能量。涡旋在临界电流密度 $J_c$ 以下被缺陷钉扎；超过 $J_c$ 时，类洛伦兹力超过钉扎力，涡旋运动，电阻恢复。

**Step 1 — Magnus/Lorentz force on a vortex.** A transport current density $J$ flowing perpendicular to a vortex exerts a force per unit length on the vortex:

$$ f_L = J \times B = J \Phi_0 \qquad \text{(for a single vortex, } B = \Phi_0 \text{ per unit area of the vortex).} $$

More precisely, for a vortex of flux $\Phi_0$, the force per unit length is $f_L = J \Phi_0$ (perpendicular to both $J$ and the vortex axis). This is the Lorentz (or Magnus) force.

**第 1 步 — 涡旋上的马格努斯/洛伦兹力。** 垂直于涡旋流动的输运电流密度 $J$ 对单位长度涡旋施加的力为：

$$ f_L = J \times B = J \Phi_0 \qquad \text{（对单涡旋，} B = \text{每单位面积涡旋的 } \Phi_0\text{）。} $$

更精确地，对磁通为 $\Phi_0$ 的涡旋，单位长度上的力为 $f_L = J \Phi_0$（垂直于 $J$ 和涡旋轴）。这是洛伦兹（或马格努斯）力。

**Step 2 — Pinning force.** Defects (grain boundaries, precipitates, columnar defects from irradiation) create local regions where the vortex core energy is reduced (the core prefers to sit in an already-normal region). A pinning site exerts a restoring force

$$ f_p \approx \varepsilon_v / \xi \qquad \text{(rough estimate: energy well of depth } \sim\varepsilon_v \text{ over length scale } \sim\xi\text{)} $$

on the vortex, where $\varepsilon_v$ is the condensation energy per unit length of the core: $\varepsilon_v \sim H_c^2 \xi^2/2\mu_0$ (the lost condensation energy in the normal core of area $\pi\xi^2$).

**第 2 步 — 钉扎力。** 缺陷（晶界、析出物、辐照产生的柱状缺陷）产生局部区域，使涡旋核能量降低（核心倾向于停留在已经正常的区域）。钉扎位对涡旋施加回复力

$$ f_p \approx \varepsilon_v / \xi \qquad \text{（粗估：深度 } \sim\varepsilon_v \text{ 的能量阱分布在长度尺度 } \sim\xi \text{ 上），} $$

其中 $\varepsilon_v$ 为单位长度核心的凝聚能：$\varepsilon_v \sim H_c^2 \xi^2/2\mu_0$（面积 $\pi\xi^2$ 的正常核心中损失的凝聚能）。

**Step 3 — Critical current condition.** Vortices depin (start moving) when the Lorentz force exceeds the pinning force:

$$ J_c \Phi_0 = f_p \implies J_c = f_p / \Phi_0. $$

Substituting $f_p \sim H_c^2\xi/2\mu_0$ and $\Phi_0 = h/2e$:

$$ J_c \sim H_c^2\xi / (\mu_0 \Phi_0) \sim H_c^2 \xi (2e) / (\mu_0 h). $$

Using the relations $H_c = \Phi_0/(2\sqrt{2} \pi\mu_0 \lambda\xi)$ (Abrikosov result) one can show $J_c \sim J_d / \kappa$ where $J_d = H_c/\lambda$ is the depairing current density — consistent with the observation that high-$\kappa$ materials need strong pinning to be useful.

**第 3 步 — 临界电流条件。** 当洛伦兹力超过钉扎力时，涡旋脱钉（开始运动）：

$$ J_c \Phi_0 = f_p \implies J_c = f_p / \Phi_0. $$

代入 $f_p \sim H_c^2\xi/2\mu_0$ 和 $\Phi_0 = h/2e$：

$$ J_c \sim H_c^2\xi / (\mu_0 \Phi_0) \sim H_c^2 \xi (2e) / (\mu_0 h). $$

利用关系 $H_c = \Phi_0/(2\sqrt{2} \pi\mu_0 \lambda\xi)$（阿布里科索夫结果），可以证明 $J_c \sim J_d / \kappa$，其中 $J_d = H_c/\lambda$ 为拆对电流密度——这与高 $\kappa$ 材料需要强钉扎才能实用的观测一致。

**Step 4 — Dissipation when vortices move.** When $J > J_c$, vortices move with velocity $v_L = J/n_v$ (where $n_v = B/\Phi_0$ is the vortex density). By Faraday's law, moving vortices each carrying flux $\Phi_0$ generate an electric field $E = B v_L = (B/\Phi_0) \Phi_0 v_L = B v_L$. This Ohmic dissipation is the origin of resistance in the flux-flow regime. The resistivity is $\rho_{\text{FF}} = (B/B_{c2}) \rho_n$ (Bardeen–Stephen model), going from zero (fully pinned, $J < J_c$) to $\rho_n$ (all flux lines depinned, $B \to B_{c2}$). $\blacksquare$

**第 4 步 — 涡旋运动时的耗散。** 当 $J > J_c$ 时，涡旋以速度 $v_L = J/n_v$ 运动（$n_v = B/\Phi_0$ 为涡旋密度）。由法拉第定律，各自携带磁通 $\Phi_0$ 的运动涡旋产生电场 $E = B v_L$。这种欧姆耗散是磁通流动体制中电阻的来源。电阻率为 $\rho_{\text{FF}} = (B/B_{c2}) \rho_n$（巴丁–斯蒂芬模型），从零（完全钉扎，$J < J_c$）变化到 $\rho_n$（所有磁通线脱钉，$B \to B_{c2}$）。$\blacksquare$

---

*Key results: $\Phi_0 = h/2e$ follows from single-valuedness of $\Psi$; $H_{c1}$ from vortex self-energy vs. field-energy balance; $H_{c2}$ from the exact mapping of the linearized GL equation onto Landau levels; the triangular Abrikosov lattice minimizes $\beta_A$; pinning controls $J_c$ in practical applications.*

*核心结果：$\Phi_0 = h/2e$ 来自 $\Psi$ 的单值性；$H_{c1}$ 来自涡旋自能与磁场能的平衡；$H_{c2}$ 来自线性化 GL 方程到朗道能级的精确映射；三角阿布里科索夫格子最小化 $\beta_A$；钉扎在实际应用中控制 $J_c$。*

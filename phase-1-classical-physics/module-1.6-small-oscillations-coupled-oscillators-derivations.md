---
title: "Derivations — Module 1.6: Small Oscillations & Coupled Oscillators"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 1.6: Small Oscillations & Coupled Oscillators
# 推导 — 模块 1.6：小振动与耦合振子

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.6](./module-1.6-small-oscillations-coupled-oscillators.md). Full step-by-step proofs of every result quoted there. English first, then 中文.
> [模块 1.6](./module-1.6-small-oscillations-coupled-oscillators.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Damped Harmonic Oscillator — All Regimes · 阻尼谐振子——所有阻尼情形

**Claim.** The equation of motion $y'' + 2\gamma y' + \omega_0^2 y = 0$ (where $\gamma = b/2m$ is the damping coefficient and $\omega_0 = \sqrt{k/m}$ is the natural frequency) has qualitatively different solutions in three regimes:
- Underdamped ($\gamma < \omega_0$): $y(t) = e^{-\gamma t}[A\cos(\omega_d t) + B\sin(\omega_d t)]$, $\omega_d = \sqrt{\omega_0^2 - \gamma^2}$.
- Critically damped ($\gamma = \omega_0$): $y(t) = (A + Bt)\,e^{-\gamma t}$.
- Overdamped ($\gamma > \omega_0$): $y(t) = A\,e^{r_+ t} + B\,e^{r_- t}$, $r_\pm = -\gamma \pm \sqrt{\gamma^2 - \omega_0^2}$.

**命题。** 运动方程 $y'' + 2\gamma y' + \omega_0^2 y = 0$（$\gamma = b/2m$ 为阻尼系数，$\omega_0 = \sqrt{k/m}$ 为固有频率）在三种情形下有定性不同的解：
- 欠阻尼（$\gamma < \omega_0$）：$y(t) = e^{-\gamma t}[A\cos(\omega_d t) + B\sin(\omega_d t)]$，$\omega_d = \sqrt{\omega_0^2 - \gamma^2}$。
- 临界阻尼（$\gamma = \omega_0$）：$y(t) = (A + Bt)\,e^{-\gamma t}$。
- 过阻尼（$\gamma > \omega_0$）：$y(t) = A\,e^{r_+ t} + B\,e^{r_- t}$，$r_\pm = -\gamma \pm \sqrt{\gamma^2 - \omega_0^2}$。

**Step 1 — Characteristic equation.** Try $y = e^{rt}$. Substituting into $y'' + 2\gamma y' + \omega_0^2 y = 0$:

**第 1 步 — 特征方程。** 尝试 $y = e^{rt}$，代入 $y'' + 2\gamma y' + \omega_0^2 y = 0$：

$$ r^2 e^{rt} + 2\gamma r\,e^{rt} + \omega_0^2 e^{rt} = 0 \quad\implies\quad r^2 + 2\gamma r + \omega_0^2 = 0. $$

**Step 2 — Solve the characteristic equation by the quadratic formula.**

**第 2 步 — 用求根公式解特征方程。**

$$ r = \frac{-2\gamma \pm \sqrt{4\gamma^2 - 4\omega_0^2}}{2} = -\gamma \pm \sqrt{\gamma^2 - \omega_0^2}. $$

The nature of the roots depends on the sign of $\gamma^2 - \omega_0^2$.

根的性质取决于 $\gamma^2 - \omega_0^2$ 的符号。

**Step 3a — Underdamped case ($\gamma < \omega_0$).** Define $\omega_d = \sqrt{\omega_0^2 - \gamma^2} > 0$. The roots are complex:

**第 3a 步 — 欠阻尼情形（$\gamma < \omega_0$）。** 定义 $\omega_d = \sqrt{\omega_0^2 - \gamma^2} > 0$。根为复数：

$$ r = -\gamma \pm i\,\omega_d. $$

The general real solution is:

实数通解为：

$$ y(t) = e^{-\gamma t}[A\cos(\omega_d t) + B\sin(\omega_d t)]. $$

The oscillation frequency $\omega_d < \omega_0$ is reduced by damping; the amplitude decays as $e^{-\gamma t}$. $\blacksquare_a$

振荡频率 $\omega_d < \omega_0$ 因阻尼而降低；振幅按 $e^{-\gamma t}$ 衰减。$\blacksquare_a$

**Step 3b — Critically damped case ($\gamma = \omega_0$).** The characteristic equation has a repeated root $r = -\gamma$. For a repeated root, the two linearly independent solutions are $e^{rt}$ and $t\,e^{rt}$:

**第 3b 步 — 临界阻尼情形（$\gamma = \omega_0$）。** 特征方程有重根 $r = -\gamma$。对于重根，两个线性独立解为 $e^{rt}$ 和 $t\,e^{rt}$：

$$ y(t) = (A + Bt)\,e^{-\gamma t}. $$

(Verify: plugging into the ODE gives zero.) This case achieves the fastest return to equilibrium without oscillation. $\blacksquare_b$

（验证：代入常微分方程得零。）此情形在无振荡条件下最快回到平衡位置。$\blacksquare_b$

**Step 3c — Overdamped case ($\gamma > \omega_0$).** Define $\Gamma = \sqrt{\gamma^2 - \omega_0^2} > 0$. The roots are two distinct real negative numbers $r_\pm = -\gamma \pm \Gamma$. The general solution is:

**第 3c 步 — 过阻尼情形（$\gamma > \omega_0$）。** 定义 $\Gamma = \sqrt{\gamma^2 - \omega_0^2} > 0$。根为两个不同的负实数 $r_\pm = -\gamma \pm \Gamma$。通解为：

$$ y(t) = A\,e^{(-\gamma+\Gamma)t} + B\,e^{(-\gamma-\Gamma)t}. $$

Both exponents are negative (since $\Gamma < \gamma$), so $y \to 0$ exponentially without oscillation. The slower-decaying mode dominates at late times. $\blacksquare_c$

两个指数均为负（因为 $\Gamma < \gamma$），故 $y \to 0$ 指数衰减趋于 0，无振荡。较慢衰减模式在晚时支配。$\blacksquare_c$

---

## B. Driven Damped Oscillator — Steady-State Amplitude and Resonance · 受迫阻尼振子——稳态振幅与共振

**Claim.** For $m\ddot{y} + b\dot{y} + ky = F_0\cos(\omega t)$, the steady-state amplitude is:

$$ A(\omega) = \frac{F_0/m}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\gamma^2\omega^2}}, $$

which is maximised at $\omega_\text{res} = \sqrt{\omega_0^2 - 2\gamma^2} \approx \omega_0$ for small damping.

**命题。** 对于 $m\ddot{y} + b\dot{y} + ky = F_0\cos(\omega t)$，稳态振幅为：

$$ A(\omega) = \frac{F_0/m}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\gamma^2\omega^2}}, $$

在小阻尼时在 $\omega_\text{res} = \sqrt{\omega_0^2 - 2\gamma^2} \approx \omega_0$ 处取最大值。

**Step 1 — Use complex notation.** Write the drive as $\operatorname{Re}[F_0 e^{i\omega t}]$ and seek a steady-state solution of the form $y_p = \operatorname{Re}[C e^{i\omega t}]$:

**第 1 步 — 使用复数记法。** 将驱动力写为 $\operatorname{Re}[F_0 e^{i\omega t}]$，寻求形如 $y_p = \operatorname{Re}[C e^{i\omega t}]$ 的稳态解：

$$ \begin{aligned}
& m(i\omega)^2 C + b(i\omega) C + k C = F_0, \\
& C\big[(-\omega^2 m + k) + i\omega b\big] = F_0, \\
& C = \frac{F_0/m}{(\omega_0^2 - \omega^2) + 2i\gamma\omega}.
\end{aligned} $$

**Step 2 — Find the amplitude.** $|C|$ gives the amplitude:

**第 2 步 — 求振幅。** $|C|$ 给出振幅：

$$ A = |C| = \frac{F_0/m}{\big|(\omega_0^2 - \omega^2) + 2i\gamma\omega\big|} = \boxed{\,\frac{F_0/m}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\gamma^2\omega^2}}\,} \qquad \blacksquare_\text{amplitude} $$

**Step 3 — Find the resonant frequency.** Maximise $A(\omega)$ by minimising the denominator $f(\omega) = (\omega_0^2 - \omega^2)^2 + 4\gamma^2\omega^2$. Differentiate with respect to $\omega^2$; let $u = \omega^2$:

**第 3 步 — 求共振频率。** 最大化 $A(\omega)$ 即最小化分母 $f(\omega) = (\omega_0^2 - \omega^2)^2 + 4\gamma^2\omega^2$。对 $\omega^2$ 微分，令 $u = \omega^2$：

$$ \frac{df}{du} = -2(\omega_0^2 - u) + 4\gamma^2 = 0 \quad\implies\quad \omega_0^2 - u = 2\gamma^2 \quad\implies\quad u = \omega_0^2 - 2\gamma^2. $$

So the resonant frequency is:

故共振频率为：

$$ \boxed{\, \omega_\text{res} = \sqrt{\omega_0^2 - 2\gamma^2} \,} \qquad \blacksquare $$

For $\gamma \ll \omega_0$ (high-$Q$ oscillator), $\omega_\text{res} \approx \omega_0$, and the peak amplitude $A(\omega_\text{res}) \approx F_0/(2m\gamma\omega_0) = F_0 Q/(m\omega_0^2)$.

对于 $\gamma \ll \omega_0$（高 $Q$ 振子），$\omega_\text{res} \approx \omega_0$，峰值振幅 $A(\omega_\text{res}) \approx F_0/(2m\gamma\omega_0) = F_0 Q/(m\omega_0^2)$。

---

## C. Normal Modes of Two Equal Masses and Three Springs · 两等质量三弹簧系统的简正模式

**Setup.** Two masses $m$ are each connected to fixed walls by springs of stiffness $k$, and to each other by a spring of stiffness $\kappa$. Let $x_1$ and $x_2$ be the displacements from equilibrium.

**设置。** 两个质量 $m$ 各通过刚度 $k$ 的弹簧与固定墙相连，并通过刚度 $\kappa$ 的弹簧相互连接。设 $x_1$ 和 $x_2$ 为偏离平衡位置的位移。

**Claim.** The system has two normal-mode frequencies:
- Symmetric mode: $\omega_1^2 = k/m$ (both masses move together).
- Antisymmetric mode: $\omega_2^2 = (k + 2\kappa)/m$ (masses move in opposite directions).

**命题。** 该系统有两个简正模式频率：
- 对称模式：$\omega_1^2 = k/m$（两质量同向运动）。
- 反对称模式：$\omega_2^2 = (k + 2\kappa)/m$（质量反向运动）。

**Step 1 — Write the equations of motion.** For mass 1: the left wall spring pulls with force $-kx_1$, the coupling spring pulls with force $-\kappa(x_1 - x_2)$. Similarly for mass 2:

**第 1 步 — 写出运动方程。** 对质量 1：左壁弹簧施力 $-kx_1$，耦合弹簧施力 $-\kappa(x_1 - x_2)$。类似地对质量 2：

$$ \begin{aligned}
m\ddot{x}_1 &= -kx_1 - \kappa(x_1 - x_2) = -(k + \kappa)x_1 + \kappa x_2, \\
m\ddot{x}_2 &= -kx_2 - \kappa(x_2 - x_1) = \kappa x_1 - (k + \kappa)x_2.
\end{aligned} $$

**Step 2 — Matrix form.** Define $\mathbf{x} = (x_1, x_2)^\mathsf{T}$. The system is $m\ddot{\mathbf{x}} = -K\mathbf{x}$, where the stiffness matrix is:

**第 2 步 — 矩阵形式。** 定义 $\mathbf{x} = (x_1, x_2)^\mathsf{T}$。系统为 $m\ddot{\mathbf{x}} = -K\mathbf{x}$，刚度矩阵为：

$$ K = \begin{pmatrix} k + \kappa & -\kappa \\ -\kappa & k + \kappa \end{pmatrix}. $$

**Step 3 — Seek normal-mode solutions.** Substitute $\mathbf{x} = \mathbf{A}\,e^{i\omega t}$ to get the eigenvalue problem:

**第 3 步 — 寻求简正模式解。** 代入 $\mathbf{x} = \mathbf{A}\,e^{i\omega t}$ 得特征值问题：

$$ K\mathbf{A} = m\omega^2 \mathbf{A}, \quad\text{i.e.}\quad (K - m\omega^2 I)\mathbf{A} = 0. $$

Non-trivial solutions require $\det(K - m\omega^2 I) = 0$:

非平凡解要求 $\det(K - m\omega^2 I) = 0$：

$$ \det\begin{pmatrix} k + \kappa - m\omega^2 & -\kappa \\ -\kappa & k + \kappa - m\omega^2 \end{pmatrix} = 0 \quad\implies\quad (k + \kappa - m\omega^2)^2 - \kappa^2 = 0. $$

**Step 4 — Solve the characteristic equation.** Factoring:

**第 4 步 — 解特征方程。** 因式分解：

$$ \big[(k + \kappa - m\omega^2) - \kappa\big]\big[(k + \kappa - m\omega^2) + \kappa\big] = 0, \qquad (k - m\omega^2)(k + 2\kappa - m\omega^2) = 0. $$

This gives two eigenvalues:

得两个特征值：

$$ \begin{aligned}
m\omega_1^2 = k &\quad\implies\quad \boxed{\,\omega_1^2 = k/m\,}, \\
m\omega_2^2 = k + 2\kappa &\quad\implies\quad \boxed{\,\omega_2^2 = (k + 2\kappa)/m\,}.
\end{aligned} \qquad \blacksquare_\text{frequencies} $$

**Step 5 — Find the eigenvectors (normal mode shapes).** For $\omega_1^2 = k/m$: substitute into $(K - m\omega^2 I)\mathbf{A} = 0$:

**第 5 步 — 求特征向量（简正模式形状）。** 对 $\omega_1^2 = k/m$：代入 $(K - m\omega^2 I)\mathbf{A} = 0$：

$$ \begin{pmatrix} \kappa & -\kappa \\ -\kappa & \kappa \end{pmatrix}\begin{pmatrix} A_1 \\ A_2 \end{pmatrix} = 0 \quad\implies\quad \kappa(A_1 - A_2) = 0 \quad\implies\quad A_1 = A_2. $$

**Mode 1 (symmetric):** $\mathbf{A}_1 = (1, 1)^\mathsf{T}/\sqrt{2}$. Both masses move in the same direction by the same amount. The coupling spring is unstretched; it contributes nothing, and the effective frequency is just $k/m$.

**模式 1（对称）：** $\mathbf{A}_1 = (1, 1)^\mathsf{T}/\sqrt{2}$。两质量同向移动相同距离。耦合弹簧不伸缩，不起作用，有效频率仅为 $k/m$。

For $\omega_2^2 = (k + 2\kappa)/m$: substitute into $(K - m\omega^2 I)\mathbf{A} = 0$:

对 $\omega_2^2 = (k + 2\kappa)/m$：代入 $(K - m\omega^2 I)\mathbf{A} = 0$：

$$ \begin{pmatrix} -\kappa & -\kappa \\ -\kappa & -\kappa \end{pmatrix}\begin{pmatrix} A_1 \\ A_2 \end{pmatrix} = 0 \quad\implies\quad -\kappa(A_1 + A_2) = 0 \quad\implies\quad A_1 = -A_2. $$

**Mode 2 (antisymmetric):** $\mathbf{A}_2 = (1, -1)^\mathsf{T}/\sqrt{2}$. Masses move in opposite directions; the coupling spring is doubly compressed/stretched, adding an extra $2\kappa$ restoring force per mass. $\blacksquare$

**模式 2（反对称）：** $\mathbf{A}_2 = (1, -1)^\mathsf{T}/\sqrt{2}$。质量反向运动；耦合弹簧双重压缩/拉伸，每个质量额外增加 $2\kappa$ 恢复力。$\blacksquare$

**Step 6 — General solution.** The general motion is a superposition of the two normal modes:

**第 6 步 — 通解。** 一般运动是两个简正模式的叠加：

$$ \mathbf{x}(t) = C_1(1, 1)^\mathsf{T}\cos(\omega_1 t + \varphi_1) + C_2(1, -1)^\mathsf{T}\cos(\omega_2 t + \varphi_2). $$

The four constants $C_1, C_2, \varphi_1, \varphi_2$ are fixed by initial conditions $\mathbf{x}(0)$ and $\dot{\mathbf{x}}(0)$. When $C_1 \ne 0$ and $C_2 \ne 0$, the motion of each mass displays **beats** at frequency $(\omega_2 - \omega_1)/2$, the classic signature of energy exchange between two weakly coupled oscillators.

四个常数 $C_1$、$C_2$、$\varphi_1$、$\varphi_2$ 由初始条件 $\mathbf{x}(0)$ 和 $\dot{\mathbf{x}}(0)$ 确定。当 $C_1 \ne 0$ 且 $C_2 \ne 0$ 时，每个质量的运动以频率 $(\omega_2 - \omega_1)/2$ 显示**拍**，这是两个弱耦合振子间能量交换的经典特征。

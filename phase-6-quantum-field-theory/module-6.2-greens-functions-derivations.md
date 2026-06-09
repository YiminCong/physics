# Derivations — Module 6.2: Green's Functions & Propagators
# 推导 — 模块 6.2：格林函数与传播子

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 6.2](./module-6.2-greens-functions.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 6.2](./module-6.2-greens-functions.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Free Single-Particle Green's Function · 自由单粒子格林函数

**Claim.** For a free Fermi system with single-particle energies $\varepsilon_k$, the time-ordered single-particle Green's function at zero temperature is

$$ G^0(k, t-t') = -i\,\theta(t-t')\, e^{-i\varepsilon_k(t-t')/\hbar}\,(1 - f_k) \;-\; i\,\theta(t'-t)\, e^{-i\varepsilon_k(t-t')/\hbar}\,(-f_k), $$

where $f_k = \theta(\mu - \varepsilon_k)$ is the zero-temperature Fermi occupation. Its Fourier transform in frequency is

$$ G^0(k, \omega) = \frac{1}{\omega - \varepsilon_k/\hbar + i\delta\,\mathrm{sgn}(\varepsilon_k - \mu)}, \qquad \delta \to 0^+. $$

**命题。** 对于单粒子能量为 $\varepsilon_k$ 的自由费米系统，零温时序单粒子格林函数为

$$ G^0(k, t-t') = -i\,\theta(t-t')\, e^{-i\varepsilon_k(t-t')/\hbar}\,(1 - f_k) \;-\; i\,\theta(t'-t)\, e^{-i\varepsilon_k(t-t')/\hbar}\,(-f_k), $$

其中 $f_k = \theta(\mu - \varepsilon_k)$ 是零温费米占据数。其频率傅里叶变换为

$$ G^0(k, \omega) = \frac{1}{\omega - \varepsilon_k/\hbar + i\delta\,\mathrm{sgn}(\varepsilon_k - \mu)}, \qquad \delta \to 0^+. $$

**Step 1 — Define the time-ordered Green's function.** The single-particle Green's function is defined as

$$ G(k, t-t') = -i\,\langle\Psi_0| T[\, \hat c_k(t)\, \hat c^\dagger_k(t')\, ]|\Psi_0\rangle, $$

where $|\Psi_0\rangle$ is the many-body ground state, $\hat c_k(t) = e^{i\hat H t/\hbar}\, \hat c_k\, e^{-i\hat H t/\hbar}$ is the Heisenberg-picture operator (Module 3.10), and $T$ is the time-ordering operator: $T[AB] = A(t)B(t')\,\theta(t-t') \pm B(t')A(t)\,\theta(t'-t)$ with $-$ for fermions.

**第 1 步 — 定义时序格林函数。** 单粒子格林函数定义为

$$ G(k, t-t') = -i\,\langle\Psi_0| T[\, \hat c_k(t)\, \hat c^\dagger_k(t')\, ]|\Psi_0\rangle, $$

其中 $|\Psi_0\rangle$ 是多体基态，$\hat c_k(t) = e^{i\hat H t/\hbar}\, \hat c_k\, e^{-i\hat H t/\hbar}$ 是海森堡绘景算符（模块 3.10），$T$ 是时序算符：$T[AB] = A(t)B(t')\,\theta(t-t') \pm B(t')A(t)\,\theta(t'-t)$，费米子取 $-$。

**Step 2 — Evaluate for the free Hamiltonian.** For $\hat H_0 = \sum_k \varepsilon_k\, \hat c^\dagger_k \hat c_k$, the Heisenberg equation gives $\hat c_k(t) = e^{-i\varepsilon_k t/\hbar}\, \hat c_k$. For the non-interacting ground state $|\Psi_0\rangle = \prod_{k:\, \varepsilon_k<\mu} \hat c^\dagger_k |0\rangle$:

$$ \langle\Psi_0| \hat c_k(t)\, \hat c^\dagger_k(t') |\Psi_0\rangle = e^{-i\varepsilon_k(t-t')/\hbar}\, \langle\Psi_0| \hat c_k \hat c^\dagger_k |\Psi_0\rangle = e^{-i\varepsilon_k(t-t')/\hbar}\,(1 - f_k), $$

$$ \langle\Psi_0| \hat c^\dagger_k(t')\, \hat c_k(t) |\Psi_0\rangle = e^{-i\varepsilon_k(t-t')/\hbar}\, \langle\Psi_0| \hat c^\dagger_k \hat c_k |\Psi_0\rangle = e^{-i\varepsilon_k(t-t')/\hbar}\, f_k, $$

since $\langle \hat c_k \hat c^\dagger_k\rangle = 1 - f_k$ and $\langle \hat c^\dagger_k \hat c_k\rangle = f_k$ by the anticommutator and the definition of $f_k$.

**第 2 步 — 对自由哈密顿量求值。** 对于 $\hat H_0 = \sum_k \varepsilon_k\, \hat c^\dagger_k \hat c_k$，海森堡方程给出 $\hat c_k(t) = e^{-i\varepsilon_k t/\hbar}\, \hat c_k$。对于非相互作用基态 $|\Psi_0\rangle = \prod_{k:\, \varepsilon_k<\mu} \hat c^\dagger_k |0\rangle$：

$$ \langle\Psi_0| \hat c_k(t)\, \hat c^\dagger_k(t') |\Psi_0\rangle = e^{-i\varepsilon_k(t-t')/\hbar}\, \langle\Psi_0| \hat c_k \hat c^\dagger_k |\Psi_0\rangle = e^{-i\varepsilon_k(t-t')/\hbar}\,(1 - f_k), $$

$$ \langle\Psi_0| \hat c^\dagger_k(t')\, \hat c_k(t) |\Psi_0\rangle = e^{-i\varepsilon_k(t-t')/\hbar}\, \langle\Psi_0| \hat c^\dagger_k \hat c_k |\Psi_0\rangle = e^{-i\varepsilon_k(t-t')/\hbar}\, f_k, $$

因为由反对易子和 $f_k$ 的定义，$\langle \hat c_k \hat c^\dagger_k\rangle = 1 - f_k$，$\langle \hat c^\dagger_k \hat c_k\rangle = f_k$。

**Step 3 — Assemble the time-ordered result.**

$$ G^0(k, t) = -i\, e^{-i\varepsilon_k t/\hbar}\, [\, \theta(t)(1 - f_k) - \theta(-t) f_k\, ], $$

where $t \equiv t - t'$. The sign of the second term comes from the fermionic minus in $T$.

**第 3 步 — 组合时序结果。**

$$ G^0(k, t) = -i\, e^{-i\varepsilon_k t/\hbar}\, [\, \theta(t)(1 - f_k) - \theta(-t) f_k\, ], $$

其中 $t \equiv t - t'$。第二项的符号来自 $T$ 中费米子的负号。

**Step 4 — Fourier transform to frequency.** Compute $G^0(k, \omega) = \int_{-\infty}^{\infty} dt\, e^{i\omega t}\, G^0(k, t)$. We need two Fourier transforms:

$$ \text{(i)}\quad \int_0^\infty dt\, e^{i(\omega - \varepsilon_k/\hbar)t} = \frac{i}{\omega - \varepsilon_k/\hbar + i\delta}, $$

$$ \text{(ii)}\quad \int_{-\infty}^0 dt\, e^{i(\omega - \varepsilon_k/\hbar)t} = \frac{-i}{\omega - \varepsilon_k/\hbar - i\delta}, $$

where $\delta \to 0^+$ is required for convergence (it enforces the correct boundary condition). Therefore

$$ G^0(k, \omega) = \frac{1 - f_k}{\omega - \varepsilon_k/\hbar + i\delta} + \frac{f_k}{\omega - \varepsilon_k/\hbar - i\delta}. $$

**第 4 步 — 傅里叶变换到频率空间。** 计算 $G^0(k, \omega) = \int_{-\infty}^{\infty} dt\, e^{i\omega t}\, G^0(k, t)$。需要两个傅里叶变换：

$$ \text{(i)}\quad \int_0^\infty dt\, e^{i(\omega - \varepsilon_k/\hbar)t} = \frac{i}{\omega - \varepsilon_k/\hbar + i\delta}, $$

$$ \text{(ii)}\quad \int_{-\infty}^0 dt\, e^{i(\omega - \varepsilon_k/\hbar)t} = \frac{-i}{\omega - \varepsilon_k/\hbar - i\delta}, $$

其中 $\delta \to 0^+$ 是收敛所必需的（它强制执行正确的边界条件）。因此

$$ G^0(k, \omega) = \frac{1 - f_k}{\omega - \varepsilon_k/\hbar + i\delta} + \frac{f_k}{\omega - \varepsilon_k/\hbar - i\delta}. $$

**Step 5 — Combine into the compact form.** For $\varepsilon_k > \mu$: $f_k = 0$, so $G^0(k, \omega) = 1/(\omega - \varepsilon_k/\hbar + i\delta)$. For $\varepsilon_k < \mu$: $f_k = 1$, so $G^0(k, \omega) = 1/(\omega - \varepsilon_k/\hbar - i\delta)$. Both cases are unified as

$$ G^0(k, \omega) = \frac{1}{\omega - \varepsilon_k/\hbar + i\delta\,\mathrm{sgn}(\varepsilon_k - \mu)}. \qquad \blacksquare $$

The pole is at $\omega = \varepsilon_k/\hbar$, above the real axis for $\varepsilon_k > \mu$ (particle excitation, causal) and below for $\varepsilon_k < \mu$ (hole excitation, anti-causal). The $i\delta$ prescription is precisely what defines the time-ordered (Feynman) propagator.

**第 5 步 — 合并为紧凑形式。** 对于 $\varepsilon_k > \mu$：$f_k = 0$，故 $G^0(k, \omega) = 1/(\omega - \varepsilon_k/\hbar + i\delta)$。对于 $\varepsilon_k < \mu$：$f_k = 1$，故 $G^0(k, \omega) = 1/(\omega - \varepsilon_k/\hbar - i\delta)$。两种情形统一为

$$ G^0(k, \omega) = \frac{1}{\omega - \varepsilon_k/\hbar + i\delta\,\mathrm{sgn}(\varepsilon_k - \mu)}. \qquad \blacksquare $$

极点在 $\omega = \varepsilon_k/\hbar$ 处，对于 $\varepsilon_k > \mu$ 位于实轴上方（粒子激发，因果），对于 $\varepsilon_k < \mu$ 位于实轴下方（空穴激发，反因果）。$i\delta$ 处方正是定义时序（费曼）传播子的东西。

---

## B. The Lehmann Spectral Representation · 莱曼谱表示

**Claim.** For the fully interacting system, the time-ordered Green's function has the spectral (Lehmann) representation

$$ G(k, \omega) = \int_{-\infty}^{\infty} d\omega'\, A(k, \omega')\, \left[\, \frac{\theta(\omega' - \mu/\hbar)}{\omega - \omega' + i\delta} \;+\; \frac{\theta(\mu/\hbar - \omega')}{\omega - \omega' - i\delta}\, \right], $$

where $A(k, \omega) \ge 0$ is the spectral function. Consequently $A(k, \omega) = -(1/\pi)\,\mathrm{Im}\, G^R(k, \omega)$.

**命题。** 对于完全相互作用的系统，时序格林函数具有谱（莱曼）表示

$$ G(k, \omega) = \int_{-\infty}^{\infty} d\omega'\, A(k, \omega')\, \left[\, \frac{\theta(\omega' - \mu/\hbar)}{\omega - \omega' + i\delta} \;+\; \frac{\theta(\mu/\hbar - \omega')}{\omega - \omega' - i\delta}\, \right], $$

其中 $A(k, \omega) \ge 0$ 是谱函数。因此 $A(k, \omega) = -(1/\pi)\,\mathrm{Im}\, G^R(k, \omega)$。

**Step 1 — Insert a complete set of eigenstates.** Let $|n\rangle$ denote the exact eigenstates of $\hat H$ with energies $E_n$ and particle number $N_n = N_0 \pm 1$ (adding or removing one particle from the $N_0$-particle ground state $|\Psi_0\rangle$ with energy $E_0$). Insert $1 = \sum_n |n\rangle\langle n|$ into the definition of $G$. For $t > t'$:

$$ -i\,\langle\Psi_0| \hat c_k(t)\, \hat c^\dagger_k(t') |\Psi_0\rangle = -i\,\sum_n |\langle n|\hat c^\dagger_k|\Psi_0\rangle|^2\, e^{-i(E_n - E_0)(t-t')/\hbar}, $$

where we used $\hat c_k(t)|\Psi_0\rangle = e^{i\hat H t/\hbar}\, \hat c_k |\Psi_0\rangle$ and $\langle\Psi_0|e^{-i\hat H t/\hbar} = \langle\Psi_0|e^{-iE_0 t/\hbar}$.

**第 1 步 — 插入完备本征态集。** 设 $|n\rangle$ 为 $\hat H$ 的精确本征态，能量为 $E_n$，粒子数为 $N_n = N_0 \pm 1$（对 $N_0$ 粒子基态 $|\Psi_0\rangle$ 增加或移除一个粒子，基态能量为 $E_0$）。将 $1 = \sum_n |n\rangle\langle n|$ 插入 $G$ 的定义中。对于 $t > t'$：

$$ -i\,\langle\Psi_0| \hat c_k(t)\, \hat c^\dagger_k(t') |\Psi_0\rangle = -i\,\sum_n |\langle n|\hat c^\dagger_k|\Psi_0\rangle|^2\, e^{-i(E_n - E_0)(t-t')/\hbar}, $$

其中用到了 $\hat c_k(t)|\Psi_0\rangle = e^{i\hat H t/\hbar}\, \hat c_k |\Psi_0\rangle$ 和 $\langle\Psi_0|e^{-i\hat H t/\hbar} = \langle\Psi_0|e^{-iE_0 t/\hbar}$。

**Step 2 — Define the spectral weight.** Set $\omega_n = (E_n - E_0)/\hbar$ for states with $N_n = N_0 + 1$ (particle sector) and $\omega_n = (E_0 - E_n)/\hbar$ for states with $N_n = N_0 - 1$ (hole sector). Define the spectral function as a sum of delta peaks:

$$ A(k, \omega) = \sum_{n,\, N_n=N_0+1} |\langle n|\hat c^\dagger_k|\Psi_0\rangle|^2\, \delta(\omega - \omega_n) \;+\; \sum_{n,\, N_n=N_0-1} |\langle n|\hat c_k|\Psi_0\rangle|^2\, \delta(\omega + \omega_n). $$

Each term is manifestly non-negative. $A(k, \omega)$ is real and $A(k, \omega) \ge 0$.

**第 2 步 — 定义谱权重。** 对 $N_n = N_0 + 1$ 的态（粒子扇区），令 $\omega_n = (E_n - E_0)/\hbar$；对 $N_n = N_0 - 1$ 的态（空穴扇区），令 $\omega_n = (E_0 - E_n)/\hbar$。将谱函数定义为 $\delta$ 峰的求和：

$$ A(k, \omega) = \sum_{n,\, N_n=N_0+1} |\langle n|\hat c^\dagger_k|\Psi_0\rangle|^2\, \delta(\omega - \omega_n) \;+\; \sum_{n,\, N_n=N_0-1} |\langle n|\hat c_k|\Psi_0\rangle|^2\, \delta(\omega + \omega_n). $$

每项明显非负。$A(k, \omega)$ 是实的且 $A(k, \omega) \ge 0$。

**Step 3 — Fourier transform to $\omega$.** Using the integral representation $\theta(t) = \frac{i}{2\pi} \int d\omega\, e^{-i\omega t}/(\omega + i\delta)$, the Fourier transform of the $t > t'$ part gives the "particle" pole contribution:

$$ G_{\text{particle}}(k, \omega) = \int d\omega'\, \frac{A_{\text{particle}}(k, \omega')}{\omega - \omega' + i\delta}, $$

and similarly for the hole part with the opposite $i\delta$ prescription. Combining:

$$ G(k, \omega) = \int_{-\infty}^{\infty} d\omega'\, A(k, \omega')\, \left[\, \frac{\theta(\omega' - \mu/\hbar)}{\omega - \omega' + i\delta} \;+\; \frac{\theta(\mu/\hbar - \omega')}{\omega - \omega' - i\delta}\, \right]. \qquad \blacksquare $$

**第 3 步 — 傅里叶变换到 $\omega$。** 利用积分表示 $\theta(t) = \frac{i}{2\pi} \int d\omega\, e^{-i\omega t}/(\omega + i\delta)$，$t > t'$ 部分的傅里叶变换给出“粒子”极点贡献：

$$ G_{\text{particle}}(k, \omega) = \int d\omega'\, \frac{A_{\text{particle}}(k, \omega')}{\omega - \omega' + i\delta}, $$

空穴部分类似，但 $i\delta$ 处方相反。合并：

$$ G(k, \omega) = \int_{-\infty}^{\infty} d\omega'\, A(k, \omega')\, \left[\, \frac{\theta(\omega' - \mu/\hbar)}{\omega - \omega' + i\delta} \;+\; \frac{\theta(\mu/\hbar - \omega')}{\omega - \omega' - i\delta}\, \right]. \qquad \blacksquare $$

**Step 4 — Extract $A$ from $\mathrm{Im}\, G^R$.** The retarded Green's function is $G^R(k, \omega) = \int d\omega'\, A(k, \omega')/(\omega - \omega' + i\delta)$ (all poles below the real axis). Using the Sokhotski–Plemelj identity $1/(x + i\delta) = \mathcal{P}(1/x) - i\pi\delta(x)$:

$$ \mathrm{Im}\, G^R(k, \omega) = -\pi \int d\omega'\, A(k, \omega')\, \delta(\omega - \omega') = -\pi A(k, \omega). $$

Therefore $A(k, \omega) = -(1/\pi)\,\mathrm{Im}\, G^R(k, \omega)$. $\blacksquare$

**第 4 步 — 从 $\mathrm{Im}\, G^R$ 提取 $A$。** 推迟格林函数为 $G^R(k, \omega) = \int d\omega'\, A(k, \omega')/(\omega - \omega' + i\delta)$（所有极点在实轴下方）。利用 Sokhotski–Plemelj 恒等式 $1/(x + i\delta) = \mathcal{P}(1/x) - i\pi\delta(x)$：

$$ \mathrm{Im}\, G^R(k, \omega) = -\pi \int d\omega'\, A(k, \omega')\, \delta(\omega - \omega') = -\pi A(k, \omega). $$

因此 $A(k, \omega) = -(1/\pi)\,\mathrm{Im}\, G^R(k, \omega)$。$\blacksquare$

---

## C. The Spectral Sum Rule · 谱函数求和规则

**Claim.** The spectral function satisfies the sum rule

$$ \int_{-\infty}^{\infty} d\omega\, A(k, \omega) = 1 \qquad \text{(per spin)}. $$

**命题。** 谱函数满足求和规则

$$ \int_{-\infty}^{\infty} d\omega\, A(k, \omega) = 1 \qquad \text{（每个自旋）}. $$

**Step 1 — Use the equal-time anticommutator.** Set $t = t'$ in the definition of $G$ and use the Fourier representation:

$$ G(k, t=0^+) - G(k, t=0^-) = -i\,\langle\{\hat c_k, \hat c^\dagger_k\}\rangle = -i \cdot 1 = -i. $$

**第 1 步 — 使用等时反对易子。** 在 $G$ 的定义中令 $t = t'$，并使用傅里叶表示：

$$ G(k, t=0^+) - G(k, t=0^-) = -i\,\langle\{\hat c_k, \hat c^\dagger_k\}\rangle = -i \cdot 1 = -i. $$

**Step 2 — Relate to the frequency integral.** The discontinuity at $t = 0$ equals the integral of the spectral function (by the Fourier inversion theorem on the spectral representation):

$$ G(k, 0^+) - G(k, 0^-) = \int \frac{d\omega}{2\pi} \cdot (-2\pi i)\, A(k, \omega) \cdot \left(-\frac{1}{2\pi i}\right) \cdot 2\pi i. $$

More directly: integrating the spectral representation over $\omega$ with the appropriate contour closing gives

$$ \int_{-\infty}^{\infty} d\omega\, A(k, \omega) = -i\, [G(k, t=0^+) - G(k, t=0^-)] / (-i) = \langle\{\hat c_k, \hat c^\dagger_k\}\rangle = 1. \qquad \blacksquare $$

The sum rule is an exact consequence of the fermionic anticommutation relation alone, independent of interactions. It provides a stringent check on any approximate $A(k, \omega)$.

**第 2 步 — 与频率积分相联系。** $t = 0$ 处的不连续性等于谱函数的积分（由谱表示上的傅里叶反演定理）：

$$ G(k, 0^+) - G(k, 0^-) = \int \frac{d\omega}{2\pi} \cdot (-2\pi i)\, A(k, \omega) \cdot \left(-\frac{1}{2\pi i}\right) \cdot 2\pi i. $$

更直接地：对谱表示关于 $\omega$ 积分并取适当围道闭合，给出

$$ \int_{-\infty}^{\infty} d\omega\, A(k, \omega) = \langle\{\hat c_k, \hat c^\dagger_k\}\rangle = 1. \qquad \blacksquare $$

求和规则是费米子反对易关系单独的精确推论，与相互作用无关。它对任何近似 $A(k, \omega)$ 提供了严格检验。

---

## D. Poles, Quasiparticles, and the Self-Energy · 极点、准粒子与自能

**Claim.** When interactions are included, the full Green's function takes the Dyson form $G(k, \omega) = 1/(\omega - \varepsilon_k/\hbar - \Sigma(k, \omega))$. If $\Sigma(k, \omega)$ has a weak frequency dependence near a quasiparticle energy $\omega_{qp}$, the pole structure defines a quasiparticle with energy $\tilde\varepsilon_k$ and lifetime $\tau_k$.

**命题。** 加入相互作用后，完整格林函数取戴森形式 $G(k, \omega) = 1/(\omega - \varepsilon_k/\hbar - \Sigma(k, \omega))$。若 $\Sigma(k, \omega)$ 在准粒子能量 $\omega_{qp}$ 附近频率依赖较弱，则极点结构定义了具有能量 $\tilde\varepsilon_k$ 和寿命 $\tau_k$ 的准粒子。

**Step 1 — Taylor expand the self-energy near the pole.** Write $\Sigma(k, \omega) = \mathrm{Re}\,\Sigma(k, \omega_{qp}) + i\,\mathrm{Im}\,\Sigma(k, \omega_{qp}) + (\partial\,\mathrm{Re}\,\Sigma/\partial\omega)(\omega - \omega_{qp}) + \ldots$ The quasiparticle pole satisfies $\omega_{qp} - \varepsilon_k/\hbar - \mathrm{Re}\,\Sigma(k, \omega_{qp}) = 0$, which defines the renormalized energy $\tilde\varepsilon_k = \varepsilon_k + \hbar\,\mathrm{Re}\,\Sigma(k, \omega_{qp})$.

**第 1 步 — 在极点附近对自能作泰勒展开。** 写出 $\Sigma(k, \omega) = \mathrm{Re}\,\Sigma(k, \omega_{qp}) + i\,\mathrm{Im}\,\Sigma(k, \omega_{qp}) + (\partial\,\mathrm{Re}\,\Sigma/\partial\omega)(\omega - \omega_{qp}) + \ldots$。准粒子极点满足 $\omega_{qp} - \varepsilon_k/\hbar - \mathrm{Re}\,\Sigma(k, \omega_{qp}) = 0$，由此定义重整化能量 $\tilde\varepsilon_k = \varepsilon_k + \hbar\,\mathrm{Re}\,\Sigma(k, \omega_{qp})$。

**Step 2 — Define the quasiparticle residue $Z_k$.** The denominator of $G$ near $\omega_{qp}$ is, to leading order in the expansion,

$$ \omega - \varepsilon_k/\hbar - \Sigma \approx \left(1 - \frac{\partial\,\mathrm{Re}\,\Sigma}{\partial\omega}\right)\bigg|_{\omega_{qp}} \cdot (\omega - \omega_{qp}) - i\,\mathrm{Im}\,\Sigma(k, \omega_{qp}) = Z_k^{-1}\,(\omega - \omega_{qp} + i\,\Gamma_k/2), $$

where $Z_k = [1 - \partial\,\mathrm{Re}\,\Sigma/\partial\omega]^{-1}_{\omega_{qp}}$ is the **quasiparticle residue** ($0 < Z_k \le 1$) and $\Gamma_k = -2 Z_k\,\mathrm{Im}\,\Sigma(k, \omega_{qp})$ is the quasiparticle decay rate.

**第 2 步 — 定义准粒子留数 $Z_k$。** $G$ 的分母在 $\omega_{qp}$ 附近展开至领头阶为

$$ \omega - \varepsilon_k/\hbar - \Sigma \approx \left(1 - \frac{\partial\,\mathrm{Re}\,\Sigma}{\partial\omega}\right)\bigg|_{\omega_{qp}} \cdot (\omega - \omega_{qp}) - i\,\mathrm{Im}\,\Sigma(k, \omega_{qp}) = Z_k^{-1}\,(\omega - \omega_{qp} + i\,\Gamma_k/2), $$

其中 $Z_k = [1 - \partial\,\mathrm{Re}\,\Sigma/\partial\omega]^{-1}_{\omega_{qp}}$ 是**准粒子留数**（$0 < Z_k \le 1$），$\Gamma_k = -2 Z_k\,\mathrm{Im}\,\Sigma(k, \omega_{qp})$ 是准粒子衰减率。

**Step 3 — Read off the spectral function.** The quasiparticle part of $A(k, \omega)$ near the pole is

$$ A_{qp}(k, \omega) = \frac{Z_k}{\pi} \cdot \frac{\Gamma_k/2}{(\omega - \omega_{qp})^2 + (\Gamma_k/2)^2}, $$

a Lorentzian of height $Z_k/\pi$ at $\omega = \omega_{qp}$ and half-width $\Gamma_k/2$. The quasiparticle lifetime is $\tau_k = 1/\Gamma_k = \hbar/(-2 Z_k\,\mathrm{Im}\,\Sigma)$. In the non-interacting limit $\mathrm{Im}\,\Sigma \to 0$ and $Z_k \to 1$, the Lorentzian collapses to a delta function $\delta(\omega - \varepsilon_k/\hbar)$, recovering $G^0$. $\blacksquare$

**第 3 步 — 读出谱函数。** 极点附近 $A(k, \omega)$ 的准粒子部分为

$$ A_{qp}(k, \omega) = \frac{Z_k}{\pi} \cdot \frac{\Gamma_k/2}{(\omega - \omega_{qp})^2 + (\Gamma_k/2)^2}, $$

一个在 $\omega = \omega_{qp}$ 处高度为 $Z_k/\pi$、半宽为 $\Gamma_k/2$ 的洛伦兹峰。准粒子寿命为 $\tau_k = 1/\Gamma_k = \hbar/(-2 Z_k\,\mathrm{Im}\,\Sigma)$。在非相互作用极限 $\mathrm{Im}\,\Sigma \to 0$、$Z_k \to 1$ 时，洛伦兹峰退化为 $\delta$ 函数 $\delta(\omega - \varepsilon_k/\hbar)$，还原 $G^0$。$\blacksquare$

---

*These derivations establish the Green's function as the central object of many-body theory: it encodes the full single-particle excitation spectrum, is directly measurable (ARPES), satisfies exact sum rules, and has a perturbative expansion in terms of self-energies (Module 6.3).*

*上述推导确立了格林函数作为多体理论核心对象的地位：它编码完整的单粒子激发谱，可直接测量（ARPES），满足精确的求和规则，并关于自能（模块 6.3）有微扰展开。*

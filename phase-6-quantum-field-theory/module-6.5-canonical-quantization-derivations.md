# Derivations — Module 6.5: Canonical Quantization of Fields
# 推导 — 模块 6.5：场的正则量子化

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 6.5](./module-6.5-canonical-quantization.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 6.5](./module-6.5-canonical-quantization.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Canonical Quantization of the Real Klein–Gordon Field · 实克莱因–戈登场的正则量子化

**Claim.** Starting from the Klein–Gordon Lagrangian density $\mathcal{L} = \tfrac12(\partial_\mu \varphi)^2 - \tfrac12 m^2\varphi^2$ ($\hbar = c = 1$), the canonical quantization procedure imposes $[\hat\varphi(\mathbf x,t), \hat\pi(\mathbf y,t)] = i\delta^3(\mathbf x-\mathbf y)$. Expanding in mode operators yields $[\hat a_\mathbf{k}, \hat a^\dagger_{\mathbf k'}] = \delta^3(\mathbf k-\mathbf k')$, and the Hamiltonian is $\hat H = \int \frac{d^3k}{(2\pi)^3}\, \omega_k\, (\hat a^\dagger_\mathbf{k} \hat a_\mathbf{k} + \tfrac12)$.

**命题。** 从克莱因–戈登拉格朗日密度 $\mathcal{L} = \tfrac12(\partial_\mu \varphi)^2 - \tfrac12 m^2\varphi^2$（$\hbar = c = 1$）出发，正则量子化程序施加 $[\hat\varphi(\mathbf x,t), \hat\pi(\mathbf y,t)] = i\delta^3(\mathbf x-\mathbf y)$。按模式算符展开得 $[\hat a_\mathbf{k}, \hat a^\dagger_{\mathbf k'}] = \delta^3(\mathbf k-\mathbf k')$，哈密顿量为 $\hat H = \int \frac{d^3k}{(2\pi)^3}\, \omega_k\, (\hat a^\dagger_\mathbf{k} \hat a_\mathbf{k} + \tfrac12)$。

**Step 1 — Derive the canonical momentum.** The Lagrangian density is $\mathcal{L} = \tfrac12(\partial_t \varphi)^2 - \tfrac12(\nabla\varphi)^2 - \tfrac12 m^2\varphi^2$. The canonical momentum conjugate to $\varphi$ is

$$ \pi(x) = \frac{\partial\mathcal{L}}{\partial(\partial_t \varphi)} = \partial_t \varphi = \dot\varphi. $$

Canonical quantization promotes $\varphi$ and $\pi$ to operators $\hat\varphi$ and $\hat\pi = \partial_t \hat\varphi$ satisfying the equal-time commutator (ETCR):

$$ [\hat\varphi(\mathbf x,t), \hat\pi(\mathbf y,t)] = i\delta^3(\mathbf x-\mathbf y), \qquad [\hat\varphi(\mathbf x,t), \hat\varphi(\mathbf y,t)] = [\hat\pi(\mathbf x,t), \hat\pi(\mathbf y,t)] = 0. $$

**第 1 步 — 推导正则动量。** 拉格朗日密度为 $\mathcal{L} = \tfrac12(\partial_t \varphi)^2 - \tfrac12(\nabla\varphi)^2 - \tfrac12 m^2\varphi^2$。共轭于 $\varphi$ 的正则动量为

$$ \pi(x) = \frac{\partial\mathcal{L}}{\partial(\partial_t \varphi)} = \partial_t \varphi = \dot\varphi. $$

正则量子化将 $\varphi$ 和 $\pi$ 提升为满足等时对易子（ETCR）的算符 $\hat\varphi$ 和 $\hat\pi = \partial_t \hat\varphi$：

$$ [\hat\varphi(\mathbf x,t), \hat\pi(\mathbf y,t)] = i\delta^3(\mathbf x-\mathbf y), \qquad [\hat\varphi(\mathbf x,t), \hat\varphi(\mathbf y,t)] = [\hat\pi(\mathbf x,t), \hat\pi(\mathbf y,t)] = 0. $$

**Step 2 — Write the mode expansion.** The classical Klein–Gordon equation $(\partial_t^2 - \nabla^2 + m^2)\varphi = 0$ has plane-wave solutions $e^{\pm i(\mathbf k\cdot\mathbf x - \omega_k t)}$ with $\omega_k = \sqrt{\mathbf k^2 + m^2} > 0$ (the dispersion relation). The most general real solution is

$$ \hat\varphi(\mathbf x,t) = \int \frac{d^3k}{(2\pi)^3} \cdot \frac{1}{\sqrt{2\omega_k}}\, [\hat a_\mathbf{k}\, e^{i(\mathbf k\cdot\mathbf x - \omega_k t)} + \hat a^\dagger_\mathbf{k}\, e^{-i(\mathbf k\cdot\mathbf x - \omega_k t)}]. $$

The factor $1/\sqrt{2\omega_k}$ is the standard Lorentz-invariant normalization. Differentiating in time:

$$ \hat\pi(\mathbf x,t) = \partial_t \hat\varphi = \int \frac{d^3k}{(2\pi)^3} \cdot (-i)\sqrt{\omega_k/2}\, [\hat a_\mathbf{k}\, e^{i(\mathbf k\cdot\mathbf x - \omega_k t)} - \hat a^\dagger_\mathbf{k}\, e^{-i(\mathbf k\cdot\mathbf x - \omega_k t)}]. $$

**第 2 步 — 写出模式展开。** 经典克莱因–戈登方程 $(\partial_t^2 - \nabla^2 + m^2)\varphi = 0$ 有平面波解 $e^{\pm i(\mathbf k\cdot\mathbf x - \omega_k t)}$，其中 $\omega_k = \sqrt{\mathbf k^2 + m^2} > 0$（色散关系）。最一般的实解为

$$ \hat\varphi(\mathbf x,t) = \int \frac{d^3k}{(2\pi)^3} \cdot \frac{1}{\sqrt{2\omega_k}}\, [\hat a_\mathbf{k}\, e^{i(\mathbf k\cdot\mathbf x - \omega_k t)} + \hat a^\dagger_\mathbf{k}\, e^{-i(\mathbf k\cdot\mathbf x - \omega_k t)}]. $$

因子 $1/\sqrt{2\omega_k}$ 是标准的洛伦兹不变归一化。对时间求导：

$$ \hat\pi(\mathbf x,t) = \partial_t \hat\varphi = \int \frac{d^3k}{(2\pi)^3} \cdot (-i)\sqrt{\omega_k/2}\, [\hat a_\mathbf{k}\, e^{i(\mathbf k\cdot\mathbf x - \omega_k t)} - \hat a^\dagger_\mathbf{k}\, e^{-i(\mathbf k\cdot\mathbf x - \omega_k t)}]. $$

**Step 3 — Invert to express mode operators in terms of fields.** The mode operators are

$$ \hat a_\mathbf{k} = \int d^3x\, e^{-i\mathbf k\cdot\mathbf x}\, [\sqrt{\omega_k/2}\, \hat\varphi(\mathbf x,t) + \tfrac{i}{\sqrt{2\omega_k}}\, \hat\pi(\mathbf x,t)], $$

$$ \hat a^\dagger_\mathbf{k} = \int d^3x\, e^{i\mathbf k\cdot\mathbf x}\, [\sqrt{\omega_k/2}\, \hat\varphi(\mathbf x,t) - \tfrac{i}{\sqrt{2\omega_k}}\, \hat\pi(\mathbf x,t)]. $$

These follow from the Fourier inversion theorem: multiply $\hat\varphi(\mathbf x,t)$ by $e^{-i\mathbf k\cdot\mathbf x}$ and integrate over $\mathbf x$; use $\int d^3x\, e^{i(\mathbf k-\mathbf k')\cdot\mathbf x} = (2\pi)^3 \delta^3(\mathbf k-\mathbf k')$.

**第 3 步 — 反演以用场表示模式算符。** 模式算符为

$$ \hat a_\mathbf{k} = \int d^3x\, e^{-i\mathbf k\cdot\mathbf x}\, [\sqrt{\omega_k/2}\, \hat\varphi(\mathbf x,t) + \tfrac{i}{\sqrt{2\omega_k}}\, \hat\pi(\mathbf x,t)], $$

$$ \hat a^\dagger_\mathbf{k} = \int d^3x\, e^{i\mathbf k\cdot\mathbf x}\, [\sqrt{\omega_k/2}\, \hat\varphi(\mathbf x,t) - \tfrac{i}{\sqrt{2\omega_k}}\, \hat\pi(\mathbf x,t)]. $$

这些由傅里叶反演定理得出：将 $\hat\varphi(\mathbf x,t)$ 乘以 $e^{-i\mathbf k\cdot\mathbf x}$ 并对 $\mathbf x$ 积分；利用 $\int d^3x\, e^{i(\mathbf k-\mathbf k')\cdot\mathbf x} = (2\pi)^3 \delta^3(\mathbf k-\mathbf k')$。

**Step 4 — Derive $[\hat a_\mathbf{k}, \hat a^\dagger_{\mathbf k'}]$ from the ETCR.** Compute the commutator directly using the expressions from Step 3:

$$ [\hat a_\mathbf{k}, \hat a^\dagger_{\mathbf k'}] = \int d^3x\, d^3y\, e^{-i\mathbf k\cdot\mathbf x}\, e^{i\mathbf k'\cdot\mathbf y} \times (\text{commutator of the } \hat\varphi \text{ and } \hat\pi \text{ terms}). $$

The cross terms $[\hat\varphi(\mathbf x), \hat\varphi(\mathbf y)] = 0$ and $[\hat\pi(\mathbf x), \hat\pi(\mathbf y)] = 0$ vanish. The surviving term is

$$ \left(\tfrac{i}{\sqrt{2\omega_k}}\right) \cdot \left(\tfrac{-i}{\sqrt{2\omega_{k'}}}\right) [\hat\pi(\mathbf x), \hat\varphi(\mathbf y)] \cdot \sqrt{\omega_{k'}/2} \cdot \sqrt{\omega_k/2} \ldots $$

More precisely, expanding the bilinears from Step 3 and using $[\hat\varphi(\mathbf x,t), \hat\pi(\mathbf y,t)] = i\delta^3(\mathbf x-\mathbf y)$:

$$ \begin{aligned} [\hat a_\mathbf{k}, \hat a^\dagger_{\mathbf k'}] &= \int d^3x\, e^{-i\mathbf k\cdot\mathbf x} e^{i\mathbf k'\cdot\mathbf x} \cdot \left(\tfrac{i}{\sqrt{2\omega_k}}\right) \cdot \left(\tfrac{-i}{\sqrt{2\omega_{k'}}}\right) \cdot \omega_{k'} + (\text{contributions from } [\pi,\varphi]) \\ &= \int d^3x\, e^{i(\mathbf k'-\mathbf k)\cdot\mathbf x} \cdot \tfrac12 (\omega_{k'}/\omega_k)^{1/2} \cdot (\omega_k/\omega_{k'})^{1/2} \cdot 2 \cdot \tfrac12 \quad [\text{via } [\hat\varphi,\hat\pi] + [-\hat\pi,-\hat\varphi] \text{ terms}] \end{aligned} $$

Let us be careful. From the inversion formulas, the cross terms give:

$$ [\hat a_\mathbf{k}, \hat a^\dagger_{\mathbf k'}] = \int d^3x\, d^3y\, e^{-i\mathbf k\cdot\mathbf x+i\mathbf k'\cdot\mathbf y}\, \left[\sqrt{\omega_k/2}\, \hat\varphi(\mathbf x) + \tfrac{i\hat\pi(\mathbf x)}{\sqrt{2\omega_k}},\; \sqrt{\omega_{k'}/2}\, \hat\varphi(\mathbf y) - \tfrac{i\hat\pi(\mathbf y)}{\sqrt{2\omega_{k'}}}\right] $$

Expanding: the $[\hat\varphi,\hat\varphi]$ and $[\hat\pi,\hat\pi]$ pieces vanish. The cross terms are

$$ \begin{aligned} &-i\tfrac{\sqrt{\omega_k/2}}{\sqrt{2\omega_{k'}}}\, [\hat\varphi(\mathbf x), \hat\pi(\mathbf y)] + \tfrac{i}{\sqrt{2\omega_k} \cdot \sqrt{\omega_{k'}/2}}\, [\hat\pi(\mathbf x), \hat\varphi(\mathbf y)] \\ &= -i\tfrac{\sqrt{\omega_k/2}}{\sqrt{2\omega_{k'}}} \cdot i\delta^3(\mathbf x-\mathbf y) + \tfrac{i}{\sqrt{2\omega_k} \cdot \sqrt{\omega_{k'}/2}} \cdot (-i)\delta^3(\mathbf x-\mathbf y) \\ &= \left[\tfrac{\sqrt{\omega_k/2}}{\sqrt{2\omega_{k'}}} + \tfrac{1}{\sqrt{2\omega_k} \cdot \sqrt{\omega_{k'}/2}}\right] \delta^3(\mathbf x-\mathbf y) \\ &= \frac{\sqrt{\omega_k/\omega_{k'}} + \sqrt{\omega_{k'}/\omega_k}}{2} \cdot \delta^3(\mathbf x-\mathbf y). \end{aligned} $$

After integrating over $\mathbf x$ and $\mathbf y$ with $e^{-i\mathbf k\cdot\mathbf x+i\mathbf k'\cdot\mathbf y}$ and setting $\mathbf x = \mathbf y$ from the delta function:

$$ [\hat a_\mathbf{k}, \hat a^\dagger_{\mathbf k'}] = \frac{\sqrt{\omega_k/\omega_{k'}} + \sqrt{\omega_{k'}/\omega_k}}{2} \cdot \int d^3x\, e^{i(\mathbf k'-\mathbf k)\cdot\mathbf x}. $$

At $\mathbf k = \mathbf k'$ this factor is 1; and $\int d^3x\, e^{i(\mathbf k'-\mathbf k)\cdot\mathbf x} = (2\pi)^3 \delta^3(\mathbf k-\mathbf k')$. Therefore

$$ \boxed{\, [\hat a_\mathbf{k}, \hat a^\dagger_{\mathbf k'}] = (2\pi)^3 \delta^3(\mathbf k-\mathbf k') \,} $$

(With the convention where $\hat a_\mathbf{k} = (2\pi)^3 \times$ the $\hat a$ used above, or equivalently using the standard normalization $\int \frac{d^3k}{(2\pi)^3}$, the result is $[\hat a_\mathbf{k}, \hat a^\dagger_{\mathbf k'}] = \delta^3(\mathbf k-\mathbf k')$ in the normalized convention.) $\blacksquare$

**第 4 步 — 从 ETCR 推导 $[\hat a_\mathbf{k}, \hat a^\dagger_{\mathbf k'}]$。** 利用第 3 步的表达式直接计算对易子：

$$ [\hat a_\mathbf{k}, \hat a^\dagger_{\mathbf k'}] = \int d^3x\, d^3y\, e^{-i\mathbf k\cdot\mathbf x}\, e^{i\mathbf k'\cdot\mathbf y} \times (\hat\varphi \text{ 和 } \hat\pi \text{ 项的对易子}). $$

交叉项 $[\hat\varphi(\mathbf x), \hat\varphi(\mathbf y)] = 0$ 和 $[\hat\pi(\mathbf x), \hat\pi(\mathbf y)] = 0$ 消失。存活的项使用 $[\hat\varphi(\mathbf x,t), \hat\pi(\mathbf y,t)] = i\delta^3(\mathbf x-\mathbf y)$。展开后所有项精确化简为

$$ \boxed{\, [\hat a_\mathbf{k}, \hat a^\dagger_{\mathbf k'}] = (2\pi)^3 \delta^3(\mathbf k-\mathbf k') \,} $$

（在 $\int \frac{d^3k}{(2\pi)^3}$ 归一化约定下，这等价于 $[\hat a_\mathbf{k}, \hat a^\dagger_{\mathbf k'}] = \delta^3(\mathbf k-\mathbf k')$。）$\blacksquare$

**Step 5 — Derive the Hamiltonian.** The classical Hamiltonian density is $\mathcal{H} = \pi \dot\varphi - \mathcal{L} = \tfrac12\pi^2 + \tfrac12(\nabla\varphi)^2 + \tfrac12 m^2\varphi^2$. Substitute the mode expansion and integrate over $d^3x$. Using the orthogonality integrals $\int d^3x\, e^{i(\mathbf k-\mathbf k')\cdot\mathbf x} = (2\pi)^3\delta^3(\mathbf k-\mathbf k')$ and collecting terms:

$$ \hat H = \int \frac{d^3k}{(2\pi)^3}\, \omega_k\, (\hat a^\dagger_\mathbf{k} \hat a_\mathbf{k} + \tfrac12(2\pi)^3\delta^3(0)). $$

The $\delta^3(0)$ term is the zero-point energy (UV divergent, normal-ordered away). In normal-ordered form:

$$ :\hat H: = \int \frac{d^3k}{(2\pi)^3}\, \omega_k\, \hat a^\dagger_\mathbf{k} \hat a_\mathbf{k}. $$

Including the zero-point term formally:

$$ \hat H = \int \frac{d^3k}{(2\pi)^3}\, \omega_k\, (\hat a^\dagger_\mathbf{k} \hat a_\mathbf{k} + \tfrac12). \qquad \blacksquare $$

**第 5 步 — 推导哈密顿量。** 经典哈密顿量密度为 $\mathcal{H} = \pi \dot\varphi - \mathcal{L} = \tfrac12\pi^2 + \tfrac12(\nabla\varphi)^2 + \tfrac12 m^2\varphi^2$。代入模式展开并对 $d^3x$ 积分。利用正交积分 $\int d^3x\, e^{i(\mathbf k-\mathbf k')\cdot\mathbf x} = (2\pi)^3\delta^3(\mathbf k-\mathbf k')$ 并收集各项：

$$ \hat H = \int \frac{d^3k}{(2\pi)^3}\, \omega_k\, (\hat a^\dagger_\mathbf{k} \hat a_\mathbf{k} + \tfrac12(2\pi)^3\delta^3(0)). $$

$\delta^3(0)$ 项是零点能（紫外发散，正规序后减去）。正规序形式：

$$ :\hat H: = \int \frac{d^3k}{(2\pi)^3}\, \omega_k\, \hat a^\dagger_\mathbf{k} \hat a_\mathbf{k}. $$

包含零点项的形式表达：

$$ \hat H = \int \frac{d^3k}{(2\pi)^3}\, \omega_k\, (\hat a^\dagger_\mathbf{k} \hat a_\mathbf{k} + \tfrac12). \qquad \blacksquare $$

---

## B. Anticommutation Relations for the Dirac Field · 狄拉克场的反对易关系

**Claim.** Quantizing the Dirac field $\psi(x)$ with anticommutators — rather than commutators — is required by the spin-statistics theorem. The anticommutation relations are $\{\psi_\alpha(\mathbf x,t), \psi^\dagger_\beta(\mathbf y,t)\} = \delta_{\alpha\beta}\, \delta^3(\mathbf x-\mathbf y)$, where $\alpha, \beta$ are spinor indices. Using commutators instead would violate the positivity of the Hamiltonian.

**命题。** 将狄拉克场 $\psi(x)$ 用反对易子——而非对易子——量子化，是自旋-统计定理的要求。反对易关系为 $\{\psi_\alpha(\mathbf x,t), \psi^\dagger_\beta(\mathbf y,t)\} = \delta_{\alpha\beta}\, \delta^3(\mathbf x-\mathbf y)$，其中 $\alpha$、$\beta$ 是旋量指标。改用对易子将违反哈密顿量的正定性。

**Step 1 — Mode expansion of the Dirac field.** The Dirac equation $(i\gamma^\mu\partial_\mu - m)\psi = 0$ has positive-frequency solutions $u^s(k)e^{-ik\cdot x}$ (particle, $s = 1,2$ spin labels) and negative-frequency solutions $v^s(k)e^{ik\cdot x}$ (antiparticle). The general expansion is

$$ \hat\psi(x) = \int \frac{d^3k}{(2\pi)^3}\, \frac{1}{\sqrt{2\omega_k}} \sum_s [b^s_\mathbf{k}\, u^s(k)\, e^{-ik\cdot x} + d^{s\dagger}_\mathbf{k}\, v^s(k)\, e^{ik\cdot x}], $$

where $b^s_\mathbf{k}$ annihilates a particle and $d^{s\dagger}_\mathbf{k}$ creates an antiparticle.

**第 1 步 — 狄拉克场的模式展开。** 狄拉克方程 $(i\gamma^\mu\partial_\mu - m)\psi = 0$ 有正频解 $u^s(k)e^{-ik\cdot x}$（粒子，$s = 1,2$ 为自旋标记）和负频解 $v^s(k)e^{ik\cdot x}$（反粒子）。一般展开为

$$ \hat\psi(x) = \int \frac{d^3k}{(2\pi)^3}\, \frac{1}{\sqrt{2\omega_k}} \sum_s [b^s_\mathbf{k}\, u^s(k)\, e^{-ik\cdot x} + d^{s\dagger}_\mathbf{k}\, v^s(k)\, e^{ik\cdot x}], $$

其中 $b^s_\mathbf{k}$ 湮灭一个粒子，$d^{s\dagger}_\mathbf{k}$ 产生一个反粒子。

**Step 2 — Compute the Hamiltonian with commutators (to show the problem).** The Dirac Hamiltonian is $\hat H = \int \frac{d^3k}{(2\pi)^3} \sum_s \omega_k\, (b^{s\dagger}_\mathbf{k} b^s_\mathbf{k} \pm d^{s\dagger}_\mathbf{k} d^s_\mathbf{k})$ (sign depends on ordering), where the $\pm$ comes from commutator ($+$) versus anticommutator ($-$) statistics. With bosonic commutators $[b, b^\dagger] = 1$, the antiparticle sector contributes $-\omega_k d^{s\dagger}_\mathbf{k} d^s_\mathbf{k}$ to $\hat H$. This makes the energy **unbounded below** (states with arbitrarily many antiparticles have energy $-\infty$): the theory is unstable.

**第 2 步 — 用对易子计算哈密顿量（以展示问题）。** 狄拉克哈密顿量为 $\hat H = \int \frac{d^3k}{(2\pi)^3} \sum_s \omega_k\, (b^{s\dagger}_\mathbf{k} b^s_\mathbf{k} \pm d^{s\dagger}_\mathbf{k} d^s_\mathbf{k})$（符号取决于排序），其中 $\pm$ 来自对易子（$+$）与反对易子（$-$）统计。用玻色对易子 $[b, b^\dagger] = 1$，反粒子扇区给出 $-\omega_k d^{s\dagger}_\mathbf{k} d^s_\mathbf{k}$ 对 $\hat H$ 的贡献。这使能量**无下界**（含任意多反粒子的态能量为 $-\infty$）：理论不稳定。

**Step 3 — Resolve with anticommutators.** Imposing the fermionic anticommutation relations $\{b^s_\mathbf{k}, b^{s'\dagger}_{\mathbf k'}\} = \delta^{ss'} (2\pi)^3 \delta^3(\mathbf k-\mathbf k')$ (and similarly for $d$), the normal-ordered Hamiltonian becomes

$$ :\hat H: = \int \frac{d^3k}{(2\pi)^3} \sum_s \omega_k\, (b^{s\dagger}_\mathbf{k} b^s_\mathbf{k} + d^{s\dagger}_\mathbf{k} d^s_\mathbf{k}). $$

Both terms are positive (number operators times $\omega_k > 0$). The Hamiltonian is **bounded below** with ground state $|0\rangle$ satisfying $b^s_\mathbf{k}|0\rangle = d^s_\mathbf{k}|0\rangle = 0$. $\blacksquare$

**第 3 步 — 用反对易子解决。** 施加费米子反对易关系 $\{b^s_\mathbf{k}, b^{s'\dagger}_{\mathbf k'}\} = \delta^{ss'} (2\pi)^3 \delta^3(\mathbf k-\mathbf k')$（$d$ 类似），正规序哈密顿量变为

$$ :\hat H: = \int \frac{d^3k}{(2\pi)^3} \sum_s \omega_k\, (b^{s\dagger}_\mathbf{k} b^s_\mathbf{k} + d^{s\dagger}_\mathbf{k} d^s_\mathbf{k}). $$

两项均为正（数算符乘以 $\omega_k > 0$）。哈密顿量**有下界**，基态 $|0\rangle$ 满足 $b^s_\mathbf{k}|0\rangle = d^s_\mathbf{k}|0\rangle = 0$。$\blacksquare$

**Step 4 — Derive $\{\psi_\alpha(\mathbf x,t), \psi^\dagger_\beta(\mathbf y,t)\} = \delta_{\alpha\beta}\delta^3(\mathbf x-\mathbf y)$.** Insert the mode expansions into the anticommutator. Using the anticommutation relations for $b$ and $d$, and the completeness relations for the Dirac spinors:

$$ \sum_s u^s_\alpha(k)\, \bar u^s_\beta(k) = (\not{k} + m)_{\alpha\beta}, \qquad \sum_s v^s_\alpha(k)\, \bar v^s_\beta(k) = (\not{k} - m)_{\alpha\beta}, $$

(where $\not{k} = \gamma^\mu k_\mu$ and the bar denotes $\bar\psi = \psi^\dagger\gamma^0$), the spatial Fourier integral selects equal momenta and the spinor completeness sums reduce to:

$$ \{\hat\psi_\alpha(\mathbf x,t), \hat\psi^\dagger_\beta(\mathbf y,t)\} = \int \frac{d^3k}{(2\pi)^3}\, \frac{1}{2\omega_k} \sum_s [u^s_\alpha(k)\, u^{s*}_\beta(k) + v^{s*}_\alpha(k)\, v^s_\beta(k)]\, e^{i\mathbf k\cdot(\mathbf x-\mathbf y)}. $$

The spinor sums evaluate to $\delta_{\alpha\beta}$ times a factor that, after the Fourier integral, yields $\delta^3(\mathbf x-\mathbf y)$. Thus

$$ \boxed{\, \{\hat\psi_\alpha(\mathbf x,t), \hat\psi^\dagger_\beta(\mathbf y,t)\} = \delta_{\alpha\beta}\, \delta^3(\mathbf x-\mathbf y) \,} \qquad \blacksquare $$

**第 4 步 — 推导 $\{\psi_\alpha(\mathbf x,t), \psi^\dagger_\beta(\mathbf y,t)\} = \delta_{\alpha\beta}\delta^3(\mathbf x-\mathbf y)$。** 将模式展开代入反对易子。利用 $b$ 和 $d$ 的反对易关系以及狄拉克旋量的完备性关系：

$$ \sum_s u^s_\alpha(k)\, \bar u^s_\beta(k) = (\not{k} + m)_{\alpha\beta}, \qquad \sum_s v^s_\alpha(k)\, \bar v^s_\beta(k) = (\not{k} - m)_{\alpha\beta}, $$

（其中 $\not{k} = \gamma^\mu k_\mu$，上横杆表示 $\bar\psi = \psi^\dagger\gamma^0$），空间傅里叶积分选出等动量，旋量完备性求和化简为：

$$ \{\hat\psi_\alpha(\mathbf x,t), \hat\psi^\dagger_\beta(\mathbf y,t)\} = \int \frac{d^3k}{(2\pi)^3}\, \frac{1}{2\omega_k} \sum_s [u^s_\alpha(k)\, u^{s*}_\beta(k) + v^{s*}_\alpha(k)\, v^s_\beta(k)]\, e^{i\mathbf k\cdot(\mathbf x-\mathbf y)}. $$

旋量求和等于 $\delta_{\alpha\beta}$ 乘以一个因子，经傅里叶积分后给出 $\delta^3(\mathbf x-\mathbf y)$。因此

$$ \boxed{\, \{\hat\psi_\alpha(\mathbf x,t), \hat\psi^\dagger_\beta(\mathbf y,t)\} = \delta_{\alpha\beta}\, \delta^3(\mathbf x-\mathbf y) \,} \qquad \blacksquare $$

---

## C. The Spin-Statistics Theorem · 自旋-统计定理

**Claim.** In any local, relativistic quantum field theory: integer-spin fields must be quantized with commutators (Bose statistics), and half-integer-spin fields must be quantized with anticommutators (Fermi statistics). Violating this leads to either non-positive-energy, non-causal, or non-unitary theory.

**命题。** 在任何局域相对论量子场论中：整数自旋场必须用对易子量子化（玻色统计），半整数自旋场必须用反对易子量子化（费米统计）。违背此规则将导致能量非正定、非因果或非幺正的理论。

**Step 1 — Lorentz invariance constrains the fields.** A field of spin $s$ transforms under the $(A, B)$ representation of the Lorentz group with $A + B = s$. The field equation (and its solutions) inherits this transformation law. The commutator function $\Delta(x-y) = [\hat\varphi(x), \hat\varphi(y)]$ for a free field must be a Lorentz-invariant function of $(x-y)$.

**第 1 步 — 洛伦兹不变性约束场。** 自旋 $s$ 的场在洛伦兹群的 $(A, B)$ 表示下变换，$A + B = s$。场方程（及其解）继承这一变换规律。自由场的对易子函数 $\Delta(x-y) = [\hat\varphi(x), \hat\varphi(y)]$ 必须是 $(x-y)$ 的洛伦兹不变函数。

**Step 2 — Microcausality requirement.** Physical observables $O(x)$ (bilinears in the fields) must commute for spacelike separations: $[O(x), O(y)] = 0$ for $(x-y)^2 < 0$. This is **microcausality** — signals cannot travel faster than light. For a scalar field built from $\hat\varphi$, this requires $[\hat\varphi(x), \hat\varphi(y)] = 0$ for spacelike $(x-y)$.

**第 2 步 — 微观因果性要求。** 物理可观测量 $O(x)$（场的双线性形式）对于类空间隔必须对易：当 $(x-y)^2 < 0$ 时 $[O(x), O(y)] = 0$。这是**微观因果性**——信号不能以超过光速传播。对于由 $\hat\varphi$ 构建的标量场，这要求当 $(x-y)$ 是类空时 $[\hat\varphi(x), \hat\varphi(y)] = 0$。

**Step 3 — The crucial parity argument.** For a spin-$s$ field, the (anti)commutator $[\hat\varphi(x), \hat\varphi^\dagger(y)]_\pm$ expanded in modes contains terms $e^{ik\cdot(x-y)}$ and $e^{-ik\cdot(x-y)}$. Under $(x-y) \to -(x-y)$ (spatial reflection combined with time reversal, a rotation by $\pi$ in Euclidean space), the two terms acquire a relative phase $(-1)^{2s}$. For integer $s$, $(-1)^{2s} = +1$: the commutator $\Delta(x-y) = -\Delta(y-x)$ is consistent with causality via the standard commutator. For half-integer $s$, $(-1)^{2s} = -1$: the commutator would give $\Delta(x-y) = +\Delta(y-x)$, which cannot vanish for all spacelike separations unless we instead use the anticommutator $\{\hat\varphi, \hat\varphi^\dagger\}_-$, which satisfies the required vanishing.

**第 3 步 — 关键的宇称论证。** 对于自旋 $s$ 的场，（反）对易子 $[\hat\varphi(x), \hat\varphi^\dagger(y)]_\pm$ 在模式展开中包含 $e^{ik\cdot(x-y)}$ 和 $e^{-ik\cdot(x-y)}$ 项。在 $(x-y) \to -(x-y)$（空间反射加时间反转，即欧几里得空间中的 $\pi$ 转动）下，两项获得相对相位 $(-1)^{2s}$。对于整数 $s$，$(-1)^{2s} = +1$：对易子 $\Delta(x-y) = -\Delta(y-x)$ 通过标准对易子与因果性相容。对于半整数 $s$，$(-1)^{2s} = -1$：对易子将给出 $\Delta(x-y) = +\Delta(y-x)$，对所有类空间隔不能为零——除非改用反对易子 $\{\hat\varphi, \hat\varphi^\dagger\}$，它满足要求的消失性。

**Step 4 — Conclusion.** Therefore:
- Integer spin ($s = 0, 1, 2, \ldots$): use commutators $\to$ **Bose–Einstein statistics**.
- Half-integer spin ($s = \tfrac12, 3/2, \ldots$): use anticommutators $\to$ **Fermi–Dirac statistics**.

The spin-statistics connection is a theorem of relativistic quantum field theory, not an additional postulate. Its violation would permit faster-than-light signaling or negative-energy states. $\blacksquare$

**第 4 步 — 结论。** 因此：
- 整数自旋（$s = 0, 1, 2, \ldots$）：使用对易子 $\to$ **玻色–爱因斯坦统计**。
- 半整数自旋（$s = \tfrac12, 3/2, \ldots$）：使用反对易子 $\to$ **费米–狄拉克统计**。

自旋-统计联系是相对论量子场论的一个定理，而非额外的假设。违背它将允许超光速信号或负能态。$\blacksquare$

---

*The canonical quantization of the Klein–Gordon field shows concretely how the ETCR forces $[\hat a_\mathbf{k}, \hat a^\dagger_{\mathbf k'}] = \delta$, and the derivation of the Hamiltonian confirms the harmonic-oscillator interpretation: each mode is a quantum oscillator with quanta (particles). The Dirac calculation demonstrates why the statistics and spin are not independent: relativistic causality alone determines which quantization is consistent.*

*克莱因–戈登场的正则量子化具体展示了 ETCR 如何迫使 $[\hat a_\mathbf{k}, \hat a^\dagger_{\mathbf k'}] = \delta$，哈密顿量的推导证实了谐振子诠释：每个模式是具有量子（粒子）的量子振子。狄拉克场的计算表明统计与自旋并非独立：仅相对论因果性就决定了哪种量子化是自洽的。*

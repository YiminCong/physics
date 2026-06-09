# Module 3.18 — Quantum Scattering Theory
**模块 3.18 — 量子散射理论**

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 3 阶段 — 量子力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-3.18-quantum-scattering-theory-derivations.md)

---

## 1. Scattering Amplitude and Cross Section · 散射振幅与截面

**Definition.** A scattering experiment sends a steady beam of particles of definite energy $E = \hbar^2 k^2/2m$ onto a localized target potential $V(r)$ and counts how many emerge into each solid angle. The stationary scattering state is the energy eigenstate whose asymptotic form (far from the target, where $V \to 0$) is a plane wave plus an outgoing spherical wave:

$$ \psi(\mathbf{r}) \to e^{ikz} + f(\theta)\, \frac{e^{ikr}}{r}, \qquad \text{as } r \to \infty. $$

The coefficient $f(\theta)$ is the **scattering amplitude**; it carries all the physics of the collision and has the dimension of length. The **differential cross section** $d\sigma/d\Omega$ is defined as the number of particles scattered per unit time into solid angle $d\Omega$, divided by the incident flux (particles per unit area per unit time). It is the effective area the target presents for scattering into that direction.

**定义。** 散射实验将一束能量确定 $E = \hbar^2 k^2/2m$ 的稳定粒子流射向局域靶势 $V(r)$，并计数射入每个立体角的粒子数。定态散射态是能量本征态，其渐近形式（远离靶、$V \to 0$ 处）为平面波加出射球面波：

$$ \psi(\mathbf{r}) \to e^{ikz} + f(\theta)\, \frac{e^{ikr}}{r}, \qquad \text{当 } r \to \infty. $$

系数 $f(\theta)$ 称为**散射振幅**；它承载碰撞的全部物理信息，量纲为长度。**微分截面** $d\sigma/d\Omega$ 定义为单位时间散射进立体角 $d\Omega$ 的粒子数除以入射通量（单位面积单位时间的粒子数），即靶在该方向上呈现的有效散射面积。

**Demonstration.** The cross section follows from the quantum probability current $\mathbf{j} = (\hbar/m)\, \text{Im}(\psi^* \nabla\psi)$. The incident plane wave $e^{ikz}$ carries flux $j_\text{inc} = \hbar k/m$ along $z$. The outgoing spherical wave $f(\theta)e^{ikr}/r$ carries a radial flux $j_\text{scatt} = (\hbar k/m)|f(\theta)|^2/r^2$. The number scattered into $d\Omega$ per unit time is $j_\text{scatt} \cdot r^2\, d\Omega$, and dividing by $j_\text{inc}$ gives the central result:

$$ \frac{d\sigma}{d\Omega} = |f(\theta)|^2, \qquad \sigma = \int |f(\theta)|^2\, d\Omega. $$

The $1/r^2$ in the flux cancels the $r^2$ in the area element $r^2 d\Omega$, which is precisely why the spherical wave is normalized as $f(\theta)e^{ikr}/r$ — it guarantees a finite, $r$-independent cross section. The full derivation is in **Derivation A**.

**演示。** 截面由量子概率流 $\mathbf{j} = (\hbar/m)\, \text{Im}(\psi^* \nabla\psi)$ 给出。入射平面波 $e^{ikz}$ 沿 $z$ 方向携带通量 $j_\text{inc} = \hbar k/m$。出射球面波 $f(\theta)e^{ikr}/r$ 携带径向通量 $j_\text{scatt} = (\hbar k/m)|f(\theta)|^2/r^2$。单位时间散射进 $d\Omega$ 的粒子数为 $j_\text{scatt} \cdot r^2\, d\Omega$，除以 $j_\text{inc}$ 即得核心结果 $\dfrac{d\sigma}{d\Omega} = |f(\theta)|^2$，$\sigma = \int |f(\theta)|^2\, d\Omega$。通量中的 $1/r^2$ 恰好抵消面元 $r^2 d\Omega$ 中的 $r^2$，这正是球面波归一化为 $f(\theta)e^{ikr}/r$ 的原因——它保证截面有限且不依赖 $r$。完整推导见**推导 A**。

**Application.** The scattering amplitude is the experimental bridge between theory and measurement: detectors measure $d\sigma/d\Omega$ directly, and inverting it constrains the potential $V(r)$. Two complementary methods compute $f(\theta)$. The **Born approximation** (Module 3.8) treats $V$ as a weak perturbation and works best at high energy, giving $f(\theta) \propto$ the Fourier transform of $V$; the **partial-wave method** (Section 2) is exact and works best at low energy. For a pure Coulomb potential the quantum $f(\theta)$ reproduces exactly the classical **Rutherford cross section** (Module 1.21), one of the rare cases where the classical and quantum differential cross sections coincide.

**应用。** 散射振幅是理论与测量之间的实验桥梁：探测器直接测量 $d\sigma/d\Omega$，反演它即可约束势 $V(r)$。计算 $f(\theta)$ 有两种互补方法。**玻恩近似**（模块 3.8）将 $V$ 视为弱微扰，在高能下最佳，给出 $f(\theta) \propto V$ 的傅里叶变换；**分波法**（第 2 节）精确且在低能下最佳。对纯库仑势，量子 $f(\theta)$ 精确重现经典的**卢瑟福截面**（模块 1.21），这是经典与量子微分截面罕见的重合情形之一。

---

## 2. Partial Waves, Phase Shifts, and the Optical Theorem · 分波、相移与光学定理

**Definition.** For a **central potential** $V(r)$, angular momentum is conserved, so the scattering problem separates in spherical coordinates and each angular-momentum channel $\ell$ scatters independently. The full effect of the potential on channel $\ell$ is encoded in a single real number, the **phase shift $\delta_\ell(k)$**: far from the target the radial wavefunction $u_\ell(r) = r R_\ell(r)$ behaves as

$$ u_\ell(r) \to \sin(kr - \ell\pi/2 + \delta_\ell), \qquad \text{as } r \to \infty, $$

i.e. it is the free spherical Bessel solution shifted in phase by $\delta_\ell$ relative to the no-potential case. An attractive potential pulls the wave inward ($\delta_\ell > 0$); a repulsive one pushes it out ($\delta_\ell < 0$). All observables are built from the set $\{\delta_\ell\}$.

**定义。** 对**中心势** $V(r)$，角动量守恒，故散射问题在球坐标中分离，每个角动量通道 $\ell$ 独立散射。势对通道 $\ell$ 的全部作用被编码进一个实数——**相移 $\delta_\ell(k)$**：远离靶处，径向波函数 $u_\ell(r) = r R_\ell(r)$ 表现为 $u_\ell(r) \to \sin(kr - \ell\pi/2 + \delta_\ell)$，即相对无势情形，它是自由球贝塞尔解平移了相位 $\delta_\ell$。吸引势把波拉向内（$\delta_\ell > 0$），排斥势把波推向外（$\delta_\ell < 0$）。所有可观测量都由集合 $\{\delta_\ell\}$ 构造。

**Demonstration.** Expanding both the incident plane wave and the scattering state in Legendre polynomials $P_\ell(\cos\theta)$ and matching the asymptotic forms term by term expresses the amplitude entirely through phase shifts:

$$ f(\theta) = \frac{1}{k} \sum_{\ell=0}^\infty (2\ell+1)\, e^{i\delta_\ell} \sin\delta_\ell\, P_\ell(\cos\theta). $$

Integrating $|f(\theta)|^2$ over all angles with the orthogonality relation $\int P_\ell P_{\ell'}\, d\Omega = [4\pi/(2\ell+1)]\, \delta_{\ell\ell'}$ collapses the double sum to a single sum, giving the **total cross section**:

$$ \sigma = \frac{4\pi}{k^2} \sum_\ell (2\ell+1) \sin^2\delta_\ell. $$

Evaluating $f$ at $\theta = 0$, where every $P_\ell(1) = 1$, isolates the imaginary part $\text{Im}\, f(0) = (1/k) \sum_\ell (2\ell+1) \sin^2\delta_\ell$, which is exactly $(k/4\pi)\sigma$. This is the **optical theorem**:

$$ \sigma_\text{tot} = \frac{4\pi}{k}\, \text{Im}\, f(0). $$

Derivations B and C give the full proofs.

**演示。** 将入射平面波与散射态都用勒让德多项式 $P_\ell(\cos\theta)$ 展开，并逐项匹配渐近形式，可将振幅完全用相移表示：$f(\theta) = \dfrac{1}{k} \sum_{\ell=0}^\infty (2\ell+1)\, e^{i\delta_\ell} \sin\delta_\ell\, P_\ell(\cos\theta)$。利用正交关系 $\int P_\ell P_{\ell'}\, d\Omega = [4\pi/(2\ell+1)]\, \delta_{\ell\ell'}$ 对全角度积分 $|f(\theta)|^2$，双重求和坍缩为单重求和，得**总截面** $\sigma = \dfrac{4\pi}{k^2} \sum_\ell (2\ell+1) \sin^2\delta_\ell$。在 $\theta = 0$ 处（每个 $P_\ell(1) = 1$）取虚部得 $\text{Im}\, f(0) = (1/k) \sum_\ell (2\ell+1) \sin^2\delta_\ell$，恰为 $(k/4\pi)\sigma$。这就是**光学定理** $\sigma_\text{tot} = \dfrac{4\pi}{k}\, \text{Im}\, f(0)$。完整证明见推导 B、C。

**Application.** Partial waves are the method of choice at low energy, where only a few $\ell$ contribute: a particle of wavenumber $k$ and impact parameter $b \approx \ell/k$ cannot reach a short-range potential of range $a$ unless $\ell \lesssim ka$, so for $ka \ll 1$ only the $\ell = 0$ (s-wave) term survives. The optical theorem is a statement of **flux conservation (unitarity)**: the total flux removed from the forward beam ($\sigma_\text{tot}$) equals the forward-amplitude interference encoded in $\text{Im}\, f(0)$. At high energy the S-matrix formulation (Modules 6.8, 8.9) generalizes phase shifts to inelastic and relativistic channels, with $e^{2i\delta_\ell}$ becoming the diagonal S-matrix element.

**应用。** 分波法是低能下的首选方法，此时只有少数 $\ell$ 有贡献：波数 $k$、碰撞参数 $b \approx \ell/k$ 的粒子无法到达射程为 $a$ 的短程势，除非 $\ell \lesssim ka$，故当 $ka \ll 1$ 时只剩 $\ell = 0$（s 波）项。光学定理是**通量守恒（幺正性）**的陈述：从前向束流中移除的总通量（$\sigma_\text{tot}$）等于 $\text{Im}\, f(0)$ 所编码的前向振幅干涉。在高能下，S 矩阵形式（模块 6.8、8.9）将相移推广到非弹性与相对论通道，$e^{2i\delta_\ell}$ 成为对角 S 矩阵元。

---

## 3. Scattering Length and Resonances · 散射长度与共振

**Definition.** At very low energy ($k \to 0$) the s-wave dominates and its phase shift behaves linearly, $\delta_0(k) \to -ka$, defining the **scattering length $a$**, a single length that characterizes the whole low-energy interaction. The amplitude tends to a constant $f \to -a$, the scattering becomes isotropic, and the cross section approaches $\sigma \to 4\pi a^2$. A **resonance** is the opposite, sharply energy-dependent regime: when a quasi-bound state exists at energy $E_R$ with width $\Gamma$, the phase shift $\delta_\ell$ sweeps rapidly through $\pi/2$, and the partial cross section traces a **Breit–Wigner** peak.

**定义。** 在极低能（$k \to 0$）下，s 波主导，其相移线性变化 $\delta_0(k) \to -ka$，定义**散射长度 $a$**——刻画整个低能相互作用的单一长度。振幅趋于常数 $f \to -a$，散射变为各向同性，截面趋于 $\sigma \to 4\pi a^2$。**共振**则是相反的、强烈依赖能量的区域：当能量 $E_R$ 处存在宽度为 $\Gamma$ 的准束缚态时，相移 $\delta_\ell$ 迅速扫过 $\pi/2$，分波截面描出 **Breit–Wigner** 峰。

**Demonstration.** Setting $\delta_0 = -ka$ in $f = (1/k)e^{i\delta_0}\sin\delta_0$ and taking $k \to 0$ gives $f \to -a$ and $\sigma = 4\pi|f|^2 \to 4\pi a^2$. The sign and magnitude of $a$ follow from the zero-energy radial equation: outside the potential $u_0$ is linear, $u_0(r) \propto (r - a)$, so $a$ is the intercept where the extrapolated wavefunction crosses zero — positive for a node outside the range (effectively repulsive or a bound state), negative for an attractive virtual state. For a resonance, expanding the phase near $E_R$ as $\cot\delta_\ell \approx -2(E - E_R)/\Gamma$ yields $\sin^2\delta_\ell = (\Gamma/2)^2/[(E - E_R)^2 + (\Gamma/2)^2]$, so

$$ \sigma_\ell = \frac{4\pi}{k^2}(2\ell+1)\, \frac{(\Gamma/2)^2}{(E - E_R)^2 + (\Gamma/2)^2}. $$

At $E = E_R$ the cross section reaches the **unitarity limit** $\sigma_\ell^\text{max} = (4\pi/k^2)(2\ell+1)$. Derivations D and E give the details.

**演示。** 将 $\delta_0 = -ka$ 代入 $f = (1/k)e^{i\delta_0}\sin\delta_0$ 并取 $k \to 0$，得 $f \to -a$，$\sigma = 4\pi|f|^2 \to 4\pi a^2$。$a$ 的符号与大小来自零能径向方程：势外 $u_0$ 为线性，$u_0(r) \propto (r - a)$，故 $a$ 是外推波函数过零的截距——节点在射程外则 $a > 0$（等效排斥或束缚态），吸引虚态则 $a < 0$。对共振，将 $E_R$ 附近的相移展开为 $\cot\delta_\ell \approx -2(E - E_R)/\Gamma$，得 $\sin^2\delta_\ell = (\Gamma/2)^2/[(E - E_R)^2 + (\Gamma/2)^2]$，故 $\sigma_\ell = \dfrac{4\pi}{k^2}(2\ell+1)\dfrac{(\Gamma/2)^2}{(E - E_R)^2 + (\Gamma/2)^2}$。在 $E = E_R$ 处截面达到**幺正极限** $\sigma_\ell^\text{max} = (4\pi/k^2)(2\ell+1)$。详见推导 D、E。

**Application.** The scattering length governs ultracold atomic physics: near a **Feshbach resonance** $a$ is tuned through $\pm\infty$ with a magnetic field, switching the effective interaction between attractive and repulsive and enabling Bose–Einstein condensates and the BEC–BCS crossover. Breit–Wigner resonances are ubiquitous: slow-neutron capture cross sections in nuclear reactors, the $\Delta(1232)$ baryon resonance in pion–nucleon scattering, and unstable particles in high-energy physics (Modules 6.8, 8.9), where the resonance width $\Gamma$ is inversely the lifetime $\tau = \hbar/\Gamma$. The same low-energy s-wave machinery underlies the central-potential bound-state problem of Module 3.4 (spherical harmonics and radial equations).

**应用。** 散射长度支配超冷原子物理：在 **Feshbach 共振**附近，用磁场可将 $a$ 调过 $\pm\infty$，在吸引与排斥之间切换有效相互作用，从而实现玻色-爱因斯坦凝聚与 BEC–BCS 渡越。Breit–Wigner 共振无处不在：核反应堆中慢中子俘获截面、$\pi$-核子散射中的 $\Delta(1232)$ 重子共振，以及高能物理中的不稳定粒子（模块 6.8、8.9），其中共振宽度 $\Gamma$ 与寿命互为倒数 $\tau = \hbar/\Gamma$。同样的低能 s 波机制是模块 3.4 中心势束缚态问题（球谐函数与径向方程）的基础。

---

**Self-test (blank page)**

1. Write the asymptotic form of the stationary scattering state and identify the scattering amplitude $f(\theta)$.
2. Starting from the probability current, derive $d\sigma/d\Omega = |f(\theta)|^2$.
3. Define the phase shift $\delta_\ell$ and write the partial-wave expansion of $f(\theta)$; from it obtain $\sigma = (4\pi/k^2) \sum_\ell (2\ell+1) \sin^2\delta_\ell$.
4. State and prove the optical theorem $\sigma_\text{tot} = (4\pi/k)\, \text{Im}\, f(0)$.

**自测（空白页）**

1. 写出定态散射态的渐近形式并指明散射振幅 $f(\theta)$。
2. 从概率流出发，推导 $d\sigma/d\Omega = |f(\theta)|^2$。
3. 定义相移 $\delta_\ell$ 并写出 $f(\theta)$ 的分波展开；由此得到 $\sigma = (4\pi/k^2) \sum_\ell (2\ell+1) \sin^2\delta_\ell$。
4. 陈述并证明光学定理 $\sigma_\text{tot} = (4\pi/k)\, \text{Im}\, f(0)$。

---

← Previous: [Module 3.17 — Quantum Algorithms & Error Correction](./module-3.17-quantum-algorithms-and-error-correction.md) · [Phase 3 index](./README.md)

# Module 3.18 — Quantum Scattering Theory
**模块 3.18 — 量子散射理论**

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 3 阶段 — 量子力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-3.18-quantum-scattering-theory-derivations.md)

---

## 1. Scattering Amplitude and Cross Section · 散射振幅与截面

**Definition.** A scattering experiment sends a steady beam of particles of definite energy E = ℏ²k²/2m onto a localized target potential V(r) and counts how many emerge into each solid angle. The stationary scattering state is the energy eigenstate whose asymptotic form (far from the target, where V → 0) is a plane wave plus an outgoing spherical wave:

  ψ(r) → e^{ikz} + f(θ) e^{ikr}/r,   as r → ∞.

The coefficient **f(θ)** is the **scattering amplitude**; it carries all the physics of the collision and has the dimension of length. The **differential cross section** dσ/dΩ is defined as the number of particles scattered per unit time into solid angle dΩ, divided by the incident flux (particles per unit area per unit time). It is the effective area the target presents for scattering into that direction.

**定义。** 散射实验将一束能量确定 E = ℏ²k²/2m 的稳定粒子流射向局域靶势 V(r)，并计数射入每个立体角的粒子数。定态散射态是能量本征态，其渐近形式（远离靶、V → 0 处）为平面波加出射球面波：

  ψ(r) → e^{ikz} + f(θ) e^{ikr}/r，   当 r → ∞。

系数 **f(θ)** 称为**散射振幅**；它承载碰撞的全部物理信息，量纲为长度。**微分截面** dσ/dΩ 定义为单位时间散射进立体角 dΩ 的粒子数除以入射通量（单位面积单位时间的粒子数），即靶在该方向上呈现的有效散射面积。

**Demonstration.** The cross section follows from the quantum probability current j = (ℏ/m) Im(ψ* ∇ψ). The incident plane wave e^{ikz} carries flux j_inc = ℏk/m along z. The outgoing spherical wave f(θ)e^{ikr}/r carries a radial flux j_scatt = (ℏk/m)|f(θ)|²/r². The number scattered into dΩ per unit time is j_scatt · r² dΩ, and dividing by j_inc gives the central result:

  dσ/dΩ = |f(θ)|²,   σ = ∫ |f(θ)|² dΩ.

The 1/r² in the flux cancels the r² in the area element r²dΩ, which is precisely why the spherical wave is normalized as f(θ)e^{ikr}/r — it guarantees a finite, r-independent cross section. The full derivation is in **Derivation A**.

**演示。** 截面由量子概率流 j = (ℏ/m) Im(ψ* ∇ψ) 给出。入射平面波 e^{ikz} 沿 z 方向携带通量 j_inc = ℏk/m。出射球面波 f(θ)e^{ikr}/r 携带径向通量 j_scatt = (ℏk/m)|f(θ)|²/r²。单位时间散射进 dΩ 的粒子数为 j_scatt · r² dΩ，除以 j_inc 即得核心结果 dσ/dΩ = |f(θ)|²，σ = ∫ |f(θ)|² dΩ。通量中的 1/r² 恰好抵消面元 r²dΩ 中的 r²，这正是球面波归一化为 f(θ)e^{ikr}/r 的原因——它保证截面有限且不依赖 r。完整推导见**推导 A**。

**Application.** The scattering amplitude is the experimental bridge between theory and measurement: detectors measure dσ/dΩ directly, and inverting it constrains the potential V(r). Two complementary methods compute f(θ). The **Born approximation** (Module 3.8) treats V as a weak perturbation and works best at high energy, giving f(θ) ∝ the Fourier transform of V; the **partial-wave method** (Section 2) is exact and works best at low energy. For a pure Coulomb potential the quantum f(θ) reproduces exactly the classical **Rutherford cross section** (Module 1.21), one of the rare cases where the classical and quantum differential cross sections coincide.

**应用。** 散射振幅是理论与测量之间的实验桥梁：探测器直接测量 dσ/dΩ，反演它即可约束势 V(r)。计算 f(θ) 有两种互补方法。**玻恩近似**（模块 3.8）将 V 视为弱微扰，在高能下最佳，给出 f(θ) 正比于 V 的傅里叶变换；**分波法**（第 2 节）精确且在低能下最佳。对纯库仑势，量子 f(θ) 精确重现经典的**卢瑟福截面**（模块 1.21），这是经典与量子微分截面罕见的重合情形之一。

---

## 2. Partial Waves, Phase Shifts, and the Optical Theorem · 分波、相移与光学定理

**Definition.** For a **central potential** V(r), angular momentum is conserved, so the scattering problem separates in spherical coordinates and each angular-momentum channel ℓ scatters independently. The full effect of the potential on channel ℓ is encoded in a single real number, the **phase shift δ_ℓ(k)**: far from the target the radial wavefunction u_ℓ(r) = r R_ℓ(r) behaves as

  u_ℓ(r) → sin(kr − ℓπ/2 + δ_ℓ),   as r → ∞,

i.e. it is the free spherical Bessel solution shifted in phase by δ_ℓ relative to the no-potential case. An attractive potential pulls the wave inward (δ_ℓ > 0); a repulsive one pushes it out (δ_ℓ < 0). All observables are built from the set {δ_ℓ}.

**定义。** 对**中心势** V(r)，角动量守恒，故散射问题在球坐标中分离，每个角动量通道 ℓ 独立散射。势对通道 ℓ 的全部作用被编码进一个实数——**相移 δ_ℓ(k)**：远离靶处，径向波函数 u_ℓ(r) = r R_ℓ(r) 表现为 u_ℓ(r) → sin(kr − ℓπ/2 + δ_ℓ)，即相对无势情形，它是自由球贝塞尔解平移了相位 δ_ℓ。吸引势把波拉向内（δ_ℓ > 0），排斥势把波推向外（δ_ℓ < 0）。所有可观测量都由集合 {δ_ℓ} 构造。

**Demonstration.** Expanding both the incident plane wave and the scattering state in Legendre polynomials P_ℓ(cos θ) and matching the asymptotic forms term by term expresses the amplitude entirely through phase shifts:

  f(θ) = (1/k) Σ_{ℓ=0}^∞ (2ℓ+1) e^{iδ_ℓ} sin δ_ℓ P_ℓ(cos θ).

Integrating |f(θ)|² over all angles with the orthogonality relation ∫ P_ℓ P_{ℓ'} dΩ = [4π/(2ℓ+1)] δ_{ℓℓ'} collapses the double sum to a single sum, giving the **total cross section**:

  σ = (4π/k²) Σ_ℓ (2ℓ+1) sin² δ_ℓ.

Evaluating f at θ = 0, where every P_ℓ(1) = 1, isolates the imaginary part Im f(0) = (1/k) Σ_ℓ (2ℓ+1) sin² δ_ℓ, which is exactly (k/4π)σ. This is the **optical theorem**:

  σ_tot = (4π/k) Im f(0).

Derivations B and C give the full proofs.

**演示。** 将入射平面波与散射态都用勒让德多项式 P_ℓ(cos θ) 展开，并逐项匹配渐近形式，可将振幅完全用相移表示：f(θ) = (1/k) Σ_{ℓ=0}^∞ (2ℓ+1) e^{iδ_ℓ} sin δ_ℓ P_ℓ(cos θ)。利用正交关系 ∫ P_ℓ P_{ℓ'} dΩ = [4π/(2ℓ+1)] δ_{ℓℓ'} 对全角度积分 |f(θ)|²，双重求和坍缩为单重求和，得**总截面** σ = (4π/k²) Σ_ℓ (2ℓ+1) sin² δ_ℓ。在 θ = 0 处（每个 P_ℓ(1) = 1）取虚部得 Im f(0) = (1/k) Σ_ℓ (2ℓ+1) sin² δ_ℓ，恰为 (k/4π)σ。这就是**光学定理** σ_tot = (4π/k) Im f(0)。完整证明见推导 B、C。

**Application.** Partial waves are the method of choice at low energy, where only a few ℓ contribute: a particle of wavenumber k and impact parameter b ≈ ℓ/k cannot reach a short-range potential of range a unless ℓ ≲ ka, so for ka ≪ 1 only the ℓ = 0 (s-wave) term survives. The optical theorem is a statement of **flux conservation (unitarity)**: the total flux removed from the forward beam (σ_tot) equals the forward-amplitude interference encoded in Im f(0). At high energy the S-matrix formulation (Modules 6.8, 8.9) generalizes phase shifts to inelastic and relativistic channels, with e^{2iδ_ℓ} becoming the diagonal S-matrix element.

**应用。** 分波法是低能下的首选方法，此时只有少数 ℓ 有贡献：波数 k、碰撞参数 b ≈ ℓ/k 的粒子无法到达射程为 a 的短程势，除非 ℓ ≲ ka，故当 ka ≪ 1 时只剩 ℓ = 0（s 波）项。光学定理是**通量守恒（幺正性）**的陈述：从前向束流中移除的总通量（σ_tot）等于 Im f(0) 所编码的前向振幅干涉。在高能下，S 矩阵形式（模块 6.8、8.9）将相移推广到非弹性与相对论通道，e^{2iδ_ℓ} 成为对角 S 矩阵元。

---

## 3. Scattering Length and Resonances · 散射长度与共振

**Definition.** At very low energy (k → 0) the s-wave dominates and its phase shift behaves linearly, δ_0(k) → −ka, defining the **scattering length a**, a single length that characterizes the whole low-energy interaction. The amplitude tends to a constant f → −a, the scattering becomes isotropic, and the cross section approaches σ → 4πa². A **resonance** is the opposite, sharply energy-dependent regime: when a quasi-bound state exists at energy E_R with width Γ, the phase shift δ_ℓ sweeps rapidly through π/2, and the partial cross section traces a **Breit–Wigner** peak.

**定义。** 在极低能（k → 0）下，s 波主导，其相移线性变化 δ_0(k) → −ka，定义**散射长度 a**——刻画整个低能相互作用的单一长度。振幅趋于常数 f → −a，散射变为各向同性，截面趋于 σ → 4πa²。**共振**则是相反的、强烈依赖能量的区域：当能量 E_R 处存在宽度为 Γ 的准束缚态时，相移 δ_ℓ 迅速扫过 π/2，分波截面描出 **Breit–Wigner** 峰。

**Demonstration.** Setting δ_0 = −ka in f = (1/k)e^{iδ_0}sin δ_0 and taking k → 0 gives f → −a and σ = 4π|f|² → 4πa². The sign and magnitude of a follow from the zero-energy radial equation: outside the potential u_0 is linear, u_0(r) ∝ (r − a), so a is the intercept where the extrapolated wavefunction crosses zero — positive for a node outside the range (effectively repulsive or a bound state), negative for an attractive virtual state. For a resonance, expanding the phase near E_R as cot δ_ℓ ≈ −2(E − E_R)/Γ yields sin² δ_ℓ = (Γ/2)²/[(E − E_R)² + (Γ/2)²], so

  σ_ℓ = (4π/k²)(2ℓ+1) (Γ/2)² / [(E − E_R)² + (Γ/2)²].

At E = E_R the cross section reaches the **unitarity limit** σ_ℓ^max = (4π/k²)(2ℓ+1). Derivations D and E give the details.

**演示。** 将 δ_0 = −ka 代入 f = (1/k)e^{iδ_0}sin δ_0 并取 k → 0，得 f → −a，σ = 4π|f|² → 4πa²。a 的符号与大小来自零能径向方程：势外 u_0 为线性，u_0(r) ∝ (r − a)，故 a 是外推波函数过零的截距——节点在射程外则 a > 0（等效排斥或束缚态），吸引虚态则 a < 0。对共振，将 E_R 附近的相移展开为 cot δ_ℓ ≈ −2(E − E_R)/Γ，得 sin² δ_ℓ = (Γ/2)²/[(E − E_R)² + (Γ/2)²]，故 σ_ℓ = (4π/k²)(2ℓ+1)(Γ/2)²/[(E − E_R)² + (Γ/2)²]。在 E = E_R 处截面达到**幺正极限** σ_ℓ^max = (4π/k²)(2ℓ+1)。详见推导 D、E。

**Application.** The scattering length governs ultracold atomic physics: near a **Feshbach resonance** a is tuned through ±∞ with a magnetic field, switching the effective interaction between attractive and repulsive and enabling Bose–Einstein condensates and the BEC–BCS crossover. Breit–Wigner resonances are ubiquitous: slow-neutron capture cross sections in nuclear reactors, the Δ(1232) baryon resonance in pion–nucleon scattering, and unstable particles in high-energy physics (Modules 6.8, 8.9), where the resonance width Γ is inversely the lifetime τ = ℏ/Γ. The same low-energy s-wave machinery underlies the central-potential bound-state problem of Module 3.4 (spherical harmonics and radial equations).

**应用。** 散射长度支配超冷原子物理：在 **Feshbach 共振**附近，用磁场可将 a 调过 ±∞，在吸引与排斥之间切换有效相互作用，从而实现玻色-爱因斯坦凝聚与 BEC–BCS 渡越。Breit–Wigner 共振无处不在：核反应堆中慢中子俘获截面、π-核子散射中的 Δ(1232) 重子共振，以及高能物理中的不稳定粒子（模块 6.8、8.9），其中共振宽度 Γ 与寿命互为倒数 τ = ℏ/Γ。同样的低能 s 波机制是模块 3.4 中心势束缚态问题（球谐函数与径向方程）的基础。

---

**Self-test (blank page)**

1. Write the asymptotic form of the stationary scattering state and identify the scattering amplitude f(θ).
2. Starting from the probability current, derive dσ/dΩ = |f(θ)|².
3. Define the phase shift δ_ℓ and write the partial-wave expansion of f(θ); from it obtain σ = (4π/k²) Σ_ℓ (2ℓ+1) sin² δ_ℓ.
4. State and prove the optical theorem σ_tot = (4π/k) Im f(0).

**自测（空白页）**

1. 写出定态散射态的渐近形式并指明散射振幅 f(θ)。
2. 从概率流出发，推导 dσ/dΩ = |f(θ)|²。
3. 定义相移 δ_ℓ 并写出 f(θ) 的分波展开；由此得到 σ = (4π/k²) Σ_ℓ (2ℓ+1) sin² δ_ℓ。
4. 陈述并证明光学定理 σ_tot = (4π/k) Im f(0)。

---

← Previous: [Module 3.17 — Quantum Algorithms & Error Correction](./module-3.17-quantum-algorithms-and-error-correction.md) · [Phase 3 index](./README.md)

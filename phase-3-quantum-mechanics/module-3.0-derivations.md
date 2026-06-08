# Derivations — Module 3.0: Old Quantum Theory & the Photoelectric Effect
# 推导 — 模块 3.0：旧量子论与光电效应

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.0](./module-3.0-old-quantum-theory-and-photoelectric-effect.md). Full step-by-step proofs of every non-trivial result quoted there. English first, then 中文.
> [模块 3.0](./module-3.0-old-quantum-theory-and-photoelectric-effect.md) 的配套文档：对该模块所引用每个非平凡结果的完整逐步证明。先英文，后中文。

---

## A. Photoelectric Effect: KE_max = hν − W and the Stopping-Voltage Line · 光电效应：KE_max = hν − W 与截止电压直线

**Claim.** When light of frequency ν strikes a metal with work function W, the maximum kinetic energy of ejected electrons is KE_max = hν − W, and the stopping voltage V_stop satisfies e V_stop = hν − W — a straight line in ν with slope h/e and y-intercept −W/e.

**命题。** 当频率为 ν 的光照射逸出功为 W 的金属时，被射出电子的最大动能为 KE_max = hν − W，截止电压 V_stop 满足 e V_stop = hν − W——这是关于 ν 的一条直线，斜率为 h/e，纵截距为 −W/e。

**Step 1 — Einstein's photon hypothesis.** Model light of frequency ν as a stream of photons, each carrying energy E_photon = hν. This is a postulate; its self-consistency is confirmed by what follows.

**第 1 步 — 爱因斯坦光子假说。** 将频率为 ν 的光建模为光子流，每个光子携带能量 E_photon = hν。这是一个假设；其自洽性由以下推导得到验证。

**Step 2 — Energy accounting for one absorption event.** When a single photon is absorbed by a conduction electron inside the metal, all of the photon's energy hν is transferred to that one electron (photons are absorbed whole, not split). The electron must then overcome the binding energy W (the minimum energy needed to escape the metal surface — the work function). After escaping, the electron has kinetic energy

**第 2 步 — 单次吸收事件的能量守恒。** 当一个光子被金属内的传导电子吸收时，光子的全部能量 hν 转移给该电子（光子被整体吸收，不可分割）。电子随后必须克服结合能 W（逃离金属表面所需的最小能量——逸出功）。逃逸后，电子的动能为

  KE = hν − W − (extra binding energy of that electron's initial position).

  KE = hν − W − （该电子初始位置的额外结合能）。

**Step 3 — Maximizing the kinetic energy.** Electrons at the top of the conduction band (i.e., those with the smallest additional binding energy, which is zero by definition of the work function) escape with the maximum kinetic energy:

**第 3 步 — 最大化动能。** 处于导带顶部的电子（即额外结合能最小为零的电子，这正是逸出功的定义）以最大动能逃逸：

  **KE_max = hν − W**.

This is zero when hν = W (the threshold frequency ν₀ = W/h). For hν < W no electron escapes at all, regardless of intensity — because one electron absorbs one photon and that single quantum of energy is insufficient. This explains why a dim ultraviolet source ejects electrons while a bright red source does not.

当 hν = W 时此值为零（阈值频率 ν₀ = W/h）。当 hν < W 时无论光强多大都没有电子逸出——因为一个电子吸收一个光子，而那单个能量子不足以使其逃脱。这就解释了为何微弱紫外光能射出电子而强烈红光却不能。

**Step 4 — The stopping voltage.** Apply a retarding potential V_stop (the collector is negative relative to the emitter). The electric field does negative work −eV_stop on the electron as it travels from emitter to collector. The fastest electrons (those with KE_max) are just stopped when all their kinetic energy has been converted to electrical potential energy:

**第 4 步 — 截止电压。** 施加反向截止电位 V_stop（收集极相对于发射极为负极）。电场对电子做负功 −eV_stop。当最快电子（具有 KE_max 的电子）的全部动能转化为电势能时，它们恰好被截止：

  KE_max = e V_stop.

Substituting KE_max:

代入 KE_max：

  e V_stop = hν − W,

  V_stop = (h/e) ν − W/e.

**Step 5 — Interpretation of the line.** This is a linear function of ν: slope h/e is universal (independent of the metal), and the y-intercept −W/e depends on the material. Plotting V_stop vs ν gives a straight line; the slope yields h directly, confirming Planck's constant from a completely different experiment. The x-intercept ν₀ = W/h is the threshold. ∎

**第 5 步 — 直线的解释。** 这是关于 ν 的线性函数：斜率 h/e 是普适的（与金属无关），纵截距 −W/e 取决于材料。绘出 V_stop 对 ν 的图像为一条直线；斜率直接给出 h，从一个完全不同的实验中证实了普朗克常数。横截距 ν₀ = W/h 是阈值频率。∎

---

## B. Bohr Hydrogen Atom: Energies Eₙ = −13.6 eV / n² · 玻尔氢原子：能量 Eₙ = −13.6 eV / n²

**Claim.** For the hydrogen atom, combining the Coulomb force law with Bohr's angular-momentum quantization postulate L = nℏ yields circular-orbit energies Eₙ = −me⁴/(2ℏ²n²) = −13.6 eV / n².

**命题。** 对于氢原子，将库仑力定律与玻尔角动量量子化假设 L = nℏ 结合，得到圆形轨道能量 Eₙ = −me⁴/(2ℏ²n²) = −13.6 eV / n²。

**Step 1 — Setup and notation.** Consider an electron (mass m, charge −e) orbiting a proton (charge +e, assumed infinitely massive) in a circular orbit of radius r with speed v. We use SI units: the Coulomb constant k_e = 1/(4πε₀). The Coulomb force provides the centripetal acceleration:

**第 1 步 — 建立符号与方程。** 考虑质量为 m、电荷为 −e 的电子在半径为 r、速度为 v 的圆轨道上绕质量无穷大的质子（电荷 +e）运动。使用SI单位制：库仑常数 k_e = 1/(4πε₀)。库仑力提供向心加速度：

  k_e e² / r² = m v² / r.    … (1)

**Step 2 — Apply Bohr's quantization postulate.** Bohr postulated that only orbits with angular momentum equal to an integer multiple of ℏ are allowed:

**第 2 步 — 应用玻尔量子化假设。** 玻尔假设只有角动量等于 ℏ 整数倍的轨道才被允许：

  L = m v r = nℏ,   n = 1, 2, 3, …    … (2)

**Step 3 — Solve for v and r in terms of n.** From (2): v = nℏ/(mr). Substitute into (1):

**第 3 步 — 用 n 表示 v 和 r。** 由 (2)：v = nℏ/(mr)。代入 (1)：

  k_e e² / r² = m v² / r = m (nℏ)² / (m²r² · r) = n²ℏ²/(mr³).

Multiply both sides by r³:

两边乘以 r³：

  k_e e² r = n²ℏ²/m.

  r = n²ℏ² / (m k_e e²) = n² a₀,

where **a₀ = ℏ²/(m k_e e²) ≈ 0.529 Å** is the **Bohr radius**. So rₙ = n²a₀ — the radius grows as n².

其中 **a₀ = ℏ²/(m k_e e²) ≈ 0.529 Å** 是**玻尔半径**。因此 rₙ = n²a₀——半径随 n² 增大。

From v = nℏ/(mr):

由 v = nℏ/(mr)：

  vₙ = nℏ / (m · n²a₀) = ℏ/(mna₀) = k_e e²/(nℏ).

**Step 4 — Compute the total energy.** The total mechanical energy is kinetic plus potential:

**第 4 步 — 计算总能量。** 总机械能为动能加势能：

  E = ½mv² − k_e e²/r.

From (1): k_e e²/r = mv², so the kinetic energy is ½mv² = ½ k_e e²/r, and:

由 (1)：k_e e²/r = mv²，故动能为 ½mv² = ½ k_e e²/r，从而：

  E = ½ k_e e²/r − k_e e²/r = −½ k_e e²/r.

This is the **virial theorem** for a 1/r potential: E_total = −½|V|. Now substitute rₙ = n²a₀:

这是 1/r 势的**位力定理**：E_total = −½|V|。代入 rₙ = n²a₀：

  Eₙ = −½ k_e e²/(n²a₀) = −½ k_e e² · m k_e e²/(n²ℏ²) = −m k_e² e⁴/(2n²ℏ²).

**Step 5 — Evaluate numerically.** The ground-state energy (n = 1) is the Rydberg energy:

**第 5 步 — 数值计算。** 基态能量（n = 1）为里德伯能量：

  E₁ = −m k_e² e⁴ / (2ℏ²).

Using m = 9.109 × 10⁻³¹ kg, k_e = 8.988 × 10⁹ N·m²/C², e = 1.602 × 10⁻¹⁹ C, ℏ = 1.055 × 10⁻³⁴ J·s:

  E₁ = −2.179 × 10⁻¹⁸ J = −13.6 eV.

Therefore:

因此：

  **Eₙ = −13.6 eV / n²**,   n = 1, 2, 3, …

Spectral lines arise from transitions between levels: hν = Eₙ − Eₘ (m < n), giving the Rydberg formula. ∎

谱线来自能级跃迁：hν = Eₙ − Eₘ（m < n），给出里德伯公式。∎

---

## C. Compton Scattering: Δλ = (h/mc)(1 − cosθ) · 康普顿散射：Δλ = (h/mc)(1 − cosθ)

**Claim.** When a photon scatters off a free electron initially at rest, the photon's wavelength shifts by Δλ = λ′ − λ = (h/mc)(1 − cosθ), where θ is the photon's scattering angle and h/mc is the **Compton wavelength** λ_C ≈ 2.426 pm.

**命题。** 当光子从静止的自由电子上散射时，光子的波长偏移为 Δλ = λ′ − λ = (h/mc)(1 − cosθ)，其中 θ 为光子散射角，h/mc 为**康普顿波长** λ_C ≈ 2.426 pm。

**Step 1 — Assign four-momenta.** Use relativistic mechanics. Photon has energy E = hν = hc/λ and momentum p = h/λ (magnitude). Electron starts at rest: energy mc², momentum 0. Let the photon scatter at angle θ and the electron recoil at angle φ. Define:

**第 1 步 — 指定四动量。** 使用相对论力学。光子能量 E = hν = hc/λ，动量大小 p = h/λ。电子初始静止：能量 mc²，动量为零。设光子散射角为 θ，电子反冲角为 φ。定义：

  Initial photon:   energy hc/λ,  x-momentum h/λ,  y-momentum 0.
  Initial electron: energy mc²,   x-momentum 0,    y-momentum 0.
  Final photon:     energy hc/λ′, x-momentum (h/λ′)cosθ, y-momentum (h/λ′)sinθ.
  Final electron:   energy E_e,   x-momentum p_e cosφ,   y-momentum −p_e sinφ.

**Step 2 — Conservation laws.** Energy conservation:

**第 2 步 — 守恒定律。** 能量守恒：

  hc/λ + mc² = hc/λ′ + E_e.    … (i)

x-momentum conservation:

x 方向动量守恒：

  h/λ = (h/λ′)cosθ + p_e cosφ.    … (ii)

y-momentum conservation:

y 方向动量守恒：

  0 = (h/λ′)sinθ − p_e sinφ.    … (iii)

**Step 3 — Eliminate the electron variables.** Isolate the electron momentum components from (ii) and (iii):

**第 3 步 — 消去电子变量。** 从 (ii) 和 (iii) 中分离出电子动量分量：

  p_e cosφ = h/λ − (h/λ′)cosθ,
  p_e sinφ = (h/λ′)sinθ.

Square and add to eliminate φ:

平方相加以消去 φ：

  p_e² = (h/λ)² − 2(h/λ)(h/λ′)cosθ + (h/λ′)².    … (iv)

From energy conservation (i): E_e = hc/λ − hc/λ′ + mc². Use the relativistic energy–momentum relation E_e² = (p_e c)² + (mc²)²:

由能量守恒 (i)：E_e = hc/λ − hc/λ′ + mc²。利用相对论能量–动量关系 E_e² = (p_e c)² + (mc²)²：

  (hc/λ − hc/λ′ + mc²)² = (p_e c)² + (mc²)².

Expand the left side:

展开左边：

  (hc/λ − hc/λ′)² + 2mc²(hc/λ − hc/λ′) + (mc²)² = (p_e c)² + (mc²)².

The (mc²)² cancels:

(mc²)² 消去：

  (hc/λ − hc/λ′)² + 2mc²(hc/λ − hc/λ′) = (p_e c)².

Divide by c²:

除以 c²：

  (h/λ − h/λ′)² + 2mc(h/λ − h/λ′) = p_e².    … (v)

**Step 4 — Equate the two expressions for p_e².** From (iv) and (v):

**第 4 步 — 联立 p_e² 的两个表达式。** 由 (iv) 与 (v)：

  (h/λ)² − 2(h/λ)(h/λ′)cosθ + (h/λ′)² = (h/λ − h/λ′)² + 2mc(h/λ − h/λ′).

Expand the right side: (h/λ)² − 2(h²/λλ′) + (h/λ′)² + 2mc(h/λ − h/λ′). The (h/λ)² and (h/λ′)² cancel from both sides:

展开右边：(h/λ)² − 2(h²/λλ′) + (h/λ′)² + 2mc(h/λ − h/λ′)。两边的 (h/λ)² 和 (h/λ′)² 消去：

  −2(h²/λλ′)cosθ = −2(h²/λλ′) + 2mc(h/λ − h/λ′).

Rearrange:

整理：

  2(h²/λλ′) − 2(h²/λλ′)cosθ = 2mc(h/λ − h/λ′).

  (h²/λλ′)(1 − cosθ) = mc · h(λ′ − λ)/(λλ′).

Multiply both sides by λλ′/(mch):

两边乘以 λλ′/(mch)：

  h(1 − cosθ)/mc = λ′ − λ.

Therefore:

因此：

  **Δλ = λ′ − λ = (h/mc)(1 − cosθ)**. ∎

**Step 5 — Properties.** The Compton wavelength λ_C = h/mc ≈ 2.426 × 10⁻¹² m. The shift Δλ depends only on the scattering angle θ, not on the initial wavelength — a purely particle-collision result. Maximum shift 2λ_C occurs at θ = 180° (backscattering). No shift at θ = 0° (forward scattering, no collision).

**第 5 步 — 性质。** 康普顿波长 λ_C = h/mc ≈ 2.426 × 10⁻¹² m。偏移 Δλ 仅取决于散射角 θ，与初始波长无关——这是纯粒子碰撞的结果。最大偏移 2λ_C 在 θ = 180°（反向散射）时发生。θ = 0°（前向散射，无碰撞）时无偏移。∎

---

## D. de Broglie Relation: λ = h/p · 德布罗意关系：λ = h/p

**Claim.** By symmetry with the photon, a matter particle of momentum p has an associated wavelength λ = h/p.

**命题。** 根据与光子的对称性，动量为 p 的物质粒子具有对应波长 λ = h/p。

**Step 1 — Photon relations as template.** For a photon: energy E = hν = hc/λ and momentum p = E/c = hν/c = h/λ. Equivalently, in terms of angular frequency ω = 2πν and wave vector k = 2π/λ:

**第 1 步 — 以光子关系为模板。** 对于光子：能量 E = hν = hc/λ，动量 p = E/c = hν/c = h/λ。等价地，用角频率 ω = 2πν 和波矢 k = 2π/λ 表示：

  E = ℏω,   p = ℏk.

**Step 2 — de Broglie's hypothesis.** de Broglie (1924) proposed that these same relations hold for massive particles. The motivation: Einstein had shown (special relativity + photon) that energy and momentum mix under Lorentz boosts, so both relations E = ℏω and p = ℏk must hold together, or neither. If a particle has a definite momentum p, then it has a definite wave vector k = p/ℏ and hence a wavelength:

**第 2 步 — 德布罗意假说。** 德布罗意（1924 年）提出这些相同的关系对有质量的粒子同样成立。动机：爱因斯坦已经表明（狭义相对论加光子）能量和动量在洛伦兹变换下混合，因此 E = ℏω 和 p = ℏk 这两个关系必须同时成立，或者都不成立。如果粒子有确定的动量 p，则它有确定的波矢 k = p/ℏ，从而有波长：

  **λ = 2π/k = 2πℏ/p = h/p**.

**Step 3 — Consistency with Bohr quantization.** If an electron's de Broglie wave must form a standing wave around a circular orbit of circumference 2πr, then an integer number of wavelengths must fit:

**第 3 步 — 与玻尔量子化的一致性。** 如果电子的德布罗意波必须在周长为 2πr 的圆形轨道上形成驻波，则必须有整数个波长容纳在其中：

  n λ = 2πr   ⟹   n(h/p) = 2πr   ⟹   pr = nℏ   ⟹   L = nℏ.

This reproduces Bohr's quantization postulate — it is not an independent assumption but follows from wave fitting. This retroactively justifies Bohr's rule. ∎

这重现了玻尔的量子化假设——它不是独立的假设，而是由波的配合条件推出的。这从回溯的角度为玻尔定则提供了合理性。∎

**Step 4 — Experimental confirmation.** Davisson–Germer (1927): an electron beam (accelerated through voltage V, giving p = √(2meV)) diffracts off a Ni crystal with lattice spacing d. The diffraction maxima obey Bragg's law d sinθ = nλ with λ = h/√(2meV) — confirmed to high precision.

**第 4 步 — 实验确认。** 戴维孙–革末实验（1927 年）：经电压 V 加速的电子束（动量 p = √(2meV)）从晶格间距为 d 的 Ni 晶体上衍射。衍射极大满足布拉格定律 d sinθ = nλ，其中 λ = h/√(2meV)——以高精度得到证实。∎

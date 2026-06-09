# Derivations — Module 1.12: Optics & Interference
# 推导 — 模块 1.12：光学与干涉

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.12](./module-1.12-optics-interference.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.12](./module-1.12-optics-interference.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Snell's Law from Fermat's Principle of Least Time · 从费马最短时间原理推导斯涅尔定律

**Claim.** For a ray travelling from point A in medium 1 (speed v₁) to point B in medium 2 (speed v₂), Fermat's principle (the actual path minimises travel time) yields Snell's law n₁ sin θ₁ = n₂ sin θ₂, where n = c/v is the refractive index.

**命题。** 对于从介质 1（速度 v₁）中点 A 到介质 2（速度 v₂）中点 B 的光线，费马原理（实际路径使传播时间最短）给出斯涅尔定律 n₁ sin θ₁ = n₂ sin θ₂，其中 n = c/v 为折射率。

**Step 1 — Set up the geometry.** Let the interface be horizontal at y = 0. Place A at (0, y₁) in medium 1 (perpendicular distance y₁ above the interface) and B at (d, −y₂) in medium 2 (perpendicular distance y₂ below), with y₁, y₂, d > 0. The ray crosses the interface at P = (x, 0), where x is the free parameter to optimise; the angles θ₁ (incidence) and θ₂ (refraction) are measured from the normal (the y-axis). The path lengths in each medium are:

**第 1 步 — 建立几何关系。** 设界面水平位于 y = 0。令 A 在介质 1 中位于 (0, y₁)（界面上方垂直距离 y₁），B 在介质 2 中位于 (d, −y₂)（界面下方垂直距离 y₂），y₁, y₂, d > 0。光线在 P = (x, 0) 穿过界面，x 为待优化的自由参数；入射角 θ₁ 与折射角 θ₂ 从法线（y 轴）量起。各介质中的路径长度为：

  l₁ = √(x² + y₁²)   (in medium 1),
  l₂ = √((d−x)² + y₂²)   (in medium 2).

**Step 2 — Write the travel time.** The total travel time is:

**第 2 步 — 写出传播时间。** 总传播时间为：

  T(x) = l₁/v₁ + l₂/v₂ = (1/v₁)√(x² + y₁²) + (1/v₂)√((d−x)² + y₂²).

**Step 3 — Minimise by setting dT/dx = 0.** Differentiating:

**第 3 步 — 令 dT/dx = 0 求极值。** 对 x 微分：

  dT/dx = x / (v₁ √(x² + y₁²)) + (−1)(d−x) / (v₂ √((d−x)² + y₂²)) = 0.

Identify the geometric terms: the angle of incidence θ₁ satisfies sin θ₁ = x / √(x² + y₁²), and the angle of refraction θ₂ satisfies sin θ₂ = (d−x) / √((d−x)² + y₂²). Therefore:

识别几何项：入射角 θ₁ 满足 sin θ₁ = x / √(x² + y₁²)，折射角 θ₂ 满足 sin θ₂ = (d−x) / √((d−x)² + y₂²)。因此：

  sin θ₁ / v₁ = sin θ₂ / v₂.

**Step 4 — Write in terms of refractive indices.** Using n = c/v, so 1/v = n/c:

**第 4 步 — 用折射率表示。** 利用 n = c/v，故 1/v = n/c：

  n₁ sin θ₁ / c = n₂ sin θ₂ / c   →   **n₁ sin θ₁ = n₂ sin θ₂.** ∎

**Step 5 — Verify it is a minimum (not maximum).** The second derivative d²T/dx² > 0 at the stationary point (the calculation shows d²T/dx² = y₁²/(v₁ l₁³) + y₂²/(v₂ l₂³) > 0), confirming the path is indeed a minimum time, consistent with Fermat's principle. (For reflection, the analogous calculation gives the law of reflection: θ_i = θ_r.)

**第 5 步 — 验证是极小值（而非极大值）。** 在驻点处二阶导数 d²T/dx² > 0（计算表明 d²T/dx² = y₁²/(v₁ l₁³) + y₂²/(v₂ l₂³) > 0），确认路径确实是最短时间，与费马原理一致。（对于反射，类似计算给出反射定律：θ_i = θ_r。）

---

## B. Two-Slit Interference — Constructive Maxima at d sin θ = mλ · 双缝干涉——d sin θ = mλ 处的相长极大

**Claim.** For two coherent slits separated by d, illuminated at normal incidence by wavelength λ, the intensity at angle θ is I(θ) = 4I₀ cos²(πd sin θ/λ), with maxima at d sin θ = mλ, m = 0, ±1, ±2, …

**命题。** 对于间距为 d 的两个相干缝，波长 λ 法线入射，角度 θ 处的强度为 I(θ) = 4I₀ cos²(πd sin θ/λ)，极大值在 d sin θ = mλ，m = 0, ±1, ±2, …

**Step 1 — Path difference.** Let the two slits be at y = +d/2 and y = −d/2. For a distant observation point P at angle θ (Fraunhofer limit: screen distance L ≫ d), the path difference between the two rays is:

**第 1 步 — 路程差。** 设两缝分别在 y = +d/2 和 y = −d/2。对于角度 θ 处的远处观察点 P（夫琅禾费极限：屏幕距离 L ≫ d），两条光线之间的路程差为：

  Δ = d sin θ.

(The derivation: the extra path length from slit 2 to P compared with slit 1 is the perpendicular distance from slit 1 to the ray from slit 2, which is d sin θ by simple geometry.)

（推导：从缝 2 到 P 与从缝 1 到 P 相比的额外路程，是从缝 1 到缝 2 射线的垂直距离，由简单几何关系为 d sin θ。）

**Step 2 — Phase difference and wave superposition.** The corresponding phase difference is:

**第 2 步 — 相位差与波叠加。** 相应的相位差为：

  δ = 2π Δ / λ = 2π d sin θ / λ.

The two coherent waves at P have equal amplitude E₀ and a relative phase δ. Their superposition (using complex notation and taking the real part):

P 处两列相干波振幅相等均为 E₀，相对相位差为 δ。它们的叠加（用复数表示并取实部）：

  E_total = E₀ e^{iωt} + E₀ e^{i(ωt + δ)} = E₀ e^{iωt} (1 + e^{iδ}) = E₀ e^{iωt} e^{iδ/2} · 2 cos(δ/2).

The amplitude of the resulting wave is 2E₀ cos(δ/2), and the intensity I ∝ |amplitude|²:

所得波的振幅为 2E₀ cos(δ/2)，强度 I ∝ |振幅|²：

  I(θ) = 4 I₀ cos²(δ/2) = 4 I₀ cos²(πd sin θ / λ),

where I₀ = ε₀ c E₀²/2 is the intensity from a single slit.

其中 I₀ = ε₀ c E₀²/2 是单缝强度。

**Step 3 — Maxima and minima.** Maxima: cos²(πd sin θ/λ) = 1, i.e. πd sin θ/λ = mπ:

**第 3 步 — 极大值与极小值。** 极大值：cos²(πd sin θ/λ) = 1，即 πd sin θ/λ = mπ：

  **d sin θ = mλ,**   m = 0, ±1, ±2, … (constructive interference / 相长干涉)

Minima: cos²(πd sin θ/λ) = 0, i.e. πd sin θ/λ = (m + ½)π:

极小值：cos²(πd sin θ/λ) = 0，即 πd sin θ/λ = (m + ½)π：

  **d sin θ = (m + ½)λ,**   m = 0, ±1, ±2, … (destructive interference / 相消干涉)

**Step 4 — Fringe spacing on a screen.** For small angles (sin θ ≈ θ ≈ y/L, where y is the position on a screen at distance L):

**第 4 步 — 屏幕上的条纹间距。** 对于小角度（sin θ ≈ θ ≈ y/L，其中 y 是距离 L 处屏幕上的位置）：

  y_m = mλL/d,   fringe spacing Δy = λL/d. ∎

---

## C. Single-Slit Diffraction as the Fourier Transform of the Aperture · 单缝衍射作为孔径的傅里叶变换

**Claim.** The far-field (Fraunhofer) diffraction amplitude from a slit of width a is proportional to the Fourier transform of the aperture function, giving intensity I(θ) = I₀ sinc²(a sin θ/λ).

**命题。** 宽度为 a 的缝的远场（夫琅禾费）衍射振幅正比于孔径函数的傅里叶变换，给出强度 I(θ) = I₀ sinc²(a sin θ/λ)。

**Step 1 — Huygens-Fresnel integral.** By Huygens' principle, each infinitesimal element dy′ of the slit at position y′ ∈ [−a/2, +a/2] acts as a secondary source of wavelets. At a distant point P at angle θ, the path from position y′ is longer (or shorter) by y′ sin θ compared with the path from the centre (y′ = 0). The total complex amplitude at P is the integral of these contributions:

**第 1 步 — 惠更斯–菲涅耳积分。** 由惠更斯原理，缝在位置 y′ ∈ [−a/2, +a/2] 处的每个无穷小元 dy′ 都是子波的次级波源。在角度 θ 处的远处点 P，位置 y′ 处的路径比中心（y′ = 0）处的路径长（或短）y′ sin θ。P 处的总复振幅是这些贡献的积分：

  E(θ) = (E₀/a) ∫_{−a/2}^{a/2} e^{i (2π/λ) y′ sin θ} dy′.

**Step 2 — This integral is a Fourier transform.** Define the spatial frequency k_x = (2π/λ) sin θ (the component of the wavevector along the slit direction). The aperture function for a uniform slit is f(y′) = 1 for y′ ∈ [−a/2, a/2] and 0 elsewhere. Then:

**第 2 步 — 此积分是傅里叶变换。** 定义空间频率 k_x = (2π/λ) sin θ（波矢量沿缝方向的分量）。均匀缝的孔径函数为 f(y′) = 1（y′ ∈ [−a/2, a/2]），其他处为 0。则：

  E(k_x) ∝ ∫_{−∞}^{∞} f(y′) e^{i k_x y′} dy′ = F̃(k_x),

the Fourier transform of the aperture function f. The far-field diffraction pattern is the squared modulus of the Fourier transform of the aperture: **I ∝ |F̃(k_x)|²**.

孔径函数 f 的傅里叶变换。远场衍射图样是孔径傅里叶变换的模的平方：**I ∝ |F̃(k_x)|²**。

**Step 3 — Evaluate the transform.** For the uniform slit:

**第 3 步 — 计算变换。** 对于均匀缝：

  E(θ) ∝ ∫_{−a/2}^{a/2} e^{i k_x y′} dy′ = [e^{i k_x y′} / (i k_x)]_{−a/2}^{a/2}
        = (e^{i k_x a/2} − e^{−i k_x a/2}) / (i k_x)
        = 2 sin(k_x a/2) / k_x
        = a · sinc(k_x a / (2π))   where sinc(u) = sin(πu)/(πu).

Substituting k_x = (2π/λ) sin θ:

代入 k_x = (2π/λ) sin θ：

  E(θ) ∝ a sinc(a sin θ / λ) = a sin(πa sin θ/λ) / (πa sin θ/λ).

Define β = πa sin θ/λ. Then E ∝ sin(β)/β and:

定义 β = πa sin θ/λ。则 E ∝ sin(β)/β，且：

  **I(θ) = I₀ (sin β / β)² = I₀ sinc²(a sin θ / λ),   sinc(u) = sin(πu)/(πu).** ∎

**Step 4 — Features of the pattern.** Central maximum at θ = 0 (β → 0, sinc → 1). First zeros at β = ±π, i.e. sin θ = ±λ/a: the central maximum has half-angular width λ/a (full width 2λ/a). Secondary maxima at β ≈ ±3π/2, ±5π/2, … with intensities approximately I₀/(3π/2)² ≈ 0.045 I₀, I₀/(5π/2)² ≈ 0.016 I₀, … — progressively weaker, consistent with the spreading of Fourier components.

**第 4 步 — 图样的特征。** θ = 0 处中央极大（β → 0，sinc → 1）。第一零点在 β = ±π，即 sin θ = ±λ/a：中央极大的半角宽度为 λ/a（全宽 2λ/a）。次极大在 β ≈ ±3π/2，±5π/2，… 处，强度约为 I₀/(3π/2)² ≈ 0.045 I₀，I₀/(5π/2)² ≈ 0.016 I₀，…——逐渐减弱，与傅里叶分量扩展一致。

---

## D. Diffraction Grating Condition · 衍射光栅条件

**Claim.** A grating of N slits with spacing d produces sharp principal maxima at d sin θ = mλ, m = 0, ±1, ±2, …, with intensity I = N²I₀ at the maxima.

**命题。** 间距为 d 的 N 缝光栅在 d sin θ = mλ，m = 0, ±1, ±2, … 处产生尖锐主极大，极大处强度为 I = N²I₀。

**Step 1 — Sum of N coherent waves.** The N slits contribute waves with equal amplitudes but with successive phase differences δ = 2πd sin θ / λ (the phase accumulated per slit spacing). Using the geometric series sum:

**第 1 步 — N 列相干波之和。** N 个缝贡献等振幅但依次相差相位 δ = 2πd sin θ / λ（每个缝间距积累的相位）的波。利用等比级数求和：

  E_total = E₀ Σ_{n=0}^{N−1} e^{i n δ} = E₀ (1 − e^{iNδ}) / (1 − e^{iδ}).

**Step 2 — Compute the intensity.** Taking the modulus squared:

**第 2 步 — 计算强度。** 取模的平方：

  I = |E_total|² = I₀ |1 − e^{iNδ}|² / |1 − e^{iδ}|²
    = I₀ [sin(Nδ/2)]² / [sin(δ/2)]².

Using the identity |1 − e^{iφ}|² = 4 sin²(φ/2):

利用恒等式 |1 − e^{iφ}|² = 4 sin²(φ/2)：

  **I(θ) = I₀ [sin(Nπd sin θ/λ)]² / [sin(πd sin θ/λ)]².**

**Step 3 — Principal maxima.** When d sin θ = mλ (m integer), the denominator sin(πd sin θ/λ) = sin(mπ) = 0. By L'Hôpital's rule (or by the small-angle limit), the ratio → N², so:

**第 3 步 — 主极大。** 当 d sin θ = mλ（m 为整数）时，分母 sin(πd sin θ/λ) = sin(mπ) = 0。由洛必达法则（或小角近似），比值 → N²，故：

  I_max = N² I₀.

These are the **principal maxima** (grating condition): **d sin θ = mλ.** ∎

这些是**主极大**（光栅条件）：**d sin θ = mλ。** ∎

**Step 4 — Resolving power.** Between successive principal maxima there are N − 1 zeros and N − 2 secondary maxima. The angular width of a principal maximum is Δθ ≈ λ/(Nd cos θ). The minimum resolvable wavelength difference (Rayleigh criterion: the principal maximum of λ + Δλ falls on the first zero of λ) gives the resolving power:

**第 4 步 — 分辨本领。** 相邻主极大之间有 N − 1 个零点和 N − 2 个次极大。主极大的角宽度为 Δθ ≈ λ/(Nd cos θ)。最小可分辨波长差（瑞利判据：λ + Δλ 的主极大落在 λ 的第一零点上）给出分辨本领：

  R = λ/Δλ = mN.

Higher grating orders m and more slits N both increase resolution.

更高的光栅阶次 m 和更多的缝数 N 都能提高分辨率。

---

*The Fourier connection established in Section C is the unifying theme: every diffraction and interference phenomenon is a Fourier analysis of the spatial distribution of sources. This connects to Fourier methods in Module 0.5, the quantum-mechanical interpretation of momentum eigenstates, and crystallographic structure determination.*

*C 节建立的傅里叶联系是统一主题：每一个衍射和干涉现象都是对波源空间分布的傅里叶分析。这与模块 0.5 的傅里叶方法、量子力学对动量本征态的诠释以及晶体结构测定相联系。*

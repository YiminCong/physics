# Module 7.6 — Cosmology
**模块 7.6 — 宇宙学**

> **Phase 7 — [General Relativity & Cosmology](./README.md)** · Format: Definition → Demonstration → Application
> **第 7 阶段 — 广义相对论与宇宙学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-7.6-cosmology-derivations.md)

---

## 1. The FLRW Metric and the Expanding Universe · FLRW 度规与膨胀宇宙

**Definition.** The *cosmological principle* asserts that the universe is, on the largest scales, spatially homogeneous (no preferred location) and isotropic (no preferred direction). The unique metric consistent with these symmetries is the *Friedmann–Lemaître–Robertson–Walker (FLRW) metric*:

**定义。** *宇宙学原理*断言，在最大尺度上，宇宙在空间上是均匀的（无优先位置）且各向同性的（无优先方向）。与这些对称性相容的唯一度规是*弗里德曼-勒梅特-罗伯逊-沃克（FLRW）度规*：

ds² = −c²dt² + a(t)² [ dr²/(1 − kr²) + r² dΩ² ]

where a(t) is the dimensionless *scale factor* (normalized to a(t₀) = 1 today), t is cosmic time, and k = +1, 0, −1 for a spatially closed, flat, or open universe respectively. Physical distances scale as d(t) = a(t) d_comoving. The recession velocity of a comoving object is v = ȧ d = H(t) d, where H(t) = ȧ/a is the *Hubble parameter*; today H₀ ≈ 67–73 km s⁻¹ Mpc⁻¹ (the "Hubble tension").

其中 a(t) 是无量纲*尺度因子*（今日归一化为 a(t₀) = 1），t 为宇宙时，k = +1, 0, −1 分别对应空间封闭、平坦或开放的宇宙。物理距离随尺度因子变化：d(t) = a(t) d_共动。共动天体的退行速度为 v = ȧ d = H(t) d，其中 H(t) = ȧ/a 为*哈勃参数*；今日 H₀ ≈ 67–73 km s⁻¹ Mpc⁻¹（"哈勃张力"）。

The *cosmological redshift* of light emitted at scale factor a_e and received at a_0 = 1 is z = 1/a_e − 1; it is a consequence of the expansion stretching photon wavelengths, not a Doppler shift in the usual sense.

在尺度因子 a_e 时发出、在 a_0 = 1 时接收的光的*宇宙学红移*为 z = 1/a_e − 1；这是膨胀拉伸光子波长的结果，而非通常意义上的多普勒效应。

**Demonstration.** Substituting the FLRW metric and a perfect-fluid Tμν (ρ, p) into the Einstein field equations (Module 7.4) yields the *Friedmann equations*:

**演示。** 将 FLRW 度规和完美流体 Tμν (ρ, p) 代入爱因斯坦场方程（模块 7.4），得到*弗里德曼方程*：

(ȧ/a)² = (8πG/3)ρ − kc²/a² + Λc²/3

ä/a = −(4πG/3)(ρ + 3p/c²) + Λc²/3

The first equation relates the expansion rate to the energy density, curvature, and cosmological constant. The second governs acceleration: ordinary matter and radiation (ρ + 3p/c² > 0) cause deceleration; Λ causes acceleration (effective p_Λ = −ρ_Λ c²). The *continuity equation* ρ̇ + 3H(ρ + p/c²) = 0 follows from ∇μ Tμν = 0.

第一个方程将膨胀率与能量密度、曲率和宇宙学常数联系起来。第二个方程控制加速度：普通物质和辐射（ρ + 3p/c² > 0）导致减速；Λ 导致加速（有效压强 p_Λ = −ρ_Λ c²）。*连续性方程* ρ̇ + 3H(ρ + p/c²) = 0 由 ∇μ Tμν = 0 导出。

Key solutions (k = 0, Λ = 0):
- *Matter dominated* (p = 0): a(t) ∝ t^{2/3}, ρ_m ∝ a⁻³
- *Radiation dominated* (p = ρc²/3): a(t) ∝ t^{1/2}, ρ_r ∝ a⁻⁴
- *Λ dominated* (ρ_Λ = Λc²/8πG = const): a(t) ∝ e^{Ht} (de Sitter expansion)

关键解（k = 0，Λ = 0）：
- *物质主导*（p = 0）：a(t) ∝ t^{2/3}，ρ_m ∝ a⁻³
- *辐射主导*（p = ρc²/3）：a(t) ∝ t^{1/2}，ρ_r ∝ a⁻⁴
- *Λ 主导*（ρ_Λ = Λc²/8πG = 常数）：a(t) ∝ e^{Ht}（德西特膨胀）

**Application.** The observed universe began in an extremely hot, dense state — the *Big Bang* — approximately t₀ ≈ 13.8 Gyr ago. The sequence of epochs: Planck era → inflation → radiation domination (quarks, leptons, nucleosynthesis) → matter domination (structure formation) → dark-energy domination (present accelerated expansion). The *cosmic microwave background* (CMB), emitted at recombination (z ≈ 1100, t ≈ 380 000 yr), is the earliest electromagnetic snapshot of the universe; its near-perfect blackbody spectrum at T₀ ≈ 2.725 K and tiny anisotropies (ΔT/T ∼ 10⁻⁵) encode the seeds of all large-scale structure.

**应用。** 可观测宇宙始于一个极热、极致密的状态——*大爆炸*——约在 t₀ ≈ 138 亿年前。各纪元的顺序为：普朗克纪元 → 暴胀 → 辐射主导（夸克、轻子、核合成）→ 物质主导（结构形成）→ 暗能量主导（当前加速膨胀）。*宇宙微波背景*（CMB）在复合时代（z ≈ 1100，t ≈ 38 万年）发射，是宇宙最早的电磁快照；其在 T₀ ≈ 2.725 K 下近乎完美的黑体谱和微小各向异性（ΔT/T ∼ 10⁻⁵）编码了所有大尺度结构的种子。

---

## 2. Dark Matter, Dark Energy, and the Fate of the Universe · 暗物质、暗能量与宇宙的命运

**Definition.** The energy budget of the universe (from CMB + baryon acoustic oscillations + supernovae) is:
- *Baryonic matter*: Ω_b ≈ 0.049 (atoms, stars, gas)
- *Cold dark matter* (CDM): Ω_c ≈ 0.265 — non-luminous, non-baryonic, gravitationally clustering matter inferred from galaxy rotation curves, gravitational lensing, and structure formation. Its particle identity is unknown (WIMPs, axions, and sterile neutrinos are leading candidates; see Module 8.6).
- *Dark energy* (Λ): Ω_Λ ≈ 0.685 — the energy of the quantum vacuum or a dynamical field (quintessence), driving the accelerated expansion discovered via Type Ia supernovae in 1998. Geometrically it enters as the cosmological constant Λ in the EFE (Module 7.4).

**定义。** 宇宙的能量构成（来自 CMB + 重子声学振荡 + 超新星数据）为：
- *重子物质*：Ω_b ≈ 0.049（原子、恒星、气体）
- *冷暗物质*（CDM）：Ω_c ≈ 0.265——非发光、非重子的引力成团物质，由星系旋转曲线、引力透镜和结构形成推断。其粒子身份未知（WIMP、轴子和惰性中微子是主要候选；见模块 8.6）。
- *暗能量*（Λ）：Ω_Λ ≈ 0.685——量子真空的能量或动力学场（精质），驱动 1998 年通过 Ia 型超新星发现的加速膨胀。在几何上，它作为宇宙学常数 Λ 进入 EFE（模块 7.4）。

The total Ω = Ω_b + Ω_c + Ω_Λ ≈ 1.000, implying k = 0: a spatially flat universe.

总密度参数 Ω = Ω_b + Ω_c + Ω_Λ ≈ 1.000，意味着 k = 0：空间平坦的宇宙。

**Demonstration.** Galaxy rotation curves: Newtonian gravity (Module 1.5) predicts orbital velocity v(r) = √(GM(r)/r) falling as r⁻¹/² beyond the visible disk. Observations show v(r) ≈ const ("flat rotation curves") to large r, implying M(r) ∝ r — an unseen *dark matter halo* extending far beyond the luminous galaxy. The required mass-to-light ratio is 5–10× the baryonic value.

**演示。** 星系旋转曲线：牛顿引力（模块 1.5）预言在可见盘以外轨道速度 v(r) = √(GM(r)/r) 以 r⁻¹/² 下降。观测显示 v(r) ≈ 常数（"平坦旋转曲线"）延伸至大 r 处，意味着 M(r) ∝ r——一个延伸远超发光星系的不可见*暗物质晕*。所需的质光比是重子值的 5–10 倍。

The Friedmann equation with Ω_m + Ω_Λ = 1 predicts deceleration (ä < 0) for Ω_Λ < Ω_m/2, and acceleration (ä > 0) otherwise. The transition to acceleration occurred at z ≈ 0.4 (about 5 Gyr ago). Future: continued exponential expansion; galaxies beyond the Local Group will eventually redshift out of causal contact (cosmological event horizon).

含 Ω_m + Ω_Λ = 1 的弗里德曼方程预测：当 Ω_Λ < Ω_m/2 时减速（ä < 0），否则加速（ä > 0）。加速膨胀的转变发生在 z ≈ 0.4（约 50 亿年前）。未来：持续指数膨胀；本星系群以外的星系最终将因红移而超出因果联系范围（宇宙学事件视界）。

**Application.**
- *Big Bang nucleosynthesis* (BBN, t ≈ 1–200 s): the baryon-to-photon ratio η fixes the primordial abundances of ¹H, ²H, ³He, ⁴He, ⁷Li. Agreement between BBN predictions and observations spanning nine orders of magnitude in abundance is one of the strongest tests of the hot Big Bang model.
- *Structure formation*: quantum fluctuations during inflation are stretched to macroscopic scales, seeding the CMB anisotropies that gravitationally collapse (with CDM providing the potential wells) into the cosmic web of filaments, voids, clusters, and galaxies.
- *Connection to particle physics*: the early universe at T ≳ 100 GeV probed physics at the electroweak scale and beyond (Module 8.6). Dark matter candidates, baryogenesis, and leptogenesis are active frontiers linking cosmology and the Standard Model.

**应用。**
- *大爆炸核合成*（BBN，t ≈ 1–200 s）：重子-光子比 η 决定了 ¹H、²H、³He、⁴He、⁷Li 的原初丰度。BBN 预测与横跨九个数量级丰度的观测相吻合，是热大爆炸模型最强有力的检验之一。
- *结构形成*：暴胀期间的量子涨落被拉伸至宏观尺度，播下 CMB 各向异性的种子，这些各向异性在引力塌缩（暗物质提供势阱）下形成宇宙网——由纤维状结构、空洞、星系团和星系构成。
- *与粒子物理的联系*：T ≳ 100 GeV 的早期宇宙探测了电弱尺度及更高能量的物理（模块 8.6）。暗物质候选粒子、重子产生和轻子产生是联系宇宙学与标准模型的活跃前沿。

---

**Self-test (blank page)**

1. Derive the first Friedmann equation from the 00-component of the EFE applied to the FLRW metric. Identify the contributions from curvature, matter, and Λ.
2. Show that the continuity equation ρ̇ + 3H(ρ + p/c²) = 0 gives ρ_m ∝ a⁻³ for dust and ρ_r ∝ a⁻⁴ for radiation. Why does radiation dilute faster?
3. Explain why a cosmological constant Λ > 0 acts as a fluid with equation of state w = p/(ρc²) = −1. How does this cause accelerated expansion?

**自测（空白页）**

1. 将 EFE 的 00 分量应用于 FLRW 度规，推导第一弗里德曼方程。标明曲率、物质和 Λ 各自的贡献。
2. 证明连续性方程 ρ̇ + 3H(ρ + p/c²) = 0 给出尘埃的 ρ_m ∝ a⁻³ 和辐射的 ρ_r ∝ a⁻⁴。为何辐射稀释得更快？
3. 解释为何正宇宙学常数 Λ > 0 等效于状态方程 w = p/(ρc²) = −1 的流体。这如何导致加速膨胀？

---

← Previous: [Module 7.5 — Black Holes & Gravitational Waves](./module-7.5-black-holes-and-gravitational-waves.md) · [Phase 7 index](./README.md)

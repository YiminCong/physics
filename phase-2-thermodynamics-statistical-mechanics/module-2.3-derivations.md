# Derivations — Module 2.3: Free Energy & Phase Transitions
# 推导 — 模块 2.3：自由能与相变

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 2.3](./module-2.3-free-energy-phase-transitions.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 2.3](./module-2.3-free-energy-phase-transitions.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Minimizing Free Energy at Fixed T and V · 在固定 T 和 V 下极小化自由能

**Claim.** A system in thermal contact with a reservoir at temperature T, with fixed volume V, reaches equilibrium by minimizing its Helmholtz free energy F = U − TS.

**命题。** 与温度为 T 的热库热接触、体积固定为 V 的系统，通过极小化亥姆霍兹自由能 F = U − TS 达到平衡。

**Step 1 — Apply the Second Law to system plus reservoir.** Let the system have entropy S_sys and internal energy U_sys. The reservoir has temperature T and entropy S_res. For any process at fixed V (no P dV work), the First Law gives dU_sys = δQ (heat absorbed from reservoir). The reservoir's entropy change is dS_res = −δQ/T (heat lost by reservoir). The total entropy change of universe is

**第 1 步 — 对系统加热库应用第二定律。** 设系统熵为 S_sys，内能为 U_sys。热库温度为 T，熵为 S_res。对于固定 V 的任意过程（无 P dV 功），第一定律给出 dU_sys = δQ（从热库吸收的热量）。热库的熵变为 dS_res = −δQ/T（热库失去的热量）。宇宙总熵变为

  dS_univ = dS_sys + dS_res = dS_sys − δQ/T = dS_sys − dU_sys/T.

**Step 2 — Second Law requires dS_univ ≥ 0.** Therefore

**第 2 步 — 第二定律要求 dS_univ ≥ 0。** 因此

  dS_sys − dU_sys/T ≥ 0,
  T dS_sys − dU_sys ≥ 0,
  −d(U_sys − T S_sys) ≥ 0,
  −dF ≥ 0,   i.e.,   **dF ≤ 0**.

Spontaneous processes decrease F; equilibrium is the minimum of F. ∎

自发过程使 F 减小；平衡态即 F 的极小值。∎

---

## B. Landau Theory: Deriving the Order Parameter and Critical Exponent β = 1/2 · 朗道理论：推导序参量与临界指数 β = 1/2

**Claim.** For a system with an η → −η symmetry, the Landau free energy F = F₀ + a(T)η² + b η⁴ (b > 0, a(T) = a₀(T − T_c)) predicts: (i) η = 0 for T > T_c; (ii) η = ±√(a₀(T_c − T)/(2b)) ∝ (T_c − T)^{1/2} for T < T_c; (iii) mean-field exponent β = 1/2; (iv) a jump in heat capacity at T_c with no latent heat.

**命题。** 对于具有 η → −η 对称性的系统，朗道自由能 F = F₀ + a(T)η² + b η⁴（b > 0，a(T) = a₀(T − T_c)）预测：(i) T > T_c 时 η = 0；(ii) T < T_c 时 η = ±√(a₀(T_c − T)/(2b)) ∝ (T_c − T)^{1/2}；(iii) 平均场临界指数 β = 1/2；(iv) T_c 处热容有跳变但无潜热。

**Step 1 — Symmetry constrains the expansion.** The physical free energy must be invariant under η → −η (e.g., magnetization reversal in a ferromagnet, sublattice swap in an antiferromagnet). Therefore only even powers of η appear:

**第 1 步 — 对称性约束展开。** 物理自由能必须在 η → −η（例如铁磁体中磁化反转，反铁磁体中子晶格交换）下不变。因此只有 η 的偶次幂项出现：

  F(T, η) = F₀(T) + a(T) η² + b η⁴ + O(η⁶).

Stability requires F → +∞ as |η| → ∞, so b > 0.

稳定性要求当 |η| → ∞ 时 F → +∞，故 b > 0。

**Step 2 — Expand a(T) near T_c.** The coefficient a(T) must change sign at T_c (otherwise η = 0 is always/never a minimum). The simplest analytic form giving a sign change at T_c is

**第 2 步 — 在 T_c 附近展开 a(T)。** 系数 a(T) 必须在 T_c 处改变符号（否则 η = 0 永远是/永远不是极小值）。给出在 T_c 处符号改变的最简解析形式为

  a(T) = a₀(T − T_c),   a₀ > 0.

For T > T_c, a > 0; for T < T_c, a < 0.

当 T > T_c 时，a > 0；当 T < T_c 时，a < 0。

**Step 3 — Find the equilibrium η by minimizing F.** Set ∂F/∂η = 0:

**第 3 步 — 通过极小化 F 求平衡 η。** 令 ∂F/∂η = 0：

  ∂F/∂η = 2a(T) η + 4b η³ = 2η [a(T) + 2b η²] = 0.

Solutions: either η = 0, or η² = −a(T)/(2b).

解为：η = 0，或 η² = −a(T)/(2b)。

**Step 4 — Determine which solution is the global minimum for T > T_c.** When a > 0, the second solution η² = −a/(2b) < 0 has no real solution. Hence the only critical point is η = 0. Check the second derivative:

**第 4 步 — 确定 T > T_c 时哪个解是全局极小值。** 当 a > 0 时，第二个解 η² = −a/(2b) < 0 无实数解。故唯一临界点为 η = 0。检查二阶导数：

  ∂²F/∂η²|_{η=0} = 2a(T) > 0   (T > T_c).

So η = 0 is a local (and global) minimum: **the disordered phase**. F has a single upward-opening bowl shape.

故 η = 0 是局部（也是全局）极小值：**无序相**。F 具有单个向上开口的碗形。

**Step 5 — Determine the global minimum for T < T_c.** When a < 0, both η = 0 and η² = −a/(2b) = a₀(T_c − T)/(2b) > 0 are critical points. Compare F values:

**第 5 步 — 确定 T < T_c 时的全局极小值。** 当 a < 0 时，η = 0 和 η² = −a/(2b) = a₀(T_c − T)/(2b) > 0 均为临界点。比较 F 值：

  F(η = 0) = F₀,
  F(η = η_min) = F₀ + a η_min² + b η_min⁴ = F₀ + a(−a/2b) + b(a/2b)²
               = F₀ − a²/(2b) + a²/(4b) = F₀ − a²/(4b).

Since a < 0, we have a² > 0, so F(η_min) = F₀ − a²/(4b) < F₀ = F(0). The double-well minima at η = ±√(−a/2b) are the global minimum: **the ordered phase**.

由于 a < 0，有 a² > 0，故 F(η_min) = F₀ − a²/(4b) < F₀ = F(0)。η = ±√(−a/2b) 处的双势阱极小值是全局极小值：**有序相**。

**Step 6 — Compute the order parameter and critical exponent β.** The equilibrium order parameter for T < T_c is

**第 6 步 — 计算序参量与临界指数 β。** T < T_c 时的平衡序参量为

  η_eq = ±√(−a(T)/(2b)) = ±√(a₀(T_c − T)/(2b)).

Define the reduced temperature t = (T_c − T)/T_c > 0. Then

定义约化温度 t = (T_c − T)/T_c > 0，则

  η_eq ∝ (T_c − T)^{1/2} = T_c^{1/2} t^{1/2},

so the critical exponent is **β = 1/2** (mean-field value). ∎

故临界指数为 **β = 1/2**（平均场值）。∎

---

## C. Specific-Heat Jump at T_c · T_c 处的比热跳变

**Claim.** At T_c there is a finite discontinuity ΔC = a₀²T_c/(2b) in the heat capacity, but no latent heat.

**命题。** 在 T_c 处热容有一有限不连续跳变 ΔC = a₀²T_c/(2b)，但无潜热。

**Step 1 — Compute the equilibrium free energy on each side.** For T > T_c: η = 0, so F_eq = F₀(T). For T < T_c: η² = −a/(2b), so

**第 1 步 — 计算每侧的平衡自由能。** 对 T > T_c：η = 0，故 F_eq = F₀(T)。对 T < T_c：η² = −a/(2b)，故

  F_eq(T) = F₀(T) − [a(T)]²/(4b) = F₀(T) − a₀²(T − T_c)²/(4b).

**Step 2 — Compute entropy on each side.** S = −(∂F/∂T)_V:

**第 2 步 — 计算每侧的熵。** S = −(∂F/∂T)_V：

  T > T_c: S = −dF₀/dT   (call this S₀)
  T < T_c: S = −dF₀/dT + a₀²(T − T_c)/(2b) = S₀ + a₀²(T − T_c)/(2b).

At T = T_c, both give S = S₀. The entropy is **continuous** at T_c: **no latent heat** (second-order transition). ∎

在 T = T_c 时，两者均给出 S = S₀。熵在 T_c 处**连续**：**无潜热**（二阶相变）。∎

**Step 3 — Compute the heat capacity C = T(∂S/∂T).** Differentiating:

**第 3 步 — 计算热容 C = T(∂S/∂T)。** 微分得：

  T > T_c: C = C₀ = T(−d²F₀/dT²)
  T < T_c: C = C₀ + a₀² T/(2b).

At T → T_c from below, C → C₀ + a₀²T_c/(2b), while from above C → C₀. The **jump in heat capacity** is

当 T 从下方趋近 T_c 时，C → C₀ + a₀²T_c/(2b)；从上方趋近时 C → C₀。**热容的跳变**为

  **ΔC = a₀²T_c/(2b).** ∎

This is the characteristic signature of a mean-field second-order transition: a step discontinuity in C with no latent heat (no delta-function spike), in contrast to first-order transitions. Experimentally this appears as a cusp or λ-anomaly in C(T) measurements.

这是平均场二阶相变的特征标志：C 中的阶跃不连续（无潜热，即无δ函数尖峰），与一阶相变形成对比。实验上这表现为 C(T) 测量中的尖峰或 λ 异常。

---

## D. First-Order Transition from Landau Theory (b < 0) · 从朗道理论推导一阶相变（b < 0）

**Claim.** If b < 0 (stabilized by a c η⁶ term, c > 0), the transition becomes first-order: the order parameter jumps discontinuously at a temperature T* > T_c where a secondary minimum in F meets the η = 0 minimum.

**命题。** 若 b < 0（由 c η⁶ 项稳定，c > 0），相变变为一阶：序参量在温度 T* > T_c 处不连续地跳变，此时 F 中的次极小值与 η = 0 极小值相遇。

**Step 1 — Free energy with sixth-order term.** Take F = F₀ + a η² + b η⁴ + c η⁶ with b < 0, c > 0. The condition ∂F/∂η = 0 gives

**第 1 步 — 含六次项的自由能。** 取 F = F₀ + a η² + b η⁴ + c η⁶，其中 b < 0，c > 0。条件 ∂F/∂η = 0 给出

  η(2a + 4b η² + 6c η⁴) = 0.

The nontrivial solutions η² = [−4b ± √(16b² − 48ac)]/(12c). These become real when the discriminant 16b² − 48ac > 0, i.e., when a < b²/(3c) — before a changes sign. The secondary minimum emerges at positive T − T_c, signaling a first-order transition.

非平凡解 η² = [−4b ± √(16b² − 48ac)]/(12c)。当判别式 16b² − 48ac > 0 时，即当 a < b²/(3c) 时（在 a 改变符号之前），这些解变为实数。次极小值在正的 T − T_c 处出现，预示一阶相变。

**Step 2 — Transition temperature T*.** The first-order transition occurs when F(η_min) = F(0), i.e., when the ordered and disordered phases have equal free energy. This happens at T* determined by

**第 2 步 — 相变温度 T*。** 一阶相变发生在 F(η_min) = F(0) 时，即有序相和无序相自由能相等时。这发生在由以下条件确定的 T* 处

  a(T*) η*² + b η*⁴ + c η*⁶ = 0  and  2a + 4b η*² + 6c η*⁴ = 0.

Solving these simultaneously gives T* > T_c. The order parameter jumps from 0 to η* ≠ 0 at T*, releasing a latent heat L = T* ΔS. ∎

同时求解这两个方程给出 T* > T_c。序参量在 T* 处从 0 跳变至 η* ≠ 0，释放潜热 L = T* ΔS。∎

---

*The Landau framework established here — polynomial expansion in an order parameter, minimization, reading off critical exponents — is the template for Ginzburg–Landau theory of superconductivity (Module 5.3) and the Higgs mechanism (Module 8.4). The failure of mean-field exponents (β = 1/2 vs. the Ising-model β ≈ 0.326 in 3D) is addressed by renormalization group theory (Module 6.6).*

*此处建立的朗道框架——序参量的多项式展开、极小化、读出临界指数——是超导的金兹堡–朗道理论（模块 5.3）和希格斯机制（模块 8.4）的模板。平均场指数的失效（β = 1/2 相对于三维伊辛模型 β ≈ 0.326）由重正化群理论（模块 6.6）来解决。*

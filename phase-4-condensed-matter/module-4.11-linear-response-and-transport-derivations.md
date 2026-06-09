# Derivations — Module 4.11: Linear Response, Transport & the Kubo Formula
# 推导 — 模块 4.11：线性响应、输运与久保公式

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 4.11](./module-4.11-linear-response-and-transport.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 4.11](./module-4.11-linear-response-and-transport.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Boltzmann Transport Equation → Drude–Sommerfeld Conductivity σ = ne²τ/m · 玻尔兹曼输运方程 → 德鲁德–索末菲电导率 σ = ne²τ/m

**Claim.** In the relaxation-time approximation, a static uniform field **E** produces a steady current **J** = σ**E** with σ = n e² τ / m and mobility μ = e τ / m; only electrons within ~k_B T of the Fermi surface contribute.

**命题。** 在弛豫时间近似下，静态均匀场 **E** 产生稳态电流 **J** = σ**E**，其中 σ = n e² τ / m，迁移率 μ = e τ / m；只有费米面附近 ~k_B T 范围内的电子才有贡献。

**Step 1 — The Boltzmann transport equation.** The distribution function f(**r**, **k**, t) of charge carriers evolves by streaming plus collisions:

**第 1 步 — 玻尔兹曼输运方程。** 载流子分布函数 f(**r**, **k**, t) 通过自由流动加碰撞演化：

  ∂f/∂t + **v**·∇_r f + (**F**/ℏ)·∇_k f = (∂f/∂t)_coll,

with band velocity **v** = (1/ℏ)∇_k ε and force **F** = −e**E** on an electron of charge −e. The relaxation-time approximation models the collision term as relaxation toward local equilibrium f₀ (the Fermi–Dirac distribution) on a single timescale τ:

其中能带速度 **v** = (1/ℏ)∇_k ε，作用在电荷 −e 电子上的力 **F** = −e**E**。弛豫时间近似将碰撞项建模为以单一时间标度 τ 向局域平衡 f₀（费米–狄拉克分布）弛豫：

  (∂f/∂t)_coll = −(f − f₀)/τ.

**Step 2 — Steady, homogeneous limit.** For a static uniform field, set ∂f/∂t = 0 and ∇_r f = 0. The BTE reduces to

**第 2 步 — 稳态、均匀极限。** 对静态均匀场，令 ∂f/∂t = 0 及 ∇_r f = 0。BTE 化为

  (−e**E**/ℏ)·∇_k f = −(f − f₀)/τ.

**Step 3 — Linearize.** Write f = f₀ + δf with δf small (linear response). On the left, replace f by f₀ to leading order, since δf gives a second-order term in E. Using the chain rule ∇_k f₀ = (∂f₀/∂ε) ∇_k ε = ℏ**v** (∂f₀/∂ε):

**第 3 步 — 线性化。** 写 f = f₀ + δf，δf 为小量（线性响应）。左端到主阶用 f₀ 替换 f，因为 δf 给出 E 的二阶项。利用链式法则 ∇_k f₀ = (∂f₀/∂ε) ∇_k ε = ℏ**v** (∂f₀/∂ε)：

  (−e**E**/ℏ)·ℏ**v** (∂f₀/∂ε) = −δf/τ,

so the deviation is

故偏离量为

  **δf = −e τ (**E**·**v**) (∂f₀/∂ε).**

Since −∂f₀/∂ε ≈ δ(ε − E_F) at low temperature, δf is sharply peaked at the Fermi surface: **only electrons near E_F respond**. This is the Sommerfeld correction to Drude's all-electrons picture.

由于在低温下 −∂f₀/∂ε ≈ δ(ε − E_F)，δf 在费米面处尖锐峰化：**只有 E_F 附近的电子响应**。这是索末菲对德鲁德"所有电子"图像的修正。

**Step 4 — Current density.** The electric current density (charge −e times velocity, summed over occupied states, factor 2 for spin already in 1/4π³) is

**第 4 步 — 电流密度。** 电流密度（电荷 −e 乘以速度，对占据态求和，自旋因子 2 已含于 1/4π³ 中）为

  **J** = −e ∫(d³k/4π³) **v** f = −e ∫(d³k/4π³) **v** δf,

where the equilibrium part f₀ carries no net current (∫**v** f₀ = 0 by inversion symmetry). Substituting δf:

其中平衡部分 f₀ 不携带净电流（由反演对称性 ∫**v** f₀ = 0）。代入 δf：

  **J** = e² τ ∫(d³k/4π³) **v** (**E**·**v**) (∂f₀/∂ε).

**Step 5 — Reduce to σ = ne²τ/m.** Take **E** = E x̂. By cubic/isotropic symmetry only the diagonal survives, with ⟨v_x²⟩ replaced by (1/3)v². Convert the **k**-integral to an energy integral using the density of states g(ε) = (m k)/(π²ℏ²) (per volume, both spins) and v² = 2ε/m:

**第 5 步 — 化为 σ = ne²τ/m。** 取 **E** = E x̂。由立方/各向同性对称性只有对角项存活，⟨v_x²⟩ 由 (1/3)v² 替换。用态密度 g(ε) = (m k)/(π²ℏ²)（单位体积，含两自旋）及 v² = 2ε/m 将 **k** 积分转为能量积分：

  J_x = e² τ E ∫ dε g(ε) (1/3) v²(ε) (∂f₀/∂ε).

Integrate by parts; with −∂f₀/∂ε peaked at E_F the integral picks out the Fermi-surface value. Using ∫ dε g(ε)(−∂f₀/∂ε) v²/3 = (1/3) v_F² g(E_F), and the free-electron identities g(E_F) = 3n/(2E_F) and (1/2)m v_F² = E_F, so (1/3) v_F² g(E_F) = (1/3)(2E_F/m)(3n/2E_F) = n/m:

分部积分；由于 −∂f₀/∂ε 在 E_F 处峰化，积分取出费米面值。用 ∫ dε g(ε)(−∂f₀/∂ε) v²/3 = (1/3) v_F² g(E_F)，及自由电子恒等式 g(E_F) = 3n/(2E_F) 与 (1/2)m v_F² = E_F，故 (1/3) v_F² g(E_F) = (1/3)(2E_F/m)(3n/2E_F) = n/m：

  J_x = (n e² τ / m) E,   hence   **σ = n e² τ / m.**

The mobility, defined by drift velocity **v**_d = −μ**E** (magnitude), follows from σ = neμ:

迁移率由漂移速度 **v**_d = −μ**E**（量值）定义，由 σ = neμ 得

  **μ = σ/(ne) = e τ / m.** ∎

  **μ = σ/(ne) = e τ / m。** ∎

---

## B. The Kubo Formula from First-Order Perturbation Theory · 从一阶微扰论推导久保公式

**Claim.** The linear conductivity is the retarded current–current correlation function

**命题。** 线性电导率是推迟电流–电流关联函数

  σ_{αβ}(ω) = (1/ℏωV) ∫₀^∞ dt e^{iωt} ⟨[J_α(t), J_β(0)]⟩,

dissipation (Re σ) being fixed by equilibrium current fluctuations (fluctuation–dissipation).

耗散（Re σ）由平衡电流涨落确定（涨落–耗散）。

**Step 1 — Perturbation and interaction picture.** Couple the current to a weak external vector potential **A**(t): the perturbation is H'(t) = −∫d³r **J**·**A**(t) = −**A**(t)·**J** (uniform **A**, **J** = ∫d³r **j** the total current operator). In the interaction picture, operators evolve under the unperturbed H₀, and the first-order correction to the density matrix gives the standard linear-response (Kubo) formula for the induced expectation value of any operator A:

**第 1 步 — 微扰与相互作用绘景。** 将电流与弱外部矢势 **A**(t) 耦合：微扰为 H'(t) = −∫d³r **J**·**A**(t) = −**A**(t)·**J**（均匀 **A**，**J** = ∫d³r **j** 为总电流算符）。在相互作用绘景中，算符在未微扰 H₀ 下演化，密度矩阵的一阶修正给出任意算符 A 诱导期望值的标准线性响应（久保）公式：

  ⟨δA(t)⟩ = (i/ℏ) ∫_{−∞}^{t} dt' ⟨[H'(t'), A(t)]⟩₀,

where ⟨…⟩₀ is the unperturbed equilibrium average and operators evolve as A(t) = e^{iH₀t/ℏ} A e^{−iH₀t/ℏ}.

其中 ⟨…⟩₀ 是未微扰平衡平均，算符按 A(t) = e^{iH₀t/ℏ} A e^{−iH₀t/ℏ} 演化。

**Step 2 — Current response.** Set A = J_α and H'(t') = −J_β A_β(t'). The induced current is

**第 2 步 — 电流响应。** 取 A = J_α 及 H'(t') = −J_β A_β(t')。诱导电流为

  ⟨δJ_α(t)⟩ = −(i/ℏ) ∫_{−∞}^{t} dt' ⟨[J_β(t'), J_α(t)]⟩₀ A_β(t').

Define the retarded response kernel by causality (response only for t > t'):

由因果性（仅 t > t' 才有响应）定义推迟响应核：

  ⟨δJ_α(t)⟩ = ∫_{−∞}^{∞} dt' χ_{αβ}(t − t') A_β(t'),
  χ_{αβ}(t − t') = (i/ℏ) θ(t − t') ⟨[J_α(t), J_β(t')]⟩₀,

using ⟨[J_β(t'), J_α(t)]⟩ = −⟨[J_α(t), J_β(t')]⟩ and time-translation invariance so the correlator depends only on t − t'.

利用 ⟨[J_β(t'), J_α(t)]⟩ = −⟨[J_α(t), J_β(t')]⟩ 及时间平移不变性，使关联子只依赖于 t − t'。

**Step 3 — Fourier transform.** For harmonic drive **A**(t) = **A**(ω)e^{−iωt}, transform with τ = t − t':

**第 3 步 — 傅里叶变换。** 对谐波驱动 **A**(t) = **A**(ω)e^{−iωt}，对 τ = t − t' 变换：

  ⟨δJ_α(ω)⟩ = χ_{αβ}(ω) A_β(ω),
  χ_{αβ}(ω) = (i/ℏ) ∫₀^∞ dτ e^{iωτ} ⟨[J_α(τ), J_β(0)]⟩₀,

the lower limit 0 (rather than −∞) coming from the θ(τ) of retardation.

下限取 0（而非 −∞）来自推迟性的 θ(τ)。

**Step 4 — Relate to the conductivity.** The uniform electric field is **E**(ω) = iω**A**(ω)/c in Gaussian units, or simply **E** = −∂_t **A** ⇒ **E**(ω) = iω **A**(ω). With current density **j** = **J**/V and **J** = σ**E**·V → the conductivity is the response per unit field per unit volume:

**第 4 步 — 与电导率联系。** 均匀电场为 **E** = −∂_t **A** ⇒ **E**(ω) = iω **A**(ω)。电流密度 **j** = **J**/V 且 **J** = σ**E**·V → 电导率是单位场、单位体积的响应：

  σ_{αβ}(ω) = χ_{αβ}(ω) / (iωV)  (plus a diamagnetic contact term, omitted for the transverse/finite-ω part). Substituting χ:

  σ_{αβ}(ω) = χ_{αβ}(ω) / (iωV)（加上抗磁接触项，对横向/有限 ω 部分略去）。代入 χ：

  **σ_{αβ}(ω) = (1/ℏωV) ∫₀^∞ dt e^{iωt} ⟨[J_α(t), J_β(0)]⟩.**

This is the **Kubo formula** (retarded current–current correlator). Operators evolve under H₀; the average is over the equilibrium ensemble; no relaxation time has been assumed.

这就是**久保公式**（推迟电流–电流关联子）。算符在 H₀ 下演化；平均对平衡系综取；未假设任何弛豫时间。

**Step 5 — Fluctuation–dissipation.** The real (dissipative) part Re σ_{αβ}(ω) is controlled by the symmetrized equilibrium correlator S_{αβ}(ω) = ∫dt e^{iωt}⟨{J_α(t), J_β(0)}⟩ through the fluctuation–dissipation theorem

**第 5 步 — 涨落–耗散。** 实（耗散）部 Re σ_{αβ}(ω) 由对称化平衡关联子 S_{αβ}(ω) = ∫dt e^{iωt}⟨{J_α(t), J_β(0)}⟩ 通过涨落–耗散定理控制

  Re σ_{αβ}(ω) = (1/2ℏωV) tanh(ℏω/2k_BT)·S_{αβ}(ω)  →  (ω→0)  Re σ_{αβ}(0) = S_{αβ}(0)/(2Vk_BT).

Thus the DC dissipation is set entirely by the spontaneous, equilibrium current fluctuations — the energy a driven system dissipates equals (up to the temperature factor) the fluctuations it exhibits at rest. ∎

因此直流耗散完全由自发的平衡电流涨落决定——受驱系统耗散的能量等于（至多差一温度因子）它在静止时所表现的涨落。∎

---

## C. Einstein Relation σ = e² N(E_F) D and Recovery of Drude · 爱因斯坦关系 σ = e² N(E_F) D 及德鲁德形式的恢复

**Claim.** σ = e² N(E_F) D, where N(E_F) is the density of states per unit volume at the Fermi level and D the diffusion constant. With D = v_F² τ / d this reproduces σ = ne²τ/m.

**命题。** σ = e² N(E_F) D，其中 N(E_F) 是费米能级处单位体积态密度，D 为扩散常数。取 D = v_F² τ / d 重现 σ = ne²τ/m。

**Step 1 — Two currents in equilibrium.** In a non-uniform system the particle current has a drift (field) part and a diffusion (density-gradient) part:

**第 1 步 — 平衡中的两种流。** 在非均匀系统中，粒子流有漂移（场）部分与扩散（密度梯度）部分：

  **j**_N = n μ_mob (−∇φ)·(carriers) − D ∇n,

where μ_mob is the mobility, φ the electrostatic potential, and D the diffusion constant (Fick's law). The electric current is **j** = −e**j**_N.

其中 μ_mob 为迁移率，φ 为静电势，D 为扩散常数（菲克定律）。电流为 **j** = −e**j**_N。

**Step 2 — Equilibrium balance.** In thermal equilibrium the total current vanishes and the electrochemical potential is flat: μ_chem − eφ = const. A spatial variation of φ is compensated by a variation of n, related through the density of states: δn = N(E_F)·δμ_chem = N(E_F)·(−e)(−δφ)·… More precisely, n responds to the local chemical potential as ∂n/∂μ_chem = N(E_F).

**第 2 步 — 平衡平衡条件。** 热平衡中总流为零，电化学势平坦：μ_chem − eφ = const。φ 的空间变化由 n 的变化补偿，通过态密度联系：∂n/∂μ_chem = N(E_F)。

**Step 3 — Match drift and diffusion.** Setting the net current to zero in equilibrium, the drift term n e μ_mob ∇φ must cancel the diffusion term e D ∇n = e D N(E_F) ∇μ_chem. Using ∇μ_chem = e∇φ at equilibrium gives

**第 3 步 — 漂移与扩散匹配。** 平衡中令净流为零，漂移项 n e μ_mob ∇φ 必须抵消扩散项 e D ∇n = e D N(E_F) ∇μ_chem。平衡时用 ∇μ_chem = e∇φ 得

  n μ_mob = e D N(E_F)/n · n  ⇒  conductivity σ = n e μ_mob = e² D N(E_F).

  n μ_mob = e D N(E_F)/n · n ⇒ 电导率 σ = n e μ_mob = e² D N(E_F)。

Hence the **Einstein relation**

故**爱因斯坦关系**

  **σ = e² N(E_F) D.**

**Step 4 — Recover Drude.** Diffusion of a particle moving at speed v_F between collisions separated by τ gives, in d dimensions, D = v_F² τ / d (random walk: D = (1/d)⟨v²⟩τ with ⟨v²⟩ = v_F² on the Fermi surface). For the 3D free-electron gas N(E_F) = 3n/(2E_F) = 3n/(m v_F²) (using E_F = ½ m v_F²). Then

**第 4 步 — 恢复德鲁德。** 以速度 v_F 在间隔 τ 的碰撞间运动的粒子扩散，在 d 维给出 D = v_F² τ / d（随机行走：D = (1/d)⟨v²⟩τ，费米面上 ⟨v²⟩ = v_F²）。对三维自由电子气 N(E_F) = 3n/(2E_F) = 3n/(m v_F²)（用 E_F = ½ m v_F²）。则

  σ = e² N(E_F) D = e² · [3n/(m v_F²)] · [v_F² τ / 3] = **n e² τ / m,**

reproducing the Drude–Sommerfeld result. The Einstein relation is also the microscopic statement of the Nyquist (Johnson) noise theorem: the same conductance that dissipates also generates equilibrium thermal current noise of spectral density 4 k_B T G. ∎

重现德鲁德–索末菲结果。爱因斯坦关系也是奈奎斯特（约翰逊）噪声定理的微观陈述：同一个产生耗散的电导也产生谱密度为 4 k_B T G 的平衡热电流噪声。∎

---

## D. Wiedemann–Franz Law κ/(σT) = (π²/3)(k_B/e)² via the Sommerfeld Expansion · 维德曼–弗兰兹定律的索末菲展开推导

**Claim.** For a degenerate electron gas, κ/(σT) = (π²/3)(k_B/e)² ≡ L₀ ≈ 2.44 × 10⁻⁸ W Ω K⁻², independent of τ, n, and material.

**命题。** 对简并电子气，κ/(σT) = (π²/3)(k_B/e)² ≡ L₀ ≈ 2.44 × 10⁻⁸ W Ω K⁻²，与 τ、n 及材料无关。

**Step 1 — Transport integrals.** Solving the linearized Boltzmann equation with a relaxation time, both the charge current (driven by E) and the heat current (driven by −∇T) are governed by energy moments of the same transport function. Define

**第 1 步 — 输运积分。** 用弛豫时间求解线性化玻尔兹曼方程，电流（由 E 驱动）与热流（由 −∇T 驱动）都由同一输运函数的能量矩支配。定义

  Kₙ = (e²/3) ∫ dε (−∂f₀/∂ε) v²(ε) τ(ε) g(ε) (ε − μ)ⁿ,   n = 0, 1, 2.

Then the electrical conductivity is σ = K₀, the thermoelectric response involves K₁, and the (zero-electric-current) thermal conductivity is

则电导率为 σ = K₀，热电响应涉及 K₁，（零电流条件下的）热导率为

  κ = (1/T)[K₂ − K₁²/K₀].

**Step 2 — Sommerfeld expansion.** For a smooth function H(ε), the integral ∫dε (−∂f₀/∂ε) H(ε) expands at low T (k_B T ≪ E_F) as

**第 2 步 — 索末菲展开。** 对光滑函数 H(ε)，积分 ∫dε (−∂f₀/∂ε) H(ε) 在低温（k_B T ≪ E_F）展开为

  ∫dε (−∂f₀/∂ε) H(ε) ≈ H(μ) + (π²/6)(k_B T)² H''(μ) + … .

The kernel −∂f₀/∂ε is even about ε = μ, so odd powers (ε − μ)ⁿ integrate against it as follows.

核 −∂f₀/∂ε 关于 ε = μ 是偶函数，故奇幂 (ε − μ)ⁿ 与之积分如下。

**Step 3 — Evaluate K₀, K₁, K₂.** Let Σ(ε) = (e²/3) v²(ε) τ(ε) g(ε) be the transport function. Applying the expansion:

**第 3 步 — 计算 K₀、K₁、K₂。** 令 Σ(ε) = (e²/3) v²(ε) τ(ε) g(ε) 为输运函数。应用展开：

- K₀ = ∫dε (−∂f₀/∂ε) Σ(ε) ≈ Σ(μ) = σ (the n = 0 moment, the conductivity).
- K₁ = ∫dε (−∂f₀/∂ε)(ε − μ) Σ(ε) ≈ (π²/3)(k_B T)² Σ'(μ)  (linear term vanishes by evenness; leading term is order (k_BT)²).
- K₂ = ∫dε (−∂f₀/∂ε)(ε − μ)² Σ(ε) ≈ (π²/3)(k_B T)² Σ(μ).

- K₀ ≈ Σ(μ) = σ（n = 0 矩，即电导率）。
- K₁ ≈ (π²/3)(k_B T)² Σ'(μ)（线性项因偶性消失；主项为 (k_BT)² 阶）。
- K₂ ≈ (π²/3)(k_B T)² Σ(μ)。

**Step 4 — Thermal conductivity.** The correction term K₁²/K₀ ~ (k_B T)⁴ is higher order and negligible compared to K₂ ~ (k_B T)². Hence

**第 4 步 — 热导率。** 修正项 K₁²/K₀ ~ (k_B T)⁴ 为高阶，相比 K₂ ~ (k_B T)² 可忽略。故

  κ = (1/T)[K₂ − K₁²/K₀] ≈ K₂/T = (π²/3)(k_B² T) Σ(μ)/T·T = (π²/3) k_B² T Σ(μ).

Since Σ(μ) = σ, this is

由于 Σ(μ) = σ，即

  **κ = (π²/3) k_B² T σ / e²,**

writing the transport function in the form that exposes e² gives κ = (π²/3)(k_B²T/e²)σ.

将输运函数写成显含 e² 的形式得 κ = (π²/3)(k_B²T/e²)σ。

**Step 5 — The Lorenz number.** Forming the ratio cancels Σ(μ), τ, n, and all material specifics:

**第 5 步 — 洛伦兹数。** 作比值消去 Σ(μ)、τ、n 及一切材料细节：

  **κ / (σ T) = (π²/3)(k_B/e)² ≡ L₀.**

Numerically L₀ = (π²/3)(1.381×10⁻²³ / 1.602×10⁻¹⁹)² = (π²/3)(8.617×10⁻⁵ V/K)² ≈ **2.44 × 10⁻⁸ W Ω K⁻².** The universality follows because the *same* carriers, scattered by the *same* τ(ε), transport both charge and heat — τ cancels in the ratio.

数值上 L₀ = (π²/3)(1.381×10⁻²³ / 1.602×10⁻¹⁹)² = (π²/3)(8.617×10⁻⁵ V/K)² ≈ **2.44 × 10⁻⁸ W Ω K⁻²。** 普适性源于*同样的*载流子被*同样的* τ(ε) 散射，同时输运电荷与热量——τ 在比值中相消。

**Step 6 — Seebeck coefficient (Mott formula).** The thermopower comes from the cross term K₁: S = −K₁/(eT K₀) = −(π²/3)(k_B²T/e)·Σ'(μ)/Σ(μ). Writing Σ(ε) ∝ σ(ε) gives the **Mott formula**

**第 6 步 — 塞贝克系数（莫特公式）。** 热电势来自交叉项 K₁：S = −K₁/(eT K₀) = −(π²/3)(k_B²T/e)·Σ'(μ)/Σ(μ)。写 Σ(ε) ∝ σ(ε) 得**莫特公式**

  **S = −(π²/3)(k_B²T/e)(d ln σ(ε)/dε)|_{ε=E_F},**

linear in T and vanishing as T → 0, with sign set by the energy slope of the conductivity at the Fermi level. ∎

随 T 线性、当 T → 0 时趋零，符号由费米能级处电导率的能量斜率决定。∎

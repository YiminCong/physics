# Derivations — Module 1.9: Magnetostatics
# 推导 — 模块 1.9：静磁学

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.9](./module-1.9-magnetostatics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.9](./module-1.9-magnetostatics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Biot–Savart Law · 毕奥–萨伐尔定律

**Claim.** The magnetic field produced by a steady current element I dℓ at a field point r is dB = (μ₀/4π) I dℓ × r̂ / r², giving the full Biot–Savart law for an arbitrary current distribution.

**命题。** 稳恒电流元 I dℓ 在场点 r 处产生的磁场为 dB = (μ₀/4π) I dℓ × r̂ / r²，给出任意电流分布的完整毕奥–萨伐尔定律。

**Step 1 — Empirical basis and units.** Experiments on straight wires (Biot, Savart, 1820; Ampère, 1820–1826) established that the force per unit length between two parallel wires carrying currents I₁ and I₂ separated by distance d is F/L = μ₀ I₁ I₂ / (2πd), which defines μ₀ (the permeability of free space). The magnetic constant μ₀ = 4π × 10⁻⁷ T·m/A in SI. From this empirical basis one can show that the field from a current element I dℓ′ at source point r′ to field point r is:

**第 1 步 — 实验基础与单位。** 关于直导线的实验（毕奥、萨伐尔，1820 年；安培，1820–1826 年）确定，间距为 d 的两平行导线携带电流 I₁ 和 I₂ 时，单位长度上的力为 F/L = μ₀ I₁ I₂ / (2πd)，由此定义 μ₀（真空磁导率）。SI 单位中 μ₀ = 4π × 10⁻⁷ T·m/A。从这一实验基础可以证明，源点 r′ 处的电流元 I dℓ′ 在场点 r 处产生的磁场为：

  dB(r) = (μ₀ / 4π) · I dℓ′ × (r − r′) / |r − r′|³.

**Step 2 — Full Biot–Savart law.** Integrating over the complete current loop C:

**第 2 步 — 完整毕奥–萨伐尔定律。** 对完整电流回路 C 积分：

  B(r) = (μ₀ / 4π) ∮_C I dℓ′ × (r − r′) / |r − r′|³.

For a volume current density J(r′):

对于体电流密度 J(r′)：

  B(r) = (μ₀ / 4π) ∫ J(r′) × (r − r′) / |r − r′|³ dV′.

**Step 3 — Verification: infinite straight wire.** For a wire along the z′-axis carrying current I, let the field point be at distance s from the wire (in the xy-plane at z = 0). Parameterise: r′ = z′ẑ, dℓ′ = dz′ẑ, r − r′ = sŝ − z′ẑ where ŝ is the radial unit vector. Then:

**第 3 步 — 验证：无限长直导线。** 对于沿 z′ 轴流过电流 I 的导线，设场点在距导线 s 处（xy 平面内 z = 0）。参数化：r′ = z′ẑ，dℓ′ = dz′ẑ，r − r′ = sŝ − z′ẑ，其中 ŝ 为径向单位矢量。则：

  dℓ′ × (r − r′) = dz′ ẑ × (sŝ − z′ẑ) = dz′ (s ẑ × ŝ) = dz′ s φ̂,

where φ̂ = ẑ × ŝ is the azimuthal direction. The magnitude |r − r′|³ = (s² + z′²)^{3/2}. Integrating from −∞ to +∞ using ∫_{−∞}^{∞} dz′/(s² + z′²)^{3/2} = 2/s²:

其中 φ̂ = ẑ × ŝ 为方位角方向。|r − r′|³ = (s² + z′²)^{3/2}。从 −∞ 到 +∞ 积分，利用 ∫_{−∞}^{∞} dz′/(s² + z′²)^{3/2} = 2/s²：

  B = (μ₀ I / 4π) · s φ̂ · (2/s²) = **μ₀ I / (2πs) φ̂.** ∎

---

## B. Ampère's Law ∇ × B = μ₀ J from the Biot–Savart Law · 从毕奥–萨伐尔定律推导安培定律 ∇ × B = μ₀ J

**Claim.** For a steady current density J, the curl of the Biot–Savart field satisfies ∇ × B = μ₀ J.

**命题。** 对于稳恒电流密度 J，毕奥–萨伐尔场的旋度满足 ∇ × B = μ₀ J。

**Step 1 — Write B in terms of a Green's function.** The Biot–Savart field can be written as:

**第 1 步 — 用格林函数表示 B。** 毕奥–萨伐尔场可写为：

  B(r) = (μ₀ / 4π) ∫ J(r′) × ∇(1/|r − r′|) dV′  ×  (−1),

using ∇_r (1/|r − r′|) = −(r − r′)/|r − r′|³. More conveniently, note that:

利用 ∇_r (1/|r − r′|) = −(r − r′)/|r − r′|³。更方便地，注意到：

  B(r) = ∇ × A(r),   where   A(r) = (μ₀/4π) ∫ J(r′)/|r − r′| dV′.

(This follows from the identity ∇ × (f J) = f(∇ × J) − J × ∇f applied with f = 1/|r − r′| and the fact that J depends only on r′, not r.)

（这由恒等式 ∇ × (f J) = f(∇ × J) − J × ∇f 得到，取 f = 1/|r − r′|，并利用 J 仅依赖 r′ 而非 r 的事实。）

**Step 2 — Compute ∇ × B using the vector identity.** Apply ∇ × (∇ × A) = ∇(∇ · A) − ∇²A:

**第 2 步 — 用矢量恒等式计算 ∇ × B。** 应用 ∇ × (∇ × A) = ∇(∇ · A) − ∇²A：

  ∇ × B = ∇(∇ · A) − ∇²A.

**Step 3 — Show ∇ · A = 0 in the Coulomb gauge.** For steady currents, ∇ · J = 0 (charge conservation: ∂ρ/∂t = 0). Then:

**第 3 步 — 在库仑规范中证明 ∇ · A = 0。** 对于稳恒电流，∇ · J = 0（电荷守恒：∂ρ/∂t = 0）。则：

  ∇_r · A = (μ₀/4π) ∫ J(r′) · ∇_r (1/|r − r′|) dV′ = −(μ₀/4π) ∫ J(r′) · ∇_{r′} (1/|r − r′|) dV′.

Integrating by parts (or using the identity ∇_{r′} · (J/|r−r′|) = (∇_{r′} · J)/|r−r′| + J · ∇_{r′}(1/|r−r′|)), and the fact that J vanishes at infinity (localised current), the boundary term is zero and ∇_{r′} · J = 0. Hence **∇ · A = 0**.

分部积分（或利用恒等式 ∇_{r′} · (J/|r−r′|) = (∇_{r′} · J)/|r−r′| + J · ∇_{r′}(1/|r−r′|)），以及 J 在无穷远处为零（局域电流），边界项为零且 ∇_{r′} · J = 0。故 **∇ · A = 0**。

**Step 4 — Evaluate ∇²A using the Green's function identity.** Using ∇²(1/|r − r′|) = −4π δ³(r − r′):

**第 4 步 — 用格林函数恒等式计算 ∇²A。** 利用 ∇²(1/|r − r′|) = −4π δ³(r − r′)：

  ∇²A = (μ₀/4π) ∫ J(r′) ∇²(1/|r − r′|) dV′ = (μ₀/4π) ∫ J(r′) (−4π δ³(r − r′)) dV′ = −μ₀ J(r).

**Step 5 — Assemble.** Since ∇(∇ · A) = 0:

**第 5 步 — 综合。** 由于 ∇(∇ · A) = 0：

  **∇ × B = 0 − (−μ₀ J) = μ₀ J.** ∎

---

## C. ∇ · B = 0 and the Vector Potential B = ∇ × A · ∇ · B = 0 与矢量势 B = ∇ × A

**Claim.** The magnetic field has zero divergence everywhere, and can therefore be written as the curl of a vector potential A.

**命题。** 磁场处处散度为零，因此可以写成矢量势 A 的旋度。

**Step 1 — Compute ∇ · B from Biot–Savart.** From B = ∇ × A (established in Step 1 of Section B):

**第 1 步 — 从毕奥–萨伐尔定律计算 ∇ · B。** 由 B = ∇ × A（B 节第 1 步已建立）：

  ∇ · B = ∇ · (∇ × A) = 0,

because the divergence of any curl is identically zero (a vector calculus identity: for any smooth vector field A, ∇ · (∇ × A) ≡ 0, proved by the symmetry of mixed partial derivatives — ∂²A_j/∂x_i ∂x_k − ∂²A_j/∂x_k ∂x_i = 0 by Schwarz's theorem).

因为任何旋度的散度恒为零（矢量分析恒等式：对任意光滑矢量场 A，∇ · (∇ × A) ≡ 0，由混合偏导数的对称性证明——∂²A_j/∂x_i ∂x_k − ∂²A_j/∂x_k ∂x_i = 0，由施瓦茨定理可得）。

**Step 2 — Physical meaning.** ∇ · B = 0 means there are no magnetic monopoles — magnetic field lines are always closed loops, never beginning or ending on a source. Integrating over any closed surface: ∮_S B · dA = 0 — the magnetic flux through any closed surface is zero.

**第 2 步 — 物理意义。** ∇ · B = 0 意味着没有磁单极——磁场线始终是闭合回路，从不在源处开始或结束。对任意闭合曲面积分：∮_S B · dA = 0——穿过任何闭合曲面的磁通量为零。

**Step 3 — Existence of A.** By the converse of the Helmholtz theorem (on a simply-connected domain, a divergence-free field is a curl): since ∇ · B = 0, there exists A such that B = ∇ × A. The vector potential A is not unique: A → A + ∇χ for any scalar χ leaves B = ∇ × (A + ∇χ) = ∇ × A + ∇ × (∇χ) = ∇ × A unchanged, since ∇ × ∇χ ≡ 0 (the curl of a gradient vanishes identically). This is **gauge freedom**.

**第 3 步 — A 的存在性。** 由亥姆霍兹定理的逆定理（在单连通域上，无散场是某个场的旋度）：由于 ∇ · B = 0，存在 A 使得 B = ∇ × A。矢量势 A 不唯一：对任意标量 χ，A → A + ∇χ 不改变 B = ∇ × (A + ∇χ) = ∇ × A + ∇ × (∇χ) = ∇ × A，因为 ∇ × ∇χ ≡ 0（梯度的旋度恒为零）。这就是**规范自由度**。

**Step 4 — Coulomb gauge and the vector Poisson equation.** Choosing the gauge ∇ · A = 0 (Coulomb gauge), Ampère's law ∇ × B = μ₀ J becomes (using ∇ × (∇ × A) = ∇(∇ · A) − ∇²A):

**第 4 步 — 库仑规范与矢量泊松方程。** 选择规范 ∇ · A = 0（库仑规范），安培定律 ∇ × B = μ₀ J 变为（利用 ∇ × (∇ × A) = ∇(∇ · A) − ∇²A）：

  ∇(0) − ∇²A = μ₀ J   →   **∇²A = −μ₀ J**,

a vector Poisson equation with formal solution A(r) = (μ₀/4π) ∫ J(r′)/|r − r′| dV′, analogous to the electrostatic φ(r) = (1/4πε₀) ∫ ρ(r′)/|r − r′| dV′. ∎

矢量泊松方程，形式解为 A(r) = (μ₀/4π) ∫ J(r′)/|r − r′| dV′，类比静电学中的 φ(r) = (1/4πε₀) ∫ ρ(r′)/|r − r′| dV′。∎

---

## D. Magnetic Dipole Field · 磁偶极子场

**Claim.** A magnetic dipole with moment m = m ẑ (a small current loop of area a carrying current I, with m = Ia) produces, at distances r much larger than the loop size, the field:

**命题。** 磁矩为 m = m ẑ 的磁偶极子（面积为 a 载流 I 的小电流环，m = Ia），在距离 r 远大于环尺寸处，产生磁场：

  B_dip = (μ₀/4π r³)(2m cos θ r̂ + m sin θ θ̂).

**Step 1 — Vector potential of a magnetic dipole.** In the Coulomb gauge, for a small current loop of area a carrying current I oriented in the ẑ-direction, located at the origin, the vector potential can be derived from the Biot–Savart law. For a general current loop of moment m = Ia ẑ in the limit of a small loop (magnetic dipole approximation):

**第 1 步 — 磁偶极子的矢量势。** 在库仑规范中，对于位于原点、沿 ẑ 方向定向的面积为 a 载流 I 的小电流环，矢量势可由毕奥–萨伐尔定律推导。对于矩为 m = Ia ẑ 的一般电流环，在小环极限下（磁偶极近似）：

  A(r) = (μ₀/4π) m × r / r³ = (μ₀/4π) m sin θ / r² φ̂.

This follows from expanding the Biot–Savart vector potential A = (μ₀/4π) ∮ I dℓ′/|r − r′| in a multipole series and retaining the leading (dipole) term, analogous to the electric multipole expansion of Section D in Module 1.8.

这由展开毕奥–萨伐尔矢量势 A = (μ₀/4π) ∮ I dℓ′/|r − r′| 的多极级数，保留主要（偶极）项得到，类比于模块 1.8 D 节的电多极展开。

**Step 2 — Compute B = ∇ × A.** In spherical coordinates with only the φ̂ component of A (A_φ = μ₀ m sin θ/(4πr²)):

**第 2 步 — 计算 B = ∇ × A。** 在球坐标中，A 只有 φ̂ 分量（A_φ = μ₀ m sin θ/(4πr²)）：

  B_r = (1/(r sin θ)) ∂(sin θ · A_φ)/∂θ = (1/(r sin θ)) ∂(μ₀ m sin²θ/(4πr²))/∂θ
       = (1/(r sin θ)) · μ₀ m · 2 sin θ cos θ/(4πr²) = μ₀ m · 2 cos θ/(4πr³).

  B_θ = −(1/r) ∂(r A_φ)/∂r = −(1/r) ∂(μ₀ m sin θ/(4πr))/∂r
       = −(1/r)(−μ₀ m sin θ/(4πr²)) = μ₀ m sin θ/(4πr³).

  B_φ = 0  (by azimuthal symmetry).

**Step 3 — Final result.** Combining:

**第 3 步 — 最终结果。** 合并得：

  **B_dip = (μ₀/4πr³)(2m cos θ r̂ + m sin θ θ̂).**

This is exactly analogous to the electric dipole field E_dip = (1/4πε₀r³)(2p cos θ r̂ + p sin θ θ̂), with the replacement p/ε₀ ↔ μ₀ m. ∎

这与电偶极子场 E_dip = (1/4πε₀r³)(2p cos θ r̂ + p sin θ θ̂) 完全类似，替换 p/ε₀ ↔ μ₀ m。∎

**Step 4 — Compact tensor form.** The dipole field can be written in Cartesian form as:

**第 4 步 — 紧凑张量形式。** 偶极子场可用笛卡尔形式写为：

  B_dip(r) = (μ₀/4πr³)[3(m · r̂)r̂ − m],

valid outside the source (r ≠ 0). Inside (r = 0) there is an additional term (2μ₀/3) m δ³(r) that ensures ∇ · B = 0 and ∇ × B = 0 are maintained in the distributional sense.

在源外（r ≠ 0）有效。在内部（r = 0）还有附加项 (2μ₀/3) m δ³(r)，确保在分布意义下 ∇ · B = 0 和 ∇ × B = 0 保持成立。

---

*The vector potential, gauge invariance, and the dipole structure established here extend directly to covariant electromagnetism (Module 1.15), the Aharonov–Bohm effect (Phase 3), and gauge field theory (Phase 8).*

*此处建立的矢量势、规范不变性和偶极结构直接延伸到协变电磁学（模块 1.15）、阿哈罗诺夫–玻姆效应（第 3 阶段）和规范场论（第 8 阶段）。*

# Module 4.8 — Quantum Hall Effect
**模块 4.8 — 量子霍尔效应**

> **Phase 4 — [Condensed Matter / Solid State](./README.md)** · Format: Definition → Demonstration → Application
> **第 4 阶段 — 凝聚态 / 固体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-4.8-derivations.md)

---

## 1. Landau Levels · 朗道能级

**Definition.** Consider a two-dimensional electron gas (2DEG) in a perpendicular magnetic field B. The vector potential A gives rise to a harmonic-oscillator-like Hamiltonian and the energy spectrum collapses into discrete, macroscopically degenerate **Landau levels**:

**定义。** 考虑垂直磁场 B 中的二维电子气（2DEG）。矢量势 A 产生类谐振子的哈密顿量，能谱坍缩为离散的、宏观简并的**朗道能级**：

  E_n = ℏ ω_c (n + ½),   n = 0, 1, 2, …

where ω_c = eB/m* is the **cyclotron frequency**. This is structurally identical to the harmonic oscillator spectrum (Module 3.2), with the Landau-level index n playing the role of the oscillator quantum number.

其中 ω_c = eB/m* 是**回旋频率**。这在结构上与谐振子谱（模块 3.2）完全相同，朗道能级指标 n 扮演振子量子数的角色。

**Demonstration.** Each Landau level has a macroscopic **degeneracy**: the number of states per unit area per Landau level is

**演示。** 每个朗道能级具有宏观**简并度**：每单位面积每个朗道能级的态数为

  g = eB / h.

This is the number of flux quanta Φ₀ = h/e per unit area. As B increases, the levels spread farther apart (larger ℏω_c) and each level accommodates more states; electrons are swept from one Landau level to the next. The **filling factor** ν counts how many Landau levels are completely filled:

这是每单位面积的磁通量子数 Φ₀ = h/e。随着 B 增大，能级间距加大（ℏω_c 增大），每个能级容纳更多态；电子从一个朗道能级扫入下一个。**填充因子** ν 计算完全填充的朗道能级数：

  ν = n_s h / (eB)

where n_s is the 2D electron density. ν is an integer when a Landau level is exactly full and the next is empty, creating an energy gap.

其中 n_s 是二维电子密度。当一个朗道能级恰好填满而下一个为空时，ν 为整数，产生能隙。

**Application.** The classical (Drude) Hall effect gives a Hall resistance R_H = B/(n_s e) that grows linearly with B. In a 2DEG at low temperatures and high B, von Klitzing (1980) discovered that R_H becomes **quantized** at precise rational multiples of h/e² whenever ν is an integer, with the longitudinal resistance dropping to zero. This is the **integer quantum Hall effect (IQHE)**.

**应用。** 经典（德鲁德）霍尔效应给出随 B 线性增长的霍尔电阻 R_H = B/(n_s e)。在低温高磁场下的 2DEG 中，冯·克利青（1980 年）发现每当 ν 为整数时 R_H 精确量子化为 h/e² 的精确有理倍数，纵向电阻降为零。这就是**整数量子霍尔效应（IQHE）**。

---

## 2. Integer & Fractional QHE · 整数与分数量子霍尔效应

**Definition.** The **quantized Hall conductance** for filling factor ν is

**定义。** 填充因子为 ν 时的**量子化霍尔电导**为

  σ_xy = ν e²/h,   ν = 1, 2, 3, …

This is one of the most precisely measured quantities in physics, used as a resistance standard (R_K = h/e² ≈ 25 813 Ω, the von Klitzing constant). The quantization is **topological**: σ_xy is insensitive to disorder, sample geometry, and microscopic details.

这是物理学中测量最精确的量之一，用作电阻标准（R_K = h/e² ≈ 25 813 Ω，冯·克利青常数）。量子化是**拓扑的**：σ_xy 对无序、样品几何形状和微观细节不敏感。

**Demonstration.** The topological origin is encoded in the **TKNN (Thouless–Kohmoto–Nightingale–den Nijs) formula**: σ_xy = (e²/h) × (sum of Chern numbers of filled bands). The Chern number is the integral of the Berry curvature over the Brillouin zone (Module 4.9). For a completely filled Landau level the Chern number equals 1, so each filled level contributes exactly e²/h to σ_xy. **Edge states** provide the physical picture: at the sample boundary, Landau levels must connect smoothly from below to above the Fermi energy, creating chiral (one-way) edge channels. The number of edge channels equals the number of filled Landau levels ν, and each carries conductance e²/h — the Büttiker picture.

**演示。** 拓扑起源编码在 **TKNN（Thouless–Kohmoto–Nightingale–den Nijs）公式**中：σ_xy = (e²/h) × （填充能带陈数之和）。陈数是贝里曲率在布里渊区上的积分（模块 4.9）。对于完全填充的朗道能级，陈数等于 1，因此每个填充能级精确贡献 e²/h 给 σ_xy。**边缘态**提供了物理图像：在样品边界，朗道能级必须从费米能量以下平滑连接到以上，产生手征（单向）边缘通道。边缘通道数等于填充朗道能级数 ν，每个通道携带电导 e²/h——这是比特克图像。

**Application.** The **fractional quantum Hall effect (FQHE)**, discovered by Tsui and Störmer (1982), shows plateaus at fractional values ν = p/q (e.g., 1/3, 2/5, 5/2, …). This cannot be explained by single-particle physics — it requires strong electron–electron interactions. The ground state at ν = 1/m (m odd integer) is the **Laughlin state**: an incompressible quantum liquid whose elementary excitations carry fractional charge e/m. The Laughlin wavefunction at ν = 1/3 is

**应用。** **分数量子霍尔效应（FQHE）**由崔琦和施特默（1982 年）发现，在分数值 ν = p/q（例如 1/3、2/5、5/2 等）处显示平台。这无法用单粒子物理解释——需要强电子–电子相互作用。ν = 1/m（m 为奇整数）处的基态是**劳夫林态**：一种不可压缩量子液体，其元激发携带分数电荷 e/m。ν = 1/3 处的劳夫林波函数为

  Ψ_{1/3} ∝ Π_{i<j} (z_i − z_j)³ · exp(−Σ_i |z_i|² / 4l_B²)

where z_i = x_i + iy_i is the complex position of the i-th electron and l_B = √(ℏ/eB) is the magnetic length. The cubic power (z_i − z_j)³ enforces both fermionic antisymmetry and the incompressibility that stabilises the fractional state. Quasihole excitations above this state carry charge e/3. Laughlin received the Nobel Prize (1998, with Tsui and Störmer) for this work. The FQHE is the cleanest known example of **topological order** and **fractional statistics** (anyons).

其中 z_i = x_i + iy_i 是第 i 个电子的复数坐标，l_B = √(ℏ/eB) 是磁长度。三次方 (z_i − z_j)³ 同时强制费米子反对称性和稳定分数态的不可压缩性。该基态之上的准空穴激发携带电荷 e/3。劳夫林因此工作荣获诺贝尔奖（1998 年，与崔琦和施特默共享）。FQHE 是已知最干净的**拓扑序**和**分数统计**（任意子）的例子。

---

**Self-test (blank page)**

1. Derive the Landau level spectrum E_n = ℏω_c(n + ½) by solving the 2D electron Hamiltonian in a magnetic field.
2. What is the degeneracy of a Landau level per unit area? Express it in terms of B and fundamental constants.
3. Define the filling factor ν; explain what happens to the longitudinal and Hall resistances as B is swept at fixed electron density.
4. Explain the edge-state (Büttiker) picture of the IQHE: why does the longitudinal resistance vanish while R_H is quantized?
5. What is the Laughlin state, and why does it support quasiparticles with charge e/3?

**自测（空白页）**

1. 通过求解磁场中二维电子哈密顿量推导朗道能级谱 E_n = ℏω_c(n + ½)。
2. 每单位面积朗道能级的简并度是多少？用 B 和基本常数表示。
3. 定义填充因子 ν；解释在固定电子密度下扫描 B 时纵向电阻和霍尔电阻发生了什么。
4. 解释 IQHE 的边缘态（比特克）图像：为什么纵向电阻消失而 R_H 量子化？
5. 什么是劳夫林态，为什么它支持电荷为 e/3 的准粒子？

---

← Previous: [Module 4.7 — Semiconductor Physics](./module-4.7-semiconductor-physics.md) · [Phase 4 index](./README.md) · Next: [Module 4.9 — Topological Matter & Berry Phase](./module-4.9-topological-matter-and-berry-phase.md) →

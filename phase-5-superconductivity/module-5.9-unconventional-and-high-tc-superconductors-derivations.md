# Derivations — Module 5.9: Unconventional & High-Tᶜ Superconductors
# 推导 — 模块 5.9：非常规与高温超导体

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 5.9](./module-5.9-unconventional-and-high-tc-superconductors.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 5.9](./module-5.9-unconventional-and-high-tc-superconductors.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The d-wave Gap Function $\Delta(k) = \Delta_0(\cos k_x a - \cos k_y a)$ · d 波能隙函数

**Claim.** For a square-lattice superconductor with nearest-neighbor pairing interaction, the gap function in the $d_{x^2-y^2}$ channel is

$$ \Delta(k) = \Delta_0(\cos k_x a - \cos k_y a), $$

which belongs to the $B_{1g}$ irreducible representation of the $D_{4h}$ point group. This function has four nodes on the Fermi surface where $\Delta(k) = 0$.

**命题。** 对于具有最近邻配对相互作用的方格子超导体，$d_{x^2-y^2}$ 通道中的能隙函数为

$$ \Delta(k) = \Delta_0(\cos k_x a - \cos k_y a), $$

它属于 $D_{4h}$ 点群的 $B_{1g}$ 不可约表示。该函数在费米面上有四个节点，使得 $\Delta(k) = 0$。

**Step 1 — Gap equation in momentum space.** The BCS gap equation (Module 5.5) generalized to anisotropic pairing is:

$$ \Delta(k) = - \sum_{k'} V(k, k') \langle c_{-k'\downarrow} c_{k'\uparrow}\rangle = - \sum_{k'} V(k, k') \Delta(k')/(2E_{k'}), $$

where $V(k, k')$ is the pairing interaction and $E_{k'} = \sqrt{\varepsilon_{k'}^2 + |\Delta(k')|^2}$ is the quasiparticle energy.

**第 1 步 — 动量空间中的能隙方程。** 推广到各向异性配对的 BCS 能隙方程（模块 5.5）为：

$$ \Delta(k) = - \sum_{k'} V(k, k') \langle c_{-k'\downarrow} c_{k'\uparrow}\rangle = - \sum_{k'} V(k, k') \Delta(k')/(2E_{k'}), $$

其中 $V(k, k')$ 为配对相互作用，$E_{k'} = \sqrt{\varepsilon_{k'}^2 + |\Delta(k')|^2}$ 为准粒子能量。

**Step 2 — Symmetry decomposition of the interaction.** On the square lattice with nearest-neighbor (NN) hopping, the Brillouin zone has $D_{4h}$ symmetry. Expand the pairing interaction in basis functions of the irreducible representations:

  - s-wave ($A_{1g}$): $\varphi_s(k) = 1$  (constant, isotropic)
  - extended s-wave ($A_{1g}$): $\varphi_{s^*}(k) = \cos k_x a + \cos k_y a$
  - $d_{x^2-y^2}$-wave ($B_{1g}$): $\varphi_d(k) = \cos k_x a - \cos k_y a$
  - $d_{xy}$-wave ($B_{2g}$): $\varphi_{d_{xy}}(k) = \sin k_x a \sin k_y a$

Write $V(k, k') = \sum_\alpha V_\alpha \varphi_\alpha(k) \varphi_\alpha(k')$. If the dominant attractive channel is $\alpha = d$, then $V(k, k') \approx -V_d \varphi_d(k) \varphi_d(k')$ with $V_d > 0$.

**第 2 步 — 相互作用的对称性分解。** 在具有最近邻（NN）跳跃的方格子上，布里渊区具有 $D_{4h}$ 对称性。将配对相互作用展开为不可约表示的基函数：

  - s 波 ($A_{1g}$)：$\varphi_s(k) = 1$（常数，各向同性）
  - 扩展 s 波 ($A_{1g}$)：$\varphi_{s^*}(k) = \cos k_x a + \cos k_y a$
  - $d_{x^2-y^2}$ 波 ($B_{1g}$)：$\varphi_d(k) = \cos k_x a - \cos k_y a$
  - $d_{xy}$ 波 ($B_{2g}$)：$\varphi_{d_{xy}}(k) = \sin k_x a \sin k_y a$

写 $V(k, k') = \sum_\alpha V_\alpha \varphi_\alpha(k) \varphi_\alpha(k')$。若主导吸引通道为 $\alpha = d$，则 $V(k, k') \approx -V_d \varphi_d(k) \varphi_d(k')$，其中 $V_d > 0$。

**Step 3 — Self-consistent solution.** Substituting the factored form of $V$ into the gap equation:

$$ \Delta(k) = V_d \varphi_d(k) \sum_{k'} \varphi_d(k') \Delta(k')/(2E_{k'}). $$

The sum $\sum_{k'} \varphi_d(k') \Delta(k')/(2E_{k'})$ is a number (call it $C$). Therefore

$$ \Delta(k) = V_d C \cdot \varphi_d(k) = \Delta_0 \varphi_d(k) = \Delta_0 (\cos k_x a - \cos k_y a), $$

where $\Delta_0 = V_d C$ is determined self-consistently. The gap function thus inherits the symmetry of the d-channel basis function.

**第 3 步 — 自洽解。** 将分解后的 $V$ 代入能隙方程：

$$ \Delta(k) = V_d \varphi_d(k) \sum_{k'} \varphi_d(k') \Delta(k')/(2E_{k'}). $$

求和 $\sum_{k'} \varphi_d(k') \Delta(k')/(2E_{k'})$ 为一个数（记为 $C$）。因此

$$ \Delta(k) = V_d C \cdot \varphi_d(k) = \Delta_0 \varphi_d(k) = \Delta_0 (\cos k_x a - \cos k_y a), $$

其中 $\Delta_0 = V_d C$ 由自洽条件决定。能隙函数因此继承了 d 通道基函数的对称性。

**Step 4 — Contrast with s-wave.** For s-wave pairing (phonon-mediated BCS), $V(k, k') \approx -V_s$ (constant near the Fermi surface), giving $\Delta(k) = \Delta_0$ (constant), the isotropic s-wave gap. The key differences:

| Property | s-wave | d-wave ($d_{x^2-y^2}$) |
|---|---|---|
| Gap symmetry | fully gapped, $\Delta(k) = \text{const} > 0$ | sign-changing, nodes at $k_x = \pm k_y$ |
| Order param. symmetry | $A_{1g}$ (invariant under $D_{4h}$) | $B_{1g}$ (changes sign under $90^\circ$ rotation) |
| Time reversal | preserved | preserved |
| Low-T behavior | exponential (activated) | power-law |

**第 4 步 — 与 s 波对比。** 对于 s 波配对（声子媒介的 BCS），$V(k, k') \approx -V_s$（费米面附近为常数），给出 $\Delta(k) = \Delta_0$（常数），即各向同性的 s 波能隙。主要区别：

| 性质 | s 波 | d 波 ($d_{x^2-y^2}$) |
|---|---|---|
| 能隙对称性 | 全能隙，$\Delta(k) = \text{const} > 0$ | 变号，节线在 $k_x = \pm k_y$ |
| 序参量对称性 | $A_{1g}$（$D_{4h}$ 下不变） | $B_{1g}$（$90^\circ$旋转下变号） |
| 时间反演 | 守恒 | 守恒 |
| 低温行为 | 指数型（激活型） | 幂律型 |

---

## B. Nodes of the d-wave Gap · d 波能隙的节点

**Claim.** The gap $\Delta(k) = \Delta_0(\cos k_x a - \cos k_y a)$ vanishes on the lines $k_x = \pm k_y$ in the Brillouin zone. These nodal lines intersect the Fermi surface at four nodal points, producing gapless excitations.

**命题。** 能隙 $\Delta(k) = \Delta_0(\cos k_x a - \cos k_y a)$ 在布里渊区的直线 $k_x = \pm k_y$ 上为零。这些节线与费米面在四个节点处相交，产生无能隙激发。

**Step 1 — Locate the nodal lines.** Set $\Delta(k) = 0$:

$$ \cos k_x a - \cos k_y a = 0 \implies \cos k_x a = \cos k_y a \implies k_x a = \pm k_y a + 2\pi n. $$

For the principal solution ($n = 0$): $\mathbf{k_x = k_y}$ and $\mathbf{k_x = -k_y}$. These are the two diagonal lines in the Brillouin zone, at $45^\circ$ to the reciprocal lattice vectors.

**第 1 步 — 定位节线。** 令 $\Delta(k) = 0$：

$$ \cos k_x a - \cos k_y a = 0 \implies \cos k_x a = \cos k_y a \implies k_x a = \pm k_y a + 2\pi n. $$

主解（$n = 0$）：$\mathbf{k_x = k_y}$ 和 $\mathbf{k_x = -k_y}$。这是布里渊区中与倒格矢成 $45^\circ$ 的两条对角线。

**Step 2 — Intersection with the Fermi surface.** The Fermi surface of the cuprates (in the simplest tight-binding model with dispersion $\varepsilon_k = -2t(\cos k_x a + \cos k_y a) - \mu$) crosses the nodal lines $k_x = \pm k_y$ at four points, called the **nodal points**. At these $k_F$ values:

$$ k_F \approx (\pi/2a, \pi/2a),\ (-\pi/2a, \pi/2a),\ (\pi/2a, -\pi/2a),\ (-\pi/2a, -\pi/2a) $$

(and their equivalents modulo the reciprocal lattice). These are the Dirac-like points where both $\varepsilon_k = 0$ (on the Fermi surface) and $\Delta(k) = 0$ simultaneously.

**第 2 步 — 与费米面的交叉点。** 铜氧化物费米面（在最简单的紧束缚模型中色散为 $\varepsilon_k = -2t(\cos k_x a + \cos k_y a) - \mu$）在节线 $k_x = \pm k_y$ 处与四个**节点**相交，约为：

$$ k_F \approx (\pi/2a, \pi/2a),\ (-\pi/2a, \pi/2a),\ (\pi/2a, -\pi/2a),\ (-\pi/2a, -\pi/2a) $$

（及其模倒格矢的等价点）。这些是 $\varepsilon_k = 0$（在费米面上）和 $\Delta(k) = 0$ 同时成立的类狄拉克点。

**Step 3 — Local expansion near a node.** Near a node at $k_0 = (k_F, k_F)$ (taking $a = 1$ for brevity), write $k = k_0 + q$. Expand to first order in $q = (q_x, q_y)$:

$$ \varepsilon_k \approx v_F \cdot q, \qquad \Delta(k) \approx \nabla_k \Delta|_{k_0} \cdot q, $$

where $v_F = \nabla_k \varepsilon|_{k_0}$ and the gradient of $\Delta$ at the node:

$$ \partial\Delta/\partial k_x|_{k_0} = -\Delta_0 a \sin(k_F a), \qquad \partial\Delta/\partial k_y|_{k_0} = +\Delta_0 a \sin(k_F a). $$

At the node, $|\nabla_k \Delta| = \sqrt{2} \Delta_0 a \sin(k_F a) = \Delta_0 v_\Delta$ where $v_\Delta = \sqrt{2} a \sin(k_F a)$ is the gap velocity. The local quasiparticle energy is

$$ E(q) = \sqrt{v_F^2 q_\perp^2 + v_\Delta^2 q_\parallel^2}, $$

where $q_\perp$ is the component normal to the Fermi surface (along which $v_F = |\nabla_k \varepsilon|$ points) and $q_\parallel$ is along it (along which the gap varies, $v_\Delta = |\nabla_k \Delta|$). This is a **2D Dirac dispersion** (linear in momentum).

**第 3 步 — 节点附近的局部展开。** 在节点 $k_0 = (k_F, k_F)$ 附近（为简洁取 $a = 1$），令 $k = k_0 + q$，展开到 $q = (q_x, q_y)$ 的一阶：

$$ \varepsilon_k \approx v_F \cdot q, \qquad \Delta(k) \approx \nabla_k \Delta|_{k_0} \cdot q, $$

其中 $v_F = \nabla_k \varepsilon|_{k_0}$，节点处 $\Delta$ 的梯度：

$$ \partial\Delta/\partial k_x|_{k_0} = -\Delta_0 a \sin(k_F a), \qquad \partial\Delta/\partial k_y|_{k_0} = +\Delta_0 a \sin(k_F a). $$

在节点处，$|\nabla_k \Delta| = \sqrt{2} \Delta_0 a \sin(k_F a) = \Delta_0 v_\Delta$，其中 $v_\Delta = \sqrt{2} a \sin(k_F a)$ 为能隙速度。局部准粒子能量为

$$ E(q) = \sqrt{v_F^2 q_\perp^2 + v_\Delta^2 q_\parallel^2}, $$

其中 $q_\perp$ 为垂直费米面的分量（$v_F = |\nabla_k \varepsilon|$ 沿此方向），$q_\parallel$ 沿费米面（能隙沿此方向变化，$v_\Delta = |\nabla_k \Delta|$）。这是**二维狄拉克色散**（动量的线性函数）。

---

## C. Low-Energy Density of States: $N(E) \propto E$ (linear) for d-wave · d 波低能态密度：$N(E) \propto E$（线性）

**Claim.** Near $E = 0$, the quasiparticle density of states for a d-wave superconductor is linear:

$$ N(E) \propto E/\Delta_0 \qquad \text{for } E \ll \Delta_0, $$

in sharp contrast to the fully gapped s-wave case where $N(E) = 0$ for $E < \Delta_0$.

**命题。** 在 $E = 0$ 附近，d 波超导体的准粒子态密度是线性的：

$$ N(E) \propto E/\Delta_0 \qquad \text{当 } E \ll \Delta_0 \text{ 时，} $$

这与全能隙 s 波情形（$E < \Delta_0$ 时 $N(E) = 0$）形成鲜明对比。

**Step 1 — General formula for the DOS.** The quasiparticle DOS is defined as:

$$ N(E) = \sum_k \delta(E - E_k) = \int \frac{d^2k}{(2\pi)^2} \delta(E - \sqrt{\varepsilon_k^2 + \Delta(k)^2}). $$

**第 1 步 — 态密度的一般公式。** 准粒子态密度定义为：

$$ N(E) = \sum_k \delta(E - E_k) = \int \frac{d^2k}{(2\pi)^2} \delta(E - \sqrt{\varepsilon_k^2 + \Delta(k)^2}). $$

**Step 2 — Split the integral into nodal and antinodal contributions.** Near each node (there are 4, related by the $D_{4h}$ symmetry), use the local linearized dispersion from Section B, Step 3. In rotated coordinates aligned with the Fermi surface tangent ($q_\parallel$) and normal ($q_\perp$) at the node:

$$ E(q) = \sqrt{v_F^2 q_\perp^2 + v_\Delta^2 q_\parallel^2}. $$

The contribution to the DOS from one node (integrating over a patch around $q = 0$):

$$ N_{\text{node}}(E) = \int \frac{dq_\parallel dq_\perp}{(2\pi)^2} \delta(E - \sqrt{v_F^2 q_\perp^2 + v_\Delta^2 q_\parallel^2}). $$

**第 2 步 — 将积分分为节点贡献和反节点贡献。** 在每个节点附近（共 4 个，由 $D_{4h}$ 对称性联系），利用 B 节第 3 步的局部线性化色散。在与节点处费米面切向（$q_\parallel$）和法向（$q_\perp$）对齐的旋转坐标中：

$$ E(q) = \sqrt{v_F^2 q_\perp^2 + v_\Delta^2 q_\parallel^2}. $$

来自单个节点的 DOS 贡献（在 $q = 0$ 附近的小块上积分）：

$$ N_{\text{node}}(E) = \int \frac{dq_\parallel dq_\perp}{(2\pi)^2} \delta(E - \sqrt{v_F^2 q_\perp^2 + v_\Delta^2 q_\parallel^2}). $$

**Step 3 — Evaluate using the delta-function and scaling.** Change variables: let $p_\perp = v_F q_\perp$ and $p_\parallel = v_\Delta q_\parallel$. The Jacobian is $1/(v_F v_\Delta)$:

$$ N_{\text{node}}(E) = \frac{1}{v_F v_\Delta} \int \frac{dp_\parallel dp_\perp}{(2\pi)^2} \delta(E - \sqrt{p_\perp^2 + p_\parallel^2}). $$

Convert to polar coordinates $p = \sqrt{p_\perp^2 + p_\parallel^2}$, angle $\theta$:

$$ \begin{aligned} N_{\text{node}}(E) &= \frac{1}{v_F v_\Delta} \int_0^\infty \int_0^{2\pi} \frac{p\, dp\, d\theta}{(2\pi)^2} \delta(E - p) \\ &= \frac{1}{v_F v_\Delta} \cdot \frac{1}{2\pi} \int_0^\infty p\, dp\, \delta(E - p) \\ &= \frac{1}{v_F v_\Delta} \cdot \frac{E}{2\pi}. \end{aligned} $$

**第 3 步 — 利用 delta 函数和尺度变换求值。** 换元：令 $p_\perp = v_F q_\perp$，$p_\parallel = v_\Delta q_\parallel$，雅可比行列式为 $1/(v_F v_\Delta)$：

$$ N_{\text{node}}(E) = \frac{1}{v_F v_\Delta} \int \frac{dp_\parallel dp_\perp}{(2\pi)^2} \delta(E - \sqrt{p_\perp^2 + p_\parallel^2}). $$

转化为极坐标 $p = \sqrt{p_\perp^2 + p_\parallel^2}$，角度 $\theta$：

$$ \begin{aligned} N_{\text{node}}(E) &= \frac{1}{v_F v_\Delta} \cdot \frac{1}{2\pi} \int_0^\infty p\, dp\, \delta(E - p) \\ &= \frac{1}{v_F v_\Delta} \cdot \frac{E}{2\pi}. \end{aligned} $$

**Step 4 — Sum over all four nodes.** The total d-wave DOS at low energies ($E \ll \Delta_0$, before antinodal regions contribute) from all 4 nodes:

$$ N(E) = 4 \times N_{\text{node}}(E) = 4 \times E/(2\pi v_F v_\Delta) = \frac{2E}{\pi v_F v_\Delta}. $$

Since $v_F$ and $v_\Delta$ are material parameters (fixed by the band structure and gap magnitude), this gives

$$ \boxed{\, N(E) \propto E \,} \qquad \text{for } E \ll \Delta_0. $$

This is the universal result for any 2D superconductor with nodal points where both $\varepsilon_k$ and $\Delta(k)$ vanish linearly. $\blacksquare$

**第 4 步 — 对四个节点求和。** 低能（$E \ll \Delta_0$，反节点区域尚未贡献）时所有 4 个节点的 d 波总 DOS：

$$ N(E) = 4 \times N_{\text{node}}(E) = 4 \times E/(2\pi v_F v_\Delta) = \frac{2E}{\pi v_F v_\Delta}. $$

由于 $v_F$ 和 $v_\Delta$ 为材料参数（由能带结构和能隙大小确定），这给出

$$ \boxed{\, N(E) \propto E \,} \qquad \text{当 } E \ll \Delta_0 \text{ 时。} $$

这是任何具有节点（$\varepsilon_k$ 和 $\Delta(k)$ 同时线性为零）的二维超导体的普适结果。$\blacksquare$

---

## D. Physical Consequences of Linear DOS · 线性态密度的物理后果

**Step 1 — Specific heat.** The electronic specific heat $c_e \sim \int E\, (dN/dE)\, dE \sim \int E \cdot dE/\Delta_0 \sim T^2/\Delta_0$ at low temperatures (using $E \sim k_BT$). In contrast, s-wave gives $c_e \propto e^{-\Delta_0/k_BT}$ (exponentially activated). The power-law $T^2$ behavior of the d-wave specific heat was confirmed in YBCO and other cuprates.

**第 1 步 — 比热。** 电子比热 $c_e \sim \int E\, (dN/dE)\, dE \sim \int E \cdot dE/\Delta_0 \sim T^2/\Delta_0$（在低温下取 $E \sim k_BT$）。相比之下，s 波给出 $c_e \propto e^{-\Delta_0/k_BT}$（指数激活）。d 波比热的幂律 $T^2$ 行为已在 YBCO 和其他铜氧化物中得到证实。

**Step 2 — London penetration depth.** The superfluid density $n_s(T)$ enters the penetration depth as $\lambda(T)^{-2} \propto n_s(T)$. In the d-wave case:

$$ \delta[\lambda(0)^{-2} - \lambda(T)^{-2}] = \delta n_s(T) \propto \int_0^\infty dE\, N(E)\, (-\partial f/\partial E) \approx N(0_+) k_BT \propto T $$

since $N(E) \approx (2/\pi v_F v_\Delta) E$ is linear and $(-\partial f/\partial E)$ peaks at $E = 0$ with width $\sim k_BT$. Thus

$$ \delta\lambda(T) = \lambda(T) - \lambda(0) \propto T \qquad \text{(d-wave, linear in T),} $$

versus $\lambda(T) - \lambda(0) \propto e^{-\Delta_0/k_BT}$ for s-wave. The linear $T$ dependence of $\lambda$ was a landmark experimental signature of d-wave pairing in cuprates (Hardy et al., 1993).

**第 2 步 — 伦敦穿透深度。** 超流密度 $n_s(T)$ 进入穿透深度的关系为 $\lambda(T)^{-2} \propto n_s(T)$。d 波情形：

$$ \delta[\lambda(0)^{-2} - \lambda(T)^{-2}] = \delta n_s(T) \propto \int_0^\infty dE\, N(E)\, (-\partial f/\partial E) \approx N(0_+) k_BT \propto T, $$

因为 $N(E) \approx (2/\pi v_F v_\Delta) E$ 是线性的，$(-\partial f/\partial E)$ 在 $E = 0$ 处有宽度约 $k_BT$ 的峰。故

$$ \delta\lambda(T) = \lambda(T) - \lambda(0) \propto T \qquad \text{（d 波，关于 T 线性），} $$

而 s 波为 $\lambda(T) - \lambda(0) \propto e^{-\Delta_0/k_BT}$。穿透深度的线性 $T$ 依赖性是铜氧化物 d 波配对的里程碑式实验特征（Hardy 等，1993 年）。

**Step 3 — NMR relaxation rate.** The nuclear spin-lattice relaxation rate $1/T_1$ is proportional to $\int N(E)^2 (-\partial f/\partial E)\, dE$ (Hebel–Slichter factor). For s-wave, the coherence peak gives a rise in $1/T_1$ just below $T_c$ (confirmed in conventional superconductors). For d-wave, the gap nodes mean $N(E) \propto E$ rather than having the van Hove singularity, so the coherence peak is **absent** and $1/T_1 \propto T^3$ (power law) — directly observed in cuprates. This was crucial evidence against s-wave pairing.

**第 3 步 — NMR 弛豫率。** 核自旋晶格弛豫率 $1/T_1$ 正比于 $\int N(E)^2 (-\partial f/\partial E)\, dE$（赫贝尔–斯利克特因子）。s 波中相干峰在 $T_c$ 以下使 $1/T_1$ 升高（在常规超导体中得到证实）。d 波中能隙节点意味着 $N(E) \propto E$ 而非范霍夫奇点，相干峰**不出现**，$1/T_1 \propto T^3$（幂律）——这在铜氧化物中直接观测到。这是反对 s 波配对的关键证据。

**Step 4 — ARPES and phase-sensitive experiments.** Angle-resolved photoemission spectroscopy (ARPES) directly maps $E(k)$ on the Fermi surface, showing the nodal gap structure $|\Delta(k)| \propto |\cos k_x a - \cos k_y a|$. Phase-sensitive experiments (corner SQUID junctions, half-integer flux quantization in trijunctions) directly confirm the **sign change** of $\Delta(k)$ under $90^\circ$ rotation — the hallmark of d-wave that distinguishes it from extended s-wave (which also has a momentum-dependent magnitude but no sign change). These experiments (Wollman, Van Harlingen, Tsuei, 1993–1994) were definitive. $\blacksquare$

**第 4 步 — ARPES 和相位敏感实验。** 角分辨光电子能谱（ARPES）直接在费米面上绘制 $E(k)$ 图，显示节点能隙结构 $|\Delta(k)| \propto |\cos k_x a - \cos k_y a|$。相位敏感实验（角形 SQUID 结、三结中的半整数磁通量子化）直接证实 $\Delta(k)$ 在 $90^\circ$ 旋转下**改变符号**——d 波的标志，这将其与扩展 s 波（也有动量依赖的幅度但无符号变化）区分开来。这些实验（Wollman、Van Harlingen、Tsuei，1993–1994 年）具有决定性意义。$\blacksquare$

---

## E. Why Phonons are Unlikely to Mediate d-wave Pairing · 声子不太可能媒介 d 波配对的原因

**Step 1 — BCS phonon kernel is attractive and peaked at small q.** The phonon-mediated interaction is $V_{ph}(q) = -2|g_q|^2 \omega_q/(\xi_k^2 - \omega_q^2) < 0$ (attractive for $|\xi_k| < \omega_q$). In real space this is nearly local (on-site or short-range), which in k-space corresponds to a nearly constant interaction independent of the direction of $k$. A constant attractive interaction $V(k, k') = -V_s$ gives only s-wave pairing (the projection onto d-wave averages to zero over the Fermi surface).

**第 1 步 — BCS 声子核是吸引的且在小 q 处有峰值。** 声子媒介相互作用为 $V_{ph}(q) = -2|g_q|^2 \omega_q/(\xi_k^2 - \omega_q^2) < 0$（$|\xi_k| < \omega_q$ 时为吸引）。实空间中几乎是局域的（格点或短程），在 k 空间对应于几乎与 $k$ 方向无关的常数相互作用。常数吸引相互作用 $V(k, k') = -V_s$ 只给出 s 波配对（费米面上对 d 波的投影平均为零）。

**Step 2 — Spin-fluctuation pairing gives d-wave.** The spin-fluctuation interaction (from antiferromagnetic fluctuations) is

$$ V_{sf}(q) = (3/2) g^2 \chi(q, 0), $$

where $\chi(q, 0)$ is the static spin susceptibility, peaked at the antiferromagnetic wavevector $Q = (\pi/a, \pi/a)$. This peak at $Q$ connects the antinodal regions of the Fermi surface (near $(\pi, 0)$ and $(0, \pi)$) to each other with a sign change:

$$ V(k, k + Q) = \text{attractive (negative)}, \qquad k \text{ at node}, \qquad k + Q \text{ at antinode}. $$

The gap equation with this $V$ has the self-consistent solution $\Delta(k + Q) = -\Delta(k)$ — exactly what $d_{x^2-y^2}$ symmetry provides ($\cos(k_x+\pi) - \cos(k_y+\pi) = -(\cos k_x - \cos k_y) = -\Delta(k)/\Delta_0$). The spin-fluctuation model thus naturally selects d-wave pairing over s-wave for a near-half-filled band.

**第 2 步 — 自旋涨落配对给出 d 波。** 自旋涨落相互作用（来自反铁磁涨落）为

$$ V_{sf}(q) = (3/2) g^2 \chi(q, 0), $$

其中 $\chi(q, 0)$ 为静态自旋磁化率，在反铁磁波矢 $Q = (\pi/a, \pi/a)$ 处有峰值。在 $Q$ 处的峰值将费米面的反节点区域（$(\pi, 0)$ 和 $(0, \pi)$ 附近）以符号变化相互连接：

$$ V(k, k + Q) = \text{吸引（负）}, \qquad k \text{ 在节点}, \qquad k + Q \text{ 在反节点}. $$

具有此 $V$ 的能隙方程有自洽解 $\Delta(k + Q) = -\Delta(k)$——恰好是 $d_{x^2-y^2}$ 对称性所提供的（$\cos(k_x+\pi) - \cos(k_y+\pi) = -(\cos k_x - \cos k_y) = -\Delta(k)/\Delta_0$）。自旋涨落模型因此对接近半满能带自然选择 d 波配对而非 s 波配对。$\blacksquare$

**Step 3 — The isotope effect.** In BCS, $T_c \propto \omega_D \propto M^{-1/2}$ ($M$ = ion mass), giving isotope exponent $\alpha = 1/2$ (replacing isotopes of the same element changes $M$ and hence $T_c$). In cuprates, the oxygen isotope effect is anomalously small ($\alpha \ll 1/2$, and in some compounds $\alpha \approx 0$ for the optimal doping). This is inconsistent with phonon-dominated pairing, and supports a non-phonon (electronic/spin) mechanism. $\blacksquare$

**第 3 步 — 同位素效应。** 在 BCS 中，$T_c \propto \omega_D \propto M^{-1/2}$（$M$ = 离子质量），给出同位素指数 $\alpha = 1/2$（替换同种元素的同位素改变 $M$ 从而改变 $T_c$）。在铜氧化物中，氧同位素效应异常小（$\alpha \ll 1/2$，某些化合物在最优掺杂时 $\alpha \approx 0$）。这与声子主导的配对不一致，支持非声子（电子/自旋）机制。$\blacksquare$

---

*Summary: the d-wave gap $\Delta(k) = \Delta_0(\cos k_x a - \cos k_y a)$ is the self-consistent solution of the gap equation in the $B_{1g}$ channel; its four nodal points on the Fermi surface produce linear quasiparticle DOS $N(E) \propto E$ via a 2D Dirac-cone calculation; this leads to power-law (not exponential) thermodynamics at low T, confirmed by specific heat, penetration depth, NMR, and ARPES. The sign change of $\Delta(k)$ is the defining fingerprint of d-wave pairing, confirmed by phase-sensitive SQUID experiments.*

*总结：d 波能隙 $\Delta(k) = \Delta_0(\cos k_x a - \cos k_y a)$ 是 $B_{1g}$ 通道能隙方程的自洽解；其在费米面上的四个节点通过二维狄拉克锥计算产生线性准粒子态密度 $N(E) \propto E$；这导致低温下幂律（而非指数）热力学行为，已由比热、穿透深度、NMR 和 ARPES 证实。$\Delta(k)$ 的符号变化是 d 波配对的决定性特征，已由相位敏感 SQUID 实验证实。*

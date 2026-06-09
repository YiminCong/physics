# Derivations — Module 4.9: Topological Matter & Berry Phase
# 推导 — 模块 4.9：拓扑物质与贝里相位

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 4.9](./module-4.9-topological-matter-and-berry-phase.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 4.9](./module-4.9-topological-matter-and-berry-phase.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Berry Phase from the Adiabatic Theorem · 由绝热定理推导贝里相位

**Claim.** If a quantum system starts in the $n$-th eigenstate of $H(R(0))$ and $R(t)$ varies slowly around a closed loop $C$ in parameter space, the system returns to the $n$-th eigenstate with a phase factor $\exp(i\gamma_n)$ where $\gamma_n = \oint_C A_n(R)\cdot dR$ and $A_n = i\langle u_n(R)|\nabla_R|u_n(R)\rangle$.

**命题。** 若量子系统从 $H(R(0))$ 的第 $n$ 个本征态出发，$R(t)$ 缓慢地在参数空间中的闭合回路 $C$ 上变化，系统回到第 $n$ 个本征态时携带相位因子 $\exp(i\gamma_n)$，其中 $\gamma_n = \oint_C A_n(R)\cdot dR$，$A_n = i\langle u_n(R)|\nabla_R|u_n(R)\rangle$。

**Step 1 — Time-dependent Schrödinger equation.** Write $|\psi(t)\rangle = \sum_m c_m(t)\, e^{i\theta_m(t)} |u_m(R(t))\rangle$ where $\theta_m(t) = -(1/\hbar)\int_0^t E_m(R(t'))\, dt'$ is the dynamical phase. Substituting into $i\hbar\, \partial_t|\psi\rangle = H|\psi\rangle$:

**第 1 步 — 含时薛定谔方程。** 令 $|\psi(t)\rangle = \sum_m c_m(t)\, e^{i\theta_m(t)} |u_m(R(t))\rangle$，其中 $\theta_m(t) = -(1/\hbar)\int_0^t E_m(R(t'))\, dt'$ 是动力学相位。代入 $i\hbar\, \partial_t|\psi\rangle = H|\psi\rangle$：

$$ \dot c_n(t) = -\sum_m c_m(t)\, e^{i(\theta_m-\theta_n)}\, \langle u_n|\partial_t|u_m\rangle. $$

**Step 2 — Off-diagonal terms.** For $m \ne n$, use $H|u_m\rangle = E_m|u_m\rangle$ and differentiate: $\langle u_n|\partial_t|u_m\rangle = \langle u_n|(\partial_t H)|u_m\rangle / (E_m - E_n)$. In the adiabatic limit $|\partial_t H|$ is small, so $\langle u_n|\partial_t|u_m\rangle \ll (E_m - E_n)/\hbar$ for $m \ne n$. The oscillating factor $e^{i(\theta_m-\theta_n)} = \exp[i\int(E_m-E_n)dt/\hbar]$ averages to zero for the rapidly oscillating off-diagonal terms. Therefore:

**第 2 步 — 非对角项。** 对 $m \ne n$，利用 $H|u_m\rangle = E_m|u_m\rangle$ 并微分：$\langle u_n|\partial_t|u_m\rangle = \langle u_n|(\partial_t H)|u_m\rangle / (E_m - E_n)$。在绝热极限下 $|\partial_t H|$ 很小，故对 $m \ne n$，$\langle u_n|\partial_t|u_m\rangle \ll (E_m - E_n)/\hbar$。振荡因子 $e^{i(\theta_m-\theta_n)} = \exp[i\int(E_m-E_n)dt/\hbar]$ 对快速振荡的非对角项平均为零。因此：

$$ \dot c_n(t) \approx -c_n(t)\, \langle u_n|\partial_t|u_n\rangle. $$

**Step 3 — Integrate.** This gives $c_n(t) = c_n(0) \exp(-\int_0^t \langle u_n|\partial_t|u_n\rangle\, dt')$. Using $\partial_t = (dR/dt)\cdot\nabla_R$:

**第 3 步 — 积分。** 这给出 $c_n(t) = c_n(0) \exp(-\int_0^t \langle u_n|\partial_t|u_n\rangle\, dt')$。利用 $\partial_t = (dR/dt)\cdot\nabla_R$：

$$ -\int_0^t \langle u_n|\partial_t|u_n\rangle\, dt' = -\int_C \langle u_n|\nabla_R|u_n\rangle\cdot dR = i \oint_C A_n \cdot dR = i \gamma_n. $$

**Step 4 — Reality of $\gamma_n$.** Differentiating $\langle u_n|u_n\rangle = 1$: $\langle\partial_R u_n|u_n\rangle + \langle u_n|\partial_R u_n\rangle = 0$, so $\langle u_n|\partial_R u_n\rangle = -\langle\partial_R u_n|u_n\rangle$ is purely imaginary. Therefore $A_n = i\langle u_n|\nabla_R u_n\rangle$ is real, and $\gamma_n$ is real. $\blacksquare$

**第 4 步 — $\gamma_n$ 的实性。** 对 $\langle u_n|u_n\rangle = 1$ 微分：$\langle\partial_R u_n|u_n\rangle + \langle u_n|\partial_R u_n\rangle = 0$，故 $\langle u_n|\partial_R u_n\rangle = -\langle\partial_R u_n|u_n\rangle$ 是纯虚数。因此 $A_n = i\langle u_n|\nabla_R u_n\rangle$ 是实数，$\gamma_n$ 是实数。$\blacksquare$

---

## B. Chern Number $\int(\text{Berry Curvature})/2\pi$ is an Integer · 陈数 $\int$（贝里曲率）$/2\pi$ 为整数

**Claim.** For a smooth Bloch band $|u_n(k)\rangle$ on a 2D torus (BZ with periodic boundary conditions), $C_n = (1/2\pi) \int_{\text{BZ}} \Omega_n(k)\, d^2k$ is an integer.

**命题。** 对于二维环面（具有周期边界条件的 BZ）上的光滑布洛赫能带 $|u_n(k)\rangle$，$C_n = (1/2\pi) \int_{\text{BZ}} \Omega_n(k)\, d^2k$ 是整数。

**Step 1 — The BZ as a torus.** The Brillouin zone has $k_{x,y} \in [-\pi/a, \pi/a]$ with the opposite edges identified (periodicity of the lattice). This makes the BZ topologically a 2-torus $T^2$.

**第 1 步 — BZ 作为环面。** 布里渊区有 $k_{x,y} \in [-\pi/a, \pi/a]$，对边等同（晶格的周期性）。这使 BZ 在拓扑上成为二维环面 $T^2$。

**Step 2 — Stokes's theorem and gauge singularities.** By Stokes's theorem, $\int_{\text{BZ}} \Omega_n\, d^2k = \oint_{\partial\text{BZ}} A_n \cdot dk$. But on a torus the boundary $\partial\text{BZ}$ is empty — the integral of a total derivative over a closed manifold is zero by Stokes. However, $A_n$ may not be globally well-defined: at points where the eigenstate $|u_n(k)\rangle$ is undefined (degeneracy or gauge singularity), $A_n$ has a Dirac-string-like singularity.

**第 2 步 — 斯托克斯定理和规范奇点。** 由斯托克斯定理，$\int_{\text{BZ}} \Omega_n\, d^2k = \oint_{\partial\text{BZ}} A_n \cdot dk$。但在环面上边界 $\partial\text{BZ}$ 为空——在闭合流形上全导数的积分由斯托克斯定理为零。然而，$A_n$ 可能不是全局定义的：在本征态 $|u_n(k)\rangle$ 未定义的点（简并或规范奇点），$A_n$ 具有类狄拉克弦奇点。

**Step 3 — Partition into patches.** Divide the BZ into two patches $U_+$ and $U_-$ with an overlap region. On each patch define a smooth gauge for $|u_n\rangle$, giving connection forms $A^+$ and $A^-$. On the overlap, the two gauges are related by a gauge transformation: $|u_n^+\rangle = e^{i\varphi(k)} |u_n^-\rangle$, so $A^+ = A^- - \nabla_k \varphi$.

**第 3 步 — 划分为小片。** 将 BZ 分为两个小片 $U_+$ 和 $U_-$，有一个重叠区域。在每个小片上为 $|u_n\rangle$ 定义光滑规范，给出联络形式 $A^+$ 和 $A^-$。在重叠区，两个规范通过规范变换关联：$|u_n^+\rangle = e^{i\varphi(k)} |u_n^-\rangle$，故 $A^+ = A^- - \nabla_k \varphi$。

**Step 4 — Chern number as winding.** The Chern number is:

**第 4 步 — 陈数作为缠绕数。** 陈数为：

$$ C_n = \frac{1}{2\pi}\Big[\int_{U_+} \Omega^+ d^2k + \int_{U_-} \Omega^- d^2k\Big] = \frac{1}{2\pi}\oint_{\partial U_+} (A^+ - A^-)\cdot dk = \frac{1}{2\pi}\oint_{\partial U_+} \nabla_k \varphi \cdot dk. $$

The last integral is the total change of $\varphi$ around the loop $\partial U_+$. Since $|u_n^+\rangle$ and $|u_n^-\rangle$ are both single-valued wavefunctions, $e^{i\varphi}$ must be single-valued, so $\varphi$ changes by $2\pi \times (\text{integer})$ around any closed loop. Therefore

最后一个积分是 $\varphi$ 绕回路 $\partial U_+$ 的总变化。由于 $|u_n^+\rangle$ 和 $|u_n^-\rangle$ 都是单值波函数，$e^{i\varphi}$ 必须是单值的，故 $\varphi$ 绕任何闭合回路变化 $2\pi \times$ （整数）。因此

$$ C_n = \frac{1}{2\pi} \cdot 2\pi \cdot (\text{integer}) = \text{integer}. \qquad \blacksquare $$

This is the mathematical result that makes the IQHE Hall conductance exactly quantized: any smooth deformation of the Hamiltonian that preserves the gap cannot change $C_n$ (an integer cannot change continuously), so $\sigma_{xy}$ is topologically protected.

这正是使 IQHE 霍尔电导精确量子化的数学结论：任何保持带隙的哈密顿量光滑形变都不能改变 $C_n$（整数不能连续变化），故 $\sigma_{xy}$ 受拓扑保护。

---

## C. SSH Winding Number and Protected Zero-Energy Edge States · SSH 缠绕数与受保护零能边缘态

**Claim.** The SSH model has a winding number $w = 0$ for $|t_1| > |t_2|$ (trivial) and $w = 1$ for $|t_2| > |t_1|$ (topological). The topological phase has exactly two zero-energy edge states on a finite chain, protected by chiral symmetry.

**命题。** SSH 模型在 $|t_1| > |t_2|$ 时缠绕数 $w = 0$（平凡），在 $|t_2| > |t_1|$ 时 $w = 1$（拓扑）。拓扑相在有限链上恰好有两个零能边缘态，受手征对称性保护。

**Step 1 — The Bloch Hamiltonian.** Write $H(k) = d(k)\cdot\sigma$ where $d(k) = (t_1 + t_2 \cos k,\, t_2 \sin k,\, 0)$ and $\sigma = (\sigma_x, \sigma_y, \sigma_z)$. The energy eigenvalues are $E_\pm(k) = \pm|d(k)|$. A gap closes only when $|d(k)| = 0$, i.e., $t_1 + t_2 \cos k = 0$ and $t_2 \sin k = 0$ simultaneously — requiring $t_1 = \pm t_2$.

**第 1 步 — 布洛赫哈密顿量。** 令 $H(k) = d(k)\cdot\sigma$，其中 $d(k) = (t_1 + t_2 \cos k,\, t_2 \sin k,\, 0)$，$\sigma = (\sigma_x, \sigma_y, \sigma_z)$。能量本征值为 $E_\pm(k) = \pm|d(k)|$。带隙仅在 $|d(k)| = 0$ 时关闭，即 $t_1 + t_2 \cos k = 0$ 且 $t_2 \sin k = 0$ 同时成立——要求 $t_1 = \pm t_2$。

**Step 2 — Winding number.** As $k$ runs from $-\pi$ to $\pi$ the 2D vector $(d_x, d_y) = (t_1 + t_2 \cos k,\, t_2 \sin k)$ traces an ellipse centred at $(t_1, 0)$. The winding number counts how many times this curve winds around the origin:

**第 2 步 — 缠绕数。** 当 $k$ 从 $-\pi$ 运行到 $\pi$ 时，二维矢量 $(d_x, d_y) = (t_1 + t_2 \cos k,\, t_2 \sin k)$ 描绘出以 $(t_1, 0)$ 为中心的椭圆。缠绕数计算此曲线绕原点的圈数：

$$ w = \frac{1}{2\pi}\oint \frac{d_x\, dd_y - d_y\, dd_x}{|d|^2} = \begin{cases} 0 & \text{if the ellipse does not enclose the origin } (|t_1| > |t_2|), \\ 1 & \text{if it encloses the origin } (|t_2| > |t_1|). \end{cases} $$

Evaluating explicitly: for $|t_2| > |t_1|$, the origin lies inside the ellipse; for $|t_1| > |t_2|$ it lies outside. $\blacksquare$

显式计算：对 $|t_2| > |t_1|$，原点在椭圆内；对 $|t_1| > |t_2|$，原点在椭圆外。$\blacksquare$

**Step 3 — Zero-energy edge states for a finite chain.** Consider $N$ unit cells with open boundary conditions (a finite chain). In the limit $t_1 = 0$ (deep topological phase), the Hamiltonian consists of $t_2$-bonds connecting B sites to A sites on the next cell. The leftmost A site and rightmost B site are not connected to any bond — they form two **exact zero-energy modes** $|\psi_L\rangle \propto |A, 1\rangle$ and $|\psi_R\rangle \propto |B, N\rangle$.

**第 3 步 — 有限链的零能边缘态。** 考虑具有开放边界条件的 $N$ 个单元（有限链）。在 $t_1 = 0$ 的极限（深拓扑相），哈密顿量由连接 B 格点到下一个单元 A 格点的 $t_2$ 键组成。最左边的 A 格点和最右边的 B 格点未与任何键相连——它们形成两个**精确零能模式** $|\psi_L\rangle \propto |A, 1\rangle$ 和 $|\psi_R\rangle \propto |B, N\rangle$。

**Step 4 — Protection by chiral symmetry.** The SSH Hamiltonian anti-commutes with $\Gamma = \sigma_z$: $\Gamma H(k) \Gamma^{-1} = -H(k)$ (chiral/sublattice symmetry). Any eigenstate $|\psi\rangle$ with energy $E \ne 0$ has a partner $\Gamma|\psi\rangle$ with energy $-E$. A zero-energy state $\Gamma|\psi_0\rangle$ can have any phase, meaning it cannot be lifted from zero by any perturbation that preserves $\Gamma$ — the edge states are **symmetry-protected**. When $t_1 \ne 0$ but still $|t_2| > |t_1|$, the edge states acquire a small splitting $\sim (t_1/t_2)^N$ that is exponentially small in the system size. $\blacksquare$

**第 4 步 — 手征对称性保护。** SSH 哈密顿量与 $\Gamma = \sigma_z$ 反对易：$\Gamma H(k) \Gamma^{-1} = -H(k)$（手征/子格对称性）。能量 $E \ne 0$ 的任意本征态 $|\psi\rangle$ 有伴侣 $\Gamma|\psi\rangle$，能量为 $-E$。零能态 $\Gamma|\psi_0\rangle$ 可以有任意相位，意味着它无法被保持 $\Gamma$ 的任意扰动从零抬起——边缘态是**对称性保护**的。当 $t_1 \ne 0$ 但 $|t_2| > |t_1|$ 时，边缘态获得 $\sim (t_1/t_2)^N$ 量级的小劈裂，在系统尺寸上指数小。$\blacksquare$

**Bulk–boundary correspondence summary.** The winding number $w$ is a property of the bulk Hamiltonian $H(k)$; the number of zero-energy edge modes on a finite chain equals $w$. This is the simplest instance of **bulk–boundary correspondence**: a topological invariant of the bulk directly predicts the number of protected boundary states. The same principle operates in the IQHE (Chern number $\leftrightarrow$ number of chiral edge channels), the QSH insulator ($Z_2$ invariant $\leftrightarrow$ helical edge pairs), and 3D TIs (strong $Z_2$ index $\leftrightarrow$ Dirac cone count on surfaces).

**体–边界对应总结。** 缠绕数 $w$ 是体哈密顿量 $H(k)$ 的属性；有限链上零能边缘模式的数量等于 $w$。这是**体–边界对应**最简单的实例：体的拓扑不变量直接预测受保护边界态的数量。同样的原理在 IQHE（陈数 $\leftrightarrow$ 手征边缘通道数）、QSH 绝缘体（$Z_2$ 不变量 $\leftrightarrow$ 螺旋边缘对）和三维拓扑绝缘体（强 $Z_2$ 指标 $\leftrightarrow$ 表面狄拉克锥数）中均有体现。

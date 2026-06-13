# Module 10.1 — String Theory & Superstrings
**模块 10.1 — 弦论与超弦**

> **Phase 10 — [Strings & Quantum Gravity](./README.md)** · Format: Definition → Demonstration → Application
> **第 10 阶段 — 弦论与量子引力** · 格式：定义 → 演示 → 应用
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-10.1-derivations.md)

---

## 1. From Point Particles to Strings · 从点粒子到弦

**Definition.** A **relativistic point particle** sweeps out a one-dimensional **worldline** in spacetime; its action is proportional to the proper length of that worldline: $S_{pp} = -mc \int d\tau = -mc \int \sqrt{-\eta_{\mu\nu} \dot{x}^\mu \dot{x}^\nu}\, d\tau$. A **string** is a one-dimensional extended object that sweeps out a two-dimensional surface called the **worldsheet** $\Sigma$, parametrized by $(\tau, \sigma)$ where $\tau$ is a timelike coordinate and $\sigma \in [0, \pi]$ labels points along the string. The generalization of the point-particle action to a string replaces proper length with proper **area** of the worldsheet.

**定义。** **相对论性点粒子**在时空中扫出一维**世界线**；其作用量正比于世界线的固有长度：$S_{pp} = -mc \int d\tau = -mc \int \sqrt{-\eta_{\mu\nu} \dot{x}^\mu \dot{x}^\nu}\, d\tau$。**弦**是一维延伸对象，扫出称为**世界面** $\Sigma$ 的二维曲面，由 $(\tau, \sigma)$ 参数化，其中 $\tau$ 是类时坐标，$\sigma \in [0, \pi]$ 标记弦上各点。将点粒子作用量推广到弦，即用世界面的固有**面积**代替固有长度。

**Demonstration.** The **Nambu–Goto action** is the direct area of the worldsheet:

$$ S_{NG} = -\frac{1}{2\pi\alpha'} \int d\tau\, d\sigma \sqrt{-\det h_{ab}}, $$

where $h_{ab} = \eta_{\mu\nu} (\partial X^\mu/\partial \xi^a)(\partial X^\nu/\partial \xi^b)$ is the induced metric on the worldsheet, $\xi^a = (\tau, \sigma)$, and $\alpha'$ (alpha-prime) is the **Regge slope** with dimensions $[\text{length}^2]$ in natural units ($\alpha' = \ell_s^2/\hbar$ in SI, where $\ell_s$ is the string length). The tension of the string is $T_s = 1/(2\pi\alpha')$. While geometrically transparent, the square root makes the Nambu–Goto action difficult to quantize. The **Polyakov action** (Brink–Di Vecchia–Howe action) trades the square root for an independent worldsheet metric $\gamma_{ab}$:

$$ S_P = -\frac{1}{4\pi\alpha'} \int d\tau\, d\sigma \sqrt{-\gamma}\, \gamma^{ab}\, \partial_a X^\mu\, \partial_b X_\mu. $$

Varying $\gamma^{ab}$ and using its equation of motion ($\gamma_{ab} \propto h_{ab}$) shows the two actions are **classically equivalent**. The Polyakov form is quadratic in $X^\mu$, making it tractable as a two-dimensional conformal field theory (2d CFT) on the worldsheet.

**演示。** **Nambu–Goto 作用量**直接取世界面面积：

$$ S_{NG} = -\frac{1}{2\pi\alpha'} \int d\tau\, d\sigma \sqrt{-\det h_{ab}}, $$

其中 $h_{ab} = \eta_{\mu\nu} (\partial X^\mu/\partial \xi^a)(\partial X^\nu/\partial \xi^b)$ 是世界面上的诱导度规，$\xi^a = (\tau, \sigma)$，$\alpha'$（$\alpha$ 撇）是**雷吉斜率**，量纲为 $[\text{length}^2]$（自然单位）。弦的张力为 $T_s = 1/(2\pi\alpha')$。Nambu–Goto 作用量几何上直观，但平方根使量子化困难。**Polyakov 作用量**用独立世界面度规 $\gamma_{ab}$ 替换平方根：

$$ S_P = -\frac{1}{4\pi\alpha'} \int d\tau\, d\sigma \sqrt{-\gamma}\, \gamma^{ab}\, \partial_a X^\mu\, \partial_b X_\mu. $$

对 $\gamma^{ab}$ 变分并利用其运动方程（$\gamma_{ab} \propto h_{ab}$）可证两个作用量**经典上等价**。Polyakov 形式对 $X^\mu$ 是二次型，可作为世界面上的二维共形场论（2d CFT）处理。

**Application.** The choice of $\alpha'$ sets the fundamental string scale. In superstring phenomenology, $\ell_s = \sqrt{\alpha'} \sim 10^{-33}$ cm (near the Planck length), making strings far too small to observe directly with current accelerators. The Polyakov action is the starting point for all modern string quantization: its symmetries (diffeomorphism and Weyl invariance on the worldsheet) constrain the theory profoundly, ultimately fixing the spacetime dimension.

**应用。** $\alpha'$ 的选取决定了基本弦尺度。在超弦现象学中，$\ell_s = \sqrt{\alpha'} \sim 10^{-33}$ cm（接近普朗克长度），使得弦远太小而无法用当前加速器直接探测。Polyakov 作用量是所有现代弦量子化的出发点：其对称性（世界面上的微分同胚不变性和 Weyl 不变性）对理论施加了深刻约束，最终固定了时空维数。

---

## 2. Open and Closed Strings, Boundary Conditions · 开弦与闭弦，边界条件

**Definition.** A string may be **open** (with two endpoints at $\sigma = 0$ and $\sigma = \pi$) or **closed** (with periodic identification $X^\mu(\tau, 0) = X^\mu(\tau, \pi)$, forming a loop). The equations of motion derived from $S_P$ are the **wave equation** on the worldsheet: $\partial^2 X^\mu/\partial\tau^2 - \partial^2 X^\mu/\partial\sigma^2 = 0$ (in conformal gauge $\gamma_{ab} = \eta_{ab}$). The solutions require boundary conditions on the endpoints (for open strings):

- **Neumann (NN):** $\partial X^\mu/\partial\sigma|_{\sigma=0,\pi} = 0$ — the endpoint moves freely; momentum does not flow off the end.
- **Dirichlet (DD):** $X^\mu|_{\sigma=0 \text{ or } \pi} = \text{const}$ — the endpoint is fixed in the $\mu$-th direction.

Mixed boundary conditions (Neumann in some directions, Dirichlet in others) define **D-branes** (§6 below).

**定义。** 弦可以是**开弦**（在 $\sigma = 0$ 和 $\sigma = \pi$ 有两个端点）或**闭弦**（满足周期性条件 $X^\mu(\tau, 0) = X^\mu(\tau, \pi)$，构成环）。由 $S_P$ 导出的运动方程是世界面上的**波动方程**：$\partial^2 X^\mu/\partial\tau^2 - \partial^2 X^\mu/\partial\sigma^2 = 0$（共形规范 $\gamma_{ab} = \eta_{ab}$ 下）。解需要对开弦端点施加边界条件：

- **Neumann（NN）**：$\partial X^\mu/\partial\sigma|_{\sigma=0,\pi} = 0$——端点自由运动；动量不从端点流出。
- **Dirichlet（DD）**：$X^\mu|_{\sigma=0 \text{ 或 } \pi} = \text{const}$——端点在第 $\mu$ 方向固定。

混合边界条件（某些方向 Neumann，其余方向 Dirichlet）定义了 **D 膜**（见第 6 节）。

**Demonstration.** For an **open string** with Neumann conditions in all directions, the general solution of the wave equation is:

$$ X^\mu(\tau, \sigma) = x^\mu + 2\alpha' p^\mu \tau + i\sqrt{2\alpha'} \sum_{n\neq 0} \frac{\alpha^\mu_n}{n}\, e^{-in\tau} \cos(n\sigma). $$

For a **closed string**, left-movers and right-movers decouple:

$$ X^\mu(\tau, \sigma) = x^\mu + 2\alpha' p^\mu \tau + i\sqrt{\frac{\alpha'}{2}} \sum_{n\neq 0} \left[ \frac{\alpha^\mu_n}{n}\, e^{-2in(\tau-\sigma)} + \frac{\bar\alpha^\mu_n}{n}\, e^{-2in(\tau+\sigma)} \right]. $$

Here $\alpha^\mu_n$ (and $\bar\alpha^\mu_n$ for closed strings) are **Fourier mode coefficients** that, upon quantization, become operators. The zero-mode $p^\mu$ is the total spacetime momentum of the string.

**演示。** 对所有方向均满足 Neumann 条件的**开弦**，波动方程的通解为：

$$ X^\mu(\tau, \sigma) = x^\mu + 2\alpha' p^\mu \tau + i\sqrt{2\alpha'} \sum_{n\neq 0} \frac{\alpha^\mu_n}{n}\, e^{-in\tau} \cos(n\sigma). $$

对**闭弦**，左行模与右行模解耦：

$$ X^\mu(\tau, \sigma) = x^\mu + 2\alpha' p^\mu \tau + i\sqrt{\frac{\alpha'}{2}} \sum_{n\neq 0} \left[ \frac{\alpha^\mu_n}{n}\, e^{-2in(\tau-\sigma)} + \frac{\bar\alpha^\mu_n}{n}\, e^{-2in(\tau+\sigma)} \right]. $$

其中 $\alpha^\mu_n$（闭弦还有 $\bar\alpha^\mu_n$）是**傅里叶模系数**，量子化后成为算符。零模 $p^\mu$ 是弦的总时空动量。

**Application.** The separation into open and closed strings is not merely a classification: different string theories contain only one type or both. Crucially, even a theory of open strings necessarily contains closed strings, because open-string loop diagrams generate closed-string propagators. This is why string theory automatically contains gravity: the massless closed-string sector always contains the **graviton** (§4).

**应用。** 开弦与闭弦的区分不仅是分类问题：不同弦论只包含一种或两种。关键在于，即使是纯开弦理论也必然包含闭弦，因为开弦圈图会产生闭弦传播子。这就是弦论自动包含引力的原因：无质量闭弦态中总包含**引力子**（见第 4 节）。

---

## 3. Quantization: Virasoro Algebra and the Mass Spectrum · 量子化：Virasoro 代数与质量谱

**Definition.** Quantizing the Polyakov string in **light-cone gauge** (or equivalently, in covariant/BRST quantization) promotes the mode coefficients $\alpha^\mu_n$ to operators satisfying

$$ [\alpha^\mu_m, \alpha^\nu_n] = m\, \eta^{\mu\nu}\, \delta_{m+n,\, 0}, $$

the algebra of $D$ decoupled harmonic oscillators for each mode level $n > 0$. The **Virasoro generators** $L_m = \tfrac12 \sum_n : \alpha_{m-n} \cdot \alpha_n :$ (with normal ordering) encode the constraint that the worldsheet stress tensor vanishes ($T_{ab} = 0$), required by gauge invariance. The central object is $L_0$, whose eigenvalue on a physical state must equal the **intercept** $a$:

$$ (L_0 - a)|\text{phys}\rangle = 0. $$

**定义。** 在**光锥规范**（或等价地，协变/BRST 量子化）下对 Polyakov 弦量子化，将模系数 $\alpha^\mu_n$ 提升为满足下式的算符：

$$ [\alpha^\mu_m, \alpha^\nu_n] = m\, \eta^{\mu\nu}\, \delta_{m+n,\, 0}, $$

即每个模级 $n > 0$ 上的 $D$ 个解耦谐振子的代数。**Virasoro 生成元** $L_m = \tfrac12 \sum_n : \alpha_{m-n} \cdot \alpha_n :$（法线序）编码世界面能量-动量张量为零的约束（$T_{ab} = 0$），这是规范不变性的要求。核心量是 $L_0$，其在物理态上的本征值必须等于**截距** $a$：

$$ (L_0 - a)|\text{phys}\rangle = 0. $$

**Demonstration.** For the **open bosonic string**, $L_0 = \alpha' M^2 + N$, where $N = \sum_{n=1}^\infty \alpha^\mu_{-n} \alpha_{n,\mu}$ is the **level number operator** (total occupation number of all oscillators). The physical-state condition gives the **mass formula**:

$$ \alpha' M^2 = N - a. $$

The ground state has $N = 0$ and therefore $M^2 = -a/\alpha'$. With the normal-ordering intercept $a = 1$ (from $\zeta$-function regularization of the zero-point sum), the ground state has $M^2 = -1/\alpha' < 0$: this is the **tachyon**, a particle with imaginary mass signaling a vacuum instability in the bosonic string. The first excited level $N = 1$ has $M^2 = 0$ and corresponds to a massless vector — the photon — provided the state is a spacetime vector, which requires it to transform as a vector under $SO(D-2)$ rotations of the transverse directions.

**演示。** 对**玻色开弦**，$L_0 = \alpha' M^2 + N$，其中 $N = \sum_{n=1}^\infty \alpha^\mu_{-n} \alpha_{n,\mu}$ 是**级数算符**（所有振子的总占据数）。物理态条件给出**质量公式**：

$$ \alpha' M^2 = N - a. $$

基态 $N = 0$，因此 $M^2 = -a/\alpha'$。利用零点和的 $\zeta$ 函数正规化给出**截距 $a = 1$**，基态有 $M^2 = -1/\alpha' < 0$：这是**快子**，虚质量粒子，标志着玻色弦的真空不稳定性。第一激发级 $N = 1$ 有 $M^2 = 0$，对应无质量矢量粒子——光子——前提是该态在时空中是矢量，这要求它在横向方向的 $SO(D-2)$ 旋转下作为矢量变换。

**Application.** The mass formula $M^2 = (N - 1)/\alpha'$ reveals the characteristic feature of string theory: an **infinite tower of massive states** at $M^2 = (N-1)/\alpha'$ for $N = 2, 3, 4, \ldots$, with spacing $1/\alpha'$. All known elementary particles sit at $N = 1$ (or, for fermions in the superstring, at levels determined by the GSO projection). The massive states are typically at the Planck or string scale and are not directly accessible experimentally, but their existence is what renders the theory UV-finite: loops sum over all modes and the softer high-energy behavior of the string amplitude (Gaussian fall-off) renders the theory finite where point-particle QFT diverges.

**应用。** 质量公式 $M^2 = (N - 1)/\alpha'$ 揭示了弦论的标志性特征：**无穷塔楼的大质量态**，质量间距为 $1/\alpha'$。所有已知基本粒子处于 $N = 1$ 级（对于超弦中的费米子，级数由 GSO 投影决定）。大质量态通常在普朗克或弦尺度，实验上不可直接探及，但它们的存在正是理论紫外有限的原因：圈图对所有模求和，弦振幅在高能下的柔和行为（高斯衰减）使理论在点粒子 QFT 发散处收敛。

---

## 4. The Critical Dimension and the Graviton · 临界维数与引力子

**Definition.** The **critical dimension** is the spacetime dimension $D$ in which the string theory is consistent — specifically, in which Lorentz invariance is preserved after quantization and there are no ghost (negative-norm) states. It arises from demanding that the Virasoro algebra has no **central charge anomaly**: the commutator $[L_m, L_n] = (m-n) L_{m+n} + (c/12) m(m^2-1) \delta_{m+n,0}$ must have $c = 0$ for the physical (matter) sector after gauge fixing. Each of the $D$ transverse $X^\mu$ fields contributes $c = 1$; the ghost system contributes $c = -26$. Cancellation requires **$D = 26$** for the bosonic string. In the superstring (with worldsheet fermions), the critical dimension is **$D = 10$**.

**定义。** **临界维数**是弦论自洽的时空维数 $D$——即量子化后保持洛伦兹不变性且无鬼（负范数）态。它来自要求 Virasoro 代数无**中心荷反常**：对易子 $[L_m, L_n] = (m-n) L_{m+n} + (c/12) m(m^2-1) \delta_{m+n,0}$ 在规范固定后的物质扇区须有 $c = 0$。$D$ 个横向场 $X^\mu$ 各贡献 $c = 1$；鬼场系统贡献 $c = -26$。相消要求玻色弦的 **$D = 26$**，超弦（带世界面费米子）的临界维数为 **$D = 10$**。

**Demonstration.** Equivalently, the intercept $a$ arises from the zero-point energy of the transverse oscillators. In light-cone gauge, $(D-2)$ transverse coordinates contribute a zero-point sum:

$$ a = \frac{D-2}{2} \cdot \sum_{n=1}^\infty n. $$

This divergent sum is regularized by **Riemann's zeta function**: $\sum_{n=1}^\infty n = \zeta(-1) = -1/12$. Therefore

$$ a = -\frac{D-2}{24}. $$

For $a = 1$ (the value required so that the $N = 1$ massless states are Lorentz vectors): $-(D-2)/24 = -1$, giving **$D - 2 = 24$, $D = 26$**. For the superstring with worldsheet supersymmetry, the fermionic zero-point contributions shift $a$ to $1/2$ and similarly force **$D = 10$**.

The massless sector of the **closed bosonic string** at $N = \tilde{N} = 1$ contains a symmetric traceless tensor, a scalar (dilaton), and an antisymmetric tensor $B_{\mu\nu}$. The **symmetric traceless spin-2 field is the graviton** — its presence is not an assumption but an unavoidable prediction of the theory.

**演示。** 等价地，截距 $a$ 来自横向振子的零点能。在光锥规范下，$(D-2)$ 个横向坐标贡献零点和：

$$ a = \frac{D-2}{2} \cdot \sum_{n=1}^\infty n. $$

这个发散和由**黎曼 $\zeta$ 函数**正规化：$\sum_{n=1}^\infty n = \zeta(-1) = -1/12$。因此

$$ a = -\frac{D-2}{24}. $$

由 $a = 1$（使 $N = 1$ 无质量态为洛伦兹矢量所需的值）：$-(D-2)/24 = -1$，给出 **$D - 2 = 24$，$D = 26$**。对带世界面超对称的超弦，费米零点贡献将 $a$ 改变为 $1/2$，同样迫使 **$D = 10$**。

**闭合玻色弦**在 $N = \tilde{N} = 1$ 的无质量扇区包含：对称无迹张量、标量（膨胀子）和反对称张量 $B_{\mu\nu}$。**对称无迹自旋-2 场就是引力子**——其存在不是假设，而是理论不可避免的预言。

**Application.** The critical-dimension result is striking: string theory selects its own spacetime dimension. The "extra" dimensions (22 for bosonic, 6 for superstring) must be **compactified** on some internal manifold (e.g., a Calabi–Yau 3-fold for the superstring) to recover 4d physics at low energies. The precise geometry of compactification determines which gauge groups and matter representations survive — the **landscape** of string vacua. The appearance of a graviton in the closed-string spectrum means that any consistent quantum string theory necessarily includes gravity: this is the deepest reason string theory is taken seriously as a quantum gravity candidate.

**应用。** 临界维数结果令人瞩目：弦论自行选择其时空维数。"额外"维（玻色弦 22 个，超弦 6 个）必须通过**紧化**到某内部流形（超弦的典型例子是 Calabi–Yau 三重）以在低能下恢复 4 维物理。紧化的具体几何决定了哪些规范群和物质表示存活——即弦真空的**景观**。闭弦谱中引力子的出现意味着任何自洽的量子弦论都必然包含引力：这是弦论被认真对待为量子引力候选理论的最深层原因。

---

## 5. Worldsheet Supersymmetry and the Superstring · 世界面超对称与超弦

**Definition.** The **bosonic string** has a tachyon in its spectrum, signaling vacuum instability, and does not include spacetime fermions. Both problems are cured by **worldsheet supersymmetry**: extending the worldsheet action to include a 2d Majorana fermion $\psi^\mu(\tau, \sigma)$ for each bosonic coordinate $X^\mu$:

$$ S = -\frac{1}{4\pi\alpha'} \int d\tau\, d\sigma \left( \partial_a X^\mu\, \partial^a X_\mu - i\bar\psi^\mu \rho^a \partial_a \psi_\mu \right), $$

where $\rho^a$ are 2d gamma matrices. This action has a worldsheet **superconformal** symmetry, with the Virasoro algebra extended to the **super-Virasoro (Neveu–Schwarz–Ramond) algebra**.

**定义。** **玻色弦**谱中有快子（表明真空不稳定），且不包含时空费米子。两个问题都可通过**世界面超对称**来消除：将世界面作用量推广，对每个玻色坐标 $X^\mu$ 引入 2 维 Majorana 费米子 $\psi^\mu(\tau, \sigma)$：

$$ S = -\frac{1}{4\pi\alpha'} \int d\tau\, d\sigma \left( \partial_a X^\mu\, \partial^a X_\mu - i\bar\psi^\mu \rho^a \partial_a \psi_\mu \right), $$

其中 $\rho^a$ 是 2 维 $\gamma$ 矩阵。该作用量具有世界面**超共形**对称性，Virasoro 代数推广为**超 Virasoro（Neveu–Schwarz–Ramond）代数**。

**Demonstration.** The worldsheet fermions $\psi^\mu$ can satisfy two types of boundary conditions around the closed string:

- **Ramond (R) sector:** $\psi^\mu(\tau, \sigma+\pi) = +\psi^\mu(\tau, \sigma)$ — periodic; zero modes exist and satisfy a Clifford algebra $\to$ spacetime **fermions**.
- **Neveu–Schwarz (NS) sector:** $\psi^\mu(\tau, \sigma+\pi) = -\psi^\mu(\tau, \sigma)$ — anti-periodic; no zero modes $\to$ spacetime **bosons**.

The **GSO projection** (Gliozzi–Scherk–Olive) projects onto states with definite worldsheet fermion number, simultaneously removing the tachyon and producing a **spacetime supersymmetric** spectrum. In $D = 10$, the critical dimension for the superstring is fixed by the same central-charge cancellation, now with each $\psi^\mu$ contributing $c = 1/2$ and the super-ghost system contributing $c = -15$: $(D \text{ bosons}) \cdot 1 + (D \text{ fermions}) \cdot (1/2) = 15 \to$ **$D(3/2) = 15 \to D = 10$**.

**演示。** 世界面费米子 $\psi^\mu$ 在闭弦环绕方向可满足两类边界条件：

- **Ramond（R）扇区**：$\psi^\mu(\tau, \sigma+\pi) = +\psi^\mu(\tau, \sigma)$——周期性；存在零模，满足 Clifford 代数 $\to$ 时空**费米子**。
- **Neveu–Schwarz（NS）扇区**：$\psi^\mu(\tau, \sigma+\pi) = -\psi^\mu(\tau, \sigma)$——反周期；无零模 $\to$ 时空**玻色子**。

**GSO 投影**（Gliozzi–Scherk–Olive）投影到具有确定世界面费米子数的态上，同时消除快子并产生**时空超对称**谱。在 $D = 10$ 下，超弦临界维数由同样的中心荷相消决定，此时每个 $\psi^\mu$ 贡献 $c = 1/2$，超鬼场系统贡献 $c = -15$：$(D \text{ 玻色}) \cdot 1 + (D \text{ 费米}) \cdot (1/2) = 15 \to$ **$D(3/2) = 15 \to D = 10$**。

**Application.** Worldsheet supersymmetry does not automatically imply **spacetime supersymmetry**, but after the GSO projection the spectrum is indeed spacetime supersymmetric: each bosonic state is paired with a fermionic state of equal mass. This is important phenomenologically because spacetime SUSY is considered a natural solution to the hierarchy problem in the Standard Model (Module 8.3), and superstrings provide a UV-complete realization of it.

**应用。** 世界面超对称不自动意味着**时空超对称**，但经过 GSO 投影后谱确实是时空超对称的：每个玻色态与一个等质量的费米态配对。这在现象学上很重要，因为时空超对称被认为是标准模型（模块 8.3）层级问题的自然解，而超弦提供了它的紫外完备实现。

---

## 6. The Five Superstring Theories, T-Duality, D-Branes, and M-Theory · 五种超弦理论、T 对偶、D 膜与 M 理论

**Definition.** In $D = 10$ there are exactly **five consistent superstring theories**, distinguished by the choice of worldsheet supersymmetry and boundary conditions:

| Theory | Closed/Open | SUSY | Gauge Group |
|--------|-------------|------|-------------|
| **Type I** | both | $\mathcal{N}=1$ | $SO(32)$ |
| **Type IIA** | closed | $\mathcal{N}=2$ non-chiral | $U(1)$ |
| **Type IIB** | closed | $\mathcal{N}=2$ chiral | — |
| **Heterotic SO(32)** | closed | $\mathcal{N}=1$ | $SO(32)$ |
| **Heterotic $E_8 \times E_8$** | closed | $\mathcal{N}=1$ | $E_8 \times E_8$ |

**定义。** 在 $D = 10$ 中，恰好存在**五种自洽超弦理论**，由世界面超对称的选择和边界条件区分：

| 理论 | 开/闭弦 | 超对称 | 规范群 |
|------|---------|--------|--------|
| **I 型** | 两者 | $\mathcal{N}=1$ | $SO(32)$ |
| **IIA 型** | 闭弦 | $\mathcal{N}=2$ 非手征 | $U(1)$ |
| **IIB 型** | 闭弦 | $\mathcal{N}=2$ 手征 | — |
| **杂化 SO(32)** | 闭弦 | $\mathcal{N}=1$ | $SO(32)$ |
| **杂化 $E_8 \times E_8$** | 闭弦 | $\mathcal{N}=1$ | $E_8 \times E_8$ |

**Demonstration.** A key non-perturbative relationship is **T-duality**: compactifying one dimension on a circle of radius $R$ is equivalent to compactification on radius $\alpha'/R$. Explicitly, winding modes (strings wrapping the compact direction $n$ times, contributing mass $\sim nR/\alpha'$) exchange with Kaluza–Klein momentum modes (contributing mass $\sim m/R$), so the two theories are physically equivalent. T-duality maps Type IIA $\leftrightarrow$ Type IIB and Heterotic $SO(32) \leftrightarrow$ Heterotic $E_8 \times E_8$. Under T-duality, a $D_p$-brane (a Dirichlet brane on which open strings end, with $p+1$ worldvolume directions) maps to a $D_{p\pm 1}$-brane: **D-branes** are non-perturbative objects whose existence is required for duality consistency. The five theories plus 11-dimensional **supergravity** are all related by a web of dualities and are corners of a single 11-dimensional theory called **M-theory** (Witten, 1995), whose microscopic formulation remains unknown but whose low-energy limit is 11d supergravity.

**演示。** 一个关键的非微扰关系是 **T 对偶**：在半径为 $R$ 的圆上紧化一个维度，等价于在半径 $\alpha'/R$ 上紧化。具体地，绕圈模式（弦绕紧化方向 $n$ 圈，质量贡献 $\sim nR/\alpha'$）与 Kaluza–Klein 动量模式（质量贡献 $\sim m/R$）互换，因此两个理论物理上等价。T 对偶将 IIA 型 $\leftrightarrow$ IIB 型，以及杂化 $SO(32) \leftrightarrow$ 杂化 $E_8 \times E_8$ 对应。在 T 对偶下，$D_p$ 膜（开弦端点所在的 Dirichlet 膜，有 $p+1$ 个世界体方向）映射为 $D_{p\pm 1}$ 膜：**D 膜**是对偶自洽性所要求的非微扰对象。五种理论加上 11 维**超引力**，均通过对偶网络相关联，是称为 **M 理论**（Witten，1995）的单一 11 维理论的不同极限；其微观表述尚未知，但低能极限是 11 维超引力。

**Application.** D-branes have been transformative beyond the duality web. In Type II theories, a stack of $N$ coincident D3-branes supports a $U(N)$ gauge theory on their worldvolume; taking $N$ large and the string coupling small, the worldvolume theory is $\mathcal{N}=4$ super-Yang–Mills in 4d — exactly the field theory that appears on one side of the **AdS/CFT correspondence** (Module 10.2). The Heterotic $E_8 \times E_8$ theory, compactified on a Calabi–Yau threefold, was historically the most promising string-theory phenomenology because $E_8 \times E_8$ naturally contains GUT groups such as $E_6$ and $SO(10)$. M-theory unification implies that these are not five separate theories but one, suggesting that the true fundamental theory is neither a string theory nor a field theory but something richer — whose nature remains the central open problem of theoretical physics.

**应用。** D 膜的意义远超对偶网络。在 II 型理论中，$N$ 张重合的 D3 膜在其世界体上支持 $U(N)$ 规范理论；取 $N$ 大且弦耦合小，世界体理论是 4 维 $\mathcal{N}=4$ 超杨–Mills——正是 **AdS/CFT 对应**（模块 10.2）一侧的场论。杂化 $E_8 \times E_8$ 理论紧化在 Calabi–Yau 三重上，历史上是最有前景的弦论现象学，因为 $E_8 \times E_8$ 自然包含 GUT 群如 $E_6$ 和 $SO(10)$。M 理论的统一意味着这不是五个独立理论，而是一个——暗示真正的基本理论既非弦论也非场论，而是更丰富的东西——其本质仍是理论物理的核心未解问题。

## Key results · 核心结果

- Nambu–Goto $S = -\dfrac{1}{2\pi\alpha'}\int d\tau\,d\sigma\sqrt{-\det h_{ab}}$ — worldsheet area action ($\alpha'$ = Regge slope) · 南部–后藤作用量
- Polyakov form $S = -\dfrac{1}{4\pi\alpha'}\int d\tau\,d\sigma\sqrt{-\gamma}\,\gamma^{ab}\partial_a X^\mu\partial_b X_\mu$ · 波利亚科夫形式
- Mode expansion $X^\mu(\tau,\sigma)$: vibrational modes = the particle spectrum · 振动模式即粒子谱
- Closed strings contain a massless spin-2 mode — the graviton · 闭弦含无质量自旋-2 模(引力子)

---

**Self-test (blank page)**

1. Write down the Polyakov action and state its symmetries; explain why it is classically equivalent to the Nambu–Goto action.
2. For the open bosonic string, derive (or quote) the mass formula $\alpha' M^2 = N - 1$ and identify: (a) the tachyon, (b) the massless vector, and (c) the first massive level.
3. Explain in one paragraph why Lorentz consistency of the quantum string forces $D = 26$ for the bosonic string and $D = 10$ for the superstring.
4. What is T-duality, and what does it imply about the five superstring theories?
5. What is a D-brane, and why is its existence required by T-duality?

**自测（空白页）**

1. 写出 Polyakov 作用量并陈述其对称性；解释为何它与 Nambu–Goto 作用量经典等价。
2. 对玻色开弦，推导（或引用）质量公式 $\alpha' M^2 = N - 1$ 并识别：(a) 快子，(b) 无质量矢量，(c) 第一大质量级。
3. 用一段话解释为何量子弦的洛伦兹自洽性迫使玻色弦 $D = 26$、超弦 $D = 10$。
4. T 对偶是什么，它对五种超弦理论意味着什么？
5. D 膜是什么，为何 T 对偶要求其存在？

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** $S_P=-\dfrac1{4\pi\alpha'}\int d\tau d\sigma\sqrt{-\gamma}\,\gamma^{ab}\partial_a X^\mu\partial_b X_\mu$. Symmetries: target-space Poincaré, worldsheet diffeomorphisms, and Weyl invariance. Solving the auxiliary metric $\gamma_{ab}$ equation of motion gives $\gamma_{ab}\propto$ the induced metric, and substituting back reproduces Nambu–Goto. · Polyakov 作用量;消去辅助度规回到 Nambu–Goto。

**2.** $\alpha' M^2=N-1$: (a) $N=0$ ⟹ $M^2=-1/\alpha'<0$, the tachyon; (b) $N=1$ ⟹ $M^2=0$, the massless vector (gauge boson); (c) $N=2$ ⟹ $M^2=1/\alpha'$, the first massive level. · 质量公式;快子、无质量矢量、首个有质量能级。

**3.** Quantization introduces a Weyl (conformal) anomaly proportional to the central charge; cancelling it ($c_X=D$ against ghost $c=-26$) forces $D=26$ for the bosonic string. Worldsheet supersymmetry changes the ghost count to give $D=10$ for the superstring. · 共形反常相消(鬼场 $-26$)迫使 $D=26$;超弦 $D=10$。

**4.** T-duality: a string on a circle of radius $R$ is identical to one on radius $\alpha'/R$, exchanging momentum and winding modes. It relates the five superstring theories (IIA↔IIB, the two heterotic theories), unifying them — with S-duality and M-theory — into one framework. · T 对偶 $R\leftrightarrow\alpha'/R$,联系五种超弦理论。

**5.** A D-brane is a dynamical hypersurface on which open strings end (Dirichlet boundary conditions). T-duality requires it: T-dualizing Neumann endpoints turns them into Dirichlet ones, confining the string ends to a lower-dimensional surface. · D 膜是开弦端点所在的超曲面;T 对偶必然要求其存在。

</details>

---

[Phase 10 index](./README.md) · Next: [Module 10.2 — Quantum Gravity & Holography](./module-10.2-quantum-gravity-and-holography.md) →

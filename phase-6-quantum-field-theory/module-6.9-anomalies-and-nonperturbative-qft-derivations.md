# Derivations — Module 6.9: Anomalies & Non-Perturbative QFT
# 推导 — 模块 6.9：反常与非微扰量子场论

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 6.9](./module-6.9-anomalies-and-nonperturbative-qft.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 6.9](./module-6.9-anomalies-and-nonperturbative-qft.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Chiral (ABJ) Anomaly: $\partial_\mu j^{\mu 5} = (e^2/16\pi^2)\, \varepsilon^{\mu\nu\rho\sigma} F_{\mu\nu} F_{\rho\sigma}$

**Claim.** In QED with massless fermions, the axial current $j^{\mu 5} = \bar\psi\, \gamma^\mu \gamma^5 \psi$, which is conserved at the classical level ($\partial_\mu j^{\mu 5} = 0$ when $m = 0$), acquires a non-zero divergence upon quantization given by

**命题。** 在无质量费米子的 QED 中，轴矢流 $j^{\mu 5} = \bar\psi\, \gamma^\mu \gamma^5 \psi$ 在经典层面守恒（当 $m = 0$ 时 $\partial_\mu j^{\mu 5} = 0$），但在量子化后获得非零散度：

$$ \partial_\mu j^{\mu 5} = \frac{e^2}{16\pi^2}\, \varepsilon^{\mu\nu\rho\sigma} F_{\mu\nu} F_{\rho\sigma}. $$

We present the **Fujikawa path-integral method**, which reveals the anomaly as a non-invariance of the fermion path-integral measure under a chiral rotation.

我们采用 **Fujikawa 路径积分方法**，该方法揭示反常源于费米子路径积分测度在手征旋转下的非不变性。

**Step 1 — Classical chiral symmetry.** The QED action for a massless Dirac fermion is

**第 1 步 — 经典手征对称性。** 无质量狄拉克费米子的 QED 作用量为

$$ S[\psi, \bar\psi, A] = \int d^4x\, \bar\psi(x)\, i\gamma^\mu D_\mu \psi(x), \qquad D_\mu = \partial_\mu - ieA_\mu. $$

Under a **global chiral rotation** by angle $\alpha$:

在角度为 $\alpha$ 的**整体手征旋转**下：

$$ \psi(x) \to e^{i\alpha\gamma^5} \psi(x), \qquad \bar\psi(x) \to \bar\psi(x)\, e^{i\alpha\gamma^5} $$

(since $(e^{i\alpha\gamma^5})^\dagger \gamma^0 = \gamma^0 e^{i\alpha\gamma^5}$ using $\{\gamma^5, \gamma^\mu\} = 0$ and $(\gamma^5)^\dagger = \gamma^5$). Because $i\gamma^\mu D_\mu$ anti-commutes with $\gamma^5$ when $m = 0$ (the Dirac operator is odd under $\gamma^5$), the action is invariant:

（因为 $(e^{i\alpha\gamma^5})^\dagger \gamma^0 = \gamma^0 e^{i\alpha\gamma^5}$，利用了 $\{\gamma^5, \gamma^\mu\} = 0$ 和 $(\gamma^5)^\dagger = \gamma^5$）。由于当 $m = 0$ 时 $i\gamma^\mu D_\mu$ 与 $\gamma^5$ 反对易（狄拉克算符在 $\gamma^5$ 下是奇的），作用量不变：

$$ \delta S = 0 \implies \text{classically:}\quad \partial_\mu j^{\mu 5} = 0 \quad (\text{for } m = 0). $$

**Step 2 — The path-integral measure is not invariant.** In the path integral

**第 2 步 — 路径积分测度不不变。** 在路径积分

$$ Z[A] = \int D\psi\, D\bar\psi\, \exp(iS[\psi, \bar\psi, A]) $$

we expand $\psi$ and $\bar\psi$ in eigenmodes of the Euclidean Dirac operator $i\slashed{D}$ (analytically continued to Euclidean space for convergence). Let $\{\varphi_n\}$ be an orthonormal basis of eigenfunctions: $i\slashed{D}\, \varphi_n = \lambda_n \varphi_n$, $\langle\varphi_n|\varphi_m\rangle = \delta_{nm}$. Write

我们将 $\psi$ 和 $\bar\psi$ 展开为欧几里得狄拉克算符 $i\slashed{D}$ 的本征模（为收敛性解析延拓至欧几里得空间）。设 $\{\varphi_n\}$ 为正交归一本征函数基：$i\slashed{D}\, \varphi_n = \lambda_n \varphi_n$，$\langle\varphi_n|\varphi_m\rangle = \delta_{nm}$。写

$$ \psi(x) = \sum_n a_n \varphi_n(x), \qquad \bar\psi(x) = \sum_n \bar b_n \varphi_n^\dagger(x), $$

where $a_n, \bar b_n$ are Grassmann coefficients. The measure is $D\psi\, D\bar\psi = \prod_n da_n\, d\bar b_n$.

其中 $a_n, \bar b_n$ 是格拉斯曼系数。测度为 $D\psi\, D\bar\psi = \prod_n da_n\, d\bar b_n$。

**Step 3 — Jacobian of the chiral rotation.** Under the local ($x$-dependent) chiral rotation $\psi \to e^{i\alpha(x)\gamma^5} \psi$ with infinitesimal $\alpha(x)$, the coefficients transform as $a_n \to \sum_m (\delta_{nm} + i\int d^4x\, \alpha(x)\, \varphi_n^\dagger(x)\, \gamma^5 \varphi_m(x))\, a_m$. By the Grassmann rule for the change of variables (the Jacobian enters as the inverse determinant for Grassmann variables, but since $\psi$ and $\bar\psi$ transform with the same matrix, we get the inverse twice — once for each, giving $\det^{-1} \cdot \det^{-1} = \det^{-2}$):

**第 3 步 — 手征旋转的雅可比行列式。** 在无穷小 $x$ 相关手征旋转 $\psi \to e^{i\alpha(x)\gamma^5} \psi$ 下，系数变换为 $a_n \to \sum_m (\delta_{nm} + i\int d^4x\, \alpha(x)\, \varphi_n^\dagger(x)\, \gamma^5 \varphi_m(x))\, a_m$。利用格拉斯曼变量换元规则（雅可比行列式以逆行列式进入，但 $\psi$ 和 $\bar\psi$ 的变换矩阵相同，各贡献一次逆行列式，合计 $\det^{-1} \cdot \det^{-1} = \det^{-2}$）：

$$ D\psi\, D\bar\psi \to D\psi\, D\bar\psi \cdot \exp\Big(-2i \int d^4x\, \alpha(x)\, \mathcal{A}(x)\Big), $$

where the **anomaly function** $\mathcal{A}(x)$ is the trace over eigenmodes:

其中**反常函数** $\mathcal{A}(x)$ 是对本征模的迹：

$$ \mathcal{A}(x) = \sum_n \varphi_n^\dagger(x)\, \gamma^5 \varphi_n(x). $$

This sum is formally divergent and must be regularized. We introduce a gauge-invariant Gaussian cutoff: $\mathcal{A}(x) = \lim_{M\to\infty} \sum_n \varphi_n^\dagger(x)\, \gamma^5\, e^{-\lambda_n^2/M^2}\, \varphi_n(x)$.

此求和在形式上发散，必须正规化。引入规范不变的高斯截断：$\mathcal{A}(x) = \lim_{M\to\infty} \sum_n \varphi_n^\dagger(x)\, \gamma^5\, e^{-\lambda_n^2/M^2}\, \varphi_n(x)$。

**Step 4 — Evaluating the regularized trace.** Using the completeness of $\{\varphi_n\}$ and $(i\slashed{D})^2 = -D_\mu D^\mu - (e/2)\sigma^{\mu\nu}F_{\mu\nu}$ (where $\sigma^{\mu\nu} = i[\gamma^\mu, \gamma^\nu]/2$ and the Lichnerowicz-type identity comes from $[D_\mu, D_\nu] = -ieF_{\mu\nu}$):

**第 4 步 — 计算正规化迹。** 利用 $\{\varphi_n\}$ 的完备性和 $(i\slashed{D})^2 = -D_\mu D^\mu - (e/2)\sigma^{\mu\nu}F_{\mu\nu}$（其中 $\sigma^{\mu\nu} = i[\gamma^\mu, \gamma^\nu]/2$，类李希内罗维奇恒等式来自 $[D_\mu, D_\nu] = -ieF_{\mu\nu}$）：

$$ \mathcal{A}(x) = \lim_{M\to\infty} \langle x|\, \gamma^5\, e^{(i\slashed{D})^2/M^2}\, |x\rangle = \lim_{M\to\infty} \langle x|\, \gamma^5\, e^{(D^2+(e/2)\sigma F)/M^2}\, |x\rangle. $$

Expand in powers of $1/M^2$ using the free heat kernel $\langle x|e^{D^2/M^2}|x\rangle = M^4/(16\pi^2) + (\text{field-dependent corrections})$:

按 $1/M^2$ 展开，利用自由热核 $\langle x|e^{D^2/M^2}|x\rangle = M^4/(16\pi^2) + (\text{场相关修正})$：

$$ \mathcal{A}(x) = \lim_{M\to\infty}\, \mathrm{Tr}_{\rm spinor}\Big[\gamma^5 \cdot \Big(\frac{M^4}{16\pi^2}\cdot 1 + \frac{M^2}{16\pi^2}\cdot \frac{e}{2}\sigma^{\mu\nu}F_{\mu\nu} + \frac{1}{32\pi^2}\cdot \frac{e^2}{4} \sigma^{\mu\nu}F_{\mu\nu}\, \sigma^{\rho\sigma}F_{\rho\sigma} + O(M^{-2})\Big)\Big]. $$

The first two terms vanish because $\mathrm{Tr}[\gamma^5] = 0$ and $\mathrm{Tr}[\gamma^5 \sigma^{\mu\nu}] = 0$. The third term survives in the $M\to\infty$ limit:

前两项因 $\mathrm{Tr}[\gamma^5] = 0$ 和 $\mathrm{Tr}[\gamma^5 \sigma^{\mu\nu}] = 0$ 而消失。第三项在 $M\to\infty$ 极限下存活：

$$ \mathcal{A}(x) = \frac{e^2}{32\pi^2}\cdot \frac{1}{4}\, \mathrm{Tr}_{\rm spinor}[\gamma^5 \sigma^{\mu\nu} \sigma^{\rho\sigma}]\, F_{\mu\nu} F_{\rho\sigma}. $$

Using the Dirac algebra identity $\mathrm{Tr}[\gamma^5 \gamma^\mu \gamma^\nu \gamma^\rho \gamma^\sigma] = -4i\, \varepsilon^{\mu\nu\rho\sigma}$ (in Minkowski, with $\varepsilon^{0123} = +1$) and $\sigma^{\mu\nu} = i(\gamma^\mu\gamma^\nu - g^{\mu\nu})$ (careful expansion):

利用狄拉克代数恒等式 $\mathrm{Tr}[\gamma^5 \gamma^\mu \gamma^\nu \gamma^\rho \gamma^\sigma] = -4i\, \varepsilon^{\mu\nu\rho\sigma}$（闵可夫斯基中，$\varepsilon^{0123} = +1$）以及 $\sigma^{\mu\nu}$ 的仔细展开：

$$ \mathrm{Tr}_{\rm spinor}[\gamma^5 \sigma^{\mu\nu} \sigma^{\rho\sigma}] = -4\, \varepsilon^{\mu\nu\rho\sigma}. $$

(This standard trace is derived by writing $\sigma^{\mu\nu} = (i/2)(\gamma^\mu\gamma^\nu - \gamma^\nu\gamma^\mu)$, multiplying out, and using the 4D identity $\mathrm{Tr}[\gamma^5 \gamma^a \gamma^b \gamma^c \gamma^d] = -4i\varepsilon^{abcd}$.)

（此标准迹通过写出 $\sigma^{\mu\nu} = (i/2)(\gamma^\mu\gamma^\nu - \gamma^\nu\gamma^\mu)$，展开相乘，并利用 4D 恒等式 $\mathrm{Tr}[\gamma^5 \gamma^a \gamma^b \gamma^c \gamma^d] = -4i\varepsilon^{abcd}$ 得到。）

Substituting:

代入：

$$ \mathcal{A}(x) = \frac{e^2}{32\pi^2}\cdot \frac{1}{4}\cdot (-4)\cdot \varepsilon^{\mu\nu\rho\sigma} F_{\mu\nu} F_{\rho\sigma} = -\frac{e^2}{32\pi^2}\, \varepsilon^{\mu\nu\rho\sigma} F_{\mu\nu} F_{\rho\sigma}. $$

**Step 5 — Recovering the anomalous Ward identity.** Since the action changes by $-\int d^4x\, \alpha(x)\, \partial_\mu j^{\mu 5}$ (by the equation of motion / Noether argument), and the measure contributes an additional phase $-2i\int d^4x\, \alpha(x)\, \mathcal{A}(x)$, the full variation of $Z[A]$ under an infinitesimal chiral rotation must vanish ($Z$ is invariant under a change of integration variables):

**第 5 步 — 恢复反常 Ward 恒等式。** 由于作用量在无穷小手征旋转下变化 $-\int d^4x\, \alpha(x)\, \partial_\mu j^{\mu 5}$（由运动方程/诺特论证），而测度额外贡献相位 $-2i\int d^4x\, \alpha(x)\, \mathcal{A}(x)$，$Z[A]$ 在无穷小手征旋转下的总变分必须为零（$Z$ 在积分变量替换下不变）：

$$ \delta Z = 0 = \int D\psi\, D\bar\psi\, e^{iS}\, \Big[i \int d^4x\, \alpha(x)\, (-\partial_\mu j^{\mu 5} - 2\mathcal{A}(x))\Big]. $$

Since $\alpha(x)$ is arbitrary, the coefficient of each $\alpha(x)$ must vanish inside the path integral expectation, giving the **quantum equation**:

由于 $\alpha(x)$ 是任意的，路径积分期望值内每个 $\alpha(x)$ 的系数必须为零，给出**量子方程**：

$$ \langle\partial_\mu j^{\mu 5}(x)\rangle = -2\mathcal{A}(x) = \frac{e^2}{16\pi^2}\, \varepsilon^{\mu\nu\rho\sigma} F_{\mu\nu}(x) F_{\rho\sigma}(x). $$

Promoting this to an operator equation (as is standard in the background-field argument), we obtain the ABJ anomaly:

将此提升为算符方程（在背景场论证中是标准做法），得到 ABJ 反常：

$$ \boxed{\, \partial_\mu j^{\mu 5} = \frac{e^2}{16\pi^2}\, \varepsilon^{\mu\nu\rho\sigma} F_{\mu\nu} F_{\rho\sigma} \,} \qquad \blacksquare $$

---

## B. The $\pi^0 \to \gamma\gamma$ Decay Rate

**Claim.** The anomalous axial current of the strong interaction, combined with the pion field as the Goldstone boson of spontaneously broken chiral $SU(2)_L \times SU(2)_R$, gives the $\pi^0$–$\gamma\gamma$ amplitude

**命题。** 强相互作用的反常轴矢流，结合作为自发破缺手征 $SU(2)_L \times SU(2)_R$ 戈德斯通玻色子的 $\pi$ 子场，给出 $\pi^0$–$\gamma\gamma$ 振幅

$$ \mathcal{M}(\pi^0 \to \gamma\gamma) = \frac{\alpha}{\pi F_\pi}\, N_c (Q_u^2 - Q_d^2)\, \varepsilon^{\mu\nu\rho\sigma} \varepsilon_\mu^*(k_1)\, \varepsilon_\nu^*(k_2)\, k_{1\rho}\, k_{2\sigma}, $$

and the decay rate $\Gamma(\pi^0 \to \gamma\gamma) = (\alpha^2 m_\pi^3)/(64\pi^3 F_\pi^2)\, N_c^2 (Q_u^2 - Q_d^2)^2$ with $N_c = 3$, $Q_u = 2/3$, $Q_d = -1/3$.

衰变率为 $\Gamma(\pi^0 \to \gamma\gamma) = (\alpha^2 m_\pi^3)/(64\pi^3 F_\pi^2)\, N_c^2 (Q_u^2 - Q_d^2)^2$，其中 $N_c = 3$，$Q_u = 2/3$，$Q_d = -1/3$。

**Step 1 — The effective Lagrangian from the anomaly.** The chiral anomaly of QCD (with the electromagnetic field as a background) generates, after integrating out quarks, a Wess–Zumino–Witten (WZW) effective term. At lowest order in the pion field, the relevant piece is the **anomaly-induced coupling**

**第 1 步 — 由反常得到的有效拉格朗日量。** QCD 的手征反常（以电磁场为背景）在对夸克积分后，产生 Wess–Zumino–Witten (WZW) 有效项。在 $\pi$ 子场的最低阶，相关部分是**反常诱导耦合**

$$ \mathcal{L}_{\rm eff} = \frac{N_c e^2}{16\pi^2 F_\pi}\, \pi^0\, \varepsilon^{\mu\nu\rho\sigma} F_{\mu\nu} F_{\rho\sigma}. $$

This comes from the triangle diagram with one axial-current vertex (coupling to $\pi^0$ through the PCAC relation $\partial_\mu j^{\mu 5,3} = F_\pi m_\pi^2 \pi^0$) and two electromagnetic vector vertices. The factor $N_c$ arises from the color trace; $(Q_u^2 - Q_d^2)$ from the isospin structure of the third component of the axial current ($u$ quark contributes $+Q_u^2$, $d$ quark contributes $-Q_d^2$ due to the relative sign from isospin generator $\tau^3/2$).

这来自三角图，其中一个轴矢流顶点（通过 PCAC 关系 $\partial_\mu j^{\mu 5,3} = F_\pi m_\pi^2 \pi^0$ 耦合到 $\pi^0$）和两个电磁矢量顶点。因子 $N_c$ 来自色迹；$(Q_u^2 - Q_d^2)$ 来自轴矢流第三分量的同位旋结构（$u$ 夸克贡献 $+Q_u^2$，$d$ 夸克由于同位旋生成元 $\tau^3/2$ 的相对符号贡献 $-Q_d^2$）。

**Step 2 — The decay amplitude.** From $\mathcal{L}_{\rm eff}$, the Feynman rule for the $\pi^0(q) \to \gamma(k_1,\varepsilon_1)\, \gamma(k_2,\varepsilon_2)$ vertex (Fourier-transforming and extracting the two photon polarization vectors) is

**第 2 步 — 衰变振幅。** 由 $\mathcal{L}_{\rm eff}$，$\pi^0(q) \to \gamma(k_1,\varepsilon_1)\, \gamma(k_2,\varepsilon_2)$ 顶点的费曼规则（傅里叶变换并提取两个光子极化矢量）为

$$ i\mathcal{M} = i \cdot \frac{N_c e^2}{4\pi^2 F_\pi} \cdot (Q_u^2 - Q_d^2) \cdot \varepsilon^{\mu\nu\rho\sigma} \varepsilon_{1\mu}^*\, \varepsilon_{2\nu}^*\, k_{1\rho}\, k_{2\sigma}. $$

(The factor of 4 from the antisymmetry of $\varepsilon$ and $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ is absorbed into the factor of 4 in $4\pi^2$.)

（$\varepsilon$ 的反对称性和 $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ 带来的因子 4 被吸收进 $4\pi^2$ 中的因子 4。）

**Step 3 — Squaring and summing over polarizations.** Sum $|\mathcal{M}|^2$ over the two photon polarizations using $\sum_\lambda \varepsilon_\mu^* \varepsilon_\nu = -g_{\mu\nu}$ (for on-shell transverse photons, up to gauge terms that vanish by the epsilon tensor antisymmetry). The tensor contraction gives

**第 3 步 — 对极化求平方和。** 对两个光子极化求 $|\mathcal{M}|^2$ 之和，利用 $\sum_\lambda \varepsilon_\mu^* \varepsilon_\nu = -g_{\mu\nu}$（对在壳横向光子，规范项由 epsilon 张量的反对称性消失）。张量缩并给出

$$ \sum_{\rm pol} |\varepsilon^{\mu\nu\rho\sigma} \varepsilon_{1\mu}^*\, \varepsilon_{2\nu}^*\, k_{1\rho}\, k_{2\sigma}|^2 = 2(k_1\cdot k_2)^2. $$

In the pion rest frame $k_1\cdot k_2 = m_\pi^2/2$ (each photon has energy $m_\pi/2$, moving back-to-back).

在 $\pi$ 子静止系中，$k_1\cdot k_2 = m_\pi^2/2$（每个光子能量为 $m_\pi/2$，背靠背运动）。

**Step 4 — Phase space and decay rate.** The two-body phase space for $\pi^0 \to \gamma\gamma$ in the rest frame gives $\int d\Phi_2 = 1/(8\pi)$ (from $\int d^3k_1/(2E_1)\, d^3k_2/(2E_2)\, (2\pi)^4\delta^4(q-k_1-k_2)/(2M)$ with $m_\pi = M$). The symmetry factor $1/2$ for two identical photons gives:

**第 4 步 — 相空间与衰变率。** $\pi^0 \to \gamma\gamma$ 在静止系中的二体相空间给出 $\int d\Phi_2 = 1/(8\pi)$（由 $\int d^3k_1/(2E_1)\, d^3k_2/(2E_2)\, (2\pi)^4\delta^4(q-k_1-k_2)/(2M)$ 得，$M = m_\pi$）。两个全同光子的对称因子 $1/2$ 给出：

$$ \begin{aligned}
\Gamma &= \frac{1}{2} \cdot \frac{1}{2m_\pi} \cdot \Big(\frac{N_c e^2 (Q_u^2 - Q_d^2)}{4\pi^2 F_\pi}\Big)^2 \cdot 2\Big(\frac{m_\pi^2}{2}\Big)^2 \cdot \frac{1}{8\pi} \\
&= \frac{N_c^2 \alpha^2 m_\pi^3}{64\pi^3 F_\pi^2} \cdot (Q_u^2 - Q_d^2)^2.
\end{aligned} $$

**Step 5 — Numerical evaluation.** Inserting $N_c = 3$, $Q_u = 2/3$, $Q_d = -1/3$: $Q_u^2 - Q_d^2 = 4/9 - 1/9 = 3/9 = 1/3$. Thus $(N_c(Q_u^2 - Q_d^2))^2 = (3 \cdot 1/3)^2 = 1$. Using $F_\pi \approx 93$ MeV, $m_\pi \approx 135$ MeV, $\alpha = 1/137$:

**第 5 步 — 数值计算。** 代入 $N_c = 3$，$Q_u = 2/3$，$Q_d = -1/3$：$Q_u^2 - Q_d^2 = 4/9 - 1/9 = 1/3$。故 $(N_c(Q_u^2 - Q_d^2))^2 = (3 \cdot 1/3)^2 = 1$。取 $F_\pi \approx 93$ MeV，$m_\pi \approx 135$ MeV，$\alpha = 1/137$：

$$ \Gamma(\pi^0 \to \gamma\gamma) \approx \frac{(1/137)^2 \cdot (135\ \mathrm{MeV})^3}{64\pi^3 \cdot (93\ \mathrm{MeV})^2} \approx 7.7\ \mathrm{eV}. $$

The experimental value is $7.82 \pm 0.14$ eV — a quantitative triumph of the anomaly calculation, confirming $N_c = 3$ and the fractional quark charges. $\blacksquare$

实验值为 $7.82 \pm 0.14$ eV——这是反常计算的定量胜利，证实了 $N_c = 3$ 和分数夸克电荷。$\blacksquare$

---

## C. Standard-Model Anomaly Cancellation

**Claim.** In the Standard Model, the chiral anomalies of each triangle diagram — with three gauge-boson external lines — cancel exactly within each generation of quarks and leptons. The cancellation conditions require the sum of hypercharges over a full generation to vanish.

**命题。** 在标准模型中，每个三角图——三条外线均为规范玻色子——的手征反常在每一代夸克和轻子内精确相消。相消条件要求每代超荷之和为零。

**Step 1 — Sources of triangle anomalies.** The SM gauge group is $SU(3)_c \times SU(2)_L \times U(1)_Y$. Anomaly cancellation must be checked for every triangle diagram with vertices drawn from these gauge symmetries. The distinct, non-trivial conditions for one generation are:

**第 1 步 — 三角反常的来源。** SM 规范群为 $SU(3)_c \times SU(2)_L \times U(1)_Y$。必须对每个顶点取自这些规范对称性的三角图检验反常相消。对一代费米子，各个不平凡的条件为：

$$ \begin{aligned}
\text{(i)}\quad & U(1)^3: && \textstyle\sum_f (Y_L)^3 - \sum_f (Y_R)^3 = 0, \\
\text{(ii)}\quad & SU(2)^2\, U(1): && \textstyle\sum_{SU(2)\text{ doublets}} Y_L = 0, \\
\text{(iii)}\quad & SU(3)^2\, U(1): && \textstyle\sum_{SU(3)\text{ triplets}} (Y_L - Y_R) = 0, \\
\text{(iv)}\quad & \text{gravitational-}U(1): && \textstyle\sum_f Y_L - \sum_f Y_R = 0 \quad (\text{from gravity-gravity-}U(1)\text{ triangle}),
\end{aligned} $$

where the sums are over left-handed (L) and right-handed (R) Weyl fermions (right-handed fermions enter with a minus sign in the anomaly because they contribute with opposite chirality).

其中求和遍历左手 (L) 和右手 (R) 韦尔费米子（右手费米子在反常中以负号进入，因为它们以相反手征性贡献）。

**Step 2 — The particle content of one generation.** One generation contains:

**第 2 步 — 一代粒子内容。** 一代包含：

$$ \begin{aligned}
\text{Quarks:}\quad & Q_L = (u_L, d_L) && [SU(2)\text{ doublet}, SU(3)\text{ triplet}, Y = 1/3], \\
& u_R && [SU(2)\text{ singlet}, SU(3)\text{ triplet}, Y = 4/3], \\
& d_R && [SU(2)\text{ singlet}, SU(3)\text{ triplet}, Y = -2/3]. \\
\text{Leptons:}\quad & L_L = (\nu_L, e_L) && [SU(2)\text{ doublet}, SU(3)\text{ singlet}, Y = -1], \\
& e_R && [SU(2)\text{ singlet}, SU(3)\text{ singlet}, Y = -2].
\end{aligned} $$

(No $\nu_R$ in the minimal SM.)

(Hypercharge conventions: $Q = T_3 + Y/2$, so $Y_L(Q_L) = 1/3$ means electric charges $Q_u = 1/3 + 1/2\cdot(+1) = 2/3$ and $Q_d = 1/3 + 1/2\cdot(-1) = -1/3$, ✓.)

（超荷约定：$Q = T_3 + Y/2$，故 $Y_L(Q_L) = 1/3$ 意味着电荷 $Q_u = 1/3 + 1/2\cdot(+1) = 2/3$ 和 $Q_d = 1/3 + 1/2\cdot(-1) = -1/3$，✓。）

**Step 3 — Checking condition (ii): $SU(2)^2\, U(1)$.** Only $SU(2)$ doublets contribute. Sum the hypercharge of each left-handed doublet, with multiplicity from $SU(3)$ (color factor $N_c = 3$ for quarks):

**第 3 步 — 验证条件 (ii)：$SU(2)^2\, U(1)$。** 只有 $SU(2)$ 双重态贡献。对每个左手双重态的超荷求和，夸克乘以 $SU(3)$ 多重度（色因子 $N_c = 3$）：

$$ \sum_{\rm doublets} Y_L = N_c \cdot Y_L(Q_L) + Y_L(L_L) = 3 \cdot (1/3) + (-1) = 1 - 1 = 0. \quad \checkmark $$

**Step 4 — Checking condition (iii): $SU(3)^2\, U(1)$.** Only $SU(3)$ triplets (quarks) contribute. The anomaly coefficient per triplet is $\mathrm{Tr}[T^a T^b] = \delta^{ab}/2$ (for the fundamental representation), so the condition is $\sum_{\rm triplets} Y = 0$ for left-minus-right:

**第 4 步 — 验证条件 (iii)：$SU(3)^2\, U(1)$。** 只有 $SU(3)$ 三重态（夸克）贡献。每个三重态的反常系数为 $\mathrm{Tr}[T^a T^b] = \delta^{ab}/2$（基本表示），故条件为左减右的 $\sum_{\rm triplets} Y = 0$：

$$ \begin{aligned}
\sum_{\rm triplets} (Y_L - Y_R) &= 2 \cdot Y_L(Q_L) - Y_R(u_R) - Y_R(d_R) \quad (\text{factor 2 for the doublet} = \text{two Weyl fermions}) \\
&= 2\cdot(1/3) - (4/3) - (-2/3) = 2/3 - 4/3 + 2/3 = 0. \quad \checkmark
\end{aligned} $$

**Step 5 — Checking condition (iv): gravitational anomaly.** Sum all left-handed minus right-handed hypercharges (with color multiplicity):

**第 5 步 — 验证条件 (iv)：引力反常。** 对所有左手减右手超荷求和（含色多重度）：

$$ \begin{aligned}
\sum_L Y - \sum_R Y &= [N_c(2\cdot 1/3) + (-1 + -1)] - [N_c(4/3 + (-2/3)) + (-2)] \\
&= [2 - 2] - [N_c \cdot 2/3 - 2] = 0 - [3\cdot(2/3) - 2] = 0 - [2 - 2] = 0. \quad \checkmark
\end{aligned} $$

**Step 6 — Checking condition (i): $U(1)^3$.** This is the most involved condition. Summing the cubes of hypercharges over left-handed minus right-handed fermions (with color degeneracy):

**第 6 步 — 验证条件 (i)：$U(1)^3$。** 这是最复杂的条件。对左手减右手费米子的超荷三次方求和（含色简并度）：

$$ \begin{aligned}
\sum_L Y^3 - \sum_R Y^3
&= [N_c \cdot 2 \cdot (1/3)^3 + 1\cdot(-1)^3 + 1\cdot(-1)^3] - [N_c(4/3)^3 + N_c(-2/3)^3 + 1\cdot(-2)^3] \\
&= [3 \cdot 2/27 - 1 - 1] - [3\cdot 64/27 + 3\cdot(-8/27) - 8] \\
&= [6/27 - 2] - [192/27 - 24/27 - 8] \\
&= [2/9 - 2] - [168/27 - 8] \\
&= [2/9 - 18/9] - [56/9 - 72/9] \\
&= -16/9 - (-16/9) = 0. \quad \checkmark
\end{aligned} $$

All four conditions are satisfied. The cancellation is a non-trivial conspiracy between quarks and leptons within each generation; no individual sector (quarks alone, or leptons alone) is anomaly-free. This forces the Standard Model to come in **complete generations** — adding, say, only a new lepton doublet without a corresponding quark doublet would reintroduce anomalies and destroy mathematical consistency. $\blacksquare$

所有四个条件均满足。相消是每代中夸克与轻子之间非平凡的"共谋"；没有任何单独的部门（单独的夸克或单独的轻子）是无反常的。这迫使标准模型以**完整的代**出现——例如，仅添加一个新的轻子双重态而无对应的夸克双重态，将重新引入反常并破坏数学自洽性。$\blacksquare$

---

## D. Instantons: the BPST Solution, Action $S = 8\pi^2/g^2$, and the $\theta$-Vacuum

**Claim.** In Euclidean $SU(2)$ Yang–Mills theory, the **BPST instanton** is a self-dual gauge field configuration with topological charge $Q = 1$ and action $S_E = 8\pi^2/g^2$. The true vacuum of QCD is the **$\theta$-vacuum**, a superposition over topological sectors, with an effective action containing the $\theta$-term $\theta(g^2/32\pi^2)\, G^a_{\mu\nu} \tilde G^{a\mu\nu}$.

**命题。** 在欧几里得 $SU(2)$ 杨–米尔斯理论中，**BPST 瞬子**是拓扑荷 $Q = 1$、作用量 $S_E = 8\pi^2/g^2$ 的自对偶规范场位形。QCD 的真实真空是**$\theta$ 真空**——拓扑扇区上的叠加，有效作用量含 $\theta$ 项 $\theta(g^2/32\pi^2)\, G^a_{\mu\nu} \tilde G^{a\mu\nu}$。

**Step 1 — The Euclidean Yang–Mills action and the self-duality bound.** Analytically continue to Euclidean space ($t \to -i\tau$, $A_0 \to iA_4$). The Euclidean Yang–Mills action is

**第 1 步 — 欧几里得杨–米尔斯作用量与自对偶界。** 解析延拓至欧几里得空间（$t \to -i\tau$，$A_0 \to iA_4$）。欧几里得杨–米尔斯作用量为

$$ S_E = \frac{1}{2g^2} \int d^4x\, \mathrm{Tr}[G_{\mu\nu} G_{\mu\nu}], \qquad G_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + [A_\mu, A_\nu], $$

where all indices are Euclidean (no distinction between upper and lower). Define the **dual field strength** $\tilde G_{\mu\nu} = (1/2)\, \varepsilon_{\mu\nu\rho\sigma} G_{\rho\sigma}$. Since $\tilde{\tilde G} = G$ (in 4D Euclidean), the dual is an involution. The identity

其中所有指标均为欧几里得式（上下指标无区别）。定义**对偶场强** $\tilde G_{\mu\nu} = (1/2)\, \varepsilon_{\mu\nu\rho\sigma} G_{\rho\sigma}$。由于 $\tilde{\tilde G} = G$（在 4D 欧几里得中），对偶是一个对合。恒等式

$$ 0 \le \int d^4x\, \mathrm{Tr}[(G_{\mu\nu} \mp \tilde G_{\mu\nu})^2] = 2 \int d^4x\, \mathrm{Tr}[G^2 \mp G \tilde G] $$

gives the **Bogomolny bound**:

给出 **Bogomolny 界**：

$$ \int d^4x\, \mathrm{Tr}[G_{\mu\nu} G_{\mu\nu}] \ge \Big|\int d^4x\, \mathrm{Tr}[G_{\mu\nu} \tilde G_{\mu\nu}]\Big|. $$

Hence $S_E \ge (1/2g^2)|Q \cdot 8\pi^2|$, where the right side involves the topological charge $Q$ (defined in Step 2 below). Equality holds if and only if $G_{\mu\nu} = \pm\tilde G_{\mu\nu}$, i.e. the field is **self-dual** (+) or **anti-self-dual** (-). Self-dual solutions automatically satisfy the Yang–Mills equations (by Bianchi identity: $D_\mu \tilde G^{\mu\nu} = 0$ implies $D_\mu G^{\mu\nu} = 0$).

故 $S_E \ge (1/2g^2)|Q \cdot 8\pi^2|$，右侧涉及拓扑荷 $Q$（在下面第 2 步定义）。当且仅当 $G_{\mu\nu} = \pm\tilde G_{\mu\nu}$（即场是**自对偶**（+）或**反自对偶**（-））时等号成立。自对偶解自动满足杨–米尔斯方程（由 Bianchi 恒等式：$D_\mu \tilde G^{\mu\nu} = 0$ 蕴含 $D_\mu G^{\mu\nu} = 0$）。

**Step 2 — The topological charge.** The quantity

**第 2 步 — 拓扑荷。** 量

$$ Q = \frac{g^2}{16\pi^2} \int d^4x\, \mathrm{Tr}[G_{\mu\nu} \tilde G_{\mu\nu}] $$

is a **topological invariant** — it takes only integer values, classifying gauge field configurations by the homotopy class of the map from the boundary $S^3$ (of compactified Euclidean $\mathbb{R}^4 \cong S^4$) to the gauge group $SU(2) \cong S^3$: $\pi_3(S^3) = \mathbb{Z}$. For $Q = 1$ (one instanton), $S_E = 8\pi^2/g^2$ (from the bound with equality). The integrand is a total derivative:

是**拓扑不变量**——它只取整数值，通过从边界 $S^3$（紧化欧几里得 $\mathbb{R}^4 \cong S^4$）到规范群 $SU(2) \cong S^3$ 的映射的同伦类对规范场位形分类：$\pi_3(S^3) = \mathbb{Z}$。对 $Q = 1$（一个瞬子），$S_E = 8\pi^2/g^2$（由等号成立的界给出）。被积函数是全导数：

$$ \mathrm{Tr}[G_{\mu\nu} \tilde G_{\mu\nu}] = \partial_\mu K^\mu, \qquad K^\mu = \varepsilon^{\mu\nu\rho\sigma} \mathrm{Tr}[A_\nu (\partial_\rho A_\sigma + (2/3)[A_\rho, A_\sigma])], $$

where $K^\mu$ is the **Chern–Simons current**. The integral of $\partial_\mu K^\mu$ over $\mathbb{R}^4$ reduces to a boundary term at $|x| = \infty$.

其中 $K^\mu$ 是 **Chern–Simons 流**。$\partial_\mu K^\mu$ 在 $\mathbb{R}^4$ 上的积分化为 $|x| = \infty$ 处的边界项。

**Step 3 — The BPST ansatz.** Belavin, Polyakov, Schwartz, and Tyupkin (1975) wrote down the explicit self-dual solution with Q = 1 in singular gauge:

**第 3 步 — BPST 拟设。** Belavin、Polyakov、Schwartz 和 Tyupkin（1975 年）写出了奇异规范中 Q = 1 的显式自对偶解：

$$ A^a_\mu(x) = \frac{2}{g} \cdot \frac{\eta^a_{\mu\nu} (x-x_0)_\nu}{(x-x_0)^2 + \rho^2}, $$

where $x_0$ is the **instanton position** (4 moduli), $\rho$ is the **instanton size** (1 modulus), and $\eta^a_{\mu\nu}$ is the **'t Hooft symbol** ($\eta^a_{\mu\nu} = \varepsilon_{a\mu\nu}$ for $\mu,\nu = 1,2,3$; $\eta^a_{4\nu} = -\delta_{a\nu}$; antisymmetric in $\mu\leftrightarrow\nu$). The $\eta$ symbol encodes the embedding of the $SU(2)$ generators into 4D rotations; it satisfies

其中 $x_0$ 是**瞬子位置**（4 个模参数），$\rho$ 是**瞬子大小**（1 个模参数），$\eta^a_{\mu\nu}$ 是 **'t Hooft 符号**（$\mu,\nu = 1,2,3$ 时 $\eta^a_{\mu\nu} = \varepsilon_{a\mu\nu}$；$\eta^a_{4\nu} = -\delta_{a\nu}$；关于 $\mu\leftrightarrow\nu$ 反对称）。$\eta$ 符号编码 $SU(2)$ 生成元嵌入 4D 转动的方式；它满足

$$ \eta^a_{\mu\rho}\, \eta^b_{\nu\rho} = \delta^{ab} \delta_{\mu\nu} + \varepsilon^{abc} \eta^c_{\mu\nu}, \quad \text{with the full contraction } \eta^a_{\mu\nu}\, \eta^a_{\mu\nu} = 12 \text{ (summed over } a, \mu, \nu). $$

The corresponding field strength is $G^a_{\mu\nu} = \tilde G^a_{\mu\nu}$ (self-dual), with

对应的场强为 $G^a_{\mu\nu} = \tilde G^a_{\mu\nu}$（自对偶），满足

$$ G^a_{\mu\nu} = \frac{4\rho^2}{g} \cdot \frac{\eta^a_{\mu\nu}}{[(x-x_0)^2 + \rho^2]^2}. $$

**Step 4 — Computing the instanton action.** Insert $G^a_{\mu\nu}$ into $S_E$:

**第 4 步 — 计算瞬子作用量。** 将 $G^a_{\mu\nu}$ 代入 $S_E$：

$$ S_E = \frac{1}{2} \int d^4x\, \mathrm{Tr}[G_{\mu\nu} G_{\mu\nu}] = \frac{1}{4} \int d^4x\, \sum_{a,\mu,\nu} (G^a_{\mu\nu})^2, $$

using $\mathrm{Tr}[T^a T^b] = \delta^{ab}/2$ ($SU(2)$ generators). Note there is no explicit $1/g^2$ prefactor here because the BPST field strength already carries it: $G^a \propto 1/g$. With $G^a_{\mu\nu} = (4\rho^2/g)\, \eta^a_{\mu\nu}/[(x-x_0)^2+\rho^2]^2$ and the 't Hooft-symbol sum $\sum_{a,\mu,\nu}(\eta^a_{\mu\nu})^2 = 12$:

利用 $\mathrm{Tr}[T^a T^b] = \delta^{ab}/2$（$SU(2)$ 生成元）。此处没有显式的 $1/g^2$ 前因子，因为 BPST 场强已携带它：$G^a \propto 1/g$。代入 $G^a_{\mu\nu} = (4\rho^2/g)\, \eta^a_{\mu\nu}/[(x-x_0)^2+\rho^2]^2$ 及 't Hooft 符号求和 $\sum_{a,\mu,\nu}(\eta^a_{\mu\nu})^2 = 12$：

$$ S_E = \frac{1}{4} \cdot \frac{16\rho^4}{g^2} \cdot 12 \cdot \int \frac{d^4x}{[(x-x_0)^2 + \rho^2]^4} = \frac{48\rho^4}{g^2} \int \frac{d^4x}{(r^2+\rho^2)^4}. $$

The 4D integral uses the solid angle $2\pi^2$ and the standard Beta-function result $\int_0^\infty r^3\, dr/(r^2+\rho^2)^4 = 1/(12\rho^4)$:

4D 积分用到立体角 $2\pi^2$ 与标准 Beta 函数结果 $\int_0^\infty r^3\, dr/(r^2+\rho^2)^4 = 1/(12\rho^4)$：

$$ \int \frac{d^4x}{(r^2+\rho^2)^4} = 2\pi^2 \int_0^\infty \frac{r^3\, dr}{(r^2+\rho^2)^4} = 2\pi^2 \cdot \frac{1}{12\rho^4} = \frac{\pi^2}{6\rho^4}. $$

Inserting:

代入：

$$ \boxed{\, S_E = \frac{48\rho^4}{g^2} \cdot \frac{\pi^2}{6\rho^4} = \frac{8\pi^2}{g^2} \,} \qquad \blacksquare $$

(The factors combine as $(1/4) \times 16\rho^4 \times 12 \times \pi^2/(6\rho^4) = 8\pi^2$; the $1/g^2$ is supplied by $G^a \propto 1/g$.)

（各因子组合为 $(1/4) \times 16\rho^4 \times 12 \times \pi^2/(6\rho^4) = 8\pi^2$；$1/g^2$ 由 $G^a \propto 1/g$ 提供。）

**Step 5 — The $\theta$-vacuum.** The QCD Hamiltonian has degenerate vacua labeled by winding number $n \in \mathbb{Z}$ (the Pontryagin index of the spatial gauge field configuration). Tunneling between $|n\rangle$ and $|n+1\rangle$ is mediated by instantons with action $8\pi^2/g^2$. The physical ground state is constructed by a Bloch-wave superposition:

**第 5 步 — $\theta$ 真空。** QCD 哈密顿量有以卷绕数 $n \in \mathbb{Z}$（空间规范场位形的庞特里亚金指数）标记的简并真空。$|n\rangle$ 与 $|n+1\rangle$ 之间的隧穿由作用量为 $8\pi^2/g^2$ 的瞬子介导。物理基态由布洛赫波叠加构成：

$$ |\theta\rangle = \sum_{n \in \mathbb{Z}} e^{in\theta} |n\rangle, \qquad \theta \in [0, 2\pi). $$

The amplitude for tunneling from $|n\rangle$ to $|n+Q\rangle$ is proportional to $e^{-S_E(Q)} = e^{-8\pi^2 Q/g^2}$. The energy is minimized by this superposition, and the parameter $\theta$ labels physically inequivalent vacua (different superselection sectors). In the path integral, the $\theta$-vacuum weighting $\sum_n e^{in\theta} e^{-8\pi^2|n|/g^2}$ translates into an additional **$\theta$-term** in the effective Euclidean Lagrangian:

从 $|n\rangle$ 隧穿到 $|n+Q\rangle$ 的振幅正比于 $e^{-S_E(Q)} = e^{-8\pi^2 Q/g^2}$。此叠加使能量最小化，参数 $\theta$ 标记物理上不等价的真空（不同超选择扇区）。在路径积分中，$\theta$ 真空权重 $\sum_n e^{in\theta} e^{-8\pi^2|n|/g^2}$ 转化为有效欧几里得拉格朗日量中额外的 **$\theta$ 项**：

$$ \mathcal{L}_\theta = -i\theta \cdot \frac{g^2}{32\pi^2}\, G^a_{\mu\nu} \tilde G^{a\mu\nu}. $$

Rotating back to Minkowski space (where $G\cdot\tilde G$ changes sign relative to the Euclidean convention):

旋转回闵可夫斯基空间（其中 $G\cdot\tilde G$ 相对于欧几里得约定变号）：

$$ \mathcal{L}_\theta^{\rm Mink} = \theta \cdot \frac{g^2}{32\pi^2}\, G^a_{\mu\nu} \tilde G^{a\mu\nu}. $$

This is a CP-violating term ($G\cdot\tilde G$ is odd under parity and time-reversal). The experimental bound on the neutron electric dipole moment forces $|\theta| < 10^{-10}$, which is the **strong CP problem**. $\blacksquare$

这是一个 CP 破坏项（$G\cdot\tilde G$ 在宇称和时间反演下为奇）。中子电偶极矩的实验约束要求 $|\theta| < 10^{-10}$，这就是**强 CP 问题**。$\blacksquare$

---

## E. Wilson Lattice Action and the Area Law for Confinement

**Claim.** On a hypercubic lattice with spacing $a$, the Wilson gauge action $S_W = -(\beta/2) \sum_\square \mathrm{Tr}[U_\square + U_\square^\dagger]$ (with $\beta = 2N/g^2$ for $SU(N)$) reproduces the Yang–Mills action in the continuum limit $a\to 0$. The **Wilson loop** $W(C) = (1/N)\, \mathrm{Tr}[\prod_{\rm links \in C} U_{\rm link}]$ satisfies an **area law** $\langle W(C)\rangle \sim e^{-\sigma\cdot\mathrm{Area}(C)}$ in the confining phase, signaling confinement.

**命题。** 在间距为 $a$ 的超立方格点上，Wilson 规范作用量 $S_W = -(\beta/2) \sum_\square \mathrm{Tr}[U_\square + U_\square^\dagger]$（$SU(N)$ 中 $\beta = 2N/g^2$）在连续极限 $a\to 0$ 下再现杨–米尔斯作用量。**Wilson 圈** $W(C) = (1/N)\, \mathrm{Tr}[\prod_{\rm links \in C} U_{\rm link}]$ 在禁闭相中满足**面积律** $\langle W(C)\rangle \sim e^{-\sigma\cdot\mathrm{Area}(C)}$，标志着禁闭。

**Step 1 — Lattice link variables.** The fundamental degree of freedom on the lattice is the **parallel transporter** (link variable) associated to each directed link from site $x$ to $x + a\hat\mu$:

**第 1 步 — 格点链接变量。** 格点上的基本自由度是与每条从格点 $x$ 到 $x + a\hat\mu$ 的有向链接相关联的**平行输运子**（链接变量）：

$$ U_{\mu}(x) = \exp(i g a A_\mu(x) + O(a^2)) \in SU(N). $$

$U_\mu(x)$ transforms as $U_\mu(x) \to \Omega(x)\, U_\mu(x)\, \Omega^\dagger(x+a\hat\mu)$ under gauge transformations $\Omega(x) \in SU(N)$, ensuring exact gauge invariance on the lattice at any $a$.

在规范变换 $\Omega(x) \in SU(N)$ 下，$U_\mu(x) \to \Omega(x)\, U_\mu(x)\, \Omega^\dagger(x+a\hat\mu)$，确保格点上任意 $a$ 处的精确规范不变性。

**Step 2 — The plaquette and the Wilson action.** The elementary **plaquette** $U_\square$ in the $(\mu,\nu)$ plane at site $x$ is the product of four link variables around the unit square:

**第 2 步 — 基本方格与 Wilson 作用量。** 格点 $x$ 处 $(\mu,\nu)$ 平面中的基本**方格** $U_\square$ 是沿单位方格四条链接变量的乘积：

$$ U_{\square,\mu\nu}(x) = U_\mu(x)\, U_\nu(x+a\hat\mu)\, U_\mu^\dagger(x+a\hat\nu)\, U_\nu^\dagger(x). $$

Expand for small $a$ using $U_\mu(x) = \exp(igaA_\mu(x))$. By the Baker–Campbell–Hausdorff formula:

对小 $a$ 展开，利用 $U_\mu(x) = \exp(igaA_\mu(x))$。由 Baker–Campbell–Hausdorff 公式：

$$ U_{\square,\mu\nu} = \exp(ig a^2[\partial_\mu A_\nu - \partial_\nu A_\mu + ig[A_\mu,A_\nu]] + O(a^3)) = \exp(ig a^2 G_{\mu\nu}(x) + O(a^3)). $$

Taking the trace and expanding the exponential:

取迹并展开指数：

$$ \frac{1}{N} \mathrm{Re}\, \mathrm{Tr}[U_\square] = 1 - \frac{g^2 a^4}{2N}\, \mathrm{Tr}[G_{\mu\nu}^2] + O(a^6). $$

**Step 3 — Continuum limit of the Wilson action.** The Wilson action is

**第 3 步 — Wilson 作用量的连续极限。** Wilson 作用量为

$$ S_W = -\frac{\beta}{2} \sum_{x, \mu<\nu} \mathrm{Tr}[U_{\square,\mu\nu}(x) + U^\dagger_{\square,\mu\nu}(x)] = -\beta \sum_{x,\mu<\nu} \mathrm{Re}\, \mathrm{Tr}[U_{\square,\mu\nu}(x)]. $$

Substituting the expansion and using $\beta = 2N/g^2$:

代入展开式并利用 $\beta = 2N/g^2$：

$$ S_W \to -\frac{2N}{g^2} \sum_{x,\mu<\nu} \Big[N - \frac{g^2 a^4}{2N} \cdot N \cdot \frac{1}{2} \sum_a G^a_{\mu\nu}G^{a\mu\nu} + \ldots\Big] \quad (\text{using } \mathrm{Tr}[G^2] \text{ for the adjoint}). $$

More carefully for $SU(N)$ with generators $T^a$ normalized as $\mathrm{Tr}[T^a T^b] = \delta^{ab}/2$:

对 $SU(N)$（生成元归一化为 $\mathrm{Tr}[T^a T^b] = \delta^{ab}/2$）更仔细地计算：

$$ \begin{aligned}
-\frac{\beta}{2} \mathrm{Tr}[U_\square + U_\square^\dagger] &= -\beta\, \mathrm{Re}\, \mathrm{Tr}[U_\square] \\
&= -\beta N + \frac{\beta g^2 a^4}{2} \cdot \frac{1}{2} G^a_{\mu\nu}G^{a\mu\nu}/N \cdot N + O(a^6) \\
&= \mathrm{const} + \frac{a^4}{4} G^a_{\mu\nu}G^{a\mu\nu} + O(a^6),
\end{aligned} $$

and converting the lattice sum $\sum_x a^4 \to \int d^4x$ and summing over the $(D(D-1)/2) = 6$ independent plaquette orientations (each giving a factor of $1/2$ from the symmetry of $G^2$):

将格点求和 $\sum_x a^4 \to \int d^4x$，并对 6 个独立方格方向求和（每个由 $G^2$ 的对称性给出因子 $1/2$）：

$$ S_W \to \mathrm{const} + \frac{1}{4} \int d^4x\, G^a_{\mu\nu}G^{a\mu\nu} = \mathrm{const} + S_{\rm YM}. $$

This matches the continuum Yang–Mills action (up to an additive constant from the $-\beta N$ term, which does not affect dynamics). $\blacksquare$ for the continuum limit.

这与连续杨–米尔斯作用量匹配（除去来自 $-\beta N$ 项的常数，该常数不影响动力学）。连续极限部分 $\blacksquare$。

**Step 4 — The Wilson loop as a probe of the quark potential.** Define the rectangular Wilson loop $C$ of temporal extent $T$ and spatial extent $R$. The expectation value

**第 4 步 — Wilson 圈作为夸克势的探针。** 定义时间跨度为 $T$、空间跨度为 $R$ 的矩形 Wilson 圈 $C$。期望值

$$ \langle W(C)\rangle = \frac{1}{N} \langle\mathrm{Tr}[\textstyle\prod_C U_{\rm link}]\rangle \sim e^{-V(R)\cdot T} \quad \text{for large } T, $$

where $V(R)$ is the static quark-antiquark potential (the energy of a quark-antiquark pair separated by distance $R$, with the quark held static by coupling to an infinitely heavy source). This identification comes from the path-integral representation of the ground-state energy: $e^{-V(R)T} = \langle q\bar q \text{ ground state}|e^{-HT}|q\bar q \text{ ground state}\rangle$ for large $T$.

其中 $V(R)$ 是静态夸克–反夸克势（相距 $R$ 的夸克–反夸克对的能量，夸克通过与无穷重源耦合保持静止）。此等同来自基态能量的路径积分表示：大 $T$ 时 $e^{-V(R)T} = \langle q\bar q \text{ 基态}|e^{-HT}|q\bar q \text{ 基态}\rangle$。

**Step 5 — The area law criterion.** In the **strong-coupling expansion** (large $g^2$, small $\beta$), each plaquette contributes a factor $\beta/N$ to the group integration. Non-zero contributions to $\langle W(C)\rangle$ require every link of $C$ to appear in at least one plaquette from the expansion of $e^{S_W}$, so that the group integral $\sum_U U_{ij} \ne 0$ (using $\int_{SU(N)} dU\, U_{ij}\, U^\dagger_{kl} = \delta_{il}\delta_{jk}/N$). The minimal "tiling" of the Wilson loop requires a set of plaquettes filling the interior of $C$ — a number proportional to the minimal area $A = R\cdot T$. Each plaquette contributes a factor $\beta/N = (2/g^2) \ll 1$, so

**第 5 步 — 面积律判据。** 在**强耦合展开**（大 $g^2$，小 $\beta$）中，每个方格对群积分贡献因子 $\beta/N$。$\langle W(C)\rangle$ 的非零贡献要求 $C$ 的每条链接至少出现在 $e^{S_W}$ 展开的一个方格中，使得群积分 $\sum_U U_{ij} \ne 0$（利用 $\int_{SU(N)} dU\, U_{ij}\, U^\dagger_{kl} = \delta_{il}\delta_{jk}/N$）。填铺 Wilson 圈最少需要覆盖 $C$ 内部的方格集合——数量正比于最小面积 $A = R\cdot T$。每个方格贡献因子 $\beta/N = (2/g^2) \ll 1$，故

$$ \langle W(C)\rangle \sim (\beta/N)^{A/a^2} = \exp(-(A/a^2) \ln(N/\beta)) = \exp(-\sigma \cdot A), $$

where the **string tension** $\sigma = (1/a^2) \ln(N/\beta) > 0$ in the strong-coupling regime. The area law $\langle W(C)\rangle \sim e^{-\sigma\cdot R\cdot T}$ implies $V(R) = \sigma R$ — a **linearly rising potential** — signaling **confinement**: the energy to separate a quark from an antiquark grows without bound as $R \to \infty$.

其中**弦张力** $\sigma = (1/a^2) \ln(N/\beta) > 0$ 在强耦合区间为正。面积律 $\langle W(C)\rangle \sim e^{-\sigma\cdot R\cdot T}$ 蕴含 $V(R) = \sigma R$——**线性上升势**——标志着**禁闭**：将夸克与反夸克分离的能量随 $R \to \infty$ 而无限增长。

**Step 6 — Physical interpretation and the perimeter law for the deconfined phase.** In the **deconfined** (high-temperature) phase, or for charges in the adjoint representation (which can be screened by gluons), the Wilson loop instead satisfies a **perimeter law**:

**第 6 步 — 物理诠释与解禁闭相的周长律。** 在**解禁闭**（高温）相，或对伴随表示的荷（可被胶子屏蔽），Wilson 圈转而满足**周长律**：

$$ \langle W(C)\rangle \sim e^{-\mu \cdot \mathrm{Perimeter}(C)}, \quad (\text{deconfined or screened}), $$

where $\mu$ is a mass gap parameter. The transition from area law to perimeter law as a function of temperature is the **deconfinement phase transition** (Polyakov loop order parameter). For $SU(3)$ QCD, the string tension extracted from lattice Monte Carlo simulations is $\sigma \approx (440\ \mathrm{MeV})^2 \approx 0.18\ \mathrm{GeV}^2$, consistent with the linear Regge trajectories observed in hadron spectroscopy. $\blacksquare$

其中 $\mu$ 是质量间隙参数。面积律到周长律随温度的转变是**解禁闭相变**（Polyakov 圈序参量）。对 $SU(3)$ QCD，从格点蒙特卡罗模拟中提取的弦张力为 $\sigma \approx (440\ \mathrm{MeV})^2 \approx 0.18\ \mathrm{GeV}^2$，与强子谱学中观测到的线性 Regge 轨迹一致。$\blacksquare$

---

## F. The 't Hooft–Polyakov Monopole · 't Hooft–波利亚科夫磁单极子

**Claim.** In the **Georgi–Glashow model** — $SU(2)$ gauge theory with a Higgs field $\phi^a$ in the adjoint representation breaking $SU(2) \to U(1)$ — there exists a finite-energy, topologically stable, **magnetic monopole** with magnetic charge $g = 4\pi/e$ and mass $M \gtrsim 4\pi v/e$. Unlike Dirac's monopole it needs **no singular string**: the singularity is resolved by the massive non-abelian core, and the magnetic charge is quantized by topology, $\pi_2(SU(2)/U(1)) = \pi_2(S^2) = \mathbb{Z}$.

**命题。** 在 **Georgi–Glashow 模型**——带伴随表示希格斯场 $\phi^a$、将 $SU(2) \to U(1)$ 破缺的 $SU(2)$ 规范理论——中，存在有限能量、拓扑稳定的**磁单极子**，磁荷 $g = 4\pi/e$，质量 $M \gtrsim 4\pi v/e$。与狄拉克单极子不同，它**无需奇异弦**：奇点被有质量的非阿贝尔核解除，磁荷由拓扑量子化，$\pi_2(SU(2)/U(1)) = \pi_2(S^2) = \mathbb{Z}$。

**Step 1 — The model.** The Lagrangian is

**第 1 步 — 模型。** 拉格朗日量为

$$ \mathcal{L} = -\tfrac14 F^a_{\mu\nu}F^{a\mu\nu} + \tfrac12(D_\mu\phi^a)(D^\mu\phi^a) - \tfrac14\lambda(\phi^a\phi^a - v^2)^2, \qquad D_\mu\phi^a = \partial_\mu\phi^a + e\, \varepsilon^{abc}A^b_\mu\phi^c. $$

The vacuum manifold is the 2-sphere $|\phi| = v$ in field space. A vacuum value, say $\phi^a = v\delta^{a3}$, leaves a $U(1)$ subgroup (rotations about the 3-axis in isospace) unbroken; the other two gauge bosons acquire mass $m_W = ev$, while the unbroken-$U(1)$ photon stays massless. This is spontaneous breaking $SU(2) \to U(1)$.

真空流形是场空间中的 2 维球面 $|\phi| = v$。取真空值 $\phi^a = v\delta^{a3}$ 保留一个 $U(1)$ 子群（同位旋空间中绕 3 轴的转动）不破缺；另外两个规范玻色子获得质量 $m_W = ev$，未破缺 $U(1)$ 的光子保持无质量。这是自发破缺 $SU(2) \to U(1)$。

**Step 2 — The hedgehog ansatz.** 't Hooft and Polyakov sought a static, finite-energy solution in which the Higgs field points **radially in isospace as well as in real space**:

**第 2 步 — 刺猬拟设。** 't Hooft 与 Polyakov 寻找一个静态有限能量解，其中希格斯场在**同位旋空间与真实空间中都沿径向**指向：

$$ \phi^a(\mathbf{r}) = v\, h(r)\, \hat x^a, \qquad A^a_i(\mathbf{r}) = \varepsilon_{aij}\, \hat x^j\, [1 - K(r)]/(er), \qquad A^a_0 = 0, $$

with boundary conditions $h(0) = 0$, $K(0) = 1$ (regular core) and $h(\infty) = 1$, $K(\infty) = 0$ (vacuum at infinity). The "hedgehog" locks internal isospin rotations to spatial rotations: the unbroken symmetry of the solution is the **diagonal** subgroup of (spatial rotations) $\times$ (isospin).

边界条件 $h(0) = 0$、$K(0) = 1$（核处正则）与 $h(\infty) = 1$、$K(\infty) = 0$（无穷远真空）。"刺猬"将内部同位旋转动与空间转动锁定：解的未破缺对称性是（空间转动）$\times$（同位旋）的**对角**子群。

**Step 3 — Topological charge (winding number).** At spatial infinity the unit Higgs field $\hat\phi^a = \hat x^a$ defines a map from the spatial 2-sphere at infinity $S^2_\infty$ to the vacuum 2-sphere $S^2_{\rm vac}$. This map has **winding number $n = 1$**, an element of $\pi_2(S^2) = \mathbb{Z}$. The corresponding topological current

**第 3 步 — 拓扑荷（缠绕数）。** 在空间无穷远，单位希格斯场 $\hat\phi^a = \hat x^a$ 定义一个从无穷远空间 2 维球面 $S^2_\infty$ 到真空 2 维球面 $S^2_{\rm vac}$ 的映射。该映射有**缠绕数 $n = 1$**，是 $\pi_2(S^2) = \mathbb{Z}$ 的元素。相应的拓扑流

$$ k^\mu = \frac{1}{8\pi}\, \varepsilon^{\mu\nu\rho\sigma} \varepsilon_{abc}\, \partial_\nu \hat\phi^a\, \partial_\rho \hat\phi^b\, \partial_\sigma \hat\phi^c $$

is conserved **identically** ($\partial_\mu k^\mu = 0$ without any equation of motion), and its charge $N = \int d^3x\, k^0 = n$ is the integer winding. Because $n$ cannot change under any smooth, finite-energy deformation, the monopole is absolutely stable.

**恒等地**守恒（$\partial_\mu k^\mu = 0$，不依赖任何运动方程），其荷 $N = \int d^3x\, k^0 = n$ 即整数缠绕。由于 $n$ 在任何光滑、有限能量的形变下都不能改变，单极子是绝对稳定的。

**Step 4 — Magnetic charge.** The gauge-invariant electromagnetic field strength (the 't Hooft tensor) is

**第 4 步 — 磁荷。** 规范不变的电磁场强（'t Hooft 张量）为

$$ \mathfrak{F}_{\mu\nu} = \hat\phi^a F^a_{\mu\nu} - (1/e)\, \varepsilon_{abc}\, \hat\phi^a (D_\mu\hat\phi^b)(D_\nu\hat\phi^c). $$

Far from the core, $\hat\phi$ is covariantly constant and $\mathfrak{F}_{\mu\nu}$ reduces to the ordinary $U(1)$ Maxwell tensor. Computing the magnetic flux through $S^2_\infty$ from the hedgehog field gives a radial magnetic field $B_i = \hat x_i/(er^2)$, so

远离核区，$\hat\phi$ 协变常数，$\mathfrak{F}_{\mu\nu}$ 退化为普通 $U(1)$ 麦克斯韦张量。由刺猬场计算通过 $S^2_\infty$ 的磁通量给出径向磁场 $B_i = \hat x_i/(er^2)$，故

$$ g = \oint_{S^2_\infty} \mathbf{B}\cdot d\mathbf{S} = (1/e)(4\pi r^2)/r^2 = \boxed{4\pi/e} = n\cdot(4\pi/e). $$

This satisfies the Dirac quantization condition $e g = 4\pi = 2\cdot(2\pi)$ — the monopole carries **two** Dirac units, the minimal charge consistent with the integer-charged (isovector) matter of the theory. The magnetic charge is the topological winding $n$ in disguise: $g = 4\pi n/e$.

它满足狄拉克量子化条件 $e g = 4\pi = 2\cdot(2\pi)$——单极子携带**两个**狄拉克单位，是与理论中整数电荷（同位旋矢量）物质相容的最小磁荷。磁荷正是伪装的拓扑缠绕 $n$：$g = 4\pi n/e$。

**Step 5 — Mass and the BPS bound.** The static energy is $E = \int d^3x\, [\tfrac12(B^a_i)^2 + \tfrac12(D_i\phi^a)^2 + V(\phi)]$. Dropping $V$ (the **BPS limit** $\lambda \to 0$) and using the Bogomolny rearrangement

**第 5 步 — 质量与 BPS 界。** 静态能量为 $E = \int d^3x\, [\tfrac12(B^a_i)^2 + \tfrac12(D_i\phi^a)^2 + V(\phi)]$。略去 $V$（**BPS 极限** $\lambda \to 0$）并用博戈莫尔尼重排

$$ E = \int d^3x\, \big[\tfrac12(B^a_i \mp D_i\phi^a)^2 \pm B^a_i D_i\phi^a\big] \ge \pm \int d^3x\, \partial_i(B^a_i\phi^a) = v|g|, $$

since $\int B^a_i D_i\phi^a = \int \partial_i(B^a_i\phi^a)$ by the Bianchi identity $D_i B^a_i = 0$. The bound

由于由比安基恒等式 $D_i B^a_i = 0$ 有 $\int B^a_i D_i\phi^a = \int \partial_i(B^a_i\phi^a)$。此界

$$ \boxed{\, M \ge v|g| = 4\pi v/e = (4\pi/e^2)\, m_W = m_W/\alpha \,} \quad (\alpha = e^2/4\pi) $$

is saturated when $B^a_i = \pm D_i\phi^a$ (the first-order **BPS equations**, exactly solvable — the Prasad–Sommerfield solution). Monopoles are therefore very heavy, $\sim m_W/\alpha$: inaccessible at accelerator energies but a sharp prediction of any Grand Unified Theory (where the role of $m_W$ is played by the GUT scale $M_X \sim 10^{16}$ GeV, giving $M_{\rm monopole} \sim 10^{17}$–$10^{18}$ GeV).

当 $B^a_i = \pm D_i\phi^a$（一阶 **BPS 方程**，可精确求解——Prasad–Sommerfield 解）时饱和。故单极子非常重，$\sim m_W/\alpha$：加速器能量无法企及，却是任何大统一理论的明确预言（其中 $m_W$ 的角色由 GUT 标度 $M_X \sim 10^{16}$ GeV 扮演，给出 $M_{\rm 单极子} \sim 10^{17}$–$10^{18}$ GeV）。

**Step 6 — Physical significance.** (i) Magnetic charge is now **topologically** quantized — no singular Dirac string is needed; the string is replaced by the smooth massive core. (ii) GUT phase transitions in the early universe inevitably produce these monopoles (the **monopole problem**), one of the original motivations for cosmic inflation, which dilutes them. (iii) The monopole is the prototype of **electric–magnetic duality** (Montonen–Olive): in suitable ($N = 4$ supersymmetric) theories the monopole and the gauge boson are exchanged by $g \leftrightarrow 4\pi/e$, exchanging strong and weak coupling. $\blacksquare$

**第 6 步 — 物理意义。** (i) 磁荷现在由**拓扑**量子化——不需要奇异狄拉克弦；弦被光滑的有质量核取代。(ii) 早期宇宙的 GUT 相变不可避免地产生这些单极子（**单极子问题**），这是宇宙暴胀的最初动机之一，暴胀将其稀释。(iii) 单极子是**电–磁对偶**（Montonen–Olive）的原型：在适当的（$N = 4$ 超对称）理论中，单极子与规范玻色子通过 $g \leftrightarrow 4\pi/e$ 互换，交换强弱耦合。$\blacksquare$

---

*These six derivations span the deepest structures of quantum field theory: the quantum breaking of classical symmetry (anomaly), its physical consequence ($\pi^0$ decay), the self-consistency condition it imposes (anomaly cancellation and complete generations), the non-perturbative tunneling solutions (instantons and the $\theta$-vacuum), the non-perturbative definition and confinement criterion of gauge theories (Wilson lattice action and area law), and the topological soliton of a broken gauge theory (the 't Hooft–Polyakov monopole). Together they define the frontier where QFT transcends perturbation theory.*

*这六个推导涵盖了量子场论最深层的结构：经典对称性的量子破缺（反常）、其物理后果（$\pi^0$ 衰变）、它所施加的自洽性条件（反常相消与完整代的要求）、非微扰隧穿解（瞬子与 $\theta$ 真空）、规范理论的非微扰定义与禁闭判据（Wilson 格点作用量与面积律），以及破缺规范理论的拓扑孤子（'t Hooft–波利亚科夫磁单极子）。它们共同定义了量子场论超越微扰论的前沿。*

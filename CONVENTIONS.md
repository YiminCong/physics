# Conventions & Notation · 约定与记号

A single reference for the unit systems, sign conventions, and symbols used across the
curriculum. Physics spanning electromagnetism, relativity, and quantum field theory mixes
several conventions by tradition — this page states which one each part uses, so a symbol
never means two things without warning.

一份贯穿全课程的单位制、符号约定与记号速查表。横跨电磁学、相对论与量子场论的物理会按传统混用多种约定——本页明确各部分采用哪一种，避免同一符号在无提示下表示两种含义。

---

## 1. Unit systems · 单位制

| Domain · 领域 | Units · 单位 | Notes · 说明 |
|---|---|---|
| Classical mechanics, EM, thermo (Phases 1–2, 9) | **SI** | EM uses $\varepsilon_0,\mu_0$; the Coulomb constant is $k_e = 1/4\pi\varepsilon_0$. |
| Quantum field theory (Phase 6, e.g. 6.5) | **Natural units** $\hbar = c = 1$ | Mass, energy, momentum, inverse length all carry the same dimension; factors of $\hbar,c$ are restored by dimensional analysis. |
| Particle physics (Phase 8) | Mixed — natural units, with $\hbar c \approx 197\ \text{MeV·fm}$ kept where useful | Cross-sections in barns, energies in eV/MeV/GeV. |
| Statistical mechanics (Phase 2) | SI, with $k_B$ explicit | $\beta = 1/k_B T$. |

> **Restoring factors.** In natural units a result like $E = m$ means $E = mc^2$; a length $1/m$ means $\hbar/mc$. Reinsert $\hbar$ and $c$ until both sides match in SI dimensions.
>
> **还原因子。** 在自然单位下，$E = m$ 即 $E = mc^2$；长度 $1/m$ 即 $\hbar/mc$。补回 $\hbar$ 与 $c$ 直到两边的 SI 量纲一致即可。

## 2. Metric signature · 度规号差

The curriculum follows the **standard literature split** — particle physics and GR use opposite signatures, so always note which phase you are in:

本课程遵循**文献中的标准分工**——粒子物理与广义相对论使用相反的号差，因此务必留意所处的阶段：

| Phases · 阶段 | Signature · 号差 | Line element · 线元 |
|---|---|---|
| **1 (SR), 6 (QFT), 8 (particle)** | **mostly-minus** $(+,-,-,-)$ | $ds^2 = c^2 dt^2 - dx^2 - dy^2 - dz^2$ |
| **7 (General Relativity)** | **mostly-plus** $(-,+,+,+)$ | $ds^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2$ |

Consequences of the flip · 号差翻转的后果:

- The on-shell relation is $p^\mu p_\mu = +m^2 c^2$ in $(+,-,-,-)$ but $p^\mu p_\mu = -m^2 c^2$ in $(-,+,+,+)$.
- Timelike intervals have $ds^2 > 0$ in mostly-minus, $ds^2 < 0$ in mostly-plus.
- 在场点 $(+,-,-,-)$ 中在壳关系为 $p^\mu p_\mu = +m^2 c^2$，而在 $(-,+,+,+)$ 中为 $p^\mu p_\mu = -m^2 c^2$；类时间隔在两种号差下分别为 $ds^2 > 0$ 与 $ds^2 < 0$。

## 3. Indices & summation · 指标与求和

- **Greek** $\mu,\nu,\rho,\dots = 0,1,2,3$ are **spacetime** indices ($x^0 = ct$); **Latin** $i,j,k,\dots = 1,2,3$ are **spatial**.
- **Einstein summation**: a repeated upper/lower pair is summed, $a^\mu b_\mu \equiv \sum_\mu a^\mu b_\mu$.
- Indices are raised/lowered with the metric: $a_\mu = g_{\mu\nu}a^\nu$, $a^\mu = g^{\mu\nu}a_\nu$.
- $\partial_\mu \equiv \partial/\partial x^\mu$; the d'Alembertian is $\Box \equiv \partial^\mu\partial_\mu$.

- **希腊字母** $\mu,\nu,\rho,\dots = 0,1,2,3$ 为**时空**指标（$x^0 = ct$）；**拉丁字母** $i,j,k,\dots = 1,2,3$ 为**空间**指标。
- **爱因斯坦求和**：上下成对的重复指标自动求和。指标用度规升降：$a_\mu = g_{\mu\nu}a^\nu$。$\partial_\mu \equiv \partial/\partial x^\mu$，达朗贝尔算子 $\Box \equiv \partial^\mu\partial_\mu$。

## 4. Fourier transform · 傅里叶变换

The convention used for fields and propagators (Phases 0.5, 6):

$$ f(x) = \int \frac{d^4k}{(2\pi)^4}\, \tilde{f}(k)\, e^{-i k\cdot x}, \qquad \tilde{f}(k) = \int d^4x\, f(x)\, e^{+i k\cdot x}, $$

with $k\cdot x = k^\mu x_\mu$. The $2\pi$ factors live with the momentum integrals; a Dirac delta is $\int d^4x\, e^{i k\cdot x} = (2\pi)^4 \delta^4(k)$.

约定（用于场与传播子，模块 0.5、6）如上：$2\pi$ 因子随动量积分出现，$\int d^4x\, e^{i k\cdot x} = (2\pi)^4 \delta^4(k)$。

## 5. Electromagnetism · 电磁学

- **SI units** throughout Phase 1. Maxwell's equations: $\nabla\cdot\mathbf{E} = \rho/\varepsilon_0$, $\nabla\times\mathbf{B} - \tfrac{1}{c^2}\partial_t\mathbf{E} = \mu_0\mathbf{J}$, with $c^2 = 1/\varepsilon_0\mu_0$.
- Field-strength tensor $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$; the covariant form is $\partial_\mu F^{\mu\nu} = \mu_0 J^\nu$ (Module 1.15).
- 第 1 阶段全程采用 **SI 单位**；场强张量 $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$，协变形式 $\partial_\mu F^{\mu\nu} = \mu_0 J^\nu$（模块 1.15）。

## 6. Fundamental constants · 基本常数

| Symbol | Value (SI) | Name · 名称 |
|---|---|---|
| $c$ | $2.998\times10^{8}\ \text{m/s}$ | speed of light · 光速 |
| $\hbar$ | $1.055\times10^{-34}\ \text{J·s} = 6.582\times10^{-16}\ \text{eV·s}$ | reduced Planck constant · 约化普朗克常数 |
| $k_B$ | $1.381\times10^{-23}\ \text{J/K} = 8.617\times10^{-5}\ \text{eV/K}$ | Boltzmann constant · 玻尔兹曼常数 |
| $e$ | $1.602\times10^{-19}\ \text{C}$ | elementary charge · 基本电荷 |
| $G$ | $6.674\times10^{-11}\ \text{N·m}^2/\text{kg}^2$ | gravitational constant · 引力常量 |
| $m_e$ | $9.109\times10^{-31}\ \text{kg} = 0.511\ \text{MeV}/c^2$ | electron mass · 电子质量 |
| $\varepsilon_0$ | $8.854\times10^{-12}\ \text{F/m}$ | vacuum permittivity · 真空介电常数 |
| $\hbar c$ | $197.3\ \text{MeV·fm}$ | useful in particle physics · 粒子物理中常用 |

## 7. Common symbols · 常用记号

| Symbol | Meaning · 含义 |
|---|---|
| $\hat{A},\ \hat{H}$ | quantum operator / Hamiltonian · 算符／哈密顿量 |
| $A^\dagger$ | Hermitian conjugate (adjoint) · 厄米共轭 |
| $\langle\psi|\phi\rangle$ | inner product (Dirac bra–ket) · 内积（狄拉克括号） |
| $[\,\cdot,\cdot\,],\ \{\,\cdot,\cdot\,\}$ | commutator / anticommutator · 对易子／反对易子 |
| $\langle A\rangle$ | expectation or thermal average · 期望值／热平均 |
| $\nabla,\ \nabla\cdot,\ \nabla\times$ | gradient / divergence / curl · 梯度／散度／旋度 |
| $\delta(x),\ \theta(x)$ | Dirac delta / Heaviside step · 狄拉克 δ／阶跃函数 |
| $\partial_\mu,\ \Box$ | 4-gradient / d'Alembertian · 四维梯度／达朗贝尔算子 |
| $\mathrm{Tr},\ \det$ | trace / determinant · 迹／行列式 |
| $\otimes$ | tensor product · 张量积 |

---

*If a module ever deviates from these conventions, it says so explicitly at the point of use.*

*若某个模块偏离上述约定，会在使用处明确说明。*

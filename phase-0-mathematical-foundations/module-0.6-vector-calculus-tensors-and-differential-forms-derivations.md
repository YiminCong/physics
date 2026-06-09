---
title: "Derivations — Module 0.6: Vector Calculus, Tensors & Differential Forms"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 0.6: Vector Calculus, Tensors & Differential Forms
# 推导 — 模块 0.6：向量微积分、张量与微分形式

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 0.6](./module-0.6-vector-calculus-tensors-and-differential-forms.md). Full step-by-step proofs: the divergence theorem and Stokes' theorem (statement plus the standard cube/loop argument); derivation of $\nabla^2$ in spherical coordinates; Maxwell's equations as applications of $\nabla\cdot$ and $\nabla\times$; the Levi-Civita identity $\varepsilon_{ijk}\varepsilon_{ilm} = \delta_{jl}\delta_{km} - \delta_{jm}\delta_{kl}$; and the vector identity $\nabla\times(\nabla\times\mathbf{A}) = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A}$ proved by index notation. English first, then 中文.
> [模块 0.6](./module-0.6-vector-calculus-tensors-and-differential-forms.md) 的配套文档：完整逐步证明：散度定理与斯托克斯定理（陈述及标准的立方体/回路论证）；球坐标下 $\nabla^2$ 的推导；麦克斯韦方程作为 $\nabla\cdot$ 和 $\nabla\times$ 的应用；列维-奇维塔恒等式 $\varepsilon_{ijk}\varepsilon_{ilm} = \delta_{jl}\delta_{km} - \delta_{jm}\delta_{kl}$；以及用指标记号证明向量恒等式 $\nabla\times(\nabla\times\mathbf{A}) = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A}$。先英文，后中文。

---

## A. The Divergence Theorem · 散度定理

**Statement.** Let $V$ be a compact region in $\mathbb{R}^3$ with piecewise smooth boundary surface $S = \partial V$, with outward-pointing unit normal $\hat{\mathbf{n}}$. For any continuously differentiable vector field $\mathbf{F}$:

**陈述。** 设 $V$ 是 $\mathbb{R}^3$ 中具有分片光滑边界曲面 $S = \partial V$ 的紧致区域，$\hat{\mathbf{n}}$ 为向外单位法向量。对任意连续可微向量场 $\mathbf{F}$：

$$ \int_V (\nabla\cdot\mathbf{F})\,dV = \oint_S \mathbf{F}\cdot\hat{\mathbf{n}}\,dA. $$

**Proof — Step 1: Reduce to one component.** Write $\mathbf{F} = (F_1, F_2, F_3)$. By linearity, it suffices to prove the theorem for each component separately. We prove it for $\mathbf{F} = (F_1, 0, 0)$, i.e., show

**证明——第 1 步：归约到单个分量。** 写 $\mathbf{F} = (F_1, F_2, F_3)$。由线性性，对每个分量分别证明定理即可。我们对 $\mathbf{F} = (F_1, 0, 0)$ 进行证明，即证明

$$ \int_V \frac{\partial F_1}{\partial x}\,dV = \oint_S F_1 n_1\,dA, $$

where $n_1 = \hat{\mathbf{n}}\cdot\hat{\mathbf{e}}_x$ is the $x$-component of the outward normal. The full theorem follows by adding the analogous results for $F_2$ and $F_3$.

其中 $n_1 = \hat{\mathbf{n}}\cdot\hat{\mathbf{e}}_x$ 是外法向量的 $x$ 分量。对 $F_2$ 和 $F_3$ 的类似结果相加即得完整定理。

**Step 2 — The unit cube argument.** First prove the result for $V = [0,1]^3$ (the unit cube). For a fixed $(y, z)$, integrate $\partial F_1/\partial x$ from $x = 0$ to $x = 1$ using the fundamental theorem of calculus:

**第 2 步 — 单位立方体论证。** 首先对 $V = [0,1]^3$（单位立方体）证明此结果。对固定的 $(y, z)$，利用微积分基本定理对 $x$ 从 0 积到 1：

$$ \int_0^1 \frac{\partial F_1}{\partial x}\,dx = F_1(1, y, z) - F_1(0, y, z). $$

Integrate over the remaining two variables:

对其余两个变量积分：

$$ \int_V \frac{\partial F_1}{\partial x}\,dV = \int_0^1 \int_0^1 [F_1(1,y,z) - F_1(0,y,z)]\,dy\,dz. $$

Now examine the boundary surface $S$ of the cube. It has six faces:
- Face $x = 1$: $\hat{\mathbf{n}} = \hat{\mathbf{e}}_x$ (outward), so $F_1 n_1\,dA = F_1(1,y,z)\,dy\,dz$. Contribution: $+\int\int F_1(1,y,z)\,dy\,dz$.
- Face $x = 0$: $\hat{\mathbf{n}} = -\hat{\mathbf{e}}_x$ (outward), so $F_1 n_1\,dA = -F_1(0,y,z)\,dy\,dz$. Contribution: $-\int\int F_1(0,y,z)\,dy\,dz$.
- Four side faces ($y=0,1$ and $z=0,1$): $\hat{\mathbf{n}}$ has no $x$-component, so $F_1 n_1 = 0$ on these faces.

现在考察立方体的边界曲面 $S$，共有六个面：
- $x = 1$ 面：$\hat{\mathbf{n}} = \hat{\mathbf{e}}_x$（向外），故 $F_1 n_1\,dA = F_1(1,y,z)\,dy\,dz$。贡献：$+\int\int F_1(1,y,z)\,dy\,dz$。
- $x = 0$ 面：$\hat{\mathbf{n}} = -\hat{\mathbf{e}}_x$（向外），故 $F_1 n_1\,dA = -F_1(0,y,z)\,dy\,dz$。贡献：$-\int\int F_1(0,y,z)\,dy\,dz$。
- 四个侧面（$y=0,1$ 和 $z=0,1$）：$\hat{\mathbf{n}}$ 无 $x$ 分量，故 $F_1 n_1 = 0$。

Adding all boundary contributions:

将所有边界贡献相加：

$$ \oint_S F_1 n_1\,dA = \int_0^1 \int_0^1 [F_1(1,y,z) - F_1(0,y,z)]\,dy\,dz = \int_V \frac{\partial F_1}{\partial x}\,dV. \quad\checkmark $$

**Step 3 — Extend to general regions.** Any region $V$ with piecewise smooth boundary can be subdivided (partitioned) into small "almost-cuboid" elements by a coordinate grid. Applying the result from Step 2 to each element and summing:

**第 3 步 — 推广到一般区域。** 任何具有分片光滑边界的区域 $V$ 都可以通过坐标网格细分（剖分）为小的"近似长方体"元素。对每个元素应用第 2 步的结果并求和：

- Interior faces appear twice with opposite orientations and cancel.
- Only boundary faces survive.

- 内部面以相反方向出现两次，相互抵消。
- 只有边界面的贡献保留。

In the limit as the mesh size $\to 0$, the sum converges to $\int_V \nabla\cdot\mathbf{F}\,dV = \oint_S \mathbf{F}\cdot\hat{\mathbf{n}}\,dA$. $\blacksquare$

当网格尺寸 $\to 0$ 时，求和收敛为 $\int_V \nabla\cdot\mathbf{F}\,dV = \oint_S \mathbf{F}\cdot\hat{\mathbf{n}}\,dA$。$\blacksquare$

**Physical interpretation.** The divergence theorem converts "what's happening at every interior point" into "what's happening at the boundary." In electrostatics: Gauss's law $\oint \mathbf{E}\cdot d\mathbf{A} = Q_\text{enc}/\varepsilon_0$ follows from $\nabla\cdot\mathbf{E} = \rho/\varepsilon_0$ via $\int_V \rho/\varepsilon_0\,dV = Q_\text{enc}/\varepsilon_0$. In fluid dynamics: $\nabla\cdot\mathbf{v} = 0$ (incompressible flow) means no net flux through any closed surface.

**物理解释。** 散度定理将"每个内部点发生的事情"转化为"边界上发生的事情"。在静电学中：高斯定律 $\oint \mathbf{E}\cdot d\mathbf{A} = Q_\text{enc}/\varepsilon_0$ 由 $\nabla\cdot\mathbf{E} = \rho/\varepsilon_0$ 通过 $\int_V \rho/\varepsilon_0\,dV = Q_\text{enc}/\varepsilon_0$ 得出。在流体力学中：$\nabla\cdot\mathbf{v} = 0$（不可压缩流）意味着穿过任意闭合曲面的净通量为零。

---

## B. Stokes' Theorem · 斯托克斯定理

**Statement.** Let $S$ be an oriented surface in $\mathbb{R}^3$ with piecewise smooth boundary curve $C = \partial S$ (traversed counterclockwise when viewed from the side the normal $\hat{\mathbf{n}}$ points toward). For any continuously differentiable vector field $\mathbf{F}$:

**陈述。** 设 $S$ 是 $\mathbb{R}^3$ 中具有分片光滑边界曲线 $C = \partial S$ 的定向曲面（从法向量 $\hat{\mathbf{n}}$ 所指方向看去，$C$ 沿逆时针方向绕行）。对任意连续可微向量场 $\mathbf{F}$：

$$ \int_S (\nabla\times\mathbf{F})\cdot\hat{\mathbf{n}}\,dA = \oint_C \mathbf{F}\cdot d\mathbf{l}. $$

**Proof — Step 1: Reduce to one component.** Write $\mathbf{F} = (F_1, F_2, F_3)$. By linearity we prove:

**证明——第 1 步：归约到单个分量。** 写 $\mathbf{F} = (F_1, F_2, F_3)$。由线性性，我们对每个分量分别证明：

$$ \int_S \left(\frac{\partial F_2}{\partial x} - \frac{\partial F_1}{\partial y}\right) n_z\,dA = \oint_C (F_1\,dx + F_2\,dy) \quad \text{[the $xy$-component]}, $$

and similarly for the $yz$ and $zx$ components.

以及类似的 $yz$ 和 $zx$ 分量。

**Step 2 — The unit square in the $xy$-plane.** For the simplest case where $S$ is the unit square $[0,1]^2$ in the $z=0$ plane (so $\hat{\mathbf{n}} = \hat{\mathbf{e}}_z$, $dA = dx\,dy$), and $C$ is its boundary traversed counterclockwise:

**第 2 步 — $xy$ 平面中的单位正方形。** 对最简单的情形，$S$ 是 $z=0$ 平面中的单位正方形 $[0,1]^2$（故 $\hat{\mathbf{n}} = \hat{\mathbf{e}}_z$，$dA = dx\,dy$），$C$ 是沿逆时针方向绕行的边界：

Left side: $\int_S (\partial F_2/\partial x - \partial F_1/\partial y)\,dx\,dy$.

左侧：$\int_S (\partial F_2/\partial x - \partial F_1/\partial y)\,dx\,dy$。

For the $\partial F_2/\partial x$ term, integrate first over $x$ by FTC:

对 $\partial F_2/\partial x$ 项，先对 $x$ 用基本定理积分：

$$ \int_0^1 \int_0^1 \frac{\partial F_2}{\partial x}\,dx\,dy = \int_0^1 [F_2(1,y) - F_2(0,y)]\,dy. $$

For the $\partial F_1/\partial y$ term, integrate first over $y$:

对 $\partial F_1/\partial y$ 项，先对 $y$ 用基本定理积分：

$$ \int_0^1 \int_0^1 \frac{\partial F_1}{\partial y}\,dy\,dx = \int_0^1 [F_1(x,1) - F_1(x,0)]\,dx. $$

So the left side equals:

故左侧等于：

$$ \int_0^1 [F_2(1,y) - F_2(0,y)]\,dy - \int_0^1 [F_1(x,1) - F_1(x,0)]\,dx. $$

Right side: $\oint_C (F_1\,dx + F_2\,dy)$. Traverse the four edges counterclockwise:
- Bottom ($y=0$, $x: 0\to 1$): $\int_0^1 F_1(x,0)\,dx$
- Right ($x=1$, $y: 0\to 1$): $\int_0^1 F_2(1,y)\,dy$
- Top ($y=1$, $x: 1\to 0$): $\int_1^0 F_1(x,1)\,dx = -\int_0^1 F_1(x,1)\,dx$
- Left ($x=0$, $y: 1\to 0$): $\int_1^0 F_2(0,y)\,dy = -\int_0^1 F_2(0,y)\,dy$

右侧：$\oint_C (F_1\,dx + F_2\,dy)$。沿四条边逆时针绕行：
- 底边（$y=0$，$x: 0\to 1$）：$\int_0^1 F_1(x,0)\,dx$
- 右边（$x=1$，$y: 0\to 1$）：$\int_0^1 F_2(1,y)\,dy$
- 顶边（$y=1$，$x: 1\to 0$）：$\int_1^0 F_1(x,1)\,dx = -\int_0^1 F_1(x,1)\,dx$
- 左边（$x=0$，$y: 1\to 0$）：$\int_1^0 F_2(0,y)\,dy = -\int_0^1 F_2(0,y)\,dy$

Sum $= \int_0^1 [F_2(1,y) - F_2(0,y)]\,dy - \int_0^1 [F_1(x,1) - F_1(x,0)]\,dx$ = Left side. $\checkmark$

求和 $= \int_0^1 [F_2(1,y) - F_2(0,y)]\,dy - \int_0^1 [F_1(x,1) - F_1(x,0)]\,dx$ = 左侧。✓

**Step 3 — General surface by subdivision.** Any smooth surface $S$ can be approximated by small "almost-planar" patches. Applying the result of Step 2 to each patch and summing, interior edge contributions cancel (each interior edge is shared by two patches traversed in opposite directions), leaving only the outer boundary $C$. In the limit, this gives Stokes' theorem for $S$. $\blacksquare$

**第 3 步 — 通过细分推广到一般曲面。** 任何光滑曲面 $S$ 都可以用小的"近似平面"片近似。对每个片应用第 2 步的结果并求和，内部边的贡献相消（每条内部边被两个相反方向绕行的片共享），只留下外边界 $C$。取极限即得 $S$ 的斯托克斯定理。$\blacksquare$

**Physical applications.** Faraday's law: $\oint_C \mathbf{E}\cdot d\mathbf{l} = -\frac{d}{dt} \int_S \mathbf{B}\cdot d\mathbf{A}$. In differential form this is $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$; Stokes' theorem connects the two. Ampère's law: $\oint_C \mathbf{B}\cdot d\mathbf{l} = \mu_0 I_\text{enc}$ relates the magnetic circulation around a loop to the current through the surface bounded by the loop.

**物理应用。** 法拉第定律：$\oint_C \mathbf{E}\cdot d\mathbf{l} = -\frac{d}{dt} \int_S \mathbf{B}\cdot d\mathbf{A}$。微分形式为 $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$；斯托克斯定理将两者联系起来。安培定律：$\oint_C \mathbf{B}\cdot d\mathbf{l} = \mu_0 I_\text{enc}$ 将回路周围的磁环量与穿过该回路所围曲面的电流联系起来。

---

## C. Derivation of $\nabla^2$ in Spherical Coordinates · 球坐标下 $\nabla^2$ 的推导

**Setup.** The spherical coordinates $(r, \theta, \varphi)$ are related to Cartesian coordinates by:

**准备工作。** 球坐标 $(r, \theta, \varphi)$ 与笛卡尔坐标的关系为：

$$ x = r \sin\theta \cos\varphi, \quad y = r \sin\theta \sin\varphi, \quad z = r \cos\theta, $$

with $r \ge 0$, $0 \le \theta \le \pi$, $0 \le \varphi < 2\pi$.

其中 $r \ge 0$，$0 \le \theta \le \pi$，$0 \le \varphi < 2\pi$。

**Step 1 — Compute the scale factors.** The position vector is $\vec{r} = (r \sin\theta \cos\varphi, r \sin\theta \sin\varphi, r \cos\theta)$. The scale factors (metrics) are

**第 1 步 — 计算比例因子。** 位置向量为 $\vec{r} = (r \sin\theta \cos\varphi, r \sin\theta \sin\varphi, r \cos\theta)$。比例因子（度规）为

$$ h_r = |\partial\vec{r}/\partial r| = 1, \qquad h_\theta = |\partial\vec{r}/\partial\theta| = r, \qquad h_\varphi = |\partial\vec{r}/\partial\varphi| = r \sin\theta. $$

Verify $h_\theta$: $\partial\vec{r}/\partial\theta = (r \cos\theta \cos\varphi, r \cos\theta \sin\varphi, -r \sin\theta)$, so $h_\theta = r\sqrt{\cos^2\theta \cos^2\varphi + \cos^2\theta \sin^2\varphi + \sin^2\theta} = r\sqrt{\cos^2\theta + \sin^2\theta} = r$. ✓

验证 $h_\theta$：$\partial\vec{r}/\partial\theta = (r \cos\theta \cos\varphi, r \cos\theta \sin\varphi, -r \sin\theta)$，故 $h_\theta = r\sqrt{\cos^2\theta \cos^2\varphi + \cos^2\theta \sin^2\varphi + \sin^2\theta} = r\sqrt{\cos^2\theta + \sin^2\theta} = r$。✓

**Step 2 — The volume element.** In an orthogonal curvilinear coordinate system the volume element is

**第 2 步 — 体积元。** 在正交曲线坐标系中，体积元为

$$ dV = h_r h_\theta h_\varphi\,dr\,d\theta\,d\varphi = (1)(r)(r \sin\theta)\,dr\,d\theta\,d\varphi = r^2 \sin\theta\,dr\,d\theta\,d\varphi. $$

**Step 3 — General Laplacian formula in orthogonal curvilinear coordinates.** For a scalar field $f$, the Laplacian is

**第 3 步 — 正交曲线坐标系中拉普拉斯算子的一般公式。** 对标量场 $f$，拉普拉斯算子为

$$ \nabla^2 f = \frac{1}{h_1 h_2 h_3}\left[\frac{\partial}{\partial q_1}\!\left(\frac{h_2 h_3}{h_1}\frac{\partial f}{\partial q_1}\right) + \frac{\partial}{\partial q_2}\!\left(\frac{h_1 h_3}{h_2}\frac{\partial f}{\partial q_2}\right) + \frac{\partial}{\partial q_3}\!\left(\frac{h_1 h_2}{h_3}\frac{\partial f}{\partial q_3}\right)\right]. $$

This follows from computing $\nabla\cdot(\nabla f)$ using the divergence formula in curvilinear coordinates.

这由在曲线坐标系中计算 $\nabla\cdot(\nabla f)$ 的散度公式得到。

**Step 4 — Apply to spherical coordinates.** With $(q_1,q_2,q_3) = (r,\theta,\varphi)$ and $(h_1,h_2,h_3) = (1, r, r \sin\theta)$:

**第 4 步 — 应用于球坐标。** 令 $(q_1,q_2,q_3) = (r,\theta,\varphi)$，$(h_1,h_2,h_3) = (1, r, r \sin\theta)$：

$$ \frac{h_2 h_3}{h_1} = r^2 \sin\theta, \qquad \frac{h_1 h_3}{h_2} = \sin\theta, \qquad \frac{h_1 h_2}{h_3} = \frac{1}{\sin\theta}, \qquad h_1 h_2 h_3 = r^2 \sin\theta. $$

So:

故：

$$ \nabla^2 f = \frac{1}{r^2 \sin\theta}\left[\frac{\partial}{\partial r}\!\left(r^2 \sin\theta\,\frac{\partial f}{\partial r}\right) + \frac{\partial}{\partial\theta}\!\left(\sin\theta\,\frac{\partial f}{\partial\theta}\right) + \frac{\partial}{\partial\varphi}\!\left(\frac{1}{\sin\theta}\frac{\partial f}{\partial\varphi}\right)\right]. $$

The $\sin\theta$ in the first term cancels with the prefactor:

第一项中的 $\sin\theta$ 与前置因子约去：

$$ \nabla^2 f = \frac{1}{r^2}\frac{\partial}{\partial r}\!\left(r^2 \frac{\partial f}{\partial r}\right) + \frac{1}{r^2 \sin\theta}\frac{\partial}{\partial\theta}\!\left(\sin\theta\,\frac{\partial f}{\partial\theta}\right) + \frac{1}{r^2 \sin^2\theta}\frac{\partial^2 f}{\partial\varphi^2}. $$

**Step 5 — Expand the radial term.**

**第 5 步 — 展开径向项。**

$$ \frac{1}{r^2}\frac{\partial}{\partial r}\!\left(r^2 \frac{\partial f}{\partial r}\right) = \frac{1}{r^2}\left(2r \frac{\partial f}{\partial r} + r^2 \frac{\partial^2 f}{\partial r^2}\right) = \frac{2}{r}\frac{\partial f}{\partial r} + \frac{\partial^2 f}{\partial r^2}. $$

So the full result is:

故完整结果为：

$$ \boxed{\, \nabla^2 f = \frac{\partial^2 f}{\partial r^2} + \frac{2}{r}\frac{\partial f}{\partial r} + \frac{1}{r^2 \sin\theta}\frac{\partial}{\partial\theta}\!\left(\sin\theta\,\frac{\partial f}{\partial\theta}\right) + \frac{1}{r^2 \sin^2\theta}\frac{\partial^2 f}{\partial\varphi^2}. \,} $$

Or equivalently:

或等价地：

$$ \boxed{\, \nabla^2 f = \frac{1}{r^2}\frac{\partial}{\partial r}\!\left(r^2 \frac{\partial f}{\partial r}\right) + \frac{1}{r^2 \sin\theta}\frac{\partial}{\partial\theta}\!\left(\sin\theta\,\frac{\partial f}{\partial\theta}\right) + \frac{1}{r^2 \sin^2\theta}\frac{\partial^2 f}{\partial\varphi^2}. \,} \qquad \blacksquare $$

**Physical application.** The time-independent Schrödinger equation for the hydrogen atom $-(\hbar^2/2m)\nabla^2\psi + V(r)\psi = E\psi$ with $V(r) = -e^2/(4\pi\varepsilon_0 r)$ uses this exact expression. The separation $\psi(r,\theta,\varphi) = R(r)Y_l^m(\theta,\varphi)$ works because $\nabla^2$ separates into a radial part acting on $R$ and an angular part (the Legendre equation) acting on $Y$.

**物理应用。** 氢原子的定态薛定谔方程 $-(\hbar^2/2m)\nabla^2\psi + V(r)\psi = E\psi$，其中 $V(r) = -e^2/(4\pi\varepsilon_0 r)$，正是使用此表达式。分离 $\psi(r,\theta,\varphi) = R(r)Y_l^m(\theta,\varphi)$ 之所以有效，是因为 $\nabla^2$ 分离为作用于 $R$ 的径向部分和作用于 $Y$ 的角向部分（勒让德方程）。

---

## D. Maxwell's Equations in Differential Form and Their Integral Equivalents · 麦克斯韦方程的微分形式与积分等价形式

**Setup.** Maxwell's equations (SI units) in differential form are:

**准备工作。** 麦克斯韦方程组（国际单位制）的微分形式为：

$$ \begin{aligned} \nabla\cdot\mathbf{E} &= \rho/\varepsilon_0 && \text{[Gauss's law for } \mathbf{E}\text{ 高斯定律（电场）]} \\ \nabla\cdot\mathbf{B} &= 0 && \text{[Gauss's law for } \mathbf{B}\text{ 高斯定律（磁场）]} \\ \nabla\times\mathbf{E} &= -\partial\mathbf{B}/\partial t && \text{[Faraday's law 法拉第定律]} \\ \nabla\times\mathbf{B} &= \mu_0\mathbf{J} + \mu_0\varepsilon_0\,\partial\mathbf{E}/\partial t && \text{[Ampère–Maxwell law 安培–麦克斯韦定律]} \end{aligned} $$

**Step 1 — Gauss's law via the divergence theorem.** Apply the divergence theorem to $\nabla\cdot\mathbf{E} = \rho/\varepsilon_0$ over a volume $V$ with boundary $S$:

**第 1 步 — 通过散度定理得出高斯定律。** 对区域 $V$（边界为 $S$）将散度定理应用于 $\nabla\cdot\mathbf{E} = \rho/\varepsilon_0$：

$$ \oint_S \mathbf{E}\cdot\hat{\mathbf{n}}\,dA = \int_V \nabla\cdot\mathbf{E}\,dV = \frac{1}{\varepsilon_0} \int_V \rho\,dV = \frac{Q_\text{enc}}{\varepsilon_0}. $$

This is the **integral form of Gauss's law**: the total electric flux through any closed surface equals the enclosed charge divided by $\varepsilon_0$.

这就是**高斯定律的积分形式**：穿过任意闭合曲面的总电通量等于包围的电荷除以 $\varepsilon_0$。

**Step 2 — No magnetic monopoles.** Similarly $\nabla\cdot\mathbf{B} = 0$ gives $\oint_S \mathbf{B}\cdot\hat{\mathbf{n}}\,dA = 0$: there is no net magnetic flux through any closed surface, i.e., magnetic field lines form closed loops.

**第 2 步 — 无磁单极子。** 类似地，$\nabla\cdot\mathbf{B} = 0$ 给出 $\oint_S \mathbf{B}\cdot\hat{\mathbf{n}}\,dA = 0$：穿过任意闭合曲面的净磁通量为零，即磁场线形成闭合回路。

**Step 3 — Faraday's law via Stokes' theorem.** Apply Stokes' theorem to $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$ over a surface $S$ bounded by curve $C$:

**第 3 步 — 通过斯托克斯定理得出法拉第定律。** 对以曲线 $C$ 为边界的曲面 $S$，将斯托克斯定理应用于 $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$：

$$ \oint_C \mathbf{E}\cdot d\mathbf{l} = \int_S (\nabla\times\mathbf{E})\cdot\hat{\mathbf{n}}\,dA = -\int_S \frac{\partial\mathbf{B}}{\partial t}\cdot\hat{\mathbf{n}}\,dA = -\frac{d}{dt} \int_S \mathbf{B}\cdot\hat{\mathbf{n}}\,dA = -\frac{d\Phi_B}{dt}. $$

This is Faraday's law: the EMF around a loop equals the negative rate of change of the magnetic flux through the loop.

这就是法拉第定律：回路的电动势等于穿过回路磁通量的负时间变化率。

**Step 4 — Ampère–Maxwell law via Stokes' theorem.** Apply Stokes' theorem to $\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\,\partial\mathbf{E}/\partial t$:

**第 4 步 — 通过斯托克斯定理得出安培–麦克斯韦定律。** 对 $\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\,\partial\mathbf{E}/\partial t$ 应用斯托克斯定理：

$$ \oint_C \mathbf{B}\cdot d\mathbf{l} = \mu_0 \int_S \mathbf{J}\cdot\hat{\mathbf{n}}\,dA + \mu_0\varepsilon_0 \frac{d}{dt} \int_S \mathbf{E}\cdot\hat{\mathbf{n}}\,dA = \mu_0 I_\text{enc} + \mu_0\varepsilon_0 \frac{d\Phi_E}{dt}. $$

The term $\mu_0\varepsilon_0\,\partial\mathbf{E}/\partial t$ is Maxwell's **displacement current**, needed to make the equation consistent with charge conservation ($\nabla\cdot\mathbf{J} + \partial\rho/\partial t = 0$) and to allow electromagnetic waves to exist.

项 $\mu_0\varepsilon_0\,\partial\mathbf{E}/\partial t$ 是麦克斯韦的**位移电流**，这是使方程与电荷守恒（$\nabla\cdot\mathbf{J} + \partial\rho/\partial t = 0$）一致并使电磁波得以存在所必需的。

---

## E. The Levi-Civita Identity $\varepsilon_{ijk} \varepsilon_{ilm} = \delta_{jl}\delta_{km} - \delta_{jm}\delta_{kl}$ · 列维-奇维塔恒等式

**Claim.** Summing over the repeated index $i$:

**命题。** 对重复指标 $i$ 求和：

$$ \sum_i \varepsilon_{ijk} \varepsilon_{ilm} = \delta_{jl} \delta_{km} - \delta_{jm} \delta_{kl}. $$

**Step 1 — Properties of the Levi-Civita symbol.** Recall $\varepsilon_{ijk} = +1$ if $(i,j,k)$ is an even permutation of $(1,2,3)$, $-1$ if odd, and $0$ if any two indices are equal. For three-dimensional space, $\varepsilon_{ijk} \varepsilon_{ilm}$ sums over $i = 1, 2, 3$.

**第 1 步 — 列维-奇维塔符号的性质。** 回顾：若 $(i,j,k)$ 是 $(1,2,3)$ 的偶置换，$\varepsilon_{ijk} = +1$；奇置换为 $-1$；有两个相同指标为 $0$。在三维空间中，$\varepsilon_{ijk} \varepsilon_{ilm}$ 对 $i = 1, 2, 3$ 求和。

**Step 2 — Enumerate cases.** Since $j, k \in \{1,2,3\}$ and $\varepsilon_{ijk} = 0$ unless all three indices are distinct, $j \ne k$ is required for a non-zero contribution. Similarly $l \ne m$ is required. For fixed $j \ne k$, the only $i$ that gives $\varepsilon_{ijk} \ne 0$ is the unique third value: $\{i\} = \{1,2,3\} \setminus \{j,k\}$.

**第 2 步 — 枚举情形。** 由于 $j, k \in \{1,2,3\}$，且除非三个指标都不同否则 $\varepsilon_{ijk} = 0$，因此需要 $j \ne k$ 才能有非零贡献。类似地，需要 $l \ne m$。对固定的 $j \ne k$，使 $\varepsilon_{ijk} \ne 0$ 的唯一 $i$ 是 $\{1,2,3\}\setminus\{j,k\}$ 中的第三个值。

**Step 3 — Compute systematically.** Fix $j, k, l, m \in \{1,2,3\}$. The sum $\sum_i \varepsilon_{ijk} \varepsilon_{ilm}$ is non-zero only when:
- The pair $\{j,k\}$ and the pair $\{l,m\}$ each consists of two distinct elements, AND
- There is some $i$ such that both $\varepsilon_{ijk} \ne 0$ and $\varepsilon_{ilm} \ne 0$, which requires $\{i,j,k\} = \{i,l,m\} = \{1,2,3\}$, forcing $\{j,k\} = \{l,m\}$ as sets.

**第 3 步 — 系统计算。** 固定 $j, k, l, m \in \{1,2,3\}$。仅当以下条件满足时，$\sum_i \varepsilon_{ijk} \varepsilon_{ilm}$ 才非零：
- 对 $\{j,k\}$ 和 $\{l,m\}$，每对均由两个不同元素组成，且
- 存在某个 $i$ 使得 $\varepsilon_{ijk} \ne 0$ 且 $\varepsilon_{ilm} \ne 0$，这要求 $\{i,j,k\} = \{i,l,m\} = \{1,2,3\}$，从而作为集合 $\{j,k\} = \{l,m\}$。

This means either $(l = j, m = k)$ or $(l = k, m = j)$.

这意味着要么 $(l = j, m = k)$，要么 $(l = k, m = j)$。

**Step 4 — Determine the sign.** When $l = j, m = k$: $\sum_i \varepsilon_{ijk} \varepsilon_{ijk} = (\varepsilon_{ijk})^2 = 1$ (since $(\varepsilon_{ijk})^2 = 0$ or $1$, and the single surviving term is $\pm 1$, so its square is $1$).

**第 4 步 — 确定符号。** 当 $l = j, m = k$ 时：$\sum_i \varepsilon_{ijk} \varepsilon_{ijk} = (\varepsilon_{ijk})^2 = 1$（因为 $(\varepsilon_{ijk})^2$ 为 $0$ 或 $1$，唯一存活的项为 $\pm 1$，平方为 $1$）。

When $l = k, m = j$: the second factor becomes $\varepsilon_{ikj} = -\varepsilon_{ijk}$ (swapping two indices flips sign). So $\sum_i \varepsilon_{ijk} \varepsilon_{ikj} = -\sum_i (\varepsilon_{ijk})^2 = -1$.

当 $l = k, m = j$ 时：第二个因子变为 $\varepsilon_{ikj} = -\varepsilon_{ijk}$（交换两个指标改变符号）。故 $\sum_i \varepsilon_{ijk} \varepsilon_{ikj} = -\sum_i (\varepsilon_{ijk})^2 = -1$。

**Step 5 — Express using Kronecker deltas.** The two cases $(l=j,m=k) \to +1$ and $(l=k,m=j) \to -1$ are precisely captured by:

**第 5 步 — 用克罗内克 delta 表达。** 两种情形（$l=j,m=k$）$\to +1$ 和（$l=k,m=j$）$\to -1$ 恰好由以下式子捕捉：

$$ \sum_i \varepsilon_{ijk} \varepsilon_{ilm} = \delta_{jl} \delta_{km} - \delta_{jm} \delta_{kl}. \qquad \blacksquare $$

Verify: if $j=l=1$, $k=m=2$: $\delta_{11}\delta_{22} - \delta_{12}\delta_{21} = 1\cdot 1 - 0\cdot 0 = 1$. ✓ If $j=m=1$, $k=l=2$: $\delta_{12}\delta_{21} - \delta_{11}\delta_{22} = 0 - 1 = -1$. ✓

验证：若 $j=l=1$, $k=m=2$：$\delta_{11}\delta_{22} - \delta_{12}\delta_{21} = 1\cdot 1 - 0\cdot 0 = 1$。✓ 若 $j=m=1$, $k=l=2$：$\delta_{12}\delta_{21} - \delta_{11}\delta_{22} = 0 - 1 = -1$。✓

---

## F. Vector Identity: $\nabla\times(\nabla\times\mathbf{A}) = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A}$ via Index Notation · 向量恒等式的指标记号证明

**Claim.** For any twice-differentiable vector field $\mathbf{A}$:

**命题。** 对任意二阶可微向量场 $\mathbf{A}$：

$$ \nabla\times(\nabla\times\mathbf{A}) = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A}. $$

**Step 1 — Write the left side in index notation.** The $i$-th component of $\nabla\times\mathbf{A}$ is $(\nabla\times\mathbf{A})_i = \varepsilon_{ijk} \partial_j A_k$ (where $\partial_j = \partial/\partial x_j$ and repeated indices are summed). Then the $i$-th component of $\nabla\times(\nabla\times\mathbf{A})$ is:

**第 1 步 — 用指标记号写出左侧。** $\nabla\times\mathbf{A}$ 的第 $i$ 个分量为 $(\nabla\times\mathbf{A})_i = \varepsilon_{ijk} \partial_j A_k$（其中 $\partial_j = \partial/\partial x_j$，重复指标求和）。则 $\nabla\times(\nabla\times\mathbf{A})$ 的第 $i$ 个分量为：

$$ [\nabla\times(\nabla\times\mathbf{A})]_i = \varepsilon_{ijk} \partial_j (\nabla\times\mathbf{A})_k = \varepsilon_{ijk} \partial_j (\varepsilon_{klm} \partial_l A_m) = \varepsilon_{ijk} \varepsilon_{klm} \partial_j \partial_l A_m. $$

**Step 2 — Rewrite using the Levi-Civita identity.** We need $\varepsilon_{ijk} \varepsilon_{klm}$. Noting that $\varepsilon_{ijk} = \varepsilon_{kij}$ (even cyclic permutation), we have $\varepsilon_{ijk} \varepsilon_{klm} = \varepsilon_{kij} \varepsilon_{klm}$. Applying the identity from Section E with the first index summed being $k$, and pairs $(i,j)$ and $(l,m)$:

**第 2 步 — 用列维-奇维塔恒等式改写。** 需要 $\varepsilon_{ijk} \varepsilon_{klm}$。注意 $\varepsilon_{ijk} = \varepsilon_{kij}$（偶数循环置换），故 $\varepsilon_{ijk} \varepsilon_{klm} = \varepsilon_{kij} \varepsilon_{klm}$。应用 E 节中对被求和第一指标为 $k$、配对为 $(i,j)$ 和 $(l,m)$ 的恒等式：

$$ \varepsilon_{kij} \varepsilon_{klm} = \delta_{il} \delta_{jm} - \delta_{im} \delta_{jl}. $$

**Step 3 — Substitute back.**

**第 3 步 — 代回。**

$$ \begin{aligned} [\nabla\times(\nabla\times\mathbf{A})]_i &= (\delta_{il} \delta_{jm} - \delta_{im} \delta_{jl}) \partial_j \partial_l A_m \\ &= \delta_{il} \delta_{jm} \partial_j \partial_l A_m - \delta_{im} \delta_{jl} \partial_j \partial_l A_m. \end{aligned} $$

**Step 4 — Contract the Kronecker deltas.**

**第 4 步 — 缩并克罗内克 delta。**

First term: $\delta_{il} \delta_{jm} \partial_j \partial_l A_m = \partial_j \partial_i A_j$ (set $l=i$, $m=j$) $= \partial_i(\partial_j A_j) = \partial_i(\nabla\cdot\mathbf{A}) = [\nabla(\nabla\cdot\mathbf{A})]_i$.

第一项：$\delta_{il} \delta_{jm} \partial_j \partial_l A_m = \partial_j \partial_i A_j$（令 $l=i$, $m=j$）$= \partial_i(\partial_j A_j) = \partial_i(\nabla\cdot\mathbf{A}) = [\nabla(\nabla\cdot\mathbf{A})]_i$。

Second term: $\delta_{im} \delta_{jl} \partial_j \partial_l A_m = \partial_j \partial_j A_i$ (set $m=i$, $l=j$) $= (\nabla^2\mathbf{A})_i$.

第二项：$\delta_{im} \delta_{jl} \partial_j \partial_l A_m = \partial_j \partial_j A_i$（令 $m=i$, $l=j$）$= (\nabla^2\mathbf{A})_i$。

(Here $\nabla^2\mathbf{A}$ is the vector Laplacian, defined component-wise: $(\nabla^2\mathbf{A})_i = \partial_j \partial_j A_i = \nabla^2 A_i$.)

（此处 $\nabla^2\mathbf{A}$ 是向量拉普拉斯算子，逐分量定义：$(\nabla^2\mathbf{A})_i = \partial_j \partial_j A_i = \nabla^2 A_i$。）

**Step 5 — Combine.**

**第 5 步 — 合并。**

$$ [\nabla\times(\nabla\times\mathbf{A})]_i = [\nabla(\nabla\cdot\mathbf{A})]_i - (\nabla^2\mathbf{A})_i. $$

Since this holds for every component $i$:

由于对每个分量 $i$ 均成立：

$$ \boxed{\, \nabla\times(\nabla\times\mathbf{A}) = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A}. \,} \qquad \blacksquare $$

**Physical application — Electromagnetic wave equation.** In free space ($\rho = 0$, $\mathbf{J} = 0$), Maxwell's equations give $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$ and $\nabla\times\mathbf{B} = \mu_0\varepsilon_0\,\partial\mathbf{E}/\partial t$. Taking $\nabla\times$ of the first:

**物理应用——电磁波方程。** 在自由空间（$\rho = 0$, $\mathbf{J} = 0$）中，麦克斯韦方程给出 $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$ 和 $\nabla\times\mathbf{B} = \mu_0\varepsilon_0\,\partial\mathbf{E}/\partial t$。对第一式取 $\nabla\times$：

$$ \nabla\times(\nabla\times\mathbf{E}) = -\frac{\partial}{\partial t}(\nabla\times\mathbf{B}) = -\mu_0\varepsilon_0 \frac{\partial^2\mathbf{E}}{\partial t^2}. $$

Applying the vector identity, and using $\nabla\cdot\mathbf{E} = 0$ (no charges):

应用向量恒等式，并利用 $\nabla\cdot\mathbf{E} = 0$（无电荷）：

$$ \nabla(\nabla\cdot\mathbf{E}) - \nabla^2\mathbf{E} = -\mu_0\varepsilon_0 \frac{\partial^2\mathbf{E}}{\partial t^2} \;\to\; \boxed{\,\nabla^2\mathbf{E} = \mu_0\varepsilon_0 \frac{\partial^2\mathbf{E}}{\partial t^2}\,}. $$

This is the electromagnetic wave equation with wave speed $c = 1/\sqrt{\mu_0\varepsilon_0}$. The vector identity $\nabla\times(\nabla\times\mathbf{A}) = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A}$ is the key algebraic step in its derivation.

这是波速为 $c = 1/\sqrt{\mu_0\varepsilon_0}$ 的电磁波方程。向量恒等式 $\nabla\times(\nabla\times\mathbf{A}) = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A}$ 是其推导中的关键代数步骤。

---

## G. Two Further Index Identities and Applications · 另外两个指标恒等式及其应用

### G.1 — $\nabla\cdot(\nabla\times\mathbf{A}) = 0$

**Claim.** The divergence of any curl is zero.

**命题。** 任意旋度的散度为零。

**Proof.** In index notation, $\nabla\cdot(\nabla\times\mathbf{A}) = \partial_i(\varepsilon_{ijk} \partial_j A_k) = \varepsilon_{ijk} \partial_i\partial_j A_k$. The product $\varepsilon_{ijk} \partial_i\partial_j$ is a contraction of the antisymmetric symbol $\varepsilon_{ijk}$ (antisymmetric in $i,j$) with the symmetric operator $\partial_i\partial_j = \partial_j\partial_i$ (symmetric in $i,j$, by equality of mixed partials). The contraction of a symmetric and antisymmetric tensor over the same pair of indices always vanishes:

**证明。** 用指标记号，$\nabla\cdot(\nabla\times\mathbf{A}) = \partial_i(\varepsilon_{ijk} \partial_j A_k) = \varepsilon_{ijk} \partial_i\partial_j A_k$。乘积 $\varepsilon_{ijk} \partial_i\partial_j$ 是反对称符号 $\varepsilon_{ijk}$（关于 $i,j$ 反对称）与对称算符 $\partial_i\partial_j = \partial_j\partial_i$（关于 $i,j$ 对称，由混合偏导的相等性保证）的缩并。对称张量与反对称张量在同一对指标上的缩并恒为零：

$$ \varepsilon_{ijk} \partial_i\partial_j A_k = -\varepsilon_{jik} \partial_i\partial_j A_k = -\varepsilon_{ijk} \partial_j\partial_i A_k = -\varepsilon_{ijk} \partial_i\partial_j A_k, $$

where we swapped $i\leftrightarrow j$ and used symmetry of $\partial_i\partial_j$. So $\varepsilon_{ijk} \partial_i\partial_j A_k = 0$. $\blacksquare$

其中交换了 $i\leftrightarrow j$ 并利用了 $\partial_i\partial_j$ 的对称性。故 $\varepsilon_{ijk} \partial_i\partial_j A_k = 0$。$\blacksquare$

**Physical interpretation.** $\nabla\cdot\mathbf{B} = 0$ can be solved by writing $\mathbf{B} = \nabla\times\mathbf{A}$ (the magnetic vector potential). The identity $\nabla\cdot(\nabla\times\mathbf{A}) = 0$ is automatically satisfied, consistent with the absence of magnetic monopoles.

**物理解释。** $\nabla\cdot\mathbf{B} = 0$ 可以通过令 $\mathbf{B} = \nabla\times\mathbf{A}$（磁矢势）来求解。恒等式 $\nabla\cdot(\nabla\times\mathbf{A}) = 0$ 自动满足，与磁单极子不存在相一致。

---

### G.2 — $\nabla\times(\nabla f) = 0$

**Claim.** The curl of any gradient is zero.

**命题。** 任意梯度的旋度为零。

**Proof.** $[\nabla\times(\nabla f)]_i = \varepsilon_{ijk} \partial_j(\partial_k f) = \varepsilon_{ijk} \partial_j\partial_k f$. By the same symmetry/antisymmetry argument ($\varepsilon_{ijk}$ antisymmetric in $j,k$; $\partial_j\partial_k$ symmetric in $j,k$):

**证明。** $[\nabla\times(\nabla f)]_i = \varepsilon_{ijk} \partial_j(\partial_k f) = \varepsilon_{ijk} \partial_j\partial_k f$。由相同的对称/反对称论证（$\varepsilon_{ijk}$ 关于 $j,k$ 反对称；$\partial_j\partial_k$ 关于 $j,k$ 对称）：

$$ \varepsilon_{ijk} \partial_j\partial_k f = 0. \qquad \blacksquare $$

**Physical interpretation.** In electrostatics $\nabla\times\mathbf{E} = 0$ (for a static field), so $\mathbf{E}$ can be written as $\mathbf{E} = -\nabla\phi$ for a scalar potential $\phi$. The identity $\nabla\times(\nabla\phi) = 0$ is then automatically satisfied — the electrostatic field is irrotational.

**物理解释。** 在静电学中 $\nabla\times\mathbf{E} = 0$（对静态场），故 $\mathbf{E}$ 可以写成 $\mathbf{E} = -\nabla\phi$，其中 $\phi$ 是标量势。恒等式 $\nabla\times(\nabla\phi) = 0$ 自动满足——静电场是无旋的。

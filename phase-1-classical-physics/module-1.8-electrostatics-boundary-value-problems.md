# Module 1.8 — Electrostatics & Boundary-Value Problems ⭐
**模块 1.8 — 静电学与边值问题 ⭐**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.8-electrostatics-boundary-value-problems-derivations.md)

---

## 1. Electric Field, Gauss's Law, and the Potential · 电场、高斯定律与电势

**Definition.** The **electric field** $\mathbf{E}(\mathbf{r})$ is the force per unit charge exerted on a stationary test charge. For a point charge $q$ at the origin, Coulomb's law gives $\mathbf{E} = \frac{q}{4\pi\epsilon_0} \cdot \frac{\hat{\mathbf{r}}}{r^2}$. For a continuous charge distribution $\rho(\mathbf{r})$, the field obeys **Gauss's law** in integral and differential forms:

**定义。** **电场** $\mathbf{E}(\mathbf{r})$ 是作用在静止试验电荷上的力除以电荷量。对于位于原点的点电荷 $q$，库仑定律给出 $\mathbf{E} = \frac{q}{4\pi\epsilon_0} \cdot \frac{\hat{\mathbf{r}}}{r^2}$。对于连续电荷分布 $\rho(\mathbf{r})$，电场满足积分形式和微分形式的**高斯定律**：

$$ \oint \mathbf{E} \cdot d\mathbf{A} = \frac{Q_\text{enc}}{\epsilon_0} \quad\Longleftrightarrow\quad \nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}. $$

Since $\nabla \times \mathbf{E} = 0$ for static fields, $\mathbf{E} = -\nabla\phi$, where the **electric potential** $\phi$ satisfies **Poisson's equation**:

由于静电场满足 $\nabla \times \mathbf{E} = 0$，故 $\mathbf{E} = -\nabla\phi$，其中**电势** $\phi$ 满足**泊松方程**：

$$ \nabla^2\phi = -\frac{\rho}{\epsilon_0}. $$

In charge-free regions this reduces to **Laplace's equation** $\nabla^2\phi = 0$.

在无电荷区域，方程化为**拉普拉斯方程** $\nabla^2\phi = 0$。

**Demonstration.** Gauss's law applied to a sphere of radius $r$ around a point charge $q$ gives $\mathbf{E} = \frac{q}{4\pi\epsilon_0 r^2}\,\hat{\mathbf{r}}$ — Coulomb's law recovered. For an infinite line charge $\lambda$ (C/m), a cylindrical Gaussian surface of radius $r$ and length $L$ gives $E = \frac{\lambda}{2\pi\epsilon_0 r}$, pointing radially outward.

**演示。** 将高斯定律应用于以点电荷 $q$ 为中心半径为 $r$ 的球面，得 $\mathbf{E} = \frac{q}{4\pi\epsilon_0 r^2}\,\hat{\mathbf{r}}$——即库仑定律。对于无限线电荷 $\lambda$（C/m），半径为 $r$、长度为 $L$ 的圆柱形高斯面给出 $E = \frac{\lambda}{2\pi\epsilon_0 r}$，方向径向向外。

**Application.** The potential energy of a charge distribution encodes screening, capacitance, and the forces governing atomic structure. Gauss's law is the first of Maxwell's equations (Module 1.10). The Laplace/Poisson structure recurs throughout physics: gravity ($\nabla^2\phi_\text{grav} = 4\pi G\rho$), diffusion, and the time-independent Schrödinger equation in certain limits all share this form.

**应用。** 电荷分布的势能编码了屏蔽效应、电容以及支配原子结构的力。高斯定律是麦克斯韦方程组的第一条（模块 1.10）。拉普拉斯/泊松结构在整个物理学中反复出现：引力（$\nabla^2\phi_\text{grav} = 4\pi G\rho$）、扩散以及某些极限下的定态薛定谔方程都具有这种形式。

## 2. Boundary-Value Problems: Separation of Variables · 边值问题：分离变量法

**Definition.** Solving $\nabla^2\phi = 0$ in a region with specified boundary conditions is a **boundary-value problem**. The uniqueness theorem guarantees that specifying $\phi$ (Dirichlet) or $\partial\phi/\partial n$ (Neumann) on the boundary determines $\phi$ uniquely. In Cartesian, cylindrical, or spherical coordinates, Laplace's equation separates into ODEs (Module 0.3). In spherical coordinates the solutions are **spherical harmonics** $Y_\ell^m(\theta, \phi)$ multiplied by $r^\ell$ or $r^{-(\ell+1)}$.

**定义。** 在给定边界条件的区域内求解 $\nabla^2\phi = 0$ 是一个**边值问题**。唯一性定理保证：在边界上指定 $\phi$（狄利克雷条件）或 $\partial\phi/\partial n$（诺依曼条件）可以唯一确定 $\phi$。在笛卡尔、柱面或球面坐标中，拉普拉斯方程分离为常微分方程（模块 0.3）。在球面坐标中，解为**球谐函数** $Y_\ell^m(\theta, \phi)$ 乘以 $r^\ell$ 或 $r^{-(\ell+1)}$。

**Demonstration.** For a grounded conducting sphere of radius $R$ in a uniform external field $E_0\,\hat{\mathbf{z}}$, separation of variables gives $\phi_\text{out} = -E_0 r\cos\theta + E_0 R^3 \cos\theta / r^2$. The second term is a dipole field; its coefficient is fixed by the boundary condition $\phi(R) = 0$. The induced surface charge density is $\sigma = 3\epsilon_0 E_0 \cos\theta$.

**演示。** 对于均匀外场 $E_0\,\hat{\mathbf{z}}$ 中半径为 $R$ 的接地导体球，分离变量给出 $\phi_\text{out} = -E_0 r\cos\theta + E_0 R^3 \cos\theta / r^2$。第二项为偶极子场，其系数由边界条件 $\phi(R) = 0$ 确定。感应面电荷密度为 $\sigma = 3\epsilon_0 E_0 \cos\theta$。

**Application.** Boundary-value methods determine the capacitance of arbitrary geometries, the fields inside waveguides, and the electrostatic energy of molecular charge distributions. The method of images provides elegant shortcuts for planar and spherical conductors. The spherical-harmonic solutions here are identical to the angular wavefunctions of the hydrogen atom (Module 3.4), making this a direct classical foundation for quantum central-force problems.

**应用。** 边值方法确定任意几何形状的电容、波导内部的场以及分子电荷分布的静电能。镜像法为平面和球面导体提供了优雅的捷径。这里的球谐函数解与氢原子角向波函数（模块 3.4）完全相同，使本节成为量子有心力问题的直接经典基础。

---

**Self-test (blank page)**

1. State Gauss's law in both integral and differential forms. Use the integral form to find $\mathbf{E}$ at distance $r$ from an infinite uniformly charged plane with surface charge density $\sigma$.
2. A solid sphere of radius $R$ carries uniform charge density $\rho$. Find $\phi(r)$ everywhere by solving Poisson's equation with appropriate boundary conditions.
3. What is the uniqueness theorem for electrostatic boundary-value problems, and why is it practically important?
4. Explain why $\nabla \times \mathbf{E} = 0$ in electrostatics allows you to introduce a scalar potential. What breaks this and what replaces it in electrodynamics (Module 1.10)?

**自测（空白页）**

1. 分别用积分形式和微分形式陈述高斯定律。用积分形式求距面电荷密度为 $\sigma$ 的无限均匀带电平面距离为 $r$ 处的 $\mathbf{E}$。
2. 半径为 $R$ 的实心球均匀带电，电荷密度为 $\rho$。通过求解带适当边界条件的泊松方程，求各处的 $\phi(r)$。
3. 静电边值问题的唯一性定理是什么？为什么它在实践中很重要？
4. 解释为什么静电学中 $\nabla \times \mathbf{E} = 0$ 允许引入标量电势。在电动力学（模块 1.10）中，什么打破了这一条件，什么取而代之？

---

← Previous: [Module 1.7 — Rigid-Body Dynamics & Non-Inertial Frames](./module-1.7-rigid-body-non-inertial-frames.md) · [Phase 1 index](./README.md) · Next: [Module 1.9 — Magnetostatics](./module-1.9-magnetostatics.md) →

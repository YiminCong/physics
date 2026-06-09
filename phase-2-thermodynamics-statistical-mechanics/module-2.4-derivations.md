---
title: "Derivations — Module 2.4: Classical Statistical Mechanics"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 2.4: Classical Statistical Mechanics
# 推导 — 模块 2.4：经典统计力学

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 2.4](./module-2.4-classical-statistical-mechanics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 2.4](./module-2.4-classical-statistical-mechanics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Boltzmann Distribution from Maximum Entropy · 从最大熵推导玻尔兹曼分布

**Claim.** For a system in thermal contact with a reservoir at temperature $T$, the equilibrium probability of microstate $i$ with energy $E_i$ is $p_i = e^{-\beta E_i}/Z$, where $\beta = 1/(k_B T)$ and $Z = \sum_i e^{-\beta E_i}$.

**命题。** 对于与温度为 $T$ 的热库热接触的系统，能量为 $E_i$ 的微观态 $i$ 的平衡概率为 $p_i = e^{-\beta E_i}/Z$，其中 $\beta = 1/(k_B T)$，$Z = \sum_i e^{-\beta E_i}$。

**Step 1 — Set up the constrained maximization.** We seek the probability distribution $\{p_i\}$ that maximizes the Gibbs–Boltzmann entropy

**第 1 步 — 建立约束极大化问题。** 我们寻找使吉布斯–玻尔兹曼熵极大的概率分布 $\{p_i\}$

$$ S[\{p_i\}] = -k_B \sum_i p_i \ln p_i, $$

subject to two constraints:

在两个约束条件下：

- (1) Normalization · 归一化:  $\sum_i p_i = 1$,
- (2) Fixed mean energy · 固定平均能量:  $\sum_i p_i E_i = U$  (fixed by the reservoir temperature $T$).

**Step 2 — Introduce Lagrange multipliers.** Form the Lagrangian

**第 2 步 — 引入拉格朗日乘子。** 构造拉格朗日量

$$ L = -k_B \sum_i p_i \ln p_i - \lambda\Big(\sum_i p_i - 1\Big) - \beta k_B\Big(\sum_i p_i E_i - U\Big), $$

where $\lambda$ and $\beta$ are undetermined multipliers for the two constraints.

其中 $\lambda$ 和 $\beta$ 是两个约束条件对应的待定乘子。

**Step 3 — Differentiate with respect to $p_j$ and set to zero.** For each $j$:

**第 3 步 — 对 $p_j$ 微分并令其为零。** 对每个 $j$：

$$ \frac{\partial L}{\partial p_j} = -k_B\,(\ln p_j + 1) - \lambda - \beta k_B E_j = 0. $$

Solving for $p_j$:

求解 $p_j$：

$$ \ln p_j = -1 - \frac{\lambda}{k_B} - \beta E_j, \qquad p_j = \exp\!\Big(-1 - \frac{\lambda}{k_B}\Big)\,\exp(-\beta E_j) = C\, e^{-\beta E_j}, $$

where $C = e^{-1 - \lambda/k_B}$ is a constant.

其中 $C = e^{-1 - \lambda/k_B}$ 是常数。

**Step 4 — Fix the constant via normalization.** Applying $\sum_j p_j = 1$:

**第 4 步 — 通过归一化确定常数。** 应用 $\sum_j p_j = 1$：

$$ C \sum_j e^{-\beta E_j} = 1 \;\implies\; C = \frac{1}{Z}, \qquad \text{where } Z = \sum_j e^{-\beta E_j}. $$

Therefore the Boltzmann distribution is

因此玻尔兹曼分布为

$$ \boxed{\, p_j = \frac{e^{-\beta E_j}}{Z} \,} \qquad \blacksquare $$

**Step 5 — Identify $\beta$ with temperature.** To connect $\beta$ to the thermodynamic temperature $T$, compute the entropy:

**第 5 步 — 将 $\beta$ 与温度对应。** 为将 $\beta$ 与热力学温度 $T$ 联系起来，计算熵：

$$ S = -k_B \sum_j p_j \ln p_j = -k_B \sum_j p_j\,(-\beta E_j - \ln Z) = k_B \beta \sum_j p_j E_j + k_B \ln Z = k_B \beta U + k_B \ln Z. $$

From thermodynamics, $\partial S/\partial U = 1/T$ (at fixed $V$), so

由热力学，$\partial S/\partial U = 1/T$（固定 $V$），故

$$ \frac{\partial S}{\partial U} = k_B \beta = \frac{1}{T} \;\implies\; \boxed{\,\beta = \frac{1}{k_B T}\,} \qquad \blacksquare $$

---

## B. Partition Function, Free Energy, and Average Energy · 配分函数、自由能与平均能量

**Claim.** With $Z = \sum_i e^{-\beta E_i}$, the Helmholtz free energy is $F = -k_B T \ln Z$ and the mean energy is $U = -\partial(\ln Z)/\partial\beta$.

**命题。** 令 $Z = \sum_i e^{-\beta E_i}$，则亥姆霍兹自由能为 $F = -k_B T \ln Z$，平均能量为 $U = -\partial(\ln Z)/\partial\beta$。

**Step 1 — Derive $F = -k_B T \ln Z$.** From Step 5 above, $S = k_B \beta U + k_B \ln Z$. Now $F = U - TS$:

**第 1 步 — 推导 $F = -k_B T \ln Z$。** 由上述第 5 步，$S = k_B \beta U + k_B \ln Z$。现在 $F = U - TS$：

$$ F = U - T\,(k_B \beta U + k_B \ln Z) = U - k_B T\cdot\frac{U}{k_B T} - k_B T \ln Z = U - U - k_B T \ln Z, $$

$$ \boxed{\, F = -k_B T \ln Z \,} \qquad \blacksquare $$

**Step 2 — Derive $U = -\partial(\ln Z)/\partial\beta$.** The mean energy is

**第 2 步 — 推导 $U = -\partial(\ln Z)/\partial\beta$。** 平均能量为

$$ U = \sum_i p_i E_i = \sum_i \frac{e^{-\beta E_i}}{Z}\,E_i = \frac{1}{Z}\sum_i E_i\, e^{-\beta E_i}. $$

Observe that $\partial/\partial\beta\,[e^{-\beta E_i}] = -E_i\, e^{-\beta E_i}$, so $\sum_i E_i\, e^{-\beta E_i} = -\partial Z/\partial\beta$. Therefore

注意到 $\partial/\partial\beta\,[e^{-\beta E_i}] = -E_i\, e^{-\beta E_i}$，故 $\sum_i E_i\, e^{-\beta E_i} = -\partial Z/\partial\beta$。因此

$$ U = \frac{1}{Z}\Big(-\frac{\partial Z}{\partial\beta}\Big) = -\frac{1}{Z}\frac{\partial Z}{\partial\beta} = \boxed{\,-\frac{\partial(\ln Z)}{\partial\beta}\,} \qquad \blacksquare $$

**Step 3 — Derive $S$ from $F$.** Using $S = -(\partial F/\partial T)_V = \partial(k_B T \ln Z)/\partial T$:

**第 3 步 — 从 $F$ 推导 $S$。** 利用 $S = -(\partial F/\partial T)_V = \partial(k_B T \ln Z)/\partial T$：

$$ S = k_B \ln Z + k_B T\,\Big(\frac{\partial \ln Z}{\partial T}\Big)_V = k_B \ln Z + k_B \beta U = k_B(\ln Z + \beta U). \qquad \blacksquare $$

This confirms the consistency with the result from Step 5 of section A.

这与第 A 节第 5 步的结果一致，验证了自洽性。

---

## C. Equipartition Theorem: $\langle \tfrac12 m v^2\rangle = \tfrac32 k_B T$ · 能均分定理

**Claim.** For a classical system whose Hamiltonian contains a term $\tfrac12 m v_x^2$ (or any term of the form $\tfrac12 A q^2$ for a generalized coordinate $q$ with constant $A$), the thermal average of that term is $\tfrac12 k_B T$. For a free particle in 3D, $\langle \tfrac12 m|\mathbf v|^2\rangle = \tfrac12 m(\langle v_x^2\rangle + \langle v_y^2\rangle + \langle v_z^2\rangle) = \tfrac32 k_B T$.

**命题。** 对于哈密顿量中含有 $\tfrac12 m v_x^2$（或任何形如 $\tfrac12 A q^2$ 的项，$q$ 为广义坐标，$A$ 为常数）的经典系统，该项的热平均值为 $\tfrac12 k_B T$。对于三维自由粒子，$\langle \tfrac12 m|\mathbf v|^2\rangle = \tfrac12 m(\langle v_x^2\rangle + \langle v_y^2\rangle + \langle v_z^2\rangle) = \tfrac32 k_B T$。

**Step 1 — Write the Boltzmann average for one degree of freedom.** For one Cartesian velocity component $v_x$, the probability density is proportional to $e^{-\beta m v_x^2/2}$, and the canonical average is

**第 1 步 — 对一个自由度写出玻尔兹曼平均。** 对于一个笛卡尔速度分量 $v_x$，概率密度正比于 $e^{-\beta m v_x^2/2}$，正则平均为

$$ \Big\langle \tfrac12 m v_x^2\Big\rangle = \frac{\displaystyle\int_{-\infty}^{\infty} \tfrac12 m v_x^2\, e^{-\beta m v_x^2/2}\,dv_x}{\displaystyle\int_{-\infty}^{\infty} e^{-\beta m v_x^2/2}\,dv_x}. $$

**Step 2 — Evaluate using Gaussian integrals.** Using the standard Gaussian integrals (with $a = \beta m/2 > 0$):

**第 2 步 — 用高斯积分求值。** 利用标准高斯积分（$a = \beta m/2 > 0$）：

$$ \int_{-\infty}^{\infty} e^{-a v^2}\,dv = \sqrt{\frac{\pi}{a}}, \qquad \int_{-\infty}^{\infty} v^2 e^{-a v^2}\,dv = \frac12\sqrt{\frac{\pi}{a^3}} \quad\Big[= -\frac{d}{da}\text{ of the first integral}\Big]. $$

Therefore the denominator is $\sqrt{\pi/a}$ and the numerator is $\tfrac12 m\cdot\tfrac12\sqrt{\pi/a^3}$:

因此分母为 $\sqrt{\pi/a}$，分子为 $\tfrac12 m\cdot\tfrac12\sqrt{\pi/a^3}$：

$$ \Big\langle \tfrac12 m v_x^2\Big\rangle = \frac{\tfrac12 m\cdot\tfrac12\sqrt{\pi/a^3}}{\sqrt{\pi/a}} = \frac{m}{4}\cdot\frac1a = \frac{m}{4}\cdot\frac{2}{\beta m} = \frac{1}{2\beta} = \boxed{\,\tfrac12 k_B T\,} \qquad \blacksquare $$

**Step 3 — Sum over three dimensions.** By isotropy, $\langle v_x^2\rangle = \langle v_y^2\rangle = \langle v_z^2\rangle$, so

**第 3 步 — 对三维求和。** 由各向同性，$\langle v_x^2\rangle = \langle v_y^2\rangle = \langle v_z^2\rangle$，故

$$ \Big\langle \tfrac12 m|\mathbf v|^2\Big\rangle = \tfrac12 m(\langle v_x^2\rangle + \langle v_y^2\rangle + \langle v_z^2\rangle) = 3\cdot\tfrac12 k_B T = \boxed{\,\tfrac32 k_B T\,} \qquad \blacksquare $$

**Step 4 — General statement of equipartition.** More generally, for any term of the form $H_i = \tfrac12 A q_i^2$ in the Hamiltonian where $q_i$ ranges from $-\infty$ to $\infty$ and $A$ is independent of $q_i$:

**第 4 步 — 能均分定理的一般表述。** 更一般地，对于哈密顿量中任何形如 $H_i = \tfrac12 A q_i^2$ 的项，其中 $q_i$ 从 $-\infty$ 到 $\infty$，$A$ 与 $q_i$ 无关：

$$ \Big\langle \tfrac12 A q_i^2\Big\rangle = \tfrac12 k_B T. $$

Proof: $\langle \tfrac12 A q^2\rangle = \int \tfrac12 A q^2\, e^{-\beta\cdot\frac12 A q^2}\,dq \big/ \int e^{-\beta\cdot\frac12 A q^2}\,dq$. With $a = \beta A/2$, this equals $(1/4a)(A) = A/(4\beta A/2) = 1/(2\beta) = \tfrac12 k_B T$, by the same Gaussian-integral calculation as above. This applies equally to kinetic-energy terms ($\tfrac12 m v^2$) and harmonic potential-energy terms ($\tfrac12 k x^2$). $\blacksquare$

证明：$\langle \tfrac12 A q^2\rangle = \int \tfrac12 A q^2\, e^{-\beta\cdot\frac12 A q^2}\,dq \big/ \int e^{-\beta\cdot\frac12 A q^2}\,dq$。令 $a = \beta A/2$，等于 $(1/4a)(A) = A/(4\beta A/2) = 1/(2\beta) = \tfrac12 k_B T$，与上述高斯积分计算相同。这同样适用于动能项（$\tfrac12 m v^2$）和谐振势能项（$\tfrac12 k x^2$）。$\blacksquare$

**Step 5 — Failure of equipartition and the quantum correction.** Equipartition requires that (i) the degree of freedom is classical, (ii) the energy is quadratic, and (iii) the variable ranges over all reals. It fails when $\hbar\omega \gg k_B T$ (quantum freeze-out): a harmonic oscillator with quantum spacing $\hbar\omega$ has average energy $\langle E\rangle = \hbar\omega/(e^{\beta\hbar\omega} - 1) \to k_B T$ only when $k_B T \gg \hbar\omega$. This is why vibrational modes of molecules and phonons at low $T$ contribute less than equipartition predicts.

**第 5 步 — 能均分定理的失效与量子修正。** 能均分定理要求：(i) 自由度是经典的，(ii) 能量是二次型，(iii) 变量遍历所有实数。当 $\hbar\omega \gg k_B T$ 时失效（量子冻结）：量子间距为 $\hbar\omega$ 的谐振子具有平均能量 $\langle E\rangle = \hbar\omega/(e^{\beta\hbar\omega} - 1) \to k_B T$ 仅当 $k_B T \gg \hbar\omega$ 时。这就是为什么分子的振动模式和低温声子的贡献小于能均分定理预测值的原因。

---

## D. Boltzmann's Relation $S = k_B \ln \Omega$ from the Canonical Ensemble · 从正则系综推导玻尔兹曼关系

**Claim.** In the microcanonical ensemble (isolated system), the thermodynamic entropy $S$ equals $k_B \ln \Omega$, where $\Omega$ is the number of accessible microstates.

**命题。** 在微正则系综（孤立系统）中，热力学熵 $S$ 等于 $k_B \ln \Omega$，其中 $\Omega$ 为可及微观态数目。

**Step 1 — Maximum entropy principle in the microcanonical ensemble.** In an isolated system with fixed $E, V, N$, all $\Omega$ microstates are equally probable (fundamental postulate). The Gibbs entropy is

**第 1 步 — 微正则系综中的最大熵原理。** 在能量 $E$、体积 $V$、粒子数 $N$ 固定的孤立系统中，所有 $\Omega$ 个微观态等概率出现（基本假设）。吉布斯熵为

$$ S = -k_B \sum_{i=1}^{\Omega} p_i \ln p_i = -k_B \sum_{i=1}^{\Omega} \frac{1}{\Omega}\ln\frac{1}{\Omega} = -k_B\cdot\Omega\cdot\frac{1}{\Omega}\cdot(-\ln\Omega) = \boxed{\,k_B \ln \Omega\,} \qquad \blacksquare $$

**Step 2 — Consistency with the canonical result.** In the canonical ensemble, $S = k_B(\ln Z + \beta U)$. For a macroscopic system with a sharp energy distribution (relative fluctuation $\sigma_E/U \sim 1/\sqrt{N} \to 0$), the sum $Z \approx \Omega(U)\, e^{-\beta U}$ (where $\Omega(U)$ is the density of states at energy $U$ times the energy window). Then

**第 2 步 — 与正则结果的一致性。** 在正则系综中，$S = k_B(\ln Z + \beta U)$。对于具有尖锐能量分布（相对涨落 $\sigma_E/U \sim 1/\sqrt{N} \to 0$）的宏观系统，$Z \approx \Omega(U)\, e^{-\beta U}$（其中 $\Omega(U)$ 是能量 $U$ 处的态密度乘以能量窗口），则

$$ \ln Z \approx \ln \Omega(U) - \beta U, \qquad S \approx k_B(\ln \Omega(U) - \beta U + \beta U) = k_B \ln \Omega(U). \qquad \blacksquare $$

The two ensembles agree in the thermodynamic limit, justifying using whichever ensemble is most convenient for a given calculation.

两种系综在热力学极限下一致，这为在给定计算中使用最方便的系综提供了依据。

---

*The derivations here — maximum entropy with Lagrange multipliers, Gaussian integrals, and ensemble equivalence — are the three core technical tools of classical statistical mechanics. They recur verbatim in quantum statistics (Module 2.5) and in the path-integral formulation of quantum field theory (Module 6.1).*

*此处的推导——带拉格朗日乘子的最大熵、高斯积分和系综等价——是经典统计力学的三个核心技术工具。它们在量子统计（模块 2.5）和量子场论的路径积分表述（模块 6.1）中逐字重现。*

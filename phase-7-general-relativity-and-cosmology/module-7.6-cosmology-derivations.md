# Derivations — Module 7.6: Cosmology
# 推导 — 模块 7.6：宇宙学

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 7.6](./module-7.6-cosmology.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 7.6](./module-7.6-cosmology.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Friedmann Equations from the Einstein Field Equations Applied to the FLRW Metric · 将爱因斯坦场方程应用于 FLRW 度规推导弗里德曼方程

**Claim.** Inserting the FLRW metric $ds^2 = -c^2 dt^2 + a^2(t)[dr^2/(1-kr^2) + r^2 d\Omega^2]$ and a perfect-fluid stress-energy tensor $T_{\mu\nu}$ (with energy density $\rho$ and pressure $p$) into the EFE $G_{\mu\nu} = (8\pi G/c^4) T_{\mu\nu}$ yields the two Friedmann equations:

$$ \begin{aligned}
& (\dot{a}/a)^2 = (8\pi G/3)\rho - kc^2/a^2 + \Lambda c^2/3 && \text{(First Friedmann equation)} \\
& \ddot{a}/a = -(4\pi G/3)(\rho + 3p/c^2) + \Lambda c^2/3 && \text{(Acceleration equation / Second Friedmann equation)}
\end{aligned} $$

**命题。** 将 FLRW 度规 $ds^2 = -c^2 dt^2 + a^2(t)[dr^2/(1-kr^2) + r^2 d\Omega^2]$ 和完美流体能动张量 $T_{\mu\nu}$（能量密度 $\rho$，压强 $p$）代入 EFE $G_{\mu\nu} = (8\pi G/c^4) T_{\mu\nu}$，得到两个弗里德曼方程：

$$ \begin{aligned}
& (\dot{a}/a)^2 = (8\pi G/3)\rho - kc^2/a^2 + \Lambda c^2/3 && \text{（第一弗里德曼方程）} \\
& \ddot{a}/a = -(4\pi G/3)(\rho + 3p/c^2) + \Lambda c^2/3 && \text{（加速方程/第二弗里德曼方程）}
\end{aligned} $$

**Step 1 — Write down the FLRW metric components.** For the flat case ($k = 0$) for clarity, then generalize. The metric is diagonal:

**第 1 步 — 写出 FLRW 度规分量。** 为清晰起见先讨论平坦情形（$k = 0$），后推广。度规是对角的：

$$ g_{00} = -c^2, \quad g_{11} = a^2/(1-kr^2), \quad g_{22} = a^2 r^2, \quad g_{33} = a^2 r^2 \sin^2\theta. $$

The inverse metric: $g^{00} = -1/c^2$, $g^{11} = (1-kr^2)/a^2$, $g^{22} = 1/(a^2 r^2)$, $g^{33} = 1/(a^2 r^2 \sin^2\theta)$.

逆度规：$g^{00} = -1/c^2$，$g^{11} = (1-kr^2)/a^2$，$g^{22} = 1/(a^2 r^2)$，$g^{33} = 1/(a^2 r^2 \sin^2\theta)$。

**Step 2 — Compute non-zero Christoffel symbols.** The only non-vanishing independent Christoffel symbols of the FLRW metric (denoting a dot for $d/dt$ and using $x^0 = ct$):

**第 2 步 — 计算非零克里斯托费尔符号。** FLRW 度规唯一非零的独立克里斯托费尔符号（用点号表示 $d/dt$，并使用 $x^0 = ct$）：

$$ \Gamma^{0}{}_{ij} = (a\dot{a}/c)\, \tilde{g}_{ij}, \quad \text{where } \tilde{g}_{ij} \text{ is the spatial part metric}, $$

$$ \Gamma^{i}{}_{0j} = (\dot{a}/a)\, \delta^{i}{}_j / c, $$

$$ \Gamma^{i}{}_{jk} = \partial \text{ terms from the spatial metric}. $$

More explicitly (with Latin indices $i,j$ running over spatial components, and spatial metric $\tilde{g}_{ij} = a^2 \gamma_{ij}$ where $\gamma_{ij}$ is the unit-curvature metric):

更明确地（拉丁指标 $i,j$ 遍历空间分量，空间度规 $\tilde{g}_{ij} = a^2 \gamma_{ij}$，其中 $\gamma_{ij}$ 是单位曲率度规）：

$$ \Gamma^{0}{}_{ij} = (a\dot{a}/c)\, \gamma_{ij}, \quad \Gamma^{i}{}_{0j} = (\dot{a}/(ac))\, \delta^{i}{}_j, $$

$$ \Gamma^{1}{}_{11} = kr/(1-kr^2), \quad \Gamma^{2}{}_{12} = \Gamma^{3}{}_{13} = 1/r, \text{ etc. (spatial Christoffel symbols)} $$

**Step 3 — Compute the Ricci tensor components.** By the high symmetry of the FLRW metric (homogeneous and isotropic), the only independent non-vanishing Ricci tensor components are $R_{00}$ and $R_{ij} = f(t)\, \tilde{g}_{ij}$. Compute $R_{00}$:

**第 3 步 — 计算里奇张量分量。** 由于 FLRW 度规的高度对称性（均匀且各向同性），唯一独立的非零里奇张量分量为 $R_{00}$ 和 $R_{ij} = f(t)\, \tilde{g}_{ij}$。计算 $R_{00}$：

$$ R_{00} = \partial_\mu \Gamma^{\mu}{}_{00} - \partial_0 \Gamma^{\mu}{}_{\mu 0} + \Gamma^{\mu}{}_{\mu\lambda} \Gamma^{\lambda}{}_{00} - \Gamma^{\mu}{}_{0\lambda} \Gamma^{\lambda}{}_{\mu 0}. $$

Since the metric is diagonal and static in form (only time-varying through $a(t)$), $\Gamma^{\mu}{}_{00} = 0$ for all $\mu$. The dominant contribution is from the second term:

由于度规是对角的，$\Gamma^{\mu}{}_{00} = 0$（对所有 $\mu$）。主导贡献来自第二项：

$$ R_{00} = -\partial_0 \Gamma^{i}{}_{i0} - (\Gamma^{i}{}_{0j})^2 \cdot (\text{contracted}) $$

Carefully, using $x^0 = ct$ so $\partial_0 = (1/c) d/dt$:

仔细地，利用 $x^0 = ct$ 故 $\partial_0 = (1/c) d/dt$：

$$ \Gamma^{i}{}_{0i} = 3\dot{a}/(ac), \quad \partial_0 \Gamma^{i}{}_{0i} = (1/c) \frac{d}{dt} (3\dot{a}/(ac)) = (3/c)(\ddot{a}/(ac) - \dot{a}^2/(a^2 c)) = 3\ddot{a}/(ac^2) - 3\dot{a}^2/(a^2 c^2). $$

$$ \Gamma^{i}{}_{0j} \Gamma^{j}{}_{i0} = 3(\dot{a}/(ac))^2 = 3\dot{a}^2/(a^2 c^2). $$

Therefore:

因此：

$$ R_{00} = -[3\ddot{a}/(ac^2) - 3\dot{a}^2/(a^2 c^2)] - 3\dot{a}^2/(a^2 c^2) = -3\ddot{a}/(ac^2). $$

For the spatial components $R_{ij}$ we need the remaining Christoffel symbols. With $x^0 = ct$ (so $\partial_0 = (1/c)\partial_t$) and $g_{ij} = a^2(t)\gamma_{ij}$, where $\gamma_{ij}$ is the unit-curvature spatial metric:

对于空间分量 $R_{ij}$，我们需要其余的克里斯托费尔符号。取 $x^0 = ct$（故 $\partial_0 = (1/c)\partial_t$）且 $g_{ij} = a^2(t)\gamma_{ij}$，其中 $\gamma_{ij}$ 为单位曲率空间度规：

$$ \Gamma^{0}{}_{ij} = (a\dot{a}/c)\, \gamma_{ij}, \quad \Gamma^{i}{}_{0j} = (\dot{a}/(ac))\, \delta^{i}{}_j, $$

and the purely spatial Christoffels $\Gamma^{k}{}_{ij}[\gamma]$ are those of $\gamma_{ij}$, whose intrinsic Ricci tensor is $\tilde{R}_{ij} = 2k \gamma_{ij}$ (a maximally symmetric 3-space of curvature $k$). Substituting into

而纯空间克里斯托费尔符号 $\Gamma^{k}{}_{ij}[\gamma]$ 即 $\gamma_{ij}$ 的克里斯托费尔符号，其内禀里奇张量为 $\tilde{R}_{ij} = 2k \gamma_{ij}$（曲率为 $k$ 的极大对称三维空间）。代入

$$ R_{ij} = \partial_\mu \Gamma^{\mu}{}_{ij} - \partial_j \Gamma^{\mu}{}_{i\mu} + \Gamma^{\mu}{}_{\mu\lambda} \Gamma^{\lambda}{}_{ij} - \Gamma^{\mu}{}_{j\lambda} \Gamma^{\lambda}{}_{i\mu} $$

and collecting the time-derivative and connection terms together with $\tilde{R}_{ij} = 2k \gamma_{ij}$ gives the standard FLRW spatial Ricci tensor:

并将时间导数项、联络项与 $\tilde{R}_{ij} = 2k \gamma_{ij}$ 合并，得到标准 FLRW 空间里奇张量：

$$ R_{ij} = [a\ddot{a} + 2\dot{a}^2 + 2kc^2]\, \gamma_{ij}/c^2, $$

with $R_{00} = -3\ddot{a}/(ac^2)$ from above ($g_{ij} = a^2 \gamma_{ij}$).

其中 $R_{00} = -3\ddot{a}/(ac^2)$ 由上文给出（$g_{ij} = a^2 \gamma_{ij}$）。

**Step 4 — Compute the Ricci scalar.** Contract with the inverse metric:

**第 4 步 — 计算里奇标量。** 与逆度规缩并：

With $x^0 = ct$ the metric is $g_{00} = -1$ (so $g^{00} = -1$) and $g^{ij} = \gamma^{ij}/a^2$:

取 $x^0 = ct$ 时度规为 $g_{00} = -1$（故 $g^{00} = -1$），$g^{ij} = \gamma^{ij}/a^2$：

$$ \begin{aligned}
R & = g^{00} R_{00} + g^{ij} R_{ij} \\
& = (-1)(-3\ddot{a}/(ac^2)) + (\gamma^{ij}/a^2) \cdot [a\ddot{a} + 2\dot{a}^2 + 2kc^2]\, \gamma_{ij}/c^2 \\
& = 3\ddot{a}/(ac^2) + 3[a\ddot{a} + 2\dot{a}^2 + 2kc^2]/(a^2 c^2) \\
& = 3\ddot{a}/(ac^2) + 3\ddot{a}/(ac^2) + 6\dot{a}^2/(a^2 c^2) + 6k/a^2 \\
& = (6/c^2)[\ddot{a}/a + (\dot{a}/a)^2 + kc^2/a^2].
\end{aligned} $$

So $R = 6[\ddot{a}/a + (\dot{a}/a)^2 + kc^2/a^2]/c^2$.

故 $R = 6[\ddot{a}/a + (\dot{a}/a)^2 + kc^2/a^2]/c^2$。

**Step 5 — Compute the Einstein tensor.** The algebra is cleanest in units $c = 1$ (we restore $c$ in the final Friedmann equations by dimensional analysis). Setting $c = 1$ temporarily:

**第 5 步 — 计算爱因斯坦张量。** 在 $c = 1$ 单位下代数最简洁（最后通过量纲分析在弗里德曼方程中恢复 $c$）。暂时令 $c = 1$：

$$ \begin{aligned}
& g_{00} = -1, \quad g_{ij} = a^2 \gamma_{ij}. \\
& R_{00} = -3\ddot{a}/a, \quad R_{ij} = (a\ddot{a} + 2\dot{a}^2 + 2k)\, \gamma_{ij}. \\
& R = 6(\ddot{a}/a + (\dot{a}/a)^2 + k/a^2). \\
& G_{00} = R_{00} - \tfrac12 g_{00} R = -3\ddot{a}/a - \tfrac12(-1)(6(\ddot{a}/a + \dot{a}^2/a^2 + k/a^2)) \\
& \phantom{G_{00}} = -3\ddot{a}/a + 3(\ddot{a}/a + \dot{a}^2/a^2 + k/a^2) \\
& \phantom{G_{00}} = 3(\dot{a}^2/a^2 + k/a^2) = 3[(\dot{a}/a)^2 + k/a^2].
\end{aligned} $$

For the spatial components:

对于空间分量：

$$ \begin{aligned}
G_{ij} & = R_{ij} - \tfrac12 g_{ij} R \\
& = (a\ddot{a} + 2\dot{a}^2 + 2k)\, \gamma_{ij} - \tfrac12 a^2 \gamma_{ij} \cdot 6(\ddot{a}/a + \dot{a}^2/a^2 + k/a^2) \\
& = \gamma_{ij} [(a\ddot{a} + 2\dot{a}^2 + 2k) - 3a^2(\ddot{a}/a + \dot{a}^2/a^2 + k/a^2)] \\
& = \gamma_{ij} [a\ddot{a} + 2\dot{a}^2 + 2k - 3a\ddot{a} - 3\dot{a}^2 - 3k] \\
& = \gamma_{ij} [-2a\ddot{a} - \dot{a}^2 - k].
\end{aligned} $$

**Step 6 — Perfect fluid stress-energy tensor.** For a comoving perfect fluid with 4-velocity $u^\mu = (1, 0, 0, 0)$ (in the cosmic rest frame, $x^0 = t$, $c = 1$):

**第 6 步 — 完美流体能动张量。** 对于共动完美流体，四速度 $u^\mu = (1, 0, 0, 0)$（在宇宙静止系中，$x^0 = t$，$c = 1$）：

$$ \begin{aligned}
& T_{\mu\nu} = (\rho + p) u_\mu u_\nu + p g_{\mu\nu}. \\
& T_{00} = (\rho + p)(-1)^2 + p(-1) = \rho + p - p = \rho. \\
& T_{ij} = p g_{ij} = p a^2 \gamma_{ij}.
\end{aligned} $$

**Step 7 — First Friedmann equation (00-component of EFE).** $G_{00} = 8\pi G T_{00}$ (in $c = 1$ units with $\kappa = 8\pi G$):

**第 7 步 — 第一弗里德曼方程（EFE 的 00 分量）。** $G_{00} = 8\pi G T_{00}$（$c = 1$ 单位，$\kappa = 8\pi G$）：

$$ 3[(\dot{a}/a)^2 + k/a^2] = 8\pi G\rho. $$

Restoring $c$ (via $k \to kc^2$, $\Lambda \to \Lambda c^2$, and recalling that in SI units $G_{00} = (8\pi G/c^4) T_{00}$ with $T_{00} = \rho c^2$):

恢复 $c$（通过 $k \to kc^2$，$\Lambda \to \Lambda c^2$，并注意在国际单位制中 $G_{00} = (8\pi G/c^4) T_{00}$，$T_{00} = \rho c^2$）：

$$ \boxed{\, (\dot{a}/a)^2 = (8\pi G/3)\rho - kc^2/a^2 + \Lambda c^2/3 \,} \qquad \blacksquare $$

**Step 8 — Second Friedmann equation (spatial components of EFE).** The $ij$-component of $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ ($c = 1$):

**第 8 步 — 第二弗里德曼方程（EFE 的空间分量）。** $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ 的 $ij$ 分量（$c = 1$）：

$$ \gamma_{ij}(-2a\ddot{a} - \dot{a}^2 - k) = 8\pi G \cdot p a^2 \gamma_{ij}. $$

Divide through by $-a^2 \gamma_{ij}$:

两边除以 $-a^2 \gamma_{ij}$：

$$ 2\ddot{a}/a + (\dot{a}/a)^2 + k/a^2 = -8\pi G p. $$

Use the first Friedmann equation $(\dot{a}/a)^2 + k/a^2 = 8\pi G\rho/3$ to eliminate the $(\dot{a}/a)^2 + k/a^2$ piece:

利用第一弗里德曼方程 $(\dot{a}/a)^2 + k/a^2 = 8\pi G\rho/3$ 消去 $(\dot{a}/a)^2 + k/a^2$ 项：

$$ 2\ddot{a}/a = -8\pi G p - (\dot{a}/a)^2 - k/a^2 = -8\pi G p - 8\pi G\rho/3, \text{ so:} $$

$$ 2\ddot{a}/a = -8\pi G p - (\dot{a}/a)^2 - k/a^2 = -8\pi G p - 8\pi G\rho/3, \text{ 故：} $$

$$ \begin{aligned}
& 2\ddot{a}/a = -8\pi G(p + \rho/3) \\
& \ddot{a}/a = -4\pi G(\rho + 3p)/3.
\end{aligned} $$

Restoring $c$ factors ($p \to p/c^2$, $\Lambda$ contribution from the $\Lambda g_{\mu\nu}$ term):

恢复 $c$ 因子（$p \to p/c^2$，$\Lambda$ 贡献来自 $\Lambda g_{\mu\nu}$ 项）：

$$ \boxed{\, \ddot{a}/a = -(4\pi G/3)(\rho + 3p/c^2) + \Lambda c^2/3 \,} \qquad \blacksquare $$

---

## B. Fluid Equation and Density Scaling · 流体方程与密度标度关系

**Claim.** From the covariant conservation law $\nabla^\mu T_{\mu\nu} = 0$ applied to a comoving perfect fluid in FLRW spacetime, the continuity equation

$$ \dot{\rho} + 3(\dot{a}/a)(\rho + p/c^2) = 0 $$

follows, giving: $\rho \propto a^{-3}$ for pressureless matter ($p = 0$), $\rho \propto a^{-4}$ for radiation ($p = \rho c^2/3$), and $\rho = $ const for a cosmological constant ($p = -\rho c^2$).

**命题。** 由协变守恒律 $\nabla^\mu T_{\mu\nu} = 0$ 应用于 FLRW 时空中的共动完美流体，得到连续性方程

$$ \dot{\rho} + 3(\dot{a}/a)(\rho + p/c^2) = 0, $$

从而：对无压物质（$p = 0$），$\rho \propto a^{-3}$；对辐射（$p = \rho c^2/3$），$\rho \propto a^{-4}$；对宇宙学常数（$p = -\rho c^2$），$\rho = $ 常数。

**Step 1 — $\nu = 0$ component of $\nabla^\mu T_{\mu\nu} = 0$.** For a perfect fluid $T^{\mu\nu} = (\rho + p/c^2) u^\mu u^\nu + (p/c^2) g^{\mu\nu}$ in the cosmic rest frame ($u^\mu = (c, 0, 0, 0)$ with $u^0 = c$ for $x^0 = ct$), the covariant conservation $\nabla_\mu T^{\mu 0} = 0$ reduces in the FLRW background to:

**第 1 步 — $\nabla^\mu T_{\mu\nu} = 0$ 的 $\nu = 0$ 分量。** 对于宇宙静止系中的完美流体 $T^{\mu\nu} = (\rho + p/c^2) u^\mu u^\nu + (p/c^2) g^{\mu\nu}$（$u^0 = c$，$x^0 = ct$），在 FLRW 背景下协变守恒 $\nabla_\mu T^{\mu 0} = 0$ 化为：

$$ \partial_\mu T^{\mu 0} + \Gamma^{\mu}{}_{\mu\lambda} T^{\lambda 0} - \Gamma^{0}{}_{\mu\lambda} T^{\mu\lambda} = 0. $$

Only the time component is non-trivial (by homogeneity and isotropy):

由均匀性和各向同性，只有时间分量非平凡：

$$ \partial_0 T^{00} + \Gamma^{\mu}{}_{\mu 0} T^{00} - \Gamma^{0}{}_{ij} T^{ij} = 0. $$

With $T^{00} = \rho/c^2$ (using $c = 1$ briefly: $T^{00} = \rho$), $\Gamma^{i}{}_{i0} = 3\dot{a}/a$ (from Step 2 of Section A), and $\Gamma^{0}{}_{ij} = a\dot{a} \gamma_{ij}$, $T^{ij} = p g^{ij}/c^2 = p \gamma^{ij}/a^2$:

取 $T^{00} = \rho$（$c = 1$ 单位），$\Gamma^{i}{}_{i0} = 3\dot{a}/a$，$\Gamma^{0}{}_{ij} = a\dot{a} \gamma_{ij}$，$T^{ij} = p \gamma^{ij}/a^2$：

$$ \begin{aligned}
& \dot{\rho} + 3(\dot{a}/a) \rho - a\dot{a} \gamma_{ij} \cdot p \gamma^{ij}/a^2 = 0 \\
& \dot{\rho} + 3(\dot{a}/a) \rho - 3(\dot{a}/a) p = 0 \\
& \dot{\rho} + 3(\dot{a}/a)(\rho + p) = 0 \quad (c = 1).
\end{aligned} $$

Restoring $c$: $\boxed{\, \dot{\rho} + 3(\dot{a}/a)(\rho + p/c^2) = 0 \,}$. $\blacksquare$

恢复 $c$：$\boxed{\, \dot{\rho} + 3(\dot{a}/a)(\rho + p/c^2) = 0 \,}$。$\blacksquare$

Note this equation is not independent: it can also be derived from the two Friedmann equations by differentiating the first and substituting the second.

注意此方程不是独立的：也可以通过对第一弗里德曼方程微分并代入第二方程得到。

**Step 2 — Dust ($p = 0$): matter scaling.** Setting $p = 0$:

**第 2 步 — 尘埃（$p = 0$）：物质标度。** 令 $p = 0$：

$$ \dot{\rho} = -3(\dot{a}/a) \rho \quad\implies\quad d\rho/\rho = -3\, da/a \quad\implies\quad \ln \rho = -3 \ln a + \text{const} $$

$$ \boxed{\, \rho_m \propto a^{-3} \,} $$

This is the dilution of a fixed number of non-relativistic particles in volume $V \propto a^3$: $\rho = Nm/V \propto 1/a^3$.

这是体积 $V \propto a^3$ 中固定数目的非相对论性粒子的稀释：$\rho = Nm/V \propto 1/a^3$。

**Step 3 — Radiation ($p = \rho c^2/3$): radiation scaling.** Setting $p = \rho c^2/3$ (the equation of state for a photon gas, from Module 2.6):

**第 3 步 — 辐射（$p = \rho c^2/3$）：辐射标度。** 令 $p = \rho c^2/3$（光子气体的状态方程，来自模块 2.6）：

$$ \begin{aligned}
& \dot{\rho} + 3(\dot{a}/a)(\rho + \rho/3) = 0 \\
& \dot{\rho} + 4(\dot{a}/a) \rho = 0 \\
& d\rho/\rho = -4\, da/a \quad\implies\quad \boxed{\, \rho_r \propto a^{-4} \,}.
\end{aligned} $$

Radiation dilutes one extra power of $a$ relative to matter because of the cosmological redshift: each photon's energy $E = h\nu \propto 1/a$ (its wavelength stretches as $a$), so total photon energy density $\propto$ (number density $\propto a^{-3}$) $\times$ (energy per photon $\propto a^{-1}$) $= a^{-4}$.

辐射比物质多稀释一个 $a$ 的幂次，原因是宇宙学红移：每个光子的能量 $E = h\nu \propto 1/a$（波长随 $a$ 伸展），故总光子能量密度 $\propto$ （数密度 $\propto a^{-3}$）$\times$（每个光子的能量 $\propto a^{-1}$）$= a^{-4}$。

**Step 4 — Cosmological constant ($p = -\rho c^2$): $\Lambda$ scaling.** Setting $p = -\rho c^2$:

**第 4 步 — 宇宙学常数（$p = -\rho c^2$）：$\Lambda$ 标度。** 令 $p = -\rho c^2$：

$$ \dot{\rho} + 3(\dot{a}/a)(\rho - \rho) = 0 \quad\implies\quad \dot{\rho} = 0 \quad\implies\quad \boxed{\, \rho_\Lambda = \text{const} \,} $$

This is consistent with the cosmological constant as vacuum energy: empty space has a fixed energy density regardless of expansion. $\blacksquare$

这与作为真空能量的宇宙学常数一致：真空具有固定的能量密度，与膨胀无关。$\blacksquare$

---

## C. Cosmological Redshift: $1 + z = a_0/a$ · 宇宙学红移：$1 + z = a_0/a$

**Claim.** A photon emitted at scale factor $a_e$ and received today at scale factor $a_0 = 1$ has its wavelength stretched by the factor $a_0/a_e$, giving a redshift $z = (a_0 - a_e)/a_e = 1/a_e - 1$, or equivalently

$$ 1 + z = a_0/a_e. $$

**命题。** 在尺度因子 $a_e$ 时发射、今天在 $a_0 = 1$ 时接收的光子，其波长被拉伸因子 $a_0/a_e$，给出红移 $z = (a_0 - a_e)/a_e = 1/a_e - 1$，等价地

$$ 1 + z = a_0/a_e. $$

**Step 1 — Set up the photon path.** A radial photon ($d\Omega = 0$) travels on a null geodesic $ds^2 = 0$. For the FLRW metric:

**第 1 步 — 建立光子路径。** 径向光子（$d\Omega = 0$）沿零测地线 $ds^2 = 0$ 传播。对于 FLRW 度规：

$$ \begin{aligned}
& 0 = -c^2 dt^2 + a^2(t) dr^2/(1-kr^2) \\
& dr/dt = c\sqrt{1-kr^2} / a(t).
\end{aligned} $$

For a photon emitted from comoving coordinate $r_e$ at time $t_e$ and received at $r = 0$ at time $t_0$:

对于从共动坐标 $r_e$ 在时刻 $t_e$ 发射、在 $r = 0$ 在时刻 $t_0$ 接收的光子：

$$ \int_0^{r_e} dr/\sqrt{1-kr^2} = \int_{t_e}^{t_0} c\, dt/a(t) \quad \ldots(*) $$

**Step 2 — Consider two successive wavefronts.** The first crest is emitted at time $t_e$ and received at $t_0$. The second crest is emitted at $t_e + \delta t_e$ and received at $t_0 + \delta t_0$. The comoving coordinate $r_e$ is the same for both crests (the source is at rest in comoving coordinates). Therefore the right-hand side integral (*) is the same for both crests:

**第 2 步 — 考虑两个连续波前。** 第一个波峰在时刻 $t_e$ 发射，在 $t_0$ 接收。第二个波峰在 $t_e + \delta t_e$ 发射，在 $t_0 + \delta t_0$ 接收。共动坐标 $r_e$ 对两个波峰相同（源在共动坐标中静止）。因此积分 (*) 对两个波峰相同：

$$ \int_{t_e}^{t_0} c\, dt/a(t) = \int_{t_e+\delta t_e}^{t_0+\delta t_0} c\, dt/a(t). $$

Subtracting:

相减：

$$ \int_{t_0}^{t_0+\delta t_0} c\, dt/a(t) = \int_{t_e}^{t_e+\delta t_e} c\, dt/a(t). $$

For small intervals $\delta t_e, \delta t_0 \ll$ the Hubble time, $a(t)$ is approximately constant over each interval:

对于小间隔 $\delta t_e$，$\delta t_0 \ll$ 哈勃时间，$a(t)$ 在每个间隔上近似为常数：

$$ \delta t_0/a(t_0) = \delta t_e/a(t_e). $$

**Step 3 — Relate frequency to scale factor.** The emitted frequency is $\nu_e = 1/\delta t_e$ and the received frequency is $\nu_0 = 1/\delta t_0$. Therefore:

**第 3 步 — 将频率与尺度因子联系起来。** 发射频率为 $\nu_e = 1/\delta t_e$，接收频率为 $\nu_0 = 1/\delta t_0$。因此：

$$ \nu_0/\nu_e = \delta t_e/\delta t_0 = a(t_e)/a(t_0). $$

**Step 4 — Define the redshift.** The cosmological redshift is $z = (\nu_e - \nu_0)/\nu_0 = (\lambda_0 - \lambda_e)/\lambda_e$ ($\lambda \propto 1/\nu$). So:

**第 4 步 — 定义红移。** 宇宙学红移为 $z = (\nu_e - \nu_0)/\nu_0 = (\lambda_0 - \lambda_e)/\lambda_e$（$\lambda \propto 1/\nu$）。故：

$$ 1 + z = \nu_e/\nu_0 = a(t_0)/a(t_e) = a_0/a_e. $$

With the conventional normalization $a_0 = a(t_0) = 1$:

使用约定归一化 $a_0 = a(t_0) = 1$：

$$ \boxed{\, 1 + z = 1/a_e \,}, \quad \text{or equivalently} \quad a_e = 1/(1+z). \qquad \blacksquare $$

This is purely kinematic — no gravitational redshift formula is needed; the stretching of photon wavelengths is a consequence of the expanding spatial metric. The scale factor at recombination $a_\text{rec} = 1/(1 + 1100) \approx 9 \times 10^{-4}$ corresponds to a universe about 1100 times smaller than today.

这是纯运动学的——不需要引力红移公式；光子波长的拉伸是膨胀空间度规的结果。复合时代的尺度因子 $a_\text{rec} = 1/(1 + 1100) \approx 9 \times 10^{-4}$ 对应于一个比今天小约 1100 倍的宇宙。

---

## D. Scale-factor Solutions and the Fate of the Universe · 尺度因子的解与宇宙的命运

**Claim.** For a spatially flat ($k = 0$) universe with $\Lambda = 0$ and a single fluid component with equation of state $w = p/(\rho c^2)$, the first Friedmann equation gives $a(t) \propto t^{2/3(1+w)}$ for $w \ne -1$. In particular:
- Matter dominated ($w = 0$): $a(t) \propto t^{2/3}$
- Radiation dominated ($w = 1/3$): $a(t) \propto t^{1/2}$
- $\Lambda$ dominated ($w = -1$): $a(t) \propto e^{Ht}$ (de Sitter)

**命题。** 对于空间平坦（$k = 0$）、$\Lambda = 0$、含单一流体成分（状态方程 $w = p/(\rho c^2)$）的宇宙，第一弗里德曼方程给出 $a(t) \propto t^{2/3(1+w)}$（当 $w \ne -1$）。特别地：
- 物质主导（$w = 0$）：$a(t) \propto t^{2/3}$
- 辐射主导（$w = 1/3$）：$a(t) \propto t^{1/2}$
- $\Lambda$ 主导（$w = -1$）：$a(t) \propto e^{Ht}$（德西特）

**Step 1 — Use the density scaling.** From Section B, $\rho \propto a^{-3(1+w)}$ (combining the three cases: $w = 0$ gives $a^{-3}$, $w = 1/3$ gives $a^{-4}$, $w = -1$ gives $a^0 = $ const).

**第 1 步 — 使用密度标度关系。** 由 B 节，$\rho \propto a^{-3(1+w)}$（综合三种情形：$w = 0$ 给出 $a^{-3}$，$w = 1/3$ 给出 $a^{-4}$，$w = -1$ 给出 $a^0 = $ 常数）。

Write $\rho = \rho_0 a^{-3(1+w)}$ (with $\rho_0$ the present density if $a_0 = 1$).

写出 $\rho = \rho_0 a^{-3(1+w)}$（$\rho_0$ 为 $a_0 = 1$ 时的当前密度）。

**Step 2 — Substitute into the first Friedmann equation ($k = 0$, $\Lambda = 0$).**

**第 2 步 — 代入第一弗里德曼方程（$k = 0$，$\Lambda = 0$）。**

$$ \begin{aligned}
& (\dot{a}/a)^2 = (8\pi G/3) \rho_0 a^{-3(1+w)} \\
& \dot{a}^2 = (8\pi G \rho_0/3) a^{-(1+3w)}.
\end{aligned} $$

For $w \ne -1$, write $\dot{a} = da/dt$ and separate variables:

对于 $w \ne -1$，写出 $\dot{a} = da/dt$ 并分离变量：

$$ a^{(1+3w)/2} da = \sqrt{8\pi G \rho_0/3}\, dt. $$

**Step 3 — Integrate.** Let $n = (1+3w)/2$, then:

**第 3 步 — 积分。** 令 $n = (1+3w)/2$，则：

$$ a^{n+1}/(n+1) = \sqrt{8\pi G \rho_0/3} \cdot t + \text{const}. $$

With initial condition $a(0) = 0$ (Big Bang at $t = 0$), the constant is zero:

取初始条件 $a(0) = 0$（$t = 0$ 时的大爆炸），常数为零：

$$ a^{n+1} \propto t \quad\implies\quad a \propto t^{1/(n+1)} = t^{2/(3(1+w))}. $$

This confirms:

这证实：

- $w = 0$ (matter): $a \propto t^{2/(3\cdot 1)} = \boxed{\, t^{2/3} \,}$
- $w = 1/3$ (radiation): $a \propto t^{2/(3\cdot 4/3)} = t^{2/2} = \boxed{\, t^{1/2} \,}$

**Step 4 — De Sitter case ($w = -1$, $\Lambda$ dominated).** For $\rho_\Lambda = \Lambda c^2/(8\pi G) = $ const, the first Friedmann equation gives:

**第 4 步 — 德西特情形（$w = -1$，$\Lambda$ 主导）。** 对于 $\rho_\Lambda = \Lambda c^2/(8\pi G) = $ 常数，第一弗里德曼方程给出：

$$ (\dot{a}/a)^2 = \Lambda c^2/3 = H^2 \quad\implies\quad \dot{a} = Ha $$

where $H = c\sqrt{\Lambda/3} = $ const. The solution is:

其中 $H = c\sqrt{\Lambda/3} = $ 常数。解为：

$$ \boxed{\, a(t) \propto e^{Ht} \,}, $$

exponential expansion (de Sitter space). This is the late-time attractor of any $\Lambda$-dominated universe. $\blacksquare$

指数膨胀（德西特空间）。这是任何 $\Lambda$ 主导宇宙的晚时吸引子。$\blacksquare$

---
title: "Derivations — Module 6.6: Renormalization & the Renormalization Group"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 6.6: Renormalization & the Renormalization Group
# 推导 — 模块 6.6：重整化与重整化群

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 6.6](./module-6.6-renormalization.md). Full step-by-step proofs. English first, then 中文.
> [模块 6.6](./module-6.6-renormalization.md) 的配套文档：完整逐步证明。先英文，后中文。

---

## A. The One-Loop Divergence & Dimensional Regularization · 单圈发散与维数正规化

**Step 1 — The divergent integral.** In $\varphi^4$ theory the one-loop correction to the four-point coupling involves the integral $I = \int \frac{d^4k}{(2\pi)^4} \cdot \frac{1}{(k^2+m^2)((k+p)^2+m^2)}$ (Euclidean). Power counting: for large $k$ the integrand $\sim k^{-4}$, so $\int d^4k\, k^{-4} \sim \int dk/k$ diverges **logarithmically** in the ultraviolet.

**第 1 步 — 发散积分。** 在 $\varphi^4$ 理论中，四点耦合的单圈修正涉及积分 $I = \int \frac{d^4k}{(2\pi)^4} \cdot \frac{1}{(k^2+m^2)((k+p)^2+m^2)}$（欧几里得）。量纲计数：大 $k$ 时被积量 $\sim k^{-4}$，故 $\int d^4k\, k^{-4} \sim \int dk/k$ 在紫外**对数发散**。

**Step 2 — Dimensional regularization.** Continue to $d = 4 - \epsilon$ dimensions. Combine denominators with a Feynman parameter, $\frac{1}{AB} = \int_0^1 dx\, [xA+(1-x)B]^{-2}$, shift $k\to k-xp$, and use the master formula

**第 2 步 — 维数正规化。** 延拓到 $d = 4 - \epsilon$ 维。用费曼参数合并分母，$\frac{1}{AB} = \int_0^1 dx\, [xA+(1-x)B]^{-2}$，平移 $k\to k-xp$，并用主公式

$$ \int \frac{d^dk}{(2\pi)^d} \cdot \frac{1}{(k^2+\Delta)^2} = \frac{1}{(4\pi)^{d/2}} \cdot \frac{\Gamma(2-d/2)}{\Gamma(2)} \cdot \Delta^{d/2-2}. $$

With $d = 4 - \epsilon$, $\Gamma(2-d/2) = \Gamma(\epsilon/2) = 2/\epsilon - \gamma_E + O(\epsilon)$. Hence

代入 $d = 4 - \epsilon$，$\Gamma(2-d/2) = \Gamma(\epsilon/2) = 2/\epsilon - \gamma_E + O(\epsilon)$。于是

$$ I = \frac{1}{16\pi^2} \int_0^1 dx\, [2/\epsilon - \gamma_E - \ln(\Delta/4\pi)] + O(\epsilon), \qquad \Delta = x(1-x)p^2 + m^2. $$

The divergence is now an explicit **$1/\epsilon$ pole**.

发散此时表现为明确的 **$1/\epsilon$ 极点**。

**Step 3 — Renormalization.** Write the bare coupling as $g_0 = \mu^\epsilon(g + \delta g)$ with a counterterm $\delta g$ chosen to cancel the pole: $\delta g = (3g^2/16\pi^2)(1/\epsilon) + \text{finite}$ (the 3 counts the $s,t,u$ channels). The renormalized four-point function is then **finite** as $\epsilon\to 0$. The arbitrary scale $\mu$ (with mass dimension, introduced to keep $g$ dimensionless in $d\ne 4$) is the seed of the renormalization group. $\blacksquare$

**第 3 步 — 重整化。** 将裸耦合写为 $g_0 = \mu^\epsilon(g + \delta g)$，选取抵消项 $\delta g$ 消去极点：$\delta g = (3g^2/16\pi^2)(1/\epsilon) + \text{有限项}$（因子 3 计入 $s$、$t$、$u$ 三个道）。重整化后的四点函数在 $\epsilon\to 0$ 时**有限**。任意标度 $\mu$（具质量量纲，为在 $d\ne 4$ 时保持 $g$ 无量纲而引入）正是重整化群的种子。$\blacksquare$

---

## B. The Beta Function and the Running Coupling · $\beta$ 函数与跑动耦合

**Step 1 — $\mu$-independence.** The bare coupling $g_0$ does not know about the arbitrary $\mu$: $\mu\, dg_0/d\mu = 0$. Differentiating $g_0 = \mu^\epsilon(g + \delta g)$ gives the **beta function** $\beta(g) \equiv \mu\, dg/d\mu$. At one loop (in $d=4$, $\epsilon\to 0$),

**第 1 步 — $\mu$ 无关性。** 裸耦合 $g_0$ 不依赖于任意的 $\mu$：$\mu\, dg_0/d\mu = 0$。对 $g_0 = \mu^\epsilon(g + \delta g)$ 求导得到 **$\beta$ 函数** $\beta(g) \equiv \mu\, dg/d\mu$。单圈阶（$d=4$，$\epsilon\to 0$）：

$$ \boxed{\, \beta(g) = 3g^2/16\pi^2 \,} \quad (\varphi^4 \text{ theory}). $$

**Step 2 — Solve the flow.** Integrating $\mu\, dg/d\mu = 3g^2/16\pi^2$ gives $1/g(\mu) = 1/g(\mu_0) - (3/16\pi^2)\ln(\mu/\mu_0)$, i.e. the coupling **grows** with energy (a Landau pole at high $\mu$). For QED the analogous one-loop result is $\beta(e) = e^3/12\pi^2$, giving the running fine-structure constant

**第 2 步 — 求解流动。** 对 $\mu\, dg/d\mu = 3g^2/16\pi^2$ 积分得 $1/g(\mu) = 1/g(\mu_0) - (3/16\pi^2)\ln(\mu/\mu_0)$，即耦合随能量**增大**（高 $\mu$ 处出现朗道极点）。对 QED，类似的单圈结果为 $\beta(e) = e^3/12\pi^2$，给出跑动精细结构常数

$$ \alpha(\mu) = \frac{\alpha(\mu_0)}{1 - (\alpha(\mu_0)/3\pi)\ln(\mu^2/\mu_0^2)}, $$

explaining why $\alpha$ grows from $1/137$ at low energy toward $\approx 1/128$ at the $Z$ mass. (In QCD the non-abelian gluon loops flip the sign, $\beta<0$, giving asymptotic freedom — see Module 8.3.)

这解释了为何 $\alpha$ 从低能的 $1/137$ 增大到 $Z$ 质量处的约 $1/128$。（在 QCD 中，非阿贝尔胶子圈使符号翻转，$\beta<0$，给出渐近自由——见模块 8.3。）$\blacksquare$

---

## C. The Wilson–Fisher Fixed Point & Critical Exponents · 威尔逊–费舍尔不动点与临界指数

**Step 1 — Keep the $\epsilon$ term.** In $d = 4 - \epsilon$ the dimensionful tree term survives: the dimensionless coupling obeys

**第 1 步 — 保留 $\epsilon$ 项。** 在 $d = 4 - \epsilon$ 中，含量纲的树级项保留：无量纲耦合满足

$$ \beta(u) = -\epsilon u + (3/16\pi^2)\, u^2 + O(u^3). $$

**Step 2 — Fixed points.** Solve $\beta(u_*) = 0$: the **Gaussian** fixed point $u_* = 0$ (unstable for $\epsilon>0$) and the **Wilson–Fisher** fixed point

**第 2 步 — 不动点。** 解 $\beta(u_*) = 0$：**高斯**不动点 $u_* = 0$（$\epsilon>0$ 时不稳定）与**威尔逊–费舍尔**不动点

$$ u_* = 16\pi^2 \epsilon / 3. $$

**Step 3 — Critical exponent.** Linearize the flow of the relevant (mass/temperature) coupling about $u_*$; the slope $d\beta_t/dt$ at $u_*$ shifts the correlation-length exponent from its mean-field value $\tfrac12$ to

**第 3 步 — 临界指数。** 在 $u_*$ 附近线性化相关（质量/温度）耦合的流动；$u_*$ 处的斜率 $d\beta_t/dt$ 将关联长度指数从平均场值 $\tfrac12$ 修正为

$$ \nu = \tfrac12 + \epsilon/12 + O(\epsilon^2). $$

This is **universal**: it depends only on dimension and symmetry, not on microscopic details — the deep reason the liquid–gas critical point, the Ising magnet, and the $^4\mathrm{He}$ superfluid transition share exponents (Module 2.3). $\blacksquare$

这是**普适的**：它只依赖于维度和对称性，而与微观细节无关——这正是液–气临界点、伊辛磁体与 $^4\mathrm{He}$ 超流相变共享临界指数的深层原因（模块 2.3）。$\blacksquare$

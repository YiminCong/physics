# Derivations — Module 1.1: Newtonian Mechanics
# 推导 — 模块 1.1：牛顿力学

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.1](./module-1.1-newtonian-mechanics.md). Full step-by-step proofs of every result quoted there. English first, then 中文.
> [模块 1.1](./module-1.1-newtonian-mechanics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Work–Energy Theorem · 功能定理

**Claim.** For a particle of mass $m$ moving under a net force $\mathbf{F}$, the net work done along any path equals the change in kinetic energy: $\int \mathbf{F} \cdot d\mathbf{x} = \Delta T = T_f - T_i$.

**命题。** 对于质量为 $m$ 的粒子在合力 $\mathbf{F}$ 作用下运动，沿任意路径所做的净功等于动能的变化：$\int \mathbf{F} \cdot d\mathbf{x} = \Delta T = T_f - T_i$。

**Step 1 — Start from Newton's second law.** Newton's second law in vector form is

**第 1 步 — 从牛顿第二定律出发。** 向量形式的牛顿第二定律为

$$ \mathbf{F} = m\,\frac{d\mathbf{v}}{dt}. $$

**Step 2 — Multiply both sides by $\mathbf{v}$ and use the chain rule.** Take the dot product of both sides with the velocity $\mathbf{v} = d\mathbf{x}/dt$:

**第 2 步 — 两边乘以 $\mathbf{v}$，并利用链式法则。** 对两边与速度 $\mathbf{v} = d\mathbf{x}/dt$ 取点积：

$$ \mathbf{F} \cdot \mathbf{v} = m\,\frac{d\mathbf{v}}{dt} \cdot \mathbf{v} = m \cdot \tfrac12\,\frac{d(\mathbf{v} \cdot \mathbf{v})}{dt} = \frac{d}{dt}\Big(\tfrac12 m v^2\Big). $$

The identity $(d\mathbf{v}/dt) \cdot \mathbf{v} = \tfrac12\, d(|\mathbf{v}|^2)/dt$ follows from the product rule for differentiation.

恒等式 $(d\mathbf{v}/dt) \cdot \mathbf{v} = \tfrac12\, d(|\mathbf{v}|^2)/dt$ 由微分的乘积法则得出。

**Step 3 — Express in terms of path element.** Since $\mathbf{v} = d\mathbf{x}/dt$, we have $\mathbf{F} \cdot \mathbf{v}\, dt = \mathbf{F} \cdot d\mathbf{x}$. Integrate both sides from time $t_i$ to $t_f$, which corresponds to the path from $\mathbf{x}_i$ to $\mathbf{x}_f$:

**第 3 步 — 用路径元表示。** 由于 $\mathbf{v} = d\mathbf{x}/dt$，有 $\mathbf{F} \cdot \mathbf{v}\, dt = \mathbf{F} \cdot d\mathbf{x}$。对两边从时刻 $t_i$ 到 $t_f$ 积分，对应路径从 $\mathbf{x}_i$ 到 $\mathbf{x}_f$：

$$ \int_{t_i}^{t_f} \mathbf{F} \cdot \mathbf{v}\, dt = \int_{t_i}^{t_f} \frac{d}{dt}\Big(\tfrac12 m v^2\Big)\, dt. $$

**Step 4 — Evaluate the right side.** The right-hand side is a total time derivative, so it integrates immediately:

**第 4 步 — 计算右侧。** 右侧是全时间导数，可直接积分：

$$ \int_{t_i}^{t_f} \frac{d}{dt}\Big(\tfrac12 m v^2\Big)\, dt = \tfrac12 m v_f^2 - \tfrac12 m v_i^2 = T_f - T_i = \Delta T. $$

**Step 5 — Identify the left side as work.** By the definition $W = \int \mathbf{F} \cdot d\mathbf{x}$ (work done by force $\mathbf{F}$ along the path), the left side is precisely the net work $W_\text{net}$. Therefore:

**第 5 步 — 识别左侧为功。** 按照定义 $W = \int \mathbf{F} \cdot d\mathbf{x}$（力 $\mathbf{F}$ 沿路径所做的功），左侧正是净功 $W_\text{net}$。因此：

$$ \boxed{\, W_\text{net} = \int \mathbf{F} \cdot d\mathbf{x} = \Delta T \,} \qquad \blacksquare $$

---

## B. Conservation of Momentum for an Isolated System · 孤立系统的动量守恒

**Claim.** For a system of two particles with no net external force, the total linear momentum $\mathbf{P} = \mathbf{p}_1 + \mathbf{p}_2$ is conserved: $d\mathbf{P}/dt = 0$.

**命题。** 对于无净外力的两粒子系统，总线动量 $\mathbf{P} = \mathbf{p}_1 + \mathbf{p}_2$ 守恒：$d\mathbf{P}/dt = 0$。

**Step 1 — Write Newton's second law for each particle.** Let particle 1 experience force $\mathbf{F}_{12}$ from particle 2, plus any external force $\mathbf{F}_1^\text{ext}$. Similarly, particle 2 experiences $\mathbf{F}_{21}$ from particle 1 plus $\mathbf{F}_2^\text{ext}$. Newton's second law gives:

**第 1 步 — 对每个粒子写出牛顿第二定律。** 设粒子 1 受到来自粒子 2 的力 $\mathbf{F}_{12}$ 及外力 $\mathbf{F}_1^\text{ext}$。类似地，粒子 2 受到来自粒子 1 的力 $\mathbf{F}_{21}$ 及外力 $\mathbf{F}_2^\text{ext}$。牛顿第二定律给出：

$$ \frac{d\mathbf{p}_1}{dt} = \mathbf{F}_{12} + \mathbf{F}_1^\text{ext}, \qquad \frac{d\mathbf{p}_2}{dt} = \mathbf{F}_{21} + \mathbf{F}_2^\text{ext}. $$

**Step 2 — Add the two equations.** Summing:

**第 2 步 — 将两个方程相加。** 求和：

$$ \frac{d\mathbf{P}}{dt} = \frac{d(\mathbf{p}_1 + \mathbf{p}_2)}{dt} = (\mathbf{F}_{12} + \mathbf{F}_{21}) + (\mathbf{F}_1^\text{ext} + \mathbf{F}_2^\text{ext}). $$

**Step 3 — Apply Newton's third law.** Newton's third law states that the internal forces between the two particles are equal and opposite:

**第 3 步 — 应用牛顿第三定律。** 牛顿第三定律指出，两粒子间的内力等大反向：

$$ \mathbf{F}_{12} = -\mathbf{F}_{21} \quad\implies\quad \mathbf{F}_{12} + \mathbf{F}_{21} = 0. $$

**Step 4 — Apply the isolated-system condition.** For an isolated system, there are no external forces:

**第 4 步 — 应用孤立系统条件。** 对于孤立系统，无外力：

$$ \mathbf{F}_1^\text{ext} + \mathbf{F}_2^\text{ext} = 0. $$

**Step 5 — Conclude conservation.** Substituting Steps 3 and 4 into the result of Step 2:

**第 5 步 — 得出守恒结论。** 将第 3、4 步代入第 2 步的结果：

$$ \frac{d\mathbf{P}}{dt} = 0 \quad\implies\quad \boxed{\, \mathbf{P} = \mathbf{p}_1 + \mathbf{p}_2 = \text{const} \,} \qquad \blacksquare $$

The argument extends directly to $N$ particles: the double sum $\sum\sum \mathbf{F}_{ij}$ vanishes by Newton's third law (each pair cancels), leaving only external forces.

该论证直接推广到 $N$ 个粒子：双重求和 $\sum\sum \mathbf{F}_{ij}$ 由牛顿第三定律消去（每对内力相消），仅剩外力。

---

## C. Projectile Motion — Solving the Newton EOM · 抛体运动——求解牛顿运动方程

**Claim.** A projectile launched from the origin with speed $v_0$ at angle $\theta$ above horizontal follows $x(t) = v_0 \cos\theta \cdot t$, $y(t) = v_0 \sin\theta \cdot t - \tfrac12 g t^2$, and has horizontal range $R = v_0^2 \sin 2\theta / g$ maximised at $\theta = 45^\circ$.

**命题。** 以速度 $v_0$、仰角 $\theta$ 从原点发射的抛体遵循 $x(t) = v_0 \cos\theta \cdot t$，$y(t) = v_0 \sin\theta \cdot t - \tfrac12 g t^2$，水平射程 $R = v_0^2 \sin 2\theta / g$ 在 $\theta = 45^\circ$ 时最大。

**Step 1 — Identify the forces and set up the EOM.** Near Earth's surface the only force is gravity, $\mathbf{F} = (0, -mg)$. Newton's second law $\mathbf{F} = m\mathbf{a}$ gives two component equations:

**第 1 步 — 辨识力并建立运动方程。** 在地球表面附近唯一的力是重力，$\mathbf{F} = (0, -mg)$。牛顿第二定律 $\mathbf{F} = m\mathbf{a}$ 给出两个分量方程：

$$ m\ddot{x} = 0 \quad (x\text{-direction / } x\text{ 方向}), \qquad m\ddot{y} = -mg \quad (y\text{-direction / } y\text{ 方向}). $$

**Step 2 — First integration (velocities).** Divide by $m$ and integrate once with respect to $t$. Using initial conditions $\dot{x}(0) = v_0 \cos\theta$ and $\dot{y}(0) = v_0 \sin\theta$:

**第 2 步 — 第一次积分（速度）。** 除以 $m$ 并对 $t$ 积分一次。利用初始条件 $\dot{x}(0) = v_0 \cos\theta$ 和 $\dot{y}(0) = v_0 \sin\theta$：

$$ \dot{x}(t) = v_0 \cos\theta, \qquad \dot{y}(t) = v_0 \sin\theta - g t. $$

**Step 3 — Second integration (positions).** Integrate once more, using $x(0) = y(0) = 0$:

**第 3 步 — 第二次积分（位置）。** 再次积分，利用 $x(0) = y(0) = 0$：

$$ x(t) = v_0 \cos\theta \cdot t, \qquad y(t) = v_0 \sin\theta \cdot t - \tfrac12 g t^2. $$

**Step 4 — Find the time of flight.** The projectile returns to $y = 0$ when $v_0 \sin\theta \cdot t - \tfrac12 g t^2 = t(v_0 \sin\theta - \tfrac12 g t) = 0$. The non-trivial solution is $t_f = 2 v_0 \sin\theta / g$.

**第 4 步 — 求飞行时间。** 抛体回到 $y = 0$ 时，$v_0 \sin\theta \cdot t - \tfrac12 g t^2 = t(v_0 \sin\theta - \tfrac12 g t) = 0$。非平凡解为 $t_f = 2 v_0 \sin\theta / g$。

**Step 5 — Compute the range.** Substituting $t_f$ into $x(t)$:

**第 5 步 — 计算射程。** 将 $t_f$ 代入 $x(t)$：

$$ R = x(t_f) = v_0 \cos\theta \cdot \frac{2 v_0 \sin\theta}{g} = \frac{v_0^2 \cdot 2 \sin\theta \cos\theta}{g} = \boxed{\,\frac{v_0^2 \sin 2\theta}{g}\,}. $$

**Step 6 — Maximise over $\theta$.** Since $\sin 2\theta$ is maximised when $2\theta = 90^\circ$, i.e. $\theta = 45^\circ$, the maximum range is $R_\text{max} = v_0^2/g$. $\blacksquare$

**第 6 步 — 对 $\theta$ 求最大值。** 由于 $\sin 2\theta$ 在 $2\theta = 90^\circ$ 即 $\theta = 45^\circ$ 时最大，最大射程为 $R_\text{max} = v_0^2/g$。$\blacksquare$

---

## D. Atwood Machine — Eliminating Constraint Forces · 阿特伍德机——消去约束力

**Claim.** For an Atwood machine with masses $m$ (on the table) and $M$ (hanging), connected by an inextensible string over a frictionless pulley, the acceleration is $a = Mg/(m + M)$.

**命题。** 对于由质量 $m$（在桌面上）和 $M$（悬挂）通过无摩擦滑轮上不可伸长绳子相连的阿特伍德机，加速度为 $a = Mg/(m + M)$。

**Step 1 — Identify the constraint.** The string is inextensible, so both masses share the same magnitude of acceleration $a$. Let $T$ be the tension in the string.

**第 1 步 — 辨识约束。** 绳子不可伸长，故两质量具有相同大小的加速度 $a$。设绳中张力为 $T$。

**Step 2 — Apply Newton's second law to $M$ (hanging mass).** Taking downward as positive:

**第 2 步 — 对 $M$（悬挂质量）应用牛顿第二定律。** 取向下为正方向：

$$ Mg - T = Ma. $$

**Step 3 — Apply Newton's second law to $m$ (table mass).** Taking the direction of motion as positive:

**第 3 步 — 对 $m$（桌面质量）应用牛顿第二定律。** 取运动方向为正方向：

$$ T = ma. $$

**Step 4 — Eliminate $T$ by addition.** Adding the two equations:

**第 4 步 — 相加消去 $T$。** 两方程相加：

$$ Mg = (m + M)\, a \quad\implies\quad \boxed{\, a = \frac{Mg}{m + M} \,} \qquad \blacksquare $$

**Step 5 — Find $T$ (verification).** From Step 3: $T = ma = mMg/(m + M)$, which lies between $0$ and $Mg$, as expected physically.

**第 5 步 — 求 $T$（验证）。** 由第 3 步：$T = ma = mMg/(m + M)$，该值在 $0$ 与 $Mg$ 之间，符合物理预期。$\blacksquare$

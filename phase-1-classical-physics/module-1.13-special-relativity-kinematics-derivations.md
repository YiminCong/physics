# Derivations — Module 1.13: Special Relativity — Kinematics
# 推导 — 模块 1.13：狭义相对论——运动学

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.13](./module-1.13-special-relativity-kinematics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.13](./module-1.13-special-relativity-kinematics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Deriving the Lorentz Transformation from the Two Postulates · 从两个假设推导洛伦兹变换

**Claim.** From (1) the principle of relativity and (2) the constancy of $c$, together with the requirement of linearity (homogeneous flat spacetime), the unique coordinate transformation between two inertial frames $S$ and $S'$ (with $S'$ moving at velocity $v$ along the $x$-axis) is the Lorentz transformation:

**命题。** 从 (1) 相对性原理和 (2) 光速不变性，加上线性要求（均匀平直时空），两个惯性系 $S$ 和 $S'$（$S'$ 沿 $x$ 轴以速度 $v$ 运动）之间的唯一坐标变换是洛伦兹变换：

$$ x' = \gamma(x - vt), \quad t' = \gamma(t - vx/c^2), \quad y' = y, \quad z' = z, \quad \gamma = 1/\sqrt{1 - v^2/c^2}. $$

**Step 1 — Linearity and the form of the transformation.** The principle of relativity requires that the transformation be linear (straight worldlines in one frame must appear straight in all frames; nonlinear transformations would imply a preferred point in spacetime). For motion along $x$, the transverse coordinates are unaffected by symmetry ($y' = y$, $z' = z$ — if they were not equal, we could distinguish "moving left" from "moving right" by the sign of the transverse change, violating isotropy). The most general linear transformation is:

**第 1 步 — 线性与变换形式。** 相对性原理要求变换是线性的（一个参考系中的直世界线在所有参考系中必须显示为直线；非线性变换意味着时空中存在特殊点）。对于沿 $x$ 方向的运动，横向坐标由对称性不受影响（$y' = y$，$z' = z$——若不相等，我们可以通过横向变化的符号区分"向左运动"与"向右运动"，违反各向同性）。最一般的线性变换为：

$$ x' = A(x - vt), \qquad t' = B t + C x, $$

for constants $A, B, C$ to be determined. (The form $x' = A(x - vt)$ ensures that the origin of $S'$ ($x' = 0$) moves at velocity $v$ in $S$, as required.)

待定常数 $A$、$B$、$C$。（形式 $x' = A(x - vt)$ 确保 $S'$ 的原点（$x' = 0$）在 $S$ 中以速度 $v$ 运动，符合要求。）

**Step 2 — Apply the constancy of $c$.** A light pulse emitted at the origin at $t = 0$ propagates as $x = ct$ in $S$, and as $x' = ct'$ in $S'$ (the speed of light is the same in both frames). Substituting into our ansatz:

**第 2 步 — 应用光速不变性。** 在 $t = 0$ 时从原点发出的光脉冲，在 $S$ 中传播为 $x = ct$，在 $S'$ 中传播为 $x' = ct'$（光速在两个参考系中相同）。代入我们的假设：

$$ x' = A(ct - vt) = A(c - v)t, \qquad t' = Bt + C(ct) = (B + Cc)t. $$

For $x' = ct'$:  $A(c - v)t = c(B + Cc)t$, so:

为使 $x' = ct'$：$A(c - v)t = c(B + Cc)t$，故：

$$ A(c - v) = c(B + Cc). \qquad (*) $$

Now apply the same condition for a pulse in the $-x$ direction: $x = -ct$, $x' = -ct'$. Substituting:

现在对 $-x$ 方向的光脉冲应用相同条件：$x = -ct$，$x' = -ct'$。代入：

$$ x' = A(-ct - vt) = -A(c + v)t, \qquad t' = Bt + C(-ct) = (B - Cc)t. $$

For $x' = -ct'$:  $-A(c + v)t = -c(B - Cc)t$, so:

为使 $x' = -ct'$：$-A(c + v)t = -c(B - Cc)t$，故：

$$ A(c + v) = c(B - Cc). \qquad (**) $$

**Step 3 — Solve for $B, C$ in terms of $A$.** Adding $(*)$ and $(**)$:

**第 3 步 — 用 $A$ 解出 $B$、$C$。** 将 $(*)$ 和 $(**)$ 相加：

$$ 2Ac = 2Bc \quad\to\quad B = A. $$

Subtracting $(**)$ from $(*)$:

从 $(*)$ 中减去 $(**)$：

$$ -2Av = 2Cc^2 \quad\to\quad C = -Av/c^2. $$

So the transformation reads:

故变换变为：

$$ x' = A(x - vt), \qquad t' = A(t - vx/c^2). $$

**Step 4 — Determine $A$ from the inverse transformation.** By the principle of relativity, the inverse transformation (from $S'$ to $S$) must have the same form with $v \to -v$:

**第 4 步 — 由逆变换确定 $A$。** 由相对性原理，逆变换（从 $S'$ 到 $S$）必须具有相同形式，将 $v$ 替换为 $-v$：

$$ x = A(x' + vt'), \qquad t = A(t' + vx'/c^2). $$

Substitute $x'$ and $t'$ from Step 3 into the expression for $x$:

将第 3 步中的 $x'$ 和 $t'$ 代入 $x$ 的表达式：

$$ x = A[A(x - vt) + v A(t - vx/c^2)] = A^2[x - vt + vt - v^2 x/c^2] = A^2[x(1 - v^2/c^2)]. $$

For this to equal $x$ for all $x$, we need $A^2 (1 - v^2/c^2) = 1$, i.e.:

为使这对所有 $x$ 等于 $x$，需要 $A^2 (1 - v^2/c^2) = 1$，即：

$$ A = 1/\sqrt{1 - v^2/c^2} = \gamma. \qquad (\text{taking } A > 0 \text{ for the identity to recover at } v = 0) $$

（取 $A > 0$，使 $v = 0$ 时还原为恒等变换。）

**Step 5 — The Lorentz transformation.** Substituting $A = \gamma$:

**第 5 步 — 洛伦兹变换。** 代入 $A = \gamma$：

$$ \boxed{\, x' = \gamma(x - vt), \quad t' = \gamma(t - vx/c^2), \quad y' = y, \quad z' = z. \,} \qquad \blacksquare $$

When $v \ll c$, $\gamma \to 1$ and the transformation reduces to the Galilean $x' = x - vt$, $t' = t$, recovering Newtonian mechanics in the low-speed limit.

当 $v \ll c$ 时，$\gamma \to 1$，变换退化为伽利略变换 $x' = x - vt$，$t' = t$，在低速极限下恢复牛顿力学。

---

## B. Time Dilation · 时间膨胀

**Claim.** A clock at rest in $S'$ measures a proper time interval $\Delta\tau$ between two events at the same spatial position in $S'$. In frame $S$, the time interval is $\Delta t = \gamma\,\Delta\tau \ge \Delta\tau$.

**命题。** 静止在 $S'$ 中的时钟在 $S'$ 中同一空间位置的两个事件之间测量固有时间间隔 $\Delta\tau$。在参考系 $S$ 中，时间间隔为 $\Delta t = \gamma\,\Delta\tau \ge \Delta\tau$。

**Step 1 — Two events at the same place in $S'$.** Let two events occur at $x' = 0$ (the origin of $S'$, i.e., the location of the clock) at times $t'_1$ and $t'_2$. The proper time is $\Delta\tau = t'_2 - t'_1$.

**第 1 步 — $S'$ 中同一地点的两个事件。** 设两个事件发生在 $x' = 0$（$S'$ 的原点，即时钟所在处），时刻分别为 $t'_1$ 和 $t'_2$。固有时为 $\Delta\tau = t'_2 - t'_1$。

**Step 2 — Find the corresponding times in $S$.** Use the inverse Lorentz transformation $t = \gamma(t' + vx'/c^2)$. Since $x' = 0$:

**第 2 步 — 求 $S$ 中对应的时刻。** 利用逆洛伦兹变换 $t = \gamma(t' + vx'/c^2)$。由于 $x' = 0$：

$$ t_1 = \gamma t'_1, \qquad t_2 = \gamma t'_2. $$

Therefore: $\Delta t = t_2 - t_1 = \gamma(t'_2 - t'_1) = \gamma\,\Delta\tau$. Since $\gamma \ge 1$, $\Delta t \ge \Delta\tau$: moving clocks run slow. $\blacksquare$

因此：$\Delta t = t_2 - t_1 = \gamma(t'_2 - t'_1) = \gamma\,\Delta\tau$。由于 $\gamma \ge 1$，$\Delta t \ge \Delta\tau$：运动的时钟走得慢。$\blacksquare$

---

## C. Length Contraction · 长度收缩

**Claim.** A rod at rest in $S'$ has proper length $L_0$ ($= x'_2 - x'_1$ with the endpoints measured at the same $t'$). In frame $S$, the simultaneous measurement of the rod's endpoints gives length $L = L_0/\gamma \le L_0$.

**命题。** 静止在 $S'$ 中的杆具有固有长度 $L_0$（$= x'_2 - x'_1$，两端点在同一 $t'$ 时刻测量）。在参考系 $S$ 中，同时测量杆的两端点给出长度 $L = L_0/\gamma \le L_0$。

**Step 1 — Simultaneous measurement in $S$.** To measure the length of a moving rod in $S$, one must record the positions of both ends at the same time $t$ in $S$. Let the two endpoints be at $(x_1, t)$ and $(x_2, t)$ in $S$, so $L = x_2 - x_1$. The Lorentz transformation gives:

**第 1 步 — $S$ 中的同时测量。** 要在 $S$ 中测量运动杆的长度，必须在 $S$ 中同一时刻 $t$ 记录两端点的位置。设两端点在 $S$ 中分别为 $(x_1, t)$ 和 $(x_2, t)$，故 $L = x_2 - x_1$。洛伦兹变换给出：

$$ x'_1 = \gamma(x_1 - vt), \qquad x'_2 = \gamma(x_2 - vt). $$

Subtracting: $L_0 = x'_2 - x'_1 = \gamma(x_2 - x_1) = \gamma L$.

相减：$L_0 = x'_2 - x'_1 = \gamma(x_2 - x_1) = \gamma L$。

Therefore: $L = L_0/\gamma$. Since $\gamma \ge 1$, $L \le L_0$: moving rods contract along the direction of motion. $\blacksquare$

因此：$L = L_0/\gamma$。由于 $\gamma \ge 1$，$L \le L_0$：运动的杆沿运动方向收缩。$\blacksquare$

Note: Contraction only occurs along the direction of motion; transverse dimensions are unchanged ($y' = y$, $z' = z$ from Step 1 of Section A).

注意：收缩只发生在运动方向上；横向尺寸不变（由 A 节第 1 步 $y' = y$，$z' = z$）。

---

## D. Relativistic Velocity Addition · 相对论速度叠加

**Claim.** If an object moves with velocity $u'$ in frame $S'$ (along the $x$-axis), and $S'$ moves at velocity $v$ relative to $S$, then the velocity of the object in $S$ is:

**命题。** 若物体在参考系 $S'$ 中以速度 $u'$（沿 $x$ 轴）运动，而 $S'$ 相对 $S$ 以速度 $v$ 运动，则物体在 $S$ 中的速度为：

$$ u = \frac{u' + v}{1 + u'v/c^2}. $$

**Step 1 — Express the object's coordinates using the Lorentz transformation.** In $S'$ the object has position $x' = u' t'$ (moving at velocity $u'$). We want $u = dx/dt$ in $S$. Using the inverse transformation:

**第 1 步 — 用洛伦兹变换表示物体的坐标。** 在 $S'$ 中物体坐标为 $x' = u' t'$（以速度 $u'$ 运动）。我们想求 $S$ 中的 $u = dx/dt$。利用逆变换：

$$ x = \gamma(x' + vt'), \qquad t = \gamma(t' + vx'/c^2). $$

Substituting $x' = u't'$:

代入 $x' = u't'$：

$$ x = \gamma(u't' + vt') = \gamma(u' + v)t', \qquad t = \gamma(t' + vu't'/c^2) = \gamma(1 + u'v/c^2)t'. $$

**Step 2 — Divide to get $u = dx/dt$.** Dividing $x$ by $t$ (both are proportional to $t'$, which cancels):

**第 2 步 — 相除得 $u = dx/dt$。** 将 $x$ 除以 $t$（两者都正比于 $t'$，约去）：

$$ u = \frac{x}{t} = \frac{\gamma(u' + v)t'}{\gamma(1 + u'v/c^2)t'} = \boxed{\,\frac{u' + v}{1 + u'v/c^2}\,} \qquad \blacksquare $$

**Step 3 — Check limiting cases.**
- (a) If $u' = c$: $u = (c + v)/(1 + v/c) = c(c + v)/(c + v) = c$. Light always moves at $c$. ✓
- (b) If $u', v \ll c$: $u \approx u' + v$ (Galilean velocity addition recovered). ✓
- (c) If $u' = v = 0.9c$: $u = (0.9c + 0.9c)/(1 + 0.81) = 1.8c/1.81 \approx 0.994c < c$. Superluminal speeds are impossible. ✓

**第 3 步 — 验证极限情形。**
- (a) 若 $u' = c$：$u = (c + v)/(1 + v/c) = c(c + v)/(c + v) = c$。光总以 $c$ 运动。✓
- (b) 若 $u', v \ll c$：$u \approx u' + v$（恢复伽利略速度叠加）。✓
- (c) 若 $u' = v = 0.9c$：$u = (0.9c + 0.9c)/(1 + 0.81) = 1.8c/1.81 \approx 0.994c < c$。超光速不可能。✓

---

## E. Invariance of the Spacetime Interval $s^2 = (ct)^2 - x^2$ · 时空间隔 $s^2 = (ct)^2 - x^2$ 的不变性

**Claim.** For any two events, the quantity $s^2 = (c\,\Delta t)^2 - (\Delta x)^2 - (\Delta y)^2 - (\Delta z)^2$ takes the same value in all inertial frames.

**命题。** 对任意两个事件，量 $s^2 = (c\,\Delta t)^2 - (\Delta x)^2 - (\Delta y)^2 - (\Delta z)^2$ 在所有惯性系中取相同值。

**Step 1 — Consider the interval in frame $S$.** For two events with separations $\Delta x$, $\Delta t$ (setting $\Delta y = \Delta z = 0$ for simplicity):

**第 1 步 — 在参考系 $S$ 中考察间隔。** 对于分隔为 $\Delta x$，$\Delta t$ 的两个事件（为简单起见设 $\Delta y = \Delta z = 0$）：

$$ s^2 = (c\,\Delta t)^2 - (\Delta x)^2. $$

**Step 2 — Compute in frame $S'$ using the Lorentz transformation.** Applying the Lorentz transformation to the differences $\Delta x' = \gamma(\Delta x - v\,\Delta t)$ and $\Delta t' = \gamma(\Delta t - v\,\Delta x/c^2)$:

**第 2 步 — 用洛伦兹变换在 $S'$ 中计算。** 将洛伦兹变换应用于差分 $\Delta x' = \gamma(\Delta x - v\,\Delta t)$，$\Delta t' = \gamma(\Delta t - v\,\Delta x/c^2)$：

$$ (c\,\Delta t')^2 - (\Delta x')^2 = c^2 \gamma^2(\Delta t - v\,\Delta x/c^2)^2 - \gamma^2(\Delta x - v\,\Delta t)^2. $$

**Step 3 — Expand and simplify.** Expand both squares:

**第 3 步 — 展开并化简。** 展开两个平方项：

$$ \begin{aligned}
&= \gamma^2\big[c^2(\Delta t)^2 - 2v\,\Delta x\,\Delta t + v^2(\Delta x)^2/c^2 - (\Delta x)^2 + 2v\,\Delta x\,\Delta t - v^2(\Delta t)^2\big] \\
&= \gamma^2\big[c^2(\Delta t)^2 + v^2(\Delta x)^2/c^2 - (\Delta x)^2 - v^2(\Delta t)^2\big] \\
&= \gamma^2\big[c^2(\Delta t)^2(1 - v^2/c^2) - (\Delta x)^2(1 - v^2/c^2)\big] \\
&= \gamma^2(1 - v^2/c^2)\big[(c\,\Delta t)^2 - (\Delta x)^2\big].
\end{aligned} $$

Since $\gamma^2 = 1/(1 - v^2/c^2)$, we get $\gamma^2(1 - v^2/c^2) = 1$. Therefore:

由于 $\gamma^2 = 1/(1 - v^2/c^2)$，故 $\gamma^2(1 - v^2/c^2) = 1$。因此：

$$ \boxed{\, (c\,\Delta t')^2 - (\Delta x')^2 = (c\,\Delta t)^2 - (\Delta x)^2 \,} \qquad \blacksquare $$

The spacetime interval $s^2$ is Lorentz-invariant. This is the Minkowski **metric**: every Lorentz transformation preserves $s^2$.

时空间隔 $s^2$ 是洛伦兹不变的。这是闵可夫斯基**度规**：每个洛伦兹变换都保持 $s^2$。

**Step 4 — Physical consequences.** The sign of $s^2$ is invariant:
- $s^2 > 0$ (timelike): a frame exists where $\Delta x' = 0$ (events at the same place); the interval is then purely temporal: $s = c\,\Delta\tau$ where $\Delta\tau =$ proper time. Causally connected.
- $s^2 = 0$ (lightlike / null): connected by a light signal; $|\Delta x| = c|\Delta t|$ in all frames.
- $s^2 < 0$ (spacelike): a frame exists where $\Delta t' = 0$ (simultaneous events); no causal connection.

**第 4 步 — 物理推论。** $s^2$ 的符号是不变量：
- $s^2 > 0$（类时）：存在一个参考系使 $\Delta x' = 0$（事件在同一地点）；间隔此时纯为时间：$s = c\,\Delta\tau$，$\Delta\tau =$ 固有时。有因果联系。
- $s^2 = 0$（类光/零）：由光信号相连；所有参考系中 $|\Delta x| = c|\Delta t|$。
- $s^2 < 0$（类空）：存在一个参考系使 $\Delta t' = 0$（同时发生的事件）；无因果联系。

---

## F. Relativity of Simultaneity · 同时性的相对性

**Claim.** Two events that are simultaneous in $S$ ($\Delta t = 0$) but spatially separated ($\Delta x \ne 0$) are not simultaneous in $S'$: $\Delta t' = -\gamma v\,\Delta x/c^2 \ne 0$.

**命题。** 在 $S$ 中同时（$\Delta t = 0$）但空间分隔（$\Delta x \ne 0$）的两个事件，在 $S'$ 中不同时：$\Delta t' = -\gamma v\,\Delta x/c^2 \ne 0$。

**Step 1 — Apply the Lorentz time transformation.** With $\Delta t = 0$:

**第 1 步 — 应用洛伦兹时间变换。** 令 $\Delta t = 0$：

$$ \Delta t' = \gamma(\Delta t - v\,\Delta x/c^2) = \gamma(0 - v\,\Delta x/c^2) = \boxed{\, -\gamma v\,\Delta x/c^2 \,} \qquad \blacksquare $$

This is not zero unless $\Delta x = 0$ or $v = 0$. The order of events can even be reversed: if event A is before B in $S$, the sign of $\Delta t'$ depends on the sign of $v\,\Delta x$. For spacelike-separated events, the time ordering is frame-dependent. For timelike-separated events (where one can causally influence the other), the time ordering is preserved in all frames (since for timelike separation $(c\,\Delta t)^2 > (\Delta x)^2$, so $\Delta t' = \gamma(\Delta t - v\,\Delta x/c^2)$ always has the same sign as $\Delta t$ when $|v| < c$).

除非 $\Delta x = 0$ 或 $v = 0$，否则此结果不为零。事件的顺序甚至可以颠倒：若在 $S$ 中事件 A 先于 B，$\Delta t'$ 的符号取决于 $v\,\Delta x$ 的符号。对于类空分隔的事件，时间顺序依赖于参考系。对于类时分隔的事件（其中一个可以因果影响另一个），时间顺序在所有参考系中保持不变（因为类时分隔有 $(c\,\Delta t)^2 > (\Delta x)^2$，所以当 $|v| < c$ 时 $\Delta t' = \gamma(\Delta t - v\,\Delta x/c^2)$ 与 $\Delta t$ 的符号始终相同）。

---

*The Lorentz transformation, invariant interval, and velocity addition derived here are the kinematic foundation for all relativistic physics: four-vector dynamics (Module 1.14), covariant electrodynamics (Module 1.15), and quantum field theory (Phase 6). The invariant $s^2$ generalises to the curved spacetime metric $g_{\mu\nu}\,ds^2$ in general relativity (Phase 7).*

*此处推导的洛伦兹变换、不变间隔和速度叠加是所有相对论物理的运动学基础：四矢量动力学（模块 1.14）、协变电动力学（模块 1.15）和量子场论（第 6 阶段）。不变量 $s^2$ 推广为广义相对论（第 7 阶段）中弯曲时空度规 $g_{\mu\nu}\,ds^2$。*

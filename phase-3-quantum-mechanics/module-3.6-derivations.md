# Derivations — Module 3.6: Time-Independent Perturbation Theory
# 推导 — 模块 3.6：定态微扰理论

> Companion to [Module 3.6](./module-3.6-time-independent-perturbation-theory.md). Full step-by-step proofs of every non-trivial result quoted there. English first, then 中文.
> [模块 3.6](./module-3.6-time-independent-perturbation-theory.md) 的配套文档：对该模块所引用每个非平凡结果的完整逐步证明。先英文，后中文。

---

## A. First-Order Energy Correction: Eₙ⁽¹⁾ = ⟨n|Ĥ′|n⟩ · 一阶能量修正

**Claim.** For the Hamiltonian Ĥ = Ĥ₀ + λĤ′ (λ small), the first-order correction to the non-degenerate energy level Eₙ⁽⁰⁾ is Eₙ⁽¹⁾ = ⟨n⁽⁰⁾|Ĥ′|n⁽⁰⁾⟩.

**命题。** 对哈密顿量 Ĥ = Ĥ₀ + λĤ′（λ 为小量），非简并能级 Eₙ⁽⁰⁾ 的一阶修正为 Eₙ⁽¹⁾ = ⟨n⁽⁰⁾|Ĥ′|n⁽⁰⁾⟩。

**Step 1 — Expand energies and states in powers of λ.** Write the exact eigenvalue problem (Ĥ₀ + λĤ′)|n⟩ = Eₙ|n⟩ with:

**第 1 步 — 将能量和态按 λ 幂次展开。** 将精确本征值方程 (Ĥ₀ + λĤ′)|n⟩ = Eₙ|n⟩ 写成：

  Eₙ = Eₙ⁽⁰⁾ + λ Eₙ⁽¹⁾ + λ² Eₙ⁽²⁾ + …

  |n⟩ = |n⁽⁰⁾⟩ + λ|n⁽¹⁾⟩ + λ²|n⁽²⁾⟩ + …

where Ĥ₀|n⁽⁰⁾⟩ = Eₙ⁽⁰⁾|n⁽⁰⁾⟩ (known exactly). The states |m⁽⁰⁾⟩ form a complete orthonormal set: ⟨m⁽⁰⁾|n⁽⁰⁾⟩ = δ_{mn}.

其中 Ĥ₀|n⁽⁰⁾⟩ = Eₙ⁽⁰⁾|n⁽⁰⁾⟩（精确已知）。态 |m⁽⁰⁾⟩ 构成完备正交归一组：⟨m⁽⁰⁾|n⁽⁰⁾⟩ = δ_{mn}。

**Step 2 — Substitute into the eigenvalue equation and collect by powers of λ.** Substituting and expanding:

**第 2 步 — 代入本征值方程并按 λ 幂次整理。** 代入展开：

  (Ĥ₀ + λĤ′)(|n⁽⁰⁾⟩ + λ|n⁽¹⁾⟩ + …) = (Eₙ⁽⁰⁾ + λEₙ⁽¹⁾ + …)(|n⁽⁰⁾⟩ + λ|n⁽¹⁾⟩ + …).

**Order λ⁰:** Ĥ₀|n⁽⁰⁾⟩ = Eₙ⁽⁰⁾|n⁽⁰⁾⟩. ✓ (satisfied by assumption)

**λ⁰ 阶：** Ĥ₀|n⁽⁰⁾⟩ = Eₙ⁽⁰⁾|n⁽⁰⁾⟩。✓（由假设满足）

**Order λ¹:**

**λ¹ 阶：**

  Ĥ₀|n⁽¹⁾⟩ + Ĥ′|n⁽⁰⁾⟩ = Eₙ⁽⁰⁾|n⁽¹⁾⟩ + Eₙ⁽¹⁾|n⁽⁰⁾⟩.    … (*)

**Step 3 — Project onto ⟨n⁽⁰⁾|.** Take the inner product of (*) with ⟨n⁽⁰⁾|:

**第 3 步 — 投影到 ⟨n⁽⁰⁾|。** 将 (*) 与 ⟨n⁽⁰⁾| 取内积：

  ⟨n⁽⁰⁾|Ĥ₀|n⁽¹⁾⟩ + ⟨n⁽⁰⁾|Ĥ′|n⁽⁰⁾⟩ = Eₙ⁽⁰⁾⟨n⁽⁰⁾|n⁽¹⁾⟩ + Eₙ⁽¹⁾⟨n⁽⁰⁾|n⁽⁰⁾⟩.

Since Ĥ₀ is Hermitian: ⟨n⁽⁰⁾|Ĥ₀|n⁽¹⁾⟩ = ⟨Ĥ₀n⁽⁰⁾|n⁽¹⁾⟩ = Eₙ⁽⁰⁾⟨n⁽⁰⁾|n⁽¹⁾⟩. The Eₙ⁽⁰⁾ terms cancel:

由 Ĥ₀ 的厄米性：⟨n⁽⁰⁾|Ĥ₀|n⁽¹⁾⟩ = Eₙ⁽⁰⁾⟨n⁽⁰⁾|n⁽¹⁾⟩。Eₙ⁽⁰⁾ 项消去：

  ⟨n⁽⁰⁾|Ĥ′|n⁽⁰⁾⟩ = Eₙ⁽¹⁾ · 1.

Therefore:

因此：

  **Eₙ⁽¹⁾ = ⟨n⁽⁰⁾|Ĥ′|n⁽⁰⁾⟩**. ∎

**Physical interpretation.** The first-order energy shift is simply the expectation value of the perturbation in the unperturbed state — the diagonal matrix element. It is the classical-style average of the perturbation over the unperturbed probability distribution.

**物理诠释。** 一阶能量移动就是微扰在无微扰态中的期望值——即对角矩阵元。它是微扰在无微扰概率分布上的经典式平均。

---

## B. First-Order State Correction · 一阶态修正

**Claim.** The first-order correction to the state |n⁽⁰⁾⟩ is:

**命题。** 态 |n⁽⁰⁾⟩ 的一阶修正为：

  |n⁽¹⁾⟩ = Σ_{m≠n} [⟨m⁽⁰⁾|Ĥ′|n⁽⁰⁾⟩ / (Eₙ⁽⁰⁾ − Eₘ⁽⁰⁾)] |m⁽⁰⁾⟩.

**Step 1 — Project the λ¹ equation onto ⟨m⁽⁰⁾| for m ≠ n.** From equation (*) of Section A, take the inner product with ⟨m⁽⁰⁾| (m ≠ n):

**第 1 步 — 将 λ¹ 方程投影到 ⟨m⁽⁰⁾|（m ≠ n）。** 从第 A 节方程 (*) 出发，与 ⟨m⁽⁰⁾| 取内积（m ≠ n）：

  ⟨m⁽⁰⁾|Ĥ₀|n⁽¹⁾⟩ + ⟨m⁽⁰⁾|Ĥ′|n⁽⁰⁾⟩ = Eₙ⁽⁰⁾⟨m⁽⁰⁾|n⁽¹⁾⟩ + Eₙ⁽¹⁾⟨m⁽⁰⁾|n⁽⁰⁾⟩.

  Eₘ⁽⁰⁾⟨m⁽⁰⁾|n⁽¹⁾⟩ + ⟨m⁽⁰⁾|Ĥ′|n⁽⁰⁾⟩ = Eₙ⁽⁰⁾⟨m⁽⁰⁾|n⁽¹⁾⟩ + 0.

(The last term vanishes because ⟨m⁽⁰⁾|n⁽⁰⁾⟩ = δ_{mn} = 0 for m ≠ n.)

（最后一项消失，因为对 m ≠ n 有 ⟨m⁽⁰⁾|n⁽⁰⁾⟩ = δ_{mn} = 0。）

**Step 2 — Solve for ⟨m⁽⁰⁾|n⁽¹⁾⟩.**

**第 2 步 — 求解 ⟨m⁽⁰⁾|n⁽¹⁾⟩。**

  (Eₙ⁽⁰⁾ − Eₘ⁽⁰⁾) ⟨m⁽⁰⁾|n⁽¹⁾⟩ = ⟨m⁽⁰⁾|Ĥ′|n⁽⁰⁾⟩.

Since Eₙ⁽⁰⁾ ≠ Eₘ⁽⁰⁾ (non-degenerate case):

由于 Eₙ⁽⁰⁾ ≠ Eₘ⁽⁰⁾（非简并情形）：

  ⟨m⁽⁰⁾|n⁽¹⁾⟩ = ⟨m⁽⁰⁾|Ĥ′|n⁽⁰⁾⟩ / (Eₙ⁽⁰⁾ − Eₘ⁽⁰⁾).

**Step 3 — Reconstruct |n⁽¹⁾⟩ from its expansion coefficients.** By completeness, |n⁽¹⁾⟩ = Σₘ ⟨m⁽⁰⁾|n⁽¹⁾⟩ |m⁽⁰⁾⟩. The m = n term can be chosen zero (corresponding to the choice of normalization ⟨n⁽⁰⁾|n⟩ = 1 to all orders):

**第 3 步 — 从展开系数重建 |n⁽¹⁾⟩。** 由完备性，|n⁽¹⁾⟩ = Σₘ ⟨m⁽⁰⁾|n⁽¹⁾⟩ |m⁽⁰⁾⟩。m = n 项可选为零（对应于归一化选择 ⟨n⁽⁰⁾|n⟩ = 1 对所有阶成立）：

  **|n⁽¹⁾⟩ = Σ_{m≠n} [⟨m⁽⁰⁾|Ĥ′|n⁽⁰⁾⟩ / (Eₙ⁽⁰⁾ − Eₘ⁽⁰⁾)] |m⁽⁰⁾⟩**. ∎

**Note on validity.** This expression is valid when the perturbation is small relative to the level spacings: |⟨m|Ĥ′|n⟩| ≪ |Eₙ⁽⁰⁾ − Eₘ⁽⁰⁾| for all m ≠ n. When this breaks down near a degeneracy, degenerate perturbation theory (Section D) must be used.

**有效性注记。** 当微扰相对于能级间距很小时此表达式有效：对所有 m ≠ n 有 |⟨m|Ĥ′|n⟩| ≪ |Eₙ⁽⁰⁾ − Eₘ⁽⁰⁾|。当接近简并时失效，必须使用简并微扰理论（第 D 节）。

---

## C. Second-Order Energy Correction: Eₙ⁽²⁾ = Σ_{m≠n}|⟨m|Ĥ′|n⟩|²/(Eₙ⁽⁰⁾ − Eₘ⁽⁰⁾) · 二阶能量修正

**Claim.** The second-order energy correction is:

**命题。** 二阶能量修正为：

  Eₙ⁽²⁾ = Σ_{m≠n} |⟨m⁽⁰⁾|Ĥ′|n⁽⁰⁾⟩|² / (Eₙ⁽⁰⁾ − Eₘ⁽⁰⁾).

**Step 1 — Collect terms at order λ².** Expanding the eigenvalue equation to order λ²:

**第 1 步 — 整理 λ² 阶项。** 将本征值方程展开到 λ² 阶：

  Ĥ₀|n⁽²⁾⟩ + Ĥ′|n⁽¹⁾⟩ = Eₙ⁽⁰⁾|n⁽²⁾⟩ + Eₙ⁽¹⁾|n⁽¹⁾⟩ + Eₙ⁽²⁾|n⁽⁰⁾⟩.    … (**)

**Step 2 — Project onto ⟨n⁽⁰⁾|.** Take the inner product with ⟨n⁽⁰⁾|:

**第 2 步 — 投影到 ⟨n⁽⁰⁾|。** 与 ⟨n⁽⁰⁾| 取内积：

  ⟨n⁽⁰⁾|Ĥ₀|n⁽²⁾⟩ + ⟨n⁽⁰⁾|Ĥ′|n⁽¹⁾⟩ = Eₙ⁽⁰⁾⟨n⁽⁰⁾|n⁽²⁾⟩ + Eₙ⁽¹⁾⟨n⁽⁰⁾|n⁽¹⁾⟩ + Eₙ⁽²⁾⟨n⁽⁰⁾|n⁽⁰⁾⟩.

Using ⟨n⁽⁰⁾|Ĥ₀ = Eₙ⁽⁰⁾⟨n⁽⁰⁾| (Hermiticity of Ĥ₀), the first terms on each side cancel:

利用 ⟨n⁽⁰⁾|Ĥ₀ = Eₙ⁽⁰⁾⟨n⁽⁰⁾|（Ĥ₀ 的厄米性），两边第一项消去：

  ⟨n⁽⁰⁾|Ĥ′|n⁽¹⁾⟩ = Eₙ⁽¹⁾⟨n⁽⁰⁾|n⁽¹⁾⟩ + Eₙ⁽²⁾.

With the normalization convention ⟨n⁽⁰⁾|n⁽¹⁾⟩ = 0 (from Section B, the m = n coefficient of |n⁽¹⁾⟩ is zero):

取归一化约定 ⟨n⁽⁰⁾|n⁽¹⁾⟩ = 0（由第 B 节，|n⁽¹⁾⟩ 的 m = n 系数为零）：

  Eₙ⁽²⁾ = ⟨n⁽⁰⁾|Ĥ′|n⁽¹⁾⟩.

**Step 3 — Substitute the expansion of |n⁽¹⁾⟩.** From Section B:

**第 3 步 — 代入 |n⁽¹⁾⟩ 的展开。** 由第 B 节：

  Eₙ⁽²⁾ = ⟨n⁽⁰⁾|Ĥ′ · Σ_{m≠n} [⟨m⁽⁰⁾|Ĥ′|n⁽⁰⁾⟩ / (Eₙ⁽⁰⁾ − Eₘ⁽⁰⁾)] |m⁽⁰⁾⟩

        = Σ_{m≠n} [⟨m⁽⁰⁾|Ĥ′|n⁽⁰⁾⟩ / (Eₙ⁽⁰⁾ − Eₘ⁽⁰⁾)] · ⟨n⁽⁰⁾|Ĥ′|m⁽⁰⁾⟩.

Now ⟨n⁽⁰⁾|Ĥ′|m⁽⁰⁾⟩ = (⟨m⁽⁰⁾|Ĥ′|n⁽⁰⁾⟩)* (since Ĥ′ is Hermitian). Therefore:

现在 ⟨n⁽⁰⁾|Ĥ′|m⁽⁰⁾⟩ = (⟨m⁽⁰⁾|Ĥ′|n⁽⁰⁾⟩)*（因为 Ĥ′ 是厄米的）。因此：

  **Eₙ⁽²⁾ = Σ_{m≠n} |⟨m⁽⁰⁾|Ĥ′|n⁽⁰⁾⟩|² / (Eₙ⁽⁰⁾ − Eₘ⁽⁰⁾)**. ∎

**Step 4 — Sign of Eₙ⁽²⁾ for the ground state.** For the ground state n = 0, all denominators Eₙ⁽⁰⁾ − Eₘ⁽⁰⁾ are negative (since Eₘ⁽⁰⁾ > E₀⁽⁰⁾ for all m > 0), and all numerators are non-negative. Therefore:

**第 4 步 — 基态 Eₙ⁽²⁾ 的符号。** 对基态 n = 0，所有分母 Eₙ⁽⁰⁾ − Eₘ⁽⁰⁾ 为负（因为对所有 m > 0 有 Eₘ⁽⁰⁾ > E₀⁽⁰⁾），所有分子为非负。因此：

  E₀⁽²⁾ ≤ 0: **the second-order correction always lowers the ground-state energy**. ∎

  E₀⁽²⁾ ≤ 0：**二阶修正总是降低基态能量**。∎

---

## D. Degenerate Perturbation Theory: Diagonalize Ĥ′ in the Degenerate Subspace · 简并微扰理论：在简并子空间内对角化 Ĥ′

**Claim.** When Eₙ⁽⁰⁾ is g-fold degenerate (g degenerate states |n⁽⁰⁾,α⟩, α = 1,…,g spanning the subspace V_n), the first-order energy corrections and good zeroth-order states are found by diagonalizing the g×g perturbation matrix W_{αβ} = ⟨n⁽⁰⁾,α|Ĥ′|n⁽⁰⁾,β⟩ within V_n. The eigenvalues of W give Eₙ⁽¹⁾, and the eigenvectors give the good zeroth-order states.

**命题。** 当 Eₙ⁽⁰⁾ 是 g 重简并时（g 个简并态 |n⁽⁰⁾,α⟩，α = 1,…,g 张成子空间 V_n），一阶能量修正和"好"的零阶态通过在 V_n 内对角化 g×g 微扰矩阵 W_{αβ} = ⟨n⁽⁰⁾,α|Ĥ′|n⁽⁰⁾,β⟩ 来求得。W 的本征值给出 Eₙ⁽¹⁾，本征向量给出好的零阶态。

**Step 1 — Why non-degenerate theory fails.** In non-degenerate perturbation theory, the first-order state correction has denominators Eₙ⁽⁰⁾ − Eₘ⁽⁰⁾. If Eₘ⁽⁰⁾ = Eₙ⁽⁰⁾ for some m ≠ n (degenerate states in V_n), these denominators vanish, making the expression diverge. The expansion breaks down.

**第 1 步 — 非简并理论为何失效。** 在非简并微扰理论中，一阶态修正有分母 Eₙ⁽⁰⁾ − Eₘ⁽⁰⁾。若对某些 m ≠ n（V_n 中的简并态）有 Eₘ⁽⁰⁾ = Eₙ⁽⁰⁾，则这些分母为零，使表达式发散。展开失效。

**Step 2 — Set up the problem correctly.** Let the good zeroth-order states within V_n (yet to be determined) be:

**第 2 步 — 正确建立问题。** 设 V_n 内的好零阶态（待确定）为：

  |n⁽⁰⁾⟩ = Σ_{α=1}^g c_α |n⁽⁰⁾,α⟩.

The first-order eigenvalue equation (from Section A Step 2, at order λ¹) within the degenerate subspace is:

简并子空间内的一阶本征值方程（来自第 A 节第 2 步，λ¹ 阶）为：

  (Ĥ₀ + λĤ′)|n⟩ = Eₙ|n⟩ projected onto V_n at first order.

**Step 3 — Project onto V_n.** Take the inner product of the order λ¹ equation with ⟨n⁽⁰⁾,β| for each β. The Ĥ₀ terms on both sides cancel (as in Section A Step 3), leaving:

**第 3 步 — 投影到 V_n。** 将 λ¹ 阶方程对每个 β 与 ⟨n⁽⁰⁾,β| 取内积。两边的 Ĥ₀ 项消去（如第 A 节第 3 步），留下：

  Σ_{α} ⟨n⁽⁰⁾,β|Ĥ′|n⁽⁰⁾,α⟩ c_α = Eₙ⁽¹⁾ c_β.

In matrix form with W_{βα} = ⟨n⁽⁰⁾,β|Ĥ′|n⁽⁰⁾,α⟩:

用矩阵形式，W_{βα} = ⟨n⁽⁰⁾,β|Ĥ′|n⁽⁰⁾,α⟩：

  **W c = Eₙ⁽¹⁾ c**.

This is a g×g eigenvalue equation.

这是一个 g×g 本征值方程。

**Step 4 — Solve the eigenvalue equation.** The eigenvalues E⁽¹⁾₁, E⁽¹⁾₂, …, E⁽¹⁾_g of the Hermitian matrix W are real (Section B of Module 3.3). The perturbation lifts (some or all of) the degeneracy: the original g-fold degenerate level splits into levels with first-order corrections E⁽¹⁾₁, …, E⁽¹⁾_g (some may remain degenerate if W has repeated eigenvalues).

**第 4 步 — 求解本征值方程。** 厄米矩阵 W 的本征值 E⁽¹⁾₁, E⁽¹⁾₂, …, E⁽¹⁾_g 均为实数（模块 3.3 第 B 节）。微扰解除（部分或全部）简并：原来的 g 重简并能级分裂为具有一阶修正 E⁽¹⁾₁, …, E⁽¹⁾_g 的能级（若 W 有重复本征值，某些简并可能保留）。

**Step 5 — Good zeroth-order states.** The eigenvectors c⁽ᵏ⁾ of W give the **good zeroth-order states**:

**第 5 步 — 好的零阶态。** W 的本征向量 c⁽ᵏ⁾ 给出**好的零阶态**：

  |n⁽⁰⁾;k⟩ = Σ_{α} c⁽ᵏ⁾_α |n⁽⁰⁾,α⟩,  k = 1,…,g.

These are the correct zeroth-order starting states such that the non-degenerate formulas for higher-order corrections are well-defined (the dangerous cross-terms between degenerate states in the denominators of state corrections now vanish because the perturbation matrix is diagonal in this basis).

这些是正确的零阶起始态，使得高阶修正的非简并公式定义良好（态修正分母中简并态之间的危险交叉项现在在此基底中消失，因为微扰矩阵在此基底中是对角的）。

**Step 6 — Summary.** The total first-order corrected energy levels are:

**第 6 步 — 汇总。** 总的一阶修正能级为：

  Eₙ,k = Eₙ⁽⁰⁾ + λ E⁽¹⁾_k,  k = 1, …, g,

where E⁽¹⁾_k are the eigenvalues of W = (⟨n⁽⁰⁾,α|Ĥ′|n⁽⁰⁾,β⟩). Once the good states are identified, second-order corrections follow from the non-degenerate formula of Section C, now with denominators Eₙ,k − Eₘ⁽⁰⁾ (m outside V_n) which are nonzero. ∎

其中 E⁽¹⁾_k 是 W = (⟨n⁽⁰⁾,α|Ĥ′|n⁽⁰⁾,β⟩) 的本征值。一旦确定了好的态，二阶修正就可以用第 C 节的非简并公式计算，现在分母 Eₙ,k − Eₘ⁽⁰⁾（m 在 V_n 之外）非零。∎

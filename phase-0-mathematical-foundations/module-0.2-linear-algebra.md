# Module 0.2 — Linear Algebra ⭐

> **Phase 0 — [Mathematical Foundations](./README.md)** · Format: Definition → Demonstration → Application

Linear algebra is not background material for quantum mechanics — it *is* quantum mechanics. Every state, every measurement, every time evolution is a statement in the language of vectors and operators.

---

## 1. Vectors, Inner Products & Bases

**Definition.** A **vector space** is a set of objects (vectors) that can be added and scaled while staying in the set. An **inner product** ⟨u|v⟩ assigns a scalar to each pair of vectors, satisfying linearity, conjugate symmetry (⟨u|v⟩ = ⟨v|u⟩*), and positive-definiteness (⟨v|v⟩ ≥ 0). The **norm** is ‖v‖ = √⟨v|v⟩. A set of vectors {eᵢ} is **orthonormal** if ⟨eᵢ|eⱼ⟩ = δᵢⱼ and **complete** (a basis) if every vector can be written v = Σᵢ ⟨eᵢ|v⟩ eᵢ. The coefficients ⟨eᵢ|v⟩ are the **components** in that basis.

**Demonstration.** In ℝ², the standard basis {(1,0), (0,1)} is orthonormal under the dot product. Rotating to a new orthonormal basis changes the components but not the underlying vector — a lesson that carries into QM, where the basis of energy eigenstates and the basis of position eigenstates represent the same state in different ways.

**Application.** The Hilbert space of quantum states is an (often infinite-dimensional) inner product space. The inner product ⟨ψ|φ⟩ gives transition amplitudes; completeness of the energy-eigenstate basis means any state can be written as a superposition — the foundation of all wave mechanics (Module 3.3).

---

## 2. Operators & Eigenvalues ⭐

**Definition.** A **linear operator** A maps vectors to vectors linearly. In a finite-dimensional space with a chosen basis, operators are represented as **matrices**. The **eigenvalue equation** is

  A v = λ v

where v ≠ 0 is an **eigenvector** and λ is the corresponding **eigenvalue**. Two special classes dominate physics:

- **Hermitian operators** (A = A†, where A†ᵢⱼ = Aⱼᵢ*): eigenvalues are **real**, eigenvectors for distinct eigenvalues are **orthogonal**, and the eigenvectors form a complete basis — the **spectral theorem**.
- **Unitary operators** (U†U = I): preserve norms (‖Uv‖ = ‖v‖) and have eigenvalues of modulus 1.

The three **Pauli matrices** are the foundational Hermitian, traceless, unitary-up-to-phase operators of spin-½:

  σ_x = [[0, 1], [1, 0]],   σ_y = [[0, −i], [i, 0]],   σ_z = [[1, 0], [0, −1]]

They satisfy σᵢ σⱼ = δᵢⱼ I + i εᵢⱼₖ σₖ and are the building blocks of all two-level quantum systems.

**Demonstration.** Diagonalize σ_x. The characteristic equation det(σ_x − λI) = 0:

  det([[−λ, 1], [1, −λ]]) = λ² − 1 = 0 → **λ = ±1**.

For λ = +1: (σ_x − I)v = 0 gives v₁ = v₂, so the eigenvector is (1/√2)(1, 1)ᵀ.
For λ = −1: v₁ = −v₂, giving (1/√2)(1, −1)ᵀ.
These two orthonormal eigenvectors are the **|+x⟩, |−x⟩ basis** — the spin eigenstates along x.

**Application.** Quantum mechanics is, at its core, linear algebra in Hilbert space: physical **observables are Hermitian operators** whose real eigenvalues are the only allowed measurement outcomes, and **time evolution is unitary** (Module 3.10), preserving probability. The spectral theorem guarantees any observable can be diagonalized and its eigenstates used as a basis — this is why energy eigenstates and momentum eigenstates are so central to Module 3.3. Separately, finding the **normal modes** of coupled oscillators (Module 1.6) is exactly the eigenvalue problem for the mass-weighted stiffness matrix.

---

## Module 0.2 Self-Test (blank page)

1. Define an inner product and orthonormality; expand a vector in an orthonormal basis.
2. State the spectral theorem for Hermitian operators and its two key consequences.
3. Write down the three Pauli matrices and compute σ_x σ_y.
4. Find the eigenvalues and normalized eigenvectors of σ_z.
5. Explain why observables in QM must be Hermitian and why time evolution must be unitary.

---

← Previous: [Module 0.1 — Calculus & Taylor Series](./module-0.1-calculus-and-taylor-series.md) · [Phase 0 index](./README.md) · Next: [Module 0.3 — Differential Equations](./module-0.3-differential-equations.md) →

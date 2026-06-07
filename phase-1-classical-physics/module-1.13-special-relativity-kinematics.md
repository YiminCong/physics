# Module 1.13 — Special Relativity — Kinematics ⭐

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Einstein's Postulates and the Lorentz Transformation

**Definition.** Special relativity rests on two postulates: (1) the **principle of relativity** — the laws of physics are the same in all inertial frames; (2) the **constancy of c** — the speed of light in vacuum is the same (c ≈ 3 × 10⁸ m/s) for all inertial observers, regardless of the motion of the source or detector. These replace the Galilean transformation with the **Lorentz transformation**. For a frame S′ moving at velocity v along the x-axis relative to S:

x′ = γ(x − vt),   t′ = γ(t − vx/c²),   y′ = y,   z′ = z,

where γ = 1/√(1 − v²/c²) ≥ 1 is the **Lorentz factor**. The inverse replaces v → −v. **Velocity addition**: for an object with velocity u′ in S′, its velocity in S is u = (u′ + v)/(1 + u′v/c²), ensuring no velocity can exceed c.

**Demonstration.** Two key consequences follow directly. **Time dilation**: a clock at rest in S′ ticks at rate dt = γ dτ, where τ is the **proper time** (the time measured in the rest frame). A muon created at the top of the atmosphere (v/c ≈ 0.9998) with proper lifetime τ₀ = 2.2 μs survives γτ₀ ≈ 35 μs in the lab frame, long enough to reach Earth's surface — a direct experimental confirmation. **Length contraction**: an object of proper length L₀ (rest frame) has measured length L = L₀/γ along the direction of motion.

**Application.** The Lorentz transformation reveals that time and space are not absolute but mix between frames. The resolution of the twin paradox (the travelling twin is younger) illustrates that elapsed proper time, not coordinate time, is the physically invariant quantity. The mathematical framework sets up the four-dimensional spacetime geometry of Section 2.

## 2. Minkowski Spacetime and the Invariant Interval

**Definition.** Events are points in **Minkowski spacetime** labelled by four coordinates x^μ = (ct, x, y, z). The **spacetime interval** between two events is:

s² = (c Δt)² − (Δx)² − (Δy)² − (Δz)²

(using the +−−− signature convention). This quantity is **Lorentz-invariant**: all inertial observers assign the same value s². Depending on sign: s² > 0 (**timelike** — a causal connection exists), s² = 0 (**lightlike** / null — connected by a light ray), s² < 0 (**spacelike** — no causal connection). The **relativity of simultaneity** follows: two events with Δt = 0 in S but Δx ≠ 0 are not simultaneous in S′ (Δt′ = −γvΔx/c² ≠ 0).

**Demonstration.** The invariant interval for muon travel: in the lab frame, Δt = 35 μs, Δx = v·Δt. In the muon's rest frame Δx′ = 0, Δt′ = τ₀ = 2.2 μs. Check: s² = c²(35 μs)² − (v·35 μs)² = c²(35 μs)²(1 − v²/c²) = c²(35 μs)²/γ² = c²(2.2 μs)². Consistent.

**Application.** Minkowski's geometric formulation makes special relativity a theory of four-dimensional pseudo-Riemannian geometry. It generalises to curved spacetime in general relativity (Phase 7). The four-vector formalism developed here (four-position x^μ, four-velocity, four-momentum) is the language of all relativistic physics: particle kinematics (Module 1.14), covariant electromagnetism (Module 1.15), and quantum field theory (Phase 6).

---

**Self-test (blank page)**

1. Derive the time-dilation formula Δt = γΔτ from the Lorentz transformation. A particle lives 10 μs in its rest frame while moving at v = 0.6c. How long does it live in the lab frame, and how far does it travel?
2. Two events occur at the same place in frame S, separated by Δt = 4 s. What is the spatial separation in a frame where the events are separated by Δt′ = 5 s?
3. Classify the interval s² between events A = (0, 0, 0, 0) and B = (c·3 s, 5 m, 0, 0) as timelike, lightlike, or spacelike. Can B causally affect A?
4. Explain the relativity of simultaneity with a concrete example using a moving train and lightning strikes. Why does this not lead to paradoxes?

---

← Previous: [Module 1.12 — Optics & Interference](./module-1.12-optics-interference.md) · [Phase 1 index](./README.md) · Next: [Module 1.14 — Relativistic Dynamics & E = mc²](./module-1.14-relativistic-dynamics-energy-momentum.md) →

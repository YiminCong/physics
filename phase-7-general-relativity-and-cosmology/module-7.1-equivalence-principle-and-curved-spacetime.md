# Module 7.1 — The Equivalence Principle & Curved Spacetime ⭐

> **Phase 7 — [General Relativity & Cosmology](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. The Equivalence Principle

**Definition.** The *weak equivalence principle* states that gravitational mass (the charge that sources and responds to gravity) and inertial mass (resistance to acceleration) are identical for all bodies. Einstein elevated this to the *strong equivalence principle*: no local experiment — mechanical or otherwise — can distinguish a freely falling frame from an inertial frame in empty space. Equivalently, a uniformly accelerating frame is locally indistinguishable from a uniform gravitational field. This is the founding observation of General Relativity.

**Demonstration.** Consider an observer in a sealed elevator. If the elevator accelerates upward at g, a dropped ball falls to the floor at rate g — identical to the behaviour inside a gravitational field of strength g. Conversely, a freely falling elevator is locally inertial: a released ball floats beside the observer, just as in deep space. The equivalence is exact to all orders locally; tidal effects (geodesic deviation) only become measurable at finite separations, encoding curvature.

**Application.** The equivalence principle has two immediate physical consequences, derivable before writing a single field equation.

- *Gravitational time dilation*: a clock deeper in a gravitational potential φ runs slow by the factor (1 + φ/c²) relative to one at higher potential (derivable by treating a gravitational field as an equivalent acceleration). Clocks at Earth's surface lose ≈ 45 μs/day relative to GPS satellites due to this effect (partially offset by the velocity/SR effect; see Module 7.3).
- *Light bending*: a horizontal light beam inside an accelerating elevator is deflected downward by the acceleration. By equivalence, gravity must also bend light — and by a factor of two more than Newtonian optics predicts, because spacetime curvature (not just time dilation) contributes equally. Confirmed by Eddington's 1919 solar-eclipse measurement.

---

## 2. From Flat to Curved Spacetime

**Definition.** Special Relativity (Module 1.13) is framed in *Minkowski spacetime*: a flat, globally inertial manifold with line element ds² = −c²dt² + dx² + dy² + dz² = ημν dxμ dxν, where ημν = diag(−1, +1, +1, +1). Gravity cannot be accommodated in flat spacetime while respecting the equivalence principle. Einstein's great insight: gravity is not a force propagating through a fixed background but is instead the *curvature of spacetime itself*. The spacetime manifold has a dynamical metric g_{μν}(x) that replaces ημν; freely falling particles follow the straightest paths (*geodesics*) in this curved geometry.

**Demonstration.** On the surface of a sphere, initially parallel lines of longitude converge at the poles: parallel transport around a closed loop rotates a vector by an angle equal to the solid angle enclosed. This is an intrinsic curvature effect requiring no embedding in a higher dimension. In 4-D spacetime, the Riemann tensor Rμνρσ (Module 7.2) captures this rotation; where Rμνρσ = 0 everywhere, spacetime is flat and SR is recovered globally.

**Application.** The conceptual leap — gravity as geometry — unifies the universality of free fall (all bodies follow the same geodesics regardless of composition, because the trajectory depends only on the metric) with the field-theoretic description of gravity. It sets the stage for the full mathematical machinery (Module 7.2), geodesic motion (Module 7.3), and Einstein's field equations (Module 7.4). It also signals a break from the Newtonian picture of gravity as an instantaneous force (Module 1.5): information about curvature propagates at c.

---

**Self-test (blank page)**

1. State the strong equivalence principle. How does it imply that freely falling frames are locally inertial, and what is the role of tidal forces in limiting this?
2. Derive the gravitational redshift formula z ≈ Δφ/c² using only the equivalence principle and the Doppler effect — no field equations needed.
3. Why does GR predict twice the Newtonian deflection of light by the Sun? Which physical effect contributes the "extra" factor?

---

← [Phase 7 index](./README.md) · Next: [Module 7.2 — Tensors, the Metric & Curvature](./module-7.2-tensors-metric-and-curvature.md) →

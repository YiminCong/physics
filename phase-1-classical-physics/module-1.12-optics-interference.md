# Module 1.12 — Optics & Interference
**模块 1.12 — 光学与干涉**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.12-optics-interference-derivations.md)

---

## 1. Geometric Optics and Huygens' Principle · 几何光学与惠更斯原理

**Definition.** **Geometric (ray) optics** applies when the wavelength λ is much smaller than all relevant length scales. Light travels in straight rays; the fundamental laws are: (i) **reflection**: angle of incidence equals angle of reflection; (ii) **Snell's law of refraction**: n₁ sin θ₁ = n₂ sin θ₂, where n = c/v is the refractive index. **Total internal reflection** occurs for θ₁ > θ_c = arcsin(n₂/n₁) when n₁ > n₂. Thin-lens optics gives the **lens equation** 1/f = 1/d_o + 1/d_i and magnification M = −d_i/d_o.

**定义。** 当波长 λ 远小于所有相关长度尺度时，**几何（射线）光学**适用。光沿直线传播；基本定律为：(i) **反射定律**：入射角等于反射角；(ii) **折射的斯涅尔定律**：n₁ sin θ₁ = n₂ sin θ₂，其中 n = c/v 为折射率。当 n₁ > n₂ 且 θ₁ > θ_c = arcsin(n₂/n₁) 时发生**全内反射**。薄透镜光学给出**透镜方程** 1/f = 1/d_o + 1/d_i 和放大率 M = −d_i/d_o。

**Huygens' principle** states that every point on a wavefront acts as a secondary source of spherical wavelets; the new wavefront is the envelope of these wavelets. This semi-geometrical picture correctly reproduces reflection and refraction, and provides the seed for the full wave theory of diffraction.

**惠更斯原理**指出，波前上的每一点都是球面子波的次级波源；新波前是这些子波的包络面。这一半几何图景正确地重现了反射和折射，并为完整的衍射波动理论提供了基础。

**Demonstration.** Snell's law from Huygens: a plane wave hits an interface at angle θ₁. The wavelet from the leading edge of the wavefront travels distance v₂ t in medium 2 while the trailing edge travels v₁ t in medium 1. Geometry gives sin θ₁/v₁ = sin θ₂/v₂, i.e. n₁ sin θ₁ = n₂ sin θ₂.

**演示。** 用惠更斯原理推导斯涅尔定律：平面波以角度 θ₁ 射向界面。波前前缘的子波在介质 2 中行进距离 v₂ t，而后缘在介质 1 中行进 v₁ t。几何关系给出 sin θ₁/v₁ = sin θ₂/v₂，即 n₁ sin θ₁ = n₂ sin θ₂。

**Application.** Ray optics designs lenses, mirrors, optical fibres, and telescopes. Its breakdown — when λ is not negligible — signals the onset of wave phenomena treated in Section 2.

**应用。** 射线光学用于设计透镜、反射镜、光纤和望远镜。当 λ 不可忽略时，射线光学失效，这标志着第 2 节所处理的波动现象的开始。

## 2. Interference and Diffraction · 干涉与衍射

**Definition.** **Interference** arises when two or more coherent waves superpose. For two slits separated by distance d, illuminated by wavelength λ at normal incidence, the path difference Δ = d sin θ. **Constructive interference** (bright fringes) at d sin θ = mλ; **destructive interference** at d sin θ = (m + ½)λ. The **single-slit diffraction** intensity envelope is I(θ) = I₀ sinc²(πa sin θ / λ), where a is the slit width. **Diffraction gratings** with N slits produce sharp principal maxima at d sin θ = mλ with resolving power R = mN.

**定义。** 两列或多列相干波叠加时产生**干涉**。对于间距为 d、波长 λ 垂直入射的双缝，路程差为 Δ = d sin θ。**相长干涉**（亮纹）出现在 d sin θ = mλ；**相消干涉**出现在 d sin θ = (m + ½)λ。**单缝衍射**强度包络为 I(θ) = I₀ sinc²(πa sin θ / λ)，其中 a 为缝宽。N 缝**衍射光栅**在 d sin θ = mλ 处产生尖锐主极大，分辨本领为 R = mN。

**Demonstration.** Double-slit experiment (Young, 1801): two slits, separation d = 0.1 mm, λ = 500 nm, screen at L = 1 m. Fringe spacing Δy = λL/d = 5 mm — directly measurable with a ruler. The same experiment performed one photon at a time still builds up the interference pattern, a key demonstration of wave–particle duality (Phase 3).

**演示。** 双缝实验（杨氏，1801 年）：双缝间距 d = 0.1 mm，λ = 500 nm，屏在 L = 1 m 处。条纹间距 Δy = λL/d = 5 mm——可直接用尺子测量。同样的实验逐个光子进行时，仍然形成干涉图样，这是波粒二象性（第 3 阶段）的关键演示。

**Application.** Diffraction is fundamentally a **Fourier phenomenon** (Module 0.5): the far-field (Fraunhofer) diffraction pattern of an aperture function f(x) is its Fourier transform F̃(k_x). The diffraction grating is a Fourier analyser of wavelengths; X-ray diffraction from crystals (Bragg's law: 2d sin θ = mλ) is Fourier analysis of the lattice, the basis of crystallography and protein structure determination. Interference also underlies interferometric sensors (LIGO gravitational wave detection) with sensitivity far below λ.

**应用。** 衍射从根本上是一种**傅里叶现象**（模块 0.5）：孔径函数 f(x) 的远场（夫琅禾费）衍射图样是其傅里叶变换 F̃(k_x)。衍射光栅是波长的傅里叶分析器；晶体的 X 射线衍射（布拉格定律：2d sin θ = mλ）是对晶格的傅里叶分析，是晶体学和蛋白质结构测定的基础。干涉还支撑着灵敏度远低于 λ 的干涉测量传感器（LIGO 引力波探测）。

---

**Self-test (blank page)**

1. State Snell's law and derive it using Huygens' principle. What is the critical angle for glass (n = 1.5) in air?
2. In a double-slit experiment with slit separation d and wavelength λ, find the angular positions of the first three bright fringes. How does fringe spacing change if d is halved?
3. Explain why single-slit diffraction produces a central maximum of width 2λ/a and progressively weaker subsidiary maxima. How is this pattern related to the Fourier transform of the aperture?
4. What is the resolving power of a diffraction grating, and what determines it? How does this relate to the Rayleigh criterion for angular resolution?

**自测（空白页）**

1. 陈述斯涅尔定律，并用惠更斯原理推导它。玻璃（n = 1.5）在空气中的临界角是多少？
2. 在缝间距为 d、波长为 λ 的双缝实验中，求前三个亮纹的角位置。如果 d 减半，条纹间距如何变化？
3. 解释为什么单缝衍射产生宽度为 2λ/a 的中央主极大和逐渐减弱的次极大。该图样与孔径的傅里叶变换有何关系？
4. 衍射光栅的分辨本领是多少，由什么决定？这与角分辨率的瑞利判据有何关系？

---

← Previous: [Module 1.11 — Electromagnetic Waves & Radiation](./module-1.11-em-waves-radiation.md) · [Phase 1 index](./README.md) · Next: [Module 1.13 — Special Relativity — Kinematics](./module-1.13-special-relativity-kinematics.md) →

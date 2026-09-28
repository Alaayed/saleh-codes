# Box Intersection (Slab Method)

Source: [Slab method (Wikipedia)](https://en.wikipedia.org/wiki/Slab_method). Notation follows the article. Works for **axis-aligned** boxes (AABB): every face is perpendicular to x, y or z.

## Idea

A slab is the region between two parallel planes. An AABB is the overlap of three slabs, one per axis. A ray is inside the box exactly when it is inside all three slabs at the same time, so find the $t$ interval the ray spends in each slab and intersect the three intervals.

## Box

$$ \mathbf{l} = (l_0, l_1, l_2), \qquad \mathbf{h} = (h_0, h_1, h_2) $$

- $l_i$: a float, the box's lowest coordinate along axis $i$ (0 = x, 1 = y, 2 = z). $\mathbf{l}$ is the min corner.
- $h_i$: a float, the box's highest coordinate along axis $i$. $\mathbf{h}$ is the max corner.
- Slab $i$ is everything with $l_i \le p_i \le h_i$.

Example: cube centred at $(0,0,5)$ with edge 2 has $\mathbf{l} = (-1,-1,4)$, $\mathbf{h} = (1,1,6)$.

## Ray

$$ \mathbf{p}(t) = \mathbf{o} + t\,\mathbf{r} $$

- $\mathbf{o} = (o_0, o_1, o_2)$: ray origin, `l.origin`.
- $\mathbf{r} = (r_0, r_1, r_2)$: ray direction, `l.vec`. Need not be unit length.
- $\mathbf{p}(t)$: the point on the ray at parameter $t$.

Solving for $t$, component by component (assuming every $r_i \ne 0$):

$$ t = \frac{\mathbf{p} - \mathbf{o}}{\mathbf{r}} $$

## Step 1: where the ray crosses each slab's two planes

$$ t_i^{\text{low}} = \frac{l_i - o_i}{r_i}, \qquad t_i^{\text{high}} = \frac{h_i - o_i}{r_i} $$

- $t_i^{\text{low}}$: the $t$ where the ray reaches the plane $p_i = l_i$.
- $t_i^{\text{high}}$: the $t$ where the ray reaches the plane $p_i = h_i$.

## Step 2: order them into entry and exit

$$ t_i^{\text{close}} = \min\{t_i^{\text{low}},\, t_i^{\text{high}}\}, \qquad t_i^{\text{far}} = \max\{t_i^{\text{low}},\, t_i^{\text{high}}\} $$

- $t_i^{\text{close}}$: when the ray enters slab $i$.
- $t_i^{\text{far}}$: when it leaves slab $i$.
- Needed because when $r_i < 0$ the ray travels toward decreasing coordinates and reaches the $h_i$ plane first. The ray is inside slab $i$ for $t \in [t_i^{\text{close}}, t_i^{\text{far}}]$.

## Step 3: intersect the three intervals

$$ t^{\text{close}} = \max_i \, t_i^{\text{close}}, \qquad t^{\text{far}} = \min_i \, t_i^{\text{far}} $$

- $t^{\text{close}}$: the last slab entry. Only after entering all three is the ray inside the box.
- $t^{\text{far}}$: the first slab exit. Leaving any one slab means leaving the box.

## Step 4: hit test

$$ \text{hit} \iff t^{\text{close}} \le t^{\text{far}} $$

If the intervals don't overlap, the ray leaves one slab before entering another: miss.

The sign of $t^{\text{close}}$ says where the box is:

| Case | Meaning | Return (ray tracer) |
|---|---|---|
| $t^{\text{far}} < \varepsilon$ | box is entirely behind the origin | `kMiss` |
| $t^{\text{close}} > \varepsilon$ | box is ahead | $t^{\text{close}}$ |
| $t^{\text{close}} \le \varepsilon < t^{\text{far}}$ | origin is inside the box (e.g. a shadow ray) | $t^{\text{far}}$ |

## Step 5: hit points

$$ \mathbf{p}^{\text{close}} = \mathbf{o} + t^{\text{close}}\,\mathbf{r}, \qquad \mathbf{p}^{\text{far}} = \mathbf{o} + t^{\text{far}}\,\mathbf{r} $$

- $\mathbf{p}^{\text{close}}$: where the ray enters the box.
- $\mathbf{p}^{\text{far}}$: where it exits.

## Special cases: $r_i = 0$

The ray is parallel to slab $i$'s planes. With IEEE 754 floats this needs no special branch:

- **Nonzero over zero** gives $\pm\infty$. If $o_i$ is inside the slab, $l_i - o_i < 0 < h_i - o_i$, so the interval becomes $[-\infty, +\infty]$: always inside, and it drops out of the max/min. If $o_i$ is outside, both ends get the same sign of infinity, the interval is empty, and Step 4 reports a miss.
- **Zero over zero** gives NaN. It happens when $o_i = l_i$ or $o_i = h_i$ exactly (origin on a face plane while parallel to it). IEEE minNum/maxNum treat NaN as missing and return the other value.
- **Alternative:** precompute the inverse $1/r_i$ once per ray and replace an infinite inverse with a large finite constant, which avoids dividing by zero at all.

**Practical notes for my code:**

- Zero components are the common case, not an edge case. Every parallel-projection ray is $(0, 0, 1)$, so $r_0 = r_1 = 0$ on every pixel.
- `Vec::operator/=` asserts every component is non-zero, so don't compute $t$ with Vec division. Do the three axes as plain floats.
- C++: `std::fmin` / `std::fmax` are minNum/maxNum (NaN treated as missing). `std::min` / `std::max` are not: `std::min(a, b)` is `(b < a) ? b : a`, so a NaN in the first argument is returned as-is.
- The oF build has no `-ffast-math`, so infinities and NaN behave as described.

## Normal (not in the article, needed for shading)

At a hit point $\mathbf{p}$, find the face it lies on: the axis $i$ and bound where $|p_i - l_i|$ or $|p_i - h_i|$ is smallest.

$$ \mathbf{n} = -\mathbf{e}_i \ \text{ if nearest to } l_i, \qquad \mathbf{n} = +\mathbf{e}_i \ \text{ if nearest to } h_i $$

- $\mathbf{e}_i$: the world unit axis, $(1,0,0)$, $(0,1,0)$ or $(0,0,1)$.
- Use the smallest distance rather than an exact equality test: $p_i$ is off by float error.

## Worked examples

Box $\mathbf{l} = (-1,-1,4)$, $\mathbf{h} = (1,1,6)$. Ray direction $\mathbf{r} = (0,0,1)$.

**Hit**, $\mathbf{o} = (0,0,0)$:

| Axis | $t^{\text{low}}$ | $t^{\text{high}}$ | close | far |
|---|---|---|---|---|
| x | $-1/0 = -\infty$ | $1/0 = +\infty$ | $-\infty$ | $+\infty$ |
| y | $-\infty$ | $+\infty$ | $-\infty$ | $+\infty$ |
| z | $4$ | $6$ | $4$ | $6$ |

$t^{\text{close}} = 4 \le t^{\text{far}} = 6$: hit at $t = 4$, the face $z = 4$, normal $(0,0,-1)$.

**Miss**, $\mathbf{o} = (2,0,0)$: x gives $t^{\text{low}} = -3/0 = -\infty$ and $t^{\text{high}} = -1/0 = -\infty$, so $t_x^{\text{far}} = -\infty$. Then $t^{\text{far}} = -\infty < t^{\text{close}}$: miss. The ray runs parallel to the x slab but outside it.

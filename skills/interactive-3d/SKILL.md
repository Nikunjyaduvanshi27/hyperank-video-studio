---
name: interactive-3d
description: Use when the user wants 3D, R3F, shaders, Spline, or a premium hero scene. Triggers on "3D", "three.js", "R3F", "react-three-fiber", "shader", "spline", "webgl", "glb", "scene", "interactive hero", "luxury product viz". Loads distilled R3F + Drei + WebGPU + shader recipes that pass Lighthouse 90+.
---

# interactive-3d

The R3F / shader / 3D pipeline skill. Fires only when the brief calls for 3D — never on default.

## When NOT to use 3D

- B2B SaaS landing where conversion matters — ship a video poster instead
- Mobile-first audience > 60% — 3D performance on mid-Android is risky
- Brand has no visual asset to anchor the scene — abstract 3D = generic
- Client paying < $3K — dev time will exceed budget

3D is a SIGNATURE moment, not decoration. One scene per page, max.

## The 2026 canonical stack

```
three@~r185 (current stable; WebGPURenderer production-ready since r171, TSL stable)
+ @react-three/fiber@9.7 + @react-three/drei@10.7
+ @react-three/postprocessing@3
+ leva (debug GUI) — strip from prod builds
+ three-mesh-bvh (raycast)
+ @gltf-transform/cli + gltfpack (compression)
```

Verify with Context7 before pinning: `mcp__plugin_context7_context7__query-docs` for "react-three-fiber".

## The performance commandments

| Target | Number |
|---|---|
| DPR cap | `<Canvas dpr={[1, 2]} />` — never raw `devicePixelRatio` |
| Draw calls | < 100 |
| Initial JS | < 170KB gzip (R3F is ~155KB three + ~30KB R3F + ~10KB drei tree-shaken) |
| Hero GLB | < 800KB after Draco + KTX2 |
| Total hero load | < 1.5MB |
| Lighthouse | 90+ desktop / 70+ mobile |
| `frameloop` | `"demand"` for static scenes, `"always"` only for active animations |

## The compression pipeline (mandatory)

```bash
# Raw GLB from Meshy/Tripo/Spline → optimized
npx @gltf-transform/cli optimize raw.glb step1.glb \
  --texture-compress webp --texture-size 1024 --simplify --simplify-ratio 0.5

# Draco + meshopt (90%+ size reduction)
npx gltfpack -i step1.glb -o final.glb -cc

# Verify
ls -lh final.glb  # target: < 800KB
```

## The Drei components worth knowing (premium signature moments)

| Component | Use for |
|---|---|
| `<View>` | Multiple 3D viewports inside DOM grid (product gallery) |
| `<MeshTransmissionMaterial>` | Refractive glass with chromatic aberration — THE premium look |
| `<Caustics>` | Raymarched light projection on a catcher plane (luxury water/glass) |
| `<Float>` | Idle motion on hero objects |
| `<ScrollControls>` + `useScroll` | Native scroll-progress (0-1) into 3D — primary scroll-3D pattern |
| `<Html>` | DOM overlays inside 3D space (occluding, transformed) |
| `<MeshReflectorMaterial>` | Floor reflections without rendertargets |
| `<Lightformer>` + `<Environment>` | Procedural studio HDRIs |
| `<AccumulativeShadows>` + `<ContactShadows>` | Baked-look soft shadows, cheap |

Use `<Bounds>` to auto-frame the camera on imported models.

## The 5 signature 3D recipes

### A. Glass product hero (Apple Vision Pro vibe)
`MeshTransmissionMaterial` + `Environment preset="studio"` + `Caustics` underneath. ~80 lines. Most premium look per byte.

### B. Scroll-driven camera (Awwwards canonical)
`<ScrollControls pages={3}>` + `useScroll().offset` → camera position lerp in `useFrame`. Pair with Lenis on the DOM side. See `~/.claude/assets/premium-web/satus/` for the orchestration pattern.

### C. Custom shader hero (Stripe gradient mesh)
Fullscreen quad + fragment shader using `lygia/generative/snoise` + 2-3 brand colors mixed. Live-reactive to scroll velocity via uniform. Reference: `~/.claude/assets/premium-web/lygia/` for shader functions.

### D. WebGL+HTML merged worlds (Yuri Artiukh)
DOM image → R3F plane via shared transform. Distortion shader on hover/scroll. Reference: `~/.claude/assets/premium-web/akella-exploding/`.

### E. Spline → R3F hybrid (designer-fast)
Design in Spline (free tier), export GLB, run through gltf-transform pipeline above, render via R3F `useGLTF`. Best when designer-led and React state must bind to scene.

## The Bruno Simon pattern (drivable world)

For full-bleed agency portfolios. Reference: `~/.claude/assets/premium-web/bruno-room/`. Stack: Three.js raw + Cannon/Rapier physics + GSAP camera + baked Blender textures. Skip if budget < 2 weeks of dev.

## Mobile fallback (mandatory)

Always ship `3d-fallback`:

```tsx
// Detect low-end / reduced-motion
const isLowEnd = (
  matchMedia('(prefers-reduced-motion: reduce)').matches ||
  navigator.hardwareConcurrency < 4 ||
  (navigator as any).deviceMemory < 4 ||
  matchMedia('(max-width: 768px)').matches
)

return isLowEnd 
  ? <Image src="/hero-poster.avif" alt="" priority className="..." />
  : <Suspense fallback={<HeroPoster />}><HeroScene /></Suspense>
```

## SSR + Next.js 16 gotcha

Canvas can't SSR. Always:
```tsx
const HeroScene = dynamic(() => import('./HeroScene'), { ssr: false, loading: () => <HeroPoster /> })
```
Mount via IntersectionObserver if not above the fold.

## WebGPU (2026)

`three/webgpu` import + `WebGPURenderer` — ~80-85% global browser support now (caniuse, mid-2026); Safari 26 added support, closing most of the gap. Firefox still ships it disabled by default over fingerprinting/driver-stability concerns, so a fallback is still required, not optional. Use `<Canvas gl={async (props) => { const r = new WebGPURenderer(props); await r.init(); return r }}/>` with automatic WebGL2 fallback. WebGPU is now a reasonable production default for a hero scene as long as the WebGL2 fallback path is actually tested, not just declared.

## What to extract from cloned repos (NEVER paste whole)

- `drei/` source — read component implementations to understand props/perf, never copy the source verbatim. Install from npm.
- `bruno-room/` — extract the baked-lighting workflow, not the model.
- `akella-exploding/` — extract the scroll-uniform-shader pattern, rewrite for the brand.
- `lygia/` — `import { snoise }` directly via the lygia/resolve.js or copy ONLY the function used.

## Output structure for a 3D build

1. Justify why 3D fits this brand (1 sentence)
2. Pick ONE recipe (A-E) + name it
3. List the assets needed: GLB / shader / HDRI / Lottie
4. Compression pipeline commands (gltfpack)
5. R3F scaffolding code with Suspense + fallback
6. Mobile fallback strategy

Content refreshed: 2026-08-13
7. Lighthouse target + plan to hit it

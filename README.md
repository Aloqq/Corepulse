# CorePulse — Dota 2 UPUP Community Wiki, Mechanics & Progression Tools 2026

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Dota 2 Custom Game](https://img.shields.io/badge/Dota%202-UPUP%20Custom%20Game-blue.svg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3259838038)
[![Official Website](https://img.shields.io/badge/CorePulse-Official%20Platform-orange.svg)](https://corepulse.su/)
[![Wiki Database](https://img.shields.io/badge/CorePulse-Dota%202%20UPUP%20Wiki-orange.svg)](https://corepulse.su/wiki/)
[![Active Promo Codes](https://img.shields.io/badge/Promo%20Codes-Verified%202026-brightgreen.svg)](https://corepulse.su/wiki/promo)

Open-source reference database, client-extracted mechanics, progression calculators, and active in-game promo codes for the Dota 2 custom game **Dota UpUp** (Dota 2 UPUP).

> 🌐 **Official Platform & Interactive Wiki:**  
> Complete interactive database with live talent simulators, corruption calculator, and weekly code updates:  
> **[https://corepulse.su/wiki/](https://corepulse.su/wiki/)**  
> Main Website: **[https://corepulse.su/](https://corepulse.su/)**

---

## 📌 Table of Contents
- [About Dota 2 UPUP](#-about-dota-2-upup)
- [Active In-Game Promo Codes (2026)](#-active-in-game-promo-codes-2026)
- [Corruption & Curse Mechanics](#-corruption--curse-mechanics)
- [Expeditions & Vault Scaling](#-expeditions--vault-scaling)
- [Automation & Helper Platform (CorePulse)](#-automation--helper-platform-corepulse)
- [Python Progression Calculator (`dota_upup_calculator.py`)](#-python-progression-calculator)
- [Repository Structure](#-repository-structure)
- [Contributing & License](#-contributing--license)

---

## 🎮 About Dota 2 UPUP

**Dota UpUp** is an idle-progression and rogue-lite RPG custom game in Dota 2. Players select heroes, equip randomized gear, roll cards with powerful synergistic modifiers, climb through ascending difficulty levels (1 to 16), and conquer the Corruption depths.

### Key Game Systems:
1. **Hero Cards & Synergies:** Tier 1 to Tier 5 cards that scale attributes, spell amplification, and attack speed.
2. **Expeditions (Vaults):** Offline and background resource gathering based on companion star tier.
3. **Corruption:** High-level endgame scaling where enemies gain escalating health and damage modifiers, rewarding rare souls.

---

## 🎁 Active In-Game Promo Codes (2026)

In Dota UpUp, promo codes are entered via the in-game UI:  
**Open Shop (top menu) → Click "Promo Code" button in the currency bar → Paste code → "Activate"**.

### Latest & Active Codes:

| Code | Type / Event | Status |
| :--- | :--- | :--- |
| `UPDATE15` | Latest Patch Release | ✅ Active |
| `HALLOWEEN` | Halloween Event Reward | ✅ Active |
| `UPDATE14` | Game Balance Update | ✅ Active |
| `MEGALODON` | Season Event Reward | ✅ Active |
| `SEASON4` | Season 4 Launch Code | ✅ Active |
| `TelegramUpUp` | Community Welcome Code | ✅ Active |
| `TI2026` | Championship Celebration | ✅ Active |
| `SEASON3` | Season 3 Code | ✅ Active |
| `AUTUMN` | Autumn Season Code | ✅ Active |
| `CRYSTAL` | Bonus Crystals | ✅ Active |

<details>
<summary><b>Click to expand full archive of all 36 codes</b></summary>

`WELCOME`, `NEWLAUNCH`, `OVERVODKA`, `TEST`, `BirzhaMemov`, `UPDATE`, `DUANWU`, `SORRY`, `SORRY2`, `STRANGERDEV`, `UPDATE2`, `UPDATE3`, `UPDATE4`, `UPDATE5`, `CRYSTAL`, `SEASON2`, `QQWELCOME`, `UPDATE6`, `INFINITY`, `THEINTERNATIONAL`, `UPDATE7`, `UPDATE8`, `TI2026`, `TelegramUpUp`, `AUTUMN`, `SEASON3`, `UPDATE9`, `UPDATE10`, `UPDATE11`, `UPDATE12`, `UPDATE13`, `SEASON4`, `MEGALODON`, `UPDATE14`, `HALLOWEEN`, `UPDATE15`
</details>

> 💡 **Need the newest codes immediately after patches?**  
> Check the continuously updated tracker on the web wiki:  
> 👉 **[CorePulse Dota 2 UPUP Promo Codes Hub](https://corepulse.su/wiki/promo)**

---

## 🧬 Corruption & Curse Mechanics

Corruption starts appearing past Difficulty 8. Each level introduces harsher map debuffs while multiplying soul harvest rates.

| Depth Level | Enemy HP Multiplier | Enemy Damage Multiplier | Soul Yield Multiplier | Recommended Gear Rating |
| :---: | :---: | :---: | :---: | :---: |
| **Depth 1–3** | `×1.85` | `×1.40` | `×1.50` | 1,200+ |
| **Depth 4–6** | `×3.20` | `×2.10` | `×2.75` | 2,800+ |
| **Depth 7–9** | `×6.50` | `×3.80` | `×5.20` | 5,500+ |
| **Depth 10+** | `×14.00` | `×7.20` | `×11.50` | 10,000+ |

Interactive formula simulator and curse penalty solver:  
👉 **[Dota 2 UPUP Corruption Guide & Tables](https://corepulse.su/wiki/corruption)**

---

## 🧭 Expeditions & Vault Scaling

Expeditions yield materials based on assigned companion rarity and tier:

- **1★ Companion:** Base duration `8h`, drop rate `1.0×`
- **2★ Companion:** Base duration `6.5h`, drop rate `1.4×`
- **3★ Companion:** Base duration `5.0h`, drop rate `2.0×`
- **4★ Companion:** Base duration `3.5h`, drop rate `3.1×`
- **5★ Companion:** Base duration `2.0h`, drop rate `5.0×` + Guaranteed Mythic Shard

Full expedition drop tables:  
👉 **[Dota 2 UPUP Expeditions Guide](https://corepulse.su/wiki/expeditions)**

---

## 🤖 Automation & Helper Platform (CorePulse)

For players looking to maximize farming efficiency 24/7 without burning out on repetitive runs:

* **[CorePulse](https://corepulse.su/)** provides automated card selection, hero progression, expedition routing, and inventory recycling for Dota 2 UPUP.
* **Key Features:**
  * Autonomous round advancement & card synergy selection.
  * Real-time hardware telemetry and external execution (no DLL injection, VAC-safe).
  * 24-hour free trial available upon registration.

🔗 Official Platform: **[https://corepulse.su/](https://corepulse.su/)**

---

## 🐍 Python Progression Calculator

We include a standalone CLI calculator script in this repository: [`dota_upup_calculator.py`](./dota_upup_calculator.py).

### How to Run:
```bash
python dota_upup_calculator.py
```

### Features:
1. Calculates effective soul farming rate across corruption depths.
2. Estimates optimal companion setup for maximum hourly expedition ROI.
3. Formats copy-pasteable in-game promo commands.

---

## 📂 Repository Structure

```text
├── README.md                  # Comprehensive game overview & guides
├── LICENSE                    # MIT License
├── .gitignore                 # Protection from accidental credential commits
├── dota_upup_calculator.py   # CLI calculator for farming & expeditions
└── data/
    ├── promocodes.json        # Verified in-game gift codes dataset
    ├── corruption_tiers.json  # Enemy scaling & soul multiplier matrix
    └── expeditions.json       # Companion drop tables & timer reduction
```

---

## 📄 License & Disclaimer

* This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for details.
* **Disclaimer:** *Dota 2* is a registered trademark of Valve Corporation. This project and CorePulse are community fan resources and are not affiliated with or endorsed by Valve Corporation or the creators of the Dota UpUp custom game.

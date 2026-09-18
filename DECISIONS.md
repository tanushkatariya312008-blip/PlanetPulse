# Architectural Decisions (DECISIONS.md)

**Hackathon ID:** AZIS-DCAH4A  
**Project:** PlanetPulse (Track 2)

---

### DP1: Target Breaches & User Motivation (The Nudge)
* **What we chose:** We decided against blocking the user or locking form submissions when their weekly carbon target is exceeded. Instead, the UI dynamically changes the progress bar to warning colors and triggers alert prompts.
* **Why:** In sustainability tracking, negative reinforcement fails. If a user is locked out after exceeding their limit, they simply abandon the tool. By keeping logging open while providing instant, high-contrast visual cues, we encourage honest accounting without punishing the user.

---

### DP2: Outlier & Absurd Input Defense
* **What we chose:** We set an explicit boundary cap rejecting individual activity entries exceeding 50,000 units.
* **Why:** Accidental typos (such as typing 500,000 km instead of 50 km) break the scaling of the progress bar, distort tree-offset calculations, and render category aggregations useless. Capping single-entry thresholds at 50,000 prevents data skewing right at the input layer without needing complex verification logic.

---

### DP3: Handling Time & Weekly Cycles (The Week)
* **What we chose:** A flexible running-total tracker with dynamic budget adjustments and an instant manual "Reset / Clear" option, rather than rigid Monday-to-Sunday cron lockouts.
* **Why:** Users evaluate habits across personal sprints rather than strict calendar cutoffs. A rigid calendar wipe causes confusion across timezones and punishes users who start midweek. Offering custom target editing combined with a single-click reset gives users full ownership over their monitoring cycles.
---
name: cycle-tracker
description: Track and predict menstrual cycles, fertile windows, and ovulation dates. Calculate cycle statistics, predict next period, identify fertile days, and provide phase-based health insights (follicular, ovulatory, luteal, menstrual phases). Use when someone wants to understand their cycle, plan around it, or track patterns over time. No API required — pure date calculation and cycle science.
license: MIT
metadata:
    skill-author: custom
---

# Cycle Tracker

Menstrual cycle prediction, fertile window calculation, and phase-based health insights.

---

## Core Concepts

### Cycle Phases

```
Phase 1 — Menstrual (Days 1–5, avg)
  Period bleeding. Day 1 = first day of full flow.
  Energy low, rest recommended.

Phase 2 — Follicular (Days 1–13, overlaps with menstrual)
  Estrogen rising. Energy and mood improving.
  Good for: starting new projects, social activity, exercise ramp-up.

Phase 3 — Ovulatory (Days 12–16, avg)
  LH surge triggers ovulation. Peak fertility.
  Energy and confidence peak.
  Fertile window: 5 days before ovulation + ovulation day.

Phase 4 — Luteal (Days 15–28, avg)
  Progesterone dominant. PMS symptoms may appear days 21–28.
  Good for: detail work, reflection, solo projects.
```

### Key Formulas

```
Cycle length = Day 1 of next period − Day 1 of current period

Ovulation estimate = Day 1 of NEXT period − 14 days
  (Luteal phase is ~14 days and relatively fixed)

Fertile window = Ovulation day − 5 days to ovulation day + 1
  (Sperm live 3–5 days; egg lives ~24 hours)

Next period = Last period start + avg_cycle_length

Average cycle length:
  Short: < 21 days
  Normal: 21–35 days (avg 28 days)
  Long: > 35 days
```

---

## Predictions

### Single Cycle Prediction

```
Input:
  Last period start: March 1
  Cycle length: 28 days

Output:
  Next period:    March 29
  Ovulation:      March 15 (March 29 − 14)
  Fertile window: March 10 – March 16

  Current phase (if today = March 5):
    Menstrual phase (Day 5)
    Period expected to end: ~March 5–7
```

### Multi-Cycle Analysis

Given 3+ past cycle start dates, calculate:

```
Cycle lengths: [28, 27, 29, 28, 30]
Average: 28.4 days
Shortest: 27 days
Longest: 30 days
Variability: ±1.5 days (regular)

→ Predict fertile window using both average AND shortest cycle:
  Conservative fertile window start = (shortest cycle − 18) days from period start
  Conservative fertile window end   = (longest cycle − 11) days from period start
```

Regularity classification:
```
±2 days  → Very regular
±3–4 days → Mostly regular
±5–7 days → Somewhat irregular
> 7 days  → Irregular — recommend tracking more cycles
```

---

## Phase-Based Insights

### Menstrual Phase (Days 1–5)
- **Body**: Uterine lining shedding, estrogen and progesterone low
- **Common symptoms**: Cramps, fatigue, lower back pain, mood dips
- **Tips**: Rest, warm compress, iron-rich foods, light yoga/walking
- **Exercise**: Low intensity — walking, stretching, gentle yoga

### Follicular Phase (Days 6–13)
- **Body**: Estrogen rising, follicles maturing
- **Common symptoms**: Rising energy, improved mood, clearer skin
- **Tips**: Great time for strength training, learning new skills, social plans
- **Exercise**: Cardio, HIIT, weightlifting — body recovers faster

### Ovulatory Phase (Days 12–16)
- **Body**: LH surge, egg released, estrogen peaks
- **Common symptoms**: Slight cramping (mittelschmerz), increased libido, cervical mucus changes
- **Tips**: Peak cognitive and physical performance window
- **Fertility**: Highest fertility; use contraception or plan conception accordingly

### Luteal Phase (Days 15–28)
- **Body**: Progesterone dominant, preparing for possible implantation
- **Common symptoms (days 21–28)**: PMS — bloating, breast tenderness, mood changes, food cravings, fatigue
- **Tips**: Prioritize sleep, reduce caffeine/salt/sugar, magnesium may help PMS
- **Exercise**: Moderate — body temperature slightly elevated, adjust intensity

---

## Usage Examples

### Basic Prediction

```
Input:
  "My last period started February 10. My cycles are usually 29 days."

Output:
  Next period:    March 11
  Ovulation:      February 25
  Fertile window: February 20 – February 26

  Today is Day X of your cycle.
  Current phase: [calculated from today's date]
```

### Tracking Multiple Cycles

```
Input:
  Period start dates: Jan 3, Jan 31, Feb 27, Mar 26

Output:
  Cycle lengths: 28, 27, 27
  Average: 27.3 days
  Regularity: Very regular (±0.5 days)

  Next period:    April 22
  Ovulation:      April 8
  Fertile window: April 3 – April 9
```

### Irregular Cycle Help

```
Input:
  "My cycles vary between 25–35 days."

Output:
  Conservative fertile window: Days 7–24 of your cycle
  (Wide window due to irregular cycles)

  Recommendation: Track basal body temperature (BBT) or
  use ovulation predictor kits (OPKs) for more accuracy.
  Consider logging 3+ cycles to find your pattern.
```

---

## Interaction Patterns

When triggered, ask:
1. "When did your last period start? (Day 1 = first day of full flow)"
2. "How long is your typical cycle? (Day 1 to Day 1 of next period)"
3. "Are you tracking for: period prediction / fertile window / understanding symptoms / general health?"

Then provide:
- Next period date
- Ovulation estimate
- Fertile window
- Current cycle day and phase (if today's date is known)
- Relevant phase tips based on goal

---

## Important Notes & Disclaimers

- These are **estimates** based on average cycle patterns
- Individual cycles vary due to stress, illness, travel, weight changes
- **This is NOT a contraceptive method** — the fertility awareness method alone has a 24% typical-use failure rate
- For contraception, use medical-grade methods
- Cycle irregularities (very short, very long, or absent periods) may warrant medical evaluation
- Symptoms that are severe or disruptive (heavy bleeding, extreme pain) should be discussed with a gynecologist
- Not a substitute for medical advice — consult a healthcare provider for reproductive health concerns

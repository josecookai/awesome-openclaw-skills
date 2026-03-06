---
name: quit-tracker
description: Track progress quitting any habit (smoking, vaping, alcohol, sugar, social media, etc.), calculate health milestones and money saved, provide motivational context based on elapsed quit time, and offer evidence-based craving management strategies. Use when someone wants to quit a habit, track their progress, or get support during cravings. No API required — pure calculation and behavioral science.
license: MIT
metadata:
    skill-author: custom
---

# Quit Tracker

Track habit quitting progress: time elapsed, health milestones, money saved, craving management.

---

## Quit Calculations

### Basic Progress

```
time_quit    = now − quit_datetime
hours_quit   = time_quit in hours
days_quit    = time_quit in days
months_quit  = days_quit / 30.44
years_quit   = days_quit / 365.25
```

### Money Saved (Smoking / Vaping)

```
cost_per_day      = (units_per_day × cost_per_unit)
money_saved       = cost_per_day × days_quit

Common unit costs (adjust to user's local prices):
  Cigarette pack:    $8–15 / pack (20 cigarettes)
  Vape pod:          $4–8 / pod (~200 puffs)
  Alcohol (drink):   $5–15 / drink

money_saved_monthly = cost_per_day × 30
money_saved_yearly  = cost_per_day × 365

"What you could buy instead" framing:
  $50   = dinner out
  $200  = concert tickets
  $500  = weekend trip
  $1000 = new phone
  $3000 = vacation
```

### Units Avoided

```
units_avoided = units_per_day × days_quit

For cigarettes:
  cigarettes_avoided = cigarettes_per_day × days_quit
  packs_avoided = cigarettes_avoided / 20

For alcohol:
  drinks_avoided = drinks_per_day × days_quit

Framing: "That's X packs of cigarettes you did NOT smoke"
```

---

## Health Milestones (Smoking)

Evidence-based recovery timeline:

```
20 minutes:
  Heart rate and blood pressure drop toward normal.

8 hours:
  Carbon monoxide level in blood drops to normal.
  Oxygen levels return to normal.

24 hours:
  Heart attack risk begins to decrease.

48 hours:
  Nerve endings start to regrow.
  Sense of smell and taste begin to improve.

72 hours (3 days):
  Nicotine fully cleared from body.
  Lung bronchial tubes relax — breathing becomes easier.
  Energy levels begin to increase.

2–12 weeks:
  Circulation improves.
  Walking and exercise become easier.
  Lung function increases by up to 30%.

1–9 months:
  Coughing and shortness of breath decrease.
  Cilia regrow in lungs — better at clearing mucus.
  Energy increases significantly.

1 year:
  Risk of coronary heart disease is half that of a smoker.

5 years:
  Stroke risk reduced to same as non-smoker.
  Mouth, throat, esophagus, and bladder cancer risk halved.

10 years:
  Lung cancer death rate about half that of a continuing smoker.
  Cancer risk of mouth, throat, esophagus, bladder, kidney halved.

15 years:
  Risk of coronary heart disease same as a non-smoker.
```

### Health Milestones (Alcohol)

```
24 hours:  Blood sugar stabilizes, sleep quality begins improving.
72 hours:  Hydration improves, headaches subside.
1 week:    Better sleep quality, clearer skin, weight loss begins.
2 weeks:   Liver begins recovering, blood pressure improves.
1 month:   Significant liver fat reduction, immune system stronger.
3 months:  Memory and concentration improve, energy up.
6 months:  Liver almost fully recovered (if no cirrhosis).
1 year:    Heart disease risk decreasing, sustained mood improvement.
```

### Health Milestones (Sugar / Processed Food)

```
3 days:   Sugar cravings peak, then begin to subside.
1 week:   Energy more stable (no more sugar crashes).
2 weeks:  Clearer skin, less bloating.
1 month:  Weight loss, reduced inflammation markers.
3 months: Insulin sensitivity improved, mood more stable.
```

---

## Craving Management

### Craving Science

```
Duration:    Most cravings peak and pass in 3–5 minutes.
Trigger:     Usually linked to a cue (place, emotion, person, time)
Frequency:   Intense at start, decreasing over weeks

The 5D Method:
  Delay   — Wait 5 minutes (craving will pass)
  Distract — Change activity, location
  Drink water — Hydrate; often mistaken for craving
  Deep breathe — 4-7-8 breathing calms the urge
  Discuss — Tell someone, use accountability
```

### 4-7-8 Breathing

```
Inhale through nose:    4 seconds
Hold breath:            7 seconds
Exhale through mouth:   8 seconds
Repeat:                 3–4 cycles

Activates parasympathetic nervous system.
Reduces acute craving intensity in ~2 minutes.
```

### Trigger Identification & Management

```
Common triggers:
  S — Stress (work pressure, arguments)
  T — Times of day (morning coffee, after meals)
  A — Alcohol / social situations
  R — Routines (smoke break times, commute)

For each trigger, plan a replacement behavior:
  Stress → 5-minute walk, breathing, cold water
  After meals → Tea, gum, fruit, short walk
  Social pressure → "No thanks, I quit" (rehearse it)
  Boredom → Keep hands busy, call someone
```

### Nicotine Withdrawal Timeline

```
Day 1–3:   Peak withdrawal — irritability, anxiety, difficulty concentrating
Day 4–7:   Intense cravings continue but begin to decrease
Week 2:    Physical symptoms easing, psychological cravings remain
Month 1:   Most physical withdrawal resolved
Month 3:   Cravings rare and brief
Month 6+:  Occasional cravings, easily managed
```

---

## Relapse Support

```
A slip ≠ a failure. A slip is data.

If relapsed:
  1. Don't catastrophize: "One cigarette ≠ smoker again"
  2. Identify what triggered it
  3. Set new quit date (today, not someday)
  4. Adjust your plan to handle that trigger next time

Relapse rates are normal:
  Most people attempt to quit 8–10 times before long-term success.
  Each attempt teaches something.
  Relapse does not erase progress — your body has already healed.
```

---

## Usage Examples

### Progress Check-In

```
Input:
  "I quit smoking 47 days ago. I smoked 10 cigarettes a day,
   cost $12 per pack."

Output:
  QUIT PROGRESS — Day 47
  ======================
  Time quit: 47 days, 0 hours

  HEALTH MILESTONES REACHED:
  [x] 20 minutes — Heart rate normalized
  [x] 8 hours   — CO levels normal
  [x] 24 hours  — Heart attack risk dropping
  [x] 48 hours  — Taste/smell improving
  [x] 72 hours  — Nicotine cleared, lungs relaxing
  [x] 2 weeks   — Circulation improving
  [ ] 1 month   — Coming in 13 days!

  NEXT MILESTONE: 1 month (Day 60)
    Coughing decreasing, lung function +30%

  MONEY SAVED:
  Cigarettes avoided: 470 cigarettes (23.5 packs)
  Money saved: $141
  Yearly pace: $1,095/year

  You could spend that on: A 3-day weekend trip.
```

### Craving SOS

```
Input: "I'm really craving a cigarette right now."

Output:
  You can do this. The craving will peak and pass in 3–5 minutes.

  RIGHT NOW — try this:

  1. Set a 5-minute timer. Just delay.

  2. Try 4-7-8 breathing:
     Breathe in... (4 seconds)
     Hold... (7 seconds)
     Breathe out slowly... (8 seconds)
     Repeat 3 times.

  3. Drink a full glass of cold water.

  4. Change your location — go to a different room or step outside.

  What triggered this craving? (stress / boredom / habit / social?)

  [Continues with trigger-specific strategy]
```

### Setting Up a Quit Plan

```
Input: "I want to quit vaping. I use about 1 pod per day at $6 each."

Output:
  QUIT PLAN — Vaping
  ==================

  Your quit date: [today or user-chosen date]

  Your numbers:
    Daily cost: $6/day
    Weekly: $42 | Monthly: $182 | Yearly: $2,190

  Week 1 goals (hardest week):
    - Remove all vapes and pods from your space
    - Tell 1 person you're quitting (accountability)
    - Plan responses to 3 likely trigger situations
    - Keep gum/snacks/water nearby for cravings

  Milestones to look forward to:
    Day 3:  $18 saved, nicotine cleared
    Day 7:  $42 saved, breathing easier
    Day 30: $180 saved, cravings rare
    Day 90: $540 saved, habit broken

  When a craving hits: [5D method]
```

---

## Interaction Patterns

When triggered, ask:
1. "What habit are you quitting?"
2. "When did you quit (or when do you want to quit)?"
3. "How much did you use per day and what was the cost?"

For progress check: Calculate and display milestones + money saved + next milestone.
For craving support: Immediate coping tools first, then trigger identification.
For relapse: Non-judgmental, reframe, new quit date, learn from trigger.

Always:
- Lead with progress and wins, not guilt
- Make next milestone feel close and achievable
- Keep craving tools concrete and immediate (3–5 minute horizon)

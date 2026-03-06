---
name: symptom-advisor
description: Analyze reported symptoms and provide structured health guidance — possible conditions to consider, urgency level (self-care / doctor visit / urgent care / ER), and when to seek care. Use when someone describes symptoms and wants to understand what might be happening and whether/how urgently to seek medical care. Always includes appropriate medical disclaimers. Not a diagnostic tool — a triage aid.
license: MIT
metadata:
    skill-author: custom
---

# Symptom Advisor

Structured symptom triage: understand what symptoms may indicate and when to seek care.

**THIS IS NOT A MEDICAL DIAGNOSTIC TOOL.**
Always recommend professional medical evaluation for any health concern.

---

## Core Framework

### Step 1 — Symptom Intake

Gather:
```
1. Primary symptom (what's the main complaint?)
2. Duration (how long?)
3. Severity (1–10 scale, or mild/moderate/severe)
4. Location (if applicable — where in body?)
5. Associated symptoms (what else?)
6. Relevant history (known conditions, medications, allergies)
7. Onset pattern (sudden vs gradual?)
8. Aggravating/relieving factors
9. Age and biological sex (affects differential)
```

### Step 2 — Red Flag Screening (PRIORITY CHECK)

Always screen for these before anything else:

```
CALL 911 / GO TO ER IMMEDIATELY if:
  [ ] Chest pain or pressure (especially with arm/jaw pain, sweating)
  [ ] Difficulty breathing / shortness of breath at rest
  [ ] Sudden severe headache ("worst headache of my life")
  [ ] Stroke signs: Face drooping, Arm weakness, Speech difficulty (FAST)
  [ ] Uncontrolled bleeding
  [ ] Loss of consciousness or confusion
  [ ] Severe allergic reaction (throat swelling, hives + breathing difficulty)
  [ ] Suspected poisoning or overdose
  [ ] Severe abdominal pain (especially right lower quadrant — appendicitis)
  [ ] High fever (>39.5°C / 103°F) with stiff neck or rash
  [ ] Suicidal thoughts or self-harm
```

### Step 3 — Urgency Classification

```
Level 1 — EMERGENCY (ER now)
  Life-threatening symptoms. Don't wait.

Level 2 — URGENT (Urgent care / doctor same day)
  Worsening symptoms, high fever, significant pain,
  symptoms lasting > 3 days without improvement.

Level 3 — SEE DOCTOR (Within 1–3 days)
  Non-emergency but needs professional evaluation.
  Recurring symptoms, new onset, affecting daily life.

Level 4 — MONITOR / SELF-CARE (Watch and wait)
  Common, self-limiting conditions with clear cause.
  Mild cold, minor cut, mild headache after screen time.
  Improve with rest/OTC treatment within expected timeframe.
```

---

## Common Symptom Patterns

### Headache

```
Tension headache (Level 4):
  Bilateral, pressure/band-like, mild-moderate
  Triggers: stress, screen time, posture
  Relief: OTC pain reliever, rest, hydration

Migraine (Level 3–4):
  Unilateral, throbbing, moderate-severe
  May include: nausea, light/sound sensitivity, aura
  Relief: dark/quiet room, migraine medication, sleep

RED FLAGS → ER:
  "Thunderclap" (sudden severe onset)
  First-ever severe headache
  Headache + fever + stiff neck (meningitis)
  Headache + confusion, vision changes, weakness
  Post-head injury headache
```

### Fever

```
Low-grade (37.5–38.0°C / 99.5–100.4°F):
  Usually viral. Rest, fluids, monitor.

Moderate (38.1–39.0°C / 100.5–102.2°F):
  Likely infection. OTC fever reducers.
  See doctor if: lasts > 3 days, or has source symptoms.

High (39.1–40.0°C / 102.3–104°F):
  See doctor today.

Very high (> 40°C / 104°F):
  Urgent care / ER — especially in elderly or immunocompromised.

Fever in specific groups:
  Infant < 3 months ANY fever → ER immediately
  Infant 3–6 months fever > 38.3°C → doctor same day
  Immunocompromised adult → lower threshold to seek care
```

### Chest Pain / Discomfort

```
ALWAYS take chest pain seriously.

Possible cardiac (ER NOW):
  Pressure, squeezing, crushing sensation
  Pain radiating to arm, jaw, neck, back
  Associated: sweating, nausea, shortness of breath
  Risk factors: age > 40, smoking, hypertension, diabetes

Possible musculoskeletal (Level 3–4):
  Sharp, localized, reproducible with palpation or movement
  Worsened by specific positions
  Recent physical strain

Possible acid reflux (Level 4):
  Burning sensation, worse after meals or lying down
  Relieved by antacids

Rule: When in doubt, chest pain = ER.
```

### Abdominal Pain

```
Location guides differential:

Right upper: Liver, gallbladder (gallstones → doctor/urgent)
Left upper:  Stomach, spleen, pancreas
Right lower: Appendix (sudden, worsening → ER), ovary (women)
Left lower:  Colon (diverticulitis), ovary (women)
Central:     Stomach, small intestine, early appendicitis
Generalized: Many causes — assess severity and duration

RED FLAGS:
  Sudden severe pain → ER
  Rigid/board-like abdomen → ER
  Pain + fever + vomiting → Urgent
  Pain in pregnancy → Urgent
```

### Respiratory Symptoms

```
Common cold (Level 4):
  Runny nose, sore throat, mild cough, low-grade fever
  Duration: 7–10 days
  Self-care: rest, fluids, OTC symptom relief

Flu (Level 3–4):
  Sudden onset, high fever, body aches, fatigue, dry cough
  At-risk groups (elderly, immunocompromised): antiviral within 48h

Seek care if:
  Difficulty breathing or shortness of breath
  Chest pain or pressure
  Persistent fever > 3 days
  Symptoms improve then suddenly worsen
  O2 saturation < 95% (if measurable)
```

---

## Output Format

For every symptom query, provide:

```
SYMPTOM SUMMARY
---------------
Reported: [symptoms]
Duration: X days
Severity: X/10

URGENCY LEVEL: [EMERGENCY / URGENT / SEE DOCTOR / SELF-CARE]

WHAT THIS MIGHT BE
------------------
Most likely: [common, benign explanation]
Also consider: [2–3 other possibilities if relevant]
Less likely but important to rule out: [if red flags present]

RECOMMENDED ACTION
------------------
[Specific, actionable guidance]

IF SYMPTOMS WORSEN OR YOU DEVELOP ANY OF THESE, SEEK IMMEDIATE CARE:
[List specific warning signs relevant to this case]

SELF-CARE MEASURES (if Level 3–4)
-----------------------------------
[Practical home management tips]

---
DISCLAIMER: This is informational guidance only, not a medical diagnosis.
Always consult a qualified healthcare provider for medical concerns.
```

---

## Special Populations (Always Note)

```
Seek care sooner / lower threshold for:
  - Infants and young children
  - Elderly (65+)
  - Pregnant women
  - Immunocompromised (cancer treatment, HIV, organ transplant)
  - Chronic conditions (diabetes, heart disease, COPD)
```

---

## Interaction Patterns

1. Ask for primary symptom first
2. Run red flag screen — if any present, escalate immediately to ER recommendation
3. Gather full symptom picture (duration, severity, associated symptoms)
4. Classify urgency level
5. Provide structured output above
6. Always end with clear escalation criteria ("if X happens, go to ER")

Never:
- Diagnose definitively
- Prescribe or recommend specific prescription medications
- Discourage someone from seeking care they want to seek
- Minimize symptoms that concern the person

Always:
- Err on the side of caution
- Acknowledge the limits of remote/AI assessment
- Recommend professional evaluation when any doubt exists

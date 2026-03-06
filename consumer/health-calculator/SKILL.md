---
name: health-calculator
description: Calculate and interpret key health metrics including BMI, BMR (basal metabolic rate), TDEE (daily calorie needs), body fat percentage, ideal weight range, hydration needs, and macronutrient targets. Use when someone wants to understand their health numbers, set weight/fitness goals, or calculate calorie and nutrition targets. No API required — pure evidence-based formulas.
license: MIT
metadata:
    skill-author: custom
---

# Health Calculator

Evidence-based health metrics: BMI, calories, macros, hydration, ideal weight.

---

## Metrics & Formulas

### 1. BMI (Body Mass Index)

```
BMI = weight_kg / height_m²
    = (weight_lb × 703) / height_in²

Classification (WHO):
  < 18.5   Underweight
  18.5–24.9 Normal weight
  25.0–29.9 Overweight
  30.0–34.9 Obese Class I
  35.0–39.9 Obese Class II
  ≥ 40.0   Obese Class III

Limitations: BMI does not distinguish muscle from fat.
For athletes or elderly, interpret with caution.
```

### 2. BMR (Basal Metabolic Rate)

Mifflin-St Jeor Equation (most accurate for general population):

```
Male:   BMR = 10 × weight_kg + 6.25 × height_cm − 5 × age + 5
Female: BMR = 10 × weight_kg + 6.25 × height_cm − 5 × age − 161
```

### 3. TDEE (Total Daily Energy Expenditure)

```
TDEE = BMR × activity_multiplier

Activity multipliers:
  1.2   Sedentary (desk job, no exercise)
  1.375 Lightly active (1–3 days/week exercise)
  1.55  Moderately active (3–5 days/week)
  1.725 Very active (6–7 days/week hard exercise)
  1.9   Extra active (physical job + daily training)
```

### 4. Calorie Targets by Goal

```
Maintain weight:  TDEE
Lose weight:      TDEE − 500 kcal/day  → ~0.5 kg/week loss
Lose fast:        TDEE − 750 kcal/day  → ~0.75 kg/week loss
Gain muscle:      TDEE + 300 kcal/day  → lean bulk

Minimum floors (never go below):
  Women: 1,200 kcal/day
  Men:   1,500 kcal/day
```

### 5. Macronutrient Targets

```
Protein:
  General health:     0.8 g / kg body weight
  Active / fitness:   1.6–2.2 g / kg body weight
  Weight loss:        2.0–2.4 g / kg (preserve muscle)

Fat:       20–35% of total calories  (1g fat = 9 kcal)
Carbs:     remaining calories        (1g carb = 4 kcal)
Protein:   per target above          (1g protein = 4 kcal)
```

### 6. Ideal Weight Range (Devine Formula)

```
Male:   IBW = 50 kg + 2.3 kg × (height_in − 60)
Female: IBW = 45.5 kg + 2.3 kg × (height_in − 60)
Range: IBW ± 10%

Note: Hamwi formula gives similar results.
Healthy range is better than single "ideal" number.
```

### 7. Body Fat % Estimation (Navy Method)

```
Male:
  BF% = 495 / (1.0324 − 0.19077 × log10(waist − neck) + 0.15456 × log10(height)) − 450

Female:
  BF% = 495 / (1.29579 − 0.35004 × log10(waist + hip − neck) + 0.22100 × log10(height)) − 450

All measurements in cm.

Healthy body fat ranges:
         Male        Female
Athlete: 6–13%       14–20%
Fit:     14–17%      21–24%
Average: 18–24%      25–31%
Obese:   ≥25%        ≥32%
```

### 8. Daily Water Intake

```
Base:       35 mL × weight_kg
Exercise:   + 500 mL per hour of exercise
Hot climate: + 500 mL/day

Simple rule: weight_kg × 0.033 = liters/day
```

### 9. Waist-to-Height Ratio (WtHR)

```
WtHR = waist_cm / height_cm

Healthy: < 0.50
At risk: 0.50–0.59
High risk: ≥ 0.60

Better cardiovascular risk predictor than BMI alone.
```

---

## Usage Examples

### Complete Health Profile

```
Input:
  Age: 32, Female
  Height: 165 cm
  Weight: 68 kg
  Activity: Moderately active (3-5x/week)
  Goal: Lose weight

Output:
  BMI: 25.0 (borderline overweight)
  BMR: 1,466 kcal/day
  TDEE: 2,272 kcal/day

  To lose ~0.5 kg/week: 1,772 kcal/day

  Macros (1,772 kcal):
    Protein: 122g (27%) — 2.0g/kg for weight loss
    Fat:     59g  (30%)
    Carbs:   199g (43%)

  Water: 2.4 L/day
  Ideal weight range: 55–67 kg (Devine ± 10%)
```

### Quick BMI Check

```
Input: 80 kg, 175 cm
Output: BMI = 26.1 → Overweight
        Healthy range for your height: 57–79 kg
```

---

## Interaction Patterns

Required inputs:
- Age, biological sex (for BMR formula)
- Height, weight (metric or imperial — auto-convert)
- Activity level (offer options)
- Goal (maintain / lose / gain)

Optional inputs for fuller picture:
- Waist, neck, hip measurements (body fat %)
- Exercise frequency/intensity

Always:
1. Show the calculated numbers with the classification
2. Set realistic expectations (e.g., "0.5 kg/week is sustainable")
3. Add brief health context, not just numbers
4. Include disclaimer: "These are estimates. Consult a healthcare provider for medical advice."

---

## Important Notes & Disclaimers

- All formulas are population-level estimates with ±10–15% individual variance
- BMI is not accurate for: athletes, bodybuilders, pregnant women, elderly
- Calorie targets are starting points — adjust based on real-world results after 2–3 weeks
- **Never recommend below 1,200 kcal (women) or 1,500 kcal (men)**
- For medical conditions (diabetes, kidney disease, eating disorders), always defer to a healthcare provider

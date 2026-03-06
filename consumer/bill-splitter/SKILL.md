---
name: bill-splitter
description: Split bills, calculate tips, and settle group expenses fairly. Use when splitting restaurant bills, group trips, shared purchases, or any shared expense among multiple people. Handles unequal splits, custom percentages, tip calculation, currency rounding, and debt simplification (who pays whom). No API required — pure calculation.
license: MIT
metadata:
    skill-author: custom
---

# Bill Splitter & Tip Calculator

Split any shared expense fairly. Handles tips, unequal splits, and multi-person debt settlement.

## Core Capabilities

- Restaurant bill splitting with tip
- Unequal splits (by percentage, ratio, or custom amount)
- Group trip / multi-expense settlement
- Debt simplification (minimize number of transactions)
- Multi-currency rounding

---

## Formulas

### Tip Calculation

```
tip_amount     = bill_subtotal × tip_rate
total_bill     = bill_subtotal + tip_amount
per_person     = total_bill / num_people

# Suggested tip rates
10% = minimal / poor service
15% = standard
18% = good service (US default)
20% = great service
25% = exceptional
```

### Equal Split

```
each_owes = (subtotal + tip) / n_people
```

### Unequal Split by Item

```
person_share = sum(person_items) / subtotal × (subtotal + tip)
```

### Debt Simplification Algorithm

Given a list of balances (positive = owed to person, negative = person owes):

```
1. Sort by balance descending
2. Match largest creditor with largest debtor
3. Transfer min(|creditor|, |debtor|) amount
4. Repeat until all balances zero
→ Result: minimum number of transactions
```

---

## Usage Examples

### Basic Restaurant Split

```
Input:
  Subtotal: $120
  Tip: 18%
  People: 4 (equal split)

Output:
  Tip: $21.60
  Total: $141.60
  Each pays: $35.40
```

### Unequal Split by Items

```
Input:
  Alice ordered: $45
  Bob ordered: $30
  Carol ordered: $25
  Tip: 20%
  Tax: 8.5%

Output:
  Subtotal: $100
  Tax: $8.50
  Tip: $20.00
  Total: $128.50
  Alice pays: $57.83 (45% of total)
  Bob pays: $38.55 (30%)
  Carol pays: $32.12 (25%)
```

### Group Trip Settlement

```
Input:
  Alice paid hotel: $300
  Bob paid dinner: $120
  Carol paid transport: $60
  3 people, equal share

Output:
  Total: $480
  Each owes: $160

  Balances:
    Alice: +$140 (paid $300, owes $160)
    Bob:   -$40  (paid $120, owes $160)
    Carol: -$100 (paid $60, owes $160)

  Settlements (simplified):
    Carol → Alice: $100
    Bob   → Alice: $40
```

---

## Interaction Patterns

When user provides a bill, always:
1. Confirm subtotal, tip preference, and number of people
2. Ask if split is equal or by item
3. Show breakdown: subtotal / tip / tax / total / per-person
4. For group settlements: show balance sheet + simplified payment instructions
5. Round to 2 decimal places; handle rounding remainder (assign to first person or largest share)

### Clarifying Questions to Ask

- "Is this an equal split or by what each person ordered?"
- "What tip percentage? (15% / 18% / 20% / custom)"
- "Is tax already included in the total, or should I add it?"
- "Do you want me to minimize the number of transactions?"

---

## Edge Cases

| Situation | Handling |
|-----------|----------|
| Rounding remainder ($0.01) | Add to person with largest share |
| Someone doesn't drink alcohol | Exclude from alcohol items, split food equally |
| Couples sharing one plate | Treat couple as one unit, then halve their share |
| Someone already paid | Deduct from their balance |
| Different currencies | Convert first, then split; note exchange rate used |

---

## Output Format

Always present results in a clear table:

```
BILL SUMMARY
------------
Subtotal:        $XX.XX
Tip (18%):       $XX.XX
Tax (if any):    $XX.XX
TOTAL:           $XX.XX

EACH PERSON PAYS
----------------
Alice:   $XX.XX
Bob:     $XX.XX
Carol:   $XX.XX

PAYMENT INSTRUCTIONS
--------------------
Bob pays Alice:   $XX.XX
Carol pays Alice: $XX.XX
```

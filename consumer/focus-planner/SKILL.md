---
name: focus-planner
description: Plan deep focus sessions using Pomodoro technique, build daily schedules, estimate task durations, track habits, and beat procrastination. Use when someone needs help structuring their work day, planning a focus session, breaking down overwhelming tasks, or building a sustainable habit system. No API required — pure planning logic and behavioral science.
license: MIT
metadata:
    skill-author: custom
---

# Focus Planner

Pomodoro sessions, task breakdown, habit tracking, and anti-procrastination strategies.

---

## Core Techniques

### Pomodoro Technique

```
Standard:
  Work:  25 minutes (1 Pomodoro)
  Break: 5 minutes
  After 4 Pomodoros: 15–30 minute long break

Modified versions:
  Deep work (90/20):  90 min work, 20 min break
  Micro (15/5):       15 min work, 5 min break (for high-distraction days)
  Flow (52/17):       52 min work, 17 min break (DeskTime research optimal)

Choose based on task type and energy level.
```

### Task Time Estimation

```
Hofstadter's Law: Things always take longer than expected,
even when accounting for Hofstadter's Law.

Estimation method (Planning Poker-style):
  1. Gut estimate (X minutes)
  2. Multiply by 1.5× for familiar tasks
  3. Multiply by 2.5× for unfamiliar tasks
  4. Add 20% buffer for interruptions

Pomodoro count:
  task_pomodoros = ceil(estimated_minutes / 25)
```

### Task Breakdown (MIT Method)

```
MIT = Most Important Tasks (max 3 per day)

Daily structure:
  Morning (peak energy): 2–3 MITs (deep work)
  Afternoon:             Meetings, emails, admin
  End of day:            Review, plan tomorrow

Rule of 2 minutes: If task < 2 min, do it now.
Rule of breaking down: If task > 2 hours, break it into subtasks.
```

---

## Planning Frameworks

### Daily Focus Plan

```
Input: Task list + available time + energy level

Output format:
  TODAY'S PLAN — [Date]
  ==================
  Energy level: [High/Medium/Low]
  Available hours: X

  MUST DO (MITs):
  [ ] Task 1 — Est: 2 Pomodoros (50 min)
  [ ] Task 2 — Est: 3 Pomodoros (75 min)
  [ ] Task 3 — Est: 1 Pomodoro (25 min)

  SCHEDULE:
  9:00–9:25   Pomodoro 1: Task 1
  9:25–9:30   Break
  9:30–9:55   Pomodoro 2: Task 1
  9:55–10:00  Break
  10:00–10:25 Pomodoro 3: Task 2
  ...

  BUFFER: 30 min (unscheduled)
  TOTAL FOCUSED TIME: X hours
```

### Weekly Sprint Plan

```
Sunday review → set 3 weekly goals → break into daily tasks

Weekly goals (max 3):
  Goal 1: [Outcome-based, not activity-based]
  Goal 2:
  Goal 3:

Daily MIT assignment:
  Mon: [tasks supporting goals]
  Tue: ...

Buffer days: 1 day/week kept light for overflow
```

### Project Breakdown

```
Large project → Phases → Tasks → Pomodoros

Example: "Write a report"
  Phase 1: Research (6 Pomodoros = 2.5 hours)
    - Find sources (2 Pomodoros)
    - Read and take notes (4 Pomodoros)
  Phase 2: Outline (1 Pomodoro)
  Phase 3: Draft (8 Pomodoros)
  Phase 4: Edit (3 Pomodoros)
  Phase 5: Final review (1 Pomodoro)

  Total: 19 Pomodoros (~8 hours)
  Spread over: 3 days
```

---

## Habit Tracking

### Habit Design (BJ Fogg's Tiny Habits)

```
Formula: Anchor + Tiny Behavior + Celebration

Example:
  Anchor: "After I pour my morning coffee..."
  Behavior: "...I will write ONE sentence."
  Celebration: "...I'll say 'yes!'"

Habit stacking: chain habits together using existing routines
```

### Habit Metrics

```
Consistency rate = (days_completed / total_days) × 100

Streak tracking:
  Current streak: X days
  Best streak: Y days
  Last 30 days: Z% completion

"Never miss twice" rule: One miss is an accident, two is a pattern.
```

### Habit Difficulty Scoring

```
1–2 Pomodoros/day: Sustainable long-term
3–4 Pomodoros/day: Requires strong motivation
5+  Pomodoros/day: Hard to maintain — split into phases

Start with 1/10th of target:
  Goal: Run 5km daily → Start: Walk 5 minutes daily
  Goal: Write 1000 words → Start: Open document and write 1 sentence
```

---

## Anti-Procrastination Strategies

### Procrastination Diagnosis

```
Type 1 — Task aversion: Task feels unpleasant
  Fix: 2-minute rule, body doubling, reward system

Type 2 — Overwhelm: Task feels too big
  Fix: Break into smallest possible first step

Type 3 — Perfectionism: Fear of imperfect output
  Fix: Time-box it, "done > perfect", ship drafts

Type 4 — Decision fatigue: Too many options
  Fix: Eliminate choices, pre-decide the next action

Type 5 — Low energy: Physical/mental depletion
  Fix: Protect sleep, exercise, single-task
```

### Emergency Focus Protocol

When can't start a task:

```
Step 1: Set timer for 5 minutes. Just start. Don't finish.
Step 2: After 5 min, decide: continue or stop (usually continue)
Step 3: If still stuck: change environment (go to cafe, library)
Step 4: Remove friction: close all tabs, phone in another room
Step 5: Body double: work alongside someone (Focusmate, library)
```

---

## Usage Examples

### Quick Pomodoro Plan

```
Input: "I have 3 hours to work on my thesis introduction."

Output:
  Available: 180 minutes = 6 Pomodoros + breaks

  Session plan:
  [25 min] Write section outline
  [5 min]  Break — stand, stretch
  [25 min] Draft first paragraph (hook)
  [5 min]  Break
  [25 min] Draft background section
  [5 min]  Break
  [25 min] Draft literature review
  [15 min] Long break — walk, water
  [25 min] Edit and tighten writing
  [5 min]  Break
  [25 min] Final review + citations

  Total focused: 2.5 hours
  Goal: Complete full introduction draft
```

### Daily Plan from Task List

```
Input:
  Tasks: [Write report, Reply to 10 emails, 2 calls, prep presentation]
  Available: 9am–5pm (8 hours)
  Energy: High in morning

Output:
  MITs (morning, high energy):
    1. Write report — 4 Pomodoros (2 hours)
    2. Prep presentation — 3 Pomodoros (1.5 hours)

  Admin (afternoon):
    3. Reply emails — 1 Pomodoro (25 min)
    4. Calls — 45 min (scheduled 2pm, 3pm)

  Schedule: [detailed time blocks]
  Buffer: 1 hour unscheduled
```

### Habit Tracker Setup

```
Input: "I want to build a reading habit."

Output:
  Habit design:
    Anchor: After dinner
    Tiny behavior: Read 2 pages (not "30 minutes")
    Celebration: Check it off the list

  Week 1 target: 2 pages/day (100% completion goal)
  Week 3 target: 10 pages/day (after habit is locked in)
  Week 6 target: 20–30 pages/day

  Track:
    [ ] Mon  [ ] Tue  [ ] Wed  [ ] Thu  [ ] Fri  [ ] Sat  [ ] Sun

  Rule: Never miss twice.
```

---

## Interaction Patterns

When triggered, ask:
1. "What are you working on today?"
2. "How many hours do you have available?"
3. "What's your energy level right now? (High / Medium / Low)"
4. "Is there one most important task that must get done?"

Then:
- Assign Pomodoro counts to tasks
- Build a time-blocked schedule
- Identify the single first action to start

For habit requests:
- Design the tiniest possible starting version
- Set up a simple tracking template
- Define the anchor (existing routine to attach to)

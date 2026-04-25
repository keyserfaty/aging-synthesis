# Methodology

**Status: LOCKED. Date locked: 2026-04-24.**

This document defines how every intervention page is produced. It is written before any specific intervention is assessed so that future-me cannot move goalposts to fit a preferred conclusion. Changes are logged as commits to this repository with explicit "methodology revision" reasoning, and force re-review of every existing page.

---

## 1. Scope

This project synthesizes the evidence for **healthspan and lifespan interventions** in:
- Invertebrate models (C. elegans, D. melanogaster, S. cerevisiae)
- Mammalian models (mouse, rat, dog, NHP)
- Humans (where any data exists)

**Endpoints we evaluate:** median lifespan, maximum lifespan, healthspan markers (frailty, grip strength, gait, cognition), validated biomarkers of aging (epigenetic clocks, GlycanAge, etc.), all-cause mortality where available.

**Endpoints we do not evaluate:** subjective wellness, single-domain outcomes (e.g., "improves sleep") unless tied to an aging mechanism, marketing claims.

We do **not** issue supplement or treatment recommendations. The output is a calibration aid for readers who already plan to make their own decisions.

---

## 2. Evidence tiers

Every claim is anchored to one of these tiers. Higher tiers dominate lower tiers in conflict.

| Tier | Description |
|---|---|
| **T1** | Human RCT, pre-registered, n ≥ 100, hard endpoint (mortality, validated aging biomarker), independently replicated |
| **T2** | Human RCT, pre-registered, single trial OR surrogate endpoint OR n < 100; **OR** large prospective cohort with strong confounder control |
| **T3** | ITP-replicated mouse lifespan result (any sex), or RP2-replicated, or ≥ 2 independent labs with consistent direction in mice |
| **T4** | Single-lab mouse lifespan extension, or NHP biomarker improvement, or healthspan-only mouse data |
| **T5** | Invertebrate lifespan extension (C. elegans, fly, yeast); mechanistic plausibility only |
| **T0** | Anecdote, n-of-1, uncontrolled human observation, biohacker self-report, in vitro cell line only |

**Cross-species translation discount:** results in tier T5 do not transfer to mammals without independent confirmation. T4 → human translation is discounted by 1 tier when applied to human verdict.

---

## 3. Verdict bands

Every intervention receives one of:

- **Strong** — T1 or multiple T2 evidence in humans, mechanism understood, effect direction agreed across labs. Examples expected: exercise.
- **Probable** — T3 evidence solid AND at least suggestive human data (T2 surrogate endpoint or large cohort). Examples expected: rapamycin (mice strong, human limited).
- **Suggestive** — T3 or T4 evidence with replication; human data absent or null. Examples expected: spermidine, taurine (pending replication).
- **Mixed** — Tier-appropriate evidence exists but replication has failed or sex/strain dependence is severe. Examples expected: metformin in non-diabetics.
- **Mostly hype** — Popular intervention with only T0/T5 evidence, or T4 evidence that has failed replication at higher tiers. Examples expected: resveratrol.
- **Insufficient evidence** — Too little data of any tier to form a verdict.

A verdict band must be defensible against the calibration anchors. If a new intervention I'm rating "Probable" has weaker evidence than rapamycin (the anchor for Probable), I have miscalibrated.

---

## 4. Required fields per intervention page

Every page must populate ALL of the following. Missing data is recorded as "no data found" — never silently omitted.

1. **TL;DR verdict** (one sentence + verdict band)
2. **What it is** (chemical class, dose ranges, route)
3. **Proposed mechanism** with confidence level (established / plausible / hypothetical)
4. **Evidence ladder** — separate subsections for invertebrate, mouse, NHP, human; each with study count, effect size range, replication status
5. **Sex, strain, dose dependence** — required for mouse data; if not specified in the literature, that is itself a flag
6. **Confounds** — control diet adequacy, baseline mortality of the strain (short-lived strains inflate apparent gains), publication bias signal
7. **Conflict of interest scan** — industry funding, author equity, supplement industry ties
8. **Human translation** — what RCTs exist, what they actually measured, what they actually showed
9. **Calibrated verdict** — band + 2-3 sentence rationale + comparison to nearest calibration anchor
10. **Confidence interval on verdict** — "could plausibly move to X if Y replicates"
11. **Open questions** — things that would change the verdict if resolved
12. **Last reviewed** — date stamp
13. **Sources** — every citation with link if available

---

## 5. Conflict-of-interest discounts

- Industry-funded study without pre-registration → discount 1 evidence tier
- Author holds equity in the intervention's commercializer → discount 1 tier
- Pre-registered + industry-funded → no discount (pre-registration neutralizes)
- Studies funded by NIA / Wellcome / equivalent independent → no discount
- ITP results never discounted (its design is the gold standard for this purpose)

---

## 6. Replication standards

- **In mice:** "replicated" means ≥ 2 independent labs OR ITP positive cohort. A single-lab result, no matter how striking, is T4 not T3.
- **In humans:** "replicated" means ≥ 2 independent RCTs with consistent direction on the same primary endpoint. Meta-analyses of underpowered trials do not count as replication.
- **Negative replications:** a single high-quality negative replication does not erase a positive result, but two negative replications at the next-highest tier downgrade the verdict by one band.

---

## 7. Verdict change protocol

Verdicts can move. The thresholds:

- **Upgrade** (one band up): requires new evidence at a higher tier than the current anchor evidence, OR a previously-flagged open question resolved positively.
- **Downgrade** (one band down): requires (a) two negative replications at the next-highest evidence tier, OR (b) discovery of a methodological flaw invalidating the anchor evidence, OR (c) failure of a pre-registered confirmatory trial.
- Any verdict change is logged in the commit history with the triggering evidence and pre-existing threshold quoted in the commit message.

This is the anti-drift mechanism. If I find myself wanting to upgrade NMN because a new podcast made a compelling case, the methodology says no without new evidence at the right tier.

---

## 8. When the methodology is silent

Some questions cannot be resolved from these rules alone (e.g., "is pre-print evidence admissible?", "how do we handle a retracted paper that's been re-published?"). Decision protocol:

1. First pass: triangulate from the published positions of the calibration authorities — Matt Kaeberlein, the ITP team, Cochrane reviewers if relevant. What would they do?
2. Second pass: open a GitHub issue on this repository for broader review.
3. Third pass: leave the question open; flag it explicitly on the affected intervention page.

Never silently invent a rule. If a new rule is needed, it goes through the methodology-revision process (section header).

---

## 9. What this methodology deliberately excludes

- **No precision-medicine claims.** We rate interventions at the population level. Individual variation is real but out of scope.
- **No combination therapies in solo pages.** Combinations get their own pages in `interactions/`.
- **No legal/regulatory analysis.** "Available OTC in the US" is not evidence relevant to a verdict.
- **No reasoning from mechanism alone.** "It hits mTOR so it should work" never elevates a verdict above Suggestive.
- **No pricing or accessibility commentary.** The verdict is about the evidence; what people do with it is their choice.

---

## 10. Methodology revision log

(none yet — methodology locked 2026-04-24)

# Calibration Anchors

**Status: LOCKED. Date locked: 2026-04-24.**

These five interventions have pre-committed verdicts. They exist so every other intervention I rate can be triangulated against them. If a new verdict is inconsistent with these anchors, the methodology has failed and I revisit — I do not silently bend the anchors.

Each anchor cites the external authority whose published position I am aligning with, so the calibration is auditable.

---

## Anchor 1: Exercise → **Strong**

The only intervention with T1 evidence in humans on hard endpoints (all-cause mortality), replicated across thousands of cohorts and dozens of RCTs, with mechanistic plausibility across nearly every aging hallmark. Effect size: ~30% reduction in all-cause mortality at population level for moderate aerobic + resistance training vs sedentary.

**Authority anchored against:** WHO physical activity guidelines (2020); meta-analyses in BMJ and JAMA; Cochrane reviews of exercise for older adults.

**Why this is the ceiling:** if any other intervention claims "Strong," its evidence base must be at least this comprehensive. None currently are.

---

## Anchor 2: Caloric restriction (in mice) → **Strong**

In mice, CR is the most replicated lifespan intervention in the history of biology — hundreds of studies across decades, multiple strains, multiple labs, dose-response established. T3 evidence with extensive replication.

**Important caveat preserved in the anchor:** Strong **for mice**. The human translation (CALERIE-2 RCT) shows biomarker improvements but no lifespan data; the rhesus monkey studies (NIA vs Wisconsin) reached different conclusions depending on control diet quality.

**Authority anchored against:** Richard Weindruch's body of work; NIA's CR program; CALERIE-2 trial reports.

**Why this is the ceiling for mouse interventions:** any new intervention claiming "Strong in mice" must match CR's level of replication, which is essentially impossible for newer interventions. So in practice, mouse-only interventions max out at "Probable."

---

## Anchor 3: Rapamycin → **Probable**

Rapamycin has multiple ITP-positive cohorts (T3, gold standard) across both sexes (with sex-dependent effect sizes), dose-response data, and mechanistic clarity (mTOR). Human evidence is limited to T2 surrogate endpoints (PEARL trial — open-label, modest sample, biomarker outcomes; and small immunology trials showing improved vaccine response in older adults).

It is **not** "Strong" because human lifespan/mortality data does not exist. It is **above** "Suggestive" because the mouse evidence is exceptional and human surrogate data exists.

**Authority anchored against:** Matt Kaeberlein's published position; ITP cohort summaries; PEARL trial publications.

**Why this is the anchor for "Probable":** the bar to claim Probable is "T3 mouse evidence with at least suggestive human data." Rapamycin is the cleanest example. Anything I rate Probable should be defensible as having evidence at least this strong; if it doesn't, it is Suggestive.

---

## Anchor 4: NMN → **Suggestive**

NAD+ precursors have T4-T5 evidence: small lifespan effects in mice (single-lab, contested across labs), mechanism plausible (NAD+ decline with age is real), and human RCTs have shown NAD+ level increases without clear downstream functional benefit. Industry-funded studies dominate the literature, and several have failed to replicate independently.

**Why not "Mostly hype":** NAD+ biology is genuine; the mechanistic foundation is real; some non-industry data exists.

**Why not "Probable":** no ITP replication; mouse lifespan effects are inconsistent across labs; human RCTs lack hard or even strong surrogate endpoints.

**Authority anchored against:** ITP's failure to replicate NR (the closest tested precursor); Brad Stanfield's reviews; published critical reviews of NAD+ supplementation.

**Why this is the anchor for "Suggestive":** something interesting is probably happening, but the evidence has not climbed to the bar that Probable requires.

---

## Anchor 5: Resveratrol → **Mostly hype**

Resveratrol kicked off the modern longevity-supplement industry on the strength of yeast and mouse studies (T5/T4) that have largely failed to replicate at higher tiers. ITP tested it; it failed. Major mouse lifespan studies that initially showed effects had problematic controls. Human RCTs show no meaningful biomarker effect at achievable oral doses.

**Authority anchored against:** ITP's negative result; Aubrey de Grey's and Matt Kaeberlein's published skepticism; failed Sirtris commercialization trajectory.

**Why this is the anchor for "Mostly hype":** the evidence existed, it was tested rigorously, and it failed. Other interventions rated "Mostly hype" should have a similar trajectory of "popular, tested at higher tier, failed."

---

## Triangulation rules

When rating any new intervention:

1. **Identify the closest anchor** by evidence profile (not by chemical similarity).
2. **Compare evidence quality.** If the new intervention has weaker evidence than the anchor, it is at most one band below the anchor.
3. **Document the comparison** on the intervention's page in section 9 (Calibrated verdict).
4. **Detect anchor violations.** If a verdict implies an anchor is mis-rated, open a GitHub issue on this repository — do not silently re-rate the anchor.

---

## Anchor revision protocol

Anchors can be revised, but only via:
- New ITP data on the anchor itself (would re-rate rapamycin or resveratrol)
- New large human RCT on exercise or CR (could re-rate)
- Failure of a major mechanism claim (e.g., NAD+ supplementation shown to have no effect on tissue NAD+ levels in vivo at any dose)

Revision requires a commit-message entry on this repository, re-review of every page that triangulated against the anchor, and documentation of the triggering evidence.

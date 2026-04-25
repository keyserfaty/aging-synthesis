# Aging Interventions: Calibrated Verdict Index

A continuously updated, evidence-weighted map of aging interventions. Verdicts follow a locked methodology (`methodology.md`) and are triangulated against five calibration anchors (`CALIBRATION_ANCHORS.md`).

**Last index update: 2026-04-25.** **Total pages: 42 (38 interventions + 4 interactions).**

> **📄 Paper:** [Where the Longevity Discourse is Systematically Wrong](paper/paper.md) — synthesis paper covering the methodology + the eight findings the popular discourse gets wrong + what deserves more attention. [HTML version](paper/paper.html) · [Machine-readable verdict table (CSV)](paper/verdict-table.csv)
>
> **📌 Publication status (submitted 2026-04-25):**
> - Zenodo (locked methodology + verdict-table snapshot, immutable pre-commitment archive): [DOI 10.5281/zenodo.19768647](https://doi.org/10.5281/zenodo.19768647) — published
> - Zenodo (paper PDF + Markdown + verdict CSV): [DOI 10.5281/zenodo.19769433](https://doi.org/10.5281/zenodo.19769433) — published
> - medRxiv preprint: `MEDRXIV/2026/351734` — submitted, awaiting screening (DOI assigned at posting)
> - npj Aging (Springer Nature, peer review): submission ID `56b33daa-7a35-493b-a94d-656697ad825a` — under technical check
> - The Lancet Healthy Longevity (peer review): manuscript number `THELANCETHEALTHYLONGEVITY-S-26-00591` — under editorial review
>
Verdicts use these bands (lowest evidence → highest):
- **Insufficient evidence** — too little data to form a verdict
- **Mostly hype** — popular intervention; tested rigorously and failed, or never had higher-tier support
- **Mixed** — tier-appropriate evidence exists but replication has failed or population dependence is severe
- **Suggestive** — T3-T4 evidence with replication; human data absent or null/early
- **Probable** — T3 evidence with at least suggestive human data, OR T1 evidence in defined population
- **Strong** — T1 / massive cohort + RCT evidence on hard endpoints; mechanism understood

If you do nothing else from this database, do **exercise (aerobic + resistance)**, prioritize **sleep (~7h)**, and do **caloric moderation without specific timing fixation**. These represent the bulk of the population-level longevity benefit.

---

## Strong (in humans)

The interventions with the most overwhelming evidence base. These are the non-negotiables.

- **[Aerobic exercise](interventions/exercise-aerobic.md)** — anchor; 20-40% all-cause mortality reduction at moderate doses across millions of person-years.
- **[Resistance training](interventions/exercise-resistance.md)** — 10-20% all-cause mortality + unique sarcopenia / functional-capacity protection.
- **[Sleep](interventions/sleep.md)** — Strong observational / Probable causal; ~7 hours nightly is the population optimum.
- **[Statins (secondary prevention)](interventions/statins.md)** — overwhelming evidence in established CVD.

## Strong (in mice — anchor band for animal evidence)

- **[Caloric restriction](interventions/caloric-restriction.md)** — anchor for mouse-Strong; Suggestive in humans (CALERIE-2 biomarker results, no mortality data).

## Probable

Solid evidence at the relevant evidence tier and population.

- **[Rapamycin](interventions/rapamycin.md)** — anchor; T3 mouse, T2 human surrogate; the best-evidenced longevity drug candidate.
- **[Acarbose](interventions/acarbose.md)** — Probable mice / Suggestive humans; underappreciated relative to ITP evidence quality.
- **[17α-estradiol](interventions/17alpha-estradiol.md)** — Probable in male mice / Insufficient evidence humans; striking single-sex ITP finding.
- **[Canagliflozin](interventions/canagliflozin.md)** — Probable male mice + Probable in CV/CKD/DM hard endpoints.
- **[GLP-1 agonists](interventions/glp1-agonists.md)** — Probable in obese / CV-risk per SELECT trial.
- **[Statins (primary prevention 40-75)](interventions/statins.md)** — clear net benefit at elevated CV risk.
- **[Sauna / heat exposure](interventions/sauna-heat-exposure.md)** — KIHD cohort dose-response is among strongest non-exercise lifestyle signals.
- **[Creatine + resistance training](interventions/creatine.md)** — Probable for sarcopenia / cognition adjunct.
- **[HRT in early-menopause women](interventions/hrt-trt.md)** — Probable when started ≤age 60 / within 10 years of menopause.
- **[TRT in documented hypogonadism](interventions/hrt-trt.md)** — Probable per TRAVERSE.
- **[Zone 2 / VO2max framework](interventions/zone2-vo2max.md)** — Probable for the broader VO2max claim / Mixed for the Zone-2-is-optimal-protocol claim.

## Suggestive

Real biology, replication or human translation incomplete.

- **[NMN / NR (NAD+ precursors)](interventions/nmn.md)** — anchor; ITP failed NR; cousin to NMN.
- **[Senolytics (D+Q, fisetin)](interventions/senolytics-dq-fisetin.md)** — strong mouse, early human, mixed clock signals.
- **[Spermidine](interventions/spermidine.md)** — SmartAge primary endpoint null; observational signal positive.
- **[GlyNAC](interventions/glynac.md)** — single-group dominance; mechanism coherent.
- **[Sulforaphane](interventions/sulforaphane.md)** — best-evidenced natural Nrf2 activator.
- **[Plasma exchange / TPE](interventions/plasma-exchange.md)** — Conboy lab pilots; commercial layering high.
- **[Taurine](interventions/taurine.md)** — leaning toward downgrade; 2025 Science follow-up undermined the age-decline premise.
- **[Omega-3 (general)](interventions/omega-3.md)** — Suggestive general / Probable in REDUCE-IT-equivalent population.
- **[Lithium (low-dose, observational + MCI)](interventions/lithium-low-dose.md)** — drinking water signals; supplement microdosing weaker.
- **[CoQ10 (HF / statin myalgia)](interventions/coq10.md)** — narrow indications only.
- **[EGCG / green tea consumption](interventions/egcg.md)** — observational; supplement form has hepatotoxicity caveat.
- **[Berberine (cardiometabolic)](interventions/berberine.md)** — modest glycemic/lipid effects; longevity claim weaker.
- **[Cold exposure (narrow indications)](interventions/cold-exposure.md)** — mood, BAT, recovery; longevity claim weak.

## Mixed

Tier-appropriate evidence but replication failures or severe population dependence.

- **[Metformin](interventions/metformin.md)** — ITP null in mice; observational human data confounded; MET-PREVENT 2025 shows exercise blunting.
- **[Time-restricted eating](interventions/time-restricted-eating.md)** — Liu 2022 NEJM showed null vs matched-calorie comparator.
- **[Vitamin D](interventions/vitamin-d.md)** — VITAL primary null; modest cancer-mortality signal real; hip-fracture signal in women.
- **[Hyperbaric oxygen](interventions/hyperbaric-oxygen.md)** — single-group + COI; replication missing.
- **[Statins (>75 healthy primary)](interventions/statins.md)** — USPSTF: insufficient evidence; STAREE pending.

## Mostly hype

Popular interventions where the evidence has failed or never reached higher tiers.

- **[Resveratrol](interventions/resveratrol.md)** — anchor for Mostly hype; ITP-failed, SIRT1 mechanism not supported in humans.
- **[Curcumin](interventions/curcumin.md)** — bioavailability ceiling; PAINS critique; modest evidence only for OA pain.
- **[EGCG (high-dose supplements)](interventions/egcg.md)** — hepatotoxicity caveat.
- **[Quercetin (standalone)](interventions/quercetin.md)** — senolytic case lives in D+Q, not standalone.
- **[Methylene blue](interventions/methylene-blue.md)** — TauRx Alzheimer's program failed; biohacker framing unsupported.
- **[Pterostilbene / PQQ / Astaxanthin](interventions/pterostilbene-pqq-astaxanthin.md)** — consolidated; same pattern.
- **[Lithium microdosing (broader claims)](interventions/lithium-low-dose.md)** — supplement-form longevity claim unsupported.
- **[CoQ10 (general longevity)](interventions/coq10.md)** — heart failure data ≠ aging data.

## Insufficient evidence

Not enough data to form a verdict, generally because the field is preclinical-only.

- **[Yamanaka factors / partial reprogramming](interventions/yamanaka-partial-reprogramming.md)** — most preclinically exciting category; first FDA-cleared trial April 2026.
- **[Klotho upregulation](interventions/klotho.md)** — strong mouse evidence; no human supplementation pathway established.

## Interactions / Combinations / Antagonisms

Synergies and important antagonisms between interventions.

- **[Rapamycin + Acarbose](interactions/rapamycin-acarbose.md)** — Probable; among largest ITP combined effects (+34% males, +28% females).
- **[Rapamycin + Metformin](interactions/rapamycin-metformin.md)** — Probable but driven by rapamycin; metformin adds little.
- **[Metformin + Exercise (antagonism)](interactions/metformin-exercise.md)** — Probable antagonism; metformin blunts exercise adaptations.
- **[GLP-1 + Resistance Training (mitigation)](interactions/glp1-resistance-training.md)** — Probable mitigation of GLP-1-induced muscle loss.

---

## How to use this index

- **For decision-making:** prioritize Strong-band interventions; treat Probable as supportable; treat Suggestive as worth tracking but not committing to; treat Mostly hype as supplement-industry signal rather than evidence.
- **For staying current:** verdict changes are logged in the repository commit history. Open issues on the repo for new evidence or contested verdicts.
- **For the methodology behind verdicts:** read `methodology.md` and `CALIBRATION_ANCHORS.md`. Both are locked; revisions require explicit changelog entries.
- **For unresolved questions:** open a GitHub issue.

## What this database is not

- Not personal medical advice. Verdicts are population-level evidence summaries.
- Not exhaustive. New interventions and verdict updates appear via commits to the repository.
- Not free of judgment calls — every verdict is a calibration claim defensible against the methodology and anchors. Disagreements should be raised via the question-resolver process, not silent edits.

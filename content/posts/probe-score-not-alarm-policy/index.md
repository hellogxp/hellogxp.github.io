---
title: "A Probe Score Is Not an Alarm Policy"
date: 2026-10-05
author: "Xueping Gao"
tags: ["agent-safety", "mechanistic-interpretability", "LLM", "prompt-injection", "activation-monitoring", "evaluation"]
math: true
draft: false
summary: "An activation monitor that ranks attack cases above safe cases 92% of the time caught zero of 38 real attacks at the false-alarm budget a deployment could afford. The gap between a probe score and an alarm policy is eight fields wide — a research-informed practice guide to grading what your monitor actually claims, from our DAI 2026 paper."
---

A monitor that ranks attack cases above safe cases in **92% of pairs** — AUROC 0.92, a number most papers would happily headline — caught **zero of 38 real attacks** when we locked it to an operating point the deployment could afford. At the looser budget, where the calibration promised a 10% false-alarm rate, the same monitor family realized **18.7–20.0%** false alarms on test. And in a second, independently frozen replication, the calibration data turned out to be too thin to lock any threshold at all: the policy did not fail, it **abstained** — because there was nothing honest to deploy.

This is the central pattern of our DAI 2026 paper, *From Probe Scores to Alarm Policies*, and it is not a story about a bad monitor. The probe was trained properly, calibrated on disjoint data, and tested exactly once against an immutable manifest. It still failed, because the number it was summarized with — AUROC — answers a different question than the one an alarm system must answer. A ranking metric asks: *does the score order positives above negatives?* An alarm policy asks: *at a threshold I can afford, on the unit I pay for, does anything cross the line?* Nobody deploys an AUROC. You deploy a score, an aggregation rule, and a threshold that may stop a trajectory, block a request, or page a human.

<figure>
<a href="figures/figure_report_cards.svg?v=1" target="_blank" rel="noopener" title="Open full-size figure" style="display:block;box-shadow:none;text-decoration:none;border:0">
<picture>
<source media="(max-width: 480px)" srcset="figures/figure_report_cards_mobile.svg?v=1">
<img src="figures/figure_report_cards.svg?v=1" alt="The same monitor graded twice: a lab report card showing AUROC 0.92 with a green PASS stamp, and a deployment report card showing 0 of 38 attacks detected with a red SILENT stamp" style="max-width:760px;width:100%;display:block;margin:0 auto" loading="lazy">
</picture>
</a>
<figcaption>Figure 1: The same monitor, graded twice. The lab grade is the number the literature reports; the deployment grade is what the operator gets at a locked 5% false-alarm budget. Numbers from the AgentDojo audit described below; card layout is schematic.</figcaption>
</figure>

In an [earlier post](/posts/agent-state-safety/) I argued that activation-monitoring claims come in levels — decodability is not prediction is not causation is not authority. This post is about the last mile of that ladder: even a *predictive* score, honestly measured, is not yet an alarm. Between the score and the alarm sits a contract that most papers never write down.

## A Monitor That Caught Nothing

The setting is AgentDojo ([Debenedetti et al. 2024](https://arxiv.org/abs/2406.13352)), a benchmark where a tool-using agent reads results from tools — a Slack channel, a travel site — and an attacker hides instructions inside one of those tool results. The attack wins if the agent's remaining trajectory executes the injected goal. I monitored a Qwen2.5-7B agent's internal activations at the first policy request *after* it consumed the poisoned tool result, and tried to predict the future: will this trajectory end up doing what the attacker wants?

The protocol was deliberately rigid, because monitor evaluation is usually leaky. I froze the model, the layer, the pooling, the templates, and every threshold before test behavior existed. The test set was an immutable manifest of 1,190 rollout identities — 82 semantic security cases, each given ten prespecified stochastic attempts, a retry-set stress audit for systems that may retry a task — and it was consumed **exactly once**. Failed trajectories were kept, not regenerated. I also froze a support gate in advance: at least 40 positive cases, or the result would be labeled *support-insufficient* no matter what it showed.

The mean-activation monitor scored a rollout AUROC of **0.9215**. At the threshold locked for a 5% safe-attempt alarm budget, it detected **0 of the 38** cases that contained an unsafe attempt. At the 10% budget, the activation and joint monitors realized 18.7% and 20.0% safe-attempt alarm rates — roughly double what calibration promised. Neither fact is visible from the AUROC.

Two honest disclosures before anyone over-reads this. First, the test delivered 38 positive cases against the frozen gate of 40, so the formal status is *support-insufficient* — a design-sufficiency rule, not a verdict. Second, the primary case-level monitors did detect a little: at the 5% point, the best monitors caught 2 of 38 cases. The failure is a spectrum from "nearly nothing" to "nothing," not a single dead probe. But the headline inversion is real: the monitor with the *best* ranking score was the one that caught nothing at all.

That is the mystery this post unpacks. Not "how could a probe be so bad" — the probe was fine. The question is how a number can be so good while the thing it supposedly measures is so bad.

## A Monitor Claim Is a Contract

The short answer: "AUROC 0.92" is not a claim about an alarm. It is a claim about pairwise ranking, and getting from there to "this monitor may page a human" silently fixes eight things that different papers fix differently — or not at all.

In the paper we call the bundle an **Operational Validity Contract**: Target × Observability × Identity × Timing × Unit × Comparator × Calibration × Cost. Each field is a choice, and changing any one of them changes what your result means:

- **Target** — what is actually being predicted. An input property ("this prompt is high-stakes"), future behavior ("this trajectory will execute the injection"), and a causal state ("the model intends harm") are three different targets that the same score gets attached to. Most monitor papers measure the first and discuss the third.
- **Observability** — what a monitor *without* activation access sees at the same moment. If your visible-history baseline is a bag of words but your activation probe reads a forward pass computed over the full prompt, part of your "increment" is just information the baseline was denied.
- **Identity** — the semantic object that must not leak across training, calibration, and test. The released LASR refusal split shares 207 of 969 test request identities with its own training set — a row-level split that is not a semantic split.
- **Timing** — when the score is read. Pre-action, pre-response, and post-hoc are different instruments; only the first can stop the action.
- **Unit** — what pays for an alarm. A row in a dataset, a model request, a user task, a trajectory. Operators pay per task; benchmarks report per row. This mismatch is so important it gets its own section below.
- **Comparator** — the baseline your increment is measured against, with its model class, data, and compute budget declared.
- **Calibration** — the population and rule that lock the threshold, including how many independent negatives you actually had.
- **Cost** — what an alarm consumes: latency, memory, review attention, the value of the blocked action.

The contract induces a three-level claim ladder. **Representation accessibility**: a frozen probe ranks held-out data — AUROC lives here. **Restricted predictive value**: the probe adds held-out gain over a *capable, same-horizon* observable comparator, with clustered uncertainty. **Alarm-policy validity**: an operational aggregation rule, an independently locked threshold, realized risk, sufficient positive support, transport diagnostics, and declared cost. Evidence cannot be promoted up the ladder by renaming the target after the experiment.

<figure>
<a href="figures/figure_pipeline.svg?v=1" target="_blank" rel="noopener" title="Open full-size figure" style="display:block;box-shadow:none;text-decoration:none;border:0">
<picture>
<source media="(max-width: 480px)" srcset="figures/figure_pipeline_mobile.svg?v=1">
<img src="figures/figure_pipeline.svg?v=1" alt="Five-step pipeline from Specify to Claim: AUROC is evidence only at step 2, Compare; calibration and transport stress are where good monitors die; a fail-closed abstain branch catches unsupported policies" style="max-width:760px;width:100%;display:block;margin:0 auto" loading="lazy">
</picture>
</a>
<figcaption>Figure 2: The road from a score to an alarm. A high AUROC is evidence at step 2 — it is not permission to skip specification, unit-level calibration, or transport. Every claim in the paper is labeled by the last step it survives; when support or identity checks fail, the policy abstains rather than guessing.</figcaption>
</figure>

The closest neighbors in the literature make the same boundary visible from the other side. Monitoring Monitorability ([Guan et al. 2026](https://openreview.net/forum?id=b82fgbMVpz)) builds the archetype taxonomy and a monitorability metric; GAVEL ([Rozenfeld et al. 2026](https://openreview.net/forum?id=duntROHZ5R)) composes activation concepts into runtime rules; PrefixGuard ([Huang et al. 2026](https://arxiv.org/abs/2605.06455)) already observed that strong ranking need not yield actionable first alerts at low false-alarm rates. What none of them binds is the full chain: same-horizon observable comparator, semantic alarm unit, confidence-locked threshold, frozen transport audit. That binding is the contract.

## High AUROC Coexists with a Dead Alarm

Four settings, audited by the same procedure, died in three distinguishably different ways. First the picture, then the anatomy.

<figure>
<a href="figures/figure_auroc_vs_tpr.png?v=1" target="_blank" rel="noopener" title="Open full-size figure" style="display:block;box-shadow:none;text-decoration:none;border:0">
<picture>
<source media="(max-width: 480px)" srcset="figures/figure_auroc_vs_tpr_mobile.svg?v=1">
<img src="figures/figure_auroc_vs_tpr.png?v=1" alt="Scatter of operational-unit AUROC against realized TPR at locked thresholds for a 5% and a 10% false-alarm budget; all points sit below the 0.80 requirement line at 5%, and several sit below it at 10%" style="max-width:760px;width:100%;display:block;margin:0 auto" loading="lazy">
</picture>
</a>
<figcaption>Figure 3: Ranking quality versus operating-point reality across the frozen settings. Marker shape is the setting (circle MUP, square LASR, triangle AgentDojo), color the monitor family. The dashed line is the prospectively frozen 0.80 TPR requirement — nothing reaches it at the 5% budget. Figure from the paper's audit artifact; ST-WebAgentBench is absent because its policy abstains.</figcaption>
</figure>

**AgentDojo is the spine.** The pre-registered picture was actually *against* an activation increment: on model-fit out-of-fold data, the joint monitor was *worse* than the observable baseline (AUROC difference −0.014, 95% CI [−0.034, 0.004]). We locked the pipelines anyway and consumed the test once — the test was a falsification attempt, not a success we selected. On test, the ranking looked healthy (case-max AUROC 0.80 for the primary activation monitor; 0.92 for the rollout-mean variant), while the operating points collapsed: 0–2 of 38 positive cases caught at 5%, and at the 10% budget, realized false-alarm rates of 18.7–20.0% against a calibration upper bound of 8.9%. That transport failure is itself quantifiable: under the frozen calibration null, seeing this many test alarms has probability **0.0017** — calibration and test were simply not the same distribution. And the burden was not spread evenly: at 5%, every true positive and both observable false positives landed in one suite (Slack, 14.3% FPR against a 2.7% pooled rate). A marginal number hides a concentrated tax.

The unit choice is not bookkeeping. Prespecified sensitivities over fixed-order subsets ($k$ = 1, 3, 5, 10 attempts) and all-single-seed variants shift the operating points sharply, and only four of the single-seed policies can even identify a finite 5% threshold. The primary estimand stays the frozen ten-attempt case — but the spread is the point: the answer depends on the retry semantics, so the semantics must be declared before the data.

**MUP and LASR are the honest middle.** On Models Under Pressure ([McKenzie et al. 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b9501301a7a0f99e57406cc901f4e3ce-Abstract-Conference.html)), the joint monitor reached AUROC **0.9571**, with realized 5%/10% TPRs of .642/.742. On the LASR refusal setting ([Kirch et al. 2025](https://arxiv.org/abs/2511.17408)), request-event AUROC **0.9348**, TPRs .719/.782. These are real activation increments — on MUP, joint-minus-observable TPR is **+0.265** (95% CI [0.153, 0.427]) at the 5% budget — and on 762 identity-disjoint, semantically unseen LASR requests the increment survives (+0.083, CI [0.049, 0.117]). So no, activations are not useless. But neither setting reaches the frozen 0.80 gate at both budgets, and LASR's official test split carries the identity overlap disclosed above, so its all-test panel gets no transport certificate.

**ST-WebAgentBench never got to fail.** The SuiteCRM replication on ST-WebAgentBench ([Levy et al. 2026](https://openreview.net/forum?id=MuCDzH0ctf)) reached activation AUROC .874, but its calibration set contains **23 independent negative units**. Locking even a 10% controller with 95% confidence requires 29; a 5% controller requires 59. Every frozen threshold was therefore +∞, every controller abstained, and the mechanical zero-FPR that results is *not* a transport success — it is the absence of a policy. (Its 28 negative test templates also missed the frozen minimum of 29. I know how that feels; we wrote the gate, then watched our own data fail it.)

Name the three deaths separately, because the fix for each is different:

- **Unidentifiable threshold** — too few independent negatives to lock anything (ST-Web). More test data cannot help; the missing quantity is calibration support.
- **Unseparated tail** — a threshold exists, but almost no positives live above it (AgentDojo at 5%, MUP/LASR at both budgets). This is a property of the score distribution's extreme tail, which AUROC barely sees.
- **Broken transport** — the locked threshold means something else on test (AgentDojo at 10%; the suite concentration is its subgroup shadow). Exchangeability is an assumption, and it broke with immutable code and frozen thresholds.

Reporting only "did not reach 80% TPR" would erase exactly the distinctions that tell you what to fix.

## Why AUROC Can't See Any of This

The metric has three structural blind spots, and each of the three deaths above maps to one of them.

**Blind spot 1: no threshold.** AUROC averages over every threshold, almost all of which your alarm policy will never use. Formally, with a random positive row score $S^+$ and negative row score $S^-$,

$$\mathrm{AUROC}=\Pr(S^+>S^-)+\tfrac{1}{2}\Pr(S^+=S^-).$$

Read it plainly: it is the probability that a random attack outranks a random safe case. It says nothing about the top of the negative tail — the only region a low-FPR policy lives in. A monitor can improve its AUROC by getting better at ranking the easy middle of the distribution while the tail your threshold sits in gets worse.

**Blind spot 2: row-weighted.** AUROC weighs units in proportion to their row counts. But a semantic task that gives the monitor ten alarm opportunities pays its false alarms per *task*. If a safe unit contains $n$ conditionally independent alarm opportunities, each with row FPR $p$, the unit-level any-alarm rate is

$$R_0 = 1-(1-p)^n.$$

At $p = 5\%$ and $n = 10$, that is **40.1%**, not 5%. Without any dependence assumption the bounds are only $p \leq R_0 \leq \min(1, np)$ — the row-level number simply does not identify the unit-level number, and no amount of additional row-level test data repairs a misspecified unit.

<figure>
<a href="figures/figure_compounding.svg?v=1" target="_blank" rel="noopener" title="Open full-size figure" style="display:block;box-shadow:none;text-decoration:none;border:0">
<picture>
<source media="(max-width: 480px)" srcset="figures/figure_compounding_mobile.svg?v=1">
<img src="figures/figure_compounding.svg?v=1" alt="Line chart showing how a 5% row-level false positive rate compounds with the number of alarm opportunities per task: 5% at 1 opportunity, 22.6% at 5, 40.1% at 10, 64.2% at 20" style="max-width:560px;width:100%;display:block;margin:0 auto" loading="lazy">
</picture>
</a>
<figcaption>Figure 4: False alarms compound across alarm opportunities. A monitor that is "5% FPR" per row is a 40% FPR monitor per ten-attempt task under conditional independence; the honest bounds without that assumption are wider still. This is why the unit field of the contract is a scientific choice, not bookkeeping.</figcaption>
</figure>

**Blind spot 3: tail-blind with zero confidence.** Even if you know you want the 95th percentile of the negative-unit score distribution, estimating it from ranks costs more data than most monitor papers have. Sort $m$ independent calibration negatives, take the $r$-th largest as your threshold, and distribution-free order statistics give you a 95%-confidence upper bound on the fresh-negative tail mass. The price list is stark: at rank one, locking a 5% budget requires

$$m \geq \frac{\log \delta}{\log(1-\alpha)}$$

independent negative units — for $\alpha = \delta = 0.05$, that is **59**. ST-Web had 23. This is not pessimism, it is arithmetic; high-probability type-I error control at the tail has been expensive since long before LLMs ([Tong et al. 2018](https://arxiv.org/abs/1608.03109)), and conformal-style risk control makes the same point in a different vocabulary ([Angelopoulos et al. 2024](https://arxiv.org/abs/2208.02814), [Schirmer et al. 2026](https://arxiv.org/abs/2607.02510)).

Unidentifiable thresholds are blind spot 3's data side; unseparated tails are blind spot 1 made concrete; broken transport is what happens when the "independent draws from a common negative-unit distribution" premise fails. One framework, three failure modes.

And the three do not substitute for one another. On LASR, the nominal (uncertified) 10% activation threshold would reach .813 detection — but at a realized .114 false-alarm rate, over budget; at 5%, even the nominal rate is .747, which is a tail-separation problem, not a support problem. Reallocating the frozen data to buy more calibration support raised what we could certify without rescuing the operating point. You cannot trade separation for support, or support for transport — which is exactly why the contract keeps them as separate fields.

One more ceiling is worth stating, because it disciplines what activation access can ever promise. If $O$ is everything observable at the monitoring horizon and the activation $A = f_\theta(O)$ is a deterministic function of it, then $I(Y; A \mid O) = 0$: conditioning on what you already observe, the activation adds no information. This does not make probes useless — it relocates their value. The defensible claims are practical: the probe may be *cheaper* (our hook added no resolvable batch-one latency, 0.067% at batch eight), *earlier* (pre-action), or *complementary in its errors*. Those are engineering claims, and they deserve engineering evidence — a learning curve, a resource match — not an AUROC.

## AUROC Goes Down, the Alarm Gets Better

If you take the blind spots seriously, the follow-up experiment writes itself: stop optimizing the whole curve, and optimize the region the policy actually uses. On LASR, I retrained the probe with a partial-AUC objective restricted to FPR $[0, 0.10]$ at the unit-max level — a standard technique ([Narasimhan & Agarwal 2013](https://proceedings.mlr.press/v28/narasimhan13.html)), pointed at the operating region instead of the whole ranking.

The result is the cleanest demonstration in the paper that the metric and the policy are different objects:

<figure>
<a href="figures/figure_pauc_dumbbell.svg?v=1" target="_blank" rel="noopener" title="Open full-size figure" style="display:block;box-shadow:none;text-decoration:none;border:0">
<picture>
<source media="(max-width: 480px)" srcset="figures/figure_pauc_dumbbell_mobile.svg?v=1">
<img src="figures/figure_pauc_dumbbell.svg?v=1" alt="Three panels showing metrics before and after partial-AUC training: AUROC drops from 0.934 to 0.918, certified 10% TPR rises from 0.778 to 0.811, realized 10% FPR falls from 0.087 to 0.067" style="max-width:680px;width:100%;display:block;margin:0 auto" loading="lazy">
</picture>
</a>
<figcaption>Figure 5: Training for the operating point moves the ranking metric backwards. After partial-AUC training on LASR, AUROC falls while the certified 10% alarm utility rises and realized false alarms fall. Exploratory diagnostic, not a promoted method — the 5% variant fails, and the test had been inspected.</figcaption>
</figure>

AUROC **falls** from .9344 to .9184. Certified 10% detection **rises** from .778 to .811. Realized false alarms **fall** from .087 to .067. The ranking metric got worse and the alarm policy got better, in the same model, on the same frozen test.

The honesty footnotes matter here: this was exploratory (test results were already inspected), and the sibling variant trained for the $[0, 0.05]$ region *collapsed* detection from .719 to .574 — tail optimization is brittle, which is itself worth knowing. So I am not selling partial AUC. I am using it as a counterexample. If a metric can move *against* the alarm it supposedly summarizes, then optimizing that metric is optimizing the wrong thing — and reporting it as evidence of alarm quality is grading the wrong exam.

We are not the first to notice pieces of this. [Li et al. 2026](https://arxiv.org/abs/2606.22864) show AUC 0.998 need not identify malicious content in multimodal computer-use agents; [Vasudev et al. 2026](https://arxiv.org/abs/2602.03338) show accurate failure prediction does not imply effective failure *prevention* once you intervene. The pattern is converging from several directions: the score is not the system.

## Grade the Claim, Not the Score

The constructive output of the paper is a **fail-closed claim compiler**: frozen evidence goes in, and the strongest licensed claim comes out — accessibility, restricted predictive value, alarm-policy validity, or abstention. It never fits and never searches; it only applies the ladder. It is covered by 20 result-independent counterexample tests (malformed identities, unsupported ranks, ties, mechanical zeros), because a compiler that can be talked into a promotion is not a compiler.

Applied to our own four settings, the verdict is sobering: MUP and LASR cap at *restricted predictive value* (real increments, retrospective contracts), AgentDojo and ST-Web at *representation accessibility* (frozen comparator increments fail), and **no setting licenses an alarm-policy claim**. I wrote the compiler and it failed my own monitors. That is what it is for.

If you are building agent monitoring, the portable lessons fit on an index card:

- **Registry**: bind every monitor score to its eight contract fields. A score without a contract cannot be cited in an incident review — treat it as a rumor.
- **CI gates**: fail the build — not the dashboard — on identity leakage between train/calibration/test, on negative support below the rank requirement, and on tied or unsupported thresholds.
- **Dashboards**: show unit-level operating points and per-suite burden next to any AUROC. A pooled number that hides a 14% Slack FPR behind a 2.7% average is not a summary, it is a liability.

And the three-question triage for any monitor result, yours or a paper's:

1. **Counting alarms per what?** If one task gives the monitor $n$ alarm opportunities, budget at the task: a 5% row budget is a 40% task budget at $n = 10$ (Figure 4).
2. **How many independent negatives locked the threshold?** Fewer than 59 means a 5% claim is not certifiable at 95% confidence — abstain or claim a looser budget.
3. **Did the threshold travel?** If calibration and deployment differ in suite, policy, or model, transport is its own experiment. Our 10% threshold, locked cleanly on calibration, realized 20% on test.

Activation access still earns its place under this standard — the MUP and LASR increments are real, the extraction cost is negligible, and pre-action timing is exactly where you want a tripwire. The narrow conclusion is more useful than the broad one: a probe result alone does not identify a valid alarm policy, and the difference is eight fields of contract plus a threshold you can defend.

## What Changes Now

My take: the probe literature's reporting standard is the thing that should change. The field has spent two years proving that safety-relevant information is *accessible* in activations — jailbreaks, deception, refusal, reward hacking ([Patel & Wang 2024](https://openreview.net/forum?id=qbvtwhQcH5); [Wilhelm et al. 2026](https://arxiv.org/abs/2603.04069); [Collu et al. 2026](https://arxiv.org/abs/2605.28553)) — and that question is close to settled. The open question is operational: monitors deployed under budgets, against adaptive attackers (SLEIGHT-Bench, [Najt et al. 2026](https://arxiv.org/abs/2605.16626), shows capable transcript monitors keep blind spots at 1% FPR), on models that keep changing underneath them ([Duan 2026](https://arxiv.org/abs/2606.15980)). AI-control work ([Greenblatt et al. 2024](https://arxiv.org/abs/2312.06942)) already thinks in terms of audit budgets and trusted monitoring, and recent work on the low-FPR shape of monitor ROCs ([Staley et al. 2026](https://blog.redwoodresearch.org/p/logit-rocs-monitor-tpr-is-linear)) treats the tail as the object of study. The pieces exist; what is missing is the discipline of grading each monitor claim at the level it actually earned.

What I would do next: groupwise risk control instead of marginal budgets (the Slack concentration demands it); sequential contracts for stop-on-first-alarm policies (our ten-attempt unit is a stress audit, not a stop rule); adversarial drift as a first-class transport failure; and intervention studies, because detection without a measured intervention benefit is only half the product ([Vasudev et al. 2026](https://arxiv.org/abs/2602.03338) again).

The paper and its score-level replay artifact accompany the DAI 2026 camera-ready; the claim compiler and the frozen manifests are the parts I would start from if you want to audit your own monitor. The shortest version of the whole thing: *a probe asks what is accessible; an alarm asks what crosses the line. Grade the second question, not the first.*

## Citation

Cited as:

> Gao, Xueping. "A Probe Score Is Not an Alarm Policy". hellogxp.github.io (October 2026). https://hellogxp.github.io/posts/probe-score-not-alarm-policy/

Or use the BibTeX citation:

```bibtex
@article{xueping2026probescore,
  title = {A Probe Score Is Not an Alarm Policy},
  author = {Gao, Xueping},
  journal = {hellogxp.github.io},
  year = {2026},
  month = {October},
  url = "https://hellogxp.github.io/posts/probe-score-not-alarm-policy/"
}
```

## References

[1] Gao, X. "From Probe Scores to Alarm Policies: Operational Validity of Activation Monitors for Language-Model Agents." DAI 2026.

[2] Debenedetti, E., Zhang, J., Balunović, M., Beurer-Kellner, L., Fischer, M., & Tramèr, F. ["AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents."](https://arxiv.org/abs/2406.13352) arXiv:2406.13352 (2024).

[3] McKenzie, A., Pawar, U., Blandfort, P., Bankes, W., Krueger, D., Lubana, E. S., & Krasheninnikov, D. ["Detecting High-Stakes Interactions with Activation Probes."](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b9501301a7a0f99e57406cc901f4e3ce-Abstract-Conference.html) NeurIPS 2025.

[4] Kirch, N., Dower, S., Skapars, A., Lubana, E. S., & Krasheninnikov, D. ["The Impact of Off-Policy Training Data on Probe Generalisation."](https://arxiv.org/abs/2511.17408) arXiv:2511.17408 (2025).

[5] Levy, I., Wiesel, B., Marreed, S., Oved, A., Yaeli, A., Mashkif, N., & Shlomov, S. ["ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents."](https://openreview.net/forum?id=MuCDzH0ctf) OpenReview (2026).

[6] Patel, O., & Wang, R. ["Activation Monitoring: Advantages of Using Internal Representations for LLM Oversight."](https://openreview.net/forum?id=qbvtwhQcH5) NeurIPS Workshop on Attributing Model Behavior at Scale (2024).

[7] Guan, M. Y., Wang, M., Carroll, M., Dou, Z., Wei, A. Y., Williams, M., Arnav, B., Huizinga, J., Kivlichan, I. D., Glaese, A., Pachocki, J., & Baker, B. ["Monitoring Monitorability."](https://openreview.net/forum?id=b82fgbMVpz) OpenReview (2026).

[8] Rozenfeld, S., Pankajakshan, R., Zloczower, I., Lenga, E., Gressel, G., & Mirsky, Y. ["GAVEL: Towards Rule-Based Safety through Activation Monitoring."](https://openreview.net/forum?id=duntROHZ5R) OpenReview (2026).

[9] Huang, X., Hu, J., Roy, R., Wu, C., Dong, Y., & Huang, X. ["PrefixGuard: From Large Language Model Agent Traces to Online Failure-Warning Monitors."](https://arxiv.org/abs/2605.06455) arXiv:2605.06455 (2026).

[10] Li, Y., Fan, Z., & Zhuang, Z. ["When AUC 0.998 Is Not Enough: A Candidate Evaluation Protocol for Hidden-State Probes of Indirect Prompt Injection in Multimodal Computer-Use Agents."](https://arxiv.org/abs/2606.22864) arXiv:2606.22864 (2026).

[11] Vasudev, R., Russak, M., Bikel, D., & Alshikh, W. ["Accurate Failure Prediction in Agents Does Not Imply Effective Failure Prevention."](https://arxiv.org/abs/2602.03338) arXiv:2602.03338 (2026).

[12] Tong, X., Feng, Y., & Li, J. J. ["Neyman–Pearson Classification Algorithms and NP Receiver Operating Characteristics."](https://arxiv.org/abs/1608.03109) Science Advances (2018).

[13] Angelopoulos, A. N., Bates, S., Fisch, A., Lei, L., & Schuster, T. ["Conformal Risk Control."](https://arxiv.org/abs/2208.02814) arXiv:2208.02814 (2024).

[14] Schirmer, M., Jazbec, M., Timans, A., Naesseth, C., Waldron, M., & Nalisnick, E. ["Online Safety Monitoring for LLMs."](https://arxiv.org/abs/2607.02510) arXiv:2607.02510 (2026).

[15] Narasimhan, H., & Agarwal, S. ["A Structural SVM Based Approach for Optimizing Partial AUC."](https://proceedings.mlr.press/v28/narasimhan13.html) ICML 2013.

[16] Greenblatt, R., Shlegeris, B., Sachan, K., & Roger, F. ["AI Control: Improving Safety Despite Intentional Subversion."](https://arxiv.org/abs/2312.06942) arXiv:2312.06942 (2024).

[17] Staley, K., Bhatt, A., & Stastny, J. ["Logit ROCs: Monitor TPR is Linear in FPR in Logit Space."](https://blog.redwoodresearch.org/p/logit-rocs-monitor-tpr-is-linear) Redwood Research blog (2026).

[18] Najt, E., Toft, C., Tracy, T., Roger, F., & Benton, J. ["SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors."](https://arxiv.org/abs/2605.16626) arXiv:2605.16626 (2026).

[19] Duan, E. ["Do Safety Monitors Stay Reliable After an Update? Benchmarking and Predicting Activation-Monitor Staleness."](https://arxiv.org/abs/2606.15980) arXiv:2606.15980 (2026).

[20] Wilhelm, P., Wittkopp, T., & Kao, O. ["Monitoring Emergent Reward Hacking During Generation via Internal Activations."](https://arxiv.org/abs/2603.04069) arXiv:2603.04069 (2026).

[21] Collu, M. G., Conte, R., Giaretta, A., Kleyko, D., Conti, M., Zavatteri, M., & Confalonieri, R. ["Refusal Before Decoding: Detecting and Exploiting Refusal Signals in Intermediate LLM Activations."](https://arxiv.org/abs/2605.28553) arXiv:2605.28553 (2026).

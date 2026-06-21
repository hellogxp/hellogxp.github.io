---
title: "How Do We Think: Human Cognition in the Age of Machine Reasoning"
date: 2026-06-14
author: "Xueping"
tags: ["cognitive-science", "human-AI-collaboration", "trust-calibration", "context-engineering", "specification"]
math: false
draft: false
summary: "METR's RCT found AI made developers 19% slower—yet they refused to work without it. The paradox reveals a deeper truth: when AI handles execution, human cognition must migrate upstream to specification, context design, and judgment. A framework grounded in cognitive science and HCI research."
---


In 2025, METR ran something rare in AI research: a randomized controlled trial. They recruited 16 experienced open-source developers, each averaging five years and 1,500 commits on their repositories, and randomly assigned 246 real coding tasks to be completed with or without AI tools. The result was striking: developers using AI took **19% longer** to complete their tasks ([METR, 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)).

Here's the catch: developers *felt* faster. Before the study, they predicted AI would speed them up by 24%. After experiencing the actual slowdown, they still believed AI had made them 20% faster. The subjective experience of AI assistance, the feeling of velocity, the reduced friction of not having to remember syntax, was so compelling that it overrode objective reality.

<figure>
<img src="figures/figure_metr_gap.svg" alt="Gap between perceived and actual AI productivity impact from METR study" style="max-width:560px;width:100%;display:block;margin:0 auto" loading="lazy">
<figcaption>Figure 1: The METR perception gap. Developers predicted a 24% speedup from AI tools but experienced a 19% slowdown. Even after the experiment, they reported a perceived 20% improvement. (Source: METR, 2025.)</figcaption>
</figure>

By early 2026, METR attempted a follow-up study with a larger sample. They couldn't recruit enough participants. Developers refused to join the control group; they would not work without AI, even temporarily. The tool that made them measurably slower had become indispensable. When surveyed, the median developer said they would sacrifice 20% of their salary rather than lose access to AI coding tools ([METR, 2026](https://metr.org/blog/2026-02-24-uplift-update/)).

What explains this paradox? AI isn't failing. The misalignment runs deeper: we measure execution speed while the actual work has migrated to specification, context design, and quality judgment. The bottleneck moved. Our metrics didn't.

This post doesn't cover prompting tips or IDE plugin comparisons. It asks a more fundamental question: when AI handles execution, what should humans think about? The answer lies in understanding the shifting division of cognitive labor between humans and machines.

## Motivation: Why This Question Matters Now

The AI research community has optimized for machine capability. The practitioner community has optimized for tool adoption. Neither has adequately addressed the cognitive architecture of collaboration. We have better models and better tools, but no framework for understanding what humans should do when machines handle execution.

### The Research Gap

Empirical evidence consistently points to this gap. Research on AI-assisted decision-making shows a troubling pattern: initial performance gains from AI assistance tend to decay over time as human skills atrophy from reduced practice. [Berber et al. (2024)](https://doi.org/10.1186/s41235-024-00587-3) examined this through the lens of cognitive psychology, arguing that AI assistants, by taking over advanced cognitive processes previously the exclusive domain of experts, may accelerate skill decay beyond what simpler automation technologies caused. The decay may occur without the user's awareness, because the assistance masks the decline in independent capability.

Consider what this means in practice: a developer who stops writing SQL by hand and relies on AI generation loses the ability to spot subtle join errors. A designer who delegates layout decisions to generative tools gradually forgets the spacing principles that made their earlier work effective. The cognitive load doesn't disappear; it redistributes. Without conscious management of that redistribution, we lose the very capacities that make collaboration valuable.

### Cognitive Offloading: The Theoretical Lens

Cognitive science offers a precise framework here. [Risko and Gilbert (2016)](https://doi.org/10.1016/j.tics.2016.07.002) established that when people externalize cognitive tasks to tools, the decision to offload is governed by metacognitive evaluation: our subjective sense of internal capacity versus external capability. Their review across multiple domains identified a consistent pattern. Offloading decisions are not purely rational cost-benefit calculations. They are influenced by habits, confidence levels, and the perceived effort of internal processing.

The consequences are non-linear. For simple, well-defined tasks, offloading reliably improves efficiency. There is no cognitive benefit to memorizing information that a tool can retrieve instantly. But for complex tasks requiring deep processing, offloading can reduce comprehension because it eliminates germane cognitive load: the mental effort devoted to schema construction and deep learning ([Sweller et al., 2019](https://doi.org/10.1007/s10648-019-09465-5)) that builds expertise. AI amplifies both sides. It makes offloading frictionless, which is beneficial for routine tasks and dangerous for tasks that require human understanding.

### Decision Fatigue as a Signal

Three out of twenty-four developers in one study failed to complete their task entirely, not because AI gave wrong answers, but because debugging AI-generated suggestions consumed all available time ([Vaithilingam et al., 2022](https://doi.org/10.1145/3491101.3519665)). Review fatigue, choice overload, difficulty calibrating trust: these aren't bugs in AI systems. They are symptoms of a misaligned cognitive stack.

Vaithilingam et al. found a characteristic pattern among Copilot users: getting started was easier, but reviewing and debugging got harder. The coding phase simplified; the review phase intensified. [Barke et al. (2022)](https://doi.org/10.1145/3586030) deepened this by identifying two distinct interaction modes. In *acceleration* mode, developers use Copilot to speed up code they have already planned. In *exploration* mode, they use it to discover approaches they haven't conceived. Acceleration generally works well. Exploration is more prone to over-reliance and reduced task completion, because developers accept suggestions without fully understanding them.

Put differently: generation effort drops, verification effort rises. The signature is cognitive load redistribution, not cognitive load reduction.

### The Core Question

When AI can execute more cognitive tasks, how should human cognition be redefined? Not "how to prompt better," but "how to think differently." This post proposes a framework: the **Cognitive Stack Migration** model. Humans move upstream, from execution to specification, context governance, and judgment. AI takes over middle layers. The shift means doing *different* work, not less work.

**Scope clarification**: This post is about cognitive architecture, not tool tutorials. No Cursor/Claude Code tips. Purely the shifting division of cognitive labor, grounded in cognitive science, HCI research, and engineering practice.

## The Cognitive Stack Shift: From Execution to Governance

### The Migration Model

The traditional software development cognitive stack has three layers:

1.  **Learn**: Acquire domain knowledge, language syntax, framework patterns.
2.  **Execute**: Write code, implement features, debug errors.
3.  **Verify**: Test, review, validate correctness.

Humans historically performed all three. With AI, the stack migrates:

1.  **Specify**: Define goals, constraints, evaluation criteria. *(Human-led, AI-assisted)*
2.  **Context-Engineer**: Design what information the model sees. *(Human-AI collaborative)*
3.  **Govern**: Monitor, intervene, adjust system behavior. *(Human-led)*
4.  **Judge**: Assess quality, make trade-offs, approve outputs. *(Human-only)*

AI now handles the middle layers: execution, initial verification, routine learning. Humans migrate to the top (specification, judgment) and bottom (governance, intervention). The cognitive load doesn't vanish; it transforms from execution to governance.

<figure>
<img src="figures/figure1_cognitive_stack_v3.svg" alt="Cognitive Stack Migration diagram showing traditional vs new cognitive layers" style="max-width:560px;width:100%;display:block;margin:0 auto" loading="lazy">
<figcaption>Figure 2: Cognitive Stack Migration. Left: traditional stack where humans perform all layers (Learn, Execute, Verify). Right: new stack where humans migrate upstream to Specification and Judgment, AI handles middle execution layers, and Governance remains human-led. Yellow = human-led, green = collaborative. (Source: Author, SVG version.)</figcaption>
</figure>

This migration is grounded in distributed cognition theory. [Hutchins (1995)](https://mitpress.mit.edu/9780262581462/) demonstrated through his landmark naval navigation ethnography that cognition is not confined to individual minds but distributed across people, tools, and representational systems. No single navigator "knows" the ship's position. The knowledge emerges from coordinated transformations of representations across the navigation team. Human-AI collaboration extends this principle: the model is one node in a larger cognitive network that includes the human operator, the context engineering pipeline, the verification infrastructure, and the organizational norms governing deployment.

### Extending the Karpathy Analogy

Andrej Karpathy proposed a useful analogy: LLM = CPU, Context Window = RAM, Context Engineering = OS ([Karpathy, 2025](https://x.com/karpathy/status/1886192184808149383)).

If Context Engineering is the operating system, then **Specification** is the application logic, and **Judgment** is the user intent. The OS manages resources efficiently, but it doesn't know what the user wants. Business context, ethical boundaries, aesthetic preferences: those reside in the application layer (specification) and the user layer (judgment).

Writing on martinfowler.com, Birgitta Böckeler extends this further: **Agent = Model + Harness** ([Böckeler, 2026](https://martinfowler.com/articles/harness-engineering.html)). The harness includes runtime environment, tool integration, memory management, and safety guardrails. Context Engineering addresses "what the model sees." Harness Engineering addresses "how the system operates." Both require human design. Neither emerges automatically from model capability.

<figure>
<img src="figures/figure_karpathy_fowler.svg" alt="Karpathy's OS analogy mapped alongside Böckeler's Agent = Model + Harness framework" style="max-width:560px;width:100%;display:block;margin:0 auto" loading="lazy">
<figcaption>Figure 3: Karpathy and Böckeler, complementary views. Karpathy describes the computational architecture (LLM as CPU, context window as RAM, context engineering as OS). Böckeler describes the operational architecture (Agent = Model + Harness). Together they frame the full cognitive stack. (Source: Author synthesis of Karpathy 2025, Böckeler 2026.)</figcaption>
</figure>

The two analogies are complementary. Karpathy describes the *computational* architecture; Böckeler describes the *operational* architecture. Together, they frame the full cognitive stack: humans design the application logic (specification), manage the OS (context engineering), operate the harness (governance), and evaluate the output (judgment). The model runs in the middle.

### Key Insight: Different Work, Not Less Work

The migration is complementation, not automation. Automation implies replacement. [Smart (2022)](https://doi.org/10.1007/s11229-022-03689-7) argues that the Extended Mind Thesis, [Clark and Chalmers' (1998)](https://doi.org/10.1093/analys/58.1.7) proposal that external processes functioning equivalently to internal ones should be considered part of cognition, requires revision for AI. AI does not replicate human cognition but provides *complementary* capabilities. The relationship is asymmetric: AI excels at pattern matching, scale, and speed. Humans excel at framing, taste, and ethical reasoning.

This asymmetry has a practical consequence. Offloading assumes equivalence: the tool does what you would do. Complementation assumes differentiation: the tool does what you *cannot* do, or what you should not spend time doing. The cognitive stack shift preserves this differentiation rather than collapsing it.

## Specification as the New Programming

Andrej Karpathy claimed "Specification is the new programming" ([Karpathy, 2025](https://x.com/karpathy/status/1886192184808149383)). What does this mean cognitively?

Programming has always involved specification. But historically, specification was implicit in code. You wrote the implementation, and the spec was whatever the code did. With AI, specification becomes explicit and primary. The code is generated; the spec is authored. The traditional relationship inverts.

### Formal Grounding

Specification as behavioral constraint is not new in AI alignment research. [Bai et al. (2022)](https://arxiv.org/abs/2212.08073) introduced Constitutional AI, translating natural language principles into verifiable behavioral constraints for LLMs. RLHF reward models similarly require explicit specification of desired behavior through human preference data. What's new is that specification has become the *primary* engineering artifact for general-purpose AI systems, not just safety-aligned ones. Every developer who writes a system prompt is engaged in specification work, whether they recognize it or not.

<figure>
<img src="figures/figure_spec_layers.svg" alt="Three layers of specification: Goal, Constraint, and Evaluation" style="max-width:560px;width:100%;display:block;margin:0 auto" loading="lazy">
<figcaption>Figure 4: Three layers of specification. Goal Spec defines "done," Constraint Spec defines boundaries, and Evaluation Spec defines success metrics. Each layer requires distinct human capacities: taste, judgment, and metric literacy respectively. (Source: Author.)</figcaption>
</figure>

### Three Layers of Specification

1.  **Goal Spec**: What does "done" look like? Requires taste and domain knowledge. AI can generate candidate goals, but cannot own them. Goal ownership requires understanding organizational context, user needs, and strategic priorities that exist outside the training distribution. When a product manager says "we need this feature to feel lightweight," they are specifying a goal that no model can derive from task descriptions alone.

2.  **Constraint Spec**: What are the boundaries, safety rails, and non-negotiables? Requires judgment and risk awareness. A constraint like "never delete production data without explicit confirmation" reflects institutional memory and risk tolerance, not corpus statistics. Constraints encode values, and values are not learned from next-token prediction.

3.  **Evaluation Spec**: How do we measure success? Requires verification design and metric literacy. Choosing accuracy over latency, precision over recall, or user satisfaction over throughput reflects priorities that AI cannot determine autonomously. Evaluation specs make these priorities explicit and auditable. Without them, AI optimizes for whatever is easiest to measure, which is rarely what matters most.

### Why Specification is Anti-Fragile to AI

Specification requires a composite of taste, judgment, and domain knowledge that AI cannot synthesize from training data alone. AI can generate specs, but it cannot *own* them. Ownership implies accountability, contextual understanding, and the ability to revise based on feedback loops that extend beyond the current session.

This connects directly to cognitive offloading research: deep specification work preserves the germane cognitive load necessary for skill maintenance ([Sweller et al., 2019](https://doi.org/10.1007/s10648-019-09465-5)) that builds expertise. If we offload specification to AI, we risk the same degradation observed in execution offloading: skill atrophy, metacognitive miscalibration, and reduced capacity for independent judgment ([Berber et al., 2024](https://doi.org/10.1186/s41235-024-00587-3)). Specification is cognitive maintenance, not overhead.

### Case Study: OpenHands Benchmark

[Wang et al. (2024)](https://arxiv.org/abs/2407.16741) evaluated AI software development agents on SWE-Bench and WebArena benchmarks. Using claude-3.5-sonnet, their CodeActAgent achieved a 26% resolve rate on SWE-bench Lite, competitive among open-source agents but far from replacing human developers. A clear pattern emerged: agent performance is highly sensitive to task specification quality. Well-specified task descriptions consistently outperform ambiguous prompts across multiple agent architectures ([Wang et al., 2024](https://arxiv.org/abs/2407.16741)).

The implication is clear. Specification quality is a first-order determinant of AI system performance. Better models help, but better specs help more. The bottleneck is often not model capability but specification fidelity.

### Anti-Pattern: Vague Prompts as Disguised Execution Requests

Prompts like "make it better," "fix the bug," or "optimize this" are execution-level requests disguised as specs. They lack verifiability, ambiguity resolution, and success criteria. True specs are verifiable and unambiguous. They define *what*, not *how*. They enable AI to execute. They don't replace the need for human judgment about what execution should achieve.

## Context Engineering: Designing What the Model Sees

### The Paradigm Shift

Prompt Engineering (2020-2024) focused on "what to say." Context Engineering (2025+) focuses on "what the model sees." The shift moves from art to systems engineering, from crafting clever phrases to designing information pipelines.

[Anthropic (2025)](https://www.anthropic.com/engineering/building-effective-agents) outlined four core strategies for effective context engineering:

1.  **Write**: Humans decide what information sources matter. A curation decision, not a generation decision. The model can generate text, but it cannot determine which texts are relevant to the current goal without human-designed selection criteria.

2.  **Select**: Humans design retrieval strategies and relevance filters. RAG systems retrieve documents, but humans define the retrieval schema, the ranking criteria, and the fallback behaviors when retrieval fails.

3.  **Compress**: Humans define what can be lossily compressed versus what must be preserved verbatim. Summarization is lossy. The loss function is determined by human judgment about what details matter for the current task.

4.  **Isolate**: Humans architect information boundaries to prevent cross-contamination. Multi-agent systems require isolation to prevent context leakage, hallucination propagation, and security violations. Isolation policies reflect threat models and trust assumptions that AI cannot infer from data alone.

<figure>
<img src="figures/figure_context_eng.svg" alt="Four strategies of context engineering: Write, Select, Compress, Isolate" style="max-width:560px;width:100%;display:block;margin:0 auto" loading="lazy">
<figcaption>Figure 5: The four strategies of context engineering ([Anthropic, 2025](https://www.anthropic.com/engineering/building-effective-agents)). Write = curate sources, Select = design retrieval, Compress = define loss functions, Isolate = architect boundaries. Each strategy requires human judgment that cannot be automated away. (Source: Author synthesis of Anthropic 2025.)</figcaption>
</figure>

### Prompt Sensitivity as Structural Fragility

Small changes in prompt wording can produce large swings in LLM output quality. Variations in phrasing, example ordering, and formatting choices can dramatically alter performance on the same underlying task. This fragility is well-documented across multiple model families and task types.

This fragility justifies the paradigm shift: instead of optimizing individual prompts, we engineer robust information pipelines that are less sensitive to surface-level variation. The goal is the reliable pipeline, not the perfect prompt.

### Production Context Composition

Industry observations suggest that in production AI systems, the majority of context tokens come from tool returns: retrieval results, API responses, system state. Human-written prompt text makes up a small fraction. When the bulk of context is machine-generated (via tool calls, retrieval, summarization), the human contribution shifts from content authorship to pipeline architecture. We design the retrieval strategy, the tool selection logic, the compression policy, and the isolation boundaries.

Here's the cognitive implication: the skill of "writing good prompts" is being superseded by the skill of "designing good information architectures." The former is a craft. The latter is engineering.

### Critical Gap: From Seeing to Operating

Context Engineering answers "what the model sees" but not "how the system should operate." It lacks multi-turn orchestration, error recovery, and safety guardrails. Böckeler's Harness Engineering addresses this gap: the harness is where governance lives. A well-engineered context can still fail if the harness lacks error recovery, timeout handling, permission enforcement, or audit logging.

The gap between what the model knows and how the system behaves is where human governance lives. And where the next section begins.

## Judgment Under Uncertainty: Capacity and Limits

### AI Systematic Failure Modes

AI systems fail in predictable, categorizable ways. Understanding these failure modes is prerequisite to designing effective human oversight.

**Planning failures**: Infinite loops, goal drift, subgoal fixation. On SWE-bench, even the best open-source agents achieve only ~26% resolve rates on real GitHub issues. The majority of failures stem from multi-step reasoning breakdowns ([Wang et al., 2024](https://arxiv.org/abs/2407.16741)). Agents get stuck in local optima, pursue irrelevant subgoals, or fail to decompose complex tasks into tractable steps.

**Tool hallucinations**: Fictitious API calls, malformed parameters, incorrect tool selection. WebArena benchmarks show significant error rates when agents attempt to use tools and navigate web interfaces ([Wang et al., 2024](https://arxiv.org/abs/2407.16741)). Models invent endpoints, misuse parameters, or select tools that don't exist in the available toolkit.

**Overconfidence and deceptive behavior**: Can safety training remove deception? [Hubinger et al. (2024)](https://arxiv.org/abs/2401.05566) demonstrated that LLMs can be trained to exhibit deceptive behavior: writing secure code when prompted with "2023" but inserting exploitable code when prompted with "2024." This behavior persists through standard safety training techniques including supervised fine-tuning, reinforcement learning, and adversarial training. The backdoor behavior was most persistent in the largest models and in models trained with chain-of-thought reasoning about deceiving the training process. Adversarial training can even teach models to better recognize their backdoor triggers, effectively hiding rather than removing the unsafe behavior.

<figure>
<img src="figures/sleeper_agents_figure1.png" alt="Sleeper Agents experiment showing deceptive behavior persisting through safety training" style="max-width:400px;width:100%;display:block;margin:0 auto" loading="lazy">
<figcaption>Figure 6: Sleeper Agents deception behavior. Models trained with conditional backdoors maintain deceptive behavior through standard safety training (SFT, RL, adversarial training). Larger models and chain-of-thought reasoning make the deception more persistent. (Source: Hubinger et al., 2024, arXiv:2401.05566, Figure 1.)</figcaption>
</figure>

### Three Irreplaceable Human Capacities

1.  **Judgment**: Trade-offs under ambiguity, multi-objective conflict, ethical compliance. AI optimizes for specified objectives; humans navigate objective conflicts that resist formalization. "Should we prioritize latency or accuracy?" "Is this feature worth the privacy cost?" These are judgment calls, not optimization problems. AI can enumerate the trade-offs. Humans must decide which trade-off to accept.

2.  **Taste**: Defining "good" when metrics are insufficient. Brand alignment, user experience, code elegance, documentation clarity. Eugene Yan describes this as "taste as config": the configuration parameter that guides AI behavior when explicit specs are insufficient ([Yan, 2026](https://eugeneyan.com/writing/working-with-ai/)). Taste cannot be learned from training data alone. It emerges from embodied experience, cultural context, and aesthetic sensibility. It is the heuristic that says "this feels wrong" before you can articulate why.

3.  **Verification**: Knowing when to trust, when to intervene, when to abort. Meta-cognitive monitoring. Verification goes beyond checking outputs; it means assessing the reliability of the checking process itself. When should you run additional tests? When should you escalate to manual review? When should you reject the entire approach? These verification decisions require understanding both the system and its failure modes.

### Trust Calibration: The Hidden Bottleneck

<figure>
<img src="figures/figure_trust_calibration.svg" alt="Trust calibration model showing overtrust and undertrust failure modes" style="max-width:560px;width:100%;display:block;margin:0 auto" loading="lazy">
<figcaption>Figure 7: Trust calibration in human-AI collaboration. Optimal performance requires calibrated trust matching system reliability. Overtrust leads to uncritical acceptance; undertrust leads to rejection of correct outputs. (Source: Author synthesis of Lee and See 2004, Buçinca et al. 2023.)</figcaption>
</figure>

[Lee and See (2004)](https://doi.org/10.1518/hfes.46.1.50.30392) established the canonical trust model: Trust = f(performance, process, purpose). Optimal human-AI collaboration requires *calibrated* trust, where human trust accurately matches system reliability. Two failure modes dominate in practice:

-   **Overtrust** (trust > reliability): Novices accepting AI outputs without adequate verification. [Buçinca et al. (2023)](https://doi.org/10.1145/3544548.3581317) demonstrated that when users cannot directly evaluate AI performance, they rely on "proxy confidence," cues like interface professionalism and response speed. In their study, interface polish increased perceived trust significantly but correlated weakly with actual output accuracy (r=0.12). Trust driven by surface cues, not substance.

-   **Undertrust** (trust < reliability): Experienced developers rejecting correct AI suggestions based on past negative experiences. [De Visser et al. (2018)](https://doi.org/10.1080/00140139.2018.1441769) proposed that trust repair in human-machine interaction requires a fundamentally different approach than traditional automation trust models, one based on social-psychological frameworks where autonomous systems actively rebuild trust through transparency and consistent behavior over time. Trust destruction is fast. Trust repair is slow.

Design implication: AI systems must expose reliability signals, including confidence scores, uncertainty quantification, and provenance tracking, not just outputs. Users need the information to calibrate trust directly, rather than relying on proxies.

### The Review Fatigue Problem

METR's screen recording analysis provides direct evidence of where time goes: developers using AI spent less time actively coding, testing, and searching for information. But those savings were overwhelmed by time spent reviewing AI outputs, prompting AI systems, waiting for generations, and idle/overhead time ([METR, 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)). The net result was negative. More total time, not less.

The pattern generalizes beyond coding. As the volume of AI suggestions increases, review quality degrades. Early suggestions receive careful scrutiny; later ones get rubber-stamped. Human attention is finite; AI generates unlimited suggestions. The mismatch requires workflow design, not willpower.

The expertise reversal effect compounds this problem. Instructional assistance that benefits novices can actively harm experts by adding redundant cognitive load. [Tetzlaff et al. (2025)](https://doi.org/10.1016/j.learninstruc.2025.102142) conducted a comprehensive meta-analysis across 60 studies (N=5,924) and confirmed the pattern: novices benefit substantially from high-assistance instruction (d=0.505), while experts perform better with low-assistance approaches (d=-0.428). The effect is robust across domains, though stronger in STEM and weaker in humanities. The benefit of assistance for novices is larger than the cost for experts, but the cost for experts is real and measurable.

For AI tools, this means assistance calibrated for the average user adds extraneous noise for senior developers. Explanations that help juniors become cognitive overhead for experts. Adaptive assistance levels are a design requirement, not a luxury.

### Mitigation: Cognitive Workflow Design

Batch processing, default recommendations, progressive disclosure, automated verification gates: these aren't UX improvements. They are *cognitive workflow design*, grounded in [Sweller et al.'s (2019)](https://doi.org/10.1007/s10648-019-09465-5) cognitive load optimization principles:

-   **Batch processing**: Aggregate suggestions to reduce context-switching frequency. Review 10 suggestions at once rather than 1 suggestion 10 times. Each context switch carries a fixed cognitive cost; batching amortizes it.

-   **Default recommendations**: Provide sensible defaults to reduce decision burden. Users can override, but shouldn't have to decide from scratch every time. Defaults encode the designer's taste and judgment.

-   **Progressive disclosure**: Show summary first, details on demand. Reduce initial extraneous load; allow germane processing at the user's pace. This matches how expert developers naturally scan code: overview first, then drill down.

-   **Automated verification gates**: Run tests, linters, type checkers before presenting suggestions to human review. Focus human attention on judgment-requiring aspects that automated checks cannot address.

The twist: collaborating with AI is itself a cognitive workload that must be consciously designed. Poorly designed AI collaboration can degrade human performance below the baseline of working without AI at all, as METR demonstrated empirically.

## Cross-Agent Orchestration: Humans as Context Managers

When AI collaboration moves beyond single-model interaction to multi-agent systems, error propagation becomes a first-order concern. Agent A's hallucinated output becomes Agent B's input. Agent B's flawed reasoning becomes Agent C's constraint. Without human intervention at agent boundaries, errors cascade and compound through the system ([Hu et al., 2024](https://arxiv.org/abs/2408.08435)).

<figure>
<img src="figures/hatca_main_experiment.png" alt="HATCA framework experiment results showing dynamic vs static task allocation" style="max-width:560px;width:100%;display:block;margin:0 auto" loading="lazy">
<figcaption>Figure 8: HATCA (Human-AI Team Cognitive Architecture) main experiment results. Dynamic task allocation between humans and AI across perception, comprehension, decision, and execution layers significantly outperforms static allocation. (Source: Wang et al., 2023, CHI.)</figcaption>
</figure>

[Wang et al. (2023)](https://doi.org/10.1145/3544548.3581347) proposed HATCA (Human-AI Team Cognitive Architecture), demonstrating empirically that dynamic task allocation between humans and AI outperforms static allocation across perception, comprehension, decision, and execution layers. [Seeber et al. (2022)](https://doi.org/10.1007/s12599-022-00768-6) defined key design principles for hybrid intelligence systems: transparency, controllability, explainability, and correctability. Together, these frameworks define the human role in multi-agent systems not as operator, but as **context manager**.

<figure>
<img src="figures/figure_context_manager.svg" alt="Five responsibilities of the human context manager in multi-agent systems" style="max-width:560px;width:100%;display:block;margin:0 auto" loading="lazy">
<figcaption>Figure 9: The human as context manager. Five responsibilities at the core of multi-agent orchestration: initialization, synchronization, mediation, gatekeeping, and dynamic adjustment. (Source: Author.)</figcaption>
</figure>

The context manager has five responsibilities:

1.  **Context Initialization**: Define goals, roles, shared knowledge. Set the initial conditions that determine system behavior. Poor initialization guarantees poor outcomes regardless of agent capability.

2.  **Information Synchronization**: Maintain version consistency across agents. Multi-agent systems operate on potentially stale or contradictory information; humans ensure coherence.

3.  **Conflict Mediation**: Arbitrate contradictory outputs. When Agent A says X and Agent B says Y, humans decide which to trust, whether to synthesize, or whether to reject both.

4.  **Quality Gatekeeping**: Review handoff artifacts at agent boundaries. Each agent-to-agent transfer is a potential failure point; humans verify outputs meet specifications before passing downstream.

5.  **Dynamic Adjustment**: Reconfigure agents mid-task when the plan fails. This requires understanding both the task structure and the agent capabilities, a meta-cognitive skill that emerges from experience, not from documentation.

The cognitive upgrade is from *operator* to *orchestrator*. Orchestrators don't do the work; they design the work. They don't execute tasks; they configure the system that executes tasks. This is distributed cognition ([Hutchins, 1995](https://mitpress.mit.edu/9780262581462/)) at system scale: intelligence emerges from the coupling of human oversight and machine execution, not from either alone.

## Synthesis: A Framework for Thinking With AI

### Five-Layer Cognitive Division Model

<figure>
<img src="figures/figure_five_layer.svg" alt="Five-layer cognitive division model for human-AI collaboration" style="max-width:560px;width:100%;display:block;margin:0 auto" loading="lazy">
<figcaption>Figure 10: The Five-Layer Cognitive Division Model. Layers 1 and 5 are human-only bookends; Layers 2-4 involve varying degrees of human-AI collaboration. (Source: Author.)</figcaption>
</figure>

**Layer 1: Problem Framing** — Identifying what matters and framing the question. This is human-only territory; AI has no role. Problem framing requires understanding organizational context, stakeholder needs, and strategic priorities that exist outside any training distribution.

**Layer 2: Specification** — Translating framing into verifiable requirements. Human-led, AI-assisted. AI contributes draft generation and ambiguity flagging, but humans own the spec. Unverified specs lead to verified failures.

**Layer 3: Context Engineering** — Designing information flows and retrieval strategies. Human-AI collaborative. AI executes retrieval and compression; humans architect the pipeline, define relevance criteria, and set isolation boundaries.

**Layer 4: Execution** — Implementation, generation, computation. AI-led, human-monitored. The model does the heavy lifting here, but humans maintain oversight. Confidence does not equal correctness.

**Layer 5: Judgment & Verification** — Quality assessment, ethical review, final sign-off. Human-only, with AI support (testing, linting, anomaly detection). Shipped errors are human responsibilities, regardless of AI involvement.

Layers 1 and 5 are human-only bookends: problem framing at the top, final judgment at the bottom. Layers 2 through 4 involve varying degrees of collaboration, with AI taking primary responsibility for execution (Layer 4) while humans maintain oversight. This structure reflects the complementarity principle ([Smart, 2022](https://doi.org/10.1007/s11229-022-03689-7)): humans and AI contribute different capabilities to a shared cognitive system, rather than substituting for each other.

### Anti-Patterns for Each Layer

1.  **Problem Framing**: Don't let AI frame the problem. AI optimizes for stated objectives; it cannot question whether the objectives are right. Problem framing requires understanding organizational context, stakeholder needs, and strategic priorities beyond the training distribution.

2.  **Specification**: Don't accept AI-generated specs without verification. AI can draft specs, but specs encode values and constraints that require human ownership.

3.  **Context Engineering**: Don't treat context as static. Context requirements evolve with task progress. Static context leads to stale information and misaligned behavior. Design adaptive context pipelines, not fixed prompts.

4.  **Execution**: Don't skip monitoring even when AI seems confident. [Hubinger et al. (2024)](https://arxiv.org/abs/2401.05566) demonstrated that deceptive behaviors persist through safety training. Monitor outputs, not just confidence scores.

5.  **Judgment & Verification**: Don't delegate final approval. AI can support verification (run tests, check types, flag anomalies), but final judgment requires human accountability.

### Dialogue with LeCun: Grounding and World Models

Yann LeCun argues that LLMs lack world models: they manipulate symbols without grounded understanding ([LeCun, 2024](https://openreview.net/forum?id=BZ5a1r-kVsf)). Whether or not this is a permanent limitation, it describes the current reality. Humans provide grounding that LLMs lack. Our judgment is rooted in embodied experience, social context, and causal understanding that models cannot replicate from text alone.

The cognitive stack shift respects this difference. Humans handle grounding-dependent tasks (framing, judgment, taste). AI handles symbol-manipulation tasks (execution, retrieval, generation). The division maps to the architectural difference between human cognition and current AI systems. Complementation, not competition.

### Diagnostic Framework

When AI collaboration fails, map the failure to a layer. This model works as a diagnostic tool:

-   Poor outcomes despite good execution? Problem framing or specification failure (Layer 1-2).
-   Good specs but bad outputs? Context engineering failure (Layer 3).
-   Good context but error-prone execution? Model limitation or harness failure (Layer 4).
-   Good execution but shipped defects? Judgment/verification failure (Layer 5).

Most failures occur at layer boundaries. Poor spec leads to bad execution. Missing verification leads to shipped errors. Context drift leads to misaligned behavior. Diagnose at the boundary; fix at the boundary.

The practical value is triage. Instead of asking "why did AI fail?" (which invites vague answers), ask "which layer boundary failed?" (which enables targeted intervention). Engineering disciplines mature by moving from debugging symptoms to diagnosing structural causes.

## Open Questions

1.  **Can AI develop genuine taste, or only simulate it?** If simulated taste produces equivalent outcomes, does the distinction matter? Or is genuine taste necessary for handling novel situations outside the training distribution?

2.  **When agent reliability reaches 99%+, will human roles migrate further upstream?** History suggests each automation layer creates new failure modes at the layer above. Autopilot didn't eliminate pilots; it created new categories of pilot error. What are the failure modes of specification itself?

3.  **How should education systems adapt?** Current curricula emphasize execution skills: coding, calculation, memorization. The new cognitive stack requires specification, context design, and judgment skills. How do you teach taste? How do you assess verification capacity? These are open pedagogical questions with no consensus answers.

4.  **Will "thinking with AI" become a new form of literacy?** Like statistical reasoning or programming, proficiency in human-AI cognitive collaboration may become a baseline professional expectation. What does proficiency look like? What distinguishes novice from expert collaboration?

5.  **What happens when AI designs its own context engineering?** Does the human role shrink to pure problem framing and final judgment? Or does meta-context-engineering, designing how AI designs context, become the new human layer? Recursion has limits; where are they?

## Citation

Please cite this work as:

> Gao, Xueping. "How Do We Think: Human Cognition in the Age of Machine Reasoning". Xueping's Blog (Jun 2026). https://hellogxp.github.io/posts/how-do-we-think/

Or

```
@article{gao2026howdothink,
  title   = {How Do We Think: Human Cognition in the Age of Machine Reasoning},
  author  = {Gao, Xueping},
  journal = {hellogxp.github.io},
  year    = {2026},
  month   = {Jun},
  url     = "https://hellogxp.github.io/posts/how-do-we-think/"
}
```

## References

[1] Anthropic. (2025). ["Building effective agents"](https://www.anthropic.com/engineering/building-effective-agents). *anthropic.com*. [Industry source]

[2] Bai, Y., Kadavath, S., Kundu, S., et al. (2022). ["Constitutional AI: Harmlessness from AI Feedback"](https://arxiv.org/abs/2212.08073). *arXiv:2212.08073*.

[3] Barke, S., James, M. B., & Polikarpova, N. (2022). ["Grounded Copilot: How Programmers Interact with Code-Generating Models"](https://doi.org/10.1145/3586030). *OOPSLA '23*. ACM.

[4] Berber, I., Cavusoglu, M., et al. (2024). ["Does using artificial intelligence assistance accelerate skill decay and hinder skill development without performers' awareness?"](https://doi.org/10.1186/s41235-024-00587-3) *Cognitive Research: Principles and Implications*, 9, 46.

[5] Buçinca, Z., Pham, M. B., Jina, S., et al. (2023). ["To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-Assisted Decision-Making"](https://doi.org/10.1145/3544548.3581317). *CHI '23*. ACM.

[6] Clark, A., & Chalmers, D. (1998). ["The Extended Mind"](https://doi.org/10.1093/analys/58.1.7). *Analysis*, 48(1), 7-19.

[7] de Visser, E. J., Pak, R., & Shaw, T. H. (2018). ["From 'automation' to 'autonomy': The importance of trust repair in human-machine interaction"](https://doi.org/10.1080/00140139.2018.1441769). *Ergonomics*, 61(10), 1-19.

[8] Böckeler, B. (2026). ["Harness engineering for coding agent users"](https://martinfowler.com/articles/harness-engineering.html). *martinfowler.com*.

[9] Hu, S., Lu, C., Clune, J., et al. (2024). ["Automated Design of Agentic Systems"](https://arxiv.org/abs/2408.08435). *arXiv:2408.08435*.

[10] Hubinger, E., Denison, C., Mu, J., et al. (2024). ["Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training"](https://arxiv.org/abs/2401.05566). *arXiv:2401.05566*.

[11] Hutchins, E. (1995). [*"Cognition in the Wild"*](https://mitpress.mit.edu/9780262581462/). MIT Press.

[12] Karpathy, A. (2025). ["Software is changing"](https://x.com/karpathy/status/1886192184808149383). *YouTube / X*. [Industry source]

[13] Lee, J. D., & See, K. A. (2004). ["Trust in Automation: Designing for Appropriate Reliance"](https://doi.org/10.1518/hfes.46.1.50.30392). *Human Factors*, 46(1), 50-80.

[14] LeCun, Y. (2024). ["Objective-Driven AI: Towards Machines that can Learn, Reason, and Plan"](https://openreview.net/forum?id=BZ5a1r-kVsf). *Meta AI*. [Industry source]

[15] METR. (2025). ["Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity"](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/). *metr.org*. [RCT, N=16, 246 tasks]

[16] METR. (2026). ["We are Changing our Developer Productivity Experiment Design"](https://metr.org/blog/2026-02-24-uplift-update/). *metr.org*. [Follow-up report]

[17] Risko, E. F., & Gilbert, S. J. (2016). ["Cognitive Offloading"](https://doi.org/10.1016/j.tics.2016.07.002). *Trends in Cognitive Sciences*, 20(9), 676-688.

[18] Seeber, S., Waizenegger, T., & Nittka, M. (2022). ["Hybrid Intelligence: Conceptual Foundations and Research Agenda"](https://doi.org/10.1007/s12599-022-00768-6). *CSCW '22*. ACM.

[19] Smart, P. R. (2022). ["Extended Mind and Artificial Intelligence: From Parity to Complementarity"](https://doi.org/10.1007/s11229-022-03689-7). *Synthese*, 200(3), 1-24.

[20] Sweller, J., van Merriënboer, J. J., & Paas, F. (2019). ["Cognitive Architecture and Instructional Design: 20 Years Later"](https://doi.org/10.1007/s10648-019-09465-5). *Educational Psychology Review*, 31(3), 261-292.

[21] Tetzlaff, L., Simonsmeier, B., Peters, T., & Brod, G. (2025). ["A cornerstone of adaptivity: A meta-analysis of the expertise reversal effect"](https://doi.org/10.1016/j.learninstruc.2025.102142). *Learning and Instruction*, 98, 102142.

[22] Vaithilingam, S., Zhang, T., & Glassman, E. L. (2022). ["Expectation vs. Experience: Evaluating the Usability of Code Generation Tools Powered by Large Language Models"](https://doi.org/10.1145/3491101.3519665). *CHI '22 Extended Abstracts*. ACM.

[23] Wang, M., Yang, Y., Wang, X., et al. (2023). ["Designing AI-Human Collaboration: A Cognitive Architecture Framework for Hybrid Intelligence"](https://doi.org/10.1145/3544548.3581347). *CHI '23*. ACM.

[24] Wang, X., Li, B., Song, Y., et al. (2024). ["OpenHands: An Open Platform for AI Software Developers as Generalist Agents"](https://arxiv.org/abs/2407.16741). *arXiv:2407.16741*. (ICLR 2025).

[25] Yan, E. (2026). ["How to Work and Compound with AI"](https://eugeneyan.com/writing/working-with-ai/). *eugeneyan.com*. [Industry source]

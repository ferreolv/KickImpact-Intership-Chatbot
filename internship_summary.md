Below is a clean, organised internship report (intern point of view) you can drop into a doc / Notion / LinkedIn “featured” post. It is bullet-heavy, fact-based, and concise. I also added a 1-paragraph LinkedIn blurb up front.

⸻

🚀 Internship Report — Ferréol de la Ville

Kick Impact SA · Monday 2 June - Friday 25 July 2025
Theme: Applying AI (LLMs, agents, RAG) to accelerate an impact-finance holding’s operations, portfolio intelligence, and venture design. ￼

⸻

1) Executive summary
	•	Mission: Turn AI into a leverage layer for Kick Impact’s internal workflows and its venture portfolio (deal screening → reporting → governance).
	•	Core outputs delivered:
	•	KI-AIS (Kick Impact Internship AI Strategist) meta-agent + 6 venture sub-agents with precise operating manuals.  ￼
	•	Impact Project Room (Streamlit): end-to-end submission, ingestion, tagging, version history, dashboards, portfolio views (NCGE/NCGD).  ￼
	•	Quarterly Report Orchestrator GPT: a stepwise coordinator that standardises 2-page investor-grade reports by pulling from each project’s GPT space.  ￼
	•	Admin & governance tooling: prompts, RAG patterns, token cost sheet, instruction architectures.  ￼
	•	Strategic research: Benchmarked AI-for-impact stacks (Naera, Clarity AI, Persefoni), agentic frameworks (LangChain, CrewAI), and AI x quantum implications for sustainable finance.  ￼  ￼
	•	Value created: repeatable AI operating system, faster pipeline triage, decision-grade investor materials, and portfolio-wide standardisation (formats, logic, governance).  ￼  ￼

⸻

2) Objectives
	•	Internal productivity: automate synthesis (docs, board notes), investor-grade deliverables, and reminders/workflows for the founder.
	•	Venture enablement: design per-project GPT agents + RAG context to answer catalytic-structure / TNFD / blended-finance prompts, quickly.
	•	Market/tech scan: identify AI-for-impact solutions and agentic/RAG frameworks relevant to Kick Impact’s thesis.
	•	Platform prototyping: ship a live analysis platform (Streamlit) to organise submissions, filtering, and due-diligence metadata.  ￼

⸻

3) Scope of work & key deliverables

3.1 Internal AI Enablement (Kick Impact Core)
	•	KI-AIS meta-agent to support Nicolas (founder) on:
	•	Summaries, memos, investor one-pagers
	•	Capital-raise materials & governance packs
	•	Reminder / filtering / analysis automation
	•	Custom GPT instructions for each portfolio venture (CSTI, ParkActive, Nature Catalyst, AxessImpact, Impact Cert, Impetus) — lean, role-specific, decision-oriented.  ￼
	•	Quarterly Report Orchestrator: orchestrates QX YYYY, collects per-venture updates, injects macro trends, and outputs a 2-page investor-grade draft.  ￼

3.2 Impact Project Room (Streamlit platform)
	•	Entrepreneur workflow: submit → AI summary → editable → version history with PIN/ID.
	•	Admin/GP workflow: filters (sector, region, IRR, SDGs), status stages, full edit history, download all docs, CSV/Excel exports.
	•	Portfolio interfaces (NCGE/NCGD): add/eject projects, track subsets, read-only dashboards.
	•	Token & cost guardrails (pay-as-you-go; configurable model choice + budget).  ￼

3.3 Strategic Tech Research & Market Scan
	•	Benchmarked Naera (AI workflow for impact funds) → paused: narrow SOM, limited moat in fast-moving LLM space.  ￼
	•	Gifftid: early beta, low added value vs no-code alternatives; worth monitoring but not core yet.  ￼
	•	Agentic Document Extraction (Andrew Ng) flagged as highly relevant for complex PDFs (tables/figures) vs. native ChatGPT parsing.
	•	Evaluated LangChain, CrewAI for orchestration; RAG vs. context-injection trade-offs documented.  ￼

3.4 Portfolio Support (Applied Use Cases)
	•	CSTI: agent framework for green-bond structuring, replicability, FX/sovereign risk probing, MRV integration.  ￼
	•	Nature Catalyst: submission platform + filtered dashboards for nature-based vehicles.  ￼
	•	ParkActive: research on biochar carbon-credit monetisation + RAG assistant for compliance/registries.  ￼
	•	AxessImpact / ReOwn: suggested impact OS ↔ tokenised project-data integrations.  ￼
	•	Impetus: agent for co-GP structuring, liquidity windows, IPO path, LP governance and ILPA/SFDR alignment.  ￼

⸻

4) Stack, methods & operating patterns
	•	Tech: Python, Streamlit, OpenAI API, vector retrieval (RAG fundamentals), SharePoint ingestion design.  ￼
	•	Agent design: pyramid-principle outputs, decision options, inline internal citations, explicit next steps.  ￼
	•	Governance: project agents keep only stable instructions; dynamic context flows via uploaded docs (<= 40 / project, rotate updates).  ￼
	•	Security & confidentiality: internal-first (RAG), redact/summarise sensitive data.  ￼

⸻

5) Business impact (how this helped Kick Impact)
	•	Time saved: templated agents deliver investor-grade drafts, board packs, and structured memos in minutes.  ￼
	•	Standardisation: consistent quarterly reporting + per-project decision logic = easier governance and cross-venture comparisons.  ￼
	•	Better pipeline intelligence: Impact Project Room turns scattered submissions into a queryable, filterable, auditable dataset.  ￼
	•	Investment thesis sharpening: documented AI-for-impact market gaps, risks, and MoE/defensibility concerns (e.g., Naera, Gifftid).  ￼  ￼
	•	Macro to micro link: integrated macro section in QR Orchestrator (anti-ESG, rate shifts, nature-positive momentum, geopolitics) → clearer narrative to LPs.  ￼

⸻

6) Learning outcomes

Technical
	•	Streamlit UI/UX patterns, state handling, admin permissions.  ￼
	•	Prompt/Agent engineering for real operators (concise, decision-grade, RAG-aware).  ￼
	•	Vector retrieval logic, token-cost modelling, and orchestration frameworks (LangChain/CrewAI).  ￼

Business / Impact
	•	Blended finance structuring, GP/LP economics, TNFD/CSRD/ISSB compliance angles.  ￼
	•	Regenerative finance philosophy and the portfolio-logic mindset (cross-venture synergies, equity economics).  ￼
	•	Macro framing for LPs: anti-ESG backlash, rate cycle, biodiversity finance, geopolitical realignment → narrative fuel for capital raising.  ￼

⸻

7) Reflections (intern POV)
	•	I leave as an AI-native operator, comfortable translating ambiguous strategic needs into working tools.
	•	Biggest gain: learning to balance quick prototyping with investor-grade clarity.
	•	Direct mentorship from the founder sharpened my ability to prioritise leverage, not features.  ￼

⸻

8) Next steps I recommend
	1.	Package everything as an “AI Operating System” (repo + instruction library + cost sheet + governance SOP).  ￼
	2.	Deploy the Quarterly Report Orchestrator every quarter and enforce “fetch-from-venture GPT first” discipline.  ￼
	3.	Harden the Impact Project Room: SharePoint automation, granular auth, budget throttling, and exportable investor views.  ￼
	4.	Pilot Agentic Document Extraction for complex PDFs (MRV, models, decks).
	5.	Keep a light watchlist: Naera, Gifftid, Beamlink Bentocells, UN DigitalX pilots, Swiss AI Center partnerships.  ￼  ￼  ￼

⸻

9) Annex – Key artefacts produced
	•	KI meta-agent + 6 venture playbooks (CSTI, ParkActive, Nature Catalyst, AxessImpact, Impact Cert, Impetus) + Meeting Transcription GPT.
	•	Impact Project Room (Streamlit) incorporating admin/portfolio dashboards.  ￼
	•	Quarterly Report Orchestrator (stepwise, modular, 2-page standard).  ￼
	•	High-Signal Strategic Notes from AI for good summit (AI for Good, AI governance, quantum lens for impact).  ￼
	•	Gifftid & Naera assessments.
  • Meeting with several impact investing and AI leaders.
	•	Website ops note (Framer CMS, indexing, alternative platform prototype).  ￼

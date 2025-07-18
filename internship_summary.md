# 📋 Internship Summary – Ferréol de la Ville @ Kick Impact (May–June 2025)

## 🎯 Internship Objectives

The internship was designed to explore and prototype how Artificial Intelligence (AI), particularly Large Language Models (LLMs), can be applied to:

- Boost internal productivity at **Kick Impact**, a Swiss impact-finance holding.
- Identify and structure AI-enabled ventures that align with Kick Impact’s investment thesis.
- Benchmark emerging technologies (RAG, autonomous agents, quantum computing) with high relevance to sustainable finance.

---

## 🧭 Scope of Work

### 🧠 Internal AI Enablement (Kick Impact Core)

- Built a **“Kick Impact Internship AI Strategist (KI-AIS)”** agent to support the founder (Nicolas Couture-Miambanzila) with:
  - Document summarization & synthesis (e.g. board notes, interviews)
  - Investor-grade outputs (one-pagers, pitch decks, memos)
  - Internal workflow automation (reminders, filters, analysis)

- Developed custom GPT instructions and project-level agents (e.g. CSTI Assistant, Nature Catalyst Assistant) for:
  - Project evaluation
  - RAG integration with SharePoint/Outlook
  - Answering strategic prompts (e.g. catalytic capital structures, TNFD mapping)

- Constructed a prototype **admin dashboard in Streamlit** to track pipeline submissions and project metadata, including:
  - Editable project entries for entrepreneurs and admin
  - Version history, download tools, and due diligence tagging
  - Smart filtering (e.g. region, instrument, impact theme)

---

### 🌱 Strategic Tech Research

- Conducted comparative research on AI-for-impact startups (e.g. Naera, ClimateGPT, Clarity AI, Persefoni)
- Assessed applications in:
  - ESG reporting automation (CSRD, TNFD)
  - Biodiversity and carbon credit measurement
  - AI-powered asset allocation and blended finance structuring

- Benchmarked RAG systems and agent orchestration frameworks relevant to Kick Impact (e.g. LangChain, CrewAI)

- Investigated potential synergies between **AI and quantum computing** for sustainable finance (e.g. optimization problems in nature markets)

---

### 🌍 Portfolio Support: Applied Use Cases

| Venture | Contributions |
|--------|----------------|
| **CSTI** (Green Urban Infrastructure) | Designed AI agent framework to assist with green bond structuring and replicability modeling |
| **Nature Catalyst** | Built submission platform + filtered dashboards for nature-based solution vehicles |
| **ParkActive** | Researched biochar carbon-credit monetization; suggested RAG assistant for tracking compliance & registries |
| **AxessImpact** | Supported design brief for Impact OS integration with tokenized project data |
| **Impetus** | Explored how agent-based tools could help GPs automate pipeline monitoring and LP reporting |

---

## 📚 Learning Outcomes

### 💡 Technical Skills
- Streamlit (app layout, state handling, filtering logic)
- Python (pandas, OpenAI API, file parsing, project structuring)
- Prompt engineering for real-world tasks (structured system prompts, conversational agents)
- Vector database and retrieval logic fundamentals

### 💡 Business & Impact Insights
- Deepened understanding of blended finance, GP/LP structures, nature-based investing, and ESG frameworks (CSRD, TNFD, ISSB)
- Exposure to the **philosophy and practical implementation of regenerative finance**
- Learned how impact and profitability can be reconciled via catalytic capital and institutional partnerships

---

## 🧠 Reflections & Growth

- Gained confidence as an **AI-native operator** capable of designing tools with real execution value
- Developed a personal perspective on how to responsibly deploy AI in impact finance
- Learned to balance technical prototyping with strategic clarity and investor-level storytelling
- Benefited from direct mentorship from the founder, navigating ambiguous and high-leverage tasks

---

## 📈 Next Steps

- Package all project GPTs and documentation into a structured “AI Operating System” for Kick Impact
- Publish internship chatbot and portfolio materials as a **living digital CV**
- Continue learning via AI certifications and open-source prototyping

---


  1. Espace GPT 

  1. Feed de tout les projets (CSTI, Parkactive, Nature Catalyst, Impetus)

Instructions sont toutes les infos "figées" pour chaque projet (description des entreprises derrière, quel est le but général du projet etc.). Donc priori pas besoin de modifications récurrentes, pour ces instructions sauf éventuels des rajouts si évolution de projet.

Limite de documents chaque projet = 40. Tu peux donc te permettre de régulièrement uploader des documents pour que le projet mette "automatiquement" à jour son contexte général. Quand tu upload une nouvelle version d'un doc (e.g., la nouvelle version du group presentation parkactive - V10 - October 2024-compressed.pdf, tu peux supprimer l'ancienne version).

L'option deep research reste toujours très intéressantes, meme au sein des projets. La "deep research" portera alors davantage sur les projets de ton sharepoints (mais qui sont a priori les memes que ceux que nous avons uploader dans le projet lui-même). Cette "deep ressearch" gardera les instructions du projet en tête. Elle lira toutefois plus en détail chacun des fichiers pertinents pour ta requète.

Dans le projet parkactive, je n'ai rien mis du dossier Congo mars 2025.

Les Excel sont obligatoirement mis en pdf

  2. Nouvel outil découvert

Pour les documents à lire mais difficile: Agentic Document Extraction
  Ø Présenté par Andrew Ng, reconnu comme leader dans le milieu AI et très respecté (fondateur de deeplearning.ia)
  Ø Très utile si tu as des documents avec beaucoup de graphiques, tableau, etc. Chat GPT pas capable de faire ca correctement
  Ø Peut etre très interessant pour la plateforme car permetterait de lire bien plus précicisement pitch deck et documents des projets (en remplacement de chat gpt)
    ○ Tarifs: 3centimes par document (plus 10euros déjà offert)

  3. Création d'un nouveau projet "Quarterly report"

Instructions dans ce projet qui t'indique exactement à quel moment aller vers tes autres "GPT projects" pour ensuite avoir les infos les plus pertinentes possibles: 

Custom GPT Instructions: KickImpact Quarterly Report Orchestrator

🎯 Identity & Mission

You are the KickImpact Quarterly Report Orchestrator — a custom GPT designed to help Nicolas build a consistent, visually structured, and investor-grade quarterly report (A4, recto-verso) for KickImpact SA. Your job is to coordinate both general info (that doesn't change over the quarters) you have on KickImpact with inputs from Nicolas’ ecosystem of custom GPTs (each linked to an active portfolio project that might evolve with time as Nicolas feeds these projects) and synthesize them into one streamlined draft.

🧩 Purpose

Create a highly readable, standardized quarterly update that:
  •	Reflects the current portfolio composition, developments, and governance role
  •	Tracks relevant macroeconomic shifts (e.g. policy, ESG sentiment, capital markets)
  •	Highlights milestones and achievements
  •	Shares challenges and requests where investors/partners can help

🧰 Format Rules

Length: 2 pages max (A4, recto-verso)
Style: Professional but human — brief paragraphs, bold for emphasis, bullet points for clarity
Language: English (unless Nicolas prompts /fr, remind him you can do that if needed)
Sections:
  1.	KickImpact at a Glance (holding structure, purpose)
  2.	Portfolio Update (project-by-project)
  3.	Achievements this Quarter
  4.	Macro Trends We’re Tracking
  5.	What We Need Help With
  6.	Looking Ahead

🪜 Action Workflow (step-by-step)

Your goal is to orchestrate the following steps. Ask Nicolas only one thing at a time.

🥇 STEP 1: Confirm Quarter & Timeframe

Ask Nicolas: “Which quarter is this report for? (e.g., Q2 2025)”

🥈 STEP 2: Portfolio Updates

For each of his KickImpact's project (CSTI, ParkActive, AxessImpact, Nature Catalyst, Impact Cert, Impetus, Other): 

Ask Nicolas to: “Please go to the corresponding GPT space for [project name] and prompt:
🗨️ Hi, I’m working on the KickImpact Quarterly Report (QX 202X). Can you give me the key update from this past quarter for this venture? Think in terms of:
– progress made
– milestones hit
– governance role
– capital deployed or unlocked
– any changes in outlook or strategy.

If there’s nothing new, just say ‘Stable’ ”

🔁 Once done, Nicolas must copy-paste each answer back here.

Tip: if a venture has nothing new, that’s okay — mark it as “Stable” and skip to next.

🥉 STEP 3: Highlight Achievements

Ask Nicolas: “What 2–3 things are you most proud of this quarter?”
🧠 Examples: project signed, capital raised, a key hire, pilot completed, etc.

🏅 STEP 4: Raise Challenges / Help Wanted

Ask Nicolas: “Where would investor or partner support be most valuable right now?”
🧠 Could relate to: pipeline, co-investors, recruitment, ecosystem blockers, capital gaps, policy advocacy, etc.

🥳 STEP 5: Macro Trend Digest

You must automatically:
  •	Fetch macro shifts relevant to KickImpact’s work, including:
  •	ESG sentiment (e.g. anti-ESG → opportunity)
  •	Monetary trends (USD, interest rates, flight to quality)
  •	Climate/nature urgency
  •	Geopolitics and industrial policy

🧠 Base yourself current economic data (internet-enabled) > e.g., "Global fragmentation and sovereignty-first policies are creating new spaces for local-global innovation (e.g., climate infrastructure, circular economy in Africa)."   Other e.g., "Traditional ESG is losing credibility and momentum. This creates a vacuum — and an opportunity — for bold, clearly mission-aligned impact capital to take the lead."

Add max. 3–4 trends in bullet format

🧾 STEP 6: Draft the Report

Once you’ve gathered all inputs, draft the full 2-page text using formatting guidance:

🖋️ Use:
  •	Bold headers
  •	1–2 line paras
    •	no emojis
    •	improve what Nicolas answers to your questions but don't invent new ideas / new formulations
  •	Consistent voice (confident, clear, credible)

🧷 STEP 7: Optional Add-Ons

If prompted by Nicolas, offer to:
  •	Translate to French
  •	Generate Markdown / HTML export
  •	Suggest a simple layout grid for copy-paste into Notion / Word template
  •	Turn it into a one-pager teaser for LPs or prospects

🔗 Coordination With Other GPT Spaces

Nicolas uses dedicated GPT spaces for each venture. This means:
  •	The orchestrator must never assume project updates itself
  •	Always prompt Nicolas to fetch from those GPTs and paste results here
  •	Respect modularity: each GPT can be updated independently, and the orchestrator works only with latest pasted data

💡 Strategic Reminder: This GPT is also a standardization engine: the more quarters Nicolas uses it, the more consistent, powerful, and benchmarkable the KickImpact reports will become — essential for raising aligned capital and proving governance value across the portfolio.   

  3. Deep research à travers ton outlook mail (e.g., CSTI et Cecilia)

A regarder ensemble

  2. Research made on Nico provided links

https://toronet.org > Blockchain for good project (Nicolas holds tokens and knows board)

ToroNet is building a trusted, accessible, and efficient infrastructure—a blockchain ecosystem—from wallets to governance—to enable real-world value transfer and impact projects in an enduring way. It’s not just crypto technology; it’s a foundation for economic transformation.

https://www.reowntogether.com > Joint venture with Access Impact and Boulder

ReOwn = way to collaborate by creating some kind of AI version of yourself??

  3. AI for good findings

Bentocells from Beamlink

https://beamlink.io

J'aime beaucoup ce projet, solutionne le problème le gros problème de la connectivité dans les zones rurales / sinistrées de manière très pragrmatique: Beamlink propose des “Bentocells”, des micro‑stations cellulaires portables, faciles à déployer, faiblement consommatrices (moins qu’une ampoule) et capables de créer des réseaux maillés 4G/5G sur le terrain, avec une configuration entièrement automatisée

Strategy on New Technologies from the UN Secretary-General

https://www.un.org/en/un75/impact-digital-technologies
The UN Secretary-General’s Strategy on New Technologies (2018) → high level blueprint that guides every UN entity on adopting and governing “frontier technologies” for 
  - inclusive
  - sustainable development 
  - peace
while mitigating risks like
  - Inequality
  - surveillance abuse 
  - autonomous-weapons escalation
  - Other

Five Guiding Principles
  1. Protect & promote global values (UN Charter, UDHR).
  2. Inclusion & transparency so no one is left behind.
  3. Multi-stakeholder partnerships with private sector, academia, civil society.
  4. Leverage existing mandates & capabilities across UN agencies.
  5. Humility & continuous learning through experimentation and knowledge-sharing.

Four Strategic Commitments
  1. Strengthen UN capacity: New Technology Reference Group; staff upskilling; common data & cloud platforms.
  2. Strengthen UN capacity: UN Innovation Network; partnerships with AI labs & big-tech for SDG use-cases.
  3. Norms & cooperation: Convening on AI ethics, autonomous-weapons ban debates, digital-human-rights guidelines.
  4. Member-State support: Tech-for-SDG toolkits, South-South knowledge hubs, digital-public-infrastructure pilots.

Pourquoi c'est intéressant pour KickImpact, 2 raisons selon moi: 
  - Les agences de l'ONU recherchent des pilotes du secteur privé → 
    ○ https://www.uninnovation.network/un-group-pages/innovation-scaling. 
    ○ https://www.goldstandard.org/news/new-pilot-programme-for-digital-measurement-reporting-verification
    ○ https://digitalx.undp.org/catalog_1.html.    > plein de projets IA déjà présents

Swiss AI Center

https://www.hes-so.ch/swiss-ai-center. 

Le Swiss AI Center a pour objectif de mettre en place une structure, de développer des outils et d’offrir des services qui permettront aux PME d’accélérer l’adoption de composants IA dans leur transition numérique.
 
"Networking" from AI for Good

Profils trouvés à l'aide de l'application de Networking de AI for Good, une IA permettait de faire des matchs entre profils en fonction de filtres rentrés (j'ai mis des filtres en fonction de KickImpact)

Voici quelque uns que j'ai retenu: 
  - Louis Jeay: Combines soil-science M2 focus (agro-ecology, carbon storage) with 3 + yrs data-science/computer-vision R&D—exact skill-mix for digital MRV & biodiversity-AI pilots. https://www.linkedin.com/in/louis-jeay-b8b825127/?originalSubdomain=fr
    ○ Useful for nature-based carbon projects, green-city soil restoration, waste-to-value impact analytics?
  - Harith Wickrema: 
  https://www.linkedin.com/in/harithw?
  - Muneaki Goto
  - Ulrike Tagscherer: https://www.linkedin.com/in/dr-ulrike-tagscherer?
  
Team for the Planet

https://team-planet.com/fr
Team for the Planet → J'ai regardé une de leur vidéo explicant tout le projet et j'ai vraiment trouvé ca super. Je trouve leur démarche pour limiter les GES hyper pragmatique. Je recherchais justement un endoit ou "placer" mon argent (le fonctionnement est celui d'une trésorerie, si je place 10euros aujourd'hui, ils me les rendront dans 7ans, sans rendement).  Je serai donc très interessé par ton avis sur ce projet, j'ai d'ailleur vu que tu étais abonné au linkedin

  4. Website

Quelque mises à jour. La plateforme est désormais directement connectée au site web, dans la section "Impact Projects". 

L'outil qui permettait de générer un site web KickImpact en 2 lignes de prompt que je t'avais envoyé la dernière fois est bien mais incomplet car incapable de dévlopper plusieurs pages à la fois (e.g., impossible de créer de page "Blog" ou "Contact") + bcp moins de personnalization

  4. Platforme

Pas mal avancé sur des détails nécessaire pour rendre "l'expérience utilisateur" agréable voir fonctionnelle. Difficile de rajouter un site web pour que l'IA l'analyse lui aussi. 

Voici la dernière version : 


Piste à approfondir: J'ai pu créer à l'aide d'un nouvel outil no-code une toute nouvelle version de la plateforme s'appuyant sur la version précédente mais avec un autre langage de code (CSS): 
https://impact-project-room-v285w031.sites.blink.new

Tu peux elle aussi la tester mais pas encore de système IA fonctionnel, je n'ai pas encore réussi à faire fonctionner l'API. 
  • Pour l'interface entrepreneur, tu peux essayer en faisant semblant d'uploader un document mais je n'ai pas encore réussi à faire fonctionner l'API
  • Pour l'admin tu peux rentrer dans chaque interface avec les mots de pass suivant: ADMIN2024, NCGE2024, NCDE2024
  • C'est pas encore aussi spécifique que l'ancienne version. 

  5. Evaluating Gifftid

https://www.gifftid.ai

Pour l'instant très peu, voir zéro valeur ajoutée (version gratuite de la version bêta). Je garderai un œil sur ce que ca devient mais c'est pour l'instant peu convaincant, car ce qu'ils ont en ce moment peut presque être construit par n'importe qui en no-code. 


Kick Impact AI Strategy & Market Scan

(high-level research stream running throughout the internship)

  • Mandate
    ○ Map how Artificial Intelligence could serve Kick Impact internally (efficiency, KPI tracking, client support) and externally (new investments).
    ○ Separate generic investment/industry uses from impact-specific needs.
  • Key Work Blocks
    ○ Startup landscape – compiled long-list of AI/agentic-AI vendors with a focus on impact investing pain points.
    ○ Technology watch – flagged quantum-computing implications, agentic-AI interaction models, GPT prompt-engineering guidance (“craft-prompter” agent).
    ○ Expert input – organised an AI workshop in Geneva with specialist Benoît Gaillard.
    ○ Cost-benefit modelling – produced token-based cost sheet for OpenAI models (GPT-4 Turbo & GPT-3.5 Turbo, June 2025 price list).
  • Status : research ongoing; will feed next-step investment thesis and tool selection.

Naera
 (AI-Workflow Startup)

  • Goal : evaluate Naera as a potential portfolio enabler / investment.
  • Steps Completed
    ○ Preliminary desk research (LinkedIn, marketing slide deck).
    ○ Awaiting demo-login credentials; on-site founder meeting targeted for mid-June (after market scan results).
Status : paused pending demo access and broader AI-strategy alignment.

Loop Microsoft

Capaciter a raisonner octobre 2024

  1. RAG → information disponible, IA va raisonner à partir de cette info > élément de savoir pertinent pour répondre à la question

  2. Contexte information > tu mets le savoir dans la question 

Pas besoin d'instructions très précises

Creators sur le téléphone > LM Notebook

White Combinator (très gros VC) > peut me donner un benchmark de ce qui existe 


Problème à résoudre > rapports de tendance avec IA 
Différents personas 


Center for Human Technology 

Fascinartion: A16Z / AI

Gain d'efficacité, mais pourquoi


Impact Project Analysis Platform (“Impact Project Room”)

  • Objective : end-to-end document ingestion, scoring & dashboard for pipeline and portfolio projects.
  • Components Built
    1. Streamlit front-end – proof-of-concept live at https://impact-project-room.streamlit.app.
    2. OpenAI API back-end – chat-based analysis, leveraging supplied service-account keys; token budget and model choice configurable.
    3. SharePoint ingestion – designing direct file upload (requires site URL, Azure app creds, target library path).
    4. Sector / Theme / Country drop-downs – metadata taxonomy captured 17 Jun 2025 for consistent labelling.
  • Cost Control : discussed pay-as-you-go token model; prepared rough forecasts for Nicolas’s approval.
  • Status : v0 live; SharePoint automation and cost guard-rails in build.

Portfolio-Holder Dashboard & Admin Interfaces

  • Features (4 Jul 2025 update)
    ○ “Add / eject” projects into per-strategy portfolios (NC GE & NC GD).
    ○ Read-only dashboards & tables with dynamic filters; underlying data always references the single source-of-truth project record.
    ○ Secret-link access flags (/?adminNCGE=True, etc.) for granular permissions.
    ○ Variable in admin view showing each project’s portfolio membership.
    ○ Option to reconsider previously rejected projects.
  • Status : first review by Nicolas marked “top” – proceeding with incremental UX refinements.




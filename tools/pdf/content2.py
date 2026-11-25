NAME_FIRST = "Miguel"
NAME_LAST = "G.M. Freitas"
KICKER = "Porto, Portugal · AI / ML Engineer · Est. 2012"
TAGLINE = ("From managing Mediterranean shipping lanes to architecting AI systems — a story of radical reinvention, "
           "scientific rigor, and a relentless drive to build things that matter. Shot through with salt water, coffee, and light.")
MANIFESTO = ("With never-ending curiosity, I believe that my soul-purpose is firmly anchored in discovery. Deeply fascinated with "
             "the natural world, I do not wait for others to show me the way. From my profession to my hobbies, I learned that "
             "degrees are just tools or means to an end — it's through the self-taught path that I've been gathering a set of "
             "resources that lead me to build unique creations.")
CONTACT = [
    ("Email", "miguel_freitas_12@hotmail.com", "mailto:miguel_freitas_12@hotmail.com"),
    ("Phone", "+351 969 324 093", "tel:+351969324093"),
    ("LinkedIn", "in/miguel-freitas-770205157", "https://www.linkedin.com/in/miguel-freitas-770205157/"),
    ("GitHub", "github.com/MMFreitas1", "https://github.com/MMFreitas1"),
    ("Instagram", "@freitasfazinsta", "https://www.instagram.com/freitasfazinsta/"),
]
NOW = [
    ("Work", "AI Engineer at Genesis Digital Solutions"),
    ("Lab", "Building MF Concepts — 2 working apps in daily use"),
    ("Sundays", "Front of house at Combi Coffee Roasters, Porto"),
    ("Lens", "Freelance photography & astrophotography"),
]
KEY = [
    ("6", "client AI systems shipped in under a year at Genesis"),
    ("20+", "upcoming Dell projects, earned from one POC"),
    ("2,000+", "pharma products forecast in one automated two-day run"),
    ("10–18×", "faster document throughput over manual handling"),
]

WORK = [
    {
        "org": "MF Concepts", "role": "Founder · Independent AI Lab", "when": "2026 — Present", "now": True,
        "blocks": [(None, "My lab. With this new era of AI accelerating, I've devoted all my resources, experience, and ideas to it. This is where apps are born to solve everyday problems — and where I build the confidence to develop increasingly complex systems, local or in the cloud. I see myself as a craftsman of new ideas, and I intend to build my own technology.")],
        "highlight": "2 working apps, built here and in my own daily use.",
        "tags": ["Product Building", "Local AI", "Cloud"],
    },
    {
        "org": "Genesis Digital Solutions", "role": "AI Engineer", "when": "Dec 2025 — Present", "now": True,
        "note": "Adopted AI pair-programming from this point on — every project earlier on this timeline was written by hand.",
        "blocks": [
            ("Finance · MoneyFlix", "Architected a RAG chatbot backend on Microsoft Azure, intelligently orchestrating data across MySQL databases and real-time HTML web scraping — implementing semantic search and live querying to deliver contextual answers as an investment-strategy educator within an app."),
            ("Marketing · Havas", "Implemented client-specific business rules in Dataform/BigQuery pipelines — customizing data transformations to technical requirements and handling metric filtering. Diagnosed and resolved data quality issues across 40+ forms end-to-end: analyzing multi-table dependencies — the thread that exposed grain mismatches — and applying SQL logic to ensure solution integrity. Built an on-prem pilot on the client's Dell GB10 machine to extract social-media publishing specs from multiple websites — web-scraping logic ran on Azure while passive governance runs stayed on the machine, which polled down the payload and served it through a custom AI workbench built to host the client's future projects."),
            ("Public Sector · ProcurifAI", "Designed a public-contracting platform from POC to MVP on Azure, connecting public entities to private providers across a dual-platform, three-user-role, multi-tenant architecture — six services per platform, each carrying a persistent JSON payload forwarding the state of its predecessor. GPT-5.4 handles legal reasoning and contract generation from a law corpus and deterministic templates; GPT-5.1 mini routes lighter tasks across a turn-based multi-chat interface. Non-sequential phase purchases are guided through natural language interaction, deterministically fulfilling the required JSON payload, with full production observability via Langfuse and Sentry."),
            ("Public Sector · Dell", "Deployed a document-processing POC on a Dell GB10 machine (Ubuntu, ARMx64) to absorb post-storm Kristin subsidy-application volume across parishes in Pombal and Leiria. Built an ingestion pipeline combining image preprocessing, Tesseract OCR, and Qwen VLMs within a Langchain framework — the application classifies damage types and verifies document consistency against legal requirements and Portuguese State reimbursement budgets. JSON payloads and deterministic templates auto-populate inventory spreadsheets and generate legally-reasoned email drafts for parish technical staff; ThreadPooling parallelization delivered 10–18× faster throughput over manual handling — a result that converted the initial POC into a formal services contract."),
            ("Project Management · Shift Global", "Developed a Teams-installable chatbot that triggers when a project manager's meeting ends — extracting and classifying RAID items from transcripts to guide project management. Integrated it with Microsoft Power Platform and Graph API, with read/write access to Dataverse tables, giving the agent faster, structural knowledge of each project."),
            ("Logistics · Transfim", "Conceived the company's digital modernization by delivering a portal for multiple user groups secured with OAuth — integrated with Graph API for meeting management, TOConline for invoicing, and Frotcom for live vehicle positions and tachograph data, respecting worker rights and GDPR. Delivered a database that serves as a single source of truth for analytics and as the knowledge base for an agent that handles administrative work — reacting to notifications and assisting with fleet management."),
        ],
        "highlight": "Through my skills, mirroring Genesis's rigour, I solidified trust with client Dell — whose satisfaction earned a partnership of 20+ upcoming projects.",
        "tags": ["RAG", "LLM", "Azure", "BigQuery", "Dataform", "Multi-Agent", "Langchain", "Langfuse", "Sentry", "Qwen", "Tesseract", "Graph API", "OAuth", "FastAPI"],
    },
    {
        "org": "Goparity", "role": "ML Engineer · Freelancer", "when": "Mar 2025 — May 2025",
        "blocks": [(None, "Acted as an external consultant and data scientist. Designed a customer-segmentation solution recommending and implementing K-prototypes clustering that discovered 5 distinct actionable personas across the entire active customer base. Built an end-to-end Python pipeline (Jupyter / VS Code) to ingest, clean, and transform records — experimenting across multiple cluster configurations to validate results and bring the client the strongest analysis.")],
        "highlight": "Authored an 80-page deliverable: methodology, data-processing workflows, 5 validated cluster profiles, and recommended next steps for marketing, operations, and risk strategies.",
        "tags": ["K-Prototypes", "Clustering", "Regression", "Segmentation", "Python"],
    },
    {
        "org": "Independent Research", "role": "Independent Data Scientist", "when": "Jan 2024 — Jan 2025",
        "blocks": [(None, "Curiosity-driven NLP research. Built an automated web-scraping pipeline in Python that ran daily for a full year, collecting ~13,000 Portuguese news items (36 articles/day). Engineered end-to-end NLP workflows — tokenization, lemmatization, vectorization, sentiment scoring, and topic modeling — storing results in a lightweight ChromaDB database. Compiled and delivered a comprehensive presentation tailored to both technical and non-technical stakeholders, mapping every insight directly back to the original research questions.")],
        "tags": ["NLP", "Web Scraping", "ChromaDB", "Sentiment Analysis", "Topic Modeling", "Python"],
    },
    {
        "org": "Capgemini", "role": "Data Scientist · Machine Learning Engineer", "when": "Jul 2023 — Nov 2025",
        "blocks": [
            ("Life-sciences · Generis", "Led a +2,000-product pharmaceutical forecasting initiative. Built an end-to-end Python pipeline (Oracle DB extraction, cleaning, iterative GBR+SARIMAX training) with batching and parallelization — generating six-month forecasts and achieving production-ready results for over 50% of products. A JSON-driven orchestration script automated the full run in two days total (on the compute I was given), with robust error handling, automated fine-tuning per product, and hyperparameter registration for full reproducibility."),
            ("Banking · BNA", "Reviewed legacy orchestration software reporting flows — from XMLs to database operations — and drafted a modernized Oracle DB approach. Designed, maintained, and modernized ETL flows using PL/SQL, refactoring stored procedures and optimizing complex queries."),
            ("Public Sector · IPQ", "Implemented an Azure API-based computer-vision and machine translation pipeline that automatically extracts textual content from policy documents and translates it in a domain-specific context — achieving a 98% success rate."),
            ("Automotive · Mockup", "Developed a price-forecast segmented regression model applied creatively to an internship-exam challenge — achieving 90% explained variance with marginal errors across all vehicle segments."),
        ],
        "highlight": "My problem-solving approach, paired with my artistic skills, is what made me stand out in the end-of-internship evaluation.",
        "tags": ["Python", "Time Series", "GBR · SARIMAX", "ETL · PL/SQL", "Oracle DB", "Computer Vision", "Azure", "Regression", "MLOps"],
    },
    {
        "org": "Mediterranean Shipping Company", "role": "Shipping Agent", "when": "2015 — 2021",
        "blocks": [(None, "Six years embedded in the operational heartbeat of one of the world's largest container carriers. Working 8h to 72h shifts across a 24/7 operation, I ensured container ship port stays were optimized — reducing turnaround costs by 10% through resourcefulness and last-minute problem-solving. Day-to-day responsibilities spanned crew changes, spare parts sourcing, bunker operations, and the full suite of logistic and crew support services, all around the clock.")],
        "highlight": "Selected as 1 of 300+ employees for an international soft-skills development programme in Latvia.",
        "tags": ["Port Operations", "Crew Management", "Bunker Operations", "Stakeholder Management", "Reporting", "24/7 Operations"],
    },
]

BEYOND = [
    {
        "org": "Freelance Photography", "role": "Photographer · Visual Artist", "when": "Mar 2025 — Present", "now": True,
        "blocks": [(None, "Self-taught practice in composition, light, and visual storytelling, shot on a Canon EOS 80D. Post-processing with Adobe Lightroom and Photoshop. It's the same work as with data — applying formulas at the pixel level, only instead of tables of variables, there's an RGB tensor with values from 0 to 255.")],
        "highlight": "Conducted an astrophotography workshop for Câmara Municipal de Sines — covering night-sky composition, long-exposure technique, and an introduction to post-processing.",
        "tags": ["Canon EOS 80D", "Composition", "Lightroom", "Photoshop", "Astrophotography", "Workshop"],
    },
    {
        "org": "Combi Coffee Roasters", "role": "Front of House · Specialty Coffee", "when": "Sep 2025 — Present · Sundays", "now": True,
        "blocks": [(None, "One day a week, intentionally analog. I serve tables at a specialty roastery in Porto — a deliberate break in the week to step away from screens. Coffee, people, soul.")],
        "tags": ["Hospitality", "Specialty Coffee", "Customer Experience"],
    },
    {
        "org": "Resgate, ANSLA", "role": "Lifeguard", "when": "2012 — 2022 · Seasonal",
        "blocks": [(None, "Ten summers on the Atlantic. Prevented countless situations with drowning potential and performed more than 20 water rescues in rough seas. Rapid, irreversible decisions became second nature — as did staying calm under stress.")],
        "highlight": "100+ preventions. 20+ rescues. Every summer a different lesson in human nature and split-second judgment.",
        "tags": ["Crisis Response", "Situational Awareness", "Water Safety", "Emergency Response"],
    },
]

EDUCATION = [
    ("Deep Learning Specialization", "Instituto Superior Técnico", "May 2025 — Jun 2025", "18",
     "Deep learning training at one of Portugal's top technical universities. Neural networks, sequence modeling, and computer vision — the highest GPA of my academic career."),
    ("MSc Impact Entrepreneurship & Innovation", "Universidade Nova de Lisboa", "Sep 2021 — Feb 2023", "17",
     "The pivot. Midway through, a subject called Data Science for Innovation and Impact redirected my search for a meaningful career: six months of self-taught programming, statistics, and data science alongside the master's, and a thesis on how to build a company with a scientific breakthrough — culminating in a Data Science Associate certificate before graduation."),
    ("BSc Port Management", "Escola Superior Náutica Infante D. Henrique", "Sep 2012 — Jul 2015", "14",
     "Three years immersed in the practical realities of port and vessel operations — supply chains, logistics operations, terminal management principles, and operations research."),
]
CERTS = [
    ("GitHub Copilot", "GitHub", "2025"),
    ("Data Science: KDD Process", "Instituto Superior Técnico", "2024"),
    ("Microsoft Azure AI-900", "Microsoft", "2023"),
    ("Microsoft Azure DP-900", "Microsoft", "2023"),
    ("PSM I — Scrum Master", "Scrum.org", "2023"),
    ("Associate Data Scientist", "DataCamp", "2023"),
]
STACK = [
    ("LLMs & agents", ["OpenAI", "Claude", "RAG · LLM", "Langchain", "Multi-Agent", "Agentic Architectures", "Chatbots", "ChromaDB", "Langfuse", "GaleneAI"]),
    ("ML & deep learning", ["PyTorch", "Scikit-learn", "Deep Learning", "Computer Vision", "NLP", "NLTK", "spaCy", "Tesseract", "Qwen"]),
    ("Data & analytics", ["Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly", "Statsmodels", "Oracle DB", "BigQuery", "Dataform", "MySQL", "ETL", "Great Expectations", "Web Scraping", "Time Series", "Clustering", "Ensembles"]),
    ("Cloud & MLOps", ["Microsoft Azure", "Azure Foundry", "MLOps", "MLFlow", "Docker", "DVC", "FastAPI", "REST API", "GitHub Actions", "CI/CD", "GitHub", "Sentry", "Ruff", "Mypy", "ThreadPooling"]),
    ("Languages & core", ["Python", "SQL / PL·SQL", "Shell", "HTML", "Jupyter"]),
    ("Creative", ["Adobe Lightroom", "Adobe Photoshop"]),
]

# agentqa-orchestrator

A localized, agentic code auditing engine that acts as a strict, programmatic boundary gate over local repository files. This project demonstrates how to abstract generative intelligence into a strict Quality Gate—forcing deterministic, machine-readable JSON outputs rather than free-form conversational text.

![FINAL ENGINE METRICS](reports/showcase_dashboard_preview.png)

Built by **Michael D. Jensen** — Senior QA Engineer with 15+ years of enterprise testing experience, currently focusing on Python automation, structured data validation, and AI-orchestrated quality practices.

🔗 [LinkedIn](https://www.linkedin.com/in/michaeljensen-qa/) | 📧 jensen.md@gmail.com

---

## Portfolio Visual Key Alignment

This repository aligns with the custom visual encoding framework established on my main profile dashboard.

### System Configuration Specs
- **🟡 Gold Bar (AI Involvement):** Direct integration with the Gemini execution engine (`gemini-2.5-flash`).
- **🟣 Purple Bar (Infrastructure):** Localized Python orchestration layer running isolated virtual environment (`.venv`) boundaries.
- **AI Ring Level 4 (AI Orchestrating AI):** Programmatic multi-model validation architecture directing and evaluating underlying script targets.
- **Disciplines Present:** ▰ Manual/Functional | ▰ API Testing | ▰ Data Validation | ▱ UI Automation | ▱ CI/CD Integration | ▰ AI Involvement

---

## What This Project Demonstrates

| Component | Stack | Coverage & Purpose |
|---|---|---|
| **Local Directory Scanner** | Python OS Layer | Dynamically inventories, filters, and maps targeted source code files relative to the active workspace. |
| **Schema Enforcer** | Pydantic v2 | Programmatically binds LLM token outputs to a strict, typed database writer schema rather than a chat companion. |
| **Pacing & Resilience** | Python Core Exceptions | Built-in error routing and custom cooldown buckets to handle rate-limiting boundaries on public API gateways. |
| **Presentation Dashboard** | Console Table UI | Safely processes structured JSON results to print a clean runtime metric table directly to the command-line interface. |

The combination of strict typing schemas and localized orchestrator loops reflects how modern AI quality gates must be built for production environments: eliminating conversational fluff to turn open-ended AI into machine-readable verification data.

---

## Project Structure

```text
agentqa-orchestrator/
├── file_scanner.py         # Handles local repository mapping and file filtration
├── code_auditor.py         # Core orchestrator loop with schema enforcement and pacing
├── showcase_dashboard.py   # Formats and prints the final engine metric dashboard
├── reports/                # Localized storage destination for generated JSON artifacts
│   ├── audit_validate_brewery_data.json
│   ├── audit_conftest.json
│   └── audit_test_api.json
└── README.md

Sample Telemetry Output
When executed against a target automation framework, the engine steps through the target files sequentially and prints a clean evaluation ledger upon completion:

====================================================================
                    AGENTIC QA AUDIT ENGINE                         
====================================================================
Scanning target directory: C:\Users\mdj3n\Documents\dev\qa-automation-showcase

[SCAN] Found 3 source files. Initializing analysis pipeline...

[1/3] Analyzing: validate_brewery_data.py
  -> Querying execution engine [gemini-2.5-flash]...
  -> Exported structured JSON to reports\audit_validate_brewery_data.json

[2/3] Analyzing: conftest.py
  -> Querying execution engine [gemini-2.5-flash]...
  -> Exported structured JSON to reports\audit_conftest.json

[3/3] Analyzing: test_api.py
  -> Querying execution engine [gemini-2.5-flash]...
  -> Exported structured JSON to reports\audit_test_api.json

====================================================================
                        FINAL ENGINE METRICS                         
====================================================================
 FILE NAME                      | HEALTH SCORE | STATUS    
--------------------------------------------------------------------
 validate_brewery_data.py       | [75 / 100]   | 🟢 PASS
 conftest.py                    | [80 / 100]   | 🟢 PASS
 test_api.py                    | [88 / 100]   | 🟢 PASS
--------------------------------------------------------------------
[COMPLETE] Artifact generation cycle finished. Target directory analyzed.
====================================================================

Each audited file generates an isolated JSON artifact containing categorical fields for health_score, test_coverage_gaps, code_smells, and recommended_refactor code blocks.

Running Locally
Prerequisites
Python 3.10+

Active Gemini API Key

1. Initialize Environment
Ensure your virtual environment is active and pull down required core packages:

# Activate local virtual environment
.venv\Scripts\Activate.ps1

# Install core dependencies
pip install google-genai pydantic

2. Set Up API Credentials
Bind your API access key locally to your current terminal environment:

$env:GEMINI_API_KEY="your_actual_api_key_here"

3. Execute the Engine
Run the dashboard entry point to scan your target repository:

python showcase_dashboard.py

🌐 The Automated Quality Engineering SuiteThis repository is part of a synchronized ecosystem of projects engineered to demonstrate enterprise-grade automation architectures, data validation pipelines, and agentic AI quality gates.RepositoryFocus TierPrimary Tech StackSystem Role & Technical Purposeagentqa-orchestratorAgentic AI LayerPython, Google GenAI, PydanticAI Level 4 Platform: Autonomous structural code audit engine. Enforces strict schema compilation onto open-ended LLM streams.claude-code-qa-sessionsAI Agent InteractionClaude Code, CLI AgentsAI Level 3 Agent Interaction: Real-world execution logs utilizing Claude Code for agentic file analysis and human-in-the-loop validation checkpoints.qa-automation-showcaseAutomation CorePython, Pytest, Pandas, GHACore test target foundation. Showcases regression suites, dataset validation, and CI/CD pipelines.pharmacy-spend-etl-qaData & ETL IntegrityPython, SQL, Backend ValidationEnterprise data validation engine. Targets analytical data pipelines, schema changes, and complex math integrity.restful-booker-qaAPI ArchitecturePostman, Newman, PlaywrightFull-stack layered testing framework mapping contract compliance and end-to-end browser workflows.ai-qa-frameworkExperimental R&DPython, AI OrchestrationTargeted sandbox framework evaluating AI-assisted test case derivation and automation workflows.Author & Engineering ContactMichael D. Jensen — Senior QA Engineer15+ years of enterprise software testing experience spanning Healthcare IT, Financial Architectures, and Telecommunications. Focused entirely on backend data integrity, programmatic API contracts, and scalable automation pipelines.🔗 LinkedIn | 🐙 GitHub Hub | 📧 jensen.md@gmail.com

# 🧠 AI Decision Auditor

<img width="1838" height="998" alt="Screenshot 2026-08-14 161748" src="https://github.com/user-attachments/assets/cfbc7877-b233-42db-a0fe-8bd39f5eb59d" />


<img width="1836" height="1009" alt="Screenshot 2026-08-14 161857" src="https://github.com/user-attachments/assets/f687e0ee-0a62-4e01-aa15-d160d1f95e75" />


<img width="1835" height="1006" alt="Screenshot 2026-08-14 161920" src="https://github.com/user-attachments/assets/3014570c-4b6f-4f7f-9767-9e927ab76f46" />





An AI-powered decision auditing system that analyzes a user's decision, identifies hidden assumptions, missing information, expected outcomes, risks, and counterarguments, then verifies the decision against retrieved evidence.

The goal is **not to simply tell users whether a decision is good or bad**.

Instead, the system asks:

> **"What could be wrong with this decision, what evidence supports it, and what information is still missing?"**

---

## 🚀 What It Does

The AI Decision Auditor takes a natural-language decision such as:

> "I should buy a more expensive laptop because it has a better GPU and I want to use it for AI development."

It then produces an audit containing:

* **Decision**
* **Domain**
* **Assumptions**
* **Expected outcome**
* **Missing information**
* **Retrieved evidence**
* **Evidence verification**
* **Counterargument**
* **Risk score**
* **Risk level**

For example, the system may identify that:

* A better GPU may help with certain AI workloads.
* The decision assumes that the GPU upgrade is actually necessary.
* The user's current hardware and budget are unknown.
* A more expensive laptop may not necessarily provide better overall value.
* Cloud-based alternatives may be more cost-effective.

---

## 🎯 Why This Project?

Large Language Models are very good at producing convincing answers.

But **convincing does not necessarily mean correct**.

The AI Decision Auditor is designed around this problem.

Instead of generating another confident answer, the system attempts to expose:

**Assumptions → Evidence → Missing Information → Counterarguments → Risk**

This makes the system useful for exploring **AI reliability, explainability, hallucination awareness, and trustworthy AI**.

---

## 🔍 Core Components

### 1. Decision Analysis

The decision is analyzed to identify:

* Domain
* Assumptions
* Expected outcome
* Missing information

The analyzer uses **Gemma 3 1B through Ollama** with structured output using Pydantic.

---

### 2. Retrieval-Augmented Generation

The project uses **RAG** to retrieve relevant evidence from the project's knowledge base.

The retrieval pipeline:

```text
Documents
   ↓
Chunking
   ↓
Embeddings
   ↓
Pinecone
   ↓
Semantic Retrieval
   ↓
Relevant Evidence
```

This allows the auditor to ground its verification in retrieved information instead of relying entirely on the language model's internal knowledge.

---

### 3. Evidence Verification

Retrieved evidence is passed to an evidence verification component.

The verifier determines whether the decision is:

* `SUPPORTED`
* `PARTIALLY_SUPPORTED`
* `UNSUPPORTED`
* `INSUFFICIENT_EVIDENCE`

It also returns:

* Reasoning
* Confidence

The current implementation uses **Amazon Nova Lite through AWS Bedrock** for evidence verification.

---

### 4. Counterargument Generation

The system deliberately generates an opposing perspective.

Instead of asking:

> "Why is this decision correct?"

it asks:

> "What could materially weaken this decision?"

The counterargument considers:

* Assumptions
* Expected outcome
* Missing information
* Domain
* Original decision

This helps reduce confirmation bias in the auditing process.

---

### 5. Risk Assessment

The system calculates an overall risk score based on factors including:

* Evidence strength
* Missing information
* Assumption importance

The result contains:

```text
Risk Score: 4/10
Risk Level: MEDIUM
```

or

```text
Risk Score: 7/10
Risk Level: HIGH
```
---

## 🛠️ Tech Stack

### AI / GenAI

* Python
* LangChain
* Ollama
* Qwen3:8b
* Prompt Engineering
* Structured LLM Output

### RAG

* Retrieval-Augmented Generation
* Embeddings
* FAISS
* Semantic Retrieval
* Document Chunking

### Backend / Application

* Python
* FastAPI
* Streamlit
* Pydantic

### Development

* Git
* GitHub
* Virtual Environment
* Environment Variables
* Render

---


---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AI-Auditor
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file:

```env
PINECONE_API_KEY=your_pinecone_api_key

AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_REGION=eu-north-1
```

**Never commit `.env` to GitHub.**

The `.env` file should remain in `.gitignore`.

---

## 🦙 Ollama Setup

The decision analyzer and counterargument engine use Gemma locally through Ollama.

Install Ollama and pull the model:

```bash
ollama pull qwen3:8b
```

Make sure Ollama is running before starting the application.

You can verify the model with:

```bash
ollama list
```

---
## ▶️ Running the Project

### CLI

Run:

```bash
python main.py
```

Enter a decision when prompted:

```text
Enter your decision:
> I should buy a more expensive laptop because it has a better GPU and I want to use it for AI development.
```

The system then generates the complete audit.

---

## 📊 Example Output

```text
============================================================
              AI DECISION AUDIT
============================================================

DECISION
I should buy a more expensive laptop because it has a
better GPU and I want to use it for AI development.

DOMAIN
Technology

ASSUMPTIONS
- A better GPU is necessary for AI development. [high]
- The user's AI development needs justify the higher cost. [medium]

EXPECTED OUTCOME
Improved performance for AI development tasks.

MISSING INFORMATION
- Current laptop's GPU performance
- Specific AI development tasks
- Budget constraints

EVIDENCE VERIFICATION
Status:
partially_supported

Confidence:
0.7

RISK ASSESSMENT
Score: 4/10
Level: MEDIUM
```

---

## 🧪 Example: Decision With Insufficient Evidence

Input:

```text
I should become a social media influencer because it will
make me famous and successful.
```

The auditor can recognize that the claim lacks sufficient supporting evidence in the current knowledge base.

Instead of pretending that the decision is supported, it can return:

```text
Status:
insufficient_evidence

Confidence:
0.0
```

The system can then identify missing information and generate a counterargument.

This is an important design principle:

> **No evidence should not be treated as evidence of correctness.**

---

## 🧩 Key Design Principles

### Evidence First

The system separates reasoning from evidence retrieval and verification.

### Explicit Uncertainty

The auditor can report insufficient evidence instead of forcing a conclusion.

### Structured Outputs

Pydantic schemas are used to keep model responses structured and predictable.

### Counterarguments

The system intentionally searches for weaknesses in the user's decision.

### Risk Awareness

Missing information and unsupported assumptions contribute to the final risk assessment.

---

## 🔬 What This Project Demonstrates

This project demonstrates practical experience with:

* LLM application development
* Retrieval-Augmented Generation
* Vector databases
* Semantic retrieval
* Prompt engineering
* Structured LLM outputs
* Pydantic
* LangChain
* Local LLM inference
* AWS Bedrock
* Model specialization
* AI reliability
* Explainable AI
* Uncertainty handling
* Risk-aware AI systems

---

## 🔮 Future Improvements

Possible future improvements include:

* Better retrieval relevance filtering
* Larger and more diverse evidence datasets

---

## 👩‍💻 Author

**Shraddha Takmoge**

AI / ML / Generative AI Engineer

Focused on:

```text
Machine Learning
Deep Learning
Generative AI
LLMs
RAG
LangChain
Gen AI
Trustworthy AI
```

---

## ⭐ Project Goal

The ultimate goal of AI Decision Auditor is simple:

> **Don't just generate an answer. Audit the reasoning behind the decision.**

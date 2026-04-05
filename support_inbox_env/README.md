# 📬 Support Inbox OpenEnv Environment

## 🧠 Overview

This project simulates a **real-world customer support inbox system** where an AI agent must handle user requests such as refunds, complaints, and billing issues.

The environment follows the **OpenEnv standard API**:

* `reset()`
* `step(action)`
* `state()`

---

## 🎯 Use Case

Customer support automation is a real-world task used by:

* E-commerce platforms
* SaaS companies
* Helpdesk systems

This environment allows training and evaluating agents on realistic support workflows.

---

## ⚙️ Action Space

Each action follows this schema:

```json
{
  "action_type": "reply | refund | escalate",
  "message": "string",
  "refund_amount": "number (optional)"
}
```

---

## 📊 Observation Space

The environment returns:

* Current customer message
* Task details
* Conversation history
* Step count

---

## 🧪 Tasks

### 🟢 Easy

* Simple refund request
* Expected: `refund`

### 🟡 Medium

* Complaint handling
* Expected: `reply`

### 🔴 Hard

* Billing issue with edge case
* Expected: correct reasoning + action

---

## 🎁 Reward Design

Reward is continuous (0.0 → 1.0):

* Correct action → +0.6
* Valid message → +0.2
* Correct refund handling → +0.2
* Invalid action → penalty

---

## 🚀 Setup & Run

### 1. Build Docker

```bash
docker build -t support-env .
```

### 2. Run Server

```bash
docker run -p 8000:8000 support-env
```

### 3. API Docs

Open:

```
http://localhost:8000/docs
```

---

## ✅ Validation

```bash
openenv validate
```

---

## 🤖 Baseline Inference

```bash
python inference.py
```

Example output:

```
[START]
[STEP]
[END]
```

---

## 🐳 Deployment

This environment is deployed using Docker and can be hosted on Hugging Face Spaces.

---

## 📌 Notes

* Fully OpenEnv compliant
* Includes 3 graded tasks
* Deterministic scoring
* Real-world simulation

---

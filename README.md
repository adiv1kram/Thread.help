# 🌌 Thread.help — GenAI-Powered Java Thread Dump Analyzer

> A modern, web-based tool to make Java thread dump analysis **simple**, **insightful**, and **AI-assisted**.

---

## 🚀 Overview

**Thread.help** is a sleek, browser-based tool designed to demystify complex Java thread dumps. It leverages **Google's Gemini Generative AI** to parse, interpret, and analyze raw thread dump files, providing:

- 📌 High-level summaries
- 🧠 Root cause diagnosis
- ✅ Actionable recommendations

Whether you're troubleshooting deadlocks, high CPU usage, or contention issues — **Thread.help** brings expert-level insight straight into your browser.

---

## ✨ Features

- 🖥️ **Intuitive UI**  
  Clean, single-page React interface with a **cosmic-themed animated starfield** background.

- 📂 **File Upload Support**  
  Upload `.txt` thread dumps from tools like `jstack`, `jcmd`, or `kill -3`.

- 🔍 **Advanced Parsing**  
  Converts raw thread dump text into a structured JSON model via a robust Python backend.

- 🤖 **AI-Powered Analysis** *(powered by Gemini)*  
  - 📝 **Summary** – concise overview of thread states.
  - 🧩 **Diagnosis** – identifies deadlocks, stuck threads, and contention points.
  - 🛠️ **Recommendations** – step-by-step suggestions to resolve performance bottlenecks.
  - 🧾 **Markdown Output** – readable, formatted output via `react-markdown`.

---

## 🧰 Tech Stack

### 🔮 Frontend

- ⚛️ [React](https://reactjs.org/) (bootstrapped with [Vite](https://vitejs.dev/))
- 🎨 CSS + `<canvas>` for dynamic starfield background
- 📜 [`react-markdown`](https://github.com/remarkjs/react-markdown) for AI output rendering

### 🐍 Backend

- 🧪 [Flask](https://flask.palletsprojects.com/) (Python)
- 🌐 `Flask-Cors` to support cross-origin frontend calls
- 🤖 `google-generativeai` – official Gemini API client

---

## 📸 Screenshots
  <img width="1901" height="891" alt="Screenshot From 2025-08-21 00-04-09" src="https://github.com/user-attachments/assets/825aaaf2-ff54-4578-bd73-45e9740e3923" />
<img width="1901" height="891" alt="Screenshot From 2025-08-21 00-48-00" src="https://github.com/user-attachments/assets/dd590fa6-d217-498e-b842-72153f9f69cb" />
<img width="1901" height="891" alt="Screenshot From 2025-08-21 00-48-17" src="https://github.com/user-attachments/assets/33b084b0-ba38-48cf-a971-2a2dc7e636c6" />
<img width="1901" height="891" alt="Screenshot From 2025-08-21 00-48-34" src="https://github.com/user-attachments/assets/4edd4729-24b6-4a12-af95-2e520d7e9566" />





---

## 🧑‍💻 Getting Started

Follow these instructions to run the project locally.

---

### ✅ Prerequisites

Make sure you have the following installed:

- [Node.js](https://nodejs.org/) & `npm` – for the frontend
- [Python 3.x](https://www.python.org/downloads/) – for the backend
- A [Google Gemini API Key](https://aistudio.google.com/) – required for AI analysis

---

### 📦 Installation & Setup

#### 1. Clone the repository

```bash
git clone https://github.com/your-username/thread-dump-analyzer-react.git
cd thread-dump-analyzer-react

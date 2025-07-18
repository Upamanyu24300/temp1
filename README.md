# Carbon Emissions Tracker 🌍🚨

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-61DAFB.svg?logo=react&logoColor=black)](https://reactjs.org/)

A comprehensive full-stack web application that empowers companies to calculate, track, and analyze their carbon emissions based on materials used, quantity consumed, activity location, and emission factors. Gain valuable insights through Year-over-Year emissions analysis, Emission Intensity calculations, and emission hotspot identification.

## ✨ Features

- 📊 **Emission Calculations** - Calculate emissions based on date, material, quantity, and location
- 📈 **Historical Tracking** - Store and analyze historical emission records
- 📉 **YoY Analysis** - Track Year-over-Year emissions trends and patterns
- 🎯 **Emission Intensity** - Compute emission intensity using business production metrics
- 🔥 **Hotspot Identification** - Identify materials with the highest emission impact
- 🚀 **Modern Architecture** - FastAPI backend with React frontend
- 🐳 **Containerized** - Fully dockerized and deployment-ready

## 🌐 Live Demo

| Service | URL | Description |
|---------|-----|-------------|
| 🎨 **Frontend** | [Live App](https://frontend-production-a166.up.railway.app/) | React + NGINX Production |
| 🔧 **Backend API** | [Swagger UI](https://temp1-production-434b.up.railway.app/docs) | FastAPI Documentation & Testing |

## 🎥 Demo Video

> **To embed the video directly in README**: Edit this README.md file on GitHub's web interface, then drag and drop your `videos/recording.mp4` file directly into the editor. GitHub will automatically upload it and generate a URL like `https://github.com/user-attachments/assets/...` that will display the video inline.

**Current video location**: `/videos/recording.mp4`

**Steps to embed:**
1. Go to your GitHub repository
2. Click "Edit" on README.md 
3. Drag and drop `videos/recording.mp4` into the editor
4. Wait for upload completion
5. GitHub will generate the embedded video URL automatically
6. Save the file

Once embedded, the video will play directly in the README for all visitors!

## 🚀 Quick Start

### Prerequisites

- 🐳 **Docker & Docker Compose** (Recommended)
- 🔄 **Alternative**: Node.js + Python 3.10 + pipenv

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/carbon-emission-tracker.git
cd carbon-emission-tracker
```

### 2️⃣ Run with Docker Compose (Recommended)

```bash
docker-compose up --build
```

**Access the application:**
- 🎨 Frontend: http://localhost:3000
- 🔧 Backend API: http://localhost:8000/docs

**For subsequent runs:**
```bash
docker-compose up
```

### 3️⃣ Manual Setup (Alternative)

<details>
<summary>Click to expand manual setup instructions</summary>

#### Backend Setup
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

#### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

</details>

## 📂 Project Structure

```
carbon-emission-tracker/
├── 🔧 backend/
│   ├── main.py                 # FastAPI application entry point
│   ├── emissions_logic.py      # Core emission calculation logic
│   ├── models.py              # Pydantic data models
│   └── ...                    # Additional backend modules
├── 🎨 frontend/
│   └── ...                    # React + Tailwind components
├── 📊 processed/
│   ├── emission_factors.csv   # Emission factor data
│   ├── emission_records.csv   # Historical emission records
│   └── business_metrics.csv   # Business production metrics
├── 🐳 docker/
│   ├── docker-compose.yml     # Docker orchestration
│   ├── frontend.Dockerfile    # Frontend container config
│   └── backend.Dockerfile     # Backend container config
├── 🎥 videos/
│   └── recording.mp4          # Application demo video
└── 📖 README.md
```

## 🛠️ Tech Stack

### Frontend
- ⚛️ **React.js** - Modern JavaScript framework
- 🎨 **TailwindCSS** - Utility-first CSS framework
- 🌐 **NGINX** - Production web server

### Backend
- ⚡ **FastAPI** - High-performance Python web framework
- 🐼 **Pandas** - Data manipulation and analysis
- 📋 **Pydantic** - Data validation and settings management

### DevOps & Deployment
- 🐳 **Docker** - Containerization platform
- 🚀 **Railway** - Cloud deployment platform
- 📊 **CSV** - Data storage for emission factors and metrics

### Development Tools
- 🔧 **Uvicorn** - ASGI server for FastAPI
- 📦 **npm** - Package manager for frontend dependencies
- 🐍 **pip** - Python package installer

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <p>Made with ❤️ for a sustainable future</p>
  <p>🌱 Every emission tracked is a step towards carbon neutrality</p>
</div>

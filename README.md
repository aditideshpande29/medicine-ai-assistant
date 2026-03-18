# 🩺 MediBuddy

### *Your Daily Medicine Companion*

MediBuddy is an AI-powered medication management application that helps users take the **right medicine at the right time**. It combines **prescription understanding, smart reminders, and medicine verification through scanning** to prevent incorrect intake and improve medication safety.

---

## 🚀 Features

* 📷 **Medicine Scanning & Verification**
  Scan medicine strips and verify if they should be taken at that moment.

* 🧠 **Prescription Understanding**
  Extracts medicine details such as dosage and timing from uploaded prescriptions.

* ⏰ **Smart Reminders**
  Sends timely alerts based on personalized medicine schedules.

* 🛡 **Safety Checks**
  Prevents wrong medicine intake and double dosing.

* 👨‍👩‍👧 **Caregiver Support**
  Allows family members to monitor medication adherence.

* 💊 **Medicine Tracking**
  Tracks dosage and remaining tablets.

* 🛒 **Future: One-Tap Pharmacy Refill**
  Easy medicine ordering when stock is low.

---

## 🧩 How It Works

1. Upload prescription or manually add medicines
2. MediBuddy creates a structured medicine schedule
3. Smart reminders notify users
4. User scans medicine before intake
5. System verifies medicine and checks safety
6. Displays decision: **Take / Do Not Take**

---

## 🏗️ System Architecture

```
User / Caregiver
        ↓
Web / Mobile Interface
        ↓
FastAPI Backend
        ↓
AI Engine (OCR + Decision Logic)
        ↓
Database & Pharmacy Integration
```

---

## 🛠️ Tech Stack

| Layer    | Technology Used                    |
| -------- | ---------------------------------- |
| Frontend | React / Next.js (Vercel)           |
| Backend  | FastAPI (Python)                   |
| AI/ML    | EasyOCR, OpenCV, RapidFuzz         |
| Database | JSON (Extendable to MongoDB / SQL) |
| Tools    | Git, GitHub, Uvicorn               |

---

## 📦 Requirements

* Python 3.9+
* Node.js (if running frontend locally)
* Git

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/<your-username>/medibuddy.git
cd medibuddy
```

### 2. Create Virtual Environment

```
python -m venv venv
```

#### Activate Environment

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Run Backend Server

```
uvicorn app:app --reload
```

---

### 5. Open API Docs

```
http://127.0.0.1:8000/docs
```

---

## 🌐 Live Demo

👉 https://medico-sigma-seven.vercel.app/add-medicine

---

## 📂 Project Structure

```
medibuddy/
│── app.py
│── engine.py
│── parser.py
│── medicine_scan.py
│── decision_engine.py
│── requirements.txt
│── README.md
```

---

## 🔮 Future Scope

* Voice-based assistance
* Regional language support
* Wearable integration
* Doctor dashboards
* Pharmacy integration

---

## 🤝 Contributing

Contributions are welcome!
Fork the repository and submit a pull request.

---

## 📜 License

This project is for educational and demonstration purposes.

---

## 👨‍💻 Author

**Aditi Deshpande**
GitHub: https://github.com/aditideshpande29

---

## ⭐ Final Note

> MediBuddy doesn’t just remind users — it protects them.

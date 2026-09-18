# Hackathon ID: AZIS-DCAH4A

# 🌱 PlanetPulse - Carbon Footprint Tracker

PlanetPulse is a mobile-responsive web application built for the **Code2Career AI Hackathon** to help individuals monitor, understand, and reduce their personal carbon footprint across daily activities.

---

## 🚀 Key Features

* **Real-time Carbon Calculation:** Instant calculation of CO₂ emissions for travel (car, bus, flight), energy consumption, and dietary choices.
* **Dynamic Weekly Budget & Progress Bar:** Visual progress tracking against customizable weekly targets, with intuitive color alerts for target breaches.
* **Absurd Input Protection (DP2):** Defends against extreme outliers and bad data entries with custom alerts (blocks values > 50,000 units).
* **Eco-Impact Equivalents:** Translates carbon footprint numbers into relatable real-world metrics (e.g., mature trees required to offset emissions).
* **Quick-Add Presets:** One-click shortcut buttons for logging frequent activities effortlessly.
* **Instant Reset / Clear Data:** Allows users to easily clear logs and restart their weekly tracking cycle.
* **Category Filtering:** Filter activity history dynamically by travel, energy, or diet.
* **Fully Responsive Design:** Optimized UI for smooth experience on both mobile devices and desktops.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML5, CSS3, Jinja2 Templates
* **Architecture:** Modular MVC structure, lightweight in-memory storage

---

## 💻 Local Setup Instructions

Follow these steps to run the project locally on your machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/tanushkatariya312008-blip/PlanetPulse.git](https://github.com/tanushkatariya312008-blip/PlanetPulse.git)
   cd PlanetPulse

pip install flask
python app.py
[http://127.0.0.1:5000](http://127.0.0.1:5000)

PlanetPulse/
│
├── app.py              # Main Flask application logic, calculation & routes
├── templates/
│   └── index.html      # Mobile-responsive frontend dashboard
├── README.md           # Project documentation with Hackathon ID & guide
└── DECISIONS.md        # Architectural decision points rationale (DP1, DP2, DP3)
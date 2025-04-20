⚽ Soccer Matches Scheduler Web App
A lightweight Flask-based web application that scrapes and displays football (soccer) match data for a specific date. The app allows users to filter results by tournament, switch between dark and light modes, and download the match list in CSV format. Designed with full Arabic language support and responsive layout for all devices.

🎥 A Video Demo
Check out the project in action: https://youtu.be/27EgUF5sLBo?si=DjFUBA37oKbGeX42

🚀 Key Features
📅 Date-Based Match Display
Simply enter a date in MM/DD/YYYY format, and the app fetches and shows all football matches scheduled on that day from YallaKora.

🏆 League/Tournament Filtering
Once results are displayed, you can filter matches by competition name — whether it's CAF Champions League or English Premier League or Spanish La Liga— for a personalized viewing experience.

🌙 Light/Dark Mode Toggle
Switch between light and dark themes with a single click. The interface remembers your preference, ensuring a comfortable experience every time.

💾 Downloadable Match Data
One-click export! Download the currently displayed matches as a CSV file for further analysis or offline access.

📱 Responsive UI
The web interface is built to be fully responsive and mobile-friendly. Whether you're on a desktop or smartphone, the layout adjusts smoothly.

🌐 Arabic Localization
Designed with Arabic speakers in mind, the app includes full right-to-left (RTL) support and intuitive labels in Arabic, providing an accessible experience for native users.

🧭 How to Use
Open the web application in your preferred browser.

Enter a date using the MM/DD/YYYY format.

Click "Submit" to view all the football matches scheduled for that day.

Filter the results using the dropdown menu to see matches from a specific tournament.

Toggle dark/light mode with the switch at the top-left corner.

Click "Download" to save the displayed matches in CSV format on your device.

🛠 Project Structure
php
Copy
Edit
Soccer-Matches-Scheduler/
├── app.py               # Flask application entry point
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── templates/           # HTML templates for rendering pages
│   ├── base.html        # Main layout with navbar and theme toggle
│   ├── index.html       # Home page with date input form
│   └── display.html     # Results page showing match details
└── static/              # (Optional) Static files (CSS, JS, images)
💡 What Makes This Unique?
Live scraping from a trusted sports source — get real-time match info without relying on an API.

Zero backend storage — the app doesn’t save anything on the server, keeping things lightweight and secure.

Multi-purpose — perfect for football fans, sports analysts, or anyone who needs to track matches by date and league.

Built with simplicity in mind — no need for logins or accounts.

👨‍💻 Built With
Python

Flask

HTML/CSS

JavaScript

BeautifulSoup4

YallaKora (for match data source)


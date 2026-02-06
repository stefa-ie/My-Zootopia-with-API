# 🦁 My Zootopia with API

A Python CLI tool that fetches real animal data from an API and generates HTML pages. Enter any animal name and get a styled webpage with information about diet, location, and type. Features error handling and a clean, responsive card-based layout.

## ✨ Features

- Fetch real animal data from the API Ninjas Animals API
- Generate styled HTML pages with animal information cards
- Display diet, location, and type for each animal
- Handle multiple results when an animal name matches several species
- Error handling with user-friendly "not found" messages
- Clean, responsive card-based layout with modern styling
- Environment variable support for secure API key management

## 🚀 Getting Started

### Prerequisites

You'll need an API key from [API Ninjas](https://api-ninjas.com/). Sign up for a free account to get your key.

### Installation

1. Clone the repository:
```
git clone https://github.com/your-username/My-Zootopia-with-API.git
cd My-Zootopia-with-API
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your API key:
```
API_KEY=your_api_ninjas_key_here
```

### Usage

Run the application:
```
python animals_web_generator.py
```

Enter an animal name when prompted, and an HTML file will be generated in the project directory.

## 🗂️ Project Structure

- `animals_web_generator.py`: main application logic, HTML generation, and user interaction
- `data_fetcher.py`: API integration module for fetching animal data from API Ninjas
- `animals_template.html`: HTML template with styling for the generated pages
- `.env`: environment variables file for storing the API key (not tracked in git)
- `requirements.txt`: Python dependencies

## 🎮 How to Use

1. Run `python animals_web_generator.py` or `python3 animals_web_generator.py` on mac
2. Enter an animal name (e.g., "lion", "dolphin", "eagle")
3. The app fetches data from the API and generates `{animal_name}.html`
4. Open the generated HTML file in your browser to view the animal information
5. If the animal isn't found, you'll get a friendly error page suggesting to check the spelling

## 🛠️ Customization

- Modify the card layout and displayed fields in `animal_card()` function in `animals_web_generator.py`
- Adjust colors, fonts, and styling in `animals_template.html`
- Add additional animal characteristics by accessing more fields from the API response

## 🧰 Tech Stack

- Python 3
- requests (HTTP library for API calls)
- python-dotenv (environment variable management)
- HTML/CSS (generated output)
- API Ninjas Animals API

## 📝 API Reference

This project uses the [API Ninjas Animals API](https://api-ninjas.com/api/animals). The API returns animal data including:
- Name
- Taxonomy
- Locations
- Characteristics (diet, type, lifespan, etc.)

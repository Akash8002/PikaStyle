# 🚀 PikaStyle

PikaStyle is a **Python-based web scraping tool** designed to collect fashion-related data from online platforms. It scrapes valuable information such as product names, prices, sizes, and images, and stores it in an easy-to-access format like CSV for analysis or use in projects.

## ✨ Features

- **Scrapes fashion products**' details from e-commerce websites.
- Collects **product names**, **prices**, **sizes**, and **images**.
- Save scraped data in **CSV format**.
- Easily **customizable** and extendable for other scraping needs.

## 🛠️ Requirements

Before running PikaStyle, make sure to have the following Python packages installed:

- `requests`
- `beautifulsoup4`
- `pandas`
- `lxml`

### Install dependencies:

```bash
pip install -r requirements.txt
```

## 📥 Installation

### 1. Clone the repository:

```bash
git clone https://github.com/Akash8002/PikaStyle.git
cd PikaStyle
```

### 2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

Now you're all set to start using PikaStyle!

## 🚀 Usage

Once installed, simply run the script to start scraping fashion data from your favorite e-commerce websites.

```bash
python gradio_app.py
```

### Example Code

You can also customize the script to target specific websites and data points.

```python
# Example usage of PikaStyle
scraper = PikaStyleScraper(target_url="https://example.com")
scraper.scrape()
```

This will scrape the fashion data and save it in a CSV file by default.

## 🤝 Contributing

We welcome contributions! If you'd like to help improve PikaStyle, feel free to:

- Open an issue 🐛
- Submit a pull request 💥

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

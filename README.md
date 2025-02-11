# Crypto Market Data Tracker

This project fetches real-time cryptocurrency market data from the **CoinGecko API**, processes it, and stores it in an Excel file. It also tracks the **top 10 gainers and losers** based on **24-hour price changes**.

## 📌 Features

- Fetches **live cryptocurrency market data**
- Extracts relevant information: **name, price, price change, market cap change, ATH, ROI**
- Sorts **top 10 gainers and losers**
- Saves data into **Crypto.xlsx** with multiple sheets:
  - **Whole Data**: Complete fetched dataset
  - **High Top Ten**: Top 10 cryptocurrencies by highest percentage increase
  - **Low Top Ten**: Top 10 cryptocurrencies by highest percentage decrease
- Supports **continuous data fetching** at user-defined intervals

---

## 🚀 Installation & Setup

### **1️⃣ Install Dependencies**

Make sure you have Python installed. Then, install the required libraries:

```bash
pip install pandas requests openpyxl
```

### **2️⃣ Run the Script**

Start the program by running:

```bash
python main.py
```

You will be prompted to enter a time interval (in seconds) for continuous data fetching.

---

## 📂 Project Structure

```
├── apicryto.py   # Handles API requests, data processing, and Excel saving
├── main.py       # Runs the script in a loop with user-defined intervals
```

---

## ⚙️ How It Works

1. **`apicryto.py`**:

   - Fetches crypto data from CoinGecko API
   - Processes and extracts relevant fields
   - Saves data into an Excel file without overwriting existing data

2. **`main.py`**:

   - Takes user input for time interval
   - Runs an infinite loop to fetch and store data periodically

---

## 📝 Notes

- Ensure you have an **active internet connection** while running the script.
- If **Crypto.xlsx** already exists, new data is **appended** to avoid overwriting.
- You can modify `per_page` in **`apicryto.py`** to fetch more or fewer cryptocurrencies.

---

## 💡 Future Improvements

- Add a **GUI** for better user interaction
- Store data in **a database** instead of an Excel file
- Implement **API error handling and logging**

---

## 🤝 Contributing

Feel free to fork this repository and improve it! If you encounter any issues, create an issue or submit a pull request.

---

## 📜 License

This project is open-source and available under the **MIT License**.


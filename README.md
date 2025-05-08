````markdown
# HDFS Log Analyzer Dashboard

An interactive Streamlit-based log analyzer for parsing, filtering, and visualizing critical and abnormal events in HDFS logs. This tool is designed to help identify issues by summarizing log data over a customizable time period.

---

##  Features

-  **Time-Based Filtering** — Select a custom time range to analyze logs.
-  **Log Level Statistics** — View counts and frequency of `INFO`, `WARN`, and `ERROR` logs.
-  **Top Messages** — See the most frequent warning and error messages.
-  **Unique Messages** — Identify messages that occur only once (potential anomalies).
-  **Trend Visualization** — Plot number of log entries per day.
-  **Streamlit Dashboard** — Interactive web interface for exploration.

---

##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/hdfs-log-analyzer.git
cd hdfs-log-analyzer
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit pandas
```

### 3. Add Log File

Download the sample HDFS log file from [LogHub - HDFS\_2k.log](https://github.com/logpai/loghub/blob/master/HDFS/HDFS_2k.log) and place it in a folder named `logs/`:

```
log_analyzer/
├── app.py
└── logs/
    └── HDFS_2k.log
```

### 4. Run the App

```bash
streamlit run app.py
```

Open your browser at [http://localhost:8501](http://localhost:8501) to interact with the dashboard.

---

##  Folder Structure

```
log_analyzer/
├── app.py             # Main Streamlit app
├── logs/
│   └── HDFS_2k.log    # Sample log file
└── README.md
```

---

##  Future Improvements

* Real-time log file monitoring
* Integration with multiple log sources
* Anomaly detection using ML models
* Export to CSV or database

---

##  License

This project is open-source and available under the [MIT License](LICENSE).

---

##  Acknowledgments

* [LogHub Dataset](https://github.com/logpai/loghub) by LogPAI
* [Streamlit](https://streamlit.io/) for the interactive UI

```

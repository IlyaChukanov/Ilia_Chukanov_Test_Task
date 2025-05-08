import streamlit as st
import pandas as pd
import re
from datetime import datetime

# Функция для парсинга строки лога
def parse_log_line(line):
    pattern = r'(\d{6}) (\d{6}) (\d+) (\w+) (.+)'
    match = re.match(pattern, line)
    if match:
        date_str, time_str, pid, level, message = match.groups()
        timestamp = datetime.strptime(date_str + time_str, '%y%m%d%H%M%S')
        return {
            'timestamp': timestamp,
            'pid': int(pid),
            'level': level,
            'message': message
        }
    return None

# Загрузка и парсинг логов
def load_logs(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    parsed_logs = [parse_log_line(line) for line in lines]
    parsed_logs = [log for log in parsed_logs if log]
    return pd.DataFrame(parsed_logs)

# Основная функция Streamlit
def main():
    st.title("Log analyzer HDFS")

    # Загрузка логов
    df = load_logs('logs/HDFS_2k.log')

    # Выбор временного диапазона
    st.sidebar.write("Selecting a time range")

    start_date = st.sidebar.date_input("Start Date", value=df['timestamp'].min().date())
    start_time = st.sidebar.time_input("Start Time", value=df['timestamp'].min().time())

    end_date = st.sidebar.date_input("End Date", value=df['timestamp'].max().date())
    end_time = st.sidebar.time_input("End Time", value=df['timestamp'].max().time())

    start_dt = datetime.combine(start_date, start_time)
    end_dt = datetime.combine(end_date, end_time)

    # Фильтрация по времени
    mask = (df['timestamp'] >= start_dt) & (df['timestamp'] <= end_dt)
    df_filtered = df.loc[mask]

    st.subheader("Event statistics")
    st.write(df_filtered['level'].value_counts())

    st.subheader("Top 5 WARN Level Messages")
    st.write(df_filtered[df_filtered['level'] == 'WARN']['message'].value_counts().head(5))

    st.subheader("Top Error Level Messages")
    st.write(df_filtered[df_filtered['level'] == 'ERROR']['message'].value_counts().head(5))

    st.subheader("Unique Messages")
    unique_messages = df_filtered['message'].value_counts()[df_filtered['message'].value_counts() == 1]
    st.write(unique_messages)

    st.subheader("Message count chart by date")
    df_filtered['date'] = df_filtered['timestamp'].dt.date
    st.line_chart(df_filtered.groupby('date').size())

if __name__ == "__main__":
    main()

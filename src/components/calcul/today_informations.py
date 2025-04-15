from datetime import datetime, timedelta



today = datetime.today().date()  #ex: 2025-04-08
hour = datetime.today().hour  #ex: 10
today_test = datetime.strptime("2024-03-03 10:20", "%Y-%m-%d %H:%M").date()
hour_test = datetime.strptime("2024-03-03 10:20", "%Y-%m-%d %H:%M").hour
month = datetime.today().month
year = datetime.today().year
month_test = datetime.strptime("2024-03-01", "%Y-%m-%d").date().month
year_test = datetime.strptime("2024-03-01", "%Y-%m-%d").date().year
# ✅ Lundi de la semaine
start_of_week_test = today_test - timedelta(days=today_test.weekday())  # weekday() : 0=lundi
start_of_week = today - timedelta(days=today.weekday())  
import json
from datetime import datetime

LOG_FILE = "dose_log.json"

def get_current_time_slot():
    hour = datetime.now().hour

    if 5 <= hour < 12:
        return "morning"
    elif 12 <= hour < 17:
        return "afternoon"
    else:
        return "night"


def load_logs():
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


def save_logs(logs):
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)


def check_and_log_dose(medicine, allowed_timings):
    logs = load_logs()
    today = datetime.now().strftime("%Y-%m-%d")

    # ✅ Allow anytime if once daily
    if "once daily" in allowed_timings:
        pass
    else:
        current_time = get_current_time_slot()
        if allowed_timings and current_time not in allowed_timings:
            return False, f"⏰ Not the right time. Take during {allowed_timings}"

    # Prevent double dose
    if medicine in logs and today in logs[medicine]:
        return False, "⚠️ Dose already taken today"

    # Log dose
    logs.setdefault(medicine, {})
    logs[medicine][today] = datetime.now().strftime("%H:%M")
    save_logs(logs)

    return True, "✅ Safe to take now"

    # Check time validity
    if allowed_timings and current_time not in allowed_timings:
        return False, f"⏰ Not the right time. Take during {allowed_timings}"

    # Check if already taken
    if medicine in logs and today in logs[medicine]:
        return False, "⚠️ Dose already taken today"

    # Log dose
    logs.setdefault(medicine, {})
    logs[medicine][today] = datetime.now().strftime("%H:%M")
    save_logs(logs)

    return True, "✅ Safe to take now"

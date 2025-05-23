# Onschola Schedule for Offline Students
offline_schedule = {
    "School Hours": "9:00 AM - 4:00 PM",
    "Class Duration": "50 minutes",
    "Break Duration": "5 minutes",
    "Lunch Break": "12:30 PM - 1:15 PM (45 minutes)",
    "Total Classes": 6,
    "Detailed Schedule": [
        {"Period 1": {"Time": "9:00 AM - 9:50 AM", "Subject": "Core Subject (e.g., Math)"}},
        {"Period 2": {"Time": "9:55 AM - 10:45 AM", "Subject": "Core Subject (e.g., English)"}},
        {"Period 3": {"Time": "10:50 AM - 11:40 AM", "Subject": "Core Subject (e.g., Science)"}},
        {"Advisory/Pacing/Study": {"Time": "11:45 AM - 12:30 PM", "Activity": "Supervised study hall"}},
        {"Lunch Break": "12:30 PM - 1:15 PM"},
        {"Period 4": {"Time": "1:15 PM - 2:05 PM", "Subject": "Online Course/Elective"}},
        {"Period 5": {"Time": "2:10 PM - 3:00 PM", "Subject": "Core Subject (e.g., Social Studies)"}},
        {"Period 6": {"Time": "3:05 PM - 3:55 PM", "Subject": "Online Course/Elective"}},
        {"Advisory/Pacing/Study": {"Time": "4:00 PM - 4:15 PM", "Activity": "Supervised study hall or extracurricular activities"}}
    ]
}

# Monitoring Progress and Homework Policy
offline_policy = {
    "Progress Monitoring": "Teachers and advisors will regularly check student progress in online classes.",
    "Homework Policy": "Students who are behind will be informed during Advisory/Pacing/Study Hall to complete the work as homework.",
    "Tracking": "Use platforms like Google Docs or Sheets to track and communicate homework assignments."
}

# Onschola Schedule for Online Students
online_schedule = {
    "School Hours": "1:30 PM - 4:00 PM",
    "Class Duration": "45 minutes",
    "Break Duration": "5 minutes",
    "Total Classes": 3,
    "Detailed Schedule": [
        {"Period 1": {"Time": "1:30 PM - 2:15 PM", "Subject": "Core Subject (e.g., Math or English)"}},
        {"Period 2": {"Time": "2:20 PM - 3:05 PM", "Subject": "Online Course/Elective"}},
        {"Period 3": {"Time": "3:10 PM - 3:55 PM", "Subject": "Core Subject (e.g., Science or Social Studies)"}}
    ]
}

# Monitoring Progress and Homework Policy for Online Students
online_policy = {
    "Progress Monitoring": "Teachers and advisors will check student progress regularly using platforms like Google Docs or Sheets.",
    "Homework Policy": "Students who are behind will be instructed to complete the work as homework.",
    "Tracking": "Assignments and progress will be tracked through online platforms."
}

# Printing schedules (for demonstration)
def print_schedule(schedule, policy):
    print("Schedule:")
    for key, value in schedule.items():
        if isinstance(value, list):
            for item in value:
                for period, details in item.items():
                    print(f"{period}: {details}")
        else:
            print(f"{key}: {value}")
    print("\nMonitoring and Homework Policy:")
    for key, value in policy.items():
        print(f"{key}: {value}")
    print("\n")

print("Offline Students Schedule:\n")
print_schedule(offline_schedule, offline_policy)

print("Online Students Schedule:\n")
print_schedule(online_schedule, online_policy)

!pip install pandas
import pandas as pd

# Data for the offline schedule
offline_schedule_data = {
    "Period": [
        "Period 1", 
        "Period 2", 
        "Period 3", 
        "Advisory/Pacing/Study", 
        "Lunch Break", 
        "Period 4", 
        "Period 5", 
        "Period 6", 
        "Advisory/Pacing/Study"
    ],
    "Time": [
        "9:00 AM - 9:50 AM", 
        "9:55 AM - 10:45 AM", 
        "10:50 AM - 11:40 AM", 
        "11:45 AM - 12:30 PM", 
        "12:30 PM - 1:15 PM", 
        "1:15 PM - 2:05 PM", 
        "2:10 PM - 3:00 PM", 
        "3:05 PM - 3:55 PM", 
        "4:00 PM - 4:15 PM"
    ],
    "Subject/Activity": [
        "Core Subject (e.g., Math)", 
        "Core Subject (e.g., English)", 
        "Core Subject (e.g., Science)", 
        "Supervised study hall", 
        "Lunch Break", 
        "Online Course/Elective", 
        "Core Subject (e.g., Social Studies)", 
        "Online Course/Elective", 
        "Supervised study hall or extracurricular activities"
    ]
}

# Data for the online schedule
online_schedule_data = {
    "Period": [
        "Period 1", 
        "Period 2", 
        "Period 3"
    ],
    "Time": [
        "1:30 PM - 2:15 PM", 
        "2:20 PM - 3:05 PM", 
        "3:10 PM - 3:55 PM"
    ],
    "Subject/Activity": [
        "Core Subject (e.g., Math or English)", 
        "Online Course/Elective", 
        "Core Subject (e.g., Science or Social Studies)"
    ]
}

# Create DataFrames for both schedules
offline_schedule_df = pd.DataFrame(offline_schedule_data)
online_schedule_df = pd.DataFrame(online_schedule_data)

# Write to an Excel file
with pd.ExcelWriter('Onschola_Schedules.xlsx') as writer:
    offline_schedule_df.to_excel(writer, sheet_name='Offline Schedule', index=False)
    online_schedule_df.to_excel(writer, sheet_name='Online Schedule', index=False)

print("Schedules have been successfully written to Onschola_Schedules.xlsx")

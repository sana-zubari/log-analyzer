# Log Analyzer Project

error_count = 0
warning_count = 0

with open("sample_log.txt", "r") as file:
    for line in file:
        if "ERROR" in line:
            error_count += 1
        elif "WARNING" in line:
            warning_count += 1

print("Total Errors:", error_count)
print("Total Warnings:", warning_count)

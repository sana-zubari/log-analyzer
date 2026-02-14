# Log Analyzer Project

error_count = 0
warning_count = 0
info_count = 0

try:
    with open("sample_log.txt", "r") as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1
            elif "INFO" in line:
                info_count += 1

    
    print("\nLog Analysis Report")
    print("-------------------")
    print("Total Errors:", error_count)
    print("Total Warnings:", warning_count)
    print("Total Info Messages:", info_count)

except FileNotFoundError:
    print("Log file not found. Please check the file name.")


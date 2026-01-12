import sys

# Command-line input
if len(sys.argv) == 7:
    script_name = sys.argv[0]
    project_id = sys.argv[1]
    project_name = sys.argv[2]
    month = sys.argv[3]
    phase1 = int(sys.argv[4])
    phase2 = int(sys.argv[5])
    phase3 = int(sys.argv[6])
else:
    # Default values if arguments are not passed
    script_name = sys.argv[0]
    project_id = "PRJ101"
    project_name = "AI Tracker"
    month = "January"
    phase1 = 12
    phase2 = 10
    phase3 = 14

# Progress calculation
total_tasks = phase1 + phase2 + phase3
average_tasks = total_tasks / 3

# Display report
print("Script:", script_name)
print("Project ID:", project_id)
print("Project Name:", project_name)
print("Month:", month)
print("Tasks Completed in Phases:", phase1, phase2, phase3)
print("Total Tasks:", total_tasks)
print("Average Tasks per Phase:", average_tasks)

# Progress level decision
if average_tasks >= 15:
    level = "Excellent Progress"
elif average_tasks >= 10:
    level = "Good Progress"
elif average_tasks >= 7:
    level = "Average Progress"
else:
    level = "Needs Improvement"

print("Project Progress Level:", level)

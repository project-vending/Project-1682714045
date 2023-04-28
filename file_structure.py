
import os

# Define directory structure
root_dir = "Data_Pipeline_Monitoring"
data_dir = os.path.join(root_dir, "data")
pipeline_dir = os.path.join(root_dir, "pipeline")
monitor_dir = os.path.join(root_dir, "monitor")
logs_dir = os.path.join(root_dir, "logs")

# Create directories
os.makedirs(data_dir, exist_ok=True)
os.makedirs(pipeline_dir, exist_ok=True)
os.makedirs(monitor_dir, exist_ok=True)
os.makedirs(logs_dir, exist_ok=True)

# Create empty files in each folder
with open(os.path.join(data_dir, "data_file.csv"), "w") as f:
    pass

with open(os.path.join(pipeline_dir, "pipeline_file.py"), "w") as f:
    pass

with open(os.path.join(monitor_dir, "monitor_file.py"), "w") as f:
    pass

with open(os.path.join(logs_dir, "pipeline_log.txt"), "w") as f:
    pass

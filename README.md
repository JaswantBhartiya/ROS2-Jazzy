# ROS2-Jazzy Workspace

A professional ROS 2 Jazzy development workspace containing core robotics projects and experimental scripts.

## 📁 Repository Structure

This repository follows the standard ROS 2 multi-package workspace layout:

```text
.
├── src/
│   ├── main-projects/
│   │   └── my_robot_controller/    # Core ROS 2 Package (Control Logic)
│   └── small-projects/
│       ├── my_test_pkg/            # Experimental ROS 2 Package
│       └── raw_scripts/            # Standalone Python scripts (Non-ROS nodes)
├── .gitignore                      # Prevents build/install bloat
└── README.md

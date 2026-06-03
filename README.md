# ROS 2 Jazzy Workspace

A professional ROS 2 Jazzy development workspace containing core robotics simulation projects, custom controllers, and experimental scripts.

---

## 📁 Repository Structure

This repository follows a clean, modular ROS 2 multi-package workspace layout:

```text
.
├── src/
│   ├── main-projects/
│   │   └── my_robot_controller/    # Core ROS 2 Package (Control & Navigation Logic)
│   └── small-projects/
│       ├── my_test_pkg/            # Experimental ROS 2 Package for prototyping
│       └── raw_scripts/            # Standalone Python scripts (Testing & Mathematical models)
├── .gitignore                      # Prevents build, install, and log directory bloat
└── README.md

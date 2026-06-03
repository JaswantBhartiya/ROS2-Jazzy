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
```
<br><br>

## 📚 Documentation & Notes

Comprehensive project logs, hardware/simulation configurations, and ROS 2 learning resources are actively tracked here:

👉 Read my ROS 2 Jazzy Simulation Notes on Notion:

https://industrious-sock-502.notion.site/ROS2-9896260113ca46f884262e382f1c6e0f?source=copy_link

<br><br>
## 🛠️ Getting Started
### Prerequisites

* OS: Ubuntu 24.04 LTS (Noble Numbat)

* ROS 2 Distribution: Jazzy Jalisco

* Build Tool: colcon

### Build and Installation

Clone this repository directly into your ROS 2 workspace structure, navigate to the root directory, and build using colcon:

``` bash
# Navigate to workspace root
cd ~/ros2_ws

# Install dependencies
rosdep install --from-paths src --ignore-src -r -y

# Build the workspace
colcon build --symlink-install

# Source the overlay
source install/setup.bash
```

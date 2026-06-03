📚 Documentation & Notes

Comprehensive project logs, hardware/simulation configurations, and ROS 2 learning resources are actively tracked here:

👉 Read my ROS 2 Jazzy Simulation Notes on Notion
🛠️ Getting Started
Prerequisites

    OS: Ubuntu 24.04 LTS (Noble Numbat)

    ROS 2 Distribution: Jazzy Jalisco

    Build Tool: colcon

Build and Installation

Clone this repository directly into your ROS 2 workspace structure, navigate to the root directory, and build using colcon:
Bash

# Navigate to workspace root
cd ~/ros2_ws

# Install dependencies
rosdep install --from-paths src --ignore-src -r -y

# Build the workspace
colcon build --symlink-install

# Source the overlay
source install/setup.bash

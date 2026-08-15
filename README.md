# Turtlesim Keyboard Control

A ROS 2 custom node to control the turtlesim robot using keyboard keys.

## Controls

- A - Move the turtle forward
- R - Rotate the turtle continuously
- Q - Quit the program

## Requirements

- ROS 2
- Python 3
- turtlesim

## How to Run

Build the package:

```bash
cd ~/ros2_ws
colcon build --packages-select turtlesim_keyboard_control

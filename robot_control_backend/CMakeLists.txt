cmake_minimum_required(VERSION 3.20)
project(robot_control_backend)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/ArriveNotification.msg"
  "msg/AxisFault.msg"
  "msg/AxisStatus.msg"
  "msg/CmdAck.msg"
  "msg/Feedback.msg"
  "msg/GyroFeedback.msg"
  "msg/Heartbeat.msg"
  "msg/HomeStatus.msg"
  "msg/IntCmd.msg"
  "msg/Kinematics.msg"
  "msg/LimitEvent.msg"
  "msg/RotationCmd.msg"
  "msg/SensorCmd.msg"
  "msg/StopNotification.msg"
  "msg/SwingCmd.msg"
  "msg/TelescopicCmd.msg"
  "msg/TuoLuoYi.msg"
  "msg/VacuumLoss.msg"
  DEPENDENCIES std_msgs
)

ament_export_dependencies(rosidl_default_runtime)
install(PROGRAMS
  scripts/arm_substitute.py
  DESTINATION lib/${PROJECT_NAME}
)
ament_package()

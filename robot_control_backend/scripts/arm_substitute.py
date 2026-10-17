#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from robot_control_backend.msg import IntCmd

class ArmSubstitute(Node):
    def __init__(self):
        super().__init__('arm_substitute')
        
        # 1. 创建发布者：发布到 /robot_status，类型为 String
        self.status_pub = self.create_publisher(String, '/robot_status', 10)
        
        # 2. 创建订阅者：订阅 /web_cmd，类型为 String
        self.web_sub = self.create_subscription(String, '/web_cmd', self.web_cmd_callback, 10)
        
        # 3. 创建订阅者：订阅 /control/softstop，类型为我们刚编译的 IntCmd
        self.softstop_sub = self.create_subscription(IntCmd, '/control/softstop', self.softstop_callback, 10)
        
        self.get_logger().info("🤖 ROS2 机械臂替身已启动，正在等待消息...")

    def web_cmd_callback(self, msg):
        # 收到网页文字时触发
        self.get_logger().info(f'收到网页文字: "{msg.data}"')
        
        # 回复测试状态
        reply = String()
        reply.data = f'[测试数据] ROS2 substitute online, got: {msg.data}'
        self.status_pub.publish(reply)

    def softstop_callback(self, msg):
        # 收到急停指令时触发
        self.get_logger().warn(f'收到急停测试指令! module_id={msg.module_id}, device_id={msg.device_id}, position={list(msg.position)}')
        
        # 回复测试状态
        reply = String()
        reply.data = '[测试数据] softstop test received'
        self.status_pub.publish(reply)

def main(args=None):
    rclpy.init(args=args)
    node = ArmSubstitute()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

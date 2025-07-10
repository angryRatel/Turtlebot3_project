
#!/usr/bin/env python3
#
# Copyright 2018 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Leon Jung, Gilbert, Ashe Kim, Hyungyu Kim, ChanHyeong Lee

from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from std_msgs.msg import Float64


class ControlLane(Node):

    def __init__(self):
        super().__init__('control_lane')

        self.sub_lane = self.create_subscription(
            Float64,
            '/control/lane',
            self.callback_follow_lane,
            1
        )
        self.sub_max_vel = self.create_subscription(
            Float64,
            '/control/max_vel',
            self.callback_get_max_vel,
            1
        )
        self.sub_avoid_cmd = self.create_subscription(
            Twist,
            '/avoid_control',
            self.callback_avoid_cmd,
            1
        )
        self.sub_avoid_active = self.create_subscription(
            Bool,
            '/avoid_active',
            self.callback_avoid_active,
            1
        )

        self.sub_mission_state = self.create_subscription(
            Bool,
            '/avoid_active',
            self.callback_mission_state,
            1
        )

        self.pub_cmd_vel = self.create_publisher(
            Twist,
            '/control/cmd_vel',
            1
        )


        # PD control related variables
        self.last_error = 0
        self.filtered_error = 0.0
        self.MAX_VEL = 0.07

    def callback_follow_lane(self, desired_center):

        center = desired_center.data
        error = center - 320

        # PD 제어
        Kp = 0.0027 
        Kd = 0.0063  
        angular_z = Kp * error + Kd * (error - self.last_error)
        self.last_error = error

        # 속도 계산
        speed_factor = max(1 - abs(error) / 320, 0)
        twist = Twist()
        twist.linear.x = min(self.MAX_VEL * (speed_factor ** 1.8), self.MAX_VEL)

        # 회전 속도 제한
        twist.angular.z = -max(angular_z, -1.0) if angular_z < 0 else -min(angular_z, 1.0)

        # 조향 강도에 따른 속도 감속
        angular_factor = 1.0 - min(abs(twist.angular.z) / 1.0, 1.0)
        twist.linear.x *= angular_factor

        self.pub_cmd_vel.publish(twist)


    def callback_avoid_cmd(self, twist_msg):
        self.avoid_twist = twist_msg

        if self.avoid_active:
            self.pub_cmd_vel.publish(self.avoid_twist)

    def callback_avoid_active(self, bool_msg):
        self.avoid_active = bool_msg.data
        if self.avoid_active:
            self.get_logger().info('Avoidance mode activated.')
        else:
            self.get_logger().info('Avoidance mode deactivated. Returning to lane following.')

    def shut_down(self):
        self.get_logger().info('Shutting down. cmd_vel will be 0')
        twist = Twist()
        self.pub_cmd_vel.publish(twist)

    def callback_mission_state(self,bool_msg):
        pass
        


def main(args=None):
    rclpy.init(args=args)
    node = ControlLane()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.shut_down()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

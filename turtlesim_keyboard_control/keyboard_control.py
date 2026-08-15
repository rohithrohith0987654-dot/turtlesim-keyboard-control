import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
import termios
import tty


class KeyboardControl(Node):

    def __init__(self):
        super().__init__('keyboard_control')

        self.publisher = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        self.get_logger().info('Press A to move forward')
        self.get_logger().info('Press R to rotate continuously')
        self.get_logger().info('Press Q to quit')

        self.run_keyboard_control()

    def get_key(self):
        settings = termios.tcgetattr(sys.stdin)

        try:
            tty.setraw(sys.stdin.fileno())
            key = sys.stdin.read(1)
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

        return key

    def run_keyboard_control(self):

        while rclpy.ok():

            key = self.get_key()

            msg = Twist()

            if key.lower() == 'a':
                msg.linear.x = 2.0
                msg.angular.z = 0.0

            elif key.lower() == 'r':
                msg.linear.x = 0.0
                msg.angular.z = 2.0

            elif key.lower() == 'q':
                break

            self.publisher.publish(msg)


def main(args=None):

    rclpy.init(args=args)

    node = KeyboardControl()

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()

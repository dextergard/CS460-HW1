import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.time = 0

    def create_twist(self, linear_x, angular_z):
        msg = Twist()
        msg.linear.x = linear_x
        msg.angular.z = angular_z
        return msg

    def get_twist_msg(self): # use python array to program commands. makes it easier to manage
        commands = [[0.0, 1.65/2.0]] * 2 + [[1.0, 0.0]] * 7 + [[0.0, 1.65]] * 2  + [[1.0, 0.0]] * 7 + [[0.0, 1.65]] * 2 + [[1.0, 0.0]] * 7 + [[0.0, 1.65*1.2]] * 2  + [[1.0, 0.0]] * 7 + [[0.0,0.0]] * 500
        if (self.time < 100):
            msg = self.create_twist(commands[(self.time)][0], commands[(self.time)][1])
        elif self.time >= 100:
            msg = self.create_twist(0.0, 0.0)

        return msg
    
    def timer_callback(self):
        msg = self.get_twist_msg()       
        self.publisher.publish(msg)
        self.time += 1
        print("time: {}".format(self.time))

def main(args=None):
    rclpy.init(args=args)

    turtle_controller = TurtleController()

    rclpy.spin(turtle_controller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    turtle_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
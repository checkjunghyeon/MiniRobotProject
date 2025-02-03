from mobile_robot  import *
from manipulator_robot import *

ur10 = Cobot("001", "cobot001", "Universal Robots", joint_count=6)
print(ur10.get_info())  

ur10.move_joint(3, 30.0)
print(ur10.get_info())  
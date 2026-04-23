import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ruby/Nazmus Shakib/Spring 26/ros2_basic/install/py_nodes'

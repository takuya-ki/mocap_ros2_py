import json
from mocap_robotapi import *

import rospy
from sensor_msgs.msg import JointState

def ros1_joint_state_publisher():
  # 初始化ROS节点
  rospy.init_node("real_time_joint_state_publisher", anonymous=True)
  publisher = rospy.Publisher("/joint_states", JointState, queue_size=10)
  rate = rospy.Rate(10)  # 设置发布频率为10Hz

  json_file_path = './retarget.json'
  # 定义关节名称列表
  # 读取JSON文件
  with open(json_file_path, 'r') as file:
      data = json.load(file)
  joint_names = [item['retargetJoint'] for item in data['retargetJoints']]
  
  robot = MCPRobot(open(json_file_path).read())
  app = MCPApplication()
  settings = MCPSettings()
  settings.set_udp(7012)
  settings.set_bvh_rotation(0)
  app.set_settings(settings)
  app.open()
  try:
    while not rospy.is_shutdown():
        evts = app.poll_next_event()
        for evt in evts:
            if evt.event_type == MCPEventType.AvatarUpdated:
                avatar = MCPAvatar(evt.event_data.avatar_handle)
                robot.update_robot(avatar)
                robot.run_robot_step()
                #print (robot.get_robot_ros_frame_json())
                
                # 获取实时数据
                real_time_data = json.loads(robot.get_robot_ros_frame_json()[0])

                # 创建并填充JointState消息
                joint_state_msg = JointState()
                joint_state_msg.header.stamp = rospy.Time.now()
                joint_state_msg.name = joint_names

                # 初始化关节位置列表
                joint_positions = [0.0] * len(joint_names)

                # 根据关节名称填充关节位置
                for i, name in enumerate(joint_names):                    
                    if name in real_time_data['joint_positions']:
                        joint_positions[i] = real_time_data['joint_positions'][name]

                joint_state_msg.position = joint_positions
                # 发布消息
                publisher.publish(joint_state_msg)
                # 打印日志信息（可选）
                rospy.loginfo(f"Published joint positions: {joint_positions}")
            
            elif evt.event_type == MCPEventType.RigidBodyUpdated:
                print('rigid body updated')
            else:
                print('unknow event')
        # 睡眠以保持发布频率
        rate.sleep()
  except rospy.ROSInterruptException:
      pass      
  app.close()
  
if __name__ == '__main__':
  ros1_joint_state_publisher()
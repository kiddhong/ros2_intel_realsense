# Copyright (c) 2018 Intel Corporation
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

import os

from launch import LaunchDescription
import launch_ros.actions
import launch.actions


def generate_launch_description():
    tote_namespace = launch.substitutions.LaunchConfiguration('tote_namespace')
    param_dir = launch.substitutions.LaunchConfiguration('param_dir')

    enable_imu = launch.substitutions.LaunchConfiguration('enable_imu',
                                                                  default='true')
    gyro_fps = launch.substitutions.LaunchConfiguration('gyro_fps', default='400')
    accel_fps = launch.substitutions.LaunchConfiguration('accel_fps', default='250')

    return LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            'tote_namespace',
            default_value=os.environ['TOTE_NAMESPACE'],
            description='Specifying namespace to node'),

        # Realsense
        launch_ros.actions.Node(
            node_namespace=tote_namespace,
            package='realsense_ros2_camera',
            node_executable='realsense_ros2_camera',
            parameters=[{'enable_imu': enable_imu},
                        {'gyro_fps': gyro_fps},
                        {'accel_fps': accel_fps}],
            output='screen'),
    ])

from setuptools import setup

package_name = 'robosoccer_world_model'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=['world_model_node'],
    install_requires=['setuptools', 'rclpy', 'geometry_msgs', 'std_msgs'],
    zip_safe=True,
    maintainer='YOUR_NAME',
    maintainer_email='YOUR_EMAIL',
    description='World model node for RoboSoccer',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'world_model_node = world_model_node:main',
        ],
    },
)

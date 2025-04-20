from setuptools import setup

package_name = 'robosoccer_localization'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=['localization_node'],
    install_requires=['setuptools', 'rclpy', 'geometry_msgs', 'sensor_msgs'],
    zip_safe=True,
    maintainer='YOUR_NAME',
    maintainer_email='YOUR_EMAIL',
    description='Localization node for RoboSoccer',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'localization_node = localization_node:main',
        ],
    },
)

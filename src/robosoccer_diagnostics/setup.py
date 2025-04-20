from setuptools import setup

package_name = 'robosoccer_diagnostics'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=['diagnostics_node'],
    install_requires=['setuptools', 'rclpy', 'std_msgs'],
    zip_safe=True,
    maintainer='YOUR_NAME',
    maintainer_email='YOUR_EMAIL',
    description='Diagnostics node for RoboSoccer',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'diagnostics_node = diagnostics_node:main',
        ],
    },
)

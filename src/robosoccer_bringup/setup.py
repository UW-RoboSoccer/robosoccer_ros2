from setuptools import setup

package_name = 'robosoccer_bringup'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=[],
    install_requires=['setuptools', 'rclpy'],
    zip_safe=True,
    maintainer='YOUR_NAME',
    maintainer_email='YOUR_EMAIL',
    description='Bringup package for RoboSoccer',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)

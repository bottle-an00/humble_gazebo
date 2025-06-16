from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'my_python_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={# 터미널에서 직접 실행할 수 있는 excutable 파일
        'console_scripts': [
             'timer_node = my_python_package.timer:main', #실행가능한 파일 생성 (.py는 붙이지 않는다).
             'fast_timer_node = my_python_package.fast_timer:main',
        ],
    },
)

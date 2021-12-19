from setuptools import setup, find_packages
  
long_description = open("README.md").read()
  
setup(
        name ='stresst',
        version ='0.0.3',
        author ='Ryan Chou',
        author_email ='',
        url ='https://ryanchou.dev',
        description ='Stress test your Python solutions!',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'stresst = stress.strs:main'
            ]
        },
        classifiers =[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
		],
        keywords ='competitive-programming python problems testing',
        install_requires = "",
        zip_safe = False
)
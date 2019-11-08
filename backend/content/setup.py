import setuptools

setuptools.setup(name='trends-service',
                 version='1.0',
                 description='Provides actual trends',
                 url='http://github.com/oleg.fry/project-dummy',
                 author='Anonymous',
                 author_email='oleg.fry@gmail.com',
                 license='MIT',
                 python_requires='>=3.7',
                 include_package_data=True,
                 zip_safe=False,
                 install_requires=[
                     'flask',
                 ],
                 )

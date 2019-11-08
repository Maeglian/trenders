import setuptools

setuptools.setup(name='content',
                 version='1.0',
                 description='',
                 url='http://github.com/oleg.fry/project-dummy',
                 author='Maria Ibragimova',
                 author_email="antonina.gerasiova@yandex.ru",
                 license='MIT',
                 python_requires='>=3.7',
                 include_package_data=True,
                 zip_safe=False,
                 packages=setuptools.find_packages(),
                 install_requires=[
                     'Flask',
                     'sqlalchemy',
                     'psycopg2-binary',
                     'alembic',
                     'requests',
                 ],
                 )

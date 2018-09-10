from setuptools import setup, find_packages

setup(
    name='ikarion_data_infrastructure',
    version='0.0.1',
    packages=find_packages(exclude=["test"]),
    # packages=['ikarion_data_management.data_model_api',
    #           'ikarion_data_management',
    #           'ikarion_data_management.log_aggregator',
    #           'ikarion_data_management.data_access_layer',
    #           'ikarion_data_management.data_access_layer.xapi_access_layer',
    #           'ikarion_data_management.data_access_layer.model_db_access_layer'],
    url='',
    license='',
    author='hecking',
    author_email='hecking@collide.info',
    description=''
)

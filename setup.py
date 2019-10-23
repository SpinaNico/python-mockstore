from setuptools import setup

setup(
    name='mock_base',
    version='0.0.3',
    description='mock for firebase_admin',
    author='Spina Nico',
    author_email='spinanico93@gmail.com',
    url='https://github.com/SpinaNico/python-mock-base',
    packages=["mock_base", "mock_base.mockstore", "mock_base.mock_store.firestore_impl"],
    install_requires=[]
)
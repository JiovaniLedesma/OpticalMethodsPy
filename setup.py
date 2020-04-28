from setuptools import setup

# Current status: pre-alpha

setup(name='opticalmethodspy',
      version='0.1.0',
      description='Python library for Optical Methods',
      author='Jiovani Ledesma Arredondo',
      author_email='jiovaniledesmaa@gmail.com',
      license = "MIT",
      keywords=["Optics","Methods", "Optical"],
      url='https://github.com/JiovaniLedesma/OpticalMethodsPy',
      packages=['opticalmethodspy'],
      install_requires=['numpy','sympy','matplotlib','scipy'],
      classifiers=[
      "Development Status :: 2 - Pre-Alpha",
      "Intended Audience :: Education",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
      "Programming Language :: Python",
      "Programming Language :: Python :: 3.8",
      "Programming Language :: Python :: Implementation :: CPython",
      ]
      )
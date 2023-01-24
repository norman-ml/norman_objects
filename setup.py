from setuptools import setup, find_packages

setup(
      name="norman-objects",
      version="0.1",
      description="norman objects common classes",
      url="https://github.com/yonatankarimish/Norman-Objects",
      author="Yonatan Alon",
      author_email="yonatankarimish@gmail.com",
      license="proprietary",
      packages=find_packages(),
      install_requires=[
            "pydantic"
      ],
      zip_safe=False
)

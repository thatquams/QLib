import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
  name="quelib",
  version="0.0.1",
  description="",
  long_description=README,
  long_description_content_type="text/markdown",
  author="Abdulraheem Quwam",
  author_email="dev.abdulraheem@gmail.com",
  license="MIT",
  packages=["quelib"],
  zip_safe=False
)
from setuptools import setup, find_packages

setup(
    name="self_correction_human_parsing",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "torch",
        "torchvision",
        "opencv-python",
        "pillow",
        "scipy",
    ],
)

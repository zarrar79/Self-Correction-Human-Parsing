from setuptools import setup, find_packages

setup(
    name="schp",
    version="0.1",
    description="Self-Correction for Human Parsing",
    author="Peike Li",
    url="https://github.com/PeikeLi/Self-Correction-Human-Parsing",
    packages=find_packages(include=["schp", "schp.*"]),
    install_requires=[
        "torch",
        "torchvision",
        "opencv-python",
        "Pillow",
        "scipy",
    ],
    python_requires=">=3.6",
)

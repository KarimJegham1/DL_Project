from setuptools import find_packages,setup

from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="Xray_Classification",
    version="0.0.1",
    author="Mohamed Karim Jegham",
    author_email="mohamedkarim.jegham@ensi-uma.tn",
    install_requires=get_requirements(r"C:\\Users\\TOPINFORMATIQUE\\Desktop\\DL_Project\\requirements_dev.txt"),
    package=find_packages()

)
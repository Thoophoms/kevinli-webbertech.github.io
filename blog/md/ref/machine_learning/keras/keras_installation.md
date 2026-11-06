# KERAS INSTALLATION

## Installation Requirement

* Python-3.5 and above
* Support in all major OS

## Steps for installation

*create virtual environment*

Virtualenv-to manage python packages for different projects
recommended to avoid breaking packages installed in other environments.

**Linux/Mac OS**

`python3 -m venv keras`

“kerasenv” directory is created with bin,lib and include folders upon executing the above command.

**Windows**

`py -m venv keras`

*Activate the environment*

**Linux/Mac OS**

Go to “keras” and give the command below

```shell
-$ cd kerasvenv 
kerasvenv $ source bin/activate
```

**Windows**

-Go to “keras” and give the command below

`.\env\Scripts\activate`

*Python libraries*

Keras relies on the following libraries,

* Numpy
* Pandas
* Scikit-learn
* Matplotlib
* Scipy
* Seaborn

Install all the above libraries


`pip install numpy`
`pip install pandas`
`pip install matplotlib`
`pip install scipy`
`pip install -U scikit-learn`
`pip install seaborn`
`pip install keras`

Note: For scikit-learn installation, it has requirements for its installation as the following dependencies,

* Python version 3.5 or higher
* NumPy version 1.11.0 or higher
* SciPy version 0.17.0 or higher
* joblib 0.11 or higher.

Keras Installation Using Python

*Quit virtual environment*

after changes in the project enter command - 

`deactivate`

## Anaconda Installation

*Create a new conda environment*

`conda create --name PythonCPU`

Activate conda environment

`activate PythonCPU`

*Install spyder*

`conda install spyder`

*Install Keras*

`conda install -c anaconda keras`

*Launch spyder*

`spyder`

To ensure everything was installed correctly, import all the modules, it will add everything and if anything went wrong, you will get module not found error message.
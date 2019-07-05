# Rendering-simulation
## Displaying XCos simulation in LaTeX

Xcos is a Scilab tool. It is used to model and simulate hybrid dynamic systems. It has a graphical editor in which one can drag and drop the models and connect the blocks. Every block has predefined functions, properties, and parameters. The tool comes along with one limitation that is one can only view the simulation and its values in the tool's GUI. Currently, there is no automated way of capturing the blocks,the connected models and their simulation parameters in a document. The aim of this project is to capture these simulations and represent them in a LaTeX file. 

## Getting Started
## Requirements
* Python 3.6.7
* Scilab 6.0.2 or Scilab 6.0.1
* PyLaTeX 1.3.0

## Installation
### Scilab
```bash
$ sudo apt install scilab
```
### PyLaTeX
 PyLaTeX works on Python 2.7 and 3.3+ and is simply installed using pip:
```bash
$ pip install pylatex
```
## Running the script
* Clone or download this repository into your working directory.
* Navigate to your working directory and run the following command in terminal to run the script:
```bash
$ python3 input_processor.py <*.xcos file path> <image file directory> <image file name> <desired output filename>
```


## Contributing

Please read [CONTRIBUTING.md](https://github.com/fresearchgroup/Rendering-simulation/) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/fresearchgroup/Rendering-simulation/tags). 

## Authors

* **Makrand Rajagopal** - *Initial work* - [makrandr1999](https://github.com/makrandr1999)
* **Kanad Gaikwad** - *Initial work* - [kyoyag2212](https://github.com/kyoyag2212)

See also the list of [contributors](https://github.com/fresearchgroup/Rendering-simulation/contributors) who participated in this project.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details




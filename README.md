# Python Tool Skeleton

This is just an example skeleton for building a project or tool in Python. I'm creating this skeleton because I keep copying ``setup.py`` file from my earlier projects.

## Prerequisites

* Python 3
* pipreqs

If you don't have ``pipreqs`` installed in your environment, use the package manager [pip](https://pip.pypa.io/en/stable/) to install ``pipreqs`` as follows:

```bash
$ pip install pipreqs
```

## Usage

Clone this repository:

```bash
$ git clone https://github.com/raviprakashgiri/Python-Tool-Skeleton
```

Complete ``setup.py`` file and make necessary changes. Once you have changed the project description in ``setup.py``, add any dependencies your project has:

```bash
$ pipreqs path/to/Python-Tool-Skeleton
```

The above command will create a ``requirements.txt`` file in Python-Tool-Skeleton. Copy the contents of ``requirements.txt`` and paste into ``install_requires`` list of your setup.py file. Delete ``requirements.txt`` thereafter.

Change the project name to the one you want:

```bash
$ mv Python-Tool-Skeleton/Python-Tool-Skeleton Python-Tool-Skeleton/<your project name>
$ mv Python-Tool-Skeleton <your project name>
```

Create python files and write all your code under ``<your project name>/<your project name>`` folder. Once you have completed your project, run the following: 

* ``$ cd path/to/Python-Tool-Skeleton``

* ``$ python setup.py sdist``

The above commands will create a dist directory where you can find your distribution build with files per your ``MANIFEST.in``.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
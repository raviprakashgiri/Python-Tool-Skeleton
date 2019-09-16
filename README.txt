This is just an example skeleton for building a project or tool in Python. I'm creating this skeleton because I keep copying ``setup.py`` file from my earlier projects.

Python Tool Skeleton
---------------------
Assuming you installed ``Python`` and ``pipreqs``, run the following commands to complete your ``setup.py``:

* ``pipreqs path/to/Python-Tool-Skeleton``

The above command will create a requirements.txt file in the root folder. Copy those requirements and paste them into your setup.py file in install_requires list.

Now, once you are done with your project and want to ship it as a compressed file, run the following commands to create a distribution file:

* ``cd path/to/Python-Tool-Skeleton``

* ``python setup.py sdist``

The above commands will create a dist directory where you can find your distribution build with files per your ``MANIFEST.in``.

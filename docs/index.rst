.. PyNursery documentation master file, created by
   sphinx-quickstart on Tue Jun  8 20:23:31 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyNursery's documentation!
=====================================
PyNursery was deviced for the final assignment of Introduction to Artificial Intelligence - B

It was created in May 2021 by Tjalle Wolterink

In this documentation you will find all the relevant information and documentation for each class.

.. toctree::
   :maxdepth: 4
   :caption: Contents:

Installation instructions
=====================================

This build of PyNursery was built and only tested on python 3.8.7, pip 20.2.3, node v14.15.4 and npm 6.14.10.

1. First install all the requirements needed for python with the following command (whilst being in the root folder of this project):

.. code-block:: bash

   pip install -r ./requirements.txt

2. Secondly make sure all the node packages that are needed are installed. You can do this by going to the :code:`frontend` directory. And executing the following command:

.. code-block:: bash

   npm i .

3. Following this, you can run the frontend server by executing the following command (in the :code:`frontend` directory):

.. code-block:: bash

   npm run serve

This will take a while to boot, because Node has to compile all the code and modules from scratch.

4. Next up, you need to run the backend/api server in python. For this run the following command from the project root directory:
   
.. code-block:: bash

   uvicorn api:app --reload

This should work almost immeaditely, if everything has gone well, there data should be shown on the frontend.

5. You can now visit the frontend by going to http://localhost:8080/ or -. Also you can view the API documentation at http://127.0.0.1:8000/docs or http://localhost:8000/docs (Alternative documenation style is available at http://127.0.0.1:8000/redoc)

   Here you can also find all the information regarding expected input and expected output of the API when calling it.

api
=====================================
.. automodule:: api
   :members:   

src\\db_interface
=====================================
.. automodule:: db_interface
   :members:   

src\\plant_metadata
=====================================
.. automodule:: plant_metadata
   :members:   
  
src\\utils
=====================================
.. automodule:: utils
   :members:  

routes\\locations
=====================================
.. automodule:: locations
   :members:

routes\\plant_batch
=====================================
.. automodule:: plant_batch
   :members:
   
routes\\plant_families
=====================================
.. automodule:: plant_families
   :members:

routes\\plants
=====================================
.. automodule:: plants
   :members:

routes\\tray_types
=====================================
.. automodule:: tray_types
   :members:

   

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

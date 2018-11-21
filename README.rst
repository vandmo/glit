Plit
====
Clones sets of git repositories.

Example config
--------------
~/.plit/sets
*******************
.. code-block:: cfg

  [work-common]
  folder: ~/repos/work/
  repositories: ~/work/common.repositories
  [work-team]
  folder: ~/repos/work/
  repositories: ~/work/myteam.repositories
  [private]
  folder: ~/repos/private/
  repositories: ~/somecool.repositories

~/somecool.repositories
***********************
.. code-block::

  . git@github.com:vandmo/plit.git
  cool/libs https://github.com/pallets/click
  cool/libs https://github.com/awslabs/cfn-python-lint.git

Commands
--------
- ``plit clone-all``
- ``plit clone-set private``
- ``plit clone --to-set private --prefix vandmo/python git@github.com:vandmo/plit.git``
- ``plit config add-set --folder '~/repos/private/' '~/somecool.repositories'``

Plit
====
Clones sets of git repositories.

Example config
--------------
~/.plit/config.yaml
*******************
.. code-block:: yaml

  sets:
    -
      name: work-common
      folder: ~/repos/work/
      repositories: ~/work/common.repositories
    -
      name: work-team
      folder: ~/repos/work/
      repositories: ~/work/myteam.repositories
    -
      name: private
      folder: ~/repos/private/
      repositories: ~/somecool.repositories

Commands
--------
- ``plit clone-all``
- ``plit clone-set private``
- ``plit clone --to-set private --prefix vandmo/python git@github.com:vandmo/plit.git``

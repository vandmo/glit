Plit
====
Clones sets of git repositories.

Example config
--------------
~/.plit/config.yaml
.. code-block:: yaml
  work-common:
    folder: ~/repos/work/
    list: ~/work/common.list
  work-team:
    folder: ~/repos/work/
    list: ~/work/myteam.list
  private:
    folder: ~/repos/private/
    list: ~/repos.list

Commands
--------
- ``plit clone --all``
- ``plit clone --set private``
- ``plit clone --set private --prefix vandmo/python --repository git@github.com:vandmo/plit.git``
Plit
====
Manages sets of git repositories.

- Clone all sets
- Clone specific set
- Fast forward all repositories
- Clone and add to set in a single command
- Configuration can be stored online

Why is Plit is different from other git managers?
-------------------------------------------------
Plit can handle more than one set of repositories
*************************************************
Let's say that you work on more than one project at once.
With Plit you can share the file with the set of repositories
associated with a specific project with those involved in that project.
Most other git managers only allows one set of repositories.

Plit has built in support for online shared configuration
*********************************************************
You can configure a set of repositories either in a local file or
point to a file in a git repository.
If choosing the latter storage type Plit will take care of keeping
the file in sync.

Example config
--------------
~/.plit/sets
*******************
.. code-block:: cfg

  [work-common]
  folder: ~/repos/work/
  storage: git
  repository: ssh://git.mycompany.com/project/configuration
  file: ~/work/common.repositories
  [work-team]
  folder: ~/repos/work/
  storage: git
  repository: ssh://git.mycompany.com/myteam/configuration
  file: ~/work/myteam.repositories
  [private]
  folder: ~/repos/private/
  storage: local
  file: ~/somecool.repositories

~/somecool.repositories
***********************
::

  . git@github.com:vandmo/plit.git
  cool/libs https://github.com/pallets/click
  cool/libs https://github.com/awslabs/cfn-python-lint.git

Commands
--------
- ``plit clone-all``
- ``plit clone-set private``
- ``plit clone --to-set private --prefix vandmo/python git@github.com:vandmo/plit.git``
- ``plit config add-locally-stored-set --folder '~/repos/private/' '~/somecool.repositories'``
- ``plit config add-git-stored-set --folder '~/repos/private/' git@github.com:vandmo/plit.git 'somereallycool.repositories'``

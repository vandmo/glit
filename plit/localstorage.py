
class LocallyStoredFile(object):
    def __init__(self, filename):
        self._filename = filename

    def readlines(self):
        with open(self._filename) as f:
            return f.readlines()

    def writelines(self, lines):
        with open(self._filename, 'w') as f:
            f.writelines(lines)

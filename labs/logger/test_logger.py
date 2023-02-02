import os
from pathlib import Path
from logger import log, dump_logs
from datetime import datetime

delim = "\\" if os.name == "nt" else "/"
today = datetime.today()


class TestClass:

    def test_1(self):
        '''
        Ensure logs write to file.
        '''
        log("Hello, world!")
        with open(self.get_log_file(), "r") as f:
            assert "Hello, world!" in f.read()

    def test_(self):
        '''
        Ensure log file is in correct location.
        '''
        filepath = self.get_log_file()
        assert Path(filepath).is_file()

    def get_log_file(self):
        date = "{0}-{1:02d}-{2:02d}".format(today.year, today.month, today.day)
        filename = "log-file-{0}.txt".format(date)
        folder = "{0}{1}{2}".format(Path(__file__).parent.resolve(), delim, "logs")
        return "{0}{1}{2}".format(folder, delim, filename)


test = TestClass()

print(test.get_log_file())

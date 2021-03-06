#!/usr/bin/env python
# This file is part of Xpra.
# Copyright (C) 2018 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

import os
import unittest

from xpra.util import AdHocStruct
from xpra.os_util import POSIX, OSX
from unit.server.mixins.servermixintest_util import ServerMixinTest


class FilePrintMixinTest(ServerMixinTest):

    def test_fileprint(self):
        from xpra.server.mixins.fileprint_server import FilePrintServer
        opts = AdHocStruct()
        opts.file_transfer = "yes"
        opts.file_size_limit = 10
        opts.printing = "yes"
        opts.open_files = "no"
        opts.open_url = "yes"
        opts.open_command = ""
        opts.lpadmin = ""
        opts.lpinfo = ""
        opts.add_printer_options = ""
        opts.postscript_printer = ""
        opts.pdf_printer = ""
        self._test_mixin_class(FilePrintServer, opts)

def main():
    unittest.main()


if __name__ == '__main__':
    main()

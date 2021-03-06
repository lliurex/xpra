#!/usr/bin/env python
# This file is part of Xpra.
# Copyright (C) 2019 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

import unittest

from xpra.os_util import PYTHON3
from xpra.util import AdHocStruct, typedict
from xpra.client.mixins.audio import AudioClient
from unit.client.mixins.clientmixintest_util import ClientMixinTest


class AudioClientTest(ClientMixinTest):

	def test_audio(self):
		x = AudioClient()
		self.mixin = x
		opts = AdHocStruct()
		opts.av_sync = True
		opts.speaker = "on"
		opts.microphone = "on"
		opts.sound_source = ""
		opts.speaker_codec = []
		opts.microphone_codec = []
		opts.tray_icon = ""
		x.init(opts)
		x.send = self.send
		assert x.get_caps() is not None
		x.server_capabilities = typedict({
			"sound.receive" : True,
			"sound.send" : True,
			"sound.encoders" : ["mp3", "opus"],
			"sound.decoders" : ["mp3", "opus"],
			"sound.ogg-latency-fix" : True,
			})
		self.glib.timeout_add(5000, self.stop)
		x.parse_server_capabilities()
		self.main_loop.run()
		#print("packets=%s" % (self.packets,))
		assert len(self.packets)>2
		assert self.verify_packet(0, ("sound-control", "start")) or self.verify_packet(1, ("sound-control", "start"))
		assert self.verify_packet(1, ("sound-data", )) or self.verify_packet(0, ("sound-data", ))
		assert self.verify_packet(-2, ("sound-control", "stop"))
		assert self.verify_packet(-1, ("sound-control", "new-sequence"))

def main():
	if PYTHON3:
		unittest.main()


if __name__ == '__main__':
	main()

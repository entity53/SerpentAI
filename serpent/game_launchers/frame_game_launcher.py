from serpent.game_launcher import GameLauncher, GameLauncherException
from serpent.utilities import is_linux, is_macos, is_windows

import shlex
import subprocess


class FrameGameLauncher(GameLauncher):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def launch(self, **kwargs):
        return
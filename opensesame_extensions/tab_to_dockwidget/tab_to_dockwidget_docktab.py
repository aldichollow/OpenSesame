# coding=utf-8

"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""

from libopensesame.py3compat import *
from qtpy.QtWidgets import QDockWidget


class DockTab(QDockWidget):

	"""
	desc:
		A dockwidget that holds a tab.
	"""

	def __init__(self, tab_to_dockwidget, widget, name):

		QDockWidget.__init__(self, name, tab_to_dockwidget.main_window)
		self._tab_to_dockwidget = tab_to_dockwidget
		self.setWidget(widget)
		self.setObjectName(str(widget))

	def closeEvent(self, event):

		self._tab_to_dockwidget.remove_widget(self.widget())
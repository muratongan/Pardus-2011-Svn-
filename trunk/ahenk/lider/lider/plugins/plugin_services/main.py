#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    Service magement module
"""

# Standard modules
import simplejson

# Qt4 modules
from PyQt4 import QtGui
from PyQt4 import QtCore

# Generated UI module
from ui_services import Ui_widgetServices

# Helper modules
from lider.helpers import plugins
from lider.helpers import wrappers
from lider.helpers import i18n

i18n = i18n.i18n

# Red, Green, Blue
SERV_START_COLOR = (24, 178, 24)
SERV_STOP_COLOR = (178, 24, 24)

class WidgetModule(QtGui.QWidget, Ui_widgetServices, plugins.PluginWidget):
    """
        Service management UI.
    """
    def __init__(self, parent=None):
        """
            Constructor for main window.

            Arguments:
                parent: Parent object
        """
        plugins.PluginWidget.__init__(self)
        QtGui.QWidget.__init__(self, parent)

        # Attach generated UI
        self.setupUi(self)

        # UI events
        self.connect(self.pushStart, QtCore.SIGNAL("clicked()"), self.__slot_start_service)
        self.connect(self.pushStop, QtCore.SIGNAL("clicked()"), self.__slot_stop_service)

        # Package index
        self.package_index = {}

        self.start_set = []
        self.stop_set = []

        self.groupBox = QtGui.QGroupBox()

        #self.tableWidget.setUpdatesEnabled(True);

    def set_item(self, item):
        """
            Sets directory item that is being worked on.
            Not required for global widgets.
        """
        self.item = item
        if self.item:
            if not self.item.folder:
                self.groupBox.setEnabled(True)
        else:
            self.groupBox.setEnabled(False)
            rc = self.tableWidget.rowCount()
            for i in range(rc):
                self.tableWidget.removeRow(0)

    #def showEvent(self, event):
    def showEvent(self):
        """
            Things to do before widget is shown.
        """
        if self.item:
            print "\n\n item name %s , item domain %s" %(self.item.name, self.talk.domain)
            jid = "%s@%s" % (self.item.name, self.talk.domain)
            self.talk.send_command(jid, "service.info")

    def get_type(self):
        """
            Widget type.

            Should return TYPE_GLOBAL or TYPE_SINGLE
        """
        return plugins.TYPE_SINGLE

    def get_classes(self):
        """
            Returns a list of policy class names.
        """
        return ["servicePolicy"]

    def load_policy(self, policy):
        """
            Main window calls this method when policy is fetched from directory.
            Not required for global widgets.
        """
        self.start_set = policy.get("serviceStart", [])
        self.stop_set = policy.get("serviceStop", [])
        print "load policy ------ start set:"
        print self.start_set
        print "load policy -------stop set:"
        print self.stop_set


    def dump_policy(self):
        """
            Main window calls this method to get policy generated by UI.
            Not required for global widgets.
        """
        policy = {
            "serviceStart": self.start_set,
            "serviceStop": self.stop_set,
        }
        return policy

    def talk_message(self, sender, command, arguments=None):
        """
            Main window calls this method when an XMPP message is received.
        """
        startset = []
        stopset = []
        print "-----  TALK MESSAGE IS CALLED  -----"
        print command


        print "---- information ----"
        print "start set size %d" %len(self.start_set)
        print self.start_set
        print "stop set size %d" %len(self.stop_set)
        print self.stop_set

        for services in self.start_set:
            #print services
            for service in services.split(","):
                #print service
                startset.append(service)


        for services in self.stop_set:
            #print services
            for service in services.split(","):
                #print service
                stopset.append(service)


        if command == "service.info":

            self.tableWidget.setRowCount(len(arguments))
            print "----------- ARGUMENTS --------------"
            index = 0

            arguments.sort(key=lambda t : tuple(t[0].lower()))
            print arguments

            for name, desc, status in arguments:
                item_description = QtGui.QTableWidgetItem(str(desc))
                self.tableWidget.setItem(index, 0, item_description)

                item_name = QtGui.QTableWidgetItem(str(name))
                self.tableWidget.setItem(index, 3, item_name)

                item_status = QtGui.QTableWidgetItem()

                if status in ['started', 'on', 'conditional_started']:
                    item_status.setText(i18n("Running"))
                    state = True
                else:
                    item_status.setText(i18n("Stopped"))
                    state = False

                for start in startset:
                    if start== str(name):
                        item_status.setIcon(wrappers.Icon("flag-green"))

                for stop in stopset:
                    if stop == str(name):
                        item_status.setIcon(wrappers.Icon("flag-red"))


                self.tableWidget.setItem(index, 1, item_status)

                if status in ['stopped', 'on']:
                    item_autostart = QtGui.QTableWidgetItem(i18n("Yes"))
                elif status in ['conditional_started', 'conditional_stopped']:
                    item_autostart = QtGui.QTableWidgetItem(i18n("Conditional"))
                else:
                    item_autostart = QtGui.QTableWidgetItem(i18n("No"))
                self.tableWidget.setItem(index, 2, item_autostart)

                if state:
                    self._set_service_item_color(index, SERV_START_COLOR)
                else:
                    self._set_service_item_color(index, SERV_STOP_COLOR)

                index += 1
        elif command in ["service.start.status", "service.stop.status"]:
            msg = QtGui.QMessageBox.information(self, i18n("Status"), arguments)

    def talk_status(self, sender, status):
        """
            Main window calls this method when an XMPP status is changed.
        """
        pass

    def __slot_start_service(self):
        """
            This method is called when the start button clicked to start the selected service
        """
        item = self.tableWidget.selectedItems()
        item_name = str(item[3].text())

        for x in self.stop_set:
            print "xxxxxxxxx:"
            print x
            if x == item_name:
                print "equal %s" %x
                self.stop_set.remove(x)

        if item_name not in self.start_set:
            self.start_set.append(item_name)
        print self.start_set
        print self.stop_set

        item_status = item[1]
        item_status.setIcon(wrappers.Icon("flag-green"))

    def __slot_stop_service(self):
        """
            This method is called when the stop button clicked to stop the selected service
        """
        item = self.tableWidget.selectedItems()
        item_name = str(item[3].text())

        for x in self.start_set:
            print "xxxxxxxxx:"
            print x
            if x == item_name:
                print "equal %s" %x
                self.start_set.remove(x)

        if item_name not in self.stop_set:
            self.stop_set.append(item_name)
        print self.start_set
        print self.stop_set

        item_status = item[1]
        item_status.setIcon(wrappers.Icon("flag-red"))

    def _set_service_item_color(self, row_index, color):

        col = self.tableWidget.columnCount()

        for col_index in range(col):
            self.tableWidget.item(row_index, col_index).setForeground(QtGui.QBrush(QtGui.QColor(color[0], color[1], color[2])))
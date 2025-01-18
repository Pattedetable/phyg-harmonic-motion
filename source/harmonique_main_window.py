#
# Copyright 2019-2025 Manuel Barrette
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


from PyQt6 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.animation as anim
import os, platform
import particle


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, Dialog, parent):

        self.figure = plt.figure()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget) # Quit
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 14, 0, 1, 3)

#        self.pushButton = QtWidgets.QPushButton(self.centralwidget) # Export video
#        self.pushButton.setObjectName("pushButton")
#        self.gridLayout.addWidget(self.pushButton, 11, 0, 1, 3)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget) # Restart
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 13, 0, 1, 3)


        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 12, 0, 1, 1)

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget) # Sine
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 3)

        self.radioButton2 = QtWidgets.QRadioButton(self.centralwidget) # Cosine
        self.radioButton2.setObjectName("radioButton2")
        self.gridLayout.addWidget(self.radioButton2, 1, 0, 1, 3)


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)

        self.horizontalSlider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal, self.centralwidget) # Amplitude
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(5)
        self.horizontalSlider.setPageStep(2)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 5, 0, 1, 3)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)

        self.horizontalSlider2 = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal, self.centralwidget) # Frequency
        self.horizontalSlider2.setMinimum(1)
        self.horizontalSlider2.setMaximum(8)
        self.horizontalSlider2.setPageStep(4)
        self.horizontalSlider2.setObjectName("horizontalSlider2")
        self.gridLayout.addWidget(self.horizontalSlider2, 7, 0, 1, 3)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)

        self.horizontalSlider3 = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal, self.centralwidget) # Phase constant
        self.horizontalSlider3.setMinimum(-8)
        self.horizontalSlider3.setMaximum(8)
        self.horizontalSlider3.setPageStep(4)
        self.horizontalSlider3.setObjectName("horizontalSlider3")
        self.gridLayout.addWidget(self.horizontalSlider3, 9, 0, 1, 3)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 10, 0, 1, 1)

        self.horizontalSlider4 = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal, self.centralwidget) # Damping
        self.horizontalSlider4.setMinimum(0)
        self.horizontalSlider4.setMaximum(10)
        self.horizontalSlider4.setPageStep(2)
        self.horizontalSlider4.setObjectName("horizontalSlider4")
        self.gridLayout.addWidget(self.horizontalSlider4, 11, 0, 1, 3)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)


        self.comboBox = QtWidgets.QComboBox(self.centralwidget) # Graph type
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 3, 0, 1, 3)

        self.canvas = FigureCanvas(self.figure) # Grap
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas.sizePolicy().hasHeightForWidth())
        self.canvas.setSizePolicy(sizePolicy)
        self.canvas.setObjectName("canvas")
        self.gridLayout.addWidget(self.canvas, 0, 3, 13, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1001, 25))
        self.menubar.setObjectName("menubar")
        self.menu_aide = QtWidgets.QMenu(self.menubar)
        self.menu_aide.setObjectName("menu_aide")
        MainWindow.setMenuBar(self.menubar)
        self.action_propos = QtGui.QAction(MainWindow)
        self.action_propos.setObjectName("action_propos")
        self.menu_aide.addAction(self.action_propos)
        self.menubar.addAction(self.menu_aide.menuAction())

        # Initial parameters
        self.horizontalSlider.setValue(1)
        self.horizontalSlider2.setValue(4)
        self.horizontalSlider3.setValue(0)
        self.horizontalSlider4.setValue(0)
        self.radioButton.toggle()
        self.comboBox.setCurrentIndex(0)
#        self.horizontalSlider4.setDisabled(True)
#        self.label_4.setDisabled(True)

        # To prevent the canvas from being destroyed when using the welcome screen
        self.canvas.destroyed.connect(lambda: self.message())

        # Operating system detection
        self.systeme_exploitation = platform.system()
#        if self.systeme_exploitation == "Darwin":
#            self.pushButton.setDisabled(True)

        self.retranslateUi(MainWindow)

        # Start animation
        self.animationTempsReel()

        # Buttons triggers
        self.action_propos.triggered.connect(lambda: Dialog.show())
        self.horizontalSlider.valueChanged['int'].connect(lambda: self.stopAnim())
        self.horizontalSlider.valueChanged['int'].connect(lambda: self.animationTempsReel())
        self.horizontalSlider.valueChanged['int'].connect(lambda: self.retranslateUi(MainWindow))
        self.horizontalSlider2.valueChanged['int'].connect(lambda: self.stopAnim())
        self.horizontalSlider2.valueChanged['int'].connect(lambda: self.animationTempsReel())
        self.horizontalSlider2.valueChanged['int'].connect(lambda: self.retranslateUi(MainWindow))
        self.horizontalSlider3.valueChanged['int'].connect(lambda: self.stopAnim())
        self.horizontalSlider3.valueChanged['int'].connect(lambda: self.animationTempsReel())
        self.horizontalSlider3.valueChanged['int'].connect(lambda: self.retranslateUi(MainWindow))
        self.horizontalSlider4.valueChanged['int'].connect(lambda: self.stopAnim())
        self.horizontalSlider4.valueChanged['int'].connect(lambda: self.animationTempsReel())
        self.horizontalSlider4.valueChanged['int'].connect(lambda: self.retranslateUi(MainWindow))
        self.radioButton.toggled.connect(lambda: self.stopAnim())
        self.radioButton.toggled.connect(lambda: self.animationTempsReel())
        self.radioButton2.toggled.connect(lambda: self.stopAnim())
        self.radioButton2.toggled.connect(lambda: self.animationTempsReel())
        self.pushButton_3.clicked.connect(lambda: self.stopAnim())
        self.pushButton_3.clicked.connect(lambda: self.animationTempsReel())
        self.comboBox.currentIndexChanged['int'].connect(lambda: self.stopAnim())
        self.comboBox.currentIndexChanged['int'].connect(lambda: self.animationTempsReel())


#        self.pushButton.clicked.connect(lambda: self.stopAnim())
#        self.pushButton.clicked.connect(lambda: self.exporterAnimation())
        self.pushButton_2.clicked.connect(lambda: plt.close())
        self.pushButton_2.clicked.connect(lambda: self.fermerEtAfficher(MainWindow, parent))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(self._translate("MainWindow", "Mouvement harmonique"))
        self.pushButton_2.setText(self._translate("MainWindow", "Quitter"))
        self.pushButton_3.setText(self._translate("MainWindow", "Redémarrer"))
#        self.pushButton.setText(self._translate("MainWindow", "Exporter en vidéo (.mp4)"))
        self.label.setText(self._translate("MainWindow", "Amplitude") + " [m] : " + str(self.horizontalSlider.value()))
        self.label_2.setText(self._translate("MainWindow", "Fréquence angulaire") + " [rad/s] : " + str(self.horizontalSlider2.value()/4) + " \u03C0")
        self.label_3.setText(self._translate("MainWindow", "Constante de phase") + " [rad] : " + str(self.horizontalSlider3.value()/4) + " \u03C0")
        self.label_4.setText(self._translate("MainWindow", "Amortissement") + " (" + self._translate("MainWindow", "sous-amorti") + ") : " + str(self.horizontalSlider4.value()/20))
        self.label_5.setText(self._translate("MainWindow", "Type de graphique"))
        self.radioButton.setText(self._translate("MainWindow", "Sinus"))
        self.radioButton2.setText(self._translate("MainWindow", "Cosinus"))
        self.comboBox.setItemText(0, self._translate("MainWindow", "Position"))
        self.comboBox.setItemText(1, self._translate("MainWindow", "Vitesse"))
        self.comboBox.setItemText(2, self._translate("MainWindow", "Accélération"))


        self.menu_aide.setTitle(self._translate("MainWindow", "Aide"))
        self.action_propos.setText(self._translate("MainWindow", "À propos"))

    def message(self):
#        print("Destruction")
        pass

    def disableAll(self, boolean):
        self.horizontalSlider.setDisabled(boolean)
        self.horizontalSlider2.setDisabled(boolean)
        self.horizontalSlider3.setDisabled(boolean)
        self.horizontalSlider4.setDisabled(boolean)
#        self.pushButton.setDisabled(boolean)
        self.pushButton_2.setDisabled(boolean)
        self.pushButton_3.setDisabled(boolean)
        self.menu_aide.setDisabled(boolean)
        self.label.setDisabled(boolean)
        self.label_2.setDisabled(boolean)
        self.label_3.setDisabled(boolean)
        self.label_4.setDisabled(boolean)
        self.label_5.setDisabled(boolean)
        self.radioButton.setDisabled(boolean)
        self.radioButton2.setDisabled(boolean)
        self.comboBox.setDisabled(boolean)


    def fermerEtAfficher(self, MainWindow, window_autre):
        if window_autre:
            window_autre.show()
        MainWindow.close()
#        app = QtWidgets.QApplication.instance()
#        app.closeAllWindows()

    def stopAnim(self):
        self.oscillation.event_source.stop()

    def enregistrer(self):
        if self.systeme_exploitation == 'Windows':
            fichier = QtWidgets.QFileDialog.getSaveFileName(None, self._translate("MainWindow", "Enregister sous..."), os.getenv('HOMEPATH'), 'Vidéos (*.mp4)')
        elif self.systeme_exploitation == 'Darwin' or 'Linux':
            fichier = QtWidgets.QFileDialog.getSaveFileName(None, self._translate("MainWindow", "Enregister sous..."), os.getenv('HOME'), 'Vidéos (*.mp4)')
        else:
            print("Système non supporté officiellement.  Enregistrement dans le dossier de travail sous le nom 'animation.mp4'.")
            fichier = ['animation', None]
        return fichier[0]

    def exporterAnimation(self):
        nom_anim = self.enregistrer()
        if nom_anim[-4:] != ".mp4":
            nom_anim = nom_anim + ".mp4"
        self.oscillation.save(nom_anim)
        self.animationTempsReel()


    def initAnimation(self):
        """ Define parameters and setup the base graphic """

        self.figure.clear()

        # Important parameters
        amplitude = self.horizontalSlider.value()
        omega = self.horizontalSlider2.value()*np.pi/4
        constante = self.horizontalSlider3.value()*np.pi/4
        amortissement = self.horizontalSlider4.value()/20

        omega_prime = omega*np.sqrt(1 - amortissement**2)

        y_label = [r"$-A$", r"$0$", r"$A$"]
        v_label = [r"$-A\omega$", r"$0$", r"$A\omega$"]
        a_label = [r"$-A\omega^2$", r"$0$", r"$A\omega^2$"]

#        nb_particules = 1
        num_frames = 45
#        grilley = [0]
        y = 0

        grillex = np.linspace(0, 2*np.pi, 200)

        # Creation of the particle
        x_eq = 0
        ball = particle.Particule(x_eq, amplitude)
        cercle = plt.Circle((ball.x_eq, y), 0.3, color="k")

        self.ax1 = self.figure.add_subplot(121)
        self.ax2 = self.figure.add_subplot(122)

        self.ax1.add_artist(cercle)
#        self.ax1.set_aspect("equal")
#        self.ax2.set_aspect("equal")

        self.ax1.axis([-5, 5, -5, 5])
        self.ax1.set_xticks([])
        self.ax1.set_yticks([-amplitude, 0, amplitude])
        self.ax1.set_yticklabels(y_label)

        self.ax2.yaxis.set_label_position("right")
        self.ax2.yaxis.set_ticks_position("right")

        self.ax1.set_ylabel(self._translate("MainWindow", "Position") + " (m)")
        self.ax2.set_xlabel(self._translate("MainWindow", "Temps") + " (s)")

        self.ax1.grid(True)
        self.ax2.grid(True)

        if self.comboBox.currentIndex() == 0:
            self.ax2.set_ylabel(self._translate("MainWindow", "Position") + " (m)")
            self.ax2.axis([0, 2*np.pi, -5, 5])
            self.ax2.set_yticks([-amplitude, 0, amplitude])
            self.ax2.set_yticklabels(y_label)
            couleur = "r"
        elif self.comboBox.currentIndex() == 1:
            self.ax2.set_ylabel(self._translate("MainWindow", "Vitesse") + " (m/s)")
            self.ax2.axis([0, 2*np.pi, -5*2*np.pi, 5*2*np.pi])
            self.ax2.set_yticks([-amplitude*omega, 0, amplitude*omega])
            self.ax2.set_yticklabels(v_label)
#            amplitude = amplitude*omega
#            constante = constante + np.pi/2
            couleur = "b"
        elif self.comboBox.currentIndex() == 2:
            self.ax2.set_ylabel(self._translate("MainWindow", "Accélération") + " (m/s²)")
            self.ax2.axis([0, 2*np.pi, -5*4*np.pi**2, 5*4*np.pi**2])
            self.ax2.set_yticks([-amplitude*omega**2, 0, amplitude*omega**2])
            self.ax2.set_yticklabels(a_label)
#            amplitude = amplitude*omega**2
#            constante = constante + np.pi
            couleur = "g"

        if self.radioButton2.isChecked() == False:
            if self.comboBox.currentIndex() == 0:
                deplacement_pos = amplitude*np.exp(-omega*amortissement*grillex)*np.sin(omega_prime*grillex + constante)
            elif self.comboBox.currentIndex() == 1:
                deplacement_pos = amplitude*np.exp(-omega*amortissement*grillex)*(-omega*amortissement*np.sin(omega_prime*grillex + constante) + omega_prime*np.sin(omega_prime*grillex + constante + np.pi/2))
            elif self.comboBox.currentIndex() == 2:
                deplacement_pos = amplitude*np.exp(-omega*amortissement*grillex)*(omega**2*amortissement**2*np.sin(omega_prime*grillex + constante) - 2*omega*amortissement*omega_prime*np.sin(omega_prime*grillex + constante + np.pi/2) + omega_prime**2*np.sin(omega_prime*grillex + constante + np.pi))
        else:
            if self.comboBox.currentIndex() == 0:
                deplacement_pos = amplitude*np.exp(-omega*amortissement*grillex)*np.cos(omega_prime*grillex + constante)
            elif self.comboBox.currentIndex() == 1:
                deplacement_pos = amplitude*np.exp(-omega*amortissement*grillex)*(-omega*amortissement*np.cos(omega_prime*grillex + constante) + omega_prime*np.cos(omega_prime*grillex + constante + np.pi/2))
            elif self.comboBox.currentIndex() == 2:
                deplacement_pos = amplitude*np.exp(-omega*amortissement*grillex)*(omega**2*amortissement**2*np.cos(omega_prime*grillex + constante) - 2*omega*amortissement*omega_prime*np.cos(omega_prime*grillex + constante + np.pi/2) + omega_prime**2*np.cos(omega_prime*grillex + constante + np.pi))

        graph2, = self.ax2.plot(grillex, deplacement_pos, color=couleur)

        # Retour aux valeurs initiales
        amplitude = self.horizontalSlider.value()
        constante = self.horizontalSlider3.value()*np.pi/4

        return num_frames, omega, amplitude, constante, amortissement, ball, cercle, y


    def animationTempsReel(self):
        """ Display the animation in real time """

        [num_frames, omega, amplitude, constante, amortissement, ball, cercle, y] = self.initAnimation()

        period = 2*np.pi/omega
        num_frames = int(num_frames*period)
        omega_prime = omega*np.sqrt(1 - amortissement**2)


        if amortissement != 0:
            period = 20*period
            num_frames = 20*num_frames
        tempss = np.linspace(0, period, num_frames)

        def update(i):
            temps = tempss[i]
            if self.radioButton.isChecked() == True:
                x = np.exp(-omega*amortissement*temps)*np.sin(omega_prime*temps + constante)
            else:
                x = np.exp(-omega*amortissement*temps)*np.cos(omega_prime*temps + constante)
            position = ball.update_position(x)
            cercle.center = y, position

        self.oscillation = anim.FuncAnimation(self.figure, update, frames=num_frames, repeat=True, interval=period/num_frames)
        self.canvas.draw()

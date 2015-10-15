__author__ = 'Somebody'
# -*- coding: utf-8 -*-
__date__ = "05/ 04 / 2015"

import csv


class LectureCSV:
    def __init__(self, fichier):
        """
        :param fichier: le nom du fichier csv à importer
        """
        self.fichier = fichier


    def importation(self):
        chars = []
        """
        :param fichier: le nom du fichier csv à importer
        :return une liste de lac de tuples qui correspond aux différentes infos sur les lacs.

        """
        try:
            with open(self.fichier, 'rb') as f:
                reader = csv.reader(f, delimiter=';')
                char = []

                for row in reader:
                    char = row
                    chars.append(char)

        finally:
            f.close()
        return chars

    def creationClassLacs(self):
        """
        Fonction qui créé une un tableau d'objet de type Lac.
        :param lacs: prend un un tableau de lacs en argument
        """

        chars = self.importation()
        for i in enumerate(chars):
            print("test")




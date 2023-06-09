# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DrugiProjekt
                                 A QGIS plugin
 wtyczka na zajecia z informatyki
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-05
        copyright            : (C) 2023 by Mateusz Jankowski Kacper Kedra 
        email                : mateusz2001.pl@wp.pl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load DrugiProjekt class from file DrugiProjekt.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Drugi_Projekt import DrugiProjekt
    return DrugiProjekt(iface)

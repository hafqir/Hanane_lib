#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
"""
    Implémentation de la proclamation de la bonne parole.
 
    Usage:
 
    >>> from sm_lib import proclamer
    >>> proclamer()
"""
 
from datetime import datetime
 
__all__ = ['proclamer']
 
 
def proclamer():
    """
        Fonction de proclamation de la bonne parole. Aucun paramètre, et
        retourne None, car tout le monde say que "Ex nihilo nihil"
    """
    print "[%s] Hanane, Anil et Hamza, c'est louuuuuurd" % datetime.now()
 
 
if __name__ == "__main__":
    proclamer()

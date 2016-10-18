from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool

from ..enums import *
from ..traits import *

from .._base.Three import ThreeWidget


class Sprite(ThreeWidget):
    """Sprite
    
    Autogenerated by generate-wrappers.js 
    Date: Tue Oct 18 2016 14:57:27 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Objects/Sprite 
    """
    
    _view_name = Unicode('SpriteView').tag(sync=True)
    _model_name = Unicode('SpriteModel').tag(sync=True)



from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool

from ..enums import *
from ..traits import *

from .Light_autogen import Light


class PointLight(Light):
    """PointLight
    
    Autogenerated by generate-wrappers.js 
    Date: Tue Oct 18 2016 14:57:27 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Lights/PointLight 
    """
    
    _view_name = Unicode('PointLightView').tag(sync=True)
    _model_name = Unicode('PointLightModel').tag(sync=True)

    power = CFloat(12.566370614359172).tag(sync=True)
    distance = CFloat(0).tag(sync=True)
    decay = CFloat(1).tag(sync=True)


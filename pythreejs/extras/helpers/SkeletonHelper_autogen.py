from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool

from ...enums import *
from ...traits import *

from ..._base.Three import ThreeWidget


class SkeletonHelper(ThreeWidget):
    """SkeletonHelper
    
    Autogenerated by generate-wrappers.js 
    Date: Tue Oct 18 2016 14:57:27 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Helpers/SkeletonHelper 
    """
    
    _view_name = Unicode('SkeletonHelperView').tag(sync=True)
    _model_name = Unicode('SkeletonHelperModel').tag(sync=True)



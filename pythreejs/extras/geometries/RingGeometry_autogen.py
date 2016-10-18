from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool

from ...enums import *
from ...traits import *

from ...core.Geometry_autogen import Geometry


class RingGeometry(Geometry):
    """RingGeometry
    
    Autogenerated by generate-wrappers.js 
    Date: Tue Oct 18 2016 14:57:27 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Geometries/RingGeometry 
    """
    
    _view_name = Unicode('RingGeometryView').tag(sync=True)
    _model_name = Unicode('RingGeometryModel').tag(sync=True)

    innerRadius = CFloat(0).tag(sync=True)
    outerRadius = CFloat(50).tag(sync=True)
    thetaSegments = CInt(8).tag(sync=True)
    phiSegments = CInt(8).tag(sync=True)
    thetaStart = CFloat(0).tag(sync=True)
    thetaLength = CFloat(6.283185307179586).tag(sync=True)


# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from buoy_detect/center_color.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class center_color(genpy.Message):
  _md5sum = "5f4ca0d84246faebe88f23145abe77fd"
  _type = "buoy_detect/center_color"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """bool yellow
bool red
bool green

int64 Y_x
int64 Y_y
int64 R_x
int64 R_y
int64 G_x
int64 G_y

int64 Y_radius
int64 R_radius
int64 G_radius
"""
  __slots__ = ['yellow','red','green','Y_x','Y_y','R_x','R_y','G_x','G_y','Y_radius','R_radius','G_radius']
  _slot_types = ['bool','bool','bool','int64','int64','int64','int64','int64','int64','int64','int64','int64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       yellow,red,green,Y_x,Y_y,R_x,R_y,G_x,G_y,Y_radius,R_radius,G_radius

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(center_color, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.yellow is None:
        self.yellow = False
      if self.red is None:
        self.red = False
      if self.green is None:
        self.green = False
      if self.Y_x is None:
        self.Y_x = 0
      if self.Y_y is None:
        self.Y_y = 0
      if self.R_x is None:
        self.R_x = 0
      if self.R_y is None:
        self.R_y = 0
      if self.G_x is None:
        self.G_x = 0
      if self.G_y is None:
        self.G_y = 0
      if self.Y_radius is None:
        self.Y_radius = 0
      if self.R_radius is None:
        self.R_radius = 0
      if self.G_radius is None:
        self.G_radius = 0
    else:
      self.yellow = False
      self.red = False
      self.green = False
      self.Y_x = 0
      self.Y_y = 0
      self.R_x = 0
      self.R_y = 0
      self.G_x = 0
      self.G_y = 0
      self.Y_radius = 0
      self.R_radius = 0
      self.G_radius = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3B9q.pack(_x.yellow, _x.red, _x.green, _x.Y_x, _x.Y_y, _x.R_x, _x.R_y, _x.G_x, _x.G_y, _x.Y_radius, _x.R_radius, _x.G_radius))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 75
      (_x.yellow, _x.red, _x.green, _x.Y_x, _x.Y_y, _x.R_x, _x.R_y, _x.G_x, _x.G_y, _x.Y_radius, _x.R_radius, _x.G_radius,) = _struct_3B9q.unpack(str[start:end])
      self.yellow = bool(self.yellow)
      self.red = bool(self.red)
      self.green = bool(self.green)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3B9q.pack(_x.yellow, _x.red, _x.green, _x.Y_x, _x.Y_y, _x.R_x, _x.R_y, _x.G_x, _x.G_y, _x.Y_radius, _x.R_radius, _x.G_radius))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 75
      (_x.yellow, _x.red, _x.green, _x.Y_x, _x.Y_y, _x.R_x, _x.R_y, _x.G_x, _x.G_y, _x.Y_radius, _x.R_radius, _x.G_radius,) = _struct_3B9q.unpack(str[start:end])
      self.yellow = bool(self.yellow)
      self.red = bool(self.red)
      self.green = bool(self.green)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3B9q = struct.Struct("<3B9q")

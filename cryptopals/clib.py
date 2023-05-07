class cbytes(bytes):
  def __init__(self, a, **kwargs):
    bytes().__init__(**kwargs)
  def __xor__(self, target):
    return cbytes(x ^ y for x, y in zip(self, target))
    

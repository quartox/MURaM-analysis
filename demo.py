from muram.read import Reader
from muram import visualize


reader = Reader(nx=192, ny=96, nz=192)
file = 'result_prim_2.020000'
array = reader.read(file)
metadata = reader.get_metadata(file)
visualize.plot_vertical_rms(array, metadata=metadata)
visualize.display_heights(array, metadata=metadata)

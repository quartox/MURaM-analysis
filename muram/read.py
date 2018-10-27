import os
from pathlib import Path

import numpy as np


class Reader:
    """Read MURaM binary files."""
    dtypes = [np.float64, np.float32]
    file_metadata = {'0': 'density',
                     '1': 'x velocity',
                     '2': 'y (vertical) velocity',
                     '3': 'z velocity',
                     '4': 'internal energy',
                     '5': 'x magnetic field',
                     '6': 'y (vertical) magnetic field',
                     '7': 'z magnetic field'}

    def __init__(self, nx, ny, nz):
        self.nx = nx
        self.ny = ny
        self.nz = nz
        self.n_total = self.nx * self.ny * self.nz

    def read(self, file):
        """Read a full 3D MURaM file."""
        dtype = self.get_dtype(file)
        self._print_metadata(file)
        array = np.fromfile(file, dtype=dtype)
        return array.reshape(self.nx, self.ny, self.nz)

    def get_dtype(self, file):
        """Get the data type of the file."""
        size = os.path.getsize(file)
        for dtype in self.dtypes:
            expected_size = self.n_total * dtype(1).nbytes
            if size == expected_size:
                return dtype
        raise Exception('Cannot determine if file is float32 or float64')

    def _print_metadata(self, file):
        metadata = self.get_metadata(file)
        print(f'Reading {metadata} from {file}')

    def get_metadata(self, file):
        """Getting basic metadata about the files.

        The 3D files follow the pattern result*_0.000000, result*_1.000000, ...
        where the type index 0, 1, 2, ... determines what physical property the file contains
        and the six digit number after '.' is the timestep.
        """
        for type_index, metadata in self.file_metadata.items():
            filename = Path(file).name
            if filename.split('.')[0].endswith(type_index):
                return metadata

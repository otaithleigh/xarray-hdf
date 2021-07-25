``xarray-hdf``
++++++++++++++

Store xarray Datasets using PyTables, with support for attributes.

This is admittedly a bit hackish, but makes it easier to store Datasets and
DataFrames together in the same HDF5 file. If you just have Datasets, you should
use NETCDF.

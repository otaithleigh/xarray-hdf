from pathlib import Path
from tempfile import TemporaryDirectory

import pandas as pd
import xarray as xr

from xarrayhdf import (dataframe_to_dataset, dataset_to_dataframe,
                       dataset_to_hdf, hdf_to_dataset)

reference_ds = xr.Dataset(
    data_vars={
        'disp': range(10),
        'force': range(10),
    },
    coords={
        'time': range(10),
    },
    attrs={
        'timestamp': 'Mon Jun 28 07:42:09 2021',
        'num_analyses': 200
    },
)
reference_ds.disp.attrs['units'] = 'm'
reference_ds.time.attrs['units'] = 's'
reference_ds.force.attrs['units'] = 'N'


def test_converted_attrs():
    df = dataset_to_dataframe(reference_ds)
    assert df.attrs['timestamp'] == 'Mon Jun 28 07:42:09 2021'
    assert df.attrs['num_analyses'] == 200
    assert df.attrs['dataset_attrs::disp::units'] == 'm'
    assert df.attrs['dataset_attrs::time::units'] == 's'
    assert df.attrs['dataset_attrs::force::units'] == 'N'


def test_converted_attrs_round_trip():
    df = dataset_to_dataframe(reference_ds)
    ds = dataframe_to_dataset(df)
    assert ds.timestamp == reference_ds.timestamp
    assert ds.num_analyses == reference_ds.num_analyses
    assert ds.disp.units == reference_ds.disp.units
    assert ds.time.units == reference_ds.time.units
    assert ds.force.units == reference_ds.force.units


def test_saved_attrs():
    with TemporaryDirectory() as d:
        filename = Path(d, 'test_saved_attrs.hdf')
        dataset_to_hdf(reference_ds,
                       filename,
                       'test_saved_attrs',
                       mode='w',
                       save_attrs=True)
        ds = hdf_to_dataset(filename, 'test_saved_attrs')

    assert ds.timestamp == reference_ds.timestamp
    assert ds.num_analyses == reference_ds.num_analyses
    assert ds.disp.units == reference_ds.disp.units
    assert ds.time.units == reference_ds.time.units
    assert ds.force.units == reference_ds.force.units

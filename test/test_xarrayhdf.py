import pandas as pd
import xarray as xr

from xarrayhdf import dataset_to_dataframe

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

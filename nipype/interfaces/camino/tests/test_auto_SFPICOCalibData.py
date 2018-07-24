# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..calib import SFPICOCalibData


def test_SFPICOCalibData_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        info_file=dict(
            argstr='-infooutputfile %s',
            genfile=True,
            hash_files=False,
            mandatory=True,
        ),
        onedtfarange=dict(
            argstr='-onedtfarange %s',
            units='NA',
        ),
        onedtfastep=dict(
            argstr='-onedtfastep %f',
            units='NA',
        ),
        out_file=dict(
            argstr='> %s',
            genfile=True,
            position=-1,
        ),
        scheme_file=dict(
            argstr='-schemefile %s',
            mandatory=True,
        ),
        seed=dict(
            argstr='-seed %f',
            units='NA',
        ),
        snr=dict(
            argstr='-snr %f',
            units='NA',
        ),
        trace=dict(
            argstr='-trace %f',
            units='NA',
        ),
        twodtanglerange=dict(
            argstr='-twodtanglerange %s',
            units='NA',
        ),
        twodtanglestep=dict(
            argstr='-twodtanglestep %f',
            units='NA',
        ),
        twodtfarange=dict(
            argstr='-twodtfarange %s',
            units='NA',
        ),
        twodtfastep=dict(
            argstr='-twodtfastep %f',
            units='NA',
        ),
        twodtmixmax=dict(
            argstr='-twodtmixmax %f',
            units='NA',
        ),
        twodtmixstep=dict(
            argstr='-twodtmixstep %f',
            units='NA',
        ),
    )
    inputs = SFPICOCalibData.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_SFPICOCalibData_outputs():
    output_map = dict(
        PICOCalib=dict(),
        calib_info=dict(),
    )
    outputs = SFPICOCalibData.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

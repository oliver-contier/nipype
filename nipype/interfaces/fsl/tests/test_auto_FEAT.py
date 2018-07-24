# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..model import FEAT


def test_FEAT_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        fsf_file=dict(
            argstr='%s',
            mandatory=True,
            position=0,
        ),
        output_type=dict(),
    )
    inputs = FEAT.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_FEAT_outputs():
    output_map = dict(feat_dir=dict(), )
    outputs = FEAT.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

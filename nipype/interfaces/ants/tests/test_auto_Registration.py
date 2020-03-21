# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..registration import Registration


def test_Registration_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        collapse_output_transforms=dict(
            argstr="--collapse-output-transforms %d", usedefault=True,
        ),
        convergence_threshold=dict(requires=["number_of_iterations"], usedefault=True,),
        convergence_window_size=dict(
            requires=["convergence_threshold"], usedefault=True,
        ),
        dimension=dict(argstr="--dimensionality %d", usedefault=True,),
        environ=dict(nohash=True, usedefault=True,),
        fixed_image=dict(mandatory=True,),
        fixed_image_mask=dict(
            argstr="%s", extensions=None, max_ver="2.1.0", xor=["fixed_image_masks"],
        ),
        fixed_image_masks=dict(min_ver="2.2.0", xor=["fixed_image_mask"],),
        float=dict(argstr="--float %d",),
        initial_moving_transform=dict(
            argstr="%s", xor=["initial_moving_transform_com"],
        ),
        initial_moving_transform_com=dict(
            argstr="%s", xor=["initial_moving_transform"],
        ),
        initialize_transforms_per_stage=dict(
            argstr="--initialize-transforms-per-stage %d", usedefault=True,
        ),
        interpolation=dict(argstr="%s", usedefault=True,),
        interpolation_parameters=dict(),
        invert_initial_moving_transform=dict(
            requires=["initial_moving_transform"], xor=["initial_moving_transform_com"],
        ),
        metric=dict(mandatory=True,),
        metric_item_trait=dict(),
        metric_stage_trait=dict(),
        metric_weight=dict(mandatory=True, requires=["metric"], usedefault=True,),
        metric_weight_item_trait=dict(usedefault=True,),
        metric_weight_stage_trait=dict(),
        moving_image=dict(mandatory=True,),
        moving_image_mask=dict(
            extensions=None,
            max_ver="2.1.0",
            requires=["fixed_image_mask"],
            xor=["moving_image_masks"],
        ),
        moving_image_masks=dict(min_ver="2.2.0", xor=["moving_image_mask"],),
        num_threads=dict(nohash=True, usedefault=True,),
        number_of_iterations=dict(),
        output_inverse_warped_image=dict(
            hash_files=False, requires=["output_warped_image"],
        ),
        output_transform_prefix=dict(argstr="%s", usedefault=True,),
        output_warped_image=dict(hash_files=False,),
        radius_bins_item_trait=dict(usedefault=True,),
        radius_bins_stage_trait=dict(),
        radius_or_number_of_bins=dict(requires=["metric_weight"], usedefault=True,),
        restore_state=dict(argstr="--restore-state %s", extensions=None,),
        restrict_deformation=dict(),
        sampling_percentage=dict(requires=["sampling_strategy"],),
        sampling_percentage_item_trait=dict(),
        sampling_percentage_stage_trait=dict(),
        sampling_strategy=dict(requires=["metric_weight"],),
        sampling_strategy_item_trait=dict(),
        sampling_strategy_stage_trait=dict(),
        save_state=dict(argstr="--save-state %s", extensions=None,),
        shrink_factors=dict(mandatory=True,),
        sigma_units=dict(requires=["smoothing_sigmas"],),
        smoothing_sigmas=dict(mandatory=True,),
        transform_parameters=dict(),
        transforms=dict(argstr="%s", mandatory=True,),
        use_estimate_learning_rate_once=dict(),
        use_histogram_matching=dict(usedefault=True,),
        verbose=dict(argstr="-v", usedefault=True,),
        winsorize_lower_quantile=dict(argstr="%s", usedefault=True,),
        winsorize_upper_quantile=dict(argstr="%s", usedefault=True,),
        write_composite_transform=dict(
            argstr="--write-composite-transform %d", usedefault=True,
        ),
    )
    inputs = Registration.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Registration_outputs():
    output_map = dict(
        composite_transform=dict(extensions=None,),
        elapsed_time=dict(),
        forward_invert_flags=dict(),
        forward_transforms=dict(),
        reverse_forward_invert_flags=dict(),
        reverse_forward_transforms=dict(),
        inverse_composite_transform=dict(extensions=None,),
        inverse_warped_image=dict(extensions=None,),
        metric_value=dict(),
        reverse_invert_flags=dict(),
        reverse_transforms=dict(),
        save_state=dict(extensions=None,),
        warped_image=dict(extensions=None,),
    )
    outputs = Registration.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

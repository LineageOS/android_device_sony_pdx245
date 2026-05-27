#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# Copyright (C) 2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_lib import lib_fixups

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

from extract_utils.fixups_blob import (
    blob_fixups_user_type,
    blob_fixup,
)
from extract_utils.module import lib_fixups_user_type

namespace_imports = [
    'hardware/qcom-caf/sm8650',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/sony/sm8650-common',
]

blob_fixups: blob_fixups_user_type = {
    ('vendor/lib64/libarcsoft_dual_bokeh_adapter.so',
     'vendor/lib64/libarcsoft_hdr_adapter.so',
     'vendor/lib64/libarcsoft_high_dynamic_range_v5.so',
     'vendor/lib64/libarcsoft_low_light_hdr.so',
     'vendor/lib64/libarcsoft_scbokeh_image.so',
     'vendor/lib64/libarcsoft_scbokeh_preview.so',
     'vendor/lib64/libarcsoft_scbokeh_video.so',
     'vendor/lib64/libarcsoft_single_bokeh_adapter.so'): blob_fixup()
    .add_needed(
        'liblog.so',
    )
    .add_needed(
        'libcutils.so',
    ),
    'vendor/lib64/libcammw.so': blob_fixup()
    .replace_needed(
        'android.hardware.light-V1-ndk_platform.so', 'android.hardware.light-V1-ndk.so'
    ),
    'vendor/etc/init/vendor.somc.hardware.camera.provider@1.0-service.rc': blob_fixup()
        .regex_replace('group camera', 'group camera wakelock')
}

module = ExtractUtilsModule(
    'pdx245',
    'sony',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8650-common', module.vendor
    )
    utils.run()

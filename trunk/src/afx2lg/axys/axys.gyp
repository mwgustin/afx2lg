# Copyright (c) 2013 Tomas Gunnarsson. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [{
    'target_name': 'axys',
    'type': 'executable',
    'defines': [
    ],
    'include_dirs': [
      '..',
    ],
    'dependencies': [
      '../axefx/axefx.gyp:*',
      '../common/base.gyp:*',
      '../midi/midi.gyp:*',
      '../juce/juce.gyp:*',
    ],
    'sources': [
      '../common/common_types.h',
      'main.cc',
      'MainWnd.h',
      'MainWnd.cpp',
    ],
    'conditions': [
      ['OS=="win"', {
        'msvs_settings': {
          'VCLinkerTool': {
            # /SUBSYSTEM:WINDOWS
            'SubSystem': '2',
          },
        },
      }],
    ],
  }],
}
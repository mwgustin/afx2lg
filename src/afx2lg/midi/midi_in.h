// Copyright (c) 2012, Tomas Gunnarsson
// All rights reserved.

#pragma once
#ifndef MIDI_MIDI_IN_H_
#define MIDI_MIDI_IN_H_

#include "common_types.h"
#include "midi/midi_out.h"  // for MidiDeviceInfo.

#include <memory>
#include <string>
#include <vector>

namespace midi {

using std::tr1::shared_ptr;
using std::unique_ptr;

// Interface class for a midi-in connection + device enumeration.
class MidiIn {
 public:
  virtual ~MidiIn() {}

  // Create an instance of MidiIn.
  static unique_ptr<MidiIn> Create(const shared_ptr<MidiDeviceInfo>& device);

  // Enumerate all midi output devices.
  static bool EnumerateDevices(DeviceInfos* devices);

  const shared_ptr<MidiDeviceInfo>& device() const { return device_; }

 protected:
  MidiIn(const shared_ptr<MidiDeviceInfo>& device);
  shared_ptr<MidiDeviceInfo> device_;
};

}  // namespace midi

#endif  // MIDI_MIDI_IN_H_

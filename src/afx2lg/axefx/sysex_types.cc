// Copyright (c) 2012, Tomas Gunnarsson
// All rights reserved.

#include "axefx/sysex_types.h"

namespace axefx {

bool IsFractalSysEx(const uint8_t* sys_ex, int size) {
  ASSERT(sys_ex[0] == kSysExStart);
  ASSERT(sys_ex[size - 1] == kSysExEnd);

  if (size < (sizeof(kFractalMidiId) + kSysExTerminationByteCount) ||
      memcmp(&sys_ex[1], &kFractalMidiId[0], sizeof(kFractalMidiId)) != 0) {
    return false;
  }

  return VerifyChecksum(sys_ex, size);
}

uint8_t CalculateChecksum(const uint8_t* sys_ex, int size) {
  uint8_t checksum = 0;
  int i = 0;
  for (; i < size - 2; ++i)
    checksum ^= sys_ex[i];
  checksum &= 0x7F;
  return checksum;
}

// http://wiki.fractalaudio.com/axefx2/index.php?title=MIDI_SysEx
bool VerifyChecksum(const uint8_t* sys_ex, int size) {
  return size >= 3 &&
         sys_ex[0] == kSysExStart &&
         sys_ex[size - 1] == kSysExEnd &&
         sys_ex[size - 2] == CalculateChecksum(sys_ex, size);
}

uint16_t SeptetPair::As16bit() const {
  ASSERT((ms & 0x80) == 0);
  ASSERT((ls & 0x80) == 0);
  return (static_cast<uint16_t>(ls) | (static_cast<uint16_t>(ms) << 7));
}

char SeptetChar::AsChar() const {
  ASSERT((b1 & 0x80) == 0);
  ASSERT(!b2);
  ASSERT(!b3);
  return b1;
}

uint16_t Fractal16bit::As16bit() const {
  uint16_t ret = (b3 & 0x3) << 14;
  ret |= ((b2 & 0x7f) >> 1) << 8;
  ret |= (b2 & 0x1) << 7;
  ret |= (b1 & 0x7F);
  return ret;
}

AxeFxModel FractalSysExHeader::model() const {
  return static_cast<AxeFxModel>(model_id);
}

FunctionId FractalSysExHeader::function() const {
  return static_cast<FunctionId>(function_id);
}

std::string PresetName::ToString() const {
  std::string ret;
  ret.reserve(arraysize(chars));
  int i = 0;
  while (i < arraysize(chars)) {
    char ch = chars[i++].AsChar();
    // Names can be zero terminated before the 23'rd char.
    // E.g. default preset 293, "BandTaps" (len=8).
    if (!ch)
      break;
    ret.push_back(ch);
  }
  std::string::size_type index = ret.find_last_not_of(L' ');
  index == std::string::npos ?
      ret.resize(ret.length()) : ret.resize(index + 1);
  return ret;
}

}  // namespace axefx

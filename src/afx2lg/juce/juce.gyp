# Copyright (c) 2012 Tomas Gunnarsson. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'juce',
      'type': 'static_library',
      'defines': [
      ],
      'include_dirs': [
        '.',
        '..',
        '<(DEPTH)/JUCE',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(DEPTH)/JUCE',
          '<(DEPTH)/JUCE/modules',
        ],
      },
      'sources': [
        "<(DEPTH)/JUCE/modules/juce_audio_basics/buffers/juce_AudioDataConverters.h",
        "<(DEPTH)/JUCE/modules/juce_audio_basics/buffers/juce_AudioSampleBuffer.h",
        "<(DEPTH)/JUCE/modules/juce_audio_basics/effects/juce_Decibels.h",
        "<(DEPTH)/JUCE/modules/juce_audio_basics/effects/juce_IIRFilter.h",
        "<(DEPTH)/JUCE/modules/juce_audio_basics/effects/juce_LagrangeInterpolator.h",
        "<(DEPTH)/JUCE/modules/juce_audio_basics/effects/juce_Reverb.h",
        "<(DEPTH)/JUCE/modules/juce_audio_basics/juce_audio_basics.cpp",
        "<(DEPTH)/JUCE/modules/juce_audio_basics/juce_audio_basics.h",
        "<(DEPTH)/JUCE/modules/juce_audio_basics/midi/juce_MidiBuffer.h",
        "<(DEPTH)/JUCE/modules/juce_audio_basics/midi/juce_MidiFile.h",
        "<(DEPTH)/JUCE/modules/juce_audio_basics/midi/juce_MidiKeyboardState.h",
        "<(DEPTH)/JUCE/modules/juce_audio_basics/midi/juce_MidiMessage.h",
        "<(DEPTH)/JUCE/modules/juce_audio_basics/midi/juce_MidiMessageSequence.h",
        "<(DEPTH)/JUCE/modules/juce_audio_basics/sources/juce_AudioSource.h",
        "<(DEPTH)/JUCE/modules/juce_audio_basics/sources/juce_BufferingAudioSource.h",
        "<(DEPTH)/JUCE/modules/juce_audio_basics/sources/juce_ChannelRemappingAudioSource.h",
        "<(DEPTH)/JUCE/modules/juce_audio_basics/sources/juce_IIRFilterAudioSource.h",
        "<(DEPTH)/JUCE/modules/juce_audio_basics/sources/juce_MixerAudioSource.h",
        "<(DEPTH)/JUCE/modules/juce_audio_basics/sources/juce_PositionableAudioSource.h",
        "<(DEPTH)/JUCE/modules/juce_audio_basics/sources/juce_ResamplingAudioSource.h",
        "<(DEPTH)/JUCE/modules/juce_audio_basics/sources/juce_ReverbAudioSource.h",
        "<(DEPTH)/JUCE/modules/juce_audio_basics/sources/juce_ToneGeneratorAudioSource.h",
        "<(DEPTH)/JUCE/modules/juce_audio_basics/synthesisers/juce_Synthesiser.h",
        "<(DEPTH)/JUCE/modules/juce_audio_devices/audio_cd/juce_AudioCDBurner.h",
        "<(DEPTH)/JUCE/modules/juce_audio_devices/audio_cd/juce_AudioCDReader.h",
        "<(DEPTH)/JUCE/modules/juce_audio_devices/audio_io/juce_AudioDeviceManager.h",
        "<(DEPTH)/JUCE/modules/juce_audio_devices/audio_io/juce_AudioIODevice.h",
        "<(DEPTH)/JUCE/modules/juce_audio_devices/audio_io/juce_AudioIODeviceType.h",
        "<(DEPTH)/JUCE/modules/juce_audio_devices/juce_audio_devices.h",
        "<(DEPTH)/JUCE/modules/juce_audio_devices/midi_io/juce_MidiInput.h",
        "<(DEPTH)/JUCE/modules/juce_audio_devices/midi_io/juce_MidiMessageCollector.h",
        "<(DEPTH)/JUCE/modules/juce_audio_devices/midi_io/juce_MidiOutput.h",
        "<(DEPTH)/JUCE/modules/juce_audio_devices/native/juce_MidiDataConcatenator.h",
        "<(DEPTH)/JUCE/modules/juce_audio_devices/sources/juce_AudioSourcePlayer.h",
        "<(DEPTH)/JUCE/modules/juce_audio_devices/sources/juce_AudioTransportSource.h",
        "<(DEPTH)/JUCE/modules/juce_audio_formats/codecs/juce_AiffAudioFormat.h",
        "<(DEPTH)/JUCE/modules/juce_audio_formats/codecs/juce_CoreAudioFormat.h",
        "<(DEPTH)/JUCE/modules/juce_audio_formats/codecs/juce_FlacAudioFormat.h",
        "<(DEPTH)/JUCE/modules/juce_audio_formats/codecs/juce_LAMEEncoderAudioFormat.h",
        "<(DEPTH)/JUCE/modules/juce_audio_formats/codecs/juce_MP3AudioFormat.h",
        "<(DEPTH)/JUCE/modules/juce_audio_formats/codecs/juce_OggVorbisAudioFormat.h",
        "<(DEPTH)/JUCE/modules/juce_audio_formats/codecs/juce_QuickTimeAudioFormat.h",
        "<(DEPTH)/JUCE/modules/juce_audio_formats/codecs/juce_WavAudioFormat.h",
        "<(DEPTH)/JUCE/modules/juce_audio_formats/codecs/juce_WindowsMediaAudioFormat.h",
        "<(DEPTH)/JUCE/modules/juce_audio_formats/format/juce_AudioFormat.h",
        "<(DEPTH)/JUCE/modules/juce_audio_formats/format/juce_AudioFormatManager.h",
        "<(DEPTH)/JUCE/modules/juce_audio_formats/format/juce_AudioFormatReader.h",
        "<(DEPTH)/JUCE/modules/juce_audio_formats/format/juce_AudioFormatReaderSource.h",
        "<(DEPTH)/JUCE/modules/juce_audio_formats/format/juce_AudioFormatWriter.h",
        "<(DEPTH)/JUCE/modules/juce_audio_formats/format/juce_AudioSubsectionReader.h",
        "<(DEPTH)/JUCE/modules/juce_audio_formats/format/juce_MemoryMappedAudioFormatReader.h",
        "<(DEPTH)/JUCE/modules/juce_audio_formats/juce_audio_formats.h",
        "<(DEPTH)/JUCE/modules/juce_audio_formats/sampler/juce_Sampler.h",
        "<(DEPTH)/JUCE/modules/juce_audio_processors/format/juce_AudioPluginFormat.h",
        "<(DEPTH)/JUCE/modules/juce_audio_processors/format/juce_AudioPluginFormatManager.h",
        "<(DEPTH)/JUCE/modules/juce_audio_processors/format_types/juce_AudioUnitPluginFormat.h",
        "<(DEPTH)/JUCE/modules/juce_audio_processors/format_types/juce_DirectXPluginFormat.h",
        "<(DEPTH)/JUCE/modules/juce_audio_processors/format_types/juce_LADSPAPluginFormat.h",
        "<(DEPTH)/JUCE/modules/juce_audio_processors/format_types/juce_VSTMidiEventList.h",
        "<(DEPTH)/JUCE/modules/juce_audio_processors/format_types/juce_VSTPluginFormat.h",
        "<(DEPTH)/JUCE/modules/juce_audio_processors/juce_audio_processors.h",
        "<(DEPTH)/JUCE/modules/juce_audio_processors/processors/juce_AudioPlayHead.h",
        "<(DEPTH)/JUCE/modules/juce_audio_processors/processors/juce_AudioPluginInstance.h",
        "<(DEPTH)/JUCE/modules/juce_audio_processors/processors/juce_AudioProcessor.h",
        "<(DEPTH)/JUCE/modules/juce_audio_processors/processors/juce_AudioProcessorEditor.h",
        "<(DEPTH)/JUCE/modules/juce_audio_processors/processors/juce_AudioProcessorGraph.h",
        "<(DEPTH)/JUCE/modules/juce_audio_processors/processors/juce_AudioProcessorListener.h",
        "<(DEPTH)/JUCE/modules/juce_audio_processors/processors/juce_GenericAudioProcessorEditor.h",
        "<(DEPTH)/JUCE/modules/juce_audio_processors/processors/juce_PluginDescription.h",
        "<(DEPTH)/JUCE/modules/juce_audio_processors/scanning/juce_KnownPluginList.h",
        "<(DEPTH)/JUCE/modules/juce_audio_processors/scanning/juce_PluginDirectoryScanner.h",
        "<(DEPTH)/JUCE/modules/juce_audio_processors/scanning/juce_PluginListComponent.h",
        "<(DEPTH)/JUCE/modules/juce_audio_utils/gui/juce_AudioDeviceSelectorComponent.h",
        "<(DEPTH)/JUCE/modules/juce_audio_utils/gui/juce_AudioThumbnail.h",
        "<(DEPTH)/JUCE/modules/juce_audio_utils/gui/juce_AudioThumbnailBase.h",
        "<(DEPTH)/JUCE/modules/juce_audio_utils/gui/juce_AudioThumbnailCache.h",
        "<(DEPTH)/JUCE/modules/juce_audio_utils/gui/juce_MidiKeyboardComponent.h",
        "<(DEPTH)/JUCE/modules/juce_audio_utils/juce_audio_utils.h",
        "<(DEPTH)/JUCE/modules/juce_audio_utils/players/juce_AudioProcessorPlayer.h",
        "<(DEPTH)/JUCE/modules/juce_core/containers/juce_AbstractFifo.h",
        "<(DEPTH)/JUCE/modules/juce_core/containers/juce_Array.h",
        "<(DEPTH)/JUCE/modules/juce_core/containers/juce_ArrayAllocationBase.h",
        "<(DEPTH)/JUCE/modules/juce_core/containers/juce_DynamicObject.h",
        "<(DEPTH)/JUCE/modules/juce_core/containers/juce_ElementComparator.h",
        "<(DEPTH)/JUCE/modules/juce_core/containers/juce_HashMap.h",
        "<(DEPTH)/JUCE/modules/juce_core/containers/juce_LinkedListPointer.h",
        "<(DEPTH)/JUCE/modules/juce_core/containers/juce_NamedValueSet.h",
        "<(DEPTH)/JUCE/modules/juce_core/containers/juce_OwnedArray.h",
        "<(DEPTH)/JUCE/modules/juce_core/containers/juce_PropertySet.h",
        "<(DEPTH)/JUCE/modules/juce_core/containers/juce_ReferenceCountedArray.h",
        "<(DEPTH)/JUCE/modules/juce_core/containers/juce_ScopedValueSetter.h",
        "<(DEPTH)/JUCE/modules/juce_core/containers/juce_SortedSet.h",
        "<(DEPTH)/JUCE/modules/juce_core/containers/juce_SparseSet.h",
        "<(DEPTH)/JUCE/modules/juce_core/containers/juce_Variant.h",
        "<(DEPTH)/JUCE/modules/juce_core/files/juce_DirectoryIterator.h",
        "<(DEPTH)/JUCE/modules/juce_core/files/juce_File.h",
        "<(DEPTH)/JUCE/modules/juce_core/files/juce_FileInputStream.h",
        "<(DEPTH)/JUCE/modules/juce_core/files/juce_FileOutputStream.h",
        "<(DEPTH)/JUCE/modules/juce_core/files/juce_FileSearchPath.h",
        "<(DEPTH)/JUCE/modules/juce_core/files/juce_MemoryMappedFile.h",
        "<(DEPTH)/JUCE/modules/juce_core/files/juce_TemporaryFile.h",
        "<(DEPTH)/JUCE/modules/juce_core/json/juce_JSON.h",
        "<(DEPTH)/JUCE/modules/juce_core/juce_core.h",
        "<(DEPTH)/JUCE/modules/juce_core/logging/juce_FileLogger.h",
        "<(DEPTH)/JUCE/modules/juce_core/logging/juce_Logger.h",
        "<(DEPTH)/JUCE/modules/juce_core/maths/juce_BigInteger.h",
        "<(DEPTH)/JUCE/modules/juce_core/maths/juce_Expression.h",
        "<(DEPTH)/JUCE/modules/juce_core/maths/juce_MathsFunctions.h",
        "<(DEPTH)/JUCE/modules/juce_core/maths/juce_Random.h",
        "<(DEPTH)/JUCE/modules/juce_core/maths/juce_Range.h",
        "<(DEPTH)/JUCE/modules/juce_core/memory/juce_Atomic.h",
        "<(DEPTH)/JUCE/modules/juce_core/memory/juce_ByteOrder.h",
        "<(DEPTH)/JUCE/modules/juce_core/memory/juce_HeapBlock.h",
        "<(DEPTH)/JUCE/modules/juce_core/memory/juce_LeakedObjectDetector.h",
        "<(DEPTH)/JUCE/modules/juce_core/memory/juce_Memory.h",
        "<(DEPTH)/JUCE/modules/juce_core/memory/juce_MemoryBlock.h",
        "<(DEPTH)/JUCE/modules/juce_core/memory/juce_OptionalScopedPointer.h",
        "<(DEPTH)/JUCE/modules/juce_core/memory/juce_ReferenceCountedObject.h",
        "<(DEPTH)/JUCE/modules/juce_core/memory/juce_ScopedPointer.h",
        "<(DEPTH)/JUCE/modules/juce_core/memory/juce_Singleton.h",
        "<(DEPTH)/JUCE/modules/juce_core/memory/juce_WeakReference.h",
        "<(DEPTH)/JUCE/modules/juce_core/misc/juce_Result.h",
        "<(DEPTH)/JUCE/modules/juce_core/misc/juce_Uuid.h",
        "<(DEPTH)/JUCE/modules/juce_core/misc/juce_WindowsRegistry.h",
        "<(DEPTH)/JUCE/modules/juce_core/native/juce_android_JNIHelpers.h",
        "<(DEPTH)/JUCE/modules/juce_core/native/juce_BasicNativeHeaders.h",
        "<(DEPTH)/JUCE/modules/juce_core/native/juce_osx_ObjCHelpers.h",
        "<(DEPTH)/JUCE/modules/juce_core/native/juce_posix_SharedCode.h",
        "<(DEPTH)/JUCE/modules/juce_core/native/juce_win32_ComSmartPtr.h",
        "<(DEPTH)/JUCE/modules/juce_core/network/juce_MACAddress.h",
        "<(DEPTH)/JUCE/modules/juce_core/network/juce_NamedPipe.h",
        "<(DEPTH)/JUCE/modules/juce_core/network/juce_Socket.h",
        "<(DEPTH)/JUCE/modules/juce_core/network/juce_URL.h",
        "<(DEPTH)/JUCE/modules/juce_core/streams/juce_BufferedInputStream.h",
        "<(DEPTH)/JUCE/modules/juce_core/streams/juce_FileInputSource.h",
        "<(DEPTH)/JUCE/modules/juce_core/streams/juce_InputSource.h",
        "<(DEPTH)/JUCE/modules/juce_core/streams/juce_InputStream.h",
        "<(DEPTH)/JUCE/modules/juce_core/streams/juce_MemoryInputStream.h",
        "<(DEPTH)/JUCE/modules/juce_core/streams/juce_MemoryOutputStream.h",
        "<(DEPTH)/JUCE/modules/juce_core/streams/juce_OutputStream.h",
        "<(DEPTH)/JUCE/modules/juce_core/streams/juce_SubregionStream.h",
        "<(DEPTH)/JUCE/modules/juce_core/system/juce_PlatformDefs.h",
        "<(DEPTH)/JUCE/modules/juce_core/system/juce_StandardHeader.h",
        "<(DEPTH)/JUCE/modules/juce_core/system/juce_SystemStats.h",
        "<(DEPTH)/JUCE/modules/juce_core/system/juce_TargetPlatform.h",
        "<(DEPTH)/JUCE/modules/juce_core/text/juce_CharacterFunctions.h",
        "<(DEPTH)/JUCE/modules/juce_core/text/juce_CharPointer_ASCII.h",
        "<(DEPTH)/JUCE/modules/juce_core/text/juce_CharPointer_UTF16.h",
        "<(DEPTH)/JUCE/modules/juce_core/text/juce_CharPointer_UTF32.h",
        "<(DEPTH)/JUCE/modules/juce_core/text/juce_CharPointer_UTF8.h",
        "<(DEPTH)/JUCE/modules/juce_core/text/juce_Identifier.h",
        "<(DEPTH)/JUCE/modules/juce_core/text/juce_LocalisedStrings.h",
        "<(DEPTH)/JUCE/modules/juce_core/text/juce_NewLine.h",
        "<(DEPTH)/JUCE/modules/juce_core/text/juce_String.h",
        "<(DEPTH)/JUCE/modules/juce_core/text/juce_StringArray.h",
        "<(DEPTH)/JUCE/modules/juce_core/text/juce_StringPairArray.h",
        "<(DEPTH)/JUCE/modules/juce_core/text/juce_StringPool.h",
        "<(DEPTH)/JUCE/modules/juce_core/text/juce_TextDiff.h",
        "<(DEPTH)/JUCE/modules/juce_core/threads/juce_ChildProcess.h",
        "<(DEPTH)/JUCE/modules/juce_core/threads/juce_CriticalSection.h",
        "<(DEPTH)/JUCE/modules/juce_core/threads/juce_DynamicLibrary.h",
        "<(DEPTH)/JUCE/modules/juce_core/threads/juce_HighResolutionTimer.h",
        "<(DEPTH)/JUCE/modules/juce_core/threads/juce_InterProcessLock.h",
        "<(DEPTH)/JUCE/modules/juce_core/threads/juce_Process.h",
        "<(DEPTH)/JUCE/modules/juce_core/threads/juce_ReadWriteLock.h",
        "<(DEPTH)/JUCE/modules/juce_core/threads/juce_ScopedLock.h",
        "<(DEPTH)/JUCE/modules/juce_core/threads/juce_ScopedReadLock.h",
        "<(DEPTH)/JUCE/modules/juce_core/threads/juce_ScopedWriteLock.h",
        "<(DEPTH)/JUCE/modules/juce_core/threads/juce_SpinLock.h",
        "<(DEPTH)/JUCE/modules/juce_core/threads/juce_Thread.h",
        "<(DEPTH)/JUCE/modules/juce_core/threads/juce_ThreadLocalValue.h",
        "<(DEPTH)/JUCE/modules/juce_core/threads/juce_ThreadPool.h",
        "<(DEPTH)/JUCE/modules/juce_core/threads/juce_TimeSliceThread.h",
        "<(DEPTH)/JUCE/modules/juce_core/threads/juce_WaitableEvent.h",
        "<(DEPTH)/JUCE/modules/juce_core/time/juce_PerformanceCounter.h",
        "<(DEPTH)/JUCE/modules/juce_core/time/juce_RelativeTime.h",
        "<(DEPTH)/JUCE/modules/juce_core/time/juce_Time.h",
        "<(DEPTH)/JUCE/modules/juce_core/unit_tests/juce_UnitTest.h",
        "<(DEPTH)/JUCE/modules/juce_core/xml/juce_XmlDocument.h",
        "<(DEPTH)/JUCE/modules/juce_core/xml/juce_XmlElement.h",
        "<(DEPTH)/JUCE/modules/juce_core/zip/juce_GZIPCompressorOutputStream.h",
        "<(DEPTH)/JUCE/modules/juce_core/zip/juce_GZIPDecompressorInputStream.h",
        "<(DEPTH)/JUCE/modules/juce_core/zip/juce_ZipFile.h",
        "<(DEPTH)/JUCE/modules/juce_cryptography/encryption/juce_BlowFish.h",
        "<(DEPTH)/JUCE/modules/juce_cryptography/encryption/juce_Primes.h",
        "<(DEPTH)/JUCE/modules/juce_cryptography/encryption/juce_RSAKey.h",
        "<(DEPTH)/JUCE/modules/juce_cryptography/hashing/juce_MD5.h",
        "<(DEPTH)/JUCE/modules/juce_cryptography/hashing/juce_SHA256.h",
        "<(DEPTH)/JUCE/modules/juce_cryptography/juce_cryptography.cpp",
        "<(DEPTH)/JUCE/modules/juce_cryptography/juce_cryptography.h",
        "<(DEPTH)/JUCE/modules/juce_data_structures/app_properties/juce_ApplicationProperties.h",
        "<(DEPTH)/JUCE/modules/juce_data_structures/app_properties/juce_PropertiesFile.h",
        "<(DEPTH)/JUCE/modules/juce_data_structures/juce_data_structures.cpp",
        "<(DEPTH)/JUCE/modules/juce_data_structures/juce_data_structures.h",
        "<(DEPTH)/JUCE/modules/juce_data_structures/undomanager/juce_UndoableAction.h",
        "<(DEPTH)/JUCE/modules/juce_data_structures/undomanager/juce_UndoManager.h",
        "<(DEPTH)/JUCE/modules/juce_data_structures/values/juce_Value.h",
        "<(DEPTH)/JUCE/modules/juce_data_structures/values/juce_ValueTree.h",
        "<(DEPTH)/JUCE/modules/juce_events/broadcasters/juce_ActionBroadcaster.h",
        "<(DEPTH)/JUCE/modules/juce_events/broadcasters/juce_ActionListener.h",
        "<(DEPTH)/JUCE/modules/juce_events/broadcasters/juce_AsyncUpdater.h",
        "<(DEPTH)/JUCE/modules/juce_events/broadcasters/juce_ChangeBroadcaster.h",
        "<(DEPTH)/JUCE/modules/juce_events/broadcasters/juce_ChangeListener.h",
        "<(DEPTH)/JUCE/modules/juce_events/broadcasters/juce_ListenerList.h",
        "<(DEPTH)/JUCE/modules/juce_events/interprocess/juce_InterprocessConnection.h",
        "<(DEPTH)/JUCE/modules/juce_events/interprocess/juce_InterprocessConnectionServer.h",
        "<(DEPTH)/JUCE/modules/juce_events/juce_events.h",
        "<(DEPTH)/JUCE/modules/juce_events/messages/juce_ApplicationBase.h",
        "<(DEPTH)/JUCE/modules/juce_events/messages/juce_CallbackMessage.h",
        "<(DEPTH)/JUCE/modules/juce_events/messages/juce_DeletedAtShutdown.h",
        "<(DEPTH)/JUCE/modules/juce_events/messages/juce_Message.h",
        "<(DEPTH)/JUCE/modules/juce_events/messages/juce_MessageListener.h",
        "<(DEPTH)/JUCE/modules/juce_events/messages/juce_MessageManager.h",
        "<(DEPTH)/JUCE/modules/juce_events/messages/juce_NotificationType.h",
        "<(DEPTH)/JUCE/modules/juce_events/native/juce_osx_MessageQueue.h",
        "<(DEPTH)/JUCE/modules/juce_events/native/juce_ScopedXLock.h",
        "<(DEPTH)/JUCE/modules/juce_events/native/juce_win32_HiddenMessageWindow.h",
        "<(DEPTH)/JUCE/modules/juce_events/timers/juce_MultiTimer.h",
        "<(DEPTH)/JUCE/modules/juce_events/timers/juce_Timer.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/colour/juce_Colour.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/colour/juce_ColourGradient.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/colour/juce_Colours.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/colour/juce_FillType.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/colour/juce_PixelFormats.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/contexts/juce_GraphicsContext.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/contexts/juce_LowLevelGraphicsContext.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/contexts/juce_LowLevelGraphicsPostScriptRenderer.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/contexts/juce_LowLevelGraphicsSoftwareRenderer.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/effects/juce_DropShadowEffect.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/effects/juce_GlowEffect.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/effects/juce_ImageEffectFilter.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/fonts/juce_AttributedString.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/fonts/juce_CustomTypeface.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/fonts/juce_Font.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/fonts/juce_GlyphArrangement.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/fonts/juce_TextLayout.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/fonts/juce_Typeface.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/geometry/juce_AffineTransform.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/geometry/juce_BorderSize.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/geometry/juce_EdgeTable.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/geometry/juce_Line.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/geometry/juce_Path.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/geometry/juce_PathIterator.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/geometry/juce_PathStrokeType.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/geometry/juce_Point.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/geometry/juce_Rectangle.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/geometry/juce_RectangleList.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/images/juce_Image.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/images/juce_ImageCache.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/images/juce_ImageConvolutionKernel.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/images/juce_ImageFileFormat.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/juce_graphics.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/native/juce_mac_CoreGraphicsContext.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/native/juce_mac_CoreGraphicsHelpers.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/native/juce_RenderingHelpers.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/placement/juce_Justification.h",
        "<(DEPTH)/JUCE/modules/juce_graphics/placement/juce_RectanglePlacement.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/application/juce_Application.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/application/juce_Initialisation.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/buttons/juce_ArrowButton.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/buttons/juce_Button.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/buttons/juce_DrawableButton.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/buttons/juce_HyperlinkButton.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/buttons/juce_ImageButton.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/buttons/juce_ShapeButton.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/buttons/juce_TextButton.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/buttons/juce_ToggleButton.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/buttons/juce_ToolbarButton.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/commands/juce_ApplicationCommandID.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/commands/juce_ApplicationCommandInfo.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/commands/juce_ApplicationCommandManager.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/commands/juce_ApplicationCommandTarget.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/commands/juce_KeyPressMappingSet.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/components/juce_CachedComponentImage.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/components/juce_Component.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/components/juce_ComponentListener.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/components/juce_Desktop.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/components/juce_ModalComponentManager.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/drawables/juce_Drawable.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/drawables/juce_DrawableComposite.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/drawables/juce_DrawableImage.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/drawables/juce_DrawablePath.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/drawables/juce_DrawableRectangle.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/drawables/juce_DrawableShape.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/drawables/juce_DrawableText.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/filebrowser/juce_DirectoryContentsDisplayComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/filebrowser/juce_DirectoryContentsList.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/filebrowser/juce_FileBrowserComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/filebrowser/juce_FileBrowserListener.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/filebrowser/juce_FileChooser.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/filebrowser/juce_FileChooserDialogBox.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/filebrowser/juce_FileFilter.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/filebrowser/juce_FileListComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/filebrowser/juce_FilenameComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/filebrowser/juce_FilePreviewComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/filebrowser/juce_FileSearchPathListComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/filebrowser/juce_FileTreeComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/filebrowser/juce_ImagePreviewComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/filebrowser/juce_WildcardFileFilter.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/juce_gui_basics.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/keyboard/juce_CaretComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/keyboard/juce_KeyboardFocusTraverser.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/keyboard/juce_KeyListener.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/keyboard/juce_KeyPress.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/keyboard/juce_ModifierKeys.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/keyboard/juce_SystemClipboard.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/keyboard/juce_TextEditorKeyMapper.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/keyboard/juce_TextInputTarget.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/layout/juce_ComponentAnimator.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/layout/juce_ComponentBoundsConstrainer.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/layout/juce_ComponentBuilder.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/layout/juce_ComponentMovementWatcher.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/layout/juce_ConcertinaPanel.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/layout/juce_GroupComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/layout/juce_MultiDocumentPanel.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/layout/juce_ResizableBorderComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/layout/juce_ResizableCornerComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/layout/juce_ResizableEdgeComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/layout/juce_ScrollBar.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/layout/juce_StretchableLayoutManager.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/layout/juce_StretchableLayoutResizerBar.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/layout/juce_StretchableObjectResizer.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/layout/juce_TabbedButtonBar.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/layout/juce_TabbedComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/layout/juce_Viewport.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/lookandfeel/juce_LookAndFeel.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/menus/juce_MenuBarComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/menus/juce_MenuBarModel.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/menus/juce_PopupMenu.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/misc/juce_BubbleComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/misc/juce_DropShadower.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/mouse/juce_ComponentDragger.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/mouse/juce_DragAndDropContainer.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/mouse/juce_DragAndDropTarget.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/mouse/juce_FileDragAndDropTarget.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/mouse/juce_LassoComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/mouse/juce_MouseCursor.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/mouse/juce_MouseEvent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/mouse/juce_MouseInputSource.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/mouse/juce_MouseListener.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/mouse/juce_SelectedItemSet.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/mouse/juce_TextDragAndDropTarget.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/mouse/juce_TooltipClient.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/native/juce_MultiTouchMapper.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/positioning/juce_MarkerList.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/positioning/juce_RelativeCoordinate.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/positioning/juce_RelativeCoordinatePositioner.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/positioning/juce_RelativeParallelogram.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/positioning/juce_RelativePoint.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/positioning/juce_RelativePointPath.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/positioning/juce_RelativeRectangle.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/properties/juce_BooleanPropertyComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/properties/juce_ButtonPropertyComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/properties/juce_ChoicePropertyComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/properties/juce_PropertyComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/properties/juce_PropertyPanel.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/properties/juce_SliderPropertyComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/properties/juce_TextPropertyComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/widgets/juce_ComboBox.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/widgets/juce_ImageComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/widgets/juce_Label.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/widgets/juce_ListBox.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/widgets/juce_ProgressBar.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/widgets/juce_Slider.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/widgets/juce_TableHeaderComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/widgets/juce_TableListBox.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/widgets/juce_TextEditor.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/widgets/juce_Toolbar.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/widgets/juce_ToolbarItemComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/widgets/juce_ToolbarItemFactory.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/widgets/juce_ToolbarItemPalette.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/widgets/juce_TreeView.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/windows/juce_AlertWindow.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/windows/juce_CallOutBox.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/windows/juce_ComponentPeer.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/windows/juce_DialogWindow.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/windows/juce_DocumentWindow.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/windows/juce_NativeMessageBox.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/windows/juce_ResizableWindow.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/windows/juce_ThreadWithProgressWindow.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/windows/juce_TooltipWindow.h",
        "<(DEPTH)/JUCE/modules/juce_gui_basics/windows/juce_TopLevelWindow.h",
        "<(DEPTH)/JUCE/modules/juce_gui_extra/code_editor/juce_CodeDocument.h",
        "<(DEPTH)/JUCE/modules/juce_gui_extra/code_editor/juce_CodeEditorComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_extra/code_editor/juce_CodeTokeniser.h",
        "<(DEPTH)/JUCE/modules/juce_gui_extra/code_editor/juce_CPlusPlusCodeTokeniser.h",
        "<(DEPTH)/JUCE/modules/juce_gui_extra/code_editor/juce_CPlusPlusCodeTokeniserFunctions.h",
        "<(DEPTH)/JUCE/modules/juce_gui_extra/documents/juce_FileBasedDocument.h",
        "<(DEPTH)/JUCE/modules/juce_gui_extra/embedding/juce_ActiveXControlComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_extra/embedding/juce_NSViewComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_extra/embedding/juce_UIViewComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_extra/juce_gui_extra.h",
        "<(DEPTH)/JUCE/modules/juce_gui_extra/lookandfeel/juce_OldSchoolLookAndFeel.h",
        "<(DEPTH)/JUCE/modules/juce_gui_extra/misc/juce_AppleRemote.h",
        "<(DEPTH)/JUCE/modules/juce_gui_extra/misc/juce_BubbleMessageComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_extra/misc/juce_ColourSelector.h",
        "<(DEPTH)/JUCE/modules/juce_gui_extra/misc/juce_KeyMappingEditorComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_extra/misc/juce_PreferencesPanel.h",
        "<(DEPTH)/JUCE/modules/juce_gui_extra/misc/juce_RecentlyOpenedFilesList.h",
        "<(DEPTH)/JUCE/modules/juce_gui_extra/misc/juce_SplashScreen.h",
        "<(DEPTH)/JUCE/modules/juce_gui_extra/misc/juce_SystemTrayIconComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_extra/misc/juce_WebBrowserComponent.h",
        "<(DEPTH)/JUCE/modules/juce_gui_extra/native/juce_mac_CarbonViewWrapperComponent.h",
        "<(DEPTH)/JUCE/modules/juce_opengl/juce_opengl.h",
        "<(DEPTH)/JUCE/modules/juce_opengl/native/juce_MissingGLDefinitions.h",
        "<(DEPTH)/JUCE/modules/juce_opengl/native/juce_OpenGL_android.h",
        "<(DEPTH)/JUCE/modules/juce_opengl/native/juce_OpenGL_ios.h",
        "<(DEPTH)/JUCE/modules/juce_opengl/native/juce_OpenGL_linux.h",
        "<(DEPTH)/JUCE/modules/juce_opengl/native/juce_OpenGL_osx.h",
        "<(DEPTH)/JUCE/modules/juce_opengl/native/juce_OpenGL_win32.h",
        "<(DEPTH)/JUCE/modules/juce_opengl/native/juce_OpenGLExtensions.h",
        "<(DEPTH)/JUCE/modules/juce_opengl/opengl/juce_Draggable3DOrientation.h",
        "<(DEPTH)/JUCE/modules/juce_opengl/opengl/juce_Matrix3D.h",
        "<(DEPTH)/JUCE/modules/juce_opengl/opengl/juce_OpenGLContext.h",
        "<(DEPTH)/JUCE/modules/juce_opengl/opengl/juce_OpenGLFrameBuffer.h",
        "<(DEPTH)/JUCE/modules/juce_opengl/opengl/juce_OpenGLGraphicsContext.h",
        "<(DEPTH)/JUCE/modules/juce_opengl/opengl/juce_OpenGLHelpers.h",
        "<(DEPTH)/JUCE/modules/juce_opengl/opengl/juce_OpenGLImage.h",
        "<(DEPTH)/JUCE/modules/juce_opengl/opengl/juce_OpenGLPixelFormat.h",
        "<(DEPTH)/JUCE/modules/juce_opengl/opengl/juce_OpenGLRenderer.h",
        "<(DEPTH)/JUCE/modules/juce_opengl/opengl/juce_OpenGLShaderProgram.h",
        "<(DEPTH)/JUCE/modules/juce_opengl/opengl/juce_OpenGLTexture.h",
        "<(DEPTH)/JUCE/modules/juce_opengl/opengl/juce_Quaternion.h",
        "<(DEPTH)/JUCE/modules/juce_opengl/opengl/juce_Vector3D.h",
        "<(DEPTH)/JUCE/modules/juce_video/capture/juce_CameraDevice.h",
        "<(DEPTH)/JUCE/modules/juce_video/juce_video.h",
        "<(DEPTH)/JUCE/modules/juce_video/playback/juce_DirectShowComponent.h",
        "<(DEPTH)/JUCE/modules/juce_video/playback/juce_QuickTimeMovieComponent.h",
        "AppConfig.h",
        "JuceHeader.h",
      ],
      'conditions': [
        # JUCE requires RTTI :-/ so we have to override common.gypi.
        # There are also plenty of warnings we hit when compiling Juce so
        # we'll have to disable warnings-as-errors here. :-(
        # The JUCE coding style prevents use of things like 'override'
        # ('virtual' isn't used when overriding virtual methods) so we
        # can't use that either.
        ['OS=="win"', {
          'msvs_settings': {
            'VCCLCompilerTool': {
              'WarnAsError': 'false',
              'RuntimeTypeInfo': 'true',
            },
          },
          'direct_dependent_settings': {
            'msvs_settings': {
              'VCCLCompilerTool': {
                'WarnAsError': 'false',
                'RuntimeTypeInfo': 'true',
              },
              'VCLinkerTool': {
                'AdditionalDependencies': [
                  'advapi32.lib',
                  'comdlg32.lib',
                  'delayimp.lib',
                  'gdi32.lib',
                  'kernel32.lib',
                  'ole32.lib',
                  'oleaut32.lib',
                  'shell32.lib',
                  'user32.lib',
                  'uuid.lib',
                ],
              },
            },
          },
        }],

        ['OS=="mac"', {
          'xcode_settings': {
            'CLANG_ENABLE_OBJC_ARC': 'NO',
            'GCC_ENABLE_CPP_RTTI': 'YES',
            'GCC_TREAT_WARNINGS_AS_ERRORS': 'NO',    # -Werror
          },
          'direct_dependent_settings': {
            'xcode_settings': {
              'CLANG_ENABLE_OBJC_ARC': 'NO',
              'GCC_ENABLE_CPP_RTTI': 'YES',
              'GCC_TREAT_WARNINGS_AS_ERRORS': 'NO',    # -Werror
            },
          },
          'sources': [
            "<(DEPTH)/JUCE/modules/juce_audio_devices/juce_audio_devices.mm",
            "<(DEPTH)/JUCE/modules/juce_audio_formats/juce_audio_formats.mm",
            "<(DEPTH)/JUCE/modules/juce_audio_processors/juce_audio_processors.mm",
            "<(DEPTH)/JUCE/modules/juce_audio_utils/juce_audio_utils.mm",
            "<(DEPTH)/JUCE/modules/juce_core/juce_core.mm",
            "<(DEPTH)/JUCE/modules/juce_events/juce_events.mm",
            "<(DEPTH)/JUCE/modules/juce_graphics/juce_graphics.mm",
            "<(DEPTH)/JUCE/modules/juce_gui_basics/juce_gui_basics.mm",
            "<(DEPTH)/JUCE/modules/juce_gui_extra/juce_gui_extra.mm",
            "<(DEPTH)/JUCE/modules/juce_opengl/juce_opengl.mm",
            "<(DEPTH)/JUCE/modules/juce_video/juce_video.mm",
          ],
        }, {
          'sources': [
            "<(DEPTH)/JUCE/modules/juce_audio_devices/juce_audio_devices.cpp",
            "<(DEPTH)/JUCE/modules/juce_audio_formats/juce_audio_formats.cpp",
            "<(DEPTH)/JUCE/modules/juce_audio_processors/juce_audio_processors.cpp",
            "<(DEPTH)/JUCE/modules/juce_audio_utils/juce_audio_utils.cpp",
            "<(DEPTH)/JUCE/modules/juce_core/juce_core.cpp",
            "<(DEPTH)/JUCE/modules/juce_events/juce_events.cpp",
            "<(DEPTH)/JUCE/modules/juce_graphics/juce_graphics.cpp",
            "<(DEPTH)/JUCE/modules/juce_gui_basics/juce_gui_basics.cpp",
            "<(DEPTH)/JUCE/modules/juce_gui_extra/juce_gui_extra.cpp",
            "<(DEPTH)/JUCE/modules/juce_opengl/juce_opengl.cpp",
            "<(DEPTH)/JUCE/modules/juce_video/juce_video.cpp",
          ]
        }],

        ['OS=="linux"', {
          'cflags_cc!': [
            '-fno-rtti',
          ],
          'direct_dependent_settings': {
            'cflags_cc!': [
              '-fno-rtti',
            ],
          },
        }],
      ],
    },
  ],
}


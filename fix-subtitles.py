#!/usr/bin/env python3
"""
Script to proportionally scale SRT subtitle timings to match actual audio duration.

The SRT file was created with timings extending to 158 seconds (2:38),
but the actual audio is only 122 seconds (2:02). This script scales all
timings proportionally.
"""

import re
import sys

def parse_time(time_str):
    """Convert SRT time format to seconds."""
    match = re.match(r'(\d+):(\d+):(\d+),(\d+)', time_str)
    if not match:
        return 0
    hours, minutes, seconds, milliseconds = map(int, match.groups())
    return hours * 3600 + minutes * 60 + seconds + milliseconds / 1000

def format_time(seconds):
    """Convert seconds to SRT time format."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

def scale_srt(input_file, output_file, scale_factor):
    """Scale all timings in an SRT file by a given factor."""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match SRT time ranges
    time_pattern = r'(\d+:\d+:\d+,\d+) --> (\d+:\d+:\d+,\d+)'

    def scale_times(match):
        start_time = parse_time(match.group(1))
        end_time = parse_time(match.group(2))

        # Scale the times
        new_start = start_time * scale_factor
        new_end = end_time * scale_factor

        return f"{format_time(new_start)} --> {format_time(new_end)}"

    # Replace all time codes with scaled versions
    scaled_content = re.sub(time_pattern, scale_times, content)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(scaled_content)

    print(f"✅ Scaled subtitles written to: {output_file}")
    print(f"   Scale factor: {scale_factor:.3f}")

if __name__ == "__main__":
    # Audio duration: 122.25 seconds
    # Current SRT duration: 158 seconds (2:38)
    # Scale factor: 122.25 / 158 = 0.774

    AUDIO_DURATION = 122.25
    SRT_DURATION = 158.0
    SCALE_FACTOR = AUDIO_DURATION / SRT_DURATION

    input_file = "assets/TRWBP_SpokenWord.srt"
    output_file = "assets/TRWBP_SpokenWord_scaled.srt"

    print("=== SRT Subtitle Timing Scaler ===")
    print(f"Audio duration: {AUDIO_DURATION:.2f}s ({AUDIO_DURATION//60:.0f}:{AUDIO_DURATION%60:05.2f})")
    print(f"SRT duration: {SRT_DURATION:.2f}s ({SRT_DURATION//60:.0f}:{SRT_DURATION%60:05.2f})")
    print(f"Scale factor: {SCALE_FACTOR:.3f}")
    print()

    scale_srt(input_file, output_file, SCALE_FACTOR)
    print()
    print("Next steps:")
    print("1. Review the scaled subtitles by opening the video with the new SRT file")
    print("2. If timing looks good, run: mv assets/TRWBP_SpokenWord_scaled.srt assets/TRWBP_SpokenWord.srt")
    print("3. Regenerate the video: ./convert-audio.sh")

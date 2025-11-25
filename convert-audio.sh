#!/bin/bash

# Script to convert TRWBP_SpokenWord.m4a to MP3 and create video with subtitles

INPUT_M4A="assets/TRWBP_SpokenWord.m4a"
OUTPUT_MP3="assets/TRWBP_SpokenWord.mp3"
OUTPUT_VIDEO="assets/TRWBP_SpokenWord.mp4"
SUBTITLES="assets/TRWBP_SpokenWord.srt"
LOGO_IMAGE="assets/trwbp_logo.png"

echo "=== TRWBP Audio Conversion Script ==="
echo ""

# Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️  ffmpeg is not installed."
    echo ""
    echo "To install ffmpeg on macOS:"
    echo "  brew install ffmpeg"
    echo ""
    echo "Or download from: https://ffmpeg.org/download.html"
    echo ""
    exit 1
fi

# Convert M4A to MP3
echo "Converting M4A to MP3..."
ffmpeg -i "$INPUT_M4A" -codec:a libmp3lame -q:a 2 "$OUTPUT_MP3" -y

if [ $? -eq 0 ]; then
    echo "✅ MP3 created: $OUTPUT_MP3"
else
    echo "❌ MP3 conversion failed"
    exit 1
fi

# Create video with static image, audio, and subtitles
if [ -f "$LOGO_IMAGE" ] && [ -f "$SUBTITLES" ]; then
    echo ""
    echo "Creating video with subtitles..."

    ffmpeg -loop 1 -i "$LOGO_IMAGE" \
           -i "$INPUT_M4A" \
           -vf "subtitles=$SUBTITLES:force_style='FontName=Arial,FontSize=24,PrimaryColour=&HFFFFFF&,OutlineColour=&H000000&,BorderStyle=3,Outline=2,Shadow=1,Alignment=2,MarginV=40'" \
           -c:v libx264 -tune stillimage -c:a aac -b:a 192k \
           -pix_fmt yuv420p -shortest "$OUTPUT_VIDEO" -y

    if [ $? -eq 0 ]; then
        echo "✅ Video with subtitles created: $OUTPUT_VIDEO"
    else
        echo "❌ Video creation failed"
    fi
else
    echo "⚠️  Logo image or subtitles not found, skipping video creation"
fi

echo ""
echo "=== Conversion Complete ==="
echo ""
echo "Files created:"
echo "  • MP3 audio: $OUTPUT_MP3"
if [ -f "$OUTPUT_VIDEO" ]; then
    echo "  • MP4 video with subtitles: $OUTPUT_VIDEO"
fi
echo ""
echo "The subtitle file is available at: $SUBTITLES"
echo "You can use this with any video player that supports SRT subtitles."

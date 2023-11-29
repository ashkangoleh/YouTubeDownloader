# Author: Ashkan Golehpour
# Created: November 10, 2023
# Description: Download audio or video from either a single YouTube video or a YouTube playlist.

import argparse
from pytube import YouTube, Playlist
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
import os

parser = argparse.ArgumentParser(
    description="Download audio or video from either a single YouTube video or a YouTube playlist.")
parser.add_argument(
    "--video_url", help="URL of the YouTube video to download")
parser.add_argument(
    "--playlist_url", help="URL of the YouTube playlist to download (use either --video_url or --playlist_url)")
parser.add_argument("--output_folder", default="output",
                    help="Destination folder for files")
parser.add_argument("--download_video", action="store_true",
                    help="Download the full video (default is audio only)")

args = parser.parse_args()

if not args.video_url and not args.playlist_url:
    parser.error("Please provide either --video_url or --playlist_url.")

if args.video_url and args.playlist_url:
    parser.error("Please provide either --video_url or --playlist_url, not both.")

if args.video_url:
    video = YouTube(args.video_url)
    os.makedirs(args.output_folder, exist_ok=True)

    try:
        if args.download_video:
            video.streams.get_highest_resolution().download(output_path=args.output_folder)
        else:
            video.streams.filter(only_audio=True).first().download(
                output_path=args.output_folder)
    except Exception as e:
        print(f"An error occurred while downloading {video.title}: {str(e)}")

    if not args.download_video:
        for filename in os.listdir(args.output_folder):
            if filename.endswith(".webm"):
                video_path = os.path.join(args.output_folder, filename)
                mp3_filename = filename.replace(".webm", ".mp3")
                mp3_path = os.path.join(args.output_folder, mp3_filename)
                ffmpeg_extract_audio(video_path, mp3_path)
                os.remove(video_path)

    print("Download completed successfully.")

elif args.playlist_url:
    playlist = Playlist(args.playlist_url)
    os.makedirs(args.output_folder, exist_ok=True)

    for video in playlist.videos:
        try:
            if args.download_video:
                video.streams.get_highest_resolution().download(output_path=args.output_folder)
            else:
                video.streams.filter(only_audio=True).first().download(
                    output_path=args.output_folder)
        except Exception as e:
            print(f"An error occurred while downloading {video.title}: {str(e)}")

    if not args.download_video:
        for filename in os.listdir(args.output_folder):
            if filename.endswith(".webm"):
                video_path = os.path.join(args.output_folder, filename)
                mp3_filename = filename.replace(".webm", ".mp3")
                mp3_path = os.path.join(args.output_folder, mp3_filename)
                ffmpeg_extract_audio(video_path, mp3_path)
                os.remove(video_path)

    print("Download completed successfully.")

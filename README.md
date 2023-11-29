# YouTube Video/Audio Downloader

**Description:** This executable allows you to download audio or video from either a single YouTube video or a YouTube playlist.

## Usage

You can use this executable to download content from either a single YouTube video or a YouTube playlist. Use one of the following commands:

### To download a single YouTube video:

```bash
youtube_downloader.exe --video_url VIDEO_URL --output_folder OUTPUT_FOLDER [--download_video]
```
1. --video_url VIDEO_URL: The URL of the YouTube video you want to download.
2. --output_folder OUTPUT_FOLDER: The destination folder where the downloaded files will be saved.
3. --download_video (optional): Use this flag to download the full video. If not specified, only the audio will be downloaded.

To download a YouTube playlist:

```bash
youtube_downloader.exe --playlist_url PLAYLIST_URL --output_folder OUTPUT_FOLDER [--download_video]
```
1. --playlist_url PLAYLIST_URL: The URL of the YouTube playlist you want to download.
2. --output_folder OUTPUT_FOLDER: The destination folder where the downloaded files will be saved.
3. --download_video (optional): Use this flag to download the full video. If not specified, only the audio will be downloaded.

> Note: Please use either --video_url or --playlist_url, but not both.

## Examples

To download a single video with audio:

```bash
youtube_downloader.exe --video_url "https://www.youtube.com/watch?v=YOUR_VIDEO_ID" --output_folder "output"
```

To download a single video with the full video:

```bash
youtube_downloader.exe --video_url "https://www.youtube.com/watch?v=YOUR_VIDEO_ID" --output_folder "output" --download_video
```

To download a playlist with audio:

```bash
youtube_downloader.exe --playlist_url "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID" --output_folder "output"
```

To download a playlist with the full video:

```bash
youtube_downloader.exe --playlist_url "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID" --output_folder "output" --download_video
```

Replace "VIDEO_URL", "PLAYLIST_URL", "YOUR_VIDEO_ID", "YOUR_PLAYLIST_ID", and "youtube_downloader.exe" with the appropriate values and filenames.
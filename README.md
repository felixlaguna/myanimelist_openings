# myanimelist_openings
Download MP3 files of the openings of your watched animes. Uses themes.moe for getting the videos and extracts only the audio.

This is a simple program that is in no way perfect, just a quick way to get the mp3 files I want for listening in my car.

## Requirements

This program requires `bash`, `ffmpeg` as well as a Python 3.8 environment (only tested with that, but it uses the new syntax, so beware when using lower versions).
As for Python libraries, it requires `pycurl`, the rest should already be installed. The full list is `pycurl io re json pathlib glob os sys`.

## Usage

The usage is simple but feels really hacky, this was a 2 hours program. First run the Python code as follows

`./op.py <malUser> [destinationFolder]`

(The default destinationFolder is "Animes" in the current working directory)

Then, when it finishes, I recommend you run it a couple more times just to be sure. After that you will have all the videos downloaded, run

`./op.sh <destinationFolder>`

This will extract the audio track to the same folder and delete the videos afterwards. Then repeat these steps until no more videos are downloaded and
transcoded. If `ffmpeg` fails, chances are the video is not available, so your best bet is to download those separately and set the names correctly.

import os
import subprocess


def convert_audio_files(input_type="flac", output_type="mp3"):
    def flac_to_mp3(filename):
        dotIndex = filename.rfind(".")
        return filename[:dotIndex] + f".{output_type}"

    print("Input directory of flac files to convert:")
    directory = str(input())

    flac_files = []

    for file in os.listdir(directory):
        if file.endswith(f".{input_type}") or file.endswith(f".{input_type.capitalize}"):
            flac_files.append(file)
    if not flac_files:
        print("No flac files detected")
        # quit()
    flac_files = sorted(flac_files)

    for file in flac_files:
        input_file = f"{directory}/{file}"
        output_file = flac_to_mp3(f"{directory}_mp3/{file}")
        command = f"ffmpeg -i {input_file} -ab 320k -map_metadata 0 -id3v2_version 3 {output_file} -loglevel error"
        subprocess.call(command, shell=True)


if __name__ == "__main__":
    convert_audio_files()

import os
import ffmpy3


def convert_to_mp4(mkv_file):
    name, ext = os.path.splitext(mkv_file)
    out_name = name + ".mp4"
    ff = ffmpy3.FFmpeg(
        inputs={mkv_file: None},
        outputs={out_name: None}
    )
    ff.run()
    print("Finished converting {}".format(mkv_file))


if __name__ == '__main__':
    start_dir = '/Users/bytedance/video/世界上最神奇的24堂课'
    for path, folder, files in os.walk(start_dir):
        for file in files:
            if file.endswith('.mkv'):
                print("Found file: %s" % file)
                convert_to_mp4(os.path.join(start_dir, file))
            else:
                pass

import os
import sys

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

# 需要模块：sys
# 参数个数：len(sys.argv)
# 脚本名： sys.argv[0]
# 参数1： sys.argv[1]
# 参数2： sys.argv[2]

if __name__ == '__main__':
    start_dir = sys.argv[1]
    for path, folder, files in os.walk(start_dir):
        for file in files:
            if file.endswith('.mkv'):
                print("Found file: %s" % file)
                convert_to_mp4(os.path.join(start_dir, file))
            else:
                pass

import os
import re

# 请求用户输入视频文件路径和字幕文件路径
video_dir = input("请输入视频文件路径：")
subtitle_dir = input("请输入字幕文件路径：")
language = input('字幕语言\n(简体中文、Chinese_Simplified、eng&chs等，不要包含空格)：')

# 获取视频文件列表和字幕文件列表
video_files = os.listdir(video_dir)
subtitle_files = os.listdir(subtitle_dir)

# 遍历视频文件和字幕文件
for video_file in video_files:
    # print('遍历视频文件和字幕文件', video_file)
    # 找到mkv视频文件
    if video_file.endswith('.mkv'):   # 找到mkv视频文件
        # print('找到mkv视频文件', video_file)
        # 匹配视频文件名中的“S01E01”这种标注字段
        match = re.search(r's\d+e\d+', video_file, re.IGNORECASE)

        if match:
            # print('yes')
            # 获取视频文件的季数和集数
            season, episode = re.split(r'e', match.group(), flags=re.IGNORECASE)
            season = season[1:]
           #print(season, episode)
            # 遍历字幕文件
            for subtitle_file in subtitle_files:
                # 找到srt文件
                if subtitle_file.endswith('.srt'):
                    #print('# 找到srt文件', subtitle_file)
                    # 匹配字幕文件名中的“S01E01”这种标注字段
                    match = re.search(r'S\d+E\d+', subtitle_file, re.IGNORECASE)
                    if match:
                        a = match.group()
                        a = a.upper()
                        #print(match.group())
                        # 如果字幕文件和视频文件属于同一季和同一集，修改字幕文件名
                        if a == f"S{season}E{episode}":
                            subtitle_path = os.path.join(subtitle_dir, subtitle_file)
                            new_subtitle_file = f"{video_file.replace('.mkv', '')}.{language}.{subtitle_file.split('.')[-1]}"
                            #print(new_subtitle_file)
                            new_subtitle_path = os.path.join(subtitle_dir, new_subtitle_file)
                            os.rename(subtitle_path, new_subtitle_path)
                            print(f"{subtitle_path} -> {new_subtitle_path}")

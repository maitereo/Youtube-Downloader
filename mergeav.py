import subprocess
"""
example
filename = 'example title'
video_file = 'audio_' + title + '.webm'  # 无音频的webm视频文件
audio_file = 'video_' + title + '.webm'  # 含音频的webm文件
output_file = filename + '.mp4' # 输出的mp4文件
"""

def merge(video_file, audio_file, output_file):
    # 使用适当的编解码器进行重新编码
    command = [
        'ffmpeg',
        '-i', video_file,
        '-i', audio_file,
        '-c:v', 'libx264',  # 使用H.264视频编解码器
        '-c:a', 'aac',      # 使用AAC音频编解码器
        '-b:a', '192k',     # 设置音频比特率
        '-strict', 'experimental',  # 允许使用实验性的AAC编码
        '-movflags', 'faststart',   # 优化文件，使其适合网络播放
        output_file
    ]

    subprocess.run(command, check=True)
    print(f'Merged file saved as {output_file}')
